from interfaces.Command import Command

class Undo_Redo(Command):

    def __init__(self, interface):
        self.interface = interface

    def execute(self, employees):
        return self.interface.option_ten(employees)