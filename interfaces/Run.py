class Run():

    def __init__(self):
        self.slot = None

    def set_command(self, command):
        self.slot = command

    def Option_choice(self):
        return self.slot.execute()
