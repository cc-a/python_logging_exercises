import logging

from mylib import run


logging.basicConfig(level=logging.DEBUG)
module_a_logger = logging.getLogger("mylib.module_a")
module_a_logger.addHandler(logging.FileHandler("./test2.log"))

run()
