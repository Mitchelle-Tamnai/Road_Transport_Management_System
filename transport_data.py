from psycopg2 import sql
from query_helper import execute_query

# Function to display all transport data
def display_transport_data(connection):
    query = sql.SQL("""
        SELECT td.data_id, r.route_name, v.vehicle_name, td.departure_time, td.arrival_time
        FROM transport_data td
        JOIN routes r ON td.route_id = r.route_id
        JOIN vehicles v ON td.vehicle_id = v.vehicle_id
    """)
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        print("\nTransport Data:")
        for row in rows:
            print(row)

# Function to add transport data
def add_transport_data(connection):
    route_id = input("Enter route ID: ")
    vehicle_id = input("Enter vehicle ID: ")
    departure_time = input("Enter departure time (YYYY-MM-DD HH:MM:SS): ")
    arrival_time = input("Enter arrival time (YYYY-MM-DD HH:MM:SS): ")
    
    query = sql.SQL("""
        INSERT INTO transport_data (route_id, vehicle_id, departure_time, arrival_time)
        VALUES (%s, %s, %s, %s)
    """)
    data = (route_id, vehicle_id, departure_time, arrival_time)
    execute_query(connection, query, data)

# Function to update transport data
def update_transport_data(connection):
    data_id = input("Enter the transport data ID to update: ")
    new_route_id = input("Enter the new route ID: ")
    new_vehicle_id = input("Enter the new vehicle ID: ")
    new_departure_time = input("Enter the new departure time (YYYY-MM-DD HH:MM:SS): ")
    new_arrival_time = input("Enter the new arrival time (YYYY-MM-DD HH:MM:SS): ")
    
    query = sql.SQL("""
        UPDATE transport_data
        SET route_id = %s, vehicle_id = %s, departure_time = %s, arrival_time = %s
        WHERE data_id = %s
    """)
    data = (new_route_id, new_vehicle_id, new_departure_time, new_arrival_time, data_id)
    execute_query(connection, query, data)

# Function to delete transport data
def delete_transport_data(connection):
    data_id = input("Enter the transport data ID to delete: ")
    query = sql.SQL("DELETE FROM transport_data WHERE data_id = %s")
    data = (data_id,)
    execute_query(connection, query, data)
