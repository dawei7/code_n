# Type of Triangle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3024 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [type-of-triangle](https://leetcode.com/problems/type-of-triangle/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/type-of-triangle/).

### Goal
Given an array of three integers representing the lengths of the sides of a potential triangle, determine if the sides can form a valid triangle. If they can, classify the triangle as "equilateral" (all sides equal), "isosceles" (exactly two sides equal), or "scalene" (no sides equal). If the sides cannot form a valid triangle, return "none".

### Function Contract
**Inputs**

- `nums`: A list of three integers representing the side lengths.

**Return value**

- A string: "equilateral", "isosceles", "scalene", or "none".

### Examples
**Example 1**

- Input: `nums = [3, 3, 3]`
- Output: `"equilateral"`

**Example 2**

- Input: `nums = [3, 4, 3]`
- Output: `"isosceles"`

**Example 3**

- Input: `nums = [3, 4, 5]`
- Output: `"scalene"`

---

## Solution
### Approach
The solution relies on the **Triangle Inequality Theorem**, which states that for any triangle, the sum of the lengths of any two sides must be strictly greater than the length of the third side. By sorting the sides such that $a \le b \le c$, we only need to verify that $a + b > c$. Once validity is confirmed, we use set theory or equality comparisons to count the number of unique side lengths to classify the triangle type.

### Complexity Analysis
- **Time Complexity**: $O(1)$. Since the input size is fixed at three elements, sorting and comparisons take constant time.
- **Space Complexity**: $O(1)$. We only use a constant amount of extra space for variables.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> str:
    # Sort the sides to easily check the triangle inequality
    nums.sort()
    a, b, c = nums

    # Triangle Inequality Theorem: sum of two smaller sides must be > largest side
    if a + b <= c:
        return "none"

    # Count unique sides using a set
    unique_sides = len(set(nums))

    if unique_sides == 1:
        return "equilateral"
    elif unique_sides == 2:
        return "isosceles"
    else:
        return "scalene"
```
</details>
