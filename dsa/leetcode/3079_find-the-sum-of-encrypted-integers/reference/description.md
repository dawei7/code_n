## Description

You are given an integer array `nums` containing **positive** integers. We define a function `encrypt` such that `encrypt(x)` replaces **every** digit in `x` with the **largest** digit in `x`. For example, $encrypt(523) = 555$ and $encrypt(213) = 333$.

Return *the **sum **of encrypted elements*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **nums = [1,2,3]

**Output: **6

**Explanation:** The encrypted elements are `[1,2,3]`. The sum of encrypted elements is $1 + 2 + 3 = 6$.

</div>
#### Example 2

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **nums = [10,21,31]

**Output: **66

**Explanation:** The encrypted elements are `[11,22,33]`. The sum of encrypted elements is $11 + 22 + 33 = 66$.

</div>
### Constraints

- $1 \le \text{nums.length} \le 50$

- $1 \le \text{nums}[i] \le 1000$