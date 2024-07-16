import datetime
from model.vehicle import Vehicle
from parkingslot import Parkingslot

class Ticket:
    def __init__(self,vehicle:Vehicle,parkingslot:Parkingslot):
        self.start_time = datetime.datetime.now().timestamp()
        self.vehicle = vehicle
        self.parkingslot = parkingslot
    