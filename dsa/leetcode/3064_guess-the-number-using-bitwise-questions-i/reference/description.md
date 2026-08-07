### 1. Description

There is a number `n` that you have to find.

There is also a pre-defined API `int commonSetBits(int num)`, which returns the number of bits where both `n` and `num` are `1` in that position of their binary representation. In other words, it returns the number of set bits in `n & num`, where `&` is the bitwise `AND` operator.

Return *the number* `n`.

**Example 1: **

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **  n = 31

**Output: **  31

**Explanation: ** It can be proven that it's possible to find `31` using the provided API.

</div>

**Example 2: **

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **  n = 33

**Output: **  33

**Explanation: ** It can be proven that it's possible to find `33` using the provided API.

</div>

### 2. Function Contract

- Refer to method signature.

### 3. Constraints

- $1 \le n \le 2^{30} - 1$

- $0 \le num \le 2^{30} - 1$

- If you ask for some `num` out of the given range, the output wouldn't be reliable.