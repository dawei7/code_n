## Description

You may recall that an array `arr` is a **mountain array** if and only if:

- $\text{arr.length} \ge 3$

- There exists some index `i` (**0-indexed**) with $0 < i < \text{arr.length} - 1$ such that:

		<li>$\text{arr}[0] < \text{arr}[1] < ... < arr[i - 1] < \text{arr}[i]$

- $\text{arr}[i] > arr[i + 1] > ... > arr[\text{arr.length} - 1]$

	</li>

Given an integer array `arr`, return *the length of the longest subarray, which is a mountain*. Return `0` if there is no mountain subarray.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** `arr = [2,1,4,7,3,2,5]`
- **Output:** `5`
- **Explanation:** The largest mountain is [1,4,7,3,2] which has length 5.
#### Example 2

- **Input:** `arr = [2,2,2]`
- **Output:** `0`
- **Explanation:** There is no mountain.
### Constraints

- $1 \le \text{arr.length} \le 10^{4}$

- $0 \le \text{arr}[i] \le 10^{4}$

**Follow up:**

- Can you solve it using only one pass?

- Can you solve it in `O(1)` space?