#Aircraft weight limits
aircraft_data = [
    ["boeing 737", 85000, 41000],
    ["airbus A320", 78000, 42000],
    ["boeing 777", 351500, 168000],
    ["airbus A350", 280000, 140000],
    ["boeing 747", 447700, 183500]
] 
#Request for inputs
aircraft_model = str(input(("Enter aircraft model: ")))
no_of_passengers = int(input(("Enter the number of passengers: ")))
average_weight_pax = int(input("Enter the average weight per passenger (kg): "))
cargo_weight = int(input("Enter total cargo weight (kg): "))
#validate the plane type
if str(aircraft_data).find(aircraft_model.lower()) == True:
    total_passenger_weight = no_of_passengers * average_weight_pax
    total_takeoff_weight = total_passenger_weight + cargo_weight
    aircraft_index = aircraft_data.index(aircraft_model)
    print(aircraft_index)
else:
    print("The aircraft model you types is invalid")