# Use an official Python runtime as a parent image
FROM python:3.9-slim
# Set the working directory in the container
WORKDIR /phonetics
# Copy the current directory contents into the container at /usr/src/app
COPY . .
# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Make port 5000 available to the world outside this container
EXPOSE 8080
# Define environment variable
# ENV FLASK_APP=app.py
# Run app.py when the container launches
# CMD ["python3", "-m", "flask", "--app", "phonetics" "run", "--host=0.0.0.0"]
CMD ["gunicorn", "phonetics:app", "--bind 0.0.0.0"]
# CMD ["python","-m","flask","--app", "phonetics", "run"]
# CMD ["gunicorn", "phonetics:app", "-bind=0.0.0.0:8080"]
