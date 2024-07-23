# Очередь реализована с помощью связного списка (linked list)
# Связный список состоит из узлов, где каждый узел содержит данные и указатель на следующий узел

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            # При добавлении первого элемента первый и последний элемент очереди равны
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Элемент \'{value}\' добавлен в очередь")

    def dequeue(self):
        if self.is_empty():
            print("Очередь пуста")
            return None
        value = self.front.value
        self.front = self.front.next
        # Если удалили последний элемент
        if self.front is None:
            self.rear = None
        print(f"Элемент \'{value}\' удалён из очереди")
        return value

    def peek(self):
        if self.is_empty():
            print("Очередь пуста")
            return None
        print(f"Первый элемент в очереди: \'{self.front.value}\'")
        return self.front.value

    def get_size(self):
        current = self.front
        count = 0
        while current is not None:
            count += 1
            current = current.next
        print(f"Число элементов в очереди: {count}")
        return count

    def print_queue(self):
        if self.is_empty():
            print("Очередь пуста")
            return
        current = self.front
        queue_elements = []
        while current is not None:
            queue_elements.append(str(current.value))
            current = current.next
        print("Содержание очереди:", " -> ".join(queue_elements))


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
