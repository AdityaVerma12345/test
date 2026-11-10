import json
import os
import heapq
from datetime import datetime

class RideRequest:
    no_of_riderequest = 0

    def __init__(self, name, destination, time_slot, year,ride_no=None, submitted_at=None):
        self.name = name
        self.destination = destination
        self.time_slot = time_slot
        self.year = year

        if ride_no is None:
            RideRequest.no_of_riderequest += 1
            self.ride_no = RideRequest.no_of_riderequest
        else:
            self.ride_no = ride_no
            RideRequest.no_of_riderequest = max(RideRequest.no_of_riderequest, ride_no)

        self.submitted_at = submitted_at or datetime.now().isoformat(timespec="seconds")


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
        destination = input("Enter Destination: ").strip().title()
        if destination not in ["Delhi", "Jaipur"]:
            print("Destination can only be 'Delhi' or 'Jaipur'")
        else:
            break

    while True:
        time = input("Enter Time slot: ").strip().title()
        if time not in ["Morning","Afternoon","Evening","Night"]:
            print('Invalid time slot, time slot can only be "Morning","Afternoon","Evening","Night" ')
        else:
            break

    while True:    
        try:
            year = int(input("Enter Year: "))
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
        best_cab = None
        max_passengers = -1
        for cab in cabs:
            if index == destinations.index(cab.destination)*4 + times.index(cab.time) and cab.has_left==False:
                c+=1
                available_seats = cab.seats - len(cab.passengers)
                passengers = min(len(arranged_requests[index]), available_seats)
                
                if passengers > max_passengers:
                    max_passengers = passengers
                    best_cab = cab
        if c == 0:
            print("No available cab for the designated destination and time")
            return

        cab = best_cab
            
        x = arranged_requests[index]
        print("Driver:",cab.name)
        if max_passengers == 0:
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

def student_to_dict(student):         # Used AI for this I'm so sorry I did'nt know persistance but know full well what this code means, but still thought I told you
    return {                          
        "name": student.name,
        "destination": student.destination,
        "time_slot": student.time_slot,
        "year": student.year,
        "ride_no": student.ride_no,
        "submitted_at": student.submitted_at
    }

def cab_to_dict(cab):
    return{
        "driver_name": cab.name,
        "seats": cab.seats,
        "destination": cab.destination,
        "time_slot": cab.time,
        "has_left": cab.has_left,
        "passengers": [student_to_dict(passenger) for passenger in cab.passengers]
    }

def save_data(requests, cabs, filename="save_data.json"):
    waiting_students = []
    cab_data = []

    for i in requests:
        waiting_students.append(student_to_dict(i))

    for i in cabs:
        cab_data.append(cab_to_dict(i))

    data = {"waiting_students": waiting_students,"cabs": cab_data,"last_ride_no": RideRequest.no_of_riderequest}

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def load_data(requests, cabs, arranged_requests, filename="save_data.json"):

    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        print("No previous data found. Starting a fresh session.")
        return
    
    with open(filename, "r") as f:
        data = json.load(f)
    for i in data["waiting_students"]:
        student = RideRequest(i["name"],i["destination"],i["time_slot"],i["year"],i["ride_no"],i["submitted_at"])
        requests.append(student)
    for i in data["cabs"]:
        cab = Cab(i["driver_name"],i["seats"],i["destination"],i["time_slot"])
        cab.has_left = i["has_left"]
        for j in i["passengers"]:
            passenger = RideRequest(j["name"], j["destination"], j["time_slot"],j["year"], j["ride_no"], j["submitted_at"])
            cab.passengers.append(passenger)
        cabs.append(cab)

    for i in requests:
        destinations = ["Delhi", "Jaipur"]
        times = ["Morning", "Afternoon", "Evening", "Night"]
        index = destinations.index(i.destination)*4 + times.index(i.time_slot)
        heapq.heappush(arranged_requests[index], (-i.year, i.ride_no, i))
    RideRequest.no_of_riderequest = data["last_ride_no"]


#####################################
cabs = []

requests = []

arranged_requests = [[],[],[],[],[],[],[],[]]
arranged_requests_time = ["Destination: Delhi, Time Slot: Morning","Destination: Delhi, Time Slot: Afternoon","Destination: Delhi, Time Slot: Evening","Destination: Delhi, Time Slot: Night","Destination: Jaipur, Time Slot: Morning","Destination: Jaipur, Time Slot: Afternoon","Destination: Jaipur, Time Slot: Evening","Destination: Jaipur, Time Slot: Night"]

if os.path.exists("save_data.json") and os.path.getsize("save_data.json") > 0:
    load_data(requests, cabs, arranged_requests)

else:
    print("No previous data found. Starting a fresh session.")

    with open("cabs.json", "r") as f:
        data = json.load(f)

    for i in data:
        cab = Cab(i["driver_name"], i["seats"], i["destination"], i["time_slot"])
        cabs.append(cab)

while True:
    print("=========== CAB POOL MATCHER ===========")
    print("Enter '1' to Add a ride request")
    print("Enter '2' to View waiting students")
    print("Enter '3' to View all cabs")
    print("Enter '4' to Find the matches")
    print("Enter '5' to Dispatch the cab")
    print("Enter '6' to Save and Quit")
    print("Enter '7' to Quit without saving")
    while True:
        try:
            x = int(input("Enter your choice: "))
            if 1<=x<=7:
                break
            print("Enter from 1 to 7")
        except ValueError:
            print("Please enter a no. ")
    if x == 1:
        add_request(requests,arranged_requests)
    elif x ==2:
        for i in range(8):
                    print(arranged_requests_time[i])
        
                    if not arranged_requests[i]:
                        print("No students waiting")
                    else:
                        temp = arranged_requests[i].copy()
        
                        while temp:
                            x = heapq.heappop(temp)[2]
                            print(f"Ride no. : {x.ride_no} Name: {x.name} Year: {x.year} Time: {x.submitted_at}")
        
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
    elif x==6:
        print("Saving data ...")
        save_data(requests, cabs)
        print("========== Thank you for visiting! ==========")
        print("========== Hope to see you again :) ==========")
        break
    else:
        print("========== Thank you for visiting! ==========")
        print("========== Hope to see you again :) ==========")
        break
# :)
