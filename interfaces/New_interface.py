from format import end_code, load_changes, save_object
from time_payments import avaliable_agendas, create_agenda, pay_employee
from employee import Employee
from utils import find_worker, generate_id
from payments import Comission, Hourly, Month


class Interface():
    
    def __init__(self):
        pass

    def option_zero(employees):
        if len(employees) == 0:
            print("Não há nenhum funcionário")
        else:
            for x in employees:
                x.print_data()
                print("")
        
        return employees

    def option_one(employees):
        save_object(employees, "data.pkl")
        employees = load_changes("data.pkl")
        name = input("Digite o nome do funcionário: ")
        address = input("Digite o endereço do funcionário: ")
        type_of_worker = input("Digite o tipo do funcionário: ")
        type_of_payment = input("Digite o método de pagamento de sua preferência: ")
        syndicate = input("O funcionário faz parte de sindicatos? [sim] [nao]\n")
        if syndicate.lower() == "sim":
            syndicate = True
        else:
            syndicate = False

        if type_of_worker.lower() == "hourly" or type_of_worker.lower() == "hour" or type_of_worker.lower() == "hora":
            employees.append(Hourly(name, address,type_of_payment, syndicate, generate_id()))
        elif type_of_worker.lower() == "month" or type_of_worker.lower() == "monthly" or type_of_worker.lower() == "mensal":
            employees.append(Month(name, address,type_of_payment, syndicate, generate_id()))
        elif type_of_worker.lower() == "comission" or type_of_worker.lower() == "comissao":
            employees.append(Comission(name, address,type_of_payment, syndicate, generate_id()))

        return employees

    def option_two(employees):
        save_object(employees, "data.pkl")
        employees = load_changes("data.pkl")
        removed = int(input("Digite o Id ou nome do funcionário que deseja remover: "))
        Employee.remove_employee(removed, employees)

        return employees

    def option_three(employees):
        save_object(employees, "data.pkl")
        employees = load_changes("data.pkl")
        Id = int(input("Digite o Id do funcionário: "))
        hours_worked = int(input("O funcionário trbalhou por quantas horas: "))
        find_worker(Id, employees).time_cards(hours_worked)
        print(f"Foi batido o ponto do funcionário {find_worker(Id, employees).name} com {hours_worked} de trabalho")

        return employees

    def option_four(employees):
        save_object(employees, "data.pkl")
        employees = load_changes("data.pkl")
        Id = int(input("Digite o Id do funcionário: "))
        value = int(input("Qual foi o valor da venda: "))
        find_worker(Id, employees).sell_results(value)
        print(f"Foi adicionado o valor da comissão ao funcionário {find_worker(Id, employees).name} com Id = {Id}")

        return employees

    def option_five(employees):
        save_object(employees, "data.pkl")
        employees = load_changes("data.pkl")
        Id = int(input("Digite o Id do funcionário: "))
        value = int(input("Qual foi o valor da taxa: "))
        find_worker(Id, employees).syndicate.service_fee(value)
        print(f"Foi adicionado o valor da taxa de serviço ao funcionário {find_worker(Id, employees).name} com Id = {Id}")

        return employees

    def option_six(employees):
        save_object(employees, "data.pkl")
        employees = load_changes("data.pkl")
        Id = int(input("Digite o Id do funcionário: "))
        worker = find_worker(Id, employees)
        while True:
            if worker.edit_info():
                new_type = input("Qual o novo tipo do funcionário: ")
                if new_type.lower() == "hourly" or new_type.lower() == "hour" or new_type.lower() == "hora":
                    try:
                        employees.append(Hourly(worker.name, worker.address,worker.type_of_payment, worker.syndicate, worker.Id, worker.per_hour))
                    except:
                        employees.append(Hourly(worker.name, worker.address,worker.type_of_payment, worker.syndicate, worker.Id))
                elif new_type.lower() == "month" or new_type.lower() == "monthly" or new_type.lower() == "mensal":
                    try:
                        employees.append(Month(worker.name, worker.address,worker.type_of_payment, worker.syndicate, worker.Id, worker.salary))
                    except:
                        employees.append(Month(worker.name, worker.address,worker.type_of_payment, worker.syndicate, worker.Id))
                elif new_type.lower() == "comission" or new_type.lower() == "comissao":
                    try:
                        employees.append(Comission(worker.name, worker.address, worker.type_of_payment, worker.syndicate, worker.Id, worker.salary, worker.comission_percent))
                    except:
                        try:
                            employees.append(Comission(worker.name, worker.address, worker.type_of_payment, worker.syndicate, worker.Id, worker.salary))
                        except:
                            employees.append(Comission(worker.name, worker.address, worker.type_of_payment, worker.syndicate, worker.Id))
                employees.remove(worker)
                if input("Deseja alterar mais algum dado? [sim] [nao]\n") == "nao":
                    break
        worker.print_data()

        return employees

    def option_seven(employees):
        save_object(employees, "data.pkl")
        employees = load_changes("data.pkl")
        day, month, year = input("Qual o data para rodar a folhar? DD/MM/YYYY\n").split()
        pay_employee(employees, int(day), int(month), int(year))

        return employees

    def option_eight(employees):
        Id = int(input("Digite o Id do funcionário: "))
        print("Estão disponíveis as seguintes agendas de pagamento: ")
        print("Digite o número respectivo a agenda desejada.")
        new_agenda = avaliable_agendas()
        find_worker(Id, employees).payment_agenda = new_agenda
        print(f"Foi alterado a agenda de pagamento do funcionário {Id} para {new_agenda}")

        return employees

    def option_nine(employees):
        create_agenda()
        print("A nova agenda foi criada e já está disponível para ser escolhida")

        return employees

    def option_ten(employees):
        undo_redo = input("[0] Desfazer\n[1] Refazer\n ")
        if undo_redo == "0":
            save_object(employees, "data_backup.pkl")
            try:
                employees = load_changes("data.pkl")
            except:
                employees = []
            save_object(employees, "data.pkl")
        elif undo_redo == "1":
            employees = load_changes("data_backup.pkl")

        return employees

    def option_minus_one(employees):
        print("\n Sistema encerrado")
        end_code()
        exit()