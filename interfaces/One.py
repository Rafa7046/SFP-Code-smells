from interfaces.Command import Command

class Add_Employee(Command):

    def __init__(self, interface):
        self.interface = interface

    def execute(self, employees):
        return self.interface.option_one(employees) 