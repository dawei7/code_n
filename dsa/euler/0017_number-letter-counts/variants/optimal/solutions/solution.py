ONESTR = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
           "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENSSTR = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def number_to_words(n: int) -> str:
    if n < 20:
        return ONESTR[n]
    elif n < 100:
        return TENSSTR[n // 10] + ONESTR[n % 10]
    elif n < 1000:
        res = ONESTR[n // 100] + "hundred"
        if n % 100 != 0:
            res += "and" + number_to_words(n % 100)
        return res
    elif n == 1000:
        return "onethousand"
    return ""


def solve(limit: int = 1000) -> int:
    """Find total letter count for numbers 1 to limit in English.
    
    Time Complexity: O(limit)
    Space Complexity: O(1)
    """
    return sum(len(number_to_words(i)) for i in range(1, limit + 1))
