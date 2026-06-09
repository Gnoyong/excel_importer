"""excel_importer — Excel 到数据库的导入工具库。

日志说明
---------
本库使用 loguru 进行日志记录，不会自动配置日志输出。
调用方需自行决定日志输出方式和级别。

快速启用调试日志（仅供开发调试）::

    from excel_importer import enable_debug_logging
    enable_debug_logging()
"""

import logging

from loguru import logger

from .cleaners import Cleaners
from .importer import ExcelImporter, SkipRowError, ExcelImporterConfig

# ------------------------------------------------------------------ #
#  NullHandler 保护：避免用户未配置日志时出现 WARNING                #
# ------------------------------------------------------------------ #
logging.getLogger("excel_importer").addHandler(logging.NullHandler())

# 模块级 logger，供内部子模块使用
logger = logger  # noqa: F811  — loguru 的全局 logger 实例


__all__ = [
    "Cleaners",
    "ExcelImporter",
    "SkipRowError",
    "ExcelImporterConfig",
    "enable_debug_logging",
]


# ------------------------------------------------------------------ #
#  可选日志配置接口（必须由使用者显式调用）                          #
# ------------------------------------------------------------------ #
def enable_debug_logging() -> None:
    """启用调试级别日志输出到控制台。

    仅供开发调试使用，生产环境请自行配置 loguru sink。
    必须由使用者显式调用，本库不会自动执行。
    """
    import sys

    logger.add(sys.stderr, level="DEBUG")

