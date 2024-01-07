import unittest

from alxlib.DataStructures.BinaryTree import BinaryTree


class TestBinaryTreeSpot(unittest.TestCase):
    # Input: value=[2,1,3]
    # Expected Output: True
    def test_height_balanced(self):
        test = BinaryTree()
        for i in [2, 1, 3]:
            test.add(value=i)
        self.assertEqual(
            True,
            test.is_height_balanced(),
            "Expected binary tree built upon [2,1,3] to be height balanced"
        )

    # Input: value=[0, "ciao"]
    # Expected Output: TypeError
    def test_mixed(self):
        with self.assertRaises(TypeError):
            test = BinaryTree()
            test.add(value=0)
            test.add(value="ciao")

    # Input: value=[2,1,3]
    # Expected Output: True
    def test_add_and_find(self):
        test = BinaryTree()
        for i in [2, 1, 3]:
            test.add(value=i)
        self.assertEqual(
            True,
            test.find(value=3),
            "Expected to find 3 in the binary tree"
        )

    # Input: value=[2,1,3]
    # Expected Output: 3
    def test_get_rightmost(self):
        test = BinaryTree()
        for i in [2, 1, 3]:
            test.add(value=i)
        self.assertEqual(
            3,
            test.get_rightmost(),
            "Expected rightmost value of binary tree to be 3"
        )

    # Input: value=[2,1,3], level=0
    # Expected Output: 2
    def test_get_rightmost_at_level(self):
        test = BinaryTree()
        for i in [2, 1, 3]:
            test.add(value=i)
        self.assertEqual(
            2,
            test.get_rightmost(level=0),
            "Expected rightmost value of binary tree to be 3"
        )

    # Input: value=[2,1,3]
    # Expected Output: [2,1,3]
    def test_traverse_bfs(self):
        test = BinaryTree()
        for i in [2, 1, 3]:
            test.add(value=i)
        self.assertEqual(
            [2, 1, 3],
            test.traverse_bfs(),
            "Expected BFS traversal of binary tree to be [2,1,3]"
        )

    # Input: value=[2,1,3]
    # Expected Output: [1,2,3]
    def test_traverse_dfs_inorder(self):
        test = BinaryTree()
        for i in [2, 1, 3]:
            test.add(value=i)
        self.assertEqual(
            [1, 2, 3],
            test.traverse_dfs_inorder(),
            "Expected inorder DFS traversal of binary tree to be [1,2,3]"
        )

    # Input: value=[2,1,3]
    # Expected Output: [2,1,3]
    def test_traverse_dfs_preorder(self):
        test = BinaryTree()
        for i in [2, 1, 3]:
            test.add(value=i)
        self.assertEqual(
            [2, 1, 3],
            test.traverse_dfs_preorder(),
            "Expected preorder DFS traversal of binary tree to be [2,1,3]"
        )

    # Input: value=[2,1,3]
    # Expected Output: [1,3,2]
    def test_traverse_dfs_postorder(self):
        test = BinaryTree()
        for i in [2, 1, 3]:
            test.add(value=i)
        self.assertEqual(
            [1, 3, 2],
            test.traverse_dfs_postorder(),
            "Expected postorder DFS traversal of binary tree to be [1,3,2]"
        )

    # Input: value=[3,2,1]
    # Expected Output: value=[2,1,3]
    def test_balance(self):
        test = BinaryTree()
        for i in [3, 2, 1]:
            test.add(value=i)
        test.balance()
        self.assertEqual(
            [2, 1, 3],
            test.traverse_bfs(),
            "Expected balanced binary tree to be [2,1,3]"
        )


class TestBinaryTreeWithMemory(unittest.TestCase):

    def setUp(self):
        self.tree = BinaryTree()

    def test_add_single(self):
        # Input: value=1
        # Expected Output: True (node added)
        self.tree.add(1)
        self.assertTrue(self.tree.find(1), "Expected to find 1 after adding it to the tree")

    def test_add_multiple(self):
        # Input: values=[2, 1, 3]
        # Expected Output: True (all nodes added)
        for value in [2, 1, 3]:
            self.tree.add(value)
        for value in [2, 1, 3]:
            self.assertTrue(self.tree.find(value), f"Expected to find {value} after adding it to the tree")

    def test_find_nonexistent(self):
        # Input: value=4
        # Expected Output: False (node not found)
        self.assertFalse(self.tree.find(4), "Expected not to find 4 in an empty tree")

    def test_get_rightmost_empty(self):
        # Input: None
        # Expected Output: None (tree is empty)
        self.assertIsNone(self.tree.get_rightmost(), "Expected rightmost value of an empty tree to be None")

    def test_get_rightmost_nonempty(self):
        # Input: values=[2, 1, 3]
        # Expected Output: 3
        for value in [2, 1, 3]:
            self.tree.add(value)
        self.assertEqual(self.tree.get_rightmost(), 3, "Expected rightmost value to be 3")

    def test_traverse_bfs_empty(self):
        # Input: None
        # Expected Output: []
        self.assertEqual(self.tree.traverse_bfs(), [], "Expected BFS traversal of an empty tree to be []")

    def test_traverse_dfs_inorder_empty(self):
        # Input: None
        # Expected Output: []
        self.assertEqual(self.tree.traverse_dfs_inorder(), [],
                         "Expected inorder DFS traversal of an empty tree to be []")

    def test_balance_empty(self):
        # Input: None
        # Expected Output: None (tree is empty)
        self.tree.balance()
        self.assertEqual(self.tree.traverse_bfs(), [],
                         "Expected BFS traversal of an empty tree to be [] after balancing")

    def test_is_height_balanced_empty(self):
        # Input: None
        # Expected Output: True (empty tree is considered balanced)
        self.assertTrue(self.tree.is_height_balanced(), "Expected an empty tree to be height balanced")

    def test_is_height_balanced_unbalanced(self):
        # Input: values=[4, 3, 2, 1]
        # Expected Output: False
        for value in [4, 3, 2, 1]:
            self.tree.add(value)
        self.assertFalse(self.tree.is_height_balanced(), "Expected a linear tree to be unbalanced")

    def test_balance_complex_tree(self):
        # Input: values=[4, 2, 6, 1, 3, 5, 7]
        # Expected Output: Tree is balanced
        for value in [4, 2, 6, 1, 3, 5, 7]:
            self.tree.add(value)
        self.tree.balance()
        self.assertTrue(self.tree.is_height_balanced(), "Expected the tree to be balanced after balancing operation")


class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        self.tree = BinaryTree()

    # Test case for adding a node to an empty tree
    def test_add_to_empty_tree(self):
        self.assertTrue(self.tree.add(1), "Expected to add value 1 to the empty tree")

    # Test case for adding a node to a non-empty tree
    def test_add_to_nonempty_tree(self):
        self.tree.add(1)
        self.assertTrue(self.tree.add(2), "Expected to add value 2 to the non-empty tree")

    # Test case for searching in an empty tree
    def test_search_empty_tree(self):
        self.assertFalse(self.tree.find(1), "Expected search in empty tree to return False")

    # Test case for searching a value that exists in the tree
    def test_search_value_exists(self):
        self.tree.add(1)
        self.assertTrue(self.tree.find(1), "Expected search for value 1 to return True")

    # Test case for searching a value that does not exist in the tree
    def test_search_value_not_exists(self):
        self.tree.add(1)
        self.assertFalse(self.tree.find(2), "Expected search for value 2 to return False")


"""
    # Test case for removing a value from an empty tree
    def test_remove_empty_tree(self):
        self.assertFalse(self.tree.remove(1), "Expected remove from empty tree to return False")

    # Test case for removing a value that exists in the tree
    def test_remove_value_exists(self):
        self.tree.add(1)
        self.assertTrue(self.tree.remove(1), "Expected remove value 1 to return True")

    # Test case for removing a value that does not exist in the tree
    def test_remove_value_not_exists(self):
        self.tree.add(1)
        self.assertFalse(self.tree.remove(2), "Expected remove value 2 to return False")
"""

if __name__ == '__main__':
    unittest.main()
