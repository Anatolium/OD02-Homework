# Очередь реализована с помощью двух списков, inbox и outbox
# Список inbox предназначен для добавления элементов, outbox – для удаления, он работает как стек
# Использование двух списков для реализации очереди позволяет эффективно разделять операции добавления и удаления

class Queue:
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def enqueue(self, data):
        print(f"Элемент \'{data}\' добавлен в очередь")
        self.inbox.append(data)

    def dequeue(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        if self.outbox:
            print(f"Элемент \'{self.outbox[-1]}\' удален из очереди")
            return self.outbox.pop()
        else:
            return None

    def print_queue(self):
        queue_contents = self.outbox[::-1] + self.inbox
        queue_str = ' -> '.join(map(str, queue_contents))
        print("Содержание очереди:", queue_str)

    def is_empty(self):
        return not self.inbox and not self.outbox

    def get_size(self):
        queue_length = len(self.inbox) + len(self.outbox)
        print(f"Число элементов в очереди: {queue_length}")
        return queue_length


queue = Queue()
queue.get_size()

queue.enqueue("Задача 1")
queue.enqueue("Задача 2")
queue.enqueue("Задача 3")
queue.enqueue("Задача 4")
print()

queue.print_queue()
queue.get_size()
print()

queue.dequeue()
queue.print_queue()
print()

queue.enqueue("Задача 5")
queue.enqueue("Задача 6")
queue.enqueue("Задача 7")
queue.print_queue()
print()

for _ in range(3):
    queue.dequeue()
queue.print_queue()
queue.get_size()
