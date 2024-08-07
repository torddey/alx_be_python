import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Torddey@1993"
        )
        
        # Check if the connection was successful
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create the database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    create_database()
