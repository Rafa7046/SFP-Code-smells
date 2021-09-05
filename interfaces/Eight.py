from interfaces.Command import Command

class Change_Paymet_Agenda(Command):

    def __init__(self, interface):
        self.interface = interface

    def execute(self, employees):
        return self.interface.option_eight(employees)