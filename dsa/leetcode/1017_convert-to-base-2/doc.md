# Convert to Base -2

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1017 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/convert-to-base-2/) |

## Problem Description

### Goal

You are given a nonnegative integer `n`. Return a binary string representing the same value in base $-2$, using only the digits `0` and `1`.

If the returned digits from right to left are $d_0,d_1,\ldots,d_{B-1}$, they must satisfy

$$
n=\sum_{i=0}^{B-1}d_i(-2)^i.
$$

The representation must not contain leading zeroes unless `n == 0`, whose representation is exactly `"0"`.

### Function Contract

**Inputs**

- `n`: an integer satisfying $0\le n\le10^9$.

Let $B$ denote the number of digits in the returned base-$-2$ string.

**Return value**

- The unique base-$-2$ representation of `n` using digits `0` and `1` without unnecessary leading zeroes.

### Examples

**Example 1**

- Input: `n = 2`
- Output: `"110"`
- Explanation: $(-2)^2+(-2)^1=2$.

**Example 2**

- Input: `n = 3`
- Output: `"111"`
- Explanation: $(-2)^2+(-2)^1+(-2)^0=3$.

**Example 3**

- Input: `n = 4`
- Output: `"100"`
- Explanation: $(-2)^2=4$.

### Required Complexity

- **Time:** $O(B)$
- **Space:** $O(B)$

<details>
<summary>Approach</summary>

#### General

**Choose a nonnegative remainder:** At each step, `remainder = n & 1` selects `0` or `1` with the same parity as `n`. This ensures `n - remainder` is divisible by `-2` and makes the remainder a valid output digit.

**Advance to the next coefficient:** Append the remainder as the current least significant digit, then execute `n = (n - remainder) // -2`. The quotient may alternate sign, which is expected for a negative base. Repeat until the quotient is zero.

**Reverse the collected digits:** Division produces coefficients from $d_0$ upward, so reverse them to obtain the conventional most-significant-first string. Handle the original value zero directly because its loop would produce no digits.

Every step maintains `old_n = new_n * -2 + remainder` with a digit in `{0, 1}`. Recursively substituting these identities yields exactly the required weighted sum, and termination leaves no unrepresented quotient. The parity choice is unique, so the resulting representation is unique.

#### Complexity detail

The quotient's magnitude decreases geometrically, and one step produces each of the $B$ output digits, for $O(B)$ time. The digit list contains $B$ characters and uses $O(B)$ space, including the returned representation.

#### Alternatives and edge cases

- **Adjusted divmod:** Dividing by `-2` and correcting a negative remainder produces the same recurrence.
- **Greedy signed powers:** Choosing coefficients from the largest power downward is possible but requires careful reachable-range reasoning.
- **Recompute each quotient:** Deriving every digit anew from the original value is correct but repeats earlier division work and takes $O(B^2)$ time.
- **Zero:** Return `"0"` rather than an empty string.
- **Negative intermediate quotient:** It is part of the conversion and must not be treated as an invalid state.

</details>
