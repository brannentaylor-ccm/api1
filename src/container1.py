#!/usr/bin/python3


"""Creates a file to put in a container - using modules that we don't have locally, but exist in the container.

watching 'containerize python applications with Docker - Neural 9
https://www.youtube.com/watch?v=0TFWtfFY87U&t=674s

This code creates a "server", listening for connections on port 9999, returning data to the caller.

"""

#imports
import sys
import os
# In summary, this line of code ensures that the parent directory of the current 
# script (api1) is included in the module search path. This allows you to import 
# modules from the parent directory, such as setup_logging from the src directory.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import socket
from sklearn.datasets import load_iris
import sys
import signal #look for control c to stop
import logging
from src import setup_logging

data = load_iris()

def server_start(listening_port:int=9999):
    # set up the server.
    # default listening_port is 9999
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', listening_port))
    server.listen()
    print(f"Server is listening...on {listening_port}")
    return server

def signal_handler(sig, frame, server):
    msg = f"\nCNTRL-C received. Shutting down the server..."
    print(msg)
    logger.warning(msg)

    try:
        server.close()
        sys.exit(0)

    except Exception as e:
        print(f"Error: {e}")
        logger.error(f"Error: {e}")
        sys.exit(1)

def main(logger):

    '''
    With this modification, when you press ctrl+c in the terminal where the server is running,
    the signal_handler function will be called, which will close the server and exit the program
    gracefully.
    '''
    logger.info('starting server')
    server = server_start()
    signal.signal(signal.SIGINT, lambda sig, frame: signal_handler(sig, frame, server))

    # in an endless loop, waiting for connections, return the data.
    while True:
        client, addr = server.accept()
        msg = f"Connection from {addr} has been established!"
        logger.info(msg)
        print(msg)
        msg = f"You are connected!\n".encode()
        logger.info(f'Sending {msg}')
        client.send(msg)
        client.send(f"{data['data'][:,0]}\n".encode())
        time.sleep(2)
        msg = f"You are being disconnected.\n".encode()
        client.send(msg)
        logger.info(f'Sent {msg}')
        logger.info(f'Closing connection to {addr}')
        client.close()


############### START HERE #####################
# if__name__ - will look into a hidden variable for the file, called 'dunder name', or 'double underscore name'.
# if this script is being run directly, as a script, and not just a container of functions, the
# if__name__ will run, to inspect the name of the script, which will be '__main__', and will evaluate to True.
# if __name__ is True, then go set some settings, and then go run the 'main()' function.
################################################
if __name__ == "__main__":
    logger = setup_logging.setup_logging('server.log')
    main(logger)