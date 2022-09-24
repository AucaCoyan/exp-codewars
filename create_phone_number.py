"""
 Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses! """
import re
from typing import List


def create_phone_number(input_ints: List[int]) -> str:
    # convert list into str
    number_list = "".join(str(number) for number in input_ints)
    phone = re.sub(r"(\d{3})(\d{3})(\d{4})", r"(\1) \2-\3", number_list)
    return phone


input = create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(input)
output = "(123) 456-7890"
print(output)
