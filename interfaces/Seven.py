from interfaces.Command import Command

class Run_Payroll(Command):

    def __init__(self, interface):
        self.interface = interface

    def execute(self, employees):
        return self.interface.option_seven(employees)