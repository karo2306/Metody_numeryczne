#ZADANIE2

def factorial(number):
    fact=1
    if number in (0,1):
        return 1
    else:
        for i in range(2,number+1):
            fact=fact*i
        return fact

num=input("Podaj liczbę:")
num=int(num)

print(factorial(num))
