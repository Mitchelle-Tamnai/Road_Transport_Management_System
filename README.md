# Transport Management System #

## Overview
The Transport Management System is a simple Python-based console application designed to manage routes, vehicles, and transport data in a PostgreSQL database. It allows users to perform CRUD (Create, Read, Update, Delete) operations on routes, vehicles, and transport records through a command-line interface.

## Features
- Add, display, update, and delete routes.

- Add, display, update, and delete vehicles.

- Add, display, update, and delete transport data (combining routes and vehicles).

- View all transport records with route and vehicle information.

## Prerequisites

Python 3.x

PostgreSQL

psycopg2 library (pip install psycopg2)

Ensure PostgreSQL is installed and running, and a database named transport_management is created.

## Setup
1. Clone the repository or download the source code.

2. Install dependencies:
    pip install psycopg2

3. Update the database credentials in the connect_to_database() function in main.py:

        connection = psycopg2.connect(
            dbname='transport_management', 
            user='your_postgres_username',
            password='your_postgres_password',
            host='localhost',
            port='5432'
        )

4. Create the necessary database tables in PostgreSQL:

        CREATE TABLE routes (
            route_id SERIAL PRIMARY KEY,
            route_name VARCHAR(255) NOT NULL
        );

        CREATE TABLE vehicles (
            vehicle_id SERIAL PRIMARY KEY,
            vehicle_name VARCHAR(255) NOT NULL,
            vehicle_type VARCHAR(50) NOT NULL
        );

        CREATE TABLE transport_data (
            data_id SERIAL PRIMARY KEY,
            route_id INT REFERENCES routes(route_id),
            vehicle_id INT REFERENCES vehicles(vehicle_id),
            departure_time TIMESTAMP NOT NULL,
            arrival_time TIMESTAMP NOT NULL
        );

## Running the Application

Run the application using Python:
        python main.py

The menu will guide you through various operations such as adding or viewing routes, vehicles, and transport data.

## License
This project is open-source and free to use under the MIT License.