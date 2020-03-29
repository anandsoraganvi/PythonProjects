import logging
import time
path="C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/LogFiles/test.log"
logging.basicConfig(filename=path,format='%(asctime)s: %(levelname)s: %(message)s',datefmt= '%d/%m/%Y %I:%M:%S %p')

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.debug("This is Debug message")
logging.info("This is Info message")
logging.warning("This is Warning message")
logging.error("This is Error message")
logging.critical("This is Critical message")
