#Используя наборы символов из пакета string написать функцию, которая получает на вход строку и возвращает строку,
# в которой все буквы латинского алфавита из исходной строки преобразованы в заглавные символы. Использовать функции
# стандартной библиотеки upper() и find() нельзя.

x = input("letter")
s2 = x.swapcase()
print("letter:", x, s2)




#Добавить к предыдущему заданию функцию с преобразованием всех символов в прописные и функцию с отражением
# (все заглавные становятся прописными и наоборот), минимально дублируя код. Использовать функции стандартной
# библиотеки lower() и find() нельзя.

x = input("letter")
trantab = str.maketrans(x, x.swapcase())
print("letter", x, x.translate(trantab))
#or
x = input("letter")
print("letter", x, x.swapcase())

#Написать программу на Python3, которая сначала запрашивает положительное число-основание системы счисления,
# затем два числа в системе счисления с этим основанием, и потом четвертое число-основание системы счисления,
# в которой надо вывести результат. В ходе выполнения программа возвращает результат сложения двух чисел в требуемой
# системе счисления. Нельзя использовать для перевода функцию int().

class Number:

    def __init__(self, num):
        self.num = num

    def convert_integer(self, base):
        if base > 36:
            return "Основание системы счисления должно быть не больше 36-ти"
        num = self.num

        number = ''

        while num > 0:
            num, remainder = divmod(num, base)
            if remainder > 9:
                remainder = chr(ord('A') + remainder - 10)
            number = str(remainder) + number
        return number


if __name__ == '__main__':
    num1 = Number(int(input("Десятичное число_1: ")))
    num2 = Number(int(input("Десятичное число_2: ")))

    base = int(input("Основание в которое переводим (2-36): "))

    sum = Number(num1.num + num2.num)
    print("Сумма двух чисел: ", num1.num + num2.num)
    print("Результат сложения двух чисел в требуемой системе счисления: ", sum.convert_integer(base))



