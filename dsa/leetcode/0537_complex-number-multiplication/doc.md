# Complex Number Multiplication

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 537 |
| Difficulty | Medium |
| Topics | Math, String, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/complex-number-multiplication/) |

## Problem Description
### Goal
Given two complex numbers encoded as strings `real+imaginaryi`, parse each signed integer real part and signed integer imaginary coefficient. The separator remains a literal plus sign even when the imaginary coefficient is negative, as in `1+-1i`.

Multiply the numbers using $(a+bi)(c+di)=(ac-bd)+(ad+bc)i$. Return the product in the same `real+imaginaryi` string format with decimal integer components and a trailing `i`. Do not return a floating-point approximation, omit a zero component, or replace the required separator format.

### Function Contract
**Inputs**

- `num1`, `num2`: complex-number strings whose real and imaginary integer components are each between `-100` and `100`

**Return value**

- The exact complex product formatted as `real+imaginaryi`, including `+-` when the imaginary result is negative

### Examples
**Example 1**

- Input: `num1 = "1+1i", num2 = "1+1i"`
- Output: `"0+2i"`

**Example 2**

- Input: `num1 = "1+-1i", num2 = "1+-1i"`
- Output: `"0+-2i"`

**Example 3**

- Input: `num1 = "100+100i", num2 = "100+-100i"`
- Output: `"20000+0i"`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Parse the two integer components**

Remove the final `i`, split once at `+`, and convert both pieces to integers. A negative imaginary component appears after the separator as a signed value, such as `"-1"` in `"1+-1i"`, so ordinary integer conversion handles it directly.

**Apply the complex multiplication identity**

For $(a+bi)(c+di)$, distribute the terms. Since $i^{2}=-1$, the real component is $ac-bd$, while the imaginary coefficient is $ad+bc$.

**Format without losing the sign convention**

Join the integer real result, a literal plus separator, the signed imaginary result, and `i`. If the imaginary value is negative, this intentionally produces `+-`, matching the required representation.

**Why the formula is exact**

Distribution produces $ac+adi+bci+bdi^2$. Replacing $i^{2}$ with $-1$ groups the real terms as $ac-bd$ and the coefficients of $i$ as $ad+bc$. Parsing and formatting preserve those integer values exactly, so the returned string represents precisely the mathematical product.

#### Complexity detail

The component range is bounded and each input has constant maximum length, so parsing, four integer multiplications, additions, and formatting take $O(1)$ time and $O(1)$ auxiliary space. With unbounded decimal integers, costs would instead depend on digit length, but that is outside this contract.

#### Alternatives and edge cases

- **Language complex-number type:** can simplify arithmetic, but floating-point formatting risks losing exact integer representation.
- **Regular expression parsing:** handles the grammar but is unnecessary for one fixed separator and suffix.
- **Repeated-addition multiplication:** is correct for these small values but performs avoidable work proportional to operand magnitude.
- **Negative imaginary component:** the input contains `+-`, and the output may do so as well.
- **Zero component:** must still be rendered explicitly, such as `"0+0i"`.
- **Cancellation:** real or imaginary terms may cancel even when all input components are nonzero.
- **Maximum magnitude:** the result components may exceed `100`; only input components are bounded.

</details>
