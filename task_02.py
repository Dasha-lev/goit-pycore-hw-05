import re
from typing import Callable, Generator

# Function generator_numbers takes a text and returns a generator of numbers
def generator_numbers(text: str) -> Generator[float, None, None]:
    # A regular expression to find numbers in the text.
    pattern = r'\b\d+\.\d+\b'
    # Find all numbers using the regular expression.
    matches = re.findall(pattern, text)
    # Iterate over the found numbers
    for match in matches:
        # Convert each found number to a float and return it.
        yield float(match)

# Function sum_profit takes a text and a generator function, and returns the sum of the numbers
def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    # Use the generator function to get the numbers from the text
    numbers = func(text)
    # Sum all the numbers and return the result
    return sum(numbers)

text = "The total income of an employee consists of several parts: 1000.01 as the base income, supplemented by additional revenues of 27.45 and 324.00 dollars."
total_income = sum_profit(text, generator_numbers)
print(f"the total income: {total_income}")  