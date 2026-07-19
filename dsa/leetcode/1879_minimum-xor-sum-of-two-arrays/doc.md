# Minimum XOR Sum of Two Arrays

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/) |
| Frontend ID | 1879 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Two equal-length integer arrays have an XOR sum obtained by XORing values at matching indices and adding the results:

$$
\sum_{i=0}^{N-1}\bigl(\texttt{nums1[i]}\mathbin{\mathrm{XOR}}\texttt{nums2[i]}\bigr).
$$

You may rearrange the elements of `nums2` in any order while leaving `nums1` fixed. Choose a permutation that minimizes this total and return the resulting minimum XOR sum. Every occurrence in `nums2`, including duplicate values, must be assigned to exactly one index of `nums1`.

### Function Contract

**Inputs**

- `nums1`, `nums2`: integer arrays of the same length $N$, where $1 \le N \le 14$ and every value lies from $0$ through $10^7$.

**Return value**

- Return the minimum sum of pairwise XOR values obtainable by permuting `nums2`.

### Examples

**Example 1**

- Input: `nums1 = [1,2], nums2 = [2,3]`
- Output: `2`

Rearranging `nums2` to `[3,2]` gives `(1 XOR 3) + (2 XOR 2) = 2`.

**Example 2**

- Input: `nums1 = [1,0,3], nums2 = [5,3,4]`
- Output: `8`

The arrangement `[5,4,3]` contributes $4+4+0$.

**Example 3**

- Input: `nums1 = [2,4,6], nums2 = [1,3,5]`
- Output: `9`

No permutation produces an XOR sum below $9$.

### Required Complexity

- **Time:** $O(N2^N)$
- **Space:** $O(2^N)$

<details>
<summary>Approach</summary>

#### General

**Encode the assigned second-array positions**

Use an $N$-bit mask. A set bit $j$ means occurrence `nums2[j]` has already been assigned. If a mask contains $K$ set bits, it represents assignments for exactly the first $K$ positions of `nums1`; the detailed order of earlier choices no longer matters once their minimum accumulated cost is known.

**Transition by the last assigned occurrence**

Let `cost[mask]` be the minimum XOR sum for the prefix of length `mask.bit_count()`. For a nonzero mask with $K$ bits, consider every set bit $j$ as the occurrence paired with `nums1[K-1]`. Removing that bit yields the preceding state, so

$$
\operatorname{cost}[\textit{mask}]
=
\min_{j\in\textit{mask}}
\left(
\operatorname{cost}[\textit{mask}\setminus\{j\}]
+
\bigl(\texttt{nums1}[K-1]\mathbin{\mathrm{XOR}}\texttt{nums2}[j]\bigr)
\right).
$$

Initialize the empty mask with cost zero and evaluate masks in increasing numerical order; removing a set bit always produces a smaller mask.

**Why the recurrence is complete**

Every permutation assigning the first $K$ positions has one definite occurrence paired with position $K-1$. Removing that final pair leaves a valid assignment represented by the predecessor mask. Conversely, extending any predecessor with any unused occurrence forms a valid larger assignment. The transition checks all possible final choices and combines each with an optimal predecessor, so induction on $K$ proves every stored value minimal. The all-ones mask therefore gives the required full assignment.

#### Complexity detail

There are $2^N$ masks, and each considers at most $N$ second-array positions. This takes $O(N2^N)$ time. The dynamic-programming array has one value per mask, requiring $O(2^N)$ space; loop indices and temporary values use constant extra storage.

#### Alternatives and edge cases

- **Enumerate every permutation:** It directly checks the definition but costs $O(N!\,N)$ time.
- **Top-down memoization:** Recursing on the used-position mask has the same $O(N2^N)$ time and $O(2^N)$ memo size, plus recursion overhead.
- **Minimum-cost matching:** The problem is an assignment instance and can also be solved by a polynomial-time matching algorithm, though bitmask DP is compact and well suited to $N\le14$.
- **Single element:** No rearrangement is possible, so return the sole XOR.
- **Duplicate values:** Bits identify occurrences rather than values, ensuring every copy is used once.
- **Zero values:** XOR with zero returns the other operand and requires no special branch.
- **Identical multisets:** Pairing equal values can make the answer zero even when the original orders differ.

</details>
