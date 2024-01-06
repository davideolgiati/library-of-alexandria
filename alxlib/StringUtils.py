import concurrent.futures
from typing import Union

# cache results on static-ish function for better perf under the hood
from functools import lru_cache


# Substring: Python does not have a built-in function to extract a substring from a string given the
# start and end indices. This operation can be performed using slicing, but a dedicated function could provide a more
# intuitive interface.
#
# String Interpolation: Python's built-in string formatting capabilities are powerful,
# but they can be complex and difficult to use for simple string interpolation tasks. Some other languages provide
# simpler string interpolation functions that can be easier to use for basic tasks.
#
# String Splitting and Joining:
# Python's built-in split and join methods are powerful, but they can be complex and difficult to use for simple
# tasks. Some other languages provide simpler functions for splitting a string into a list of substrings based on a
# delimiter, or joining a list of strings into a single string with a delimiter.
#
# String Replacement: Python's built-in replace method can replace
# all occurrences of a substring with another substring, but there is no built-in function to replace only the first
# occurrence or the last occurrence of a substring.
#
# String Trimming: Python's built-in strip method can remove
# leading and trailing whitespace from a string, but there is no built-in function to remove only leading whitespace
# or only trailing whitespace.
#
# String Testing: Python's built-in string methods can test if a string is all upper
# case, all lower case, or all digits, but there are no built-in functions to test if a string is all letters,
# all alphanumeric characters, or all printable characters.
#
# String Encoding and Decoding: Python's built-in string
# methods can encode a string into bytes using a specified encoding, and decode bytes into a string using a specified
# encoding, but there are no built-in functions to encode a string into a specific format (such as Base64 or URL
# encoding) or decode a string from a specific format.

# These are just a few examples of useful string operations that are not included in Python's standard library. There
# are many more possibilities, depending on the specific needs of your application.


@lru_cache(maxsize=128)
def leftpad(_input: str, _len: int, char: Union[str, None] = ' ') -> str:
    """
    Left pad a string with a specified character up to a given length.

    Parameters:
        _input (str): The input string to be padded.
        _len (int): The target length of the padded string.
        char (Union[str, None], optional): The character used for padding. Defaults to ' '.

    Returns:
        str: The left-padded string.

    Example:
        leftpad("hello", 8) returns "hello   "
        leftpad("123", 5, char='0') returns "12300"
    """
    # Handle the case where char is an empty string
    if char == "":
        return _input

    # If char is None, set it to a space character
    if char is None:
        char = ' '

    # Calculate the size of padding needed
    pad_size = _len - len(_input)

    # If no padding is needed, return the original input
    if pad_size < 1:
        return _input
    else:
        # Left pad the input with the specified character
        return pad_size * char[0] + _input


@lru_cache(maxsize=128)
def rightpad(_input: str, _len: int, char: Union[str, None] = ' ') -> str:
    """
    Right pad a string with a specified character up to a given length.

    Parameters:
        _input (str): The input string to be padded.
        _len (int): The target length of the padded string.
        char (Union[str, None], optional): The character used for padding. Defaults to ' '.

    Returns:
        str: The right-padded string.

    Example:
        rightpad("hello", 8) returns "hello   "
        rightpad("123", 5, char='0') returns "12300"
    """
    # Handle the case where char is an empty string
    if char == "":
        return _input

    # If char is None, set it to a space character
    if char is None:
        char = ' '

    # Calculate the size of padding needed
    pad_size = _len - len(_input)

    # If no padding is needed, return the original input
    if pad_size < 1:
        return _input
    else:
        # Right pad the input with the specified character
        return _input + pad_size * char[0]


@lru_cache(maxsize=128)
def is_upper_case(_input: Union[str, None]) -> bool:
    """
    Check if a string is in uppercase.

    Parameters:
        _input (Union[str, None]): The input string to be checked.

    Returns:
        bool: True if the string is in uppercase, False otherwise.

    Raises:
        TypeError: If the input is None.

    Example:
        is_upper_case("HELLO") returns True
        is_upper_case("Hello") returns False
    """
    # Check if the input is None, raise TypeError if so
    if _input is None:
        raise TypeError

    # Check if the input is empty or contains only whitespace, return True
    if _input in ['', ' ']:
        return True

    # Check if the first character of the input is in lowercase
    if _input[0].upper() != _input[0]:
        return False

    # Check if the entire input string in uppercase is equal to the original input
    return _input.upper() == _input


def pascal_case(_input: str, separator: Union[str, None] = ' ') -> str:
    """
    Converts a string to PascalCase.

    Parameters:
        _input (str): The input string to be converted.
        separator (Union[str, None], optional): The separator between words in the input string. Defaults to ' '.

    Returns:
        str: The PascalCase representation of the input string.

    Note:
        If the input string is empty or contains only whitespace, the function returns the input unchanged.

    Example:
        pascal_case("hello world") returns "HelloWorld"
        pascal_case("hello_world", separator="_") returns "HelloWorld"
    """
    # Check if the input is empty or contains only whitespace
    if _input in ['', ' ', None]:
        return _input

    # Split the input string into words using the specified separator
    tmp = _input.split(separator)

    # Use a ThreadPoolExecutor to concurrently apply the transformation to each word
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Map function to capitalize the first letter and lowercase the rest for each word
        results = list(
            executor.map(
                lambda a: a if a == '' else a[0].upper() + a[1:].lower(),
                tmp
            )
        )

    # Join the transformed words using the separator
    return separator.join([result for result in results])


def toggle_case(_input: Union[str, None]) -> str:
    if _input is None:
        raise TypeError

    if _input in ['', ' ']:
        return _input

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(
            executor.map(
                lambda a: a.lower() if a.upper() == a else a.upper(),
                list(_input)
            )
        )

    return ''.join([result for result in results])


def reverse_string(_input: Union[str, None]) -> str:
    if _input is None:
        raise TypeError

    if _input in ['', ' '] or len(_input) == 1:
        return _input

    return _input[::-1]
