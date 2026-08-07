## Description

Given an integer array of size `n`, find all elements that appear more than $⌊n / 3⌋$ times.
### Function Contract

**Inputs**

- `nums`: The nonempty integer array whose value frequencies are considered.

**Return value**

Return all values occurring more than $\lfloor \texttt{nums.length}/3 \rfloor$ times, in any order.

### Examples

#### Example 1

- **Input:** `nums = [3,2,3]`
- **Output:** `[3]`
#### Example 2

- **Input:** `nums = [1]`
- **Output:** `[1]`
#### Example 3

- **Input:** `nums = [1,2]`
- **Output:** `[1,2]`
### Constraints

- $1 \le \text{nums.length} \le 5 * 10^{4}$

- $-10^{9} \le \text{nums}[i] \le 10^{9}$

**Follow up:** Could you solve the problem in linear time and in `O(1)` space?