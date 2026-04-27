"""
此为 mbse_core 包内协议规范（stipulation）模块的初始化文件；负责下述功能：

- 定义协议模块内的动态导入机制，以便在需要时才导入相关功能，减少初始导入时间和循环依赖问题。
- 定义协议模块内可用的属性列表，以便在使用 `dir()` 函数时正确显示可用的属性。
- 定义协议模块内的公共 API，包括警告类、装饰器函数和路径处理函数等，这些功能将通过动态导入机制提供给用户使用。
"""

from typing import TYPE_CHECKING

from mbse_core.__sti__.dynamic_import import import_attr

if TYPE_CHECKING:
    from langchain_core._api.beta_decorator import (
        MBSE_Warning,
        beta,
        suppress_langchain_beta_warning,
        surface_langchain_beta_warnings,
    )
    from langchain_core._api.deprecation import (
        LangChainDeprecationWarning,
        deprecated,
        suppress_langchain_deprecation_warning,
        surface_langchain_deprecation_warnings,
        warn_deprecated,
    )
    from langchain_core._api.path import as_import_path, get_relative_path

__all__ = (
    "MBSE_Warning",
    "LangChainDeprecationWarning",
    "as_import_path",
    "beta",
    "deprecated",
    "get_relative_path",
    "suppress_langchain_beta_warning",
    "suppress_langchain_deprecation_warning",
    "surface_langchain_beta_warnings",
    "surface_langchain_deprecation_warnings",
    "warn_deprecated",
)

_dynamic_imports = {
    "MBSE_Warning": "beta_decorator",
    "beta": "beta_decorator",
    "suppress_langchain_beta_warning": "beta_decorator",
    "surface_langchain_beta_warnings": "beta_decorator",
    "as_import_path": "path",
    "get_relative_path": "path",
    "LangChainDeprecationWarning": "deprecation",
    "deprecated": "deprecation",
    "surface_langchain_deprecation_warnings": "deprecation",
    "suppress_langchain_deprecation_warning": "deprecation",
    "warn_deprecated": "deprecation",
}


def __getattr__(attr_name: str) -> object:
    """Dynamically import and return an attribute from a submodule.

    This function enables lazy loading of API functions from submodules, reducing
    initial import time and circular dependency issues.

    Args:
        attr_name: Name of the attribute to import.

    Returns:
        The imported attribute object.

    Raises:
        AttributeError: If the attribute is not a valid dynamic import.
    """
    module_name = _dynamic_imports.get(attr_name)
    result = import_attr(attr_name, module_name, __spec__.parent)
    globals()[attr_name] = result
    return result


def __dir__() -> list[str]:
    """Return a list of available attributes for this module.

    Returns:
        List of attribute names that can be imported from this module.
    """
    return list(__all__)
