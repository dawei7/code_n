## Description

You are given a **0-indexed** integer array `nums`.

We say that an integer x is **expressible** from `nums` if there exist some integers $0 \le \text{index}_{1} < \text{index}_{2} < ... < \text{index}_{k} < \text{nums.length}$ for which $nums[\text{index}_{1}] | nums[\text{index}_{2}] | ... | nums[\text{index}_{k}] = x$. In other words, an integer is expressible if it can be written as the bitwise OR of some subsequence of `nums`.

Return *the minimum **positive non-zero integer** that is not **expressible from *`nums`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

```
**Input:** nums = [2,1]
**Output:** 4
**Explanation:** 1 and 2 are already present in the array. We know that 3 is expressible, since nums[0] | nums[1] = 2 | 1 = 3. Since 4 is not expressible, we return 4.
```
#### Example 2

- **Input:** `nums = [5,3,2]`
- **Output:** `1`
- **Explanation:** We can show that 1 is the smallest number that is not expressible.
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$