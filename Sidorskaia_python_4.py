# 1. Написать класс связанных списков

class Node(object):
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def get_data(self): #Геттеры (получатели) в Python – это методы, которые используются в объектно-ориентированном
        # программировании (ООП) для доступа к частным атрибутам класса.
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data): # Сеттер (установщик) в Python – это метод, который используется для установки значения
        # свойства. В объектно-ориентированном программировании очень полезно устанавливать значение частных атрибутов в классе.
        self.data = data

# В Python property() является встроенной функцией для создания и возврата свойства объекта.

    def set_next(self, next):
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        if cur_node == None:
            self.head = new_node
            return
        while cur_node.get_next() != None:
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)

    def show(self):
        cur_node = self.head
        output = ""
        while cur_node != None:
            output += str(cur_node.get_data())
            cur_node = cur_node.get_next()
        print(output)

    def length(self):
        cur_node = self.head
        count = 0
        while cur_node != None:
            count += 1
            cur_node = cur_node.get_next()
        print(count)


if __name__ == '__main__':

    my_list = LinkedList()

    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    my_list.append(5)

    my_list.show()
    my_list.length()

#2. Написать класс очереди и стека, используя внутри только списки.
# Стек следует принципу Последний пришел – первый ушел.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        if not self.stack:
            return
        return self.stack.pop(0)


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, num):
        self.queue.append(num)

    def dequeue(self):
        if not self.queue:
            return
        return self.queue.pop(0)


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)



#3. Создать классы, описывающие биологические последовательности ДНК, РНК, белков, наследующие от общего класса
# «последовательность». Каждый класс должен иметь свойство алфавит, уметь возвращать название последовательности,
# саму последовательность, ее длину, статистику по использованию в ней символов, ее молекулярную массу, а также
# специфичные функции (возврат комплементарной последовательности, транскрипция ДНК --> РНК, трансляция РНК --> белок)

