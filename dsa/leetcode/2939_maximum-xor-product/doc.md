# Maximum Xor Product

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2939 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Greedy, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-xor-product/) |

## Problem Description
### Goal
Given nonnegative integers `a` and `b`, choose a nonnegative integer `x`
whose binary representation uses only the lowest `n` bit positions; formally,
$0 \le x < 2^n$. The same chosen value is XORed with both inputs, producing
`a XOR x` and `b XOR x`.

Maximize the ordinary integer product
`(a XOR x) * (b XOR x)` over every permitted `x`. Because that maximum can
be large, return the maximum value modulo $10^9+7$. The maximization is
performed before taking the modulus.

### Function Contract
**Inputs**

- `a`: the first nonnegative integer
- `b`: the second nonnegative integer
- `n`: the number of low bit positions that `x` may change

The contract guarantees $0 \le a,b < 2^{50}$ and $0 \le n \le 50$.

**Return value**

The maximum possible product of the two XOR results, reduced modulo
$10^9+7$.

### Examples
**Example 1**

- Input: `a = 12, b = 5, n = 4`
- Output: `98`
- Explanation: Choosing `x = 2` produces factors `14` and `7`, whose
  product is `98`.

**Example 2**

- Input: `a = 6, b = 7, n = 5`
- Output: `930`
- Explanation: Choosing `x = 25` produces factors `31` and `30`.

**Example 3**

- Input: `a = 1, b = 6, n = 3`
- Output: `12`
- Explanation: Choosing `x = 5` produces factors `4` and `3`.
