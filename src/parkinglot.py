from typing import List
from parkingfloor import ParkingFloor
from model.vehicle import Vehicle
from model.ticket import Ticket
from parkingslot import Parkingslot
import datetime


class ParkingLot:

    parkingLot = None

    def __init__(self, name: str, parkingfloors: List[ParkingFloor]) -> None:
        self.name = name
        self.parkingfloors = parkingfloors

    @staticmethod
    def getInstance(name: str, parkingfloors: List[ParkingFloor]):
        if not ParkingLot.parkingLot:
            ParkingLot.parkingLot = ParkingLot(name, parkingfloors)
        return ParkingLot.parkingLot

    def addFloors(self, name, parkSlots):
        parkfloor = ParkingFloor(name, parkSlots)
        self.parkingfloors.append(parkfloor)

    def removefloors(self, parkingFloor):
        self.parkingfloors.remove(parkingFloor)

    def assignTicket(self,vehicle:Vehicle ):
        parkingslot = self.get_parking_slot_for_vehicle_and_park(vehicle)
        if parkingslot is None:
            return None
        parking_ticket = self.create_ticket_for_slot(parkingslot,vehicle)
        return parking_ticket
    
    def create_ticket_for_slot(self,parkingslot:Parkingslot,vehicle:Vehicle):
        return Ticket(vehicle,parkingslot)
    
    def scan_and_pay(self,ticket:Ticket):
        endtime = datetime.datetime.now().timestamp()
        ticket.parkingslot.removevehicle(ticket.vehicle)
        duration =  endtime-ticket.start_time
        price = ticket.parkingslot.parkingslottype.getPriceForParking(duration)*10
        return price
    

    def  get_parking_slot_for_vehicle_and_park(self,vehicle:Vehicle) :
        parking_slot = None
        for floor in self.parkingfloors:
            parking_slot = floor.get_relevant_slot_for_vehicle_and_park(vehicle)
            if parking_slot is not None:
                break
        return parking_slot