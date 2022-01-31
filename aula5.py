# EXEMPLO 5 - Fatorial de um número 
'''''
Crie um programa que um número e imprime o fatorial daquele  número  

# Método SQ,s montar um algorítimo:


Analíse criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voze peça mais informações/investigue mais até você compreender completamente o problema.)

1.Quais são os dados de entreda necessários?
Numero
2.O que devo fazer com este dados ?
Eu devo calcular o fatorial do número que for passado para o meu programa e o exiber na tela.
3.Quais são os as restrições deste problema?
 - O número deve ser um valor positivo
 - O número deve ser um valor inteiro
4.Qual é o resultado esperado ?
 - o resultado esperando é que o fatorial do número providenciado seja exibido.
5. Qual é o sequencía de passos a ser feitas para chegar ao resultado esperado?

'''
numero = int(input('Digite um numero'))
if numero > 0:
  fatorial = 1 
  for item in range (1,numero +1):
    fatorial = fatorial + item 
print (fatorial)
