from interfaces.Command import Command

class Finish(Command):

    def __init__(self, interface):
        self.interface = interface

    def execute(self):
        return self.interface.option_minus_one()