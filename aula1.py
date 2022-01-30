Velocidade_internet = 10
print(Velocidade_internet)
Nota_filme = 8.5 #float
#valores boleanos
esta_aberto = True
# Strngs
nome_do_curso = 'Lógica de Progração'

# Com variáveis seriam usadas em programa real?
# Problema 1 - valor por hora 
# Escreve um programa que retorna o valor de um funcionario com base no seu salário mensal e horas trabalhadas por mês.
'''
Eu cheguei atrasado na aula,ainda posso entrar?
Se essa não for sua terceira vez trasado,então pode sim, caso 
contrário irá tomar um suspenção.
'''
numero_de_atrasos = 2
if numero_de_atrasos >= 3:
      print('Você está supenso')
elif numero_de_atrasos == 1: 
        print('Pode entrar,porém caso toma mais  2 falta,irá ser supenso')
elif numero_de_atrasos == 2:
          print('Pode entrar,porém caso tome mais 1 falta,irá ser supenso')
else:
             print('Pode entrar')
