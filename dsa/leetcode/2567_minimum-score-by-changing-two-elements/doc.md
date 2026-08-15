# Minimum Score by Changing Two Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2567 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [minimum-score-by-changing-two-elements](https://leetcode.com/problems/minimum-score-by-changing-two-elements/) |

## Problem Description

### Goal

For an integer array `nums`, define its low score as the smallest absolute difference between any pair of elements and its high score as the largest such absolute difference. The array's total score is the sum of those two quantities.

Change the values at two array positions to any integers you choose. Return the smallest total score that can be obtained after those changes. The array always contains at least three elements, so at least one original value remains available while the two selected positions are changed.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $3 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.

**Return value**

- The minimum possible sum of the low and high scores after changing two elements.

### Examples

#### Example 1

- **Input:** `nums = [1, 4, 7, 8, 5]`
- **Output:** `3`
- **Explanation:** Changing `1` and `4` to `6` creates a duplicate, so the low score is $0$; the remaining range from $5$ to $8$ makes the high score $3$.

#### Example 2

- **Input:** `nums = [1, 4, 3]`
- **Output:** `0`
- **Explanation:** Change two entries to match the third, making all three values equal.

#### Example 3

- **Input:** `nums = [31, 25, 72, 79, 74, 65]`
- **Output:** `14`
- **Explanation:** Neutralizing the two smallest values leaves unchanged values from $65$ through $79$, whose range is $14$.
