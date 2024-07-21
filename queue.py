class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        print(f"Добавлен элемент \'{item}\'")
        self.items.insert(0, item)

    def dequeue(self):
        del_item = self.items.pop()
        print(f"Удалён элемент \'{del_item}\'")
        return del_item

    def size(self):
        print(f"Размер очереди: {len(self.items)}")
        return len(self.items)

queue = Queue()
print(queue.is_empty())

queue.enqueue("действие 1")
queue.enqueue("действие 2")
queue.enqueue("действие 3")
queue.enqueue("действие 4")

print(queue.is_empty())
queue.size()
queue.dequeue()
queue.size()
