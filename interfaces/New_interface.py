from create_type_worker.Create_comission import Create_Comission
from create_type_worker.Create_monthly import Create_Monthly
from create_type_worker.Type import Employee_Type
from create_type_worker.Create_hourly import Create_Hourly
from format import end_code, load_changes, save_object
from time_payments import avaliable_agendas, create_agenda, pay_employee
from employee import Employee
from utils import find_worker, generate_id
from payments import Comission, Hourly, Month


class Interface():
    
    def __init__(self, employees):
        self.employees = employees

    def __backup(self):
        save_object(self.employees, "data.pkl")
        self.employees = load_changes("data.pkl")
        return self.employees

    def option_zero(self):
        if len(self.employees) == 0:
            print("Não há nenhum funcionário")
        else:
            for x in self.employees:
                x.print_data()
                print("")
        
        return self.employees

    def option_one(self):
        self.employees = self.__backup()

        list = [0, Create_Hourly(Employee_Type()), Create_Monthly(Employee_Type()), Create_Comission(Employee_Type())]   

        return Employee.add_employee(self.employees, list)

    def option_two(self):
        self.employees = self.__backup()

        return Employee.remove_employee(self.employees)

    def option_three(self):
        self.employees = self.__backup()

        Id = int(input("Digite o Id do funcionário: "))
        worker = find_worker(Id, self.employees)
        worker.time_cards()
        print(f"Foi batido o ponto do funcionário {worker.name}")

        return self.employees

    def option_four(self):
        self.employees = self.__backup()

        Id = int(input("Digite o Id do funcionário: "))
        worker = find_worker(Id, self.employees)
        worker.sell_results()
        print(f"Foi adicionado o valor da comissão ao funcionário {worker.name} com Id = {Id}")

        return self.employees

    def option_five(self):
        self.employees = self.__backup()

        Id = int(input("Digite o Id do funcionário: "))
        worker = find_worker(Id, self.employees)
        worker.syndicate.service_fee()
        print(f"Foi adicionado o valor da taxa de serviço ao funcionário {worker.name} com Id = {Id}")

        return self.employees

    def option_six(self):
        self.employees = self.__backup()

        Id = int(input("Digite o Id do funcionário: "))
        worker = find_worker(Id, self.employees)
        while True:
            if worker.edit_info():
                new_type = input("Qual o novo tipo do funcionário: ")
                if new_type.lower() == "hourly" or new_type.lower() == "hour" or new_type.lower() == "hora":
                    try:
                        self.employees.append(Hourly(worker.name, worker.address,worker.type_of_payment, worker.syndicate, worker.Id, worker.per_hour))
                    except:
                        self.employees.append(Hourly(worker.name, worker.address,worker.type_of_payment, worker.syndicate, worker.Id))
                elif new_type.lower() == "month" or new_type.lower() == "monthly" or new_type.lower() == "mensal":
                    try:
                        self.employees.append(Month(worker.name, worker.address,worker.type_of_payment, worker.syndicate, worker.Id, worker.salary))
                    except:
                        self.employees.append(Month(worker.name, worker.address,worker.type_of_payment, worker.syndicate, worker.Id))
                elif new_type.lower() == "comission" or new_type.lower() == "comissao":
                    try:
                        self.employees.append(Comission(worker.name, worker.address, worker.type_of_payment, worker.syndicate, worker.Id, worker.salary, worker.comission_percent))
                    except:
                        try:
                            self.employees.append(Comission(worker.name, worker.address, worker.type_of_payment, worker.syndicate, worker.Id, worker.salary))
                        except:
                            self.employees.append(Comission(worker.name, worker.address, worker.type_of_payment, worker.syndicate, worker.Id))
                self.employees.remove(worker)
                if input("Deseja alterar mais algum dado? [sim] [nao]\n") == "nao":
                    break
            else:
                break
        worker.print_data()

        return self.employees

    def option_seven(self):
        self.employees = self.__backup()
        
        day, month, year = input("Qual o data para rodar a folhar? DD/MM/YYYY\n").split()
        pay_employee(self.employees, int(day), int(month), int(year))

        return self.employees

    def option_eight(self):
        Id = int(input("Digite o Id do funcionário: "))
        print("Estão disponíveis as seguintes agendas de pagamento: ")
        print("Digite o número respectivo a agenda desejada.")
        new_agenda = avaliable_agendas()
        find_worker(Id, self.employees).payment_agenda = new_agenda
        print(f"Foi alterado a agenda de pagamento do funcionário {Id} para {new_agenda}")

        return self.employees

    def option_nine(self):
        create_agenda()
        print("A nova agenda foi criada e já está disponível para ser escolhida")

        return self.employees

    def option_ten(self):
        undo_redo = input("[0] Desfazer\n[1] Refazer\n ")
        if undo_redo == "0":
            save_object(self.employees, "data_backup.pkl")
            try:
                self.employees = load_changes("data.pkl")
            except:
                self.employees = []
            save_object(self.employees, "data.pkl")
        elif undo_redo == "1":
            self.employees = load_changes("data_backup.pkl")

        return self.employees

    def option_minus_one(self):
        print("\n Sistema encerrado")
        end_code()
        exit()