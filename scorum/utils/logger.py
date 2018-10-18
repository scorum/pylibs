"""
Source: https://stackoverflow.com/questions/17275334/what-is-a-correct-way-to-filter-different-loggers-using-python-logging
"""

import logging


LOG_LEVEL_MAP = {
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "error": logging.ERROR,
    "warning": logging.WARNING,
    "critical": logging.CRITICAL,
    "off": logging.NOTSET
}

DEFAULT_CONFIG = {
    'level': logging.INFO,
    'format': "%(asctime)s.%(msecs)03d (%(name)s) %(levelname)s - %(message)s",
    "datefmt": "%Y-%m-%d %H:%M:%S"
}


class Whitelist(logging.Filter):

    def __init__(self, *whitelist):
        super().__init__()
        self.whitelist = [logging.Filter(name) for name in whitelist]

    def filter(self, record):
        return any(f.filter(record) for f in self.whitelist)


class Blacklist(Whitelist):
    def filter(self, record):
        return not Whitelist.filter(self, record)


def setup_logger(level, format, datefmt, blacklist: list=None):

    logging.basicConfig(level=level, format=format, datefmt=datefmt)

    if blacklist:
        for handler in logging.root.handlers:
            for item in blacklist:
                handler.addFilter(Blacklist(item))


def get_logger(name):
    return logging.getLogger(name)


if __name__ == "__main__":
    setup_logger(**DEFAULT_CONFIG)
    log = get_logger("logger")
    log.info("Test message.")
