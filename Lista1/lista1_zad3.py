#ZADANIE3

def the_lowest(numbers):
    low=numbers[0]
    for i in numbers:
        if i <=low:
            low = i

    return 'index:', numbers.index(low), 'value: ' ,low

list=[]
for i in range(5):
    list.append(int(input('Podaj liczby:')))

print(the_lowest(list))
