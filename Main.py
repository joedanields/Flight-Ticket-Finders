import datetime
import json

try:
    # Load the flight data from the JSON file
    with open("flight_details.json") as flights_file:
        flights_data = json.load(flights_file)  # Correctly load JSON data
    
    # Function to find flights within a 1-hour range
    def find_flights_within_time_range(flights, query_time):
        query_time = datetime.datetime.strptime(query_time, "%H:%M")  # Parse input time
        result = []
        for flight in flights:
            flight_time = datetime.datetime.strptime(flight["time"], "%H:%M")  # Parse flight time
            time_difference = abs((flight_time - query_time).total_seconds()) / 3600  # Difference in hours
            if time_difference <= 1:  # Check if within 1 hour
                result.append(flight)
        return result
    
    # User input for time
    user_time = input("Enter the time (HH:MM): ")
    # Find matching flights
    matching_flights = find_flights_within_time_range(flights_data, user_time)
    
    # Display results
    if matching_flights:
        print("\nFlights within 1-hour range:")
        for flight in matching_flights:
            print(f"Flight No: {flight['flight_no']}, From: {flight['from']}, To: {flight['to']}, "
                  f"Price: {flight['price']}, Discount: {flight['discound']}%, Time: {flight['time']}")
    else:
        print("No flights found within 1-hour range.")
except Exception as e:
    print("Invalid input. Please enter a valid time in HH:MM format.", e)
