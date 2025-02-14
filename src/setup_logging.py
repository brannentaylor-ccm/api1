#!/usr/bin/python3


"""set up logging - 

code from copilot"""

import logging
import os

def setup_logging(filename:str=''):
    # Ensure the log directory exists at the same level as src
    log_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'log'))
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Create a custom logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create handlers
    c_handler = logging.StreamHandler()

    if not filename:
        filename = os.path.join(log_directory, 'logging.log')
    else:
        filename = os.path.join(log_directory, filename)
    
    f_handler = logging.FileHandler(filename)
    c_handler.setLevel(logging.WARN)
    f_handler.setLevel(logging.DEBUG)

    # Create formatters and add them to the handlers
    c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger

def main():
    """Main is a runner function, used to call individual functions in order."""
    logger = setup_logging()
    logger.info(f'Main function - from setup_logging')


############### START HERE #####################
# if__name__ - will look into a hidden variable for the file, called 'dunder name', or 'double underscore name'.
# if this script is being run directly, as a script, and not just a container of functions, the
# if__name__ will run, to inspect the name of the script, which will be '__main__', and will evaluate to True.
# if __name__ is True, then go set some settings, and then go run the 'main()' function.
################################################
if __name__ == "__main__":
    main()