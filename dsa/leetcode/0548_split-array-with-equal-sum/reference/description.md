## Description

Given an integer array `nums` of length `n`, return `true` if there is a triplet `(i, j, k)` which satisfies the following conditions:

- $0 < i, i + 1 < j, j + 1 < k < n - 1$

- The sum of subarrays $(0, i - 1)$, $(i + 1, j - 1)$, $(j + 1, k - 1)$ and $(k + 1, n - 1)$ is equal.

A subarray `(l, r)` represents a slice of the original array starting from the element indexed `l` to the element indexed `r`.
### Function Contract

**Inputs**

- `nums`: the integer array to test.

Let $n = \lvert\texttt{nums}\rvert$. A valid result requires three ordered separator indices with at least one array
element before, between, and after them. Inputs with $n < 7$ are legal under the source constraints but cannot contain
such a split. Values may be positive, zero, or negative, and the separator values never contribute to a section sum.

**Return value**

Return `True` if some valid `(i, j, k)` makes the four retained subarray sums equal; otherwise return `False`. Only
feasibility is returned, not the indices or shared sum.

### Examples
#### Example 1

- **Input:** `nums = [1,2,1,2,1,2,1]`
- **Output:** `true`
- **Explanation:**
i = 1, j = 3, k = 5.
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1
#### Example 2

- **Input:** `nums = [1,2,1,2,1,2,1,2]`
- **Output:** `false`
### Constraints

- $n = \text{nums.length}$

- $1 \le n \le 2000$

- $-10^{6} \le \text{nums}[i] \le 10^{6}$