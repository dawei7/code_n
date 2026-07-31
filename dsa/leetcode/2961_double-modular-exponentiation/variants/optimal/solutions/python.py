from typing import List


def solve(variables: List[List[int]], target: int) -> List[int]:
    return [
        index
        for index, (a, b, c, modulus) in enumerate(variables)
        if pow(pow(a, b, 10), c, modulus) == target
    ]
