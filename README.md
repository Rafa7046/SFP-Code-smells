# Sistema de Folha de Pagamento - Refactor

__**Descrição**__

  Segunda parte do projeto

__**Bibliotecas**__

  Foram utilizadas bibliotecas nativas do python sendo elas: os, random e calendar
  e também utilizada a biblioteca externa dill
  
  __**Smells**__
  
- [x] Chain constructors:

No arquivo payments, existem classes que com os construtores com trechos de códigos repetidos

- [x] Command:

No arquivo interface tinha uma sequencia de ifs que puderam ser resolvidos com o command

Para a criação de um funcionário na hora de selecionar o tipo não é mais necessário checar com ifs o tipo do funcionário

- [x] Extract method:

No arquivo New_interface tinhamos trechos de códigos em vários métodos
