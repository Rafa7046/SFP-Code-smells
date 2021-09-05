from interfaces.Command import Command

class Remove_Employee(Command):

    def __init__(self, interface):
        self.interface = interface

    def execute(self):
        return self.interface.option_two()