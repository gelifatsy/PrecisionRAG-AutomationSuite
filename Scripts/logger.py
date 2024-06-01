import logging
import os

def logger(log_directory="../logs"):
  """
  Configures logging with separate files for errors, warnings, infos, and console output.

  Args:
      log_directory (str, optional): The directory to store log files. Defaults to "../logs".
  """

  script_dir = os.path.dirname(os.path.abspath(__file__))
  logger = logging.getLogger(__name__)
  logger.setLevel(logging.DEBUG)

  formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s - %(message)s')

  handlers = [
      logging.FileHandler(os.path.join(script_dir, log_directory, "errors.log"), level=logging.ERROR, formatter=formatter),
      logging.FileHandler(os.path.join(script_dir, log_directory, "infos.log"), level=logging.INFO, formatter=formatter),
      logging.FileHandler(os.path.join(script_dir, log_directory, "warnings.log"), level=logging.WARNING, formatter=formatter),
      logging.StreamHandler(formatter=formatter),
  ]

  for handler in handlers:
    logger.addHandler(handler)

# Example usage
logger()

# Use the logger throughout your code
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
