###1Числа Фибоначи
n = int(input("Number"))
a=0
b=1
for i in range(1, n):
 c=a+b
 a=b
 b=c
 print(b)

####2Простое или составное число

n = int(input("Number"))
simple = True
i = 2
while i < n:
    if n % i == 0:
        simple = False
    i += 1
if simple:
    print("Простое число")
else:
    print("Сложное число")

###3 Нахождение делителей
numb = int(input("Введите целое число: "))
print('Простые: ', end = ' ')
for i in range(numb - 1, 1, -1):
    is_simple = 0
    if (numb % i == 0):
        for j in range(i - 1, 1, -1):
            if (i % j == 0):
                is_simple = is_simple + 1
        if (is_simple == 0):
    print(i, end = ' ')

###4 Программа находит наибольший общий делитель для двух введенных чисел.

def find(a,b):
    while a!= b:
        if a > b:
            a-= b
        else:
            b -= a
    return a
res = find(84, 24)
print(res)

###5 Программа запрашивает число, а затем выводит квадрат из *, где длина стороны равна данному числу.
n = int(input('Namber: '))
for i in range (n):
    print("*" * n)

###6  Программа запрашивает два числа, а затем выводит прямоугольник из *, где длины сторон равны данным числам.

n = 3
m = 4
print(('*' * n + '\n') * m)

###7 Программа запрашивает два числа и выводит на экран прямоугольник, в котором змейкой по вертикали записаны числа, начиная с 1
n = 3
for i in range(1, n+1):
    print(range(i, n * n + 1, n))