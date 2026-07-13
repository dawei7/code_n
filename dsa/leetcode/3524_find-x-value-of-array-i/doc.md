# Find X Value of Array I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3524 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-x-value-of-array-i](https://leetcode.com/problems/find-x-value-of-array-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-x-value-of-array-i/).

### Goal
Given an array of integers, determine the "X-value," which is defined as the maximum possible result of a bitwise XOR operation performed on a non-empty subarray. The goal is to identify the subarray that yields the highest XOR sum.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`) where each element is non-negative.

**Return value**

- An integer representing the maximum XOR sum achievable from any contiguous subarray of `nums`.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `3`
- Explanation: Subarrays are [1], [2], [3], [1,2]=3, [2,3]=1, [1,2,3]=0. Max is 3.

**Example 2**

- Input: `nums = [5, 2, 4, 6]`
- Output: `7`
- Explanation: The subarray [5, 2] gives 7 (5 XOR 2 = 7).

**Example 3**

- Input: `nums = [10, 1, 10]`
- Output: `11`
- Explanation: The subarray [10, 1] gives 11.

---

## Solution
### Approach
The problem utilizes the property of prefix XORs: the XOR sum of a subarray `nums[i...j]` can be calculated as `prefix[j] ^ prefix[i-1]`, where `prefix[k]` is the XOR sum of `nums[0...k]`. To find the maximum XOR of any two prefix XOR values, a **Trie (Prefix Tree)** data structure is used to store binary representations of prefix XORs, allowing for efficient querying of the maximum XOR pair in $O(N \cdot \text{bits})$ time.

### Complexity Analysis
- **Time Complexity**: $O(N \cdot W)$, where $N$ is the length of the array and $W$ is the number of bits (typically 32). We iterate through the array once and perform constant-time operations per bit.
- **Space Complexity**: $O(N \cdot W)$ to store the Trie nodes.

### Reference Implementations
<details>
<summary>python</summary>

```python
class TrieNode:
    def __init__(self):
        self.children = {}

def insert(root, val):
    node = root
    for i in range(31, -1, -1):
        bit = (val >> i) & 1
        if bit not in node.children:
            node.children[bit] = TrieNode()
        node = node.children[bit]

def query(root, val):
    node = root
    res = 0
    for i in range(31, -1, -1):
        bit = (val >> i) & 1
        target = 1 - bit
        if target in node.children:
            res |= (1 << i)
            node = node.children[target]
        else:
            node = node.children.get(bit, node)
    return res

def solve(nums: list[int]) -> int:
    root = TrieNode()
    insert(root, 0)

    max_xor = 0
    current_prefix = 0

    for num in nums:
        current_prefix ^= num
        insert(root, current_prefix)
        max_xor = max(max_xor, query(root, current_prefix))

    return max_xor
```
</details>
