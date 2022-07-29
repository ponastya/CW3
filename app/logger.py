import logging

from app.paths import PATH_LOGGING

STRING_FORMAT = '%(asctime)s [%(levelname)s] %(message)s'
logging.basicConfig(
    format=STRING_FORMAT,
    level=logging.INFO,
    filename=PATH_LOGGING
)

logger = logging.getLogger(__name__)
