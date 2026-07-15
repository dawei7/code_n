# Circular Permutation in Binary Representation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1238 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Backtracking, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/circular-permutation-in-binary-representation/) |

## Problem Description

### Goal

Given integers `n` and `start`, return any permutation `p` of every integer from $0$ through $2^n-1$. The first element must be `start`, and the $n$-bit representations of each adjacent pair `p[i]` and `p[i + 1]` must differ in exactly one bit.

The permutation is circular: the binary representations of its last and first elements must also differ in exactly one bit. Every value in the $n$-bit domain must occur exactly once. More than one ordering may satisfy these requirements, and any valid ordering may be returned.

### Function Contract

**Inputs**

- `n`: The number of bits, where $1\le n\le16$.
- `start`: The required first value, where $0\le\texttt{start}<2^n$.

**Return value**

- Any circular one-bit-difference permutation of all $2^n$ values whose first element is `start`.

### Examples

**Example 1**

- Input: `n = 2`, `start = 3`
- Output: `[3,2,0,1]`

In binary, `11`, `10`, `00`, and `01` differ by one bit around the full cycle.

**Example 2**

- Input: `n = 3`, `start = 2`
- Output: `[2,6,7,5,4,0,1,3]`

The sequence contains every three-bit value and returns from `3` to `2` by one bit.

**Example 3**

- Input: `n = 1`, `start = 1`
- Output: `[1,0]`

The two one-bit values are adjacent in both circular directions.

### Required Complexity

- **Time:** $O(2^n)$
- **Space:** $O(2^n)$

<details>
<summary>Approach</summary>

#### General

**Generate the reflected binary Gray cycle.** For each integer `i` from `0` through `(1 << n) - 1`, the value `i ^ (i >> 1)` is its reflected Gray code. Consecutive indices produce codes differing in exactly one bit, every $n$-bit value occurs once, and the last code differs from the first code in one bit as well.

**Translate the entire cycle with XOR.** XOR every Gray code with `start`. The first Gray code is zero, so the translated first value is `0 ^ start`, which equals `start`. XOR by a fixed value is a bijection, preserving the fact that the sequence contains every domain value exactly once.

For any two values, XORing both with the same mask leaves their difference unchanged: `(a ^ start) ^ (b ^ start) == a ^ b`. Therefore every adjacent one-bit difference, including the closing edge from the last value to the first, survives the translation. The generated list consequently satisfies every condition without searching or rotating a sequence.

#### Complexity detail

The algorithm computes and emits exactly $2^n$ values with constant work per value, so it takes $O(2^n)$ time. The returned permutation contains $2^n$ integers, giving $O(2^n)$ output space and $O(1)$ auxiliary space beyond the result.

#### Alternatives and edge cases

- **Backtracking through the hypercube:** Searching for a Hamiltonian cycle can find a valid permutation but performs unnecessary branching and visited-state work.
- **Build then rotate a Gray list:** Locating `start` and rotating is correct, but XOR translation produces the requested start directly.
- **Explicit uniqueness scans:** Checking each generated value against the growing result preserves correctness but degrades construction to $O(4^n)$ time.
- **One bit:** The only valid domain is `{0, 1}`, and either requested start gives the two-element cycle.
- **Start zero:** XOR changes nothing, so the ordinary reflected Gray sequence is returned.
- **Circular boundary:** Validating only consecutive list entries is insufficient; the final and first entries must also differ by one bit.
- **Output lower bound:** Any solution must emit all $2^n$ values, so linear time in the output size is optimal.

</details>
