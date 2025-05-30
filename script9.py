import logging

from mylib import run


logging.basicConfig(level=logging.DEBUG)
mylib_logger = logging.getLogger("mylib")
mylib_logger.setLevel(level=logging.WARNING)

run()
