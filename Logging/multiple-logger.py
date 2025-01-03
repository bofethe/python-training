import logging

# You can pass a name for your logger, otherwise root will be used. Passing __name__ will
# use the global name variable which makes it more meaningful when importing other libraries
logger = logging.getLogger(__name__)

# Clear existing handlers to avoid buildup if re-rerunning in same session
if logger.hasHandlers():
    logger.handlers.clear()

# Create multiple handlers, and add individual min log level per handler
general_handler = logging.FileHandler('general.log') # output name
general_handler.setLevel(logging.DEBUG) # all error levels

error_handler = logging.FileHandler('error.log') # output name
error_handler.setLevel(logging.ERROR) # error and above

# Format the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') # see LogRecord attributes
general_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)

# Set the min log level to be recorded, NOTE: defualt is WARNING
logger.setLevel(logging.DEBUG) # options in order are DEBUG, INFO, WARNING, ERROR, CRITICAL

# Add both handlers to the logger
logger.addHandler(general_handler)
logger.addHandler(error_handler)

# Write the logs to file
logger.debug('Debugging details')
logger.info('App started successfully')
logger.warning('API response delayed')
logger.error('Database connection failed')
logger.critical('System is shutting down!')