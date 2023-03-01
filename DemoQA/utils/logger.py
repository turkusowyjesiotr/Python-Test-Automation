import logging


class Logger:
    @staticmethod
    def logger(log_level=logging.INFO):
        logger = logging.getLogger(__name__)
        logger.setLevel(log_level)
        file_handler = logging.FileHandler('logs/report.log', mode='w')
        formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger
