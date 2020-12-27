import logging

logging.basicConfig(filename="C://Downloadfiles//test.log",

                    level=logging.DEBUG
                   )

logging.debug("This is a debug msg")
logging.info("This is a info msg")
logging.warning("This is a warn msg")
logging.error("This is a error msg")
logging.critical("This is a critical msg")