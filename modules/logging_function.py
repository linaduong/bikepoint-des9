import logging
import os

def logging_setup(log_dir:str, timestamp: str):
    os.makedirs(log_dir, exist_ok=True)
    log_filename = f'{log_dir}/{timestamp}.log'

    #don't have to write on separate lines, but makes it easier to read
    logging.basicConfig(
        filename = log_filename,
        #don't question the format - time - severity of the message - the actual message
        format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        #ignore anything that's below INFO
        level = logging.INFO
    )

    logger = logging.getLogger()
    #logger.info can be found across all print statements, to log the outcome into the historic log
    logger.info('logger was successfully initialised')