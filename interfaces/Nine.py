from interfaces.Command import Command

class Create_Payment_Agenda(Command):

    def __init__(self, interface):
        self.interface = interface

    def execute(self):
        return self.interface.option_nine()