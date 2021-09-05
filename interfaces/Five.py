from interfaces.Command import Command

class Service_Fee(Command):

    def __init__(self, interface):
        self.interface = interface

    def execute(self, employees):
        return self.interface.option_five(employees)