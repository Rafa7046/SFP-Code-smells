from interfaces.Command import Command

class Change_Paymet_Agenda(Command):

    def __init__(self, interface):
        self.interface = interface

    def execute(self):
        return self.interface.option_eight()