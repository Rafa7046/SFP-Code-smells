from utils import generate_id
from payments import Comission, Hourly, Month


class Employee_Type():

    def __init__(self):
        pass

    def hourly(self, name, address, type_of_payment, syndicate):
       return Hourly(name, address,type_of_payment, syndicate, generate_id())

    def monthly(self, name, address, type_of_payment, syndicate):
        return Month(name, address,type_of_payment, syndicate, generate_id())

    def comission(self, name, address,type_of_payment, syndicate):
        return Comission(name, address,type_of_payment, syndicate, generate_id())