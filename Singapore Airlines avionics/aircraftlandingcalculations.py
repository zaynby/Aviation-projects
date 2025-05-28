#pull data from master data
file = open("Aviation project\\Flightmasterdata.txt", "r")
lines = file.readlines()
# changi runway condition 
runway_distance = 4000
lda = 0.6 * runway_distance
runway_condition = 'dry'
#gather information of the aicraft
flight_number = str(input("Enter your flight number: "))
for i in range(5):
    individual_data = str(lines[i]).split(",")
    if flight_number == individual_data[0]:
        print("plane found")
        print(individual_data)
#calculate the landing distance and whether it is safe to land    
        if runway_condition == 'dry':
            rld = int(individual_data[3]) * 1.67
            if rld > float(lda):
                print("The plane cannot land")
            elif rld < float(lda):
                print("Able to land")
        elif runway_condition == 'wet':
            rld = int(individual_data[3]) * 1.92
            if rld > float(lda):
                print("The plane cannot land")
            elif rld < float(lda):
                print("Able to land")
#predict the exit the plane exits
        else:
            print("Runway conditions are not certain")
            break
    else:
        print("FLight number not found please try again")