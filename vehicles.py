from psycopg2 import sql
from query_helper import execute_query

# Function to display all vehicles
def display_vehicles(connection):
    query = sql.SQL("SELECT * FROM vehicles")
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        print("\nVehicles:")
        for row in rows:
            print(row)

# Function to add a vehicle
def add_vehicle(connection):
    vehicle_name = input("Enter vehicle name: ")
    vehicle_type = input("Enter vehicle type (e.g., Bus, Van, Truck): ")
    query = sql.SQL("INSERT INTO vehicles (vehicle_name, vehicle_type) VALUES (%s, %s)")
    data = (vehicle_name, vehicle_type)
    execute_query(connection, query, data)

# Function to update a vehicle
def update_vehicle(connection):
    vehicle_id = input("Enter the vehicle ID to update: ")
    new_vehicle_name = input("Enter the new vehicle name: ")
    new_vehicle_type = input("Enter the new vehicle type: ")
    query = sql.SQL("UPDATE vehicles SET vehicle_name = %s, vehicle_type = %s WHERE vehicle_id = %s")
    data = (new_vehicle_name, new_vehicle_type, vehicle_id)
    execute_query(connection, query, data)

# Function to delete a vehicle
def delete_vehicle(connection):
    vehicle_id = input("Enter the vehicle ID to delete: ")
    query = sql.SQL("DELETE FROM vehicles WHERE vehicle_id = %s")
    data = (vehicle_id,)
    execute_query(connection, query, data)
