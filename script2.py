import logging

from mylib import run

root_logger = logging.getLogger()
root_logger.addHandler(logging.FileHandler("./test.log"))

run()
