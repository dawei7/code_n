# Double Modular Exponentiation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2961 |
| Difficulty | Medium |
| Topics | Array, Math, Simulation |
| Official Link | [double-modular-exponentiation](https://leetcode.com/problems/double-modular-exponentiation/) |

## Problem Description & Examples
### Goal
Identify all indices `i` in a given list of quadruplets `variables` such that the expression `((a^b % 10)^c % m)` equals `target`. Each quadruplet consists of four integers `[a, b, c, m]`.

### Function Contract
**Inputs**

- `variables`: A list of lists, where each inner list contains four integers `[a, b, c, m]`.
- `target`: An integer representing the required result of the modular expression.

**Return value**

- A list of integers representing the indices of the quadruplets that satisfy the condition.

### Examples
**Example 1**

- Input: `variables = [[2,3,3,10], [3,3,3,1], [6,1,1,4]], target = 2`
- Output: `[0, 2]`

**Example 2**

- Input: `variables = [[39,3,1000,1000]], target = 17`
- Output: `[]`

**Example 3**

- Input: `variables = [[1,2,3,4]], target = 1`
- Output: `[0]`

---

## Underlying Base Algorithm(s)
The solution utilizes **Modular Exponentiation** (specifically the `pow(base, exp, mod)` function in Python). This algorithm efficiently computes `(base^exp) % mod` in logarithmic time, preventing integer overflow and ensuring performance even with large exponents.

---

## Complexity Analysis
- **Time Complexity**: `O(n * log(max(b)))`, where `n` is the number of quadruplets. For each quadruplet, we perform two modular exponentiations, each taking logarithmic time relative to the exponent.
- **Space Complexity**: `O(k)`, where `k` is the number of indices that satisfy the condition, used to store the result list.
