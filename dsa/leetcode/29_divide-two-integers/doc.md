# Divide Two Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 29 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/divide-two-integers/) |

## Problem Description
### Goal
You are given a signed 32-bit `dividend` and a nonzero signed 32-bit `divisor`. Compute their integer quotient without using multiplication, division, or modulo operators. Fractional parts are discarded by truncating toward zero, not by taking the mathematical floor for negative results.

Return the quotient within the signed 32-bit range $[-2^{31}, 2^{31}-1]$. The only mathematically overflowing input is $-2^{31}$ divided by $-1$; clamp that result to $2^{31}-1$. All sign combinations and magnitudes at the negative boundary must otherwise behave normally.

### Function Contract
**Inputs**

- `dividend`: signed 32-bit `int`
- `divisor`: nonzero signed 32-bit `int`

**Return value**

The truncated and clamped signed 32-bit integer quotient.

### Examples
**Example 1**

- Input: `dividend = 10, divisor = 3`
- Output: `3`

**Example 2**

- Input: `dividend = 7, divisor = -3`
- Output: `-2`

**Example 3**

- Input: `dividend = -2147483648, divisor = -1`
- Output: `2147483647`

### Required Complexity

- **Time:** $O(\log |dividend|)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Separate the quotient sign from its magnitude**

The quotient is negative exactly when the operands have different signs. Record that Boolean before changing either operand. In Python, work with absolute magnitudes so bit comparisons and subtractions are nonnegative, then apply the sign at the end.

In a strictly signed 32-bit implementation, taking the absolute value of $-2^{31}$ cannot itself be represented. Such implementations can keep both working operands negative or promote only the intermediate magnitude to a wider integer type. The mathematical bit-selection logic remains the same; the representation choice must not overflow before division begins.

**Build the quotient from its highest bit downward**

Compare the bit lengths of the two magnitudes to find the largest potentially useful shift. Test shifts from that value down to zero. Whenever `divisor_magnitude << shift` is no larger than the remainder, subtract it and set bit `shift` in the quotient.

This chooses powers-of-two multiples exactly as decimal long division chooses place-value multiples, without using any prohibited arithmetic operator.

**Why a chosen high bit can never need revision**

Before shift `b` is considered, the original dividend magnitude equals `quotient * divisor_magnitude + remainder`, and all quotient bits above `b` are final. Subtracting `divisor_magnitude << b` and setting bit `b` preserves this equality. If the shifted divisor is too large, setting that bit would already exceed the remainder, and no combination of lower bits can make an oversized contribution valid.

After shift zero, the remainder is smaller than the divisor magnitude. Otherwise one more unshifted divisor could have been subtracted. The quotient and remainder therefore satisfy the defining Euclidean-division conditions for positive magnitudes.

**Trace quotient bits rather than repeated subtraction**

For $10 / 3$, shifted divisor 6 fits at bit 1, leaving remainder 4 and quotient 2. Shift zero contributes another 3, leaving remainder 1 and quotient 3. Restoring the positive sign returns 3.

**Most-significant quotient bits are irrevocable**

At bit position $b$, the shifted divisor represents choosing $2^b$ copies. If it exceeds the current remainder, that quotient bit must be zero because the sum of all still-lower choices cannot justify subtracting this oversized multiple. If it fits, setting the bit and subtracting the multiple is necessary for the greatest quotient representable by the remaining bit positions.

After the last bit, the accumulated quotient and remainder satisfy `dividend = divisor * quotient + remainder` with `0 <= remainder < divisor`. That identity uniquely characterizes integer division of positive magnitudes. Applying the saved sign gives truncation toward zero; the single mathematical overflow case $-2^{31} / -1$ is handled by the required clamp.

#### Complexity detail

There is one iteration per relevant dividend bit, and each performs constant-time fixed-width shifts, comparisons, and subtraction. For 32-bit inputs this is bounded by 32 operations; expressed in input magnitude, time is $O(\log |dividend|)$. Only a fixed number of integer variables are stored, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Repeated subtraction:** correct for small quotients but requires time proportional to the quotient.
- **Repeated doubling with nested searches:** improves over single subtraction but may redo shifts; one descending bit pass is simpler.
- **Built-in division followed by conversion:** violates the operator restriction and can hide language-specific negative rounding behavior.
- The divisor is guaranteed nonzero. If `abs(dividend) < abs(divisor)`, no quotient bit is selected and the answer is zero.
- Truncation toward zero follows from dividing magnitudes and applying the sign afterward; floor division would differ for a negative nonintegral quotient.
- $-2^{31} / -1$ is the sole mathematical quotient outside the signed 32-bit range and must return $2^{31} - 1$.

</details>
