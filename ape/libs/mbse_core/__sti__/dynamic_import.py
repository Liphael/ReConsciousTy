from importlib import import_module


def import_attr(
    attribute_name: str,
    module_name: str | None,
    package: str | None,
) -> object:
    """懒加载基础支持函数，用于在协议规范__sti__模块内动态导入对象的属性。

    此功能可以通过协议模块内定义的 `__getattr__` 方法来调用，以便在需要时才导入相关功能，减少初始导入时间和循环依赖问题。

    参数args:
        attribute_name: 要导入的属性名称。
        module_name: 要导入的模块名称。

            如果为 `None`，则从包本身导入属性。
        package: 模块所在的包名称。

    异常raises:
        ImportError: 如果找不到模块。
        AttributeError: 如果属性在模块或包中不存在。

    返回returns:
        导入的属性对象。
    """
    if module_name == "__module__" or module_name is None:
        try:
            result = import_module(f".{attribute_name}", package=package)
        except ModuleNotFoundError:
            msg = f"module '{package!r}' has no attribute {attribute_name!r}"
            raise AttributeError(msg) from None
    else:
        try:
            module = import_module(f".{module_name}", package=package)
        except ModuleNotFoundError as err:
            msg = f"module '{package!r}.{module_name!r}' not found ({err})"
            raise ImportError(msg) from None
        result = getattr(module, attribute_name)
    return result
