from create_type_worker.Create_type import Create_Type
from syndicate import Syndicate
from utils import find_worker

class Employee:

    def __init__(self, name, address, type_of_payment, syndicate, Id, syndicate_id_prev=0, syndicate_fee_Prev=0, syndicate_total_fee_prev=0):
        self.name = name
        self.address = address
        self.type_of_payment = type_of_payment
        if syndicate:
            try:
                self.syndicate = Syndicate(syndicate_id_prev, syndicate_fee_Prev, syndicate_total_fee_prev)
            except:
                self.syndicate = Syndicate()
        else:
            self.syndicate = "Funcionário não faz parte de nenehum sindicato."
        self.Id = Id

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address

    @property
    def type_of_payment(self):
        return self._type_of_payment

    @property
    def Id(self):
        return self._Id

    @name.setter
    def name(self, value):
        self._name = value

    @address.setter
    def address(self, value):
        self._address = value

    @type_of_payment.setter
    def type_of_payment(self, value):
        self._type_of_payment = value

    @Id.setter
    def Id(self, value):
        self._Id = value

    def add_employee(employees, list):     
        name = input("Digite o nome do funcionário: ")
        address = input("Digite o endereço do funcionário: ")
        type_of_worker = int(input("Escolha o tipo do funcionário: \n[1] Hora\n[2] Mensal\n[3] Comissão\n"))
        type_of_payment = input("Digite o método de pagamento de sua preferência: ")
        syndicate = input("O funcionário faz parte de sindicatos? [sim] [nao]\n")
        if syndicate.lower() == "sim":
            syndicate = True
        else:
            syndicate = False
        system_Function = list[type_of_worker]
        run = Create_Type()
        run.set_command(system_Function)
        employees.append(run.create(name, address,type_of_payment, syndicate))

        return employees

    def remove_employee(employees):
        removed = int(input("Digite o Id ou nome do funcionário que deseja remover: "))
        to_remove = find_worker(removed, employees)

        if to_remove == None:
            print("Esse funcionário não existe")
        else:
            print(f"O funcionário {to_remove.name} com Id = {to_remove.Id} foi removido.\n")
            employees.remove(to_remove)
        
        return employees

    def edit_info(self):
        while True:
            info = input("Qual informação deseja alterar: ")
            if info.lower() == "nome":
                self.name = input("Digite o novo nome: ")
            elif info.lower() == "endereço" or info.lower() == "endereco":
                self.address = input("Digite o novo endereço: ")
            elif info.lower() == "metodo de pagamento" or info.lower() == "método de pagamento":
                self.type_of_payment = input("Digite o método de pagamento desejado: ")
            elif info.lower() == "sindicato":
                temp_syndicate = input("Digite se o funcionário vai fazer parte do sindicato. [sim] [nao} :")
                if temp_syndicate.lower() == "sim" and self.syndicate == "Funcionário não faz parte de nenehum sindicato.":
                    self.syndicate = Syndicate()
                elif temp_syndicate.lower() == "nao" and temp_syndicate.lower() != "Funcionário não faz parte de nenehum sindicato.":
                    self.syndicate.delete()
                    self.syndicate = "Funcionário não faz parte de nenehum sindicato."
            elif info.lower() == "identificação no sindicato" or info.lower() == "identificacao no sindicato":
                try:
                    self.syndicate.info_edit("id")
                except:
                    print("Funcionário não faz parte de nehum sindicato")
            elif info.lower() == "taxa do sindicato":
                try:
                    self.syndicate.info_edit("taxa do sindicato")
                except:
                    print("Funcionário não faz parte de nehum sindicato")
            elif info.lower() == "tipo":
                return 1
            if input("Deseja alterar mais algum dado? [sim] [nao]\n") == "nao":
                return 0

    def print_data(self):
        print("")
        print(f"O nome do empregrado é {self.name} \nMora no endereço {self.address} \nÉ do tipo {self.__class__.__name__} \nID = {self.Id}")
        print("")

    def delete(self):
        del self

