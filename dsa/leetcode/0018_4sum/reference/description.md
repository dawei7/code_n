## Description

Given an array `nums` of `n` integers, return *an array of all the **unique** quadruplets* `[nums[a], nums[b], nums[c], nums[d]]` such that:

- $0 \le a, b, c, d < n$

- `a`, `b`, `c`, and `d` are **distinct**.

- $\text{nums}[a] + \text{nums}[b] + \text{nums}[c] + \text{nums}[d] = target$

You may return the answer in **any order**.
### Function Contract

**Inputs**

- `nums`: The integer array to search.
- `target`: The required quadruplet sum.

Let $n = \lvert\texttt{nums}\rvert$.

**Return value**

Return every unique value quadruplet whose distinct source indices sum to `target`, in any order.

### Examples
#### Example 1

- **Input:** `nums = [1,0,-1,0,-2,2], target = 0`
- **Output:** `[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]`
#### Example 2

- **Input:** `nums = [2,2,2,2,2], target = 8`
- **Output:** `[[2,2,2,2]]`
### Constraints

- $1 \le \text{nums.length} \le 200$

- $-10^{9} \le \text{nums}[i] \le 10^{9}$

- $-10^{9} \le target \le 10^{9}$