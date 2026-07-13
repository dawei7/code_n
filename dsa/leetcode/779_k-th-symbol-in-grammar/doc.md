# K-th Symbol in Grammar

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 779 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Bit Manipulation, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/k-th-symbol-in-grammar/) |

## Problem Description

### Goal

The first grammar row is `0`. To create each following row, replace every `0` in the previous row with `01` and every `1` with `10`, preserving the order of all replacement pairs.

Given a one-based row number `n` and a one-based position `k`, return the symbol at that position of row `n`. The result is the integer `0` or `1`; the row may be exponentially long, but the requested symbol is defined by the recursive grammar.

### Function Contract

**Inputs**

- `n`: a positive row number.
- `k`: a one-based position satisfying $1 \le k \le 2^{(n - 1)}$.

**Return value**

- The integer `0` or `1` stored at position `k` of row `n`.

### Examples

**Example 1**

- Input: `n = 1, k = 1`
- Output: `0`
- Explanation: The first row contains only its initial zero.

**Example 2**

- Input: `n = 2, k = 1`
- Output: `0`
- Explanation: Expanding the first row produces `01`.

**Example 3**

- Input: `n = 2, k = 2`
- Output: `1`
- Explanation: The second position of `01` is one.

### Required Complexity

- **Time:** $O(\log k)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Follow the implicit ancestry**

Each symbol produces a left child equal to itself and a right child equal to its complement. For the zero-based position $k - 1$, a zero bit in its binary representation selects a left child at that level, while a one bit selects a right child and flips the inherited symbol.

**Count flips instead of building rows**

Start with symbol `0`. Repeatedly inspect the lowest bit of $k - 1$: toggle the symbol when that bit is one, then shift the position right. The final symbol is the parity of the number of right-child choices, equivalently the parity of the set-bit count of $k - 1$.

The root symbol is zero, and every step along its unique descendant path either preserves or complements it exactly as the corresponding position bit indicates. Toggling once per right edge therefore reproduces every grammar expansion on that path, so the parity returned after all position bits are consumed is precisely the requested symbol.

#### Complexity detail

The loop consumes one binary digit of $k - 1$ per iteration, taking $O(\log k)$ time. It stores only the current position and one bit of parity, for $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Built-in population count:** Return `(k - 1).bit_count() % 2`; this expresses the same parity rule directly.
- **Recursive parent lookup:** Move to parent position $\lceil k/2 \rceil$ and complement the result for an even $k$; this takes $O(n)$ time and recursion space.
- **Construct every row:** Applying the substitutions literally is correct but requires exponential time and space in `n`.
- **First position:** $k = 1$ has zero right-child choices, so its symbol is always zero.
- **Last position:** Its zero-based index consists entirely of ones, so the answer is the parity of $n - 1$.
- **Role of `n`:** Once `k` is guaranteed to lie in row `n`, the ancestry and answer are determined by $k - 1$; no row storage is needed.

</details>
