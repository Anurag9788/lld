from model.vehicle import Vehicle
from parkingslot import Parkingslot
from model.parkingslottype import Parkingslottype
from model.vehiclecategory import Vehiclecategory


class ParkingFloor:
    def __init__(self, name, parkingSlots: dict) -> None:
        self.name = name
        self.parkingSlots = parkingSlots

    def get_relevant_slot_for_vehicle_and_park(self, vehicle: Vehicle) -> Parkingslot:
        vehicle_category = vehicle.vehicle_category
        parkingslottype = self.pick_correct_slot(vehicle_category)
        relevantparkingslot: dict = self.parkingSlots.get(parkingslottype)
        slot = None
        for key, value in relevantparkingslot.items():
            if value.is_available:
                slot = value
                slot.addvehicle(vehicle)
                break
        return slot

    def pick_correct_slot(self, vehiclecategory: Vehiclecategory):
        return (
            Parkingslottype.twowheeler
            if vehiclecategory == Vehiclecategory.TwoWheeler
            else (
                Parkingslottype.compact
                if vehiclecategory == Vehiclecategory.Hatchback
                or vehiclecategory == Vehiclecategory.Sedan
                else (
                    Parkingslottype.medium
                    if vehiclecategory == Vehiclecategory.SUV
                    else (
                        Parkingslottype.large
                        if vehiclecategory == Vehiclecategory.Bus
                        else None
                    )
                )
            )
        )
