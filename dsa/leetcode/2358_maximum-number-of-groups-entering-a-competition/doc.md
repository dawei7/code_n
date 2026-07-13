# Maximum Number of Groups Entering a Competition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2358 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Binary Search, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-number-of-groups-entering-a-competition](https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/).

### Goal
Given an array of positive integers `grades` representing student grades, we want to partition the students into the maximum possible number of groups $k$ such that:
1. The sum of grades in group $i$ is strictly less than the sum of grades in group $i+1$ for all $1 \le i < k$.
2. The number of students in group $i$ is strictly less than the number of students in group $i+1$ for all $1 \le i < k$.

Return the maximum number of groups that can be formed.

### Function Contract
**Inputs**

- `grades`: `List[int]` - An array of positive integers representing the grades of the students.

**Return value**

- `int` - The maximum number of groups that can be formed under the given conditions.

### Examples
**Example 1**

- Input: `grades = [10, 6, 12, 7, 3, 5]`
- Output: `3`
- Explanation: We can form 3 groups:
  - Group 1: `[3]` (sum = 3, size = 1)
  - Group 2: `[5, 6]` (sum = 11, size = 2)
  - Group 3: `[7, 10, 12]` (sum = 29, size = 3)
  This satisfies both conditions: sums (3 < 11 < 29) and sizes (1 < 2 < 3).

**Example 2**

- Input: `grades = [8, 8]`
- Output: `1`
- Explanation: We can only form 1 group of size 1. We cannot form 2 groups because the second group would need at least 2 students, requiring 3 students in total.

**Example 3**

- Input: `grades = [47, 2, 18, 46, 8, 32, 45, 19, 23, 4, 12]`
- Output: `4`
- Explanation: With 11 students, we can form 4 groups of sizes 1, 2, 3, and 5 (or 1, 2, 3, 4 with 1 left over). The sum of sizes is $1+2+3+5 = 11$ or $1+2+3+4 = 10 \le 11$.

---

## Solution
### Approach
The problem can be simplified using a **Greedy** approach and **Mathematics**.

Since all grades are positive, if we sort the grades in ascending order, we can greedily place the smallest elements in the first group, the next smallest in the second group, and so on. Because the elements are sorted and positive, a group of size $i+1$ containing larger elements will always have a strictly greater sum than a group of size $i$ containing smaller elements.

Thus, the actual values of the grades do not affect the maximum number of groups we can form. The problem reduces to finding the maximum number of groups $k$ such that the sum of the sizes of the groups $1 + 2 + 3 + \dots + k$ is less than or equal to the total number of students $n$.

This is represented by the inequality:
$$\frac{k(k+1)}{2} \le n$$

We can solve this inequality for $k$ using the quadratic formula:
$$k^2 + k - 2n \le 0$$
$$k = \lfloor \frac{-1 + \sqrt{1 + 8n}}{2} \rfloor$$

This mathematical formula provides an $O(1)$ time complexity solution.

### Complexity Analysis
- **Time Complexity**: `O(1)` because we can compute the result directly using a closed-form mathematical formula.
- **Space Complexity**: `O(1)` as we only use a few variables for the calculation.

### Reference Implementations
<details>
<summary>python</summary>

```python
import math

def solve(grades: list[int]) -> int:
    n = len(grades)
    # Solve k * (k + 1) / 2 <= n
    # k^2 + k - 2n <= 0
    # k = (-1 + sqrt(1 + 8n)) / 2
    return (-1 + math.isqrt(1 + 8 * n)) // 2
```
</details>
