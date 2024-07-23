# Стек реализован с помощью связного списка (linked list)
# Связный список состоит из узлов, где каждый узел содержит данные и указатель на следующий узел

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        print(f"Добавлен элемент {value}")

    def pop(self):
        if self.is_empty():
            print(f"Стек не содержит элементов")
            return None
        value = self.top.value
        self.top = self.top.next
        print(f"Удалён элемент {value}")
        return value

    def peek(self):
        if self.is_empty():
            print(f"Стек не содержит элементов")
            return None
        print(f"Последний элемент в стеке: {self.top.value}")
        return self.top.value

    def get_size(self):
        current = self.top
        count = 0
        while current is not None:
            count += 1
            current = current.next
        print(f"Число элементов в стеке: {count}")
        return count

    def print_stack(self):
        current = self.top
        stack_elements = []
        while current is not None:
            stack_elements.append(current.value)
            current = current.next
        print("Содержание стека:", " -> ".join(map(str, stack_elements)))


stack = Stack()
stack.get_size()

stack.push(1)
stack.push(2)
stack.push(3)

stack.print_stack()
stack.get_size()
print()
stack.peek()
stack.pop()
stack.peek()

stack.print_stack()
print()

stack.push(9)
stack.push(8)
stack.push(7)
stack.peek()

stack.print_stack()
stack.get_size()
