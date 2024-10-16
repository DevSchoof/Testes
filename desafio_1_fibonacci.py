def is_fibonacci(num):
    fib1, fib2 = 0, 1
    if num == fib1 or num == fib2:
        return f"{num} pertence à sequência de Fibonacci."
    
    while fib2 < num:
        fib1, fib2 = fib2, fib1 + fib2
       
    if fib2 == num:
        return f"{num} pertence à sequência de Fibonacci"
    else:
        return f"{num} não pertence à sequência de Fibonacci"

        
numero = int(input("Digite um número: "))
resultado = is_fibonacci(numero)
if resultado:
    print(resultado)
