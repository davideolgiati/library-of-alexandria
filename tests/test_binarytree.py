import unittest

from alxlib.DataStructures.BinaryTree import BinaryTree


class TestBinaryTree(unittest.TestCase):

    # Input: value="data"
    # Expected Output: "data"
    def test_add(self):
        test = BinaryTree()
        self.assertEqual(
            "data",
            test.add(value="data"),
            "Expected an add to binary tree with value 'data' to return data"
        )

    # Input: value="data"
    # Expected Output: True
    def test_find(self):
        test = BinaryTree()
        test.add(value="data")
        self.assertEqual(
            True,
            test.find("data"),
            "Expected binary tree to contain 'data'"
        )

    # Input: value="data"
    # Expected Output: False
    def test_find_not_present(self):
        test = BinaryTree()
        self.assertEqual(
            False,
            test.find("data"),
            "Expected binary tree not to contain 'data'"
        )

    # Input: value="data", level=-1
    # Expected Output: "data"
    def test_get_rightmost(self):
        test = BinaryTree()
        test.add(value="data")
        self.assertEqual(
            "data",
            test.get_rightmost(),
            "Expected rightmost value of binary tree to be 'data'"
        )

    # Input: value="data", level=0
    # Expected Output: None
    def test_get_rightmost_level_zero(self):
        test = BinaryTree()
        test.add(value="data")
        test.add(value="data1")
        test.add(value="aaaa")
        self.assertEqual(
            "data",
            test.get_rightmost(level=0),
            "Expected rightmost value of binary tree at level 0 to be 'data'"
        )

    # Input: value="data1", value="data2"
    # Expected Output: "data2"
    def test_get_rightmost_multiple_values(self):
        test = BinaryTree()
        test.add(value="data1")
        test.add(value="data2")
        self.assertEqual(
            "data2",
            test.get_rightmost(),
            "Expected rightmost value of binary tree to be 'data2'"
        )

    # Input: None
    # Expected Output: None
    def test_get_rightmost_empty_tree(self):
        test = BinaryTree()
        self.assertEqual(
            None,
            test.get_rightmost(),
            "Expected rightmost value of empty binary tree to be None"
        )

    # Input: None
    # Expected Output: BinaryTree object
    def test_init(self):
        test = BinaryTree()
        self.assertIsInstance(
            test,
            BinaryTree,
            "Expected object to be instance of BinaryTree"
        )

    # Input: None
    # Expected Output: None
    def test_init_root(self):
        test = BinaryTree()
        self.assertIsNone(
            test.root,
            "Expected root of new binary tree to be None"
        )

    # Input: value=range(1, 1001)
    # Expected Output: 1000
    def test_large_number_of_nodes(self):
        test = BinaryTree()
        for i in range(1, 1001):
            test.add(value=i)
        self.assertEqual(
            1000,
            test.get_rightmost(),
            "Expected rightmost value of binary tree to be 10000"
        )

    # Input: value=[]
    # Expected Output: []
    def test_traverse_dfs_inorder_empty(self):
        test = BinaryTree()
        self.assertEqual(
            [],
            test.traverse_dfs_inorder(),
            "Expected the traverse_dfs_inorder operation on an empty binary tree to return []"
        )

    # Input: value=[2,1,4,3]
    # Expected Output: [1,2,3,4]
    def test_traverse_dfs_inorder_unordered(self):
        test = BinaryTree()
        for i in [2, 1, 4, 3]:
            test.add(value=i)
        self.assertEqual(
            [1, 2, 3, 4],
            test.traverse_dfs_inorder(),
            "Expected the traverse_dfs_inorder operation on a binary tree built upon [2,1,4,3] to return [1,2,3,4]"
        )

    # Input: value=[1]
    # Expected Output: [1]
    def test_traverse_dfs_inorder_single_node(self):
        test = BinaryTree()
        test.add(value=1)
        self.assertEqual(
            [1],
            test.traverse_dfs_inorder(),
            "Expected the traverse_dfs_inorder operation on a binary tree with a single node to return [1]"
        )

    # Input: value=[5,2,7,1,3,6,8]
    # Expected Output: [1,2,3,5,6,7,8]
    def test_traverse_dfs_inorder_full_tree(self):
        test = BinaryTree()
        for i in [5, 2, 7, 1, 3, 6, 8]:
            test.add(value=i)
        self.assertEqual(
            [1, 2, 3, 5, 6, 7, 8],
            test.traverse_dfs_inorder(),
            "Expected the traverse_dfs_inorder operation on a full binary tree to return [1,2,3,5,6,7,8]"
        )

    # Input: value=[3,3,3,3]
    # Expected Output: [3,3,3,3]
    def test_traverse_dfs_inorder_duplicate_values(self):
        test = BinaryTree()
        for i in [3, 3, 3, 3]:
            test.add(value=i)
        self.assertEqual(
            [3, 3, 3, 3],
            test.traverse_dfs_inorder(),
            "Expected the traverse_dfs_inorder operation on a binary tree with duplicate values to return [3,3,3,3]"
        )

    # Input: value=[4,2,6,1,3,5,7]
    # Expected Output: [1,2,3,4,5,6,7]
    def test_traverse_dfs_inorder_balanced_tree(self):
        test = BinaryTree()
        for i in [4, 2, 6, 1, 3, 5, 7]:
            test.add(value=i)
        self.assertEqual(
            [1, 2, 3, 4, 5, 6, 7],
            test.traverse_dfs_inorder(),
            "Expected the traverse_dfs_inorder operation on a balanced binary tree to return [1,2,3,4,5,6,7]"
        )

    # Input: value=[1,2,3,4,5,6,7,8,9,10]
    # Expected Output: [1,2,3,4,5,6,7,8,9,10]
    def test_traverse_dfs_inorder_large_tree(self):
        test = BinaryTree()
        for i in range(1, 11):
            test.add(value=i)
        self.assertEqual(
            list(range(1, 11)),
            test.traverse_dfs_inorder(),
            "Expected the traverse_dfs_inorder operation on a large binary tree to return [1,2,3,4,5,6,7,8,9,10]"
        )

    # Input: value=[5,2,8,-1,3,7,9]
    # Expected Output: [-1,2,3,5,7,8,9]
    def test_traverse_dfs_inorder_negative_values(self):
        test = BinaryTree()
        for i in [5, 2, 8, -1, 3, 7, 9]:
            test.add(value=i)
        self.assertEqual(
            [-1, 2, 3, 5, 7, 8, 9],
            test.traverse_dfs_inorder(),
            "Expected the traverse_dfs_inorder operation on a binary tree with negative values to return [-1,2,3,5,7,8,9]"
        )

    # Input: value=[10,5,0,-5,-10]
    # Expected Output: [-10,-5,0,5,10]
    def test_traverse_dfs_inorder_descending_order(self):
        test = BinaryTree()
        for i in [10, 5, 0, -5, -10]:
            test.add(value=i)
        self.assertEqual(
            [-10, -5, 0, 5, 10],
            test.traverse_dfs_inorder(),
            "Expected the traverse_dfs_inorder operation on a binary tree with descending order values to return [-10,-5,0,5,10]"
        )

    # Test if the tree is height balanced with a simple 3-node complete tree
    # Input: value=[2,1,3]
    # Expected Output: True
    def test_is_height_balanced_simple(self):
        test = BinaryTree()
        for i in [2, 1, 3]:
            test.add(value=i)
        self.assertTrue(
            test.is_height_balanced(),
            "Expected binary tree built upon [2,1,3] to be height balanced"
        )

    # Test if the tree is height balanced after adding multiple nodes
    # Input: value=[3,1,4,2,5]
    # Expected Output: True
    def test_is_height_balanced_multiple_nodes(self):
        test = BinaryTree()
        for i in [3, 1, 4, 2, 5]:
            test.add(value=i)
        self.assertTrue(
            test.is_height_balanced(),
            "Expected binary tree built upon [3,1,4,2,5] to be height balanced"
        )

    # Test if the tree is height balanced with a single node
    # Input: value=[1]
    # Expected Output: True
    def test_is_height_balanced_single_node(self):
        test = BinaryTree()
        test.add(value=1)
        self.assertTrue(
            test.is_height_balanced(),
            "Expected binary tree with a single node to be height balanced"
        )

    # Test if the tree is height balanced with an empty tree
    # Input: value=[]
    # Expected Output: True
    def test_is_height_balanced_empty_tree(self):
        test = BinaryTree()
        self.assertTrue(
            test.is_height_balanced(),
            "Expected empty binary tree to be height balanced"
        )

    # Test if the tree is height balanced with a left-skewed tree
    # Input: value=[4,3,2,1]
    # Expected Output: False
    def test_is_height_balanced_left_skewed(self):
        test = BinaryTree()
        for i in [4, 3, 2, 1]:
            test.add(value=i)
        self.assertFalse(
            test.is_height_balanced(),
            "Expected left-skewed binary tree to be not height balanced"
        )

    # Test if the tree is height balanced with a right-skewed tree
    # Input: value=[1,2,3,4]
    # Expected Output: False
    def test_is_height_balanced_right_skewed(self):
        test = BinaryTree()
        for i in [1, 2, 3, 4]:
            test.add(value=i)
        self.assertFalse(
            test.is_height_balanced(),
            "Expected right-skewed binary tree to be not height balanced"
        )

    # Test if the tree is height balanced with a full tree
    # Input: value=[4,2,6,1,3,5,7]
    # Expected Output: True
    def test_is_height_balanced_full_tree(self):
        test = BinaryTree()
        for i in [4, 2, 6, 1, 3, 5, 7]:
            test.add(value=i)
        self.assertTrue(
            test.is_height_balanced(),
            "Expected full binary tree to be height balanced"
        )

    # Test if the tree is height balanced with a complete tree missing some nodes
    # Input: value=[4,2,6,1,3,5]
    # Expected Output: True
    def test_is_height_balanced_almost_full_tree(self):
        test = BinaryTree()
        for i in [4, 2, 6, 1, 3, 5]:
            test.add(value=i)
        self.assertTrue(
            test.is_height_balanced(),
            "Expected almost full binary tree to be height balanced"
        )

    # Test if the tree is height balanced with a tree having only left children
    # Input: value=[3,2,1]
    # Expected Output: False
    def test_is_height_balanced_left_children_only(self):
        test = BinaryTree()
        for i in [3, 2, 1]:
            test.add(value=i)
        self.assertFalse(
            test.is_height_balanced(),
            "Expected binary tree with only left children to be not height balanced"
        )

    # Test if the tree is height balanced with a tree having only right children
    # Input: value=[1,2,3]
    # Expected Output: False
    def test_is_height_balanced_right_children_only(self):
        test = BinaryTree()
        for i in [1, 2, 3]:
            test.add(value=i)
        self.assertFalse(
            test.is_height_balanced(),
            "Expected binary tree with only right children to be not height balanced"
        )

    # Test if the tree is height balanced with a tree having random node values
    # Input: value=[10,5,15,2,7,12,17,1,3,6,8,11,13,16,18]
    # Expected Output: True
    def test_is_height_balanced_random_values(self):
        test = BinaryTree()
        for i in [10, 5, 15, 2, 7, 12, 17, 1, 3, 6, 8, 11, 13, 16, 18]:
            test.add(value=i)
        self.assertTrue(
            test.is_height_balanced(),
            "Expected binary tree with random node values to be height balanced"
        )

    # Test if the tree is height balanced with a tree having duplicate values
    # Input: value=[5,3,7,3,7]
    # Expected Output: True
    def test_is_height_balanced_with_duplicates(self):
        test = BinaryTree()
        for i in [5, 3, 7, 3, 7]:
            test.add(value=i)
        self.assertTrue(
            test.is_height_balanced(),
            "Expected binary tree with duplicate values to be height balanced"
        )

    # Test if the tree is height balanced with a tree having negative values
    # Input: value=[-10,-20,0,-30,-15,-5,10]
    # Expected Output: True
    def test_is_height_balanced_negative_values(self):
        test = BinaryTree()
        for i in [-10, -20, 0, -30, -15, -5, 10]:
            test.add(value=i)
        self.assertTrue(
            test.is_height_balanced(),
            "Expected binary tree with negative values to be height balanced"
        )

    # Test if the tree is height balanced with a tree having a large number of nodes
    # Input: value=range(1, 1001)
    # Expected Output: False
    def test_is_height_balanced_large_tree(self):
        test = BinaryTree()
        for i in range(1, 1001):
            test.add(value=i)
        self.assertFalse(
            test.is_height_balanced(),
            "Expected large binary tree to be not height balanced"
        )

    # Test if the tree is height balanced with a tree having a single child at each level
    # Input: value=[10,5,15,20]
    # Expected Output: False
    def test_is_height_balanced_single_child_at_each_level(self):
        test = BinaryTree()
        for i in [10, 5, 15, 20]:
            test.add(value=i)
        self.assertTrue(
            test.is_height_balanced(),
            "Expected binary tree with a single child at each level to be not height balanced"
        )

    # Test if the tree is height balanced with a tree having alternating left and right children
    # Input: value=[10,5,15,3,7,13,17]
    # Expected Output: True
    def test_is_height_balanced_alternating_children(self):
        test = BinaryTree()
        for i in [10, 5, 15, 3, 7, 13, 17]:
            test.add(value=i)
        self.assertTrue(
            test.is_height_balanced(),
            "Expected binary tree with alternating left and right children to be height balanced"
        )

    # Test if the tree is height balanced with a tree having multiple levels of single children
    # Input: value=[10,20,30,40,50]
    # Expected Output: False
    def test_is_height_balanced_multiple_levels_single_children(self):
        test = BinaryTree()
        for i in [10, 20, 30, 40, 50]:
            test.add(value=i)
        self.assertFalse(
            test.is_height_balanced(),
            "Expected binary tree with multiple levels of single children to be not height balanced"
        )

    # Test if the balance method correctly balances a right-skewed tree
    # Input: value=[1,2,3,4]
    # Expected Output: True
    def test_balance_right_skewed(self):
        test = BinaryTree()
        for i in [1, 2, 3, 4]:
            test.add(value=i)
        test.balance()
        self.assertTrue(
            test.is_height_balanced(),
            "Expected right-skewed binary tree to be balanced after balance operation"
        )

    # Test if the balance method correctly balances a left-skewed tree
    # Input: value=[4,3,2,1]
    # Expected Output: True
    def test_balance_left_skewed(self):
        test = BinaryTree()
        for i in [4, 3, 2, 1]:
            test.add(value=i)
        test.balance()
        self.assertTrue(
            test.is_height_balanced(),
            "Expected left-skewed binary tree to be balanced after balance operation"
        )

    # Test if the balance method correctly balances a tree with a single child at each level
    # Input: value=[10,5,15,20]
    # Expected Output: True
    def test_balance_single_child_at_each_level(self):
        test = BinaryTree()
        for i in [10, 5, 15, 20]:
            test.add(value=i)
        test.balance()
        self.assertTrue(
            test.is_height_balanced(),
            "Expected binary tree with a single child at each level to be balanced after balance operation"
        )

    # Test if the balance method correctly balances a tree with alternating left and right children
    # Input: value=[10,5,15,3,7,13,17]
    # Expected Output: True
    def test_balance_alternating_children(self):
        test = BinaryTree()
        for i in [10, 5, 15, 3, 7, 13, 17]:
            test.add(value=i)
        test.balance()
        self.assertTrue(
            test.is_height_balanced(),
            "Expected binary tree with alternating left and right children to be balanced after balance operation"
        )

    # Test if the balance method correctly balances a tree with multiple levels of single children
    # Input: value=[10,20,30,40,50]
    # Expected Output: True
    def test_balance_multiple_levels_single_children(self):
        test = BinaryTree()
        for i in [10, 20, 30, 40, 50]:
            test.add(value=i)
        test.balance()
        self.assertTrue(
            test.is_height_balanced(),
            "Expected binary tree with multiple levels of single children to be balanced after balance operation"
        )

    # Test if the balance method correctly balances a tree with random node values
    # Input: value=[10,5,15,2,7,12,17,1,3,6,8,11,13,16,18]
    # Expected Output: True
    def test_balance_random_values(self):
        test = BinaryTree()
        for i in [10, 5, 15, 2, 7, 12, 17, 1, 3, 6, 8, 11, 13, 16, 18]:
            test.add(value=i)
        test.balance()
        self.assertTrue(
            test.is_height_balanced(),
            "Expected binary tree with random node values to be balanced after balance operation"
        )

    # Test if the balance method correctly balances a tree with duplicate values
    # Input: value=[5,3,7,3,7]
    # Expected Output: True
    def test_balance_with_duplicates(self):
        test = BinaryTree()
        for i in [5, 3, 7, 3, 7]:
            test.add(value=i)
        test.balance()
        self.assertTrue(
            test.is_height_balanced(),
            "Expected binary tree with duplicate values to be balanced after balance operation"
        )

    # Test if the balance method correctly balances a tree with negative values
    # Input: value=[-10,-20,0,-30,-15,-5,10]
    # Expected Output: True
    def test_balance_negative_values(self):
        test = BinaryTree()
        for i in [-10, -20, 0, -30, -15, -5, 10]:
            test.add(value=i)
        test.balance()
        self.assertTrue(
            test.is_height_balanced(),
            "Expected binary tree with negative values to be balanced after balance operation"
        )

    # Test if the balance method correctly balances a large tree
    # Input: value=range(1, 1001)
    # Expected Output: True
    def test_balance_large_tree(self):
        test = BinaryTree()
        for i in range(1, 1001):
            test.add(value=i)
        test.balance()
        self.assertTrue(
            test.is_height_balanced(),
            "Expected large binary tree to be balanced after balance operation"
        )

    # Input with a single node
    # Expected Output: The value of the single node
    def test_single_node(self):
        test = BinaryTree()
        test.add(5)
        self.assertEqual(
            5,
            test.get_rightmost(),
            "Expected the rightmost value to be 5 in a tree with a single node"
        )

    # Input with all nodes having the same value
    # Expected Output: The value of the rightmost node
    def test_same_value_nodes(self):
        test = BinaryTree()
        for i in [3, 3, 3, 3]:
            test.add(i)
        self.assertEqual(
            3,
            test.get_rightmost(),
            "Expected the rightmost value to be 3 in a tree with all nodes having the same value"
        )

    # Input with a large unbalanced tree
    # Expected Output: The value of the rightmost node
    def test_large_unbalanced_tree(self):
        test = BinaryTree()
        for i in range(10000, 0, -1):
            test.add(i)
        self.assertEqual(
            10000,
            test.get_rightmost(),
            "Expected the rightmost value to be 1 in a large unbalanced tree"
        )

    # Input with a completely balanced tree
    # Expected Output: The value of the rightmost node
    def test_completely_balanced_tree(self):
        test = BinaryTree()
        for i in [5, 3, 7, 2, 4, 6, 8]:
            test.add(i)
        self.assertEqual(
            8,
            test.get_rightmost(),
            "Expected the rightmost value to be 8 in a completely balanced tree"
        )

    # Input with a randomly shuffled tree
    # Expected Output: The value of the rightmost node
    def test_random_shuffled_tree(self):
        test = BinaryTree()
        for i in [7, 3, 9, 2, 5, 8, 10, 4, 6]:
            test.add(i)
        self.assertEqual(
            10,
            test.get_rightmost(),
            "Expected the rightmost value to be 10 in a randomly shuffled tree"
        )

    # Input with a right-skewed tree
    # Expected Output: The value of the rightmost node
    def test_right_skewed_tree(self):
        test = BinaryTree()
        for i in range(1, 10001):
            test.add(i)
        self.assertEqual(
            10000,
            test.get_rightmost(),
            "Expected the rightmost value to be 10000 in a right-skewed tree"
        )

    # Input with an empty tree
    # Expected Output: None
    def test_empty_tree(self):
        test = BinaryTree()
        self.assertIsNone(
            test.get_rightmost(),
            "Expected None for the rightmost value in an empty tree"
        )

    # Input with a tree containing negative values
    # Expected Output: The value of the rightmost node
    def test_negative_values_tree(self):
        test = BinaryTree()
        for i in [-3, -1, -2, -5, -4]:
            test.add(i)
        self.assertEqual(
            -1,
            test.get_rightmost(),
            "Expected the rightmost value to be -1 in a tree containing negative values"
        )

    # Input with a tree containing floating point numbers
    # Expected Output: The value of the rightmost node
    def test_float_values_tree(self):
        test = BinaryTree()
        for i in [3.5, 1.2, 4.8, 2.7, 3.2]:
            test.add(i)
        self.assertEqual(
            4.8,
            test.get_rightmost(),
            "Expected the rightmost value to be 4.8 in a tree containing floating point numbers"
        )

    # Input with a tree containing large integer values
    # Expected Output: The value of the rightmost node
    def test_large_integer_values_tree(self):
        test = BinaryTree()
        for i in [999999999, 777777777, 888888888, 555555555]:
            test.add(i)
        self.assertEqual(
            999999999,
            test.get_rightmost(),
            "Expected the rightmost value to be 999999999 in a tree containing large integer values"
        )

    # Input with a tree containing duplicate values
    # Expected Output: The value of the rightmost node
    def test_duplicate_values_tree(self):
        test = BinaryTree()
        for i in [5, 3, 7, 3, 2, 6, 8, 2, 4]:
            test.add(i)
        self.assertEqual(
            8,
            test.get_rightmost(),
            "Expected the rightmost value to be 8 in a tree containing duplicate values"
        )

    # Input with a tree containing both positive and negative values
    # Expected Output: The value of the rightmost node
    def test_mixed_positive_negative_values_tree(self):
        test = BinaryTree()
        for i in [-5, 3, -7, 2, 4, -6, 8, -2]:
            test.add(i)
        self.assertEqual(
            8,
            test.get_rightmost(),
            "Expected the rightmost value to be 8 in a tree containing both positive and negative values"
        )

    # Input with a tree where all nodes are left children
    # Expected Output: The value of the rightmost node (the root)
    def test_all_left_children_tree(self):
        test = BinaryTree()
        for i in [8, 7, 6, 5, 4, 3, 2, 1]:
            test.add(i)
        self.assertEqual(
            8,
            test.get_rightmost(),
            "Expected the rightmost value to be the root (8) in a tree where all nodes are left children"
        )

    # Input with a tree where all nodes are right children
    # Expected Output: The value of the rightmost leaf node
    def test_all_right_children_tree(self):
        test = BinaryTree()
        for i in [1, 2, 3, 4, 5, 6, 7, 8]:
            test.add(i)
        self.assertEqual(
            8,
            test.get_rightmost(),
            "Expected the rightmost value to be the rightmost leaf node (8) in a tree where all nodes are right children"
        )

    # Input with a tree containing only one branch
    # Expected Output: The value of the rightmost node
    def test_single_branch_tree(self):
        test = BinaryTree()
        for i in [1, 2, 3, 4, 5, 6, 7]:
            test.add(i)
        self.assertEqual(
            7,
            test.get_rightmost(),
            "Expected the rightmost value to be 7 in a tree containing only one branch"
        )

    # Input with a tree containing a single left child
    # Expected Output: The value of the rightmost node
    def test_single_left_child_tree(self):
        test = BinaryTree()
        for i in [5, 3]:
            test.add(i)
        self.assertEqual(
            5,
            test.get_rightmost(),
            "Expected the rightmost value to be 5 in a tree containing a single left child"
        )

    # Input with a tree containing a single right child
    # Expected Output: The value of the rightmost node
    def test_single_right_child_tree(self):
        test = BinaryTree()
        for i in [3, 5]:
            test.add(i)
        self.assertEqual(
            5,
            test.get_rightmost(),
            "Expected the rightmost value to be 5 in a tree containing a single right child"
        )

    # Input with a tree containing only negative values
    # Expected Output: The value of the rightmost node
    def test_all_negative_values_tree(self):
        test = BinaryTree()
        for i in [-3, -5, -2, -4, -1]:
            test.add(i)
        self.assertEqual(
            -1,
            test.get_rightmost(),
            "Expected the rightmost value to be -1 in a tree containing only negative values"
        )


if __name__ == '__main__':
    unittest.main()
