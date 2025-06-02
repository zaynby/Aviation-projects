path = 'Air traffic management\\'
file = open(path + 'current traffic.txt', "a")
intended_landing_time = int(input("What is your intended landing time: "))
flight_number = input("What is your flight number? ")
traffic_info = f'{flight_number} | {intended_landing_time}'
