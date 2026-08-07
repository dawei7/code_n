## Description

There is a number `n` that you have to find.

There is also a pre-defined API `int commonSetBits(int num)`, which returns the number of bits where both `n` and `num` are `1` in that position of their binary representation. In other words, it returns the number of <span data-keyword="set-bit">set bits</span> in `n & num`, where `&` is the bitwise `AND` operator.

Return *the number* `n`.

**Example 1: **

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> n = 31 </span>

**Output: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> 31 </span>

**Explanation: ** It can be proven that it's possible to find `31` using the provided API.

</div>

**Example 2: **

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> n = 33 </span>

**Output: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> 33 </span>

**Explanation: ** It can be proven that it's possible to find `33` using the provided API.

</div>

**Constraints:**

	- `1 <= n <= 2^30 - 1`

	- `0 <= num <= 2^30 - 1`

	- If you ask for some `num` out of the given range, the output wouldn't be reliable.
