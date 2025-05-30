from logging import getLogger

from .module_a import A
from .module_b import B

logger = getLogger(__name__)


def run():
    print_logging_config()
    a = A()
    a.warn()
    a.info()
    b = B()
    b.warn()
    b.info()


def print_logging_config():
    rl = getLogger()
    print(rl, "handlers:", rl.handlers)
    print(logger, "handlers:", logger.handlers)
    for logger_name in "mylib.module_a", "mylib.module_b":
        ml = getLogger(logger_name)
        print(ml, "handlers:", ml.handlers)
    print()
