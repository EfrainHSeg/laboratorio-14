#1.    Elabore un módulo que almacene tres funciones:
#a.    Que retorne verdadero si el número ingresado es par,caso contrario falso

def number_is_even (n):
 return True if n % 2 ==0 else False

#b.    Que retorne verdadero si el número ingresado es impar,caso contrario falso

def number_is_odd(n):
    return True if n % 2 != 0 else True

#c.    Que retorne los numeros pares de un intervalo

def list_even_numbers(n):
    list=[]
    for i in range  (n+1):
        list.append(i) if i % 2 == 0 else None
    return list