## Description

You are given a string `s` consisting of characters `'U'`, `'D'`, `'L'`, and `'R'`, representing moves on an infinite 2D Cartesian grid.

- `'U'`: Move from `(x, y)` to $(x, y + 1)$.

- `'D'`: Move from `(x, y)` to $(x, y - 1)$.

- `'L'`: Move from `(x, y)` to $(x - 1, y)$.

- `'R'`: Move from `(x, y)` to $(x + 1, y)$.

You are also given a positive integer `k`.

You **must** choose and remove **exactly one** contiguous substring of length `k` from `s`. Then, start from coordinate `(0, 0)` and perform the remaining moves in order.

Return an integer denoting the number of **distinct** final coordinates reachable.
### Function Contract

**Inputs**

- `s`: A nonempty movement string containing only `U`, `D`, `L`, and `R`.
- `k`: The exact length of the one contiguous substring that must be removed.

Every possible start position for a length-`k` substring is considered. The retained prefix and suffix are concatenated implicitly and executed in their original order from $(0,0)$.

**Return value**

Return the number of distinct endpoints produced by the valid substring removals.

### Examples

#### Example 1

<div class="example-block">
**Input:** s = "LUL", k = 1

**Output:** 2

**Explanation:**

After removing a substring of length 1, `s` can be `"UL"`, `"LL"` or `"LU"`. Following these moves, the final coordinates will be `(-1, 1)`, `(-2, 0)` and `(-1, 1)` respectively. There are two distinct points `(-1, 1)` and `(-2, 0)` so the answer is 2.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "UDLR", k = 4

**Output:** 1

**Explanation:**

After removing a substring of length 4, `s` can only be the empty string. The final coordinates will be `(0, 0)`. There is only one distinct point `(0, 0)` so the answer is 1.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "UU", k = 1

**Output:** 1

**Explanation:**

After removing a substring of length 1, `s` becomes `"U"`, which always ends at `(0, 1)`, so there is only one distinct final coordinate.

</div>
### Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` consists of only `'U'`, `'D'`, `'L'`, and `'R'`.

- $1 \le k \le \text{s.length}$