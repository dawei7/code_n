# Minimum Cost to Make Array Equalindromic

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2967 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Binary Search, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-cost-to-make-array-equalindromic](https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/).

### Goal
Given an array of integers, determine the minimum total cost to transform every element in the array into the same palindromic number. The cost of changing a number $x$ to a target palindrome $p$ is defined as $|x - p|$.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`) representing the input array.

**Return value**

- An integer representing the minimum total cost to make all elements equal to some palindrome.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `2`
- Explanation: We can make all elements equal to 2 (which is a palindrome). Cost: |1-2| + |2-2| + |3-2| = 1 + 0 + 1 = 2.

**Example 2**

- Input: `nums = [10, 12, 13]`
- Output: `2`
- Explanation: We can make all elements equal to 11. Cost: |10-11| + |12-11| + |13-11| = 1 + 1 + 2 = 4. Wait, 11 is a palindrome. Cost is |10-11| + |12-11| + |13-11| = 1 + 1 + 2 = 4. Actually, 11 is the best choice.

**Example 3**

- Input: `nums = [22, 33, 22]`
- Output: `22`
- Explanation: Making all elements 22 costs |22-22| + |33-22| + |22-22| = 11.

---

## Solution
### Approach
The problem relies on the property that the optimal target value for a set of numbers to minimize the sum of absolute differences is the median. Since the target must be a palindrome, we identify the median of the array, find the closest palindromes to that median, and evaluate the cost for each candidate to find the global minimum.

### Complexity Analysis
- **Time Complexity**: $O(N \log N)$ due to sorting the array to find the median, where $N$ is the number of elements. Palindrome generation and cost calculation are $O(N \cdot \log(\max(nums)))$.
- **Space Complexity**: $O(1)$ (excluding the input array storage), as we only store a few candidate palindromes.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    nums.sort()
    n = len(nums)
    median = nums[n // 2]

    def is_palindrome(n: int) -> bool:
        s = str(n)
        return s == s[::-1]

    def get_candidates(val: int) -> list[int]:
        s = str(val)
        length = len(s)
        candidates = set()

        # Add edge cases: 10^(n-1) - 1 and 10^n + 1
        candidates.add(10**(length - 1) - 1)
        candidates.add(10**length + 1)

        # Generate palindromes by modifying the prefix
        prefix = int(s[:(length + 1) // 2])
        for i in [-1, 0, 1]:
            p = str(prefix + i)
            if length % 2 == 0:
                res = p + p[::-1]
            else:
                res = p + p[:-1][::-1]
            candidates.add(int(res))

        return [c for c in candidates if c > 0]

    candidates = get_candidates(median)

    min_cost = float('inf')
    for cand in candidates:
        current_cost = sum(abs(x - cand) for x in nums)
        if current_cost < min_cost:
            min_cost = current_cost

    return int(min_cost)
```
</details>
