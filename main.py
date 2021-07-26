import Aleatorio as cAl
import Fibonacci as cFi

'''
funetes
https://www.udemy.com/course/python-programming-tutorial-for-the-absolute-beginner-code-included/learn/lecture/15989880#overview
https://www.youtube.com/watch?v=rC7D39VuNyo&t=73s
'''
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

'''
print("Despliega vía variable")
print(cFb.Fibonacci.varA)
print(cFb.Fibonacci.varB)
'''

print("...")
ar = cAl.Aleatorio()
#ar._Fibonacci__seta(123)
#print(f"Despliega vía encapsulado metodo get: {float(ar._Fibonacci__geta())}")


yy = range(10)
for n in yy:
    #ar.generaNumeroAleatorio(9,0,9)
    ar.generaNumeroAleatorio(5, 1, 56)

#ar.generaNumeroAleatorio(6,1,49)


print("...")
cb = cFi.Fibonacci()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
