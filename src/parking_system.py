from sys import argv
from models import Parking_lot

class Parking_manager():

    def _read_commands(self, input_file_name: str) -> list:
        '''
        Reads the commands from input file 

        Returns list of commands 
        '''    
        with open(input_file_name, 'r') as commands_file:
            commands = commands_file.readlines()
        # Remove emtpy lines from commands
        commands = [command for command in commands if not command.isspace()]
        return commands


    def _create_parking_lot(self, slots: int) -> Parking_lot:
        '''
        Takes slots as input
        Returns the Parking lot of given slots
        '''
        slots = int(slots)
        parking_lot = Parking_lot(slots)
        print(f"Created parking of {slots} slots.")
        return parking_lot


    def manage(self, input_file_name):
        '''
        Main function that manages the whole parking lot.

        This little guy here is the one calling the shots.
        '''
        commands = self._read_commands(input_file_name)
        first_command = commands[0].strip().split()

        # Check if first command is to create parking lot
        if first_command[0] != "Create_parking_lot":
            print('NO parking lot exists ! ') 
            print("Please provide first command as 'Create_parking_lot [size]'")
            exit(0)
        else:
            slot = first_command[1]
            parking_lot = self._create_parking_lot(slot)
        
        for command in commands[1:]:
            '''
            Iterate through commands 
            '''
            command_components = command.strip().split()
            action = command_components[0]
            if action == "Park":
                _, vehicle_reg_num, _,  driver_age = command_components
                driver_age = int(driver_age)
                try:
                    slot = parking_lot.park(vehicle_reg_num, driver_age)
                    print(f'Car with vehicle registration number "{slot.vehicle_reg_num}" has been parked at slot number {slot.slot_number}')
                except IndexError as e:
                    print(f'{e}')
            elif action == "Slot_numbers_for_driver_of_age":
                driver_age = int(command_components[-1])
                slot_numbers = parking_lot.query_get_slot_number_with_driver_age(driver_age)
                print(",".join(map(str, slot_numbers)))
            elif action == "Slot_number_for_car_with_number":
                vehicle_reg_num = command_components[-1]
                slot_number = parking_lot.query_get_slot_number_with_vehicle_reg_number(vehicle_reg_num)
                print(f'Car with vehicle registration number "{vehicle_reg_num}" has been parked at slot number {slot_number}')
            elif action == "Leave":
                slot_number = int(command_components[-1])
                slot = parking_lot.leave(slot_number)
                print(f'Slot number {slot.slot_number} vacated, the car with vehicle registration number "{slot.vehicle_reg_num}" left the space, the driver of the car was of age {slot.driver_age}')
            elif action == "Vehicle_registration_number_for_driver_of_age":
                driver_age = int(command_components[-1])
                vehicle_reg_nums = parking_lot.query_get_vehicle_reg_num_with_driver_age(driver_age)
                print(",".join(vehicle_reg_nums))


if __name__ == "__main__":
    input_file_name = argv[1]
    parking_manager = Parking_manager()
    parking_manager.manage(input_file_name)