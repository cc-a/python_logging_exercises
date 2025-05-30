from logging import getLogger

logger = getLogger(__name__)


class B:
    def __init__(self):
        logger.debug("Initialising B")

    def info(self):
        logger.info("Info from B")

    def warn(self):
        logger.warn("Warning from B")
