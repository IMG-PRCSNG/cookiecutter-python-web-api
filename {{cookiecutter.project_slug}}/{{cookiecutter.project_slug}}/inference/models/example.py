from {{cookiecutter.project_slug}}.inference import IModel
from pytriton.triton import Tensor

import numpy as np


class ExampleModel(IModel):

    @staticmethod
    def infer(**inputs):
        a, b = inputs.values()
        print(a.shape, b.shape)
        return {
            'output': a + b
        }

    @property
    def inputs(self) -> list[Tensor]:
        return [
            Tensor(dtype=np.float32, shape=(-1,)),
            Tensor(dtype=np.float32, shape=(-1,))
        ]

    @property
    def outputs(self) -> list[Tensor]:
        return [
            Tensor(name="output", dtype=np.float32, shape=(-1,))
        ]