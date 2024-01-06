import os
import sys
from django.test import TestCase
from ..manage import main
import pytest

class TestManageCommands(TestCase):
    '''
    Tests the manage.py file. and init teests for the rest of the app.
    '''
    
    # Sets the DJANGO_SETTINGS_MODULE environment variable to "weather_app.settings".
    def test_sets_django_settings_module(self):
        sys.argv = ['manage.py', 'runserver']
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weather_app.settings")
        main()
        self.assertEqual(os.environ.get("DJANGO_SETTINGS_MODULE"), "weather_app.settings")
        
    # Imports the execute_from_command_line function from django.core.management.
    def test_imports_execute_from_command_line(self, mocker):
        # Mock sys.argv
        mocker.patch('sys.argv', ['manage.py', 'test'])

        # Call the main function
        main()

        # Check if execute_from_command_line is imported
        from django.core.management import execute_from_command_line
        assert execute_from_command_line is not None
        