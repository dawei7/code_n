# Find Kth Bit in Nth Binary String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1545 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Recursion, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/) |

## Problem Description
### Goal
A sequence of binary strings is defined recursively. The first string is `S1 = "0"`. For every $i > 1$, form `Si` by concatenating `S(i - 1)`, one `"1"`, and the reverse of the bitwise inversion of `S(i - 1)`. Inversion changes every `"0"` to `"1"` and every `"1"` to `"0"`.

Given `n` and a one-indexed position `k`, return the `k`-th bit of `Sn`. The full string has length $2^n - 1$, but only the requested character is needed.

### Function Contract
**Inputs**

- `n`: the sequence level, where $1 \le n \le 20$.
- `k`: a one-indexed position satisfying $1 \le k \le 2^n - 1$.

**Return value**

The character `"0"` or `"1"` at position `k` in `Sn`.

### Examples
**Example 1**

- Input: `n = 3, k = 1`
- Output: `"0"`
- Explanation: `S3 = "0111001"`, whose first character is `"0"`.

**Example 2**

- Input: `n = 4, k = 11`
- Output: `"1"`
- Explanation: The eleventh character of `S4 = "011100110110001"` is `"1"`.

**Example 3**

- Input: `n = 1, k = 1`
- Output: `"0"`
- Explanation: The base string contains only that bit.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Use the recursive symmetry instead of constructing strings**

The length of `Sn` is $2^n - 1$, so its middle position is $2^{n-1}$. The construction places `"1"` exactly there. Positions to the left are unchanged positions of `S(n - 1)`, so a left-side query can descend to the previous level with the same `k`.

**Reflect a right-side query into the left half**

The right half is the reversed, inverted copy of `S(n - 1)`. Reflecting position `k` across the full string maps it to position $2^n-k$ in the previous string. Recursively find that source bit, then invert it. This reduces the level by one without allocating either half.

**Reach a directly known bit**

At each level, the query is either the known middle bit, a left query, or an inverted reflected right query. Every recursive call decreases `n`, so it must reach a middle position or the base string `S1 = "0"`. These cases exactly mirror the three parts of the defining concatenation, which proves that the returned bit is the requested character.

#### Complexity detail

Each recursive call performs constant arithmetic and reduces $n$ by one, producing at most $n$ calls. The time is therefore $O(n)$. The recursion stack holds at most $n$ frames, so auxiliary space is $O(n)$. No string of length $2^n-1$ is constructed.

#### Alternatives and edge cases

- **Construct every sequence string:** direct simulation is easy to verify, but its time and memory grow as $O(2^n)$ even though only one bit is requested.
- **Iterative reflection:** track whether the answer is inverted while repeatedly reflecting right-half positions; this keeps $O(n)$ time and reduces auxiliary space to $O(1)$.
- At $n=1$, the only legal query returns `"0"`.
- Every level's middle position returns `"1"` without further recursion.
- The first position remains `"0"` at every level.
- A right-half reflection must both reverse the position and invert the resulting bit.
- Positions are one-indexed, so the middle is $2^{n-1}$ rather than an array-style zero-based index.

</details>
