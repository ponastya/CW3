import logging

STRING_FORMAT = '%(asctime)s [%(levelname)s] %(message)s'
logging.basicConfig(
    format=STRING_FORMAT,
    level=logging.INFO,
    filename='logging_data.log'
)

logger = logging.getLogger(__name__)
