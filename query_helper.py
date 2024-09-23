# Function to execute a SQL query
def execute_query(connection, query, data=None):
    with connection.cursor() as cursor:
        try:
            cursor.execute(query, data)
            connection.commit()
            print("Query executed successfully.")
        except Exception as e:
            print(f"Error executing query: {e}")
