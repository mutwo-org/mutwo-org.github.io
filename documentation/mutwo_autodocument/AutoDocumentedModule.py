import functools
import types
import typing

from mutwo_autodocument import AutoDocumentedObject


SUBMODULE_NAME_TUPLE = ("abc", "configurations", "constants")


class AutoDocumentedModule(AutoDocumentedObject):
    def __init__(self, module_to_document: types.ModuleType, package_name: str):
        self.module_to_document = module_to_document
        self.package_name = package_name

    def get_submodule(self, submodule_name: str) -> typing.Optional[types.ModuleType]:
        return getattr(self.module_to_document, submodule_name, None)

    @functools.cached_property
    def module_name(self):
        return self.module_to_document.__name__

    @functools.cached_property
    def object_name_tuple(self) -> tuple[str, ...]:
        return getattr(self.module_to_document, "__all__", tuple([]))

    @functools.cached_property
    def object_tuple(self) -> tuple[typing.Type, ...]:
        return tuple(
            getattr(self.module_to_document, object_name)
            for object_name in self.object_name_tuple
        )

    @functools.cached_property
    def submodule_tuple(self) -> tuple[types.ModuleType, ...]:
        submodule_list = []
        for submodule_name in SUBMODULE_NAME_TUPLE:
            if submodule := self.get_submodule(submodule_name):
                submodule_list.append(submodule)
        return tuple(submodule_list)

    @functools.cached_property
    def object_documentation(self) -> str:
        function_documentation_list = []
        class_documentation_list = []
        for object_to_document in self.object_tuple:
            if hasattr(object_to_document, "__mro__"):
                class_documentation = rf"""
.. autoclass:: {self.module_name}.{object_to_document.__name__}

        .. autoclasstoc::
    """
                class_documentation_list.append(class_documentation)

            elif hasattr(object_to_document, "__call__"):
                function_documentation = rf"""

.. autofunction:: {object_to_document.__name__}
    """
                function_documentation_list.append(function_documentation)

            else:
                print(
                    "UNDOCUMENTED OBJECT:",
                    object_to_document,
                    "OF TYPE",
                    type(object_to_document),
                )

        return "\n".join(
            [
                "\n".join(documentation_list)
                for documentation_list in (
                    function_documentation_list,
                    class_documentation_list,
                )
            ]
        )

    @functools.cached_property
    def submodule_documentation(self) -> str:
        submodule_documentation_list = []
        for submodule in self.submodule_tuple:
            submodule_name = submodule.__name__
            member_to_document_list = ["members"]
            if submodule_name.split('_')[-1] == "version":
                member_to_document_list.extend(["special-members", "private-members"])
            member_to_document = "\n".join([f"   :{member}:" for member in member_to_document_list])
            submodule_documentation = rf"""
{submodule_name}
{self.get_underline(submodule_name, '-')}

.. automodule:: {submodule_name}
{member_to_document}
"""
            submodule_documentation_list.append(submodule_documentation)
        return "\n".join(submodule_documentation_list)

    @functools.cached_property
    def list_table(self) -> str:
        object_documentation_list = []
        for object_ in self.object_tuple:
            part_list = [f":class:`{self.module_name}.{object_.__name__}`"]
            if object_.__doc__:
                part_list.append(object_.__doc__.splitlines()[0])
            else:
                part_list.append("")
            object_documentation_part = [f'- {part}' for part in part_list]
            object_documentation_part[0] = "   * " + object_documentation_part[0]
            object_documentation_part[1] = "     " + object_documentation_part[1]
            object_documentation_list.extend(object_documentation_part)
        object_string = "\n".join(object_documentation_list)
        return f"""
.. list-table::
   :width: 95%
   :header-rows: 1

   * - Object
     - Documentation
{object_string}
"""

    @functools.cached_property
    def module_directive(self):
        return rf".. currentmodule:: {self.module_name}"

    @functools.cached_property
    def documentation(self) -> str:
        module_to_document = rf"""
{self.module_directive}

{self.module_name}
{self.get_underline(self.module_name, "=")}

.. contents:: Table of content
   :depth: 3

.. automodule:: {self.module_name}
   :members:

{self.list_table}

{self.object_documentation}

{self.submodule_documentation}
"""
        return module_to_document

    def export(self, path: str):
        with open(path, "w") as module_documentation_file:
            module_documentation_file.write(self.documentation)
