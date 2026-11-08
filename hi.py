import json
import heapq
from datetime import datetime

class RideRequest:
    no_of_riderequest=0
    def __init__(self, name, destination, time_slot, year):
        self.name = name
        self.destination = destination
        self.time_slot = time_slot
        self.year = year
        RideRequest.no_of_riderequest+=1
        self.ride_no = RideRequest.no_of_riderequest
        self.submitted_at = datetime.now()


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


def add_request(requests,arranged_requests):
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
    destinations = ["Delhi", "Jaipur"]
    times = ["Morning", "Afternoon", "Evening", "Night"]
    index = destinations.index(student.destination)*4 + times.index(student.time_slot)
    heapq.heappush(arranged_requests[index], (-1*student.year, student.ride_no, student))


def find_matches(cabs, arranged_requests):
    if not cabs:
        print("No cabs available")
        return
    for cab in cabs:
        if cab.has_left:
            continue
        destinations = ["Delhi", "Jaipur"]
        times = ["Morning", "Afternoon", "Evening", "Night"]
        index = destinations.index(cab.destination)*4 + times.index(cab.time)
        temp = arranged_requests[index].copy()
        count =0
        print("Driver:",cab.name)
        if not temp:
            print("No students waiting")
        while temp and count < cab.seats:
            x = heapq.heappop(temp)[2]
            count+=1        
            print(f"Passenger name = {x.name} and Ride no. = {x.ride_no}")

def dispatch (cabs, arranged_requests,d,t,requests):
        destinations = ["Delhi", "Jaipur"]
        times = ["Morning", "Afternoon", "Evening", "Night"]
        index = destinations.index(d)*4 + times.index(t)
        c = 0
        for cab in cabs:
            if index == destinations.index(cab.destination)*4 + times.index(cab.time) and cab.has_left==False:
                c+=1
                break
        if c == 0:
            print("No available cab for the designated destination and time")
            return
        
        x = arranged_requests[index]
        print("Driver:",cab.name)
        if not x:
            print("No students waiting")
            return
        
        while x and cab.seats>len(cab.passengers):
            y = heapq.heappop(x)[2]     
            cab.passengers.append(y)
            print(f"Name: {y.name}, Year: {y.year}, Ride no.: {y.ride_no}")
            requests.remove(y)

        cab.has_left = True
        print("Cab departed")
            

#####################################

cabs = []

requests = []

arranged_requests = [[],[],[],[],[],[],[],[]]
arranged_requests_time = ["Destination: Delhi, Time Slot: Morning","Destination: Delhi, Time Slot: Afternoon","Destination: Delhi, Time Slot: Evening","Destination: Delhi, Time Slot: Night","Destination: Jaipur, Time Slot: Morning","Destination: Jaipur, Time Slot: Afternoon","Destination: Jaipur, Time Slot: Evening","Destination: Jaipur, Time Slot: Night"]


with open("cabs.json", "r") as f:
    data = json.load(f)


for i in data:
    cab = Cab(i['driver_name'], i['seats'], i['destination'], i['time_slot'])
    cabs.append(cab)



while True:
    print("=========== CAB POOL MATCHER ===========")
    print("1. Add a ride request")
    print("2. View waiting students")
    print("3. View all cabs")
    print("4. Find the matches")
    print("5. Dispatch the cab")
    print("6. Quit")
    while True:
        try:
            x = int(input("Enter your choice: "))
            if 1<=x<=6:
                break
            print("Enter from 1 to 6")
        except ValueError:
            print("Please enter a no. ")
    if x == 1:
        add_request(requests,arranged_requests)
    elif x ==2:
        # showrequests(requests)
        for i in range(8):
                    print(arranged_requests_time[i])
        
                    if not arranged_requests[i]:
                        print("No students waiting")
                    else:
                        temp = arranged_requests[i].copy()
        
                        while temp:
                            x = heapq.heappop(temp)[2]
                            print(f"Ride no. : {x.ride_no} Name: {x.name} Year: {x.year}")
        
                    print("")
    elif x == 3:
        showcabs(cabs)
    elif x ==4:
        find_matches(cabs,arranged_requests)
    elif x ==5:
        while True:
            d = input("Enter the Destination ").strip().title()
            if d not in ["Delhi", "Jaipur"]:
                print("Destination can only be 'Delhi' or 'Jaipur'")
            else:
                break

        while True:
            t = input("Enter Time slot ").strip().title()
            if t not in ["Morning","Afternoon","Evening","Night"]:
                print('Invalid time slot, time slot can only be "Morning","Afternoon","Evening","Night" ')
            else:
                break

        dispatch(cabs, arranged_requests,d,t,requests)
        
    else:
        print("========== Thank you for visiting! ==========")
        print("========== Hope to see you again :) ==========")
        break
