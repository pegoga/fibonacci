class Fibonacci:
    def __init__(self):
        pass

    #callback
    def callbackFx(s):return s + 1
    def sumaValor(entrada,callback):
        salida = entrada
        return callback(salida)


    # callback
    def promedio(*args):
        return sum(args)/len(args)
    def estado(funcionPormedio):
        if (funcionPormedio >=6):
            print("Aprobado")
        else:
            print("Reprobado")

    #functions
    def function_1(x): return x ** 2
    def function_2(x): return x ** 3
    def function_3(x): return x ** 4

    def fibonacci_generator():
        a = b = 1
        while True:
            yield a
            a, b = b , a+b


    #do
    print("---Functions")
    callbacks=[function_1, function_2, function_3]
    for function in callbacks : print(f"Resultado: {function(2)}")

    print("---Lambda Functions")
    callbacks1 = [lambda x:x**0, lambda x:x**1, lambda x:x**5]
    for fx in callbacks1: print(f"Resultado: {fx(3)}")

    print("---Anonymous Functions / Callback")
    print(sumaValor(19,callbackFx))

    print("---Anonymous Functions / Callback")
    estado(promedio(9,8,9,5))
    estado(promedio(1.9, 1.8, 9, 5))

    print("---Fibonacci")
    fib = fibonacci_generator()
    for i in fib:
        if i>100:
            break
        else:
            print(f"Generated: {i}")


# https://pythonexamples.org/python-callback-function/
# https://www.youtube.com/watch?v=p_xjgC3rvvs