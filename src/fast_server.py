#!/usr/bin/python3


"""Containerizing a fast api application.
Watching youtube Neural9 video.
https://youtu.be/0TFWtfFY87U?t=791
Brannen Taylor - 20240217

"""
import os
import sys
import uvicorn

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from setup_logging import setup_logging
from fastapi import FastAPI

# Create app
app = FastAPI(debug=True)
# print("Current working directory:", os.getcwd())
# print("Python path:", sys.path)

@app.get("/")
def central_function():
    return {"Neural": "Nine"}

def main(logger):
    logger.info('entered main func')
    app = FastAPI()


if __name__ == "__main__":
    logger = setup_logging('logging.log')



    #start the uvicorn server
    try:

        logger.info('starting server')
        uvicorn.run(app, port=8000, host="0.0.0.0")

    except Exception as e:
        logger.error(f"Error starting server: {e}")

    main(logger)