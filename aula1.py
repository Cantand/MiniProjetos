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
input salario mensal 
input horas_trabalhadas_por_mes
valor_hora - salario_mensal / horas_trabalhadas_por_mes
print valor_hora
'''
salario_mensal  = input('Qual é seu saláriol mensal')
hora_trabalhaos_por_mes = input('Quantas horas trabalha por mês? ')
valor_hora = int(salario_mensal) / int ('horas_trabalhadas_por_mes')
print(valor_hora)