# Maximum Strong Pair XOR II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2935 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Bit Manipulation, Trie, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-strong-pair-xor-ii](https://leetcode.com/problems/maximum-strong-pair-xor-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-strong-pair-xor-ii/).

### Goal
Given an array of integers, identify all "strong pairs" (x, y) such that the absolute difference between the two numbers is less than or equal to the smaller of the two (i.e., |x - y| ≤ min(x, y)). Among all such pairs, determine the maximum possible value of the bitwise XOR operation (x ^ y).

### Function Contract
**Inputs**

- `nums`: A list of non-negative integers.

**Return value**

- An integer representing the maximum XOR value achievable by any strong pair in the input array.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4, 5]`
- Output: `7`
- Explanation: Strong pairs include (2, 3) where |2-3| <= 2, (4, 5) where |4-5| <= 4, etc. The max XOR is 3 ^ 5 = 6, or 2 ^ 5 = 7.

**Example 2**

- Input: `nums = [10, 20]`
- Output: `0`
- Explanation: |10 - 20| = 10. min(10, 20) = 10. Since 10 <= 10, (10, 20) is a strong pair. 10 ^ 20 = 30.

**Example 3**

- Input: `nums = [5, 6, 25, 30]`
- Output: `7`

---

## Solution
### Approach
The problem is solved using a **Trie (Prefix Tree)** combined with a **Sliding Window** approach. By sorting the array, the condition `|x - y| <= min(x, y)` simplifies to `y <= 2 * x` (assuming `x <= y`). As we iterate through the sorted array with a pointer `y`, we maintain a sliding window of valid `x` values in the Trie. We remove elements from the Trie that no longer satisfy the condition as `y` increases, and query the Trie for the value that maximizes the XOR with the current `y`.

### Complexity Analysis
- **Time Complexity**: `O(N * log(max(nums)))`, where `N` is the length of the array. Sorting takes `O(N log N)`, and for each element, we perform constant-time Trie insertions and queries proportional to the number of bits (approx. 20).
- **Space Complexity**: `O(N * log(max(nums)))` to store the Trie nodes.

### Reference Implementations
<details>
<summary>python</summary>

```python
class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.count = 0

def insert(root, num):
    node = root
    for i in range(19, -1, -1):
        bit = (num >> i) & 1
        if not node.children[bit]:
            node.children[bit] = TrieNode()
        node = node.children[bit]
        node.count += 1

def remove(root, num):
    node = root
    for i in range(19, -1, -1):
        bit = (num >> i) & 1
        node = node.children[bit]
        node.count -= 1

def get_max_xor(root, num):
    node = root
    res = 0
    for i in range(19, -1, -1):
        bit = (num >> i) & 1
        target = 1 - bit
        if node.children[target] and node.children[target].count > 0:
            res |= (1 << i)
            node = node.children[target]
        elif node.children[bit] and node.children[bit].count > 0:
            node = node.children[bit]
        else:
            return 0
    return res

def solve(nums):
    nums.sort()
    root = TrieNode()
    max_xor = 0
    left = 0

    for right in range(len(nums)):
        insert(root, nums[right])

        while nums[left] * 2 < nums[right]:
            remove(root, nums[left])
            left += 1

        max_xor = max(max_xor, get_max_xor(root, nums[right]))

    return max_xor
```
</details>
