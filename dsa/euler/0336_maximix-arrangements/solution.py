"""Project Euler 336: Maximix Arrangements

Find the 2011th lexicographic maximix arrangement for eleven carriages.
"""

from __future__ import annotations


def solve(num_carriages: int = 11, target_rank: int = 2011) -> str:
    """Finds the target_rank-th (1-indexed) lexicographic maximix arrangement for num_carriages

    by working backwards from the sorted state.
    """
    n = num_carriages

    # Base state at step n - 2: the last two carriages are reversed
    curr_list: list[list[int]] = [
        [i for i in range(n - 2)] + [n - 1, n - 2]
    ]

    # Apply reverse shunting moves backwards from i = n - 3 down to 0
    for i in range(n - 3, -1, -1):
        next_list: list[list[int]] = []
        for arr in curr_list:
            # 1. Reverse suffix from i to n - 1
            arr1 = arr[:i] + arr[i:][::-1]
            # 2. For each valid pivot j in i + 1 .. n - 2, reverse suffix from j to n - 1
            for j in range(i + 1, n - 1):
                arr2 = arr1[:j] + arr1[j:][::-1]
                next_list.append(arr2)
        curr_list = next_list

    # Convert numeric permutations to alphabetical strings and sort lexicographically
    arrangements = [
        "".join(chr(ord("A") + x) for x in arr) for arr in curr_list
    ]
    arrangements.sort()
    return arrangements[target_rank - 1]


if __name__ == "__main__":
    print(solve())
