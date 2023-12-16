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
- AI-powered weather predictions.
- Integration with various weather APIs for accurate information.

## How to Run

### Running the Django Application Locally

1. Ensure you have Python 3.8 installed on your machine. You can download it from [here](https://www.python.org/downloads/).

2. Clone the Github repository using:

    '''sh
    git clone https://github.com/nathan-perrier23/IA1-Weather-App-Django
    '''

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

1. Ensure you have Docker installed on your machine. You can download it from [here](https://www.docker.com/products/docker-desktop).

2. Clone the Github repository using:

    '''sh
    git clone https://github.com/nathan-perrier23/IA1-Weather-App-Django
    '''

3. Build the Docker image:

    ```sh
    docker build -t weather_app -f DockerFile .
    ```

4. Run the Docker container:

    ```sh
    docker run -p 8000:8000 weather-app
    ```

5. Open your web browser and visit `http://localhost:8000/`.

## Resources and References

This Project utilised various projects and resources, that can be seen in the [REFERENCES](REFERENCES.md) file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.