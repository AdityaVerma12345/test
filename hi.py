import json
import heapq

class RideRequest:
    no_of_riderequest=0
    def __init__(self, name, destination, time_slot, year):
        self.name = name
        self.destination = destination
        self.time_slot = time_slot
        self.year = year
        RideRequest.no_of_riderequest+=1
        self.ride_no = RideRequest.no_of_riderequest


class Cab:
    def __init__(self, name, seats, destination, time_slot):
        self.name = name
        self.seats = seats
        self.destination = destination
        self.time = time_slot

        self.has_left = False
        self.passengers = []


def showcabs(cabs):
    if len(cabs) == 0:
            print("No cabs available")
            return
    for i in range(len(cabs)):
        print(f"{i+1}. Driver: {cabs[i].name}")
        print(f"   Destination : {cabs[i].destination}")
        print(f"   Time Slot : {cabs[i].time}")
        print(f"   Seats :{len(cabs[i].passengers)}/ {cabs[i].seats}")
        if cabs[i].has_left:
            print("   Status: Left")
        else:
            print("   Status: Open")

def showrequests(requests):
    if len(requests) == 0:
        print("No waiting student")
        return
    
    for i in range(len(requests)):
        x = requests[i]
        print(f"{i+1}. {x.name}, {x.destination}, {x.time_slot}, year {x.year} ")


def add_request(requests):
    while True:    
        name = input("Name of the student: ").strip().title()
        if name:
            break
        print("Name cannot be empty")

    while True:
        destination = input("Destination? ").strip().title()
        if destination not in ["Delhi", "Jaipur"]:
            print("Destination can only be 'Delhi' or 'Jaipur'")
        else:
            break

    while True:
        time = input("Time_slot? ").strip().title()
        if time not in ["Morning","Afternoon","Evening","Night"]:
            print('Invalid time slot, time slot can only be "Morning","Afternoon","Evening","Night" ')
        else:
            break

    while True:    
        try:
            year = int(input("Year: "))
            if 1 <= year <= 5:
                break
            else:
                print("Year must be between 1 and 5")
        except ValueError:
            print("Please enter a number")

    student = RideRequest(name,destination,time,year)
    requests.append(student)
    print(f"Request submitted! Ride number: {student.ride_no}")

def arrange(requests,arranged_requests):
    destinations = ["Delhi", "Jaipur"]
    times = ["Morning", "Afternoon", "Evening", "Night"]
    for i in range(len(requests)):
        x = requests[i]
        index =  destinations.index(x.destination)*4 + times.index(x.time_slot)
        arranged_requests[index].append(requests[i])


cabs = []

requests = []

arranged_requests = [[],[],[],[],[],[],[],[]]
rearranged_requests = [[],[],[],[],[],[],[],[]]
arranged_requests_time = ["Destination: Delhi, Time Slot: Morning","Destination: Delhi, Time Slot: Afternoon","Destination: Delhi, Time Slot: Evening","Destination: Delhi, Time Slot: Night","Destination: Jaipur, Time Slot: Morning","Destination: Jaipur, Time Slot: Afternoon","Destination: Jaipur, Time Slot: Evening","Destination: Jaipur, Time Slot: Night"]


with open("cabs.json", "r") as f:
    data = json.load(f)


for i in data:
    cab = Cab(i['driver_name'], i['seats'], i['destination'], i['time_slot'])
    cabs.append(cab)


print("=========== CAB POOL MATCHER ===========")
print("1. Add a ride request")
print("2. View waiting students")
print("3. View all cabs")
print("4. Quit \n")


while True:
    while True:
        try:
            x = int(input("Enter your choice: "))
            if 1<=x<=4:
                break
            print("Enter from 1 to 4")
        except ValueError:
            print("Please enter a no. ")
    if x == 1:
        add_request(requests)
    elif x ==2:
        showrequests(requests)
    elif x == 3:
        showcabs(cabs)
    else:
        print("========== Thank you for visiting! ==========")
        print("========== Hope to see you again :) ==========")
        break

arrange(requests,arranged_requests)

for i in range(8):
    print(arranged_requests_time[i])

    if not arranged_requests[i]:
        print("No students waiting")
    else:
        for j in range(len(arranged_requests[i])):
            x = arranged_requests[i][j]
            print(f"Ride no. :- {x.ride_no} Name: {x.name} Year: {x.year}")

    print("")
