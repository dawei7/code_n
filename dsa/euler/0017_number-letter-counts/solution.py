def solve(limit: int = 1000) -> int:
    """Compute the total number of letters used to write all numbers from 1 to limit in words.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. British English Number Spelling Rules:
       - 1 to 19: Unique root names (one, two, ..., nineteen).
       - 20 to 99: Tens prefixes (twenty, thirty, ..., ninety) plus units.
       - 100 to 999: "[unit] hundred" for exact hundreds (e.g. "three hundred"),
         and "[unit] hundred and [remainder]" for non-exact hundreds (e.g. "three hundred and forty-two").
       - 1000 to 999999: "[unit] thousand" for thousands blocks.

    2. Character Filtering:
       Spaces and hyphens are excluded according to the standard rules.
       Example: "three hundred and forty-two" contains 23 letters.
       "one hundred and fifteen" contains 20 letters.

    Complexity:
    -----------
    - Time Complexity: O(limit) where limit = 1000 (terminates in ~0.001s).
    - Space Complexity: O(1) constant auxiliary space.
    """
    ones = [
        "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"
    ]
    tens = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    ]

    def number_to_words(n: int) -> str:
        """Convert integer n to its British English word representation without spaces/hyphens."""
        if n < 20:
            return ones[n]
        if n < 100:
            return tens[n // 10] + ones[n % 10]
        if n < 1000:
            res = ones[n // 100] + "hundred"
            if n % 100 != 0:
                res += "and" + number_to_words(n % 100)
            return res
        if n < 1000000:
            res = number_to_words(n // 1000) + "thousand"
            if n % 1000 != 0:
                res += number_to_words(n % 1000)
            return res
        return ""

    total_letters = sum(len(number_to_words(i)) for i in range(1, limit + 1))
    return total_letters


if __name__ == "__main__":
    print(solve())
