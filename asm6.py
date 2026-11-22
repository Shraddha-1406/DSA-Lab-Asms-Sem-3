from collections import deque
class Node:
    def __init__(self, emp_id):
        self.emp_id = emp_id
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self, emp_id):
        if self.root is None:
            self.root = Node(emp_id)
        else:
            self._insert_recursive(self.root, emp_id)
    def _insert_recursive(self, current, emp_id):
        if emp_id < current.emp_id:
            if current.left is None:
                current.left = Node(emp_id)
            else:
                self._insert_recursive(current.left, emp_id)
        elif emp_id > current.emp_id:
            if current.right is None:
                current.right = Node(emp_id)
            else:
                self._insert_recursive(current.right, emp_id)
    def display_level_wise(self):
        if not self.root:
            print("Tree is empty.")
            return
        queue = deque([self.root])
        level = 1
        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(str(node.emp_id))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(f"Level {level}: {' '.join(current_level)}")
            level += 1
    def copy_tree(self):
        new_bst = BST()
        new_bst.root = self._copy_recursive(self.root)
        return new_bst
    def _copy_recursive(self, node):
        if node is None:
            return None
        new_node = Node(node.emp_id)
        new_node.left = self._copy_recursive(node.left)
        new_node.right = self._copy_recursive(node.right)
        return new_node
    def get_height(self):
        return self._height_recursive(self.root)
    def _height_recursive(self, node):
        if node is None:
            return 0  
        left_h = self._height_recursive(node.left)
        right_h = self._height_recursive(node.right)
        return 1 + max(left_h, right_h)
    def print_leaf_nodes(self):
        leaf_nodes = []
        self._get_leaf_nodes_recursive(self.root, leaf_nodes)
        if leaf_nodes:
            print("Leaf nodes (employees with no subordinates):", leaf_nodes)
        else:
            print("No leaf nodes found (tree is empty).")
    def _get_leaf_nodes_recursive(self, node, leaf_nodes):
        if node is None:
            return
        if node.left is None and node.right is None:
            leaf_nodes.append(node.emp_id)
            return
        self._get_leaf_nodes_recursive(node.left, leaf_nodes)
        self._get_leaf_nodes_recursive(node.right, leaf_nodes)
if __name__ == "__main__":
    original_bst = BST()
    emp_ids = [50, 30, 70, 20, 40, 60, 80]
    print(f"Inserting Employee IDs: {emp_ids}\n")
    for emp_id in emp_ids:
        original_bst.insert(emp_id)
    print("--- Original BST (Level-Wise) ---")
    original_bst.display_level_wise()
    copied_bst = original_bst.copy_tree()
    print("\n--- Copied BST (Level-Wise) ---")
    copied_bst.display_level_wise()
    print(f"\nHeight of the BST: {original_bst.get_height()}")
    original_bst.print_leaf_nodes()
