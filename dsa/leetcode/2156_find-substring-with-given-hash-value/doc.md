# Find Substring With Given Hash Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2156 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Sliding Window, Rolling Hash, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/find-substring-with-given-hash-value/) |

## Problem Description

### Goal

For a lowercase string $t$ of length $k$, define
$\operatorname{val}(\texttt{a})=1$ through
$\operatorname{val}(\texttt{z})=26$. Given integers $p$ and $m$, its hash is

$$
\operatorname{hash}(t,p,m)
=
\left(
\sum_{j=0}^{k-1}
\operatorname{val}(t[j])p^j
\right)
\bmod m.
$$

Given a lowercase string `s` and the values `power`, `modulo`, `k`, and
`hashValue`, find the first contiguous substring of `s` whose length is
exactly `k` and whose hash under this definition equals `hashValue`. A matching
substring is guaranteed to exist.

### Function Contract

**Inputs**

- `s`: a lowercase English string with length from $1$ through $2\cdot10^4$.
- `power`: the hash base, where $1 \le \texttt{power} \le 10^9$.
- `modulo`: the modulus, where $1 \le \texttt{modulo} \le 10^9$.
- `k`: the required substring length, where $1 \le k \le \lvert s\rvert$.
- `hashValue`: the required residue, where
  $0 \le \texttt{hashValue} < \texttt{modulo}$.

**Return value**

The leftmost length-`k` substring whose defined hash equals `hashValue`.

### Examples

**Example 1**

- Input: `s = "leetcode", power = 7, modulo = 20, k = 2, hashValue = 0`
- Output: `"ee"`
- Explanation: The hash is `(5 * 1 + 5 * 7) % 20 = 0`, and `"ee"` is the
  first matching length-two substring.

**Example 2**

- Input: `s = "fbxzaad", power = 31, modulo = 100, k = 3, hashValue = 32`
- Output: `"fbx"`
- Explanation: Both `"fbx"` and the later substring `"bxz"` hash to `32`, so
  the earlier one is returned.
