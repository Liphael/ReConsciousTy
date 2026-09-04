'''
此为 mbse_core 包的初始化根文件；负责下述功能：
- 为 mbse_core 包的入口标识
- 定义 mbse_core 包的版本号元数据
- 定义 mbse_core 包警告系统初始化行为
- 确保包根命名空间轻量化

待定：
是否需要加入依赖检测？
'''

# 定义包的版本号
from mbse_core.__sti__ import (
    surface_mbse_core_beta_warnings,
    surface_mbse_core_deprecation_warnings,
)

# 在包导入时调用警告函数，以便在使用过时或处于测试阶段的功能时向用户发出警告。
from mbse_core.version import VERSION

__version__ = VERSION

surface_mbse_core_deprecation_warnings()
surface_mbse_core_beta_warnings()
