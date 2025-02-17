# docker file to containerize a python script.
# watching Neural9 video
# https://www.youtube.com/watch?v=0TFWtfFY87U&t=674s
FROM python:3.12.3

# set the working directory
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt /app/

# Copy the source files to the container
COPY  src/container1.py /app/
COPY  src/setup_logging.py /app/

# Install any necessary dependencies (if requr)
RUN pip install -r requirements.txt

# Command to run the script
CMD ["python", "container1.py"]
