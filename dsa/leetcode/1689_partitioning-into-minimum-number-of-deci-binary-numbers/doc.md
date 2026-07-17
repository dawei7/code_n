# Partitioning Into Minimum Number Of Deci-Binary Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1689 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/) |

## Problem Description
### Goal

A positive decimal integer is deci-binary when every digit in its ordinary base-10 representation is either `0` or `1`. For example, `10` and `101` are deci-binary, whereas a number containing any digit from `2` through `9` is not.

The positive integer to decompose is supplied as a decimal string `n`, which may be much longer than a built-in numeric type can hold. Express its value as a sum of positive deci-binary integers and return the minimum possible number of addends. Only the count is required, not the addends themselves.

### Function Contract
**Inputs**

- `n`: the digit string of a positive decimal integer with no leading zero, of length $L$

**Return value**

The minimum number of positive deci-binary integers whose arithmetic sum equals the value represented by `n`.

### Examples
**Example 1**

- Input: `n = "32"`
- Output: `3`

One decomposition is `11 + 11 + 10`.

**Example 2**

- Input: `n = "82734"`
- Output: `8`

The leading digit 8 already requires eight addends.

**Example 3**

- Input: `n = "27346209830709182346"`
- Output: `9`

The string contains a digit 9, which determines the answer.

### Required Complexity

- **Time:** $O(L)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**A digit gives a lower bound**

Suppose a decimal position of `n` contains digit $d$. Each deci-binary addend contributes at most one at that position. With fewer than $d$ addends, every column sum is below 10, so no carry can arise from a less significant position to supply the missing amount. At least $d$ addends are therefore necessary. The largest digit $m$ in `n` proves a global lower bound of $m$.

**Layer all positions simultaneously**

That lower bound is attainable. Create $m$ conceptual layers. For a target digit $d$, place `1` in that position of the first $d$ layers and `0` in the rest. The column then sums to exactly $d$. Applying this independently at every position constructs $m$ deci-binary values whose sum is `n`; leading zeroes in a layer are simply omitted from its ordinary representation. A position containing $m$ ensures every layer is positive.

The construction proves that no more than the maximum digit is needed, while the lower bound proves that no fewer can work. Scan the string and return its maximum digit.

#### Complexity detail

Finding the maximum examines all $L$ characters once, taking $O(L)$ time. The running maximum occupies $O(1)$ auxiliary space, and the potentially enormous decimal value is never parsed as an integer.

#### Alternatives and edge cases

- **Construct every addend:** the layer construction is valid but unnecessary when only the count is requested; materializing it uses $O(L)$ output-sized storage.
- **Repeated subtraction:** subtracting deci-binary layers digit by digit reaches the same count but performs extra passes and mutations.
- **Parse the decimal integer:** the input can contain up to $10^5$ digits, so fixed-width conversion is invalid and arbitrary-precision conversion is needless.
- **Digits only zero or one:** the input itself is deci-binary, so one addend suffices.
- **Internal maximum digit:** the decisive digit need not be the first or last character.
- **Digit nine:** nine is the largest possible answer for any legal decimal string.

</details>
