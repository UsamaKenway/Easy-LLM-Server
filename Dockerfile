# Use the official Python image with version 3.10 as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the LLMApp code into the container
#COPY ./LLMAPP ./LLMAPP
COPY LLMApp /app/LLMApp

# Expose the port that UVicorn will listen on
EXPOSE 8080

CMD ["uvicorn", "LLMApp.main:app", "--host", "0.0.0.0", "--port", "8080"]