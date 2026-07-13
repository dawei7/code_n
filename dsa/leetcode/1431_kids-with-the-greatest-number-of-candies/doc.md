# Kids With the Greatest Number of Candies

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1431 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [kids-with-the-greatest-number-of-candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/).

### Goal
For each child, decide whether giving them all `extraCandies` would make their candy count at least as large as every other child's count.

### Function Contract
**Inputs**

- `candies`: each child's current candy count.
- `extraCandies`: candies that can be given to one child for the check.

**Return value**

A boolean list where each entry says whether that child can reach the greatest count.

### Examples
**Example 1**

- Input: `candies = [2,3,5,1,3], extraCandies = 3`
- Output: `[true,true,true,false,true]`

**Example 2**

- Input: `candies = [4,2,1,1,2], extraCandies = 1`
- Output: `[true,false,false,false,false]`

**Example 3**

- Input: `candies = [12,1,12], extraCandies = 10`
- Output: `[true,false,true]`

---

## Solution
### Approach
Single-pass comparison against the maximum existing candy count.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` for the returned list.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(candies, extra_candies):
    best = max(candies) if candies else 0
    return [candy + extra_candies >= best for candy in candies]
```
</details>
