import unittest

from alxlib.DataStructures.Stack import Stack


class StackTests(unittest.TestCase):
    # Input: _input="data"
    # Expected Output: "data"
    def test_add(self):
        test = Stack()
        self.assertEqual(
            "data",
            test.add("data"),
            "Expected an add to stack with value 'data' to return data"
        )
        self.assertEqual(
            "data",
            test.peek(),
            "Expected stack to contain 'data' as first value"
        )

    # Input: _input="another data"
    # Expected Output: "another data"
    def test_add_another(self):
        test = Stack()
        test.add("data")
        self.assertEqual(
            "another data",
            test.add("another data"),
            "Expected an add to stack with value 'another data' to return 'another data'"
        )
        self.assertEqual(
            "another data",
            test.peek(),
            "Expected stack to contain 'another data' as first value"
        )

    # Input: _input="data"
    # Expected Output: "data"
    def test_pop(self):
        test = Stack()
        test.add("data")
        self.assertEqual(
            "data",
            test.pop(),
            "Expected pop from stack to return 'data'"
        )

    # Input: _input="another data"
    # Expected Output: "another data"
    def test_pop_another(self):
        test = Stack()
        test.add("data")
        test.add("another data")
        self.assertEqual(
            "another data",
            test.pop(),
            "Expected pop from stack to return 'another data'"
        )

    # Input: _input="data"
    # Expected Output: "data"
    def test_peek(self):
        test = Stack()
        test.add("data")
        self.assertEqual(
            "data",
            test.peek(),
            "Expected peek at stack to return 'data'"
        )

    # Input: _input="another data"
    # Expected Output: "another data"
    def test_peek_another(self):
        test = Stack()
        test.add("data")
        test.add("another data")
        self.assertEqual(
            "another data",
            test.peek(),
            "Expected peek at stack to return 'another data'"
        )

    # Input: _input=None
    # Expected Output: None
    def test_init(self):
        test = Stack()
        self.assertEqual(
            None,
            test.peek(),
            "Expected new stack to be empty"
        )

    # Input: _input=None
    # Expected Output: None
    def test_add_none(self):
        test = Stack()
        self.assertEqual(
            None,
            test.add(None),
            "Expected an add to stack with value 'None' to return None"
        )

    # Input: _input=empty string
    # Expected Output: empty string
    def test_add_empty_string(self):
        test = Stack()
        self.assertEqual(
            "",
            test.add(""),
            "Expected an add to stack with value '' to return ''"
        )

    # Input: _input=0
    # Expected Output: 0
    def test_add_zero(self):
        test = Stack()
        self.assertEqual(
            0,
            test.add(0),
            "Expected an add to stack with value '0' to return 0"
        )

    # Input: _input=empty stack
    # Expected Output: None
    def test_pop_empty(self):
        test = Stack()
        self.assertEqual(
            None,
            test.pop(),
            "Expected pop from empty stack to return None"
        )

    # Input: _input=empty stack
    # Expected Output: None
    def test_peek_empty(self):
        test = Stack()
        self.assertEqual(
            None,
            test.peek(),
            "Expected peek at empty stack to return None"
        )

    # Input: _input=stack with one element
    # Expected Output: None
    def test_pop_one_element(self):
        test = Stack()
        test.add("data")
        test.pop()
        self.assertEqual(
            None,
            test.peek(),
            "Expected peek at stack after popping the only element to return None"
        )

    # Input: _input=stack with multiple elements
    # Expected Output: first added element
    def test_pop_until_empty(self):
        test = Stack()
        test.add("data1")
        test.add("data2")
        test.add("data3")
        test.pop()
        test.pop()
        self.assertEqual(
            "data1",
            test.pop(),
            "Expected pop from stack until empty to return the first added element"
        )

    # Input: _input=stack with multiple elements
    # Expected Output: first added element
    def test_peek_after_multiple_pops(self):
        test = Stack()
        test.add("data1")
        test.add("data2")
        test.add("data3")
        test.pop()
        test.pop()
        self.assertEqual(
            "data1",
            test.peek(),
            "Expected peek at stack after multiple pops to return the first added element"
        )

    # Input: _input=stack with multiple elements
    # Expected Output: last added element
    def test_peek_after_multiple_adds(self):
        test = Stack()
        test.add("data1")
        test.add("data2")
        test.add("data3")
        self.assertEqual(
            "data3",
            test.peek(),
            "Expected peek at stack after multiple adds to return the last added element"
        )

    # Input: _input=stack with multiple elements
    # Expected Output: None
    def test_pop_all_elements(self):
        test = Stack()
        test.add("data1")
        test.add("data2")
        test.add("data3")
        test.pop()
        test.pop()
        test.pop()
        self.assertEqual(
            None,
            test.peek(),
            "Expected peek at stack after popping all elements to return None"
        )


if __name__ == '__main__':
    unittest.main()
