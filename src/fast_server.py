#!/usr/bin/python3

"""Containerizing a fast api application.
Watching youtube Neural9 video.
https://youtu.be/0TFWtfFY87U?t=791
Brannen Taylor - 20240217
"""

import os
import sys
import uvicorn
from fastapi import FastAPI

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from setup_logging import setup_logging

# Create app
app = FastAPI(debug=True)
logger = setup_logging('logging.log')

@app.get("/")
def central_function():
    logger.info('returning data')
    return {"Neural": "Nine"}

def main(logger):
    logger.info('entered main func')

    # Configure uvicorn to use the same logger
    uvicorn.run(app, host="0.0.0.0", port=8000, log_config=None, access_log=True)

if __name__ == "__main__":
    main(logger)