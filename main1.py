from rooms.space import Space
from switches.switch import Switch
from simulator import Simulator

# Example usage
if __name__ == "__main__":
    # Create a space (room)
    living_room = Space("Living Room")

    # Create switches
    light_switch = Switch("Living Room Light")
    fan_switch = Switch("Living Room Fan")

    # Add switches to the room
    living_room.add_device(light_switch)
    living_room.add_device(fan_switch)

    # Create a simulator for the living room
    living_room_simulator = Simulator("Living Room", "Living Room Simulator")
    
    # Add devices to the simulator
    living_room_simulator.add_device(light_switch)
    living_room_simulator.add_device(fan_switch)

    # Run simulation
    living_room_simulator.run_simulation()
