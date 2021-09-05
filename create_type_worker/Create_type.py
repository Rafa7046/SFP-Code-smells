class Create_Type():
    
    def __init__(self):
        self.slot = None

    def set_command(self, command):
        self.slot = command

    def create(self, name, address,type_of_payment, syndicate):
        return self.slot.execute(name, address,type_of_payment, syndicate)