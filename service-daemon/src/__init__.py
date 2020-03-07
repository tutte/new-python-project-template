## Main program
from .configuration import config
import logging
import sys

log = logging.getLogger(config.name)
log_handler = logging.StreamHandler(sys.stdout)
log.addHandler(log_handler)
log.setLevel(config.log_level)

def main():
    log.info(config.name)
    return 0
