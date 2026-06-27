from typing import List

def solve(words: List[str], x: str) -> List[int]:
    """
    Returns a list of indices of words that contain the character x.
    """
    result = []
    for index, word in enumerate(words):
        if x in word:
            result.append(index)
    return result
