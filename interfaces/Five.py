from interfaces.Command import Command

class Service_Fee(Command):

    def __init__(self, interface):
        self.interface = interface

    def execute(self):
        return self.interface.option_five()