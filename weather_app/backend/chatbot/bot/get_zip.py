import sqlite3
from weather_app.settings import BASE_DIR
from .sql import SQL, SQL_INSERT

class PostcodeDatabase:
    """A class to interact with the postcodes_geo database."""

    def __init__(self, lat, lon):
        """Initialize the database connection and cursor."""
        
        self.db_name = 'australian_postcodes.db'
        self.sql_file = f'{BASE_DIR}/weather_app/backend/chatbot/bot/australian-postcodes.sql'
        self.sql_path = f'{BASE_DIR}/weather_app/backend/chatbot/bot/{self.db_name}'
        
        self.conn = sqlite3.connect(self.sql_path)
        self.cursor = self.conn.cursor()
        
        self.lat = lat
        self.lon = lon
        
        self.create_table()
        self.insert_data()

    def create_table(self):
        """Create the postcodes_geo table if it doesn't exist."""
        # with open(self.sql_file, 'r', encoding='utf-8') as f:
        #     sql = f.read()
        self.cursor.execute(SQL)
        self.conn.commit()

    def insert_data(self):
        """Insert data into the postcodes_geo table."""
        self.cursor.execute(SQL_INSERT)
        self.conn.commit()

    def get_postcode(self):
        try:
            """Get the postcode for a given latitude and longitude."""
            self.cursor.execute("""
                SELECT postcode FROM postcodes_geo WHERE latitude = ? AND longitude = ?
            """, (self.lat, self.lon))
            result = self.cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            print(e)
        finally:
            self.close()

    def close(self):
        """Close the database connection."""
        self.conn.close()