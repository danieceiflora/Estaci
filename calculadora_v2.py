saida = ''

def soma(num1, num2):
  return num1 + num2

def subtracao(num1, num2):
  return num1 - num2  

def multiplicacao(num1, num2):  
  return num1 * num2   

def divisao(num1, num2):  
  if num1 == 0 or num2 == 0:
    return('Não foi pssível realizar a divisão por 0')
  else:
    return num1 / num2

def calculadora(num1, num2, operacao):
  if operacao.lower() == 'soma' or operacao == '+':
    resultado = soma(num1, num2)
    return resultado
  elif operacao.lower() == 'subtracão' or operacao == '-':
    resultado = subtracao(num1, num2)
    return resultado
  elif operacao.lower() == 'multiplicação' or operacao == '*':
    resultado = multiplicacao(num1, num2)
    return resultado
  elif operacao.lower() == 'divisão' or operacao == '/':
    resultado = divisao(num1, num2)
    return resultado
  else:
    print('Operação inválida')
  
while saida != 's':
  try:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    operacao = input('Digite a operação: ')
  except:
    print('Digite apenas números')
    continue
  
  resultadooperacao = (calculadora(num1, num2, operacao)) 
  print(f'Resultado da operação {resultadooperacao}')
  saida = input('Digite S para sair e N para continuar: ')
  saida = saida.lower()