class Slot(object):
    '''
    A Datamodel for Slot
    '''

    def __init__(self, vehicle_reg_num: str,
                     driver_age: int, slot_number: int):
        self.occupied = True
        self.driver_age = driver_age
        self.vehicle_reg_num = vehicle_reg_num
        self.slot_number = slot_number

    @property
    def occupied(self):
        return self._occupied

    @occupied.setter
    def occupied(self, is_occupied):
        self._occupied = is_occupied

    @property
    def driver_age(self):
        return self._driver_age

    @driver_age.setter
    def driver_age(self, age):
        self._driver_age = age 
    
    @property
    def vehicle_reg_num(self):
        return self._vehicle_reg_num
    
    @vehicle_reg_num.setter
    def vehicle_reg_num(self, reg_num):
        self._vehicle_reg_num = reg_num
    
    @property
    def slot_number(self):
        return self._slot_number

    @slot_number.setter
    def slot_number(self, slot):
        self._slot_number = slot


class Parking_lot(object):
    '''
    A Data model for Parking lot
    '''
    def __init__(self, total_slots:int):
        """
        Parking lot initializer
        """
        self.total_slots = total_slots
        self._parked_cars = dict()


    def _is_full(self):
        '''
        Utility function

        Returns True is Parking lot is full
        '''
        if len(self._parked_cars) == self.total_slots:
            return True
        return False


    def _get_available_slot_number(self):
        '''
        Utility function

        Returns the alloted slot
        '''
        if self._is_full():
            raise IndexError("Parking lot is full")
        utilized_slot = set(map(int, self._parked_cars.keys()))
        available_slots = set(range(1,self.total_slots+1)) - utilized_slot
        alloted_slot = min(available_slots)
        return alloted_slot


    def park(self, vehicle_reg_num: str, driver_age: int) -> Slot:
        '''
        Takes in vehicle registration number and
        driver's age

        Returns slot or raiseError
        '''
        slot_number = self._get_available_slot_number()
        slot = Slot(vehicle_reg_num, driver_age, slot_number)
        self._parked_cars[slot_number] = slot
        return slot
        

    def query_get_slot_number_with_driver_age(self, driver_age: int
                                ) -> list:
        '''
        Takes in driver age as input

        Returns list of slot numbers
        '''
        query_result = [
            slot.slot_number for slot in self._parked_cars.values() if slot.driver_age == driver_age]
        return query_result


    def query_get_slot_number_with_vehicle_reg_number(self, vehicle_reg_num: str
                                ) -> Slot.slot_number:
        '''
        Takes in vehicle registration number as input

        Return slot number or None
        '''
        query_result = [
            slot.slot_number if slot.vehicle_reg_num == vehicle_reg_num else None for slot in self._parked_cars.values()][0]
        return query_result


    def query_get_vehicle_reg_num_with_driver_age(self, driver_age: int
                                ) -> list:
        '''
        Takes in driver age as input

        Returns list of vehicle registration numbers
        '''
        query_result = [
            slot.vehicle_reg_num for slot in self._parked_cars.values() if slot.driver_age == driver_age]
        return query_result


    def leave(self, slot_number: int):
        '''
        Takes in slot number as input

        Returns slot
        '''
        slot = self._parked_cars.pop(slot_number)
        return slot
    