from interfaces.Minus_one import Finish
from interfaces.Ten import Undo_Redo
from interfaces.Nine import Create_Payment_Agenda
from interfaces.Eight import Change_Paymet_Agenda
from interfaces.Seven import Run_Payroll
from interfaces.Six import Change_Info
from interfaces.Five import Service_Fee
from interfaces.Four import Sell_Result
from interfaces.Zero import List_Employee
from interfaces.three import Punch_Clock
from interfaces.New_interface import Interface
from interfaces.two import Remove_Employee
from interfaces.One import Add_Employee
from interfaces.Run import Run

list = [List_Employee(Interface), Add_Employee(Interface), Remove_Employee(Interface), Punch_Clock(Interface), Sell_Result(Interface), Service_Fee(Interface), Change_Info(Interface), Run_Payroll(Interface), Change_Paymet_Agenda(Interface), Create_Payment_Agenda(Interface), Undo_Redo(Interface), Finish(Interface)]

def start(employees):
    print("Selecione a opção desjeada")
    print("[0] Ver informações dos funcionários")
    print("[1] Adicionar um funcionário")
    print("[2] Remover um funcionário")
    print("[3] Lançar um cartão de ponto")
    print("[4] Lançar um Resultado Venda")
    print("[5] Lançar uma taxa de serviço")
    print("[6] Alterar detalhes de um empregado")
    print("[7] Rodar a folha de pagamento")
    print("[8] Alterar agenda de pagamento")
    print("[9] Criar agenda de pagamento")
    print("[10] Desfazer ou refazer")
    print("[-1] Sair")
    option = int(input(""))
    if option == -1: option = 11
    system_Function = list[option]
    run = Run()
    run.set_command(system_Function)
    return run.Option_choice(employees)