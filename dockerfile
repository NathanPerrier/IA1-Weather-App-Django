# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app 

# Install dependencies
RUN apt-get update && apt-get install -y git
RUN git clone https://nathan-perrier23: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@github.com/nathan-perrier23/IA1-Weather-App-Django.git . 

COPY . /app/

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]