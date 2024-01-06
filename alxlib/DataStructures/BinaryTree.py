class BinaryTree:
    class _Node:
        def set_left(self, node):
            if not type(node) is BinaryTree._Node:
                raise TypeError
            self.left = node

        def set_right(self, node):
            if not type(node) is BinaryTree._Node:
                raise TypeError
            self.right = node

        def get_left(self):
            return self.left

        def get_right(self):
            return self.right

        def get_value(self):
            return self.value

        def __init__(self, value):
            self.value = value
            self.right = None
            self.left = None

    def add(self, value):
        if self.root is None:
            self.root = BinaryTree._Node(value)
            self.type = type(value)
        else:
            levels = 0
            if type(value) is not self.type:
                raise TypeError
            keep_going = True
            current_node = self.root
            while keep_going:
                levels = levels + 1
                if current_node.get_value() < value:
                    if current_node.get_right() is None:
                        current_node.set_right(BinaryTree._Node(value))
                        keep_going = False
                    else:
                        current_node = current_node.get_right()
                else:
                    if current_node.get_left() is None:
                        current_node.set_left(BinaryTree._Node(value))
                        keep_going = False
                    else:
                        current_node = current_node.get_left()
            if levels > self.levels:
                self.levels = levels

        return value

    def find(self, value):
        current_node = self.root
        keep_going = True
        found = True

        while keep_going:
            if current_node is None:
                found = False
                keep_going = False
            else:
                if current_node.get_value() == value:
                    keep_going = False
                elif current_node.get_value() > value:
                    current_node = current_node.get_left()
                else:
                    current_node = current_node.get_right()

        return found

    def get_rightmost(self, level=-1):
        if not self.root:
            return None
        if level == -1:
            stop = self.levels + 1
        else:
            stop = level

        current = 0

        current_node = self.root

        while current_node.get_right() is not None and current < stop:
            current_node = current_node.get_right()
            current = current + 1

        return current_node.get_value()

    def traverse_bfs(self):
        stack = [self.root]
        return_stack = []

        while stack:
            current_node = stack.pop()

            if current_node is not None:
                stack.append(current_node.get_right())
                stack.append(current_node.get_left())
                return_stack.append(current_node.get_value())

        return return_stack

    def traverse_dfs_inorder(self):
        stack = [self.root]
        return_stack = []

        while stack:
            current_node = stack.pop()

            while current_node is not None:
                stack.append(current_node)
                current_node = current_node.get_left()

            if stack:
                current_node = stack.pop()
                return_stack.append(current_node.get_value())
                stack.append(current_node.get_right())

        return return_stack

    def traverse_dfs_preorder(self):
        stack = [self.root]
        return_stack = []

        while stack:
            current_node = stack.pop()

            if current_node is not None:
                return_stack.append(current_node.get_value())
                stack.append(current_node.get_left())
                stack.append(current_node.get_right())

        return return_stack

    def traverse_dfs_postorder(self):
        stack = [self.root]
        return_stack = []

        while stack:
            current_node = stack.pop()

            while current_node is not None:
                stack.append(current_node)
                current_node = current_node.get_left()

            if stack:
                current_node = stack.pop()
                return_stack.append(current_node.get_value())
                stack.append(current_node.get_right())

        return return_stack

    def balance(self):
        # Set The middle element of the array as root.
        #     Recursively do the same for the left half and right half.
        #         Get the middle of the left half and make it the left child of the root created in step 1.
        #         Get the middle of the right half and make it the right child of the root created in step 1.

        new = BinaryTree()
        current = self.traverse_dfs_inorder()

        stack = [{"min": 0, "max": len(current) - 1}]

        while stack:
            next_node_details = stack.pop()

            _min = next_node_details["min"]
            _max = next_node_details["max"]
            mid = int((_min + _max) / 2)

            new.add(current[mid])

            if _min <= (mid - 1):
                stack.append({"min": _min, "max": mid - 1})

            if _max >= (mid + 1):
                stack.append({"min": mid + 1, "max": _max})

        self.root = new.root

    def is_height_balanced(self):
        # To check if a Binary tree is balanced we need to check three conditions :
        #     The absolute difference between heights of left and right subtrees at any node should be less than 1.
        #     For each node, its left subtree should be a balanced binary tree.
        #     For each node, its right subtree should be a balanced binary tree.

        stack = [dict(node=self.root, depth=0)]

        min_depth = float('inf')
        max_depth = -float('inf')

        is_balanced = True

        while stack:
            current_input = stack.pop()
            current_node = current_input["node"]

            if not current_node or (not current_node.get_left() and not current_node.get_right()):
                min_depth = min(current_input["depth"], min_depth)
                max_depth = max(current_input["depth"], max_depth)

                if max_depth - min_depth > 1:
                    is_balanced = False
                    stack = []
            else:
                stack.append(dict(
                    node=current_node.get_left(),
                    depth=current_input["depth"] + (1 if current_node.get_left() is not None else 0)
                ))
                stack.append(dict(
                    node=current_node.get_right(),
                    depth=current_input["depth"] + (1 if current_node.get_right() is not None else 0)
                ))

        return is_balanced

    def __init__(self):
        self.root = None
        self.type = None
        self.levels = 0
