import logging

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] [%(levelname)s] [%(module)s] - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def get_logger(name):
    return logging.getLogger(name)