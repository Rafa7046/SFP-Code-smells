from interfaces.Command import Command

class Punch_Clock(Command):

    def __init__(self, interface):
        self.interface = interface

    def execute(self, employees):
        return self.interface.option_three(employees)