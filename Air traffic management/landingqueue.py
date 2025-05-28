#extract the data
lines = []
file = open("Aviation project\\Flightmasterdata.txt", "r")
lines = file.readlines()
flight_number = str(input("Enter your flight number: "))
for i in range(5):
    individual_data = str(lines[i-1]).split(",")
    if flight_number == individual_data[0]:
        print("plane found")
        print(individual_data)
#Brief pilot of current traffic        
        if i-1 <= 1:
            print(f"You are number {i} to land")
            print("No plane ahead")
        elif i-1 > 1:
            print(f"You are number {i} to land")
            individual_data = str(lines[i-2]).split(",")
            print(f"Plane Ahead: {individual_data[:2]}")