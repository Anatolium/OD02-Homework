class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        print(f"Добавлен элемент {item}")
        self.items.append(item)

    def pop(self):
        print(f"Удалён элемент {self.items[-1]}")
        return self.items.pop()

    def peek(self):
        print(f"Последний элемент в стеке: {self.items[-1]}")
        return self.items[-1]

    def print_stack(self):
        if self.is_empty():
            print("Стек пуст")
        else:
            print("Текущий стек:", " -> ".join(map(str, reversed(self.items))))


stack = Stack()
print(stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.is_empty())
stack.peek()
stack.pop()
stack.peek()

stack.push(4)
stack.push(5)
stack.print_stack()
