class Vehicle:
    def __init__(self,vehicle_number=None,vehicle_category=None):
        self._vehicle_numer= vehicle_number
        self._vehicle_category= vehicle_category
    @property
    def vehicle_number(self):
        return self._vehicle_numer
    @property
    def vehicle_category(self):
        return self._vehicle_category
    @vehicle_category.setter
    def vehicle_category(self,category):
        self._vehicle_category = category
    @vehicle_number.setter
    def vehicle_number(self,v_num):
        self._vehicle_numer = v_num