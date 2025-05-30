from logging import getLogger

logger = getLogger(__name__)


class A:
    def __init__(self):
        logger.debug("Initialising A")

    def info(self):
        logger.info("Info from A")

    def warn(self):
        logger.warn("Warning from A")
