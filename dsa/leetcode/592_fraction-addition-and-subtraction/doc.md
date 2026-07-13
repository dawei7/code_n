# Fraction Addition and Subtraction

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 592 |
| Difficulty | Medium |
| Topics | Math, String, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/fraction-addition-and-subtraction/) |

## Problem Description
### Goal
Given a string `expression` representing fraction addition and subtraction, evaluate all of its terms exactly. Each term is a signed or unsigned fraction, and the operators between consecutive terms are `+` or `-`; calculations must preserve rational values rather than use an inexact decimal approximation.

Return the calculation result as a string containing one irreducible fraction. Keep the denominator positive and reduce the numerator and denominator by their greatest common divisor. If the result is an integer, it must still use fraction format with denominator `1`, such as `2/1`; a positive result does not include a leading plus sign.

### Function Contract
**Inputs**

- `expression: str`: consecutive fraction terms of the form `numerator / denominator`, separated by `+` or `-`

**Return value**

- A string `"numerator/denominator"` representing the exact reduced result
- The denominator must be positive
- An integer result still uses denominator `1`

### Examples
**Example 1**

- Input: `expression = "-1/2+1/2"`
- Output: `"0/1"`

**Example 2**

- Input: `expression = "-1/2+1/2+1/3"`
- Output: `"1/3"`

**Example 3**

- Input: `expression = "1/3-1/2"`
- Output: `"-1/6"`

### Required Complexity

- **Time:** $O(n \log V)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Parse one signed fraction at a time**

Advance an index through the expression. Read an optional leading sign, then collect numerator digits up to `/` and denominator digits up to the next sign or end of input. Applying the sign to the numerator keeps every denominator positive.

**Maintain one exact running fraction**

If the running value is $a / b$ and the next term is $c / d$, replace it with $(a d + c b) / (b d)$. This uses integer arithmetic throughout, so no precision is lost.

**Reduce after every addition**

Compute `gcd(abs(numerator), denominator)` and divide both parts by it after each term. Incremental reduction keeps intermediate integers smaller and automatically turns any zero result into $0 / 1$.

**Why the final fraction is canonical**

The update is the standard common-denominator identity, so induction over terms shows the running fraction equals the parsed prefix exactly. Dividing numerator and denominator by their greatest common divisor preserves that value and leaves them coprime. Since every parsed denominator is positive, the final denominator stays positive, giving the unique requested representation.

#### Complexity detail

The parser advances monotonically across `n` characters. Each term performs a greatest-common-divisor calculation taking $O(\log V)$ arithmetic steps for the current integer magnitude `V`, so total time is $O(n \log V)$. Only indices and the running numerator and denominator are stored, giving $O(1)$ auxiliary space apart from integer representation.

#### Alternatives and edge cases

- **Regular-expression tokenization:** cleanly extracts signed fractions, but stores all tokens and uses $O(n)$ additional space.
- **Language rational-number type:** can simplify arithmetic when available, though the parsing and output contract still need care.
- **Repeated suffix rebuilding:** is correct but can repeatedly copy the unparsed expression and take $O(n^2)$ time.
- **Zero result:** must be normalized to $0/1$.
- **Negative first term:** its leading minus belongs to the numerator.
- **Positive first term:** may omit a leading plus.
- **Integer result:** still returns an explicit denominator of one.
- **Several denominators:** use exact cross multiplication, never floating-point conversion.
- **Large intermediate products:** reduce after each term to control growth.

</details>
