
from parkingslot import Parkingslot
from model.parkingslottype import Parkingslottype
from parkingfloor import ParkingFloor
from parkinglot import ParkingLot
from model.vehicle import Vehicle
from model.vehiclecategory import Vehiclecategory
import time

def main():
    
    name_of_parking_lot ="Magarpatta Parking"
    all_slots = {}
    compact_slot = {}
    compact_slot["C1"] = Parkingslot("C1",Parkingslottype.compact)
    compact_slot["C2"] = Parkingslot("C2",Parkingslottype.compact)
    compact_slot["C3"] = Parkingslot("C3",Parkingslottype.compact)
    all_slots[Parkingslottype.compact]=compact_slot

 
    large_slot = {}
    large_slot["L1"] = Parkingslot("L1",Parkingslottype.large)
    large_slot["L2"] = Parkingslot("L2",Parkingslottype.large)
    large_slot["L3"] = Parkingslot("L3",Parkingslottype.large)
    all_slots[Parkingslottype.large]=large_slot
    parkingFloor =  ParkingFloor("1",all_slots);
    parkingFloors = []
    parkingFloors.append(parkingFloor)
    parkingLot = ParkingLot.getInstance(name_of_parking_lot,parkingFloors)

    vehicle =  Vehicle()
    vehicle.vehicle_category = Vehiclecategory.Hatchback
    vehicle.vehicle_number = "MH-40-X-9743"
    ticket = parkingLot.assignTicket(vehicle)
    time.sleep(3)
    price = parkingLot.scan_and_pay(ticket)
    print( price)
if __name__ == "__main__":
    main()
