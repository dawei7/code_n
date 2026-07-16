# Minimum One Bit Operations to Make Integers Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1611 |
| Difficulty | Hard |
| Topics | Math, Dynamic Programming, Bit Manipulation, Recursion, Memoization |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/) |

## Problem Description
### Goal
Transform the non-negative integer `n` into zero by changing one bit per operation. The rightmost bit, at index 0, may always be flipped.

For any index $i>0$, bit $i$ may be flipped only when bit $i-1$ is 1 and every lower bit from $i-2$ through 0 is 0. Apply either legal operation as often as needed and return the minimum number of operations required to reach zero.

### Function Contract
**Inputs**

- `n`: an integer satisfying $0 \le n \le 10^9$.

**Return value**

Return the minimum number of legal single-bit changes that transform `n` into 0.

### Examples
**Example 1**

- Input: `n = 3`
- Output: `2`
- Explanation: Binary `11` can flip its second bit to become `01`, then flip the rightmost bit to reach `00`.

**Example 2**

- Input: `n = 6`
- Output: `4`
- Explanation: One shortest sequence is `110 -> 010 -> 011 -> 001 -> 000`.

**Example 3**

- Input: `n = 0`
- Output: `0`

### Required Complexity
- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Recognize the reflected Gray-code path.** Beginning at zero, the states produced by the only legal next bit changes follow binary-reflected Gray-code order. At step $k$, the represented state is

$$
G(k)=k\mathbin{\mathtt{xor}}(k\mathbin{\mathtt{>>}}1).
$$

Thus the required operation count is the inverse Gray-code value of `n`: the index $k$ whose Gray representation is `n`. Reversing a transformation is no longer than applying it forward because every bit flip is reversible under the same neighboring-bit condition.

**Invert Gray code with suffix XORs.** If the Gray bits from most significant to least significant are $g_b,\ldots,g_0$, the corresponding binary bit $b_i$ is the XOR of $g_b$ through $g_i$. Numerically, XORing `n` with each of its successive right shifts performs all of those suffix accumulations:

`operations = n ^ (n >> 1) ^ (n >> 2) ^ ...`.

The loop folds one shifted copy at a time into the answer until no set bit remains. The resulting binary value is exactly the Gray-code index of `n`, which equals the minimum distance to zero along the legal state path.

#### Complexity detail

Each iteration removes one bit position by shifting `n` right. There are $O(\log n)$ positions for positive `n`, so the method takes $O(\log n)$ time and stores only the running XOR and shifted value, using $O(1)$ space. For `n = 0`, the loop performs no iterations.

#### Alternatives and edge cases

- **Highest-bit recurrence:** If $2^b$ is the highest set bit, the answer satisfies `f(n) = (2^(b + 1) - 1) - f(n ^ 2^b)`. This is also $O(\log n)$ but needs recursive or explicit stack state.
- **Enumerate Gray-code states:** Increasing $k$ until `k ^ (k >> 1) == n` is correct, but it performs work proportional to the answer rather than to the bit length.
- **Breadth-first search over integers:** It finds a shortest path for small bit widths but explores exponentially many states and is infeasible near $10^9$.
- Zero already needs zero operations.
- A power of two requires $2^{b+1}-1$ operations because reaching and clearing its isolated highest bit traverses the entire lower reflected pattern.
- Ordinary popcount is insufficient: flipping a high bit may require temporarily setting and clearing lower bits.
- The answer can be much larger than the number of set bits while still fitting comfortably in the problem's integer range.

</details>
