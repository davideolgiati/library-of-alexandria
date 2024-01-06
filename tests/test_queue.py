import unittest

from alxlib.DataStructures.Queue import Queue


class QueueTests(unittest.TestCase):
    # Input: _input="data"
    # Expected Output: "data"
    def test_add(self):
        test = Queue()
        self.assertEqual(
            "data",
            test.add("data"),
            "Expected an add to Queue with value 'data' to return data"
        )
        self.assertEqual(
            "data",
            test.peek(),
            "Expected Queue to contain 'data' as first value"
        )

    # Input: _input="another data"
    # Expected Output: "another data"
    def test_add_another(self):
        test = Queue()
        test.add("data")
        self.assertEqual(
            "another data",
            test.add("another data"),
            "Expected an add to Queue with value 'another data' to return 'another data'"
        )
        self.assertEqual(
            "data",
            test.peek(),
            "Expected Queue to contain 'data' as first value"
        )

    # Input: _input="data"
    # Expected Output: "data"
    def test_pop(self):
        test = Queue()
        test.add("data")
        self.assertEqual(
            "data",
            test.pop(),
            "Expected pop from Queue to return 'data'"
        )

    # Input: _input="another data"
    # Expected Output: "another data"
    def test_pop_another(self):
        test = Queue()
        test.add("data")
        test.add("another data")
        self.assertEqual(
            "data",
            test.pop(),
            "Expected pop from Queue to return 'data'"
        )

    # Input: _input="data"
    # Expected Output: "data"
    def test_peek(self):
        test = Queue()
        test.add("data")
        self.assertEqual(
            "data",
            test.peek(),
            "Expected peek at Queue to return 'data'"
        )

    # Input: _input="another data"
    # Expected Output: "another data"
    def test_peek_another(self):
        test = Queue()
        test.add("data")
        test.add("another data")
        self.assertEqual(
            "data",
            test.peek(),
            "Expected peek at Queue to return 'data'"
        )

    # Input: _input=None
    # Expected Output: None
    def test_init(self):
        test = Queue()
        self.assertEqual(
            None,
            test.peek(),
            "Expected new Queue to be empty"
        )

    # Input: _input=None
    # Expected Output: None
    def test_add_none(self):
        test = Queue()
        self.assertEqual(
            None,
            test.add(None),
            "Expected an add to Queue with value 'None' to return None"
        )

    # Input: _input=empty string
    # Expected Output: empty string
    def test_add_empty_string(self):
        test = Queue()
        self.assertEqual(
            "",
            test.add(""),
            "Expected an add to Queue with value '' to return ''"
        )

    # Input: _input=0
    # Expected Output: 0
    def test_add_zero(self):
        test = Queue()
        self.assertEqual(
            0,
            test.add(0),
            "Expected an add to Queue with value '0' to return 0"
        )

    # Input: _input=empty Queue
    # Expected Output: None
    def test_pop_empty(self):
        test = Queue()
        self.assertEqual(
            None,
            test.pop(),
            "Expected pop from empty Queue to return None"
        )

    # Input: _input=empty Queue
    # Expected Output: None
    def test_peek_empty(self):
        test = Queue()
        self.assertEqual(
            None,
            test.peek(),
            "Expected peek at empty Queue to return None"
        )

    # Input: _input=Queue with one element
    # Expected Output: None
    def test_pop_one_element(self):
        test = Queue()
        test.add("data")
        test.pop()
        self.assertEqual(
            None,
            test.peek(),
            "Expected peek at Queue after popping the only element to return None"
        )

    # Input: _input=Queue with multiple elements
    # Expected Output: first added element
    def test_pop_until_empty(self):
        test = Queue()
        test.add("data1")
        test.add("data2")
        test.add("data3")
        test.pop()
        test.pop()
        self.assertEqual(
            "data3",
            test.pop(),
            "Expected pop from Queue until empty to return the last added element"
        )

    # Input: _input=Queue with multiple elements
    # Expected Output: first added element
    def test_peek_after_multiple_pops(self):
        test = Queue()
        test.add("data1")
        test.add("data2")
        test.add("data3")
        test.pop()
        test.pop()
        self.assertEqual(
            "data3",
            test.peek(),
            "Expected peek at Queue after multiple pops to return the last added element"
        )

    # Input: _input=Queue with multiple elements
    # Expected Output: last added element
    def test_peek_after_multiple_adds(self):
        test = Queue()
        test.add("data1")
        test.add("data2")
        test.add("data3")
        self.assertEqual(
            "data1",
            test.peek(),
            "Expected peek at Queue after multiple adds to return the first added element"
        )

    # Input: _input=Queue with multiple elements
    # Expected Output: None
    def test_pop_all_elements(self):
        test = Queue()
        test.add("data1")
        test.add("data2")
        test.add("data3")
        test.pop()
        test.pop()
        test.pop()
        self.assertEqual(
            None,
            test.peek(),
            "Expected peek at Queue after popping all elements to return None"
        )


if __name__ == '__main__':
    unittest.main()
