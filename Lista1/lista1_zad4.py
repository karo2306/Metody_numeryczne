#ZADANIE4
#4 looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any chart of a given length.
import matplotlib.pyplot as plt

a=int(input("Podaj lczbę: "))
length=[]
for i in range(a+1):
    length.append(i)
print(length)

y=[2]*(a+1)
plt.plot(length,y)
plt.show()

