import logging

import requests

from mylib import run

logging.basicConfig()
mylib_logger = logging.getLogger("mylib")
mylib_logger.setLevel(logging.DEBUG)

run()

requests.get("http://example.com")
