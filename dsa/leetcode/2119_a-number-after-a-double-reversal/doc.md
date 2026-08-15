# A Number After a Double Reversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2119 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/a-number-after-a-double-reversal/) |

## Problem Description

### Goal

Reversing an integer reverses the order of its decimal digits. Any zeros that
would lead the reversed representation are discarded; for example, reversing
`12300` produces `321`. Digits elsewhere in the representation remain present,
and the reversed result is interpreted as an ordinary nonnegative integer
rather than as a fixed-width digit sequence.

Given a nonnegative integer `num`, reverse it once to obtain `reversed1`, then
reverse that result to obtain `reversed2`. Determine whether `reversed2` equals
the original number exactly. The comparison concerns the numeric values after
both applications of the same leading-zero rule.

### Function Contract

**Inputs**

- `num`: An integer from $0$ through $10^6$.

**Return value**

Return `true` when reversing `num` twice restores it exactly; otherwise return
`false`.

### Examples

#### Example 1

- **Input:** `num = 526`
- **Output:** `true`

The reversals are `526 -> 625 -> 526`.

#### Example 2

- **Input:** `num = 1800`
- **Output:** `false`

The first reversal discards two leading zeros, giving `81`, and the second
therefore produces only `18`.

#### Example 3

- **Input:** `num = 0`
- **Output:** `true`

Zero remains zero under both reversals.
