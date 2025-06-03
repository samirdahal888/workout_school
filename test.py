from logger.logger import get_logger
import logging
from logtail import LogtailHandler
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# format = logging.Formatter('%(asctime)s -%(name)s: %(levelname)s - %(message)s')
# SOURCE_TOKEN='23as3WGNbUkf8vxrbbjDmP2Q'
# INGESTING_HOST = "s1334161.eu-nbg-2.betterstackdata.com"
# Betterstack_handler = LogtailHandler(
#         source_token=SOURCE_TOKEN,
#         host=F"https://{INGESTING_HOST}"

#     )
# Betterstack_handler.setFormatter(format)

# logger.addHandler(Betterstack_handler)
# logger.propagate = False

# logger.info('hello')
logger = get_logger(__name__,logging.DEBUG)
logger.info('its justa wow')