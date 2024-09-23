from psycopg2 import sql
from query_helper import execute_query

# Function to display all routes
def display_routes(connection):
    query = sql.SQL("SELECT * FROM routes")
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        print("\nRoutes:")
        for row in rows:
            print(row)

# Function to add a route
def add_route(connection):
    route_name = input("Enter route name: ")
    query = sql.SQL("INSERT INTO routes (route_name) VALUES (%s)")
    data = (route_name,)
    execute_query(connection, query, data)

# Function to update a route
def update_route(connection):
    route_id = input("Enter the route ID to update: ")
    new_route_name = input("Enter the new route name: ")
    query = sql.SQL("UPDATE routes SET route_name = %s WHERE route_id = %s")
    data = (new_route_name, route_id)
    execute_query(connection, query, data)

# Function to delete a route
def delete_route(connection):
    route_id = input("Enter the route ID to delete: ")
    query = sql.SQL("DELETE FROM routes WHERE route_id = %s")
    data = (route_id,)
    execute_query(connection, query, data)
