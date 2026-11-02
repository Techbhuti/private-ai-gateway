# Use lightweight Python image
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements/code
COPY main.py .

# Install FastAPI and Uvicorn
RUN pip install --no-cache-dir fastapi uvicorn pydantic

# Expose the API port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
