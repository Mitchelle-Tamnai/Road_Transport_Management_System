import psycopg2

# Function to connect to PostgreSQL database
def connect_to_database():
    try:
        connection = psycopg2.connect(
            dbname='transport_management',  # Database name
            user='postgres',                # Username
            password='teerex001',           # Password
            host='localhost',               # Database host
            port='5432'                     # Port number
        )
        print("Database connection successful.")
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None
