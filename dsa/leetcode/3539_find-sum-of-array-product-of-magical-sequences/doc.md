# Find Sum of Array Product of Magical Sequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3539 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Bit Manipulation, Combinatorics, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/) |

## Problem Description

### Goal

Given integers `m` and `k` and an integer array `nums`, consider every ordered sequence `seq` of length `m` whose entries are valid indices into `nums`. Repeated indices are allowed, and sequences that differ at any position are distinct.

For a sequence, form the integer

$$
S = \sum_{j=0}^{m-1} 2^{\texttt{seq[j]}}.
$$

The sequence is magical exactly when the binary representation of $S$ contains `k` set bits. Its array product is the product of the selected array values,

$$
\prod_{j=0}^{m-1}\texttt{nums[seq[j]]}.
$$

Return the sum of these products over all magical sequences, modulo $10^9+7$.

### Function Contract

**Inputs**

- `m`: The required sequence length, where $1 \le m \le 30$.
- `k`: The required number of set bits, where $1 \le k \le m$.
- `nums`: Positive weights for the selectable indices, with $1 \le \lvert\texttt{nums}\rvert \le 50$ and $1 \le \texttt{nums[i]} \le 10^8$.

Let $N=\lvert\texttt{nums}\rvert$.

**Return value**

- The sum of all magical sequences' array products modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `m = 5, k = 5, nums = [1,10,100,10000,1000000]`
- **Output:** `991600007`
- **Explanation:** Every permutation of the five distinct indices contributes the same product, $10^{13}$, and the modular sum of those products is returned.

#### Example 2

- **Input:** `m = 2, k = 2, nums = [5,4,3,2,1]`
- **Output:** `170`
- **Explanation:** The magical sequences are the ordered pairs of distinct indices; their weighted products sum to `170`.

#### Example 3

- **Input:** `m = 1, k = 1, nums = [28]`
- **Output:** `28`
- **Explanation:** The only sequence is `[0]`, and its binary power sum has one set bit.
