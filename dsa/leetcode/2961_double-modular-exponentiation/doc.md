# Double Modular Exponentiation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2961 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [double-modular-exponentiation](https://leetcode.com/problems/double-modular-exponentiation/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/double-modular-exponentiation/).

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

## Solution
### Approach
The solution utilizes **Modular Exponentiation** (specifically the `pow(base, exp, mod)` function in Python). This algorithm efficiently computes `(base^exp) % mod` in logarithmic time, preventing integer overflow and ensuring performance even with large exponents.

### Complexity Analysis
- **Time Complexity**: `O(n * log(max(b)))`, where `n` is the number of quadruplets. For each quadruplet, we perform two modular exponentiations, each taking logarithmic time relative to the exponent.
- **Space Complexity**: `O(k)`, where `k` is the number of indices that satisfy the condition, used to store the result list.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(variables: list[list[int]], target: int) -> list[int]:
    """
    Computes the indices of variables that satisfy ((a^b % 10)^c % m) == target.
    Uses Python's built-in pow(a, b, m) for efficient modular exponentiation.
    """
    result = []

    for i, (a, b, c, m) in enumerate(variables):
        # Step 1: Calculate (a^b % 10)
        # Step 2: Calculate (result_of_step1^c % m)
        # We use the three-argument pow(base, exp, mod) for efficiency.
        val = pow(a, b, 10)
        final_val = pow(val, c, m)

        if final_val == target:
            result.append(i)

    return result
```
</details>
