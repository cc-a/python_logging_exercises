import logging

import requests

from mylib import run

logging.basicConfig()
module_a_logger = logging.getLogger("mylib.module_a")
module_a_logger.setLevel(logging.DEBUG)

run()

requests.get("http://example.com")
