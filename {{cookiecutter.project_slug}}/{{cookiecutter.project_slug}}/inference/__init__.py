from .base import IModel, BaseModelConfig, ModelManager
import importlib
import pkgutil

def iter_namespace(ns_pkg):
    # Specifying the second argument (prefix) to iter_modules makes the
    # returned name an absolute name instead of a relative one. This allows
    # import_module to work without having to do additional modification to
    # the name.
    return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + ".")


def load(model_configs: dict[str, BaseModelConfig]):
    import {{cookiecutter.project_slug}}.inference.models
    discovered_plugins = {
        name: importlib.import_module(name)
        for finder, name, ispkg
        in iter_namespace({{cookiecutter.project_slug}}.inference.models)
    }
    print(discovered_plugins)

    model_manager = ModelManager(model_configs)
    return model_manager