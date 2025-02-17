#!/usr/bin/python3


"""set up logging - 

code from copilot"""

import logging
import os

def setup_logging(filename:str='logging.log'):
    # Create a custom logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create handlers
    c_handler = logging.StreamHandler()

    # Adjust the path to save the log file one level up from the /src directory
    log_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    log_file_path = os.path.join(log_directory, filename)
    
    f_handler = logging.FileHandler(log_file_path)
    c_handler.setLevel(logging.WARN)
    f_handler.setLevel(logging.DEBUG)

    # Create formatters and add them to the handlers
    c_format = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s  - %(funcName)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s  - %(funcName)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger

def main():
    """Main is a runner function, used to call individual functions in order."""
    logger = setup_logging()
    logger.info(f'i am main func')


############### START HERE #####################
# if__name__ - will look into a hidden variable for the file, called 'dunder name', or 'double underscore name'.
# if this script is being run directly, as a script, and not just a container of functions, the
# if__name__ will run, to inspect the name of the script, which will be '__main__', and will evaluate to True.
# if __name__ is True, then go set some settings, and then go run the 'main()' function.
################################################
if __name__ == "__main__":
    main()