## Problem Description & Examples
### Goal
Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

Value mappings:
- `I`: 1, `V`: 5, `X`: 10, `L`: 50, `C`: 100, `D`: 500, `M`: 1000

Given a roman numeral, convert it to an integer.

### Function Contract
**Inputs**

- `s`: str

**Return value**

int - converted integer

### Examples
**Example 1**

- Input: `s = "LVIII"`
- Output: `58`

**Example 2**

- Input: `s = 'XL'`
- Output: `40`

**Example 3**

- Input: `s = 'IX'`
- Output: `9`

---

## Underlying Base Algorithm(s)
- [Euclidean GCD](math_01_gcd-euclidean.md)
- [Modular exponentiation](math_03_modular-exponentiation.md)
- [Convex hull](geometric_02_convex-hull-graham-scan.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
