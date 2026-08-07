## Description

You are given an integer `n` and a digit `x`.

A number is considered **valid** if:

- It contains **at least one** occurrence of digit `x`, and

- It **does not start** with digit `x`.

Return `true` if `n` is **valid**, otherwise return `false`.
### Function Contract

**Inputs**

- `n`: A nonnegative integer whose decimal digits are inspected.
- `x`: One decimal digit from `0` through `9`.

The decimal representation has no leading zeros. In particular, the representation of `0` is the one-character sequence `0`. An occurrence at the first position satisfies the containment condition but simultaneously violates the leading-digit condition.

**Return value**

Return `true` when the decimal representation of `n` contains `x` at least once and its first digit is not `x`. Return `false` in every other case.

### Examples
#### Example 1

<div class="example-block">
**Input:** n = 101, x = 0

**Output:** true

**Explanation:**

The number contains digit 0 at index 1. It does not start with 0, so it satisfies both conditions. Thus, the answer is `true`​​​​​​​.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 232, x = 2

**Output:** false

**Explanation:**

The number starts with 2, which violates the condition. Thus, the answer is `false`.

</div>
#### Example 3

<div class="example-block">
**Input:** n = 5, x = 1

**Output:** false

**Explanation:**

The number does not contain digit 1. Thus, the answer is `false`.

</div>
### Constraints

- $0 \le n \le 10^{5}​​​​​​​$

- $0 \le x \le 9$