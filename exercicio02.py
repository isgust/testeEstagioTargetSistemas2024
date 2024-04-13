def fibonacci(n): #Definição da Função Fibonacci
    fib = [0, 1]  #Lista com os dois primeiros numeros 
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    if n in fib:
        return True
    else:
        return False

numero = int(input("Informe um número: "))
if fibonacci(numero): #Passando o valor de entrada para o parametro da função e verificando se a confição é TRUE ou FALSE
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
