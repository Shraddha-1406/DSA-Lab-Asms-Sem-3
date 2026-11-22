class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert a node
    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        temp = self.root

        while True:
            if data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    break
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    break
                temp = temp.right

    # Non-Recursive Inorder Traversal
    def inorder(self):
        stack = []
        temp = self.root

        print("Inorder Traversal:", end=" ")

        while temp or stack:
            while temp:
                stack.append(temp)
                temp = temp.left

            temp = stack.pop()
            print(temp.data, end=" ")
            temp = temp.right

    # Non-Recursive Preorder Traversal
    def preorder(self):
        if self.root is None:
            return

        stack = [self.root]

        print("\nPreorder Traversal:", end=" ")

        while stack:
            temp = stack.pop()
            print(temp.data, end=" ")

            if temp.right:
                stack.append(temp.right)

            if temp.left:
                stack.append(temp.left)


# Main Program
tree = BST()

n = int(input("Enter number of nodes: "))

for i in range(n):
    value = int(input("Enter node value: "))
    tree.insert(value)

tree.inorder()
tree.preorder()
