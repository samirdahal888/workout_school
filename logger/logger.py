import logging
from logtail import LogtailHandler
import os
from dotenv import load_dotenv
load_dotenv()
SOURCE_TOKEN = os.getenv("SOURCE_TOKEN")
INGESTING_HOST = os.getenv("INGESTING_HOST")

def get_logger(logger_name: str,log_level) -> logging.Logger:
    """Use this function to get a logger in different modules."""
    # Create a logger with the specified name.
    # Tip: Use __name__ as the logger name in each module.
    logger = logging.getLogger(logger_name)

    # Configure logging level
    logger.setLevel(log_level)

    # Create a stream handler to log message to console.
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(log_level)
    #formate
    format = logging.Formatter('%(asctime)s -%(name)s: %(levelname)s - %(message)s')
    stream_handler.setFormatter(format)
    logger.addHandler(stream_handler)
    #send logs to Betterstack
    Betterstack_handler = LogtailHandler(
        source_token=SOURCE_TOKEN,
        host=F"https://{INGESTING_HOST}"

    )
    Betterstack_handler.setFormatter(format)
    
    logger.addHandler(Betterstack_handler)
    logger.propagate = False
    return logger