import unittest
from alxlib.FunctionUtils import time_this_function
from alxlib.StringUtils import leftpad, rightpad, is_upper_case, pascal_case, toggle_case, reverse_string


class LeftPadTests(unittest.TestCase):
    # Input: _input="hello", _len=10, char="*"
    # Expected Output: "*****hello"
    def test_normal_operation_with_padding(self):
        self.assertEqual(
            "*****hello",
            leftpad(_input="hello", _len=10, char="*"),
            f"Expected the leftpad of 'hello' with length 10 with char '*' "
            f"to be '*****hello'"
        )

    # Input: _input="hello", _len=5, char="*"
    # Expected Output: "hello"
    def test_normal_operation_with_no_padding_needed(self):
        self.assertEqual(
            "hello",
            leftpad(_input="hello", _len=5, char="*"),
            f"Expected the leftpad of 'hello' with length 5 with char '*' "
            f"to be 'hello'"
        )

    # Input: _input="hello", _len=10, char=None
    # Expected Output: "     hello"
    def test_padding_with_default_character(self):
        self.assertEqual(
            "     hello",
            leftpad(_input="hello", _len=10, char=None),
            f"Expected the leftpad of 'hello' with length 10 and no char provided "
            f"to be '     hello'"
        )

    # Input: _input="hello", _len=10, char=""
    # Expected Output: "hello"
    def test_padding_with_an_empty_string(self):
        self.assertEqual(
            leftpad(_input="hello", _len=10, char=""),
            "hello",
            f"Expected the leftpad of 'hello' with length 10 with empty char "
            f"to be 'hello'"
        )

    # Input: _input = "helloworld!", _len = 5, char = "*"
    # Expected Output: "helloworld!"
    def test_string_is_longer_than_the_specified_length(self):
        self.assertEqual(
            "helloworld!",
            leftpad(_input="helloworld!", _len=5, char="*"),
            f"Expected the leftpad of 'helloworld!' with length 5 with char '*' "
            f"to be 'helloworld!'"
        )

    # Input: _input="negative", _len=-5, char="*"
    # Expected Output: "negative"
    def test_specified_length_is_negative(self):
        self.assertEqual(
            "negative",
            leftpad(_input="negative", _len=-5, char="*"),
            f"Expected the leftpad of 'negative' with length -5 with char '*' "
            f"to be 'negative'"
        )

    # Input: _input = "multi", _len = 10, char = "ab"
    # Expected Output: "aaaaamulti"
    def test_padding_with_a_multi_character_string(self):
        self.assertEqual(
            "aaaaamulti",
            leftpad(_input="multi", _len=10, char="ab"),
            f"Expected the leftpad of 'multi' with length 10 with char 'ab' "
            f"to be 'aaaaamulti'"
        )

    # Input: _input="!@#$%", _len=10, char="*"
    # Expected Output: "*****!@#$%"
    def test_input_string_contains_special_characters(self):
        self.assertEqual(
            "*****!@#$%",
            leftpad(_input="!@#$%", _len=10, char="*"),
            f"Expected the leftpad of '!@#$%' with length 10 with char '*' "
            f"to be '*****!@#$%'"
        )

    # Input: _input="你好", _len=5, char="*"
    # Expected Output: "***你好"
    def test_padding_a_string_that_contains_unicode_characters(self):
        self.assertEqual(
            "***你好",
            leftpad(_input="你好", _len=5, char="*"),
            f"Expected the leftpad of '你好' with length 5 with char '*' "
            f"to be '***你好'"
        )

    # Input: _input="123", _len=5, char="0"
    # Expected Output: "00123"
    def test_padding_a_numeric_string(self):
        self.assertEqual(
            "00123",
            leftpad(_input="123", _len=5, char="0"),
            f"Expected the leftpad of '123' with length 5 with char '0' "
            f"to be '00123'"
        )

    # Input: _input="line", _len=6, char="\n"
    # Expected Output: "\n\nline"
    def test_padding_a_string_with_a_newline_character(self):
        self.assertEqual(
            "\n\nline",
            leftpad(_input="line", _len=6, char="\n"),
            f"Expected the leftpad of 'line' with length 6 with char '\\n' "
            f"to be '\\n\\nline'"
        )

    # Input: _input="hidden", _len=10, char="\x00"
    # Expected Output: "\x00\x00\x00\x00hidden"
    def test_padding_a_string_with_a_non_printable_character(self):
        self.assertEqual(
            "\x00\x00\x00\x00hidden",
            leftpad(_input="hidden", _len=10, char="\x00"),
            f"Expected the leftpad of 'hidden' with length 10 with char '\\x00' "
            f"to be '\\x00\\x00\\x00\\x00hidden'"
        )

    # Input: _input="", _len=5, char="*"
    # Expected Output: "*****"
    def test_empty_input_string(self):
        self.assertEqual(
            "*****",
            leftpad(_input="", _len=5, char="*"),
            f"Expected the leftpad of empty input with length 5 with char '*' "
            f"to be '*****'"
        )

    # Input: _input="zero", _len=0, char="*"
    # Expected Output: "zero"
    def test_zero_length(self):
        self.assertEqual(
            "zero",
            leftpad(_input="zero", _len=0, char="*"),
            f"Expected the leftpad of 'zero' with length 0 with char '*' "
            f"to be 'zero'"
        )

    # Input: _input="number", _len=10, char="1"
    # Expected Output: "1111number"
    def test_padding_with_a_number_as_a_character(self):
        self.assertEqual(
            "1111number",
            leftpad(_input="number", _len=10, char="1"),
            f"Expected the leftpad of 'number' with length 10 with char '1' "
            f"to be '1111number'"
        )

    # Performance test
    def test_performance(self):
        expected = {
            100:    1500000,  # run / sec
            1000:   1000000,
            10000:  700000,
            100000: 100000
        }

        for y in [100, 1000, 10000, 100000]:
            for x in [100, 1000, 10000, 100000]:
                for ch in [None, '*', 'ab']:
                    elapsed = time_this_function(leftpad, x, "I love python", y, ch)
                    self.assertGreater(
                        int(x/elapsed),
                        expected[y],
                        f"Expected the function rightpad to have throughput higher than "
                        f"{expected[y]} run / second, the recorder value was {int(x / elapsed)}.\n"
                        f"The function was run {x} times and completed in {elapsed:0.6f} seconds.\n"
                        f"Input values: _input:'I love python', _len:{y}, char:{ch}"
                    )


class RightPadTests(unittest.TestCase):
    # Input: _input="hello", _len=10, char="*"
    # Expected Output: "hello*****"
    def test_normal_operation_with_padding(self):
        self.assertEqual(
            "hello*****",
            rightpad(_input="hello", _len=10, char="*"),
            f"Expected the rightpad of 'hello' with length 10 with char '*' "
            f"to be 'hello*****'"
        )

    # Input: _input="hello", _len=5, char="*"
    # Expected Output: "hello"
    def test_normal_operation_with_no_padding_needed(self):
        self.assertEqual(
            "hello",
            rightpad(_input="hello", _len=5, char="*"),
            f"Expected the rightpad of 'hello' with length 5 with char '*' "
            f"to be 'hello'"
        )

    # Input: _input="hello", _len=10, char=None
    # Expected Output: "hello     "
    def test_padding_with_default_character(self):
        self.assertEqual(
            "hello     ",
            rightpad(_input="hello", _len=10, char=None),
            f"Expected the rightpad of 'hello' with length 10 with no char provided "
            f"to be 'hello'"
        )

    # Input: _input="hello", _len=10, char=""
    # Expected Output: "hello"
    def test_padding_with_an_empty_string(self):
        self.assertEqual(
            "hello",
            rightpad(_input="hello", _len=10, char=""),
            f"Expected the rightpad of 'hello' with length 10 with empty char provided "
            f"to be 'hello'"
        )

    # Input: _input = "helloworld!", _len = 5, char = "*"
    # Expected Output: "helloworld!"
    def test_string_is_longer_than_the_specified_length(self):
        self.assertEqual(
            "helloworld!",
            rightpad(_input="helloworld!", _len=5, char="*"),
            f"Expected the rightpad of 'helloworld!' with length 5 with char '*' "
            f"to be 'hello'"
        )

    # Input: _input="negative", _len=-5, char="*"
    # Expected Output: "negative"
    def test_specified_length_is_negative(self):
        self.assertEqual(
            "negative",
            rightpad(_input="negative", _len=-5, char="*"),
            f"Expected the rightpad of 'negative' with length -5 with char '*' "
            f"to be 'negative'"
        )

    # Input: _input = "multi", _len = 10, char = "ab"
    # Expected Output: "multiaaaaa"
    def test_padding_with_a_multi_character_string(self):
        self.assertEqual(
            "multiaaaaa",
            rightpad(_input="multi", _len=10, char="ab"),
            f"Expected the rightpad of 'multi' with length 10 with char 'ab' "
            f"to be 'multiaaaaa'"
        )

    # Input: _input="!@#$%", _len=10, char="*"
    # Expected Output: "!@#$%*****"
    def test_input_string_contains_special_characters(self):
        self.assertEqual(
            "!@#$%*****",
            rightpad(_input="!@#$%", _len=10, char="*"),
            f"Expected the rightpad of '!@#$%' with length 10 with char '*' "
            f"to be '!@#$%*****'"
        )

    # Input: _input="你好", _len=5, char="*"
    # Expected Output: "你好***"
    def test_padding_a_string_that_contains_unicode_characters(self):
        self.assertEqual(
            "你好***",
            rightpad(_input="你好", _len=5, char="*"),
            f"Expected the rightpad of '你好' with length 10 with char '*' "
            f"to be '你好***'"
        )

    # Input: _input="123", _len=5, char="0"
    # Expected Output: "00123"
    def test_padding_a_numeric_string(self):
        self.assertEqual(
            "12300",
            rightpad(_input="123", _len=5, char="0"),
            f"Expected the rightpad of '123' with length 10 with char '0' "
            f"to be '12300'"
        )

    # Input: _input="line", _len=6, char="\n"
    # Expected Output: "line\n\n"
    def test_padding_a_string_with_a_newline_character(self):
        self.assertEqual(
            "line\n\n",
            rightpad(_input="line", _len=6, char="\n"),
            f"Expected the rightpad of 'line' with length 6 with char '\\n' "
            f"to be 'line\\n\\n'"
        )

    # Input: _input="hidden", _len=10, char="\x00"
    # Expected Output: "hidden\x00\x00\x00\x00"
    def test_padding_a_string_with_a_non_printable_character(self):
        self.assertEqual(
            "hidden\x00\x00\x00\x00",
            rightpad(_input="hidden", _len=10, char="\x00"),
            f"Expected the rightpad of 'hidden' with length 10 with char '\\x00' "
            f"to be 'hidden\\x00\\x00\\x00\\x00'"
        )

    # Input: _input="", _len=5, char="*"
    # Expected Output: "*****"
    def test_empty_input_string(self):
        self.assertEqual(
            "*****",
            rightpad(_input="", _len=5, char="*"),
            f"Expected the rightpad of empty string with length 5 with char '*' "
            f"to be '*****'"
        )

    # Input: _input="zero", _len=0, char="*"
    # Expected Output: "zero"
    def test_zero_length(self):
        self.assertEqual(
            "zero",
            rightpad(_input="zero", _len=0, char="*"),
            f"Expected the rightpad of 'zero' with length 0 with char '*' "
            f"to be 'zero'"
        )

    # Input: _input="number", _len=10, char="1"
    # Expected Output: "number1111"
    def test_padding_with_a_number_as_a_character(self):
        self.assertEqual(
            "number1111",
            rightpad(_input="number", _len=10, char="1"),
            f"Expected the rightpad of 'number' with length 10 with char '1' "
            f"to be 'number1111'"
        )

    # Performance test
    def test_performance(self):
        expected = {
            100: 1500000,  # run / sec
            1000: 1000000,
            10000: 700000,
            100000: 100000
        }

        for y in [100, 1000, 10000, 100000]:
            for x in [100, 1000, 10000, 100000]:
                for ch in [None, '*', 'ab']:
                    elapsed = time_this_function(rightpad, x, "I love python", y, ch)
                    self.assertGreater(
                        int(x / elapsed),
                        expected[y],
                        f"Expected the function rightpad to have throughput higher than "
                        f"{expected[y]} run / second, the recorder value was {int(x / elapsed)}.\n"
                        f"The function was run {x} times and completed in {elapsed:0.6f} seconds.\n"
                        f"Input values: _input:'I love python', _len:{y}, char:{ch}"
                    )


class TestIsUpperCase(unittest.TestCase):
    # Input: _input="zero"
    # Expected Output: False
    def test_lower_case_string(self):
        self.assertEqual(
            False,
            is_upper_case(_input="zero"),
            "Expected the return value for is_upper_case of 'zero' to be False"
        )

    # Input: _input="ZERO"
    # Expected Output: True
    def test_upper_case_string(self):
        self.assertEqual(
            True,
            is_upper_case(_input="ZERO"),
            "Expected the return value for is_upper_case of 'ZERO' to be True"
        )

    # Input: _input="ZeRo"
    # Expected Output: False
    def test_mixed_case_string(self):
        self.assertEqual(
            False,
            is_upper_case(_input="ZeRo"),
            "Expected the return value for is_upper_case of 'ZeRo' to be False"
        )

    # Input: _input=""
    # Expected Output: True
    def test_empty_string(self):
        self.assertEqual(
            True,
            is_upper_case(_input=""),
            "Expected the return value for is_upper_case of an empty string to be True"
        )

    # Input: _input=None
    # Expected Output: Raises TypeError
    def test_null_input(self):
        with self.assertRaises(TypeError):
            is_upper_case(_input=None)

    # Input: _input="!@#$%"
    # Expected Output: True
    def test_special_characters(self):
        self.assertEqual(
            True,
            is_upper_case(_input="!@#$%"),
            "Expected the return value for is_upper_case of '!@#$%' to be True"
        )

    # Input: _input="12345"
    # Expected Output: True
    def test_numeric_characters(self):
        self.assertEqual(
            True,
            is_upper_case(_input="12345"),
            "Expected the return value for is_upper_case of '12345' to be True"
        )

    # Input: _input="A"*10001
    # Expected Output: True
    def test_long_string(self):
        self.assertEqual(
            True,
            is_upper_case(_input="A" * 10001),
            "Expected the return value for is_upper_case of a string with 10001 'A's to be True"
        )

    # Input: _input="ΔΘΣ"
    # Expected Output: True
    def test_unicode_characters(self):
        self.assertEqual(
            True,
            is_upper_case(_input="ΔΘΣ"),
            "Expected the return value for is_upper_case of 'ΔΘΣ' to be True"
        )


class TestPascalCase(unittest.TestCase):
    # Input: _input="hello world!"
    # Expected Output: "Hello World!"
    def test_lower_case_string(self):
        self.assertEqual(
            "Hello World!",
            pascal_case(_input="hello world!"),
            "Expected the return value for pascal_case of 'hello world!' to be 'Hello World!'"
        )

    # Input: _input="zero"
    # Expected Output: "Zero"
    def test_single_word(self):
        self.assertEqual(
            "Zero",
            pascal_case(_input="zero"),
            "Expected the return value for pascal_case of 'zero' to be 'Zero'"
        )

    # Input: _input=""
    # Expected Output: ""
    def test_empty_string(self):
        self.assertEqual(
            "",
            pascal_case(_input=""),
            "Expected the return value for pascal_case of an empty string to be an empty string"
        )

    # Input: _input="hello_world!"
    # Expected Output: "Hello World!"
    def test_string_with_special_characters(self):
        self.assertEqual(
            "Hello_world!",
            pascal_case(_input="hello_world!"),
            "Expected the return value for pascal_case of 'hello_world!' to be 'Hello_world!'"
        )

    # Input: _input="hello2 world3!"
    # Expected Output: "Hello2 World3!"
    def test_string_with_numbers(self):
        self.assertEqual(
            "Hello2 World3!",
            pascal_case(_input="hello2 world3!"),
            "Expected the return value for pascal_case of 'hello2 world3!' to be 'Hello2 World3!'"
        )

    # Input: _input="hello  world!"
    # Expected Output: "Hello  World!"
    def test_string_with_multiple_spaces(self):
        self.assertEqual(
            "Hello  World!",
            pascal_case(_input="hello  world!"),
            "Expected the return value for pascal_case of 'hello  world!' to be 'Hello  World!'"
        )

    # Input: _input="hello\tworld\n!", separator='\t'
    # Expected Output: "Hello\tWorld\n!"
    def test_string_with_tabs_and_newlines(self):
        self.assertEqual(
            "Hello\tWorld\n!",
            pascal_case(_input="hello\tworld\n!", separator='\t'),
            "Expected the return value for pascal_case of 'hello\tworld\n!' to be 'Hello\tWorld\n!'"
        )

    # Input: _input="héllo wørld!"
    # Expected Output: "Héllo Wørld!"
    def test_string_with_non_english_characters(self):
        self.assertEqual(
            "Héllo Wørld!",
            pascal_case(_input="héllo wørld!"),
            "Expected the return value for pascal_case of 'héllo wørld!' to be 'Héllo Wørld!'"
        )


class TestToggleCase(unittest.TestCase):
    # Input: _input="zEro"
    # Expected Output: "ZeRO"
    def test_mixed_case_string(self):
        self.assertEqual(
            "ZeRO",
            toggle_case(_input="zEro"),
            "Expected the return value for toggle_case of 'zEro' to be 'ZeRO'"
        )

    # Input: _input="HELLO"
    # Expected Output: "hello"
    def test_all_uppercase_string(self):
        self.assertEqual(
            "hello",
            toggle_case(_input="HELLO"),
            "Expected the return value for toggle_case of 'HELLO' to be 'hello'"
        )

    # Input: _input="world"
    # Expected Output: "WORLD"
    def test_all_lowercase_string(self):
        self.assertEqual(
            "WORLD",
            toggle_case(_input="world"),
            "Expected the return value for toggle_case of 'world' to be 'WORLD'"
        )

    # Input: _input=""
    # Expected Output: ""
    def test_empty_string(self):
        self.assertEqual(
            "",
            toggle_case(_input=""),
            "Expected the return value for toggle_case of an empty string to be an empty string"
        )

    # Input: _input=None
    # Expected Output: Raises TypeError
    def test_none_input(self):
        with self.assertRaises(TypeError):
            toggle_case(_input=None)

    # Input: _input="123"
    # Expected Output: "123"
    def test_numeric_string(self):
        self.assertEqual(
            "123",
            toggle_case(_input="123"),
            "Expected the return value for toggle_case of '123' to be '123'"
        )

    # Input: _input="!@#"
    # Expected Output: "!@#"
    def test_special_characters_string(self):
        self.assertEqual(
            "!@#",
            toggle_case(_input="!@#"),
            "Expected the return value for toggle_case of '!@#' to be '!@#'"
        )

    # Input: _input="  "
    # Expected Output: "  "
    def test_whitespace_string(self):
        self.assertEqual(
            "  ",
            toggle_case(_input="  "),
            "Expected the return value for toggle_case of '  ' to be '  '"
        )

    # Input: _input="Python3"
    # Expected Output: "pYTHON3"
    def test_alphanumeric_string(self):
        self.assertEqual(
            "pYTHON3",
            toggle_case(_input="Python3"),
            "Expected the return value for toggle_case of 'Python3' to be 'pYTHON3'"
        )

    # Input: _input="Python Test"
    # Expected Output: "pYTHON tEST"
    def test_string_with_space(self):
        self.assertEqual(
            "pYTHON tEST",
            toggle_case(_input="Python Test"),
            "Expected the return value for toggle_case of 'Python Test' to be 'pYTHON tEST'"
        )


class TestReverseString(unittest.TestCase):

    # Input: _input="Hello"
    # Expected Output: "olleH"
    def test_standard_string(self):
        self.assertEqual(
            "olleH",
            reverse_string(_input="Hello"),
            "Expected the return value for reverse_string of 'Hello' to be 'olleH'"
        )

    # Input: _input="Python"
    # Expected Output: "nohtyP"
    def test_another_standard_string(self):
        self.assertEqual(
            "nohtyP",
            reverse_string(_input="Python"),
            "Expected the return value for reverse_string of 'Python' to be 'nohtyP'"
        )

    # Input: _input=""
    # Expected Output: ""
    def test_empty_string(self):
        self.assertEqual(
            "",
            reverse_string(_input=""),
            "Expected the return value for reverse_string of an empty string to be an empty string"
        )

    # Input: _input=None
    # Expected Output: Raise TypeError
    def test_none_input(self):
        with self.assertRaises(TypeError):
            reverse_string(_input=None)

    # Input: _input="A"
    # Expected Output: "A"
    def test_single_character(self):
        self.assertEqual(
            "A",
            reverse_string(_input="A"),
            "Expected the return value for reverse_string of 'A' to be 'A'"
        )

    # Input: _input="AB"
    # Expected Output: "BA"
    def test_two_characters(self):
        self.assertEqual(
            "BA",
            reverse_string(_input="AB"),
            "Expected the return value for reverse_string of 'AB' to be 'BA'"
        )

    # Input: _input="A man, a plan, a canal: Panama"
    # Expected Output: "amanaP :lanac a ,nalp a ,nam A"
    def test_string_with_punctuation(self):
        self.assertEqual(
            "amanaP :lanac a ,nalp a ,nam A",
            reverse_string(_input="A man, a plan, a canal: Panama"),
            "Expected the return value for reverse_string of "
            "'A man, a plan, a canal: Panama' to be 'amanaP :lanac a ,nalp a ,nam A'"
        )

    # Input: _input="12345"
    # Expected Output: "54321"
    def test_numeric_string(self):
        self.assertEqual(
            "54321",
            reverse_string(_input="12345"),
            "Expected the return value for reverse_string of '12345' to be '54321'"
        )

    # Input: _input="  Hello  "
    # Expected Output: "  olleH  "
    def test_string_with_leading_and_trailing_spaces(self):
        self.assertEqual(
            "  olleH  ",
            reverse_string(_input="  Hello  "),
            "Expected the return value for reverse_string of '  Hello  ' to be '  olleH  '"
        )

    # Input: _input="Hello\nWorld"
    # Expected Output: "dlroW\nolleH"
    def test_string_with_newline_character(self):
        self.assertEqual(
            "dlroW\nolleH",
            reverse_string(_input="Hello\nWorld"),
            "Expected the return value for reverse_string of 'Hello\nWorld' to be 'dlroW\nolleH'"
        )


if __name__ == '__main__':
    unittest.main()
