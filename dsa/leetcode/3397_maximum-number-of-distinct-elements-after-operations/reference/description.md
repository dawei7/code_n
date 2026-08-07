## Description

You are given an integer array `nums` and an integer `k`.

You are allowed to perform the following **operation** on each element of the array **at most** *once*:

- Add an integer in the range `[-k, k]` to the element.

Return the **maximum** possible number of **distinct** elements in `nums` after performing the **operations**.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,2,2,3,3,4], k = 2

**Output:** 6

**Explanation:**

`nums` changes to `[-1, 0, 1, 2, 3, 4]` after performing operations on the first four elements.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [4,4,4,4], k = 1

**Output:** 3

**Explanation:**

By adding -1 to $\text{nums}[0]$ and 1 to $\text{nums}[1]$, `nums` changes to `[3, 5, 4, 4]`.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$

- $0 \le k \le 10^{9}$