class Switch:
    def __init__(self, name, state=False):
        self.name = name
        self.state = state

    def turn_on(self):
        self.state = True
        print(f"{self.name} turned ON.")

    def turn_off(self):
        self.state = False
        print(f"{self.name} turned OFF.")
