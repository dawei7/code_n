## Description

You are given an integer `n`, a 2D integer array `restrictions`, and an integer array `diff` of length $n - 1$. Your task is to construct a sequence of length `n`, denoted by $a[0], a[1], ..., a[n - 1]$, such that it satisfies the following conditions:

- $a[0]$ is 0.

- All elements in the sequence are **non-negative**.

- For every index `i` ($0 \le i \le n - 2$), $abs(a[i] - a[i + 1]) \le \text{diff}[i]$.

- For each $\text{restrictions}[i] = [idx, maxVal]$, the value at position `idx` in the sequence must not exceed `maxVal` (i.e., $a[idx] \le maxVal$).

Your goal is to construct a valid sequence that **maximizes** the **largest** value within the sequence while satisfying all the above conditions.

Return an integer denoting the **largest** value present in such an optimal sequence.
### Function Contract

**Inputs**

- `n`: The required sequence length.
- `restrictions`: Pairs `[idx, maxVal]` giving upper bounds at distinct nonzero indices.
- `diff`: Exactly `n - 1` positive edge limits; `diff[i]` applies between positions `i` and `i + 1`.

The constructed sequence is not returned. A restriction is only an upper bound, and the adjacent-difference rule limits both upward and downward changes.

**Return value**

Return the greatest value that can appear in any valid sequence while the maximum over that entire sequence is as large as possible.

### Examples
#### Example 1

<div class="example-block">
**Input:** n = 10, restrictions = [[3,1],[8,1]], diff = [2,2,3,1,4,5,1,1,2]

**Output:** 6

**Explanation:**

- The sequence $a = [0, 2, 4, 1, 2, 6, 2, 1, 1, 3]$ satisfies the given constraints ($a[3] \le 1$ and $a[8] \le 1$).

- The maximum value in the sequence is 6.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 8, restrictions = [[3,2]], diff = [3,5,2,4,2,3,1]

**Output:** 12

**Explanation:**

- The sequence $a = [0, 3, 3, 2, 6, 8, 11, 12]$ satisfies the given constraints ($a[3] \le 2$).

- The maximum value in the sequence is 12.

</div>
### Constraints

- $2 \le n \le 10^{5}$

- $1 \le \text{restrictions.length} \le n - 1$

- $\text{restrictions}[i].length = 2$

- $\text{restrictions}[i] = [idx, maxVal]$

- $1 \le idx < n$

- $1 \le maxVal \le 10^{6}$

- $\text{diff.length} = n - 1$

- $1 \le \text{diff}[i] \le 10$

- The values of $\text{restrictions}[i][0]$ are unique.