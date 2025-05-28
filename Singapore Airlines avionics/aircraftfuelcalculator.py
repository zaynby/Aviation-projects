#Displaying the available flights
file = open("Aviation project\\Flightmasterdata.txt", "r")
lines = file.readlines()
print(f"Available Flights: \n {lines[0]} \n {lines[1]} \n {lines[2]} \n {lines[3]} \n {lines[4]}")
#Requesting for input
flight_number = int(input("Enter flight number: "))
fuel_efficiency = float(input("Enter the fuel efficiency of the aircraft (liters per km): "))
max_fuel = int(input("Enter max fuel capacity: "))
#Extracting the distance in numerical form and finding weight of fuel needed
flight_info = lines[flight_number]
organizer = flight_info.split("|")
distance = organizer[2]
int_dist = distance[11:(len(distance)-3)].replace(",", '')
actual_max_fuel = float(int_dist) * fuel_efficiency
#displaying the output
print(organizer[0][3:])
print(distance)
print(f"Fuel Required: {actual_max_fuel}")
if actual_max_fuel > float(max_fuel):
    print("Warning: Fuel required exceeds max capacity!")
elif actual_max_fuel < float(max_fuel):
    print("Perfect: Fuel required does not exceed max capacity")
else:
    print("Fuel calculations cannot be fufiled please try again.")