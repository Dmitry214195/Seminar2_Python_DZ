''' Задание 3: Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных ИНДЕКСАХ. 
Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.'''

N = int(input("Введите число: "))
datalist = [2, 2, 3, 1, 4]

numbers = list(range (-N,N + 1))

def get_numbers(numbers):
    count =0 
    for element in numbers:
        count +=1
    return count

def get_mult(numbers, index):
    mult = 1
    for i in datalist:
        mult *= numbers[i]
    return mult

print(numbers)
print(datalist)
print(get_mult(numbers, datalist))