# Find the Most Common Response

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3527 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-most-common-response](https://leetcode.com/problems/find-the-most-common-response/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-most-common-response/).

### Goal
Given a list of strings representing user responses, identify the string that appears with the highest frequency. If multiple strings share the same maximum frequency, return the one that is lexicographically smallest.

### Function Contract
**Inputs**

- `responses`: A list of strings (`List[str]`) representing the collected responses.

**Return value**

- A string (`str`) representing the most frequent response, or the lexicographically smallest one in case of a tie.

### Examples
**Example 1**

- Input: `["apple", "banana", "apple", "cherry", "banana"]`
- Output: `"apple"`

**Example 2**

- Input: `["cat", "dog", "cat", "dog"]`
- Output: `"cat"`

**Example 3**

- Input: `["a", "b", "c", "a", "b", "c"]`
- Output: `"a"`

---

## Solution
### Approach
The problem is solved using a Hash Map (dictionary in Python) to perform frequency counting. By iterating through the list once, we build a mapping of strings to their respective counts. We then iterate through the map to find the key with the maximum value, applying a tie-breaking condition based on lexicographical order.

### Complexity Analysis
- **Time Complexity**: `O(N * K)`, where `N` is the number of responses and `K` is the average length of a string. We iterate through the list once to count and once through the unique keys to find the maximum.
- **Space Complexity**: `O(N * K)` to store the frequency map containing all unique strings.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter
from typing import List

def solve(responses: List[str]) -> str:
    if not responses:
        return ""

    # Count the frequency of each response
    counts = Counter(responses)

    # Initialize variables to track the best response
    most_common_response = ""
    max_count = -1

    # Iterate through the dictionary to find the most frequent
    # and lexicographically smallest string
    for response, count in counts.items():
        if count > max_count:
            max_count = count
            most_common_response = response
        elif count == max_count:
            if response < most_common_response:
                most_common_response = response

    return most_common_response
```
</details>
