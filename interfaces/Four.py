from interfaces.Command import Command

class Sell_Result(Command):

    def __init__(self, interface):
        self.interface = interface

    def execute(self):
        return self.interface.option_four()