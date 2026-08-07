## Description

Given an integer array `nums`, return *the maximum result of *$\text{nums}[i] XOR \text{nums}[j]$, where $0 \le i \le j < n$.
### Function Contract

**Inputs**

- `nums`: An array of nonnegative integers.

**Return value**

Return the maximum value of `nums[i] ^ nums[j]` among all valid position pairs with $i \le j$.

Here, $n = \lvert\texttt{nums}\rvert$.

### Examples
#### Example 1

- **Input:** `nums = [3,10,5,25,2,8]`
- **Output:** `28`
- **Explanation:** The maximum result is 5 XOR 25 = 28.
#### Example 2

- **Input:** `nums = [14,70,53,83,49,91,36,80,92,51,66,70]`
- **Output:** `127`
### Constraints

- $1 \le \text{nums.length} \le 2 * 10^{5}$

- $0 \le \text{nums}[i] \le 2^{31} - 1$