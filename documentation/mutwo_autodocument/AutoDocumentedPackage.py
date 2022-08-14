import functools
import importlib
import pkgutil
import types

from mutwo_autodocument import AutoDocumentedObject
from mutwo_autodocument import AutoDocumentedModule


class AutoDocumentedPackage(AutoDocumentedObject):
    def __init__(self, package_to_document: types.ModuleType):
        self.package_to_document = package_to_document

    @functools.cached_property
    def package_name(self):
        return self.package_to_document.__name__

    @functools.cached_property
    def module_tuple(self) -> tuple[types.ModuleType, ...]:
        module_list = []
        for module_info in pkgutil.iter_modules(self.package_to_document.__path__):
            module_name = module_info.name
            module = importlib.import_module(
                f"{self.package_to_document.__name__}.{module_name}"
            )
            module_list.append(module)
        return tuple(module_list)

    @functools.cached_property
    def auto_documented_module_tuple(self) -> tuple[AutoDocumentedModule, ...]:
        return tuple(
            AutoDocumentedModule(module_to_document, self.package_name)
            for module_to_document in self.module_tuple
        )

    @functools.cached_property
    def documentation(self) -> str:
        module_name_list = []
        for auto_documented_module in self.auto_documented_module_tuple:
            module_name_list.append(f"   {auto_documented_module.module_name}")

        module_name_string = "\n".join(module_name_list)

        title = f"{self.package_name} API documentation"

        documentation = fr"""
{title}
{self.get_underline(title)}

.. py:module:: {self.package_name}

Modules
-------

.. toctree::
   :maxdepth: 1

{module_name_string}
"""
        return documentation

    def export(self, path: str):
        with open(f"{path}/api_documentation.rst", "w") as toctree_file:
            toctree_file.write(self.documentation)

        auto_documented_module_path_list = []
        for auto_documented_module in self.auto_documented_module_tuple:
            auto_documented_module_path = (
                f"{path}/{auto_documented_module.module_name}.rst"
            )
            auto_documented_module.export(auto_documented_module_path)
            auto_documented_module_path_list.append(auto_documented_module_path)
