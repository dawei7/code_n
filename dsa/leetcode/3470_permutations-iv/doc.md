# Permutations IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3470 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Combinatorics, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [permutations-iv](https://leetcode.com/problems/permutations-iv/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/permutations-iv/).

### Goal
Given an integer `n` and a 64-bit integer `k`, return the `k`-th lexicographically smallest permutation of the sequence `[1, 2, ..., n]`. The permutation should be represented as a list of integers. Note that `k` is 1-indexed.

### Function Contract
**Inputs**

- `n`: An integer representing the range of numbers from 1 to `n`.
- `k`: A 64-bit integer representing the rank of the desired permutation.

**Return value**

- A list of integers representing the `k`-th lexicographical permutation.

### Examples
**Example 1**

- Input: `n = 3, k = 3`
- Output: `[2, 1, 3]`

**Example 2**

- Input: `n = 4, k = 9`
- Output: `[2, 3, 1, 4]`

**Example 3**

- Input: `n = 3, k = 1`
- Output: `[1, 2, 3]`

---

## Solution
### Approach
The problem is solved using the **Factorial Number System (Factoradic)**. Since there are `(n-1)!` permutations starting with any specific digit, we can determine the first digit by calculating `(k-1) // (n-1)!`. We then update `k` to `(k-1) % (n-1)!` and repeat the process for the remaining `n-1` elements, maintaining a list of available numbers to pick from.

### Complexity Analysis
- **Time Complexity**: `O(n^2)` due to the list deletion operation `pop(index)` inside the loop, which takes `O(n)` time, repeated `n` times.
- **Space Complexity**: `O(n)` to store the list of available numbers and the resulting permutation.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(n: int, k: int) -> list[int]:
    cap = 10**18
    factorial = [1] * (n + 1)
    for value in range(1, n + 1):
        factorial[value] = min(cap, factorial[value - 1] * value)

    def count_with_next(odd_count: int, even_count: int, next_parity: int) -> int:
        length = odd_count + even_count
        next_slots = (length + 1) // 2
        other_slots = length // 2
        required_odd = next_slots if next_parity == 1 else other_slots
        required_even = length - required_odd
        if odd_count != required_odd or even_count != required_even:
            return 0
        return min(cap, factorial[odd_count] * factorial[even_count])

    numbers = list(range(1, n + 1))
    odd_count = (n + 1) // 2
    even_count = n // 2
    answer: list[int] = []
    previous_parity: int | None = None

    while numbers:
        chosen = False
        for index, value in enumerate(numbers):
            parity = value & 1
            if previous_parity is not None and parity == previous_parity:
                continue
            next_odd = odd_count - parity
            next_even = even_count - (1 - parity)
            ways = (
                count_with_next(next_odd, next_even, 1 - parity)
                if next_odd + next_even
                else 1
            )
            if k > ways:
                k -= ways
                continue
            answer.append(value)
            numbers.pop(index)
            odd_count = next_odd
            even_count = next_even
            previous_parity = parity
            chosen = True
            break
        if not chosen:
            return []
    return answer
```
</details>
