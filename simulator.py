from rooms.space import Space
from switches.switch import Switch
class Simulator(Space, Switch):
    def __init__(self, room_name, switch_name):
        Space.__init__(self, room_name)
        Switch.__init__(self, switch_name)

    def run_simulation(self):
        print(f"Starting simulation in {self.name}...")
        for device in self.devices:
            if isinstance(device, Switch):
                if device.state:
                    print(f"{device.name} is ON.")
                else:   
                    print(f"{device.name} is OFF.")
