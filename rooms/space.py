class Space:
    def __init__(self, name):
        self.name = name
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
