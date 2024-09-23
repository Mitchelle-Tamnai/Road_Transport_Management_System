from db_connection import connect_to_database
import routes
import vehicles
import transport_data

# Main function
def main():
    connection = connect_to_database()
    if connection:
        while True:
            print("\nTransport Management System")
            print("1. Add Route")
            print("2. Add Vehicle")
            print("3. Add Transport Data")
            print("4. Display Routes")
            print("5. Display Vehicles")
            print("6. Display Transport Data")
            print("7. Update Route")
            print("8. Update Vehicle")
            print("9. Update Transport Data")
            print("10. Delete Route")
            print("11. Delete Vehicle")
            print("12. Delete Transport Data")
            print("13. Exit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                routes.add_route(connection)
            elif choice == '2':
                vehicles.add_vehicle(connection)
            elif choice == '3':
                transport_data.add_transport_data(connection)
            elif choice == '4':
                routes.display_routes(connection)
            elif choice == '5':
                vehicles.display_vehicles(connection)
            elif choice == '6':
                transport_data.display_transport_data(connection)
            elif choice == '7':
                routes.update_route(connection)
            elif choice == '8':
                vehicles.update_vehicle(connection)
            elif choice == '9':
                transport_data.update_transport_data(connection)
            elif choice == '10':
                routes.delete_route(connection)
            elif choice == '11':
                vehicles.delete_vehicle(connection)
            elif choice == '12':
                transport_data.delete_transport_data(connection)
            elif choice == '13':
                print("Exiting...")
                connection.close()
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
