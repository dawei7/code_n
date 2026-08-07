## Description

Given an integer array `nums` and two integers `lower` and `upper`, return *the number of range sums that lie in* `[lower, upper]` *inclusive*.

Range sum `S(i, j)` is defined as the sum of the elements in `nums` between indices `i` and `j` inclusive, where $i \le j$.
### Function Contract

**Inputs**

- `nums`: The integer array whose contiguous ranges are counted.
- `lower`: The inclusive lower sum bound.
- `upper`: The inclusive upper sum bound.

**Return value**

Return the number of pairs $(i,j)$ with $i \le j$ whose inclusive range sum is between `lower` and `upper`.

### Examples
#### Example 1

- **Input:** `nums = [-2,5,-1], lower = -2, upper = 2`
- **Output:** `3`
- **Explanation:** The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.
#### Example 2

- **Input:** `nums = [0], lower = 0, upper = 0`
- **Output:** `1`
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $-2^{31} \le \text{nums}[i] \le 2^{31} - 1$

- $-10^{5} \le lower \le upper \le 10^{5}$

- The answer is **guaranteed** to fit in a **32-bit** integer.