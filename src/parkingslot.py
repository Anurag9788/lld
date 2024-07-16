from model.vehicle import Vehicle
from model.parkingslottype import Parkingslottype
class Parkingslot:
    def __init__(self,name,parkingslottype:Parkingslottype,is_available:bool=True):
        self._name = name
        self._is_available = is_available
        self._parkingslottype = parkingslottype
    
    @property
    def name(self):
        return self._name
    @property
    def is_available(self):
        return self._is_available
    @property
    def vehicle(self):
        return self._vehicle
    @property
    def parkingslottype(self):
        return self._parkingslottype

    def addvehicle(self,vehicle:Vehicle):
        self._vehicle = vehicle
        self._is_available = False
    def removevehicle(self,vehicle:Vehicle=None):
        self._vehicle = None
        self._is_available = True
    
