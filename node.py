class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        print(f"Добавлен узел со значением {key}")
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def print_tree(root):
    if root:
        # Рекурсивно проходим по левому поддереву
        print_tree(root.left)
        # Печатаем значение узла
        print(root.val, end=' ')
        # Рекурсивно проходим по правому поддереву
        print_tree(root.right)

my_node = Node(70)

my_node = insert(my_node, 30)
my_node = insert(my_node, 56)
my_node = insert(my_node, 89)
my_node = insert(my_node, 45)
my_node = insert(my_node, 60)
my_node = insert(my_node, 73)
my_node = insert(my_node, 98)
my_node = insert(my_node, 84)

print("Дерево:")
print_tree(my_node)  # Вывод: 30 45 56 60 70 73 84 89 98
