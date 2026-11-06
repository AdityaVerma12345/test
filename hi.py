import json


class RideRequest:
    no_of_riderequest=0
    def __init__(self, name, destination, time_slot, year):
        self.name = name
        self.destination = destination
        self.time_slot = time_slot
        self.year = year
        RideRequest.no_of_riderequest+=1
        self.ride_no = RideRequest.no_of_riderequest
        print(f"Ride no. is {self.ride_no}")


class Cab:
    def __init__(self, name, seats, destination, time_slot):
        self.name = name
        self.seats = seats
        self.destination = destination
        self.time = time_slot

        self.has_left = False
        self.passengers = []


def showcabs(cabs):
    for i in range(len(cabs)):
        print(f"{i+1}. Driver: {cabs[i].name}")
        print(f"   Destination : {cabs[i].destination}")
        print(f"   Time Slot : {cabs[i].time}")
        print(f"   Seats :{len(cabs[i].passengers)}/ {cabs[i].seats}")
        if cabs[i].has_left:
            print("   Status: Left")
        else:
            print("   Status: Open")

with open("cabs.json", "r") as f:
    data = json.load(f)

cabs = []

for i in data:
    cab = Cab(i['driver_name'], i['seats'], i['destination'], i['time_slot'])
    cabs.append(cab)

showcabs(cabs)


