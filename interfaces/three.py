from interfaces.Command import Command

class Punch_Clock(Command):

    def __init__(self, interface):
        self.interface = interface

    def execute(self):
        return self.interface.option_three()