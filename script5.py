import logging

import requests

from mylib import run

logging.basicConfig(level=logging.DEBUG)

run()

requests.get("http://example.com")
