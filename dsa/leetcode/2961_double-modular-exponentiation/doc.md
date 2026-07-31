# Double Modular Exponentiation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2961 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/double-modular-exponentiation/) |

## Problem Description
### Goal
You are given a 0-indexed array `variables`. Each row has four positive
integers `[a, b, c, m]`, and you are also given an integer `target`.

For row `i`, first raise `a` to `b` and take the result modulo $10$. Raise that
residue to `c`, then take the result modulo `m`. Index `i` is good exactly when
this final residue equals `target`:

$$
\left((a_i^{b_i}\bmod 10)^{c_i}\right)\bmod m_i
=\texttt{target}.
$$

Return all good indices in any order.

### Function Contract
**Inputs**

- `variables`: rows `[a, b, c, m]` defining the two modular exponentiations
- `target`: the residue that a row must produce

Let $V=\lvert\texttt{variables}\rvert$. The contract guarantees
$1\le V\le100$, every row contains four integers from $1$ through $1000$, and
$0\le\texttt{target}\le1000$.

**Return value**

An array containing exactly the indices whose nested modular exponentiation
equals `target`; any order is accepted.

### Examples
**Example 1**

- Input: `variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]], target = 2`
- Output: `[0,2]`
- Explanation: Rows `0` and `2` evaluate to two, while row `1` evaluates to zero modulo one.

**Example 2**

- Input: `variables = [[39,3,1000,1000]], target = 17`
- Output: `[]`
- Explanation: The inner residue is nine and its thousandth power is congruent to one modulo 1000, not 17.
