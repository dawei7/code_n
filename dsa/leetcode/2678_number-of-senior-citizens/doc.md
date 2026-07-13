# Number of Senior Citizens

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2678 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-senior-citizens](https://leetcode.com/problems/number-of-senior-citizens/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-senior-citizens/).

### Goal
Given a list of strings, where each string represents a passenger's details, determine and return the total count of passengers who are considered "senior citizens". A passenger is a senior citizen if their age, which is encoded as a two-digit number at specific character positions within their detail string, is strictly greater than 60.

### Function Contract
**Inputs**

- `details`: A `List[str]`, where each string `details[i]` is exactly 15 characters long. The passenger's age is represented by the characters at indices 11 and 12 (0-indexed) of each string.

**Return value**

- An `int` representing the total number of senior citizens found in the `details` list.

### Examples
**Example 1**

- Input: `details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]`
- Output: `2`
- Explanation:
    - "7868190130M**75**22": Age is 75. 75 > 60, so this is a senior citizen.
    - "5303914400F**92**11": Age is 92. 92 > 60, so this is a senior citizen.
    - "9273338290F**40**10": Age is 40. 40 is not > 60, so not a senior citizen.
    - Total senior citizens: 2.

**Example 2**

- Input: `details = ["1313579440F2036", "2921522980M5644"]`
- Output: `0`
- Explanation:
    - "1313579440F**20**36": Age is 20. Not a senior citizen.
    - "2921522980M**56**44": Age is 56. Not a senior citizen.
    - Total senior citizens: 0.

**Example 3**

- Input: `details = ["0000000000M6100"]`
- Output: `1`
- Explanation:
    - "0000000000M**61**00": Age is 61. 61 > 60, so this is a senior citizen.
    - Total senior citizens: 1.

---

## Solution
### Approach
The problem primarily involves iterating through a list of strings and performing basic string manipulation and type conversion for each element.
1.  **Iteration**: A simple loop (e.g., `for` loop) is used to process each passenger detail string in the input list.
2.  **String Slicing**: For each string, a substring representing the age is extracted using string slicing based on the specified start and end indices.
3.  **Type Conversion**: The extracted age substring (which is a string) is converted into an integer to allow for numerical comparison.
4.  **Conditional Counting**: An `if` statement checks if the converted age meets the "senior citizen" criterion (age > 60), and a counter is incremented accordingly.

### Complexity Analysis
- **Time Complexity**: `O(N)`
    - Where `N` is the number of passenger detail strings in the `details` list.
    - The algorithm iterates through each of the `N` strings exactly once.
    - For each string, operations like string slicing (to extract a fixed-length substring), string-to-integer conversion, and integer comparison take constant time, as the length of the age substring is fixed (2 characters).
    - Therefore, the total time complexity is directly proportional to the number of strings.
- **Space Complexity**: `O(1)`
    - The algorithm uses a constant amount of extra space regardless of the input size.
    - A single integer variable is used to store the count of senior citizens. No auxiliary data structures that grow with `N` are created.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(details: List[str]) -> int:
    """
    Counts the number of senior citizens from a list of passenger detail strings.

    A passenger is considered a senior citizen if their age, extracted from
    indices 11 and 12 of their detail string, is strictly greater than 60.

    Args:
        details: A list of strings, where each string is 15 characters long
                 and contains passenger information.

    Returns:
        The total count of senior citizens.
    """
    senior_citizens_count = 0

    for passenger_detail in details:
        # Extract the age substring from indices 11 and 12 (inclusive)
        # Python slicing [11:13] extracts characters at index 11 and 12.
        age_str = passenger_detail[11:13]

        # Convert the age string to an integer
        age = int(age_str)

        # Check if the passenger is a senior citizen (age strictly greater than 60)
        if age > 60:
            senior_citizens_count += 1

    return senior_citizens_count
```
</details>
