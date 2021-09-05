from create_type_worker.Command import Command


class Create_Monthly(Command):

    def __init__(self, type):
        self.type = type

    def execute(self, name, address,type_of_payment, syndicate):
        return self.type.monthly(name, address,type_of_payment, syndicate)