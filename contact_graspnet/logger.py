import logging

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S')
logger = logging.getLogger('cgn')
logger.setLevel(logging.DEBUG)
