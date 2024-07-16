from enum import Enum
from util import bind

class Parkingslottype(Enum):
    twowheeler = 1
    compact = 2
    medium = 3
    large = 4
    @bind('twowheeler')
    def getPriceForParking(self,duration:float):
        return duration*0.05

    @bind('compact')
    def getPriceForParking(self,duration:float):
        return duration*0.075

    @bind('medium')
    def getPriceForParking(self,duration:float):
        return duration*0.09
    
    @bind('large')
    def getPriceForParking(self,duration:float):
        return duration*0.10
    