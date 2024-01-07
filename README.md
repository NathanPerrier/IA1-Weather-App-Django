# Weather App

Created by Nathan Danial Perrier

16/12/2023

IA1 - Digital Solutions - Year 12

## Description

This is a weather application built with Django, inspired by the innovative design of Netflix. The application uses the Django framework and follows the MVC design pattern. It also includes user authentication features.

The application uses various APIs and AI technologies to provide users with accurate and up-to-date weather information. This allows users to make informed decisions based on the current and forecasted weather conditions.

The application's design is user-friendly and intuitive, making it easy for users to navigate and find the information they're looking for. The design is also responsive, ensuring a seamless experience on desktop, tablets, and mobile devices.

## Features

- View current weather information for various locations.
- User authentication.
- Responsive design that works on desktop, tablets, and mobile.
- API-powered weather predictions.
- Integration with various AI's for a better user experience.
- User-friendly and intuitive design inspired by Netflix.
- Routes and directions based on local weather.

## How to Run

### Running the Django Application Locally

1. Ensure you have Python 3.8 installed on your machine. You can download it from [here](https://www.python.org/downloads/).

2. Clone the Github repository using:

    `git clone https://github.com/nathan-perrier23/IA1-Weather-App-Django`

3. Set up environment variables for configuration. These are stored in a `.env` file at the root of the        
    project. You'll need to create this file and add the following parameters. REMEMBER to replace the values with your own and to change set and change the password for the redis server:

    ```properties
    CELERY_BROKER_URL = 'redis://:{password}@localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://:{password}@localhost:6379/0'
    REDIS_HOST = 'redis'
    REDIS_BACKEND = 'redis://192.168.68.55:6379'

    SECRET_KEY = 'your-secret-key'

    OPENAI_API_KEY = 'your-openai-api-key'
    TOMORROWIO_API_KEY = 'your-tomorrowio-api-key'
    GOOGLE_MAPS_API_KEY = 'your-google-maps-api-key'
    MAPBOX_ACCESS_TOKEN = 'your-mapbox-access-token'

    EMAIL_HOST_USER = 'your-gmail-email'
    EMAIL_HOST_PASSWORD = 'your-gmail-app-password'
   
    OPENWEATHERMAP_API_KEY = 'your-openweathermap-api-key'
    ```

    NOTE: To use a Gmail account to send emails, you must set up an app password - but to do this you first need to enable 2-Step Verification, then select ‘App passwords’ under ‘2-Step Verification’. You must also turn on the ‘Less Secure App Access’ option in your google account.

3. Install the required Python packages using pip:

    ```sh
    pip install -r requirements.txt
    ```

4. Navigate to the project directory and run the Django server:

    ```sh
    python manage.py runserver
    ```

5. Open your web browser and visit `http://127.0.0.1:8000/`.

### Running the Application Using Docker

1. Ensure you have Docker (and optionally Docker Desktop) installed on your machine. You can download it from [here](https://www.docker.com/products/docker-desktop). Make sure you start docker using `sudo service docker start`

2. Clone the Github repository using:

    `git clone https://github.com/nathan-perrier23/IA1-Weather-App-Django`

3. Set up environment variables for configuration. These are stored in a `.env` file at the root of the        
    project. You'll need to create this file and add the following parameters. REMEMBER to replace the values with your own and to change set and change the password for the redis server:

    ```properties
    CELERY_BROKER_URL = 'redis://:{password}@localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://:{password}@localhost:6379/0'
    REDIS_HOST = 'redis'
    REDIS_BACKEND = 'redis://192.168.68.55:6379'

    SECRET_KEY = 'your-secret-key'

    OPENAI_API_KEY = 'your-openai-api-key'
    TOMORROWIO_API_KEY = 'your-tomorrowio-api-key'
    MAPBOX_ACCESS_TOKEN = 'your-mapbox-access-token'

    EMAIL_HOST_USER = 'your-gmail-email'
    EMAIL_HOST_PASSWORD = 'your-gmail-app-password'
    
    OPENWEATHERMAP_API_KEY = 'your-openweathermap-api-key'
    ```

    NOTE: To use a Gmail account to send emails, you must set up an app password - but to do this you first need to enable 2-Step Verification, then select ‘App passwords’ under ‘2-Step Verification’. You must also turn on the ‘Less Secure App Access’ option in your google account.

4. Build the Docker image (ensure docker is running):

    ```sh
    docker build -t weather_app -f DockerFile .
    ```

5. Run the Docker container:

    For Deployment:

    ```sh
    docker run -p 8000:8000 weather_app
    ```

    or 

    For Development:

    ```sh 
    docker run -p 8000:8000 -v "$(pwd):/app" weather_app
    ```

6. Open your web browser and visit `http://localhost:8000/`.

7. When you make changes , you will need to rebuild the Docker images and restart the Docker containers. You 
    can do this with `docker-compose down` and then `docker-compose up --build`.

### NOTE

If you are using Docker Toolbox, you will need to visit the IP address of the Docker Machine instead of `localhost`. You can find the IP address by running `docker-machine ip` in the terminal.

if you are trying to migrate us `docker-compose run app python manage.py makemigrations` then `docker-compose run app python manage.py migrate`

 Use `docker system prune -a` to remove all unused containers, networks, images (both dangling and unreferenced), and optionally, volumes.

## Resources and References

This Project utilised various projects and resources, that can be seen in the [REFERENCES](REFERENCES.md) file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.