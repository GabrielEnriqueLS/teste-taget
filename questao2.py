numero = 13

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci_sequence = [fibonacci(i) for i in range(numero)]
encontrado = numero in fibonacci_sequence

if encontrado:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")



