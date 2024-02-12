from fastapi import FastAPI
from rooms.space import Space
from switches.switch import Switch
from simulator import Simulator

app = FastAPI()
living_room = None

@app.post("/room/add_device")
def add_device(room_name: str, device_name: str, device_type: str):
    global living_room
    if not living_room:
        living_room = Space(room_name)
    if device_type == "switch":
        switch = Switch(device_name)
        living_room.add_device(switch)
        return {"message": f"Switch {device_name} added to {room_name}."}
    else:
        return {"error": "Unsupported device type."}

@app.post("/switch/turn_on")
def turn_switch_on(switch_name: str):
    global living_room
    if living_room:
        for device in living_room.devices:
            if isinstance(device, Switch) and device.name == switch_name:
                device.turn_on()
                return {"message": f"{switch_name} turned ON."}
    return {"error": "Switch not found."}

@app.post("/switch/turn_off")
def turn_switch_off(switch_name: str):
    global living_room
    if living_room:
        for device in living_room.devices:
            if isinstance(device, Switch) and device.name == switch_name:
                device.turn_off()
                return {"message": f"{switch_name} turned OFF."}
    return {"error": "Switch not found."}

@app.post("/simulator/run")
def run_simulation():
    global living_room
    if living_room:
        simulator = Simulator(living_room.name, "Home Automation Simulator")
        simulator.devices = living_room.devices
        simulator.run_simulation()
        return {"message": "Simulation completed."}
    return {"error": "No room defined."}
