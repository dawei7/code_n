from typing import List

def solve(words: List[str], separator: str) -> List[str]:
    """
    Splits each string in the list by the given separator and returns
    a flattened list of all non-empty substrings.
    """
    result = []
    for word in words:
        # Split the string by the separator
        parts = word.split(separator)
        # Filter out empty strings and extend the result list
        for part in parts:
            if part:
                result.append(part)
    return result
