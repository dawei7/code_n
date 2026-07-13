# Unique 3-Digit Even Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3483 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Recursion, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [unique-3-digit-even-numbers](https://leetcode.com/problems/unique-3-digit-even-numbers/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/unique-3-digit-even-numbers/).

### Goal
Given a collection of digits (provided as an array), determine all possible unique 3-digit even integers that can be formed by selecting three digits from the input. The resulting numbers must not have a leading zero and must be returned in ascending order.

### Function Contract
**Inputs**

- `digits`: A list of integers representing the available digits (0-9).

**Return value**

- A sorted list of unique integers, each being a 3-digit even number formed using the provided digits.

### Examples
**Example 1**

- Input: `[2, 1, 3, 0]`
- Output: `[102, 120, 132, 302, 312, 320]`

**Example 2**

- Input: `[2, 2, 8, 8, 2]`
- Output: `[222, 228, 282, 288, 822, 828, 882]`

**Example 3**

- Input: `[3, 7, 5]`
- Output: `[]`

---

## Solution
### Approach
The problem is solved using frequency counting (Hash Map/Array) to track the availability of each digit (0-9). Since we only need to form 3-digit numbers, we iterate through all possible even 3-digit numbers (100 to 998 with a step of 2). For each candidate number, we verify if it can be constructed using the available digit counts.

### Complexity Analysis
- **Time Complexity**: O(1). The range of 3-digit numbers is fixed (100-999), making the loop constant time. Digit frequency counting takes O(N) where N is the length of the input array.
- **Space Complexity**: O(1). The frequency map stores at most 10 digits, and the output list is bounded by the number of 3-digit integers.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter

def solve(digits: list[int]) -> int:
    # Count the frequency of each available digit
    counts = Counter(digits)
    result = []

    # Iterate through all possible 3-digit even numbers
    # A 3-digit number ranges from 100 to 999.
    for num in range(100, 1000, 2):
        # Extract digits of the current number
        d1 = num // 100
        d2 = (num // 10) % 10
        d3 = num % 10

        # Check if we have enough of each digit to form this number
        temp_counts = Counter([d1, d2, d3])

        possible = True
        for digit, freq in temp_counts.items():
            if counts[digit] < freq:
                possible = False
                break

        if possible:
            result.append(num)

    return len(result)
```
</details>
