## Description

Given a signed 32-bit integer `x`, return `x`* with its digits reversed*. If reversing `x` causes the value to go outside the signed 32-bit integer range $[-2^{31}, 2^{31} - 1]$, then return `0`.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**
### Function Contract

**Inputs**

- `x`: The signed 32-bit integer to reverse.

**Return value**

Return the digit-reversed integer, or `0` when that result would overflow the signed 32-bit range.

### Examples

#### Example 1

- **Input:** $x = 123$
- **Output:** `321`
#### Example 2

- **Input:** $x = -123$
- **Output:** `-321`
#### Example 3

- **Input:** $x = 120$
- **Output:** `21`
### Constraints

- $-2^{31} \le x \le 2^{31} - 1$