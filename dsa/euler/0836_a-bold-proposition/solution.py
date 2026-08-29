"""Project Euler Problem 836: A Bold Proposition.

Problem Analysis:
This problem was published on April 1, 2023 (as indicated by the input parameter 20230401).
The mathematical jargon is an April Fools' puzzle.
The task instructs: "Give as your answer the concatenation of the first letters of each bolded word."

The bolded mathematical keywords in the original problem statement are:
1.  **a**ffine
2.  **p**lane
3.  **r**adically
4.  **i**ntegral
5.  **l**ocal
6.  **f**ield
7.  **o**pen
8.  **o**riented
9.  **l**ine
10. **s**ection
11. **j**acobian
12. **o**rthogonal
13. **k**ernel
14. **e**mbedding

Extracting the initial letters:
a-p-r-i-l-f-o-o-l-s-j-o-k-e -> 'aprilfoolsjoke'.
"""

from __future__ import annotations


def solve() -> str:
    """Extract and concatenate the first letter of each bolded word in the problem text."""
    bolded_terms = [
        "affine",
        "plane",
        "radically",
        "integral",
        "local",
        "field",
        "open",
        "oriented",
        "line",
        "section",
        "jacobian",
        "orthogonal",
        "kernel",
        "embedding",
    ]

    letters = [term[0].lower() for term in bolded_terms]
    return "".join(letters)


if __name__ == "__main__":
    print(solve())
