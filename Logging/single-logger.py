import logging

# You can pass a name for your logger, otherwise root will be used. Passing __name__ will
# use the global name variable which makes it more meaningful when importing other libraries
logger = logging.getLogger(__name__)

# Clear existing handlers to avoid buildup if re-rerunning in same session
if logger.hasHandlers():
    logger.handlers.clear()

# Create a handler and format it
handler = logging.FileHandler('app.log') # output name
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') # see LogRecord attributes
handler.setFormatter(formatter)

# Set the min log level to be recorded, NOTE: defualt is WARNING
logger.setLevel(logging.DEBUG) # options in order are DEBUG, INFO, WARNING, ERROR, CRITICAL

# Add the handler to the logger
logger.addHandler(handler)

# # OPTIONAL: You can also add the log to console if you want by creating a StreamHandler
# # and repeating the steps above
# stream_handler = logging.StreamHandler()
# stream_handler.setLevel(logging.DEBUG)
# logger.addHandler(stream_handler)

# Write the logs to file
logger.debug('Debugging details')
logger.info('App started successfully')
logger.warning('API response delayed')
logger.error('Database connection failed')
logger.critical('System is shutting down!')