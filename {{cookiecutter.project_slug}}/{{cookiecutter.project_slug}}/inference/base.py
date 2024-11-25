
from abc import ABCMeta, abstractmethod
from multiprocessing import Process
from typing import Type, Dict, Tuple
from pytriton.triton import Triton, ModelConfig, Tensor
from pytriton.client import ModelClient
from pytriton.decorators import batch
from pydantic import BaseModel

class ModelRegistry:
    _registry: Dict[str, Type] = {}

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        if cls.__name__ != 'IModelPlugin':
            ModelRegistry._registry[cls.__name__] = cls

class BaseModelConfig(BaseModel):
    batching: bool = False
    max_batch_size: int = 1
    response_cache: bool = False
    pass

class IModel(ModelRegistry, metaclass=ABCMeta):
    def __init__(self, _triton: Triton, config: BaseModelConfig):
        super().__init__()
        self._name = self.__class__.__name__
        self._config = config
        _triton.bind(
            model_name=self._name,
            infer_func=batch(self.__class__.infer),
            inputs=self.inputs,
            outputs=self.outputs,
            config=ModelConfig(
                batching = self._config.batching,
                response_cache = self._config.response_cache,
                max_batch_size = self._config.max_batch_size,
            )
        )


    @property
    def config(self):
        return self._config

    @staticmethod
    @abstractmethod
    def infer(sample):
        raise NotImplementedError

    @property
    @abstractmethod
    def inputs(self) -> list[Tensor]:
        raise NotImplementedError

    @property
    @abstractmethod
    def outputs(self) -> list[Tensor]:
        raise NotImplementedError



class ModelManager:
    def __init__(self, model_configs: dict[str, BaseModelConfig]):
        self.models: dict[str, Tuple[IModel, ModelClient]] = {}
        self.model_configs = model_configs
        self._triton = None

    def _start(self):
        if self._triton is None:
            print('starting local triton')
            self._triton = Triton()
            self._triton.run()

    def get(self, name):
        if self._triton is None:
            self._start()

        if name not in self.models:
            if name not in ModelRegistry._registry:
                raise ValueError('Unknown model')

            model_config = self.model_configs.get(name, BaseModelConfig())
            cls = ModelRegistry._registry[name]
            model = cls(self._triton, model_config)
            client = ModelClient('http://localhost:8000', name)

            self.models[name] = (model, client)
        return ModelClient.from_existing_client(self.models[name][1])

    def remove(self, name):
        # Ignore unknown models
        if name not in self.models:
            return

        # If model is present, unload it
        model, client = self.models.pop(name)
        client.unload_model()
        client.close()
        del model


    def stop(self):
        for n in list(self.models.keys()):
            self.remove(n)

        if self._triton:
            self._triton.stop()

        print(self.models)
        self._triton = None