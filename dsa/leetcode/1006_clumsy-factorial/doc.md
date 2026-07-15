# Clumsy Factorial

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1006 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Stack, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/clumsy-factorial/) |

## Problem Description

### Goal

The factorial of a positive integer $n$ multiplies all positive integers from $n$ down through $1$. A clumsy factorial keeps those integers in decreasing order but replaces the multiplication signs with the repeating operator sequence multiplication, division, addition, and subtraction.

Evaluate the resulting expression with the usual arithmetic order of operations: multiplication and division occur before addition and subtraction, and adjacent multiplication and division operations are processed from left to right. Division is floor division as defined by the problem; for example, `10 * 9 / 8` evaluates as `90 / 8`, giving `11`. Given `n`, return its clumsy factorial.

### Function Contract

**Inputs**

- `n`: a positive integer satisfying $1\le n\le10^4$.

**Return value**

- The integer value of the clumsy-factorial expression formed from `n` down through `1`.

### Examples

**Example 1**

- Input: `n = 4`
- Output: `7`
- Explanation: The expression is `4 * 3 / 2 + 1`, which evaluates to `7`.

**Example 2**

- Input: `n = 10`
- Output: `12`
- Explanation: The expression is `10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1`.

**Example 3**

- Input: `n = 3`
- Output: `6`
- Explanation: The available operators produce `3 * 2 / 1`.

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Separate the first product from later groups:** For $n>4$, the leading group `n * (n - 1) / (n - 2)` evaluates to $n+1$. Every complete later block has the form `-a * (a - 1) / (a - 2) + (a - 3)`. Since `a * (a - 1) / (a - 2)` evaluates to $a+1$ for these decreasing positive integers, a complete block contributes $-(a+1)+(a-3)=-4$.

**Collapse the repeating blocks:** Decreasing `a` by four and adding the next block preserves this fixed correction. Only the final incomplete block depends on the remainder of `n` modulo $4$. Simplifying those four endings yields $n+1$ when `n % 4 == 0`, $n+2$ when the remainder is `1` or `2`, and $n-1$ when the remainder is `3`.

**Handle the short expressions directly:** The periodic derivation assumes a full leading group and a later operator boundary. Therefore return `1`, `2`, `6`, and `7` directly for `n` from `1` through `4`. These values also prevent a remainder formula from being applied before its algebraic pattern begins.

The block identity accounts for every complete set of four decreasing operands, and the remainder case accounts for every operand left at the end. Thus the closed form is exactly the value produced by a precedence-aware simulation.

#### Complexity detail

The result uses a fixed number of comparisons and arithmetic operations, independent of $n$, for $O(1)$ time. It stores only the input and its remainder, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Stack simulation:** Applying multiplication and division immediately while storing additive terms mirrors precedence clearly, but processes all $n$ operands and uses $O(n)$ space.
- **Four-term streaming simulation:** Accumulating one operator block at a time reduces auxiliary space to $O(1)$ but still takes $O(n)$ time.
- **Values below five:** Return the explicitly evaluated results because the stable four-value pattern has not started.
- **Incomplete final block:** The remainder modulo $4$ determines which multiplication, division, or addition operands are missing.
- **Operator precedence:** Do not evaluate the full expression strictly from left to right; multiplication and division bind before addition and subtraction.

</details>
