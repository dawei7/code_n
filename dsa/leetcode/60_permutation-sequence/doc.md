# Permutation Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 60 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/permutation-sequence/) |

## Problem Description
### Goal
The set of distinct digits from `1` through `n`, where $1 \le n \le 9$, contains $n!$ unique permutations. Arrange those permutations in lexicographic order. The rank `k` is one-based: $k = 1$ names the increasing permutation, and $k = n!$ names the final one.

Return the digits of the permutation at rank `k` as a string. Each digit must appear exactly once. Determine the ranked arrangement directly from the ordering structure rather than generating and storing every preceding permutation.

### Function Contract
**Inputs**

- `n`: the number of distinct digits, with $1 \le n \le 9$
- `k`: a one-based rank satisfying $1 \le k \le n!$

**Return value**

The ranked permutation as a string.

### Examples
**Example 1**

- Input: `n = 3, k = 3`
- Output: `"213"`

**Example 2**

- Input: `n = 4, k = 9`
- Output: `"2314"`

**Example 3**

- Input: `n = 3, k = 1`
- Output: `"123"`

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Lexicographic prefixes occupy equal factorial-sized blocks**

With $r$ sorted digits remaining, each possible next digit heads a contiguous block of $(r - 1)!$ permutations. Convert the one-based rank to `rank = k - 1` before division. Then `floor(rank / block_size)` is a zero-based digit-list index and `rank % block_size` is the rank within that chosen prefix block.

The zero-based conversion is essential at exact block boundaries. For example, one-based rank $(r - 1)!$ still belongs to the first block, whereas dividing it directly would incorrectly select the second block.

**Remove the selected digit and recurse into its block**

Keep unused digits in sorted order. Pop the selected index and append that digit to the answer. After one digit is fixed, update the block size from $(r - 1)!$ to $(r - 2)!$ and repeat with the remainder rank. When only one digit remains, its block size is one and it is selected directly.

**Rank is always relative to the current fixed prefix**

Before each selection, the answer is the fixed prefix of the desired permutation, the digit list contains exactly its unused symbols in order, and `k` is the zero-based rank among permutations sharing that prefix.

**Trace quotient and remainder choices**

For $n = 4, k = 9$, use zero-based rank 8. Blocks have size 6, so index 1 selects `2` and leaves rank 2. Blocks then have size 2, so index 1 selects `3`; the remaining rank 0 selects `1` and then `4`, producing `2314`.

**Factorial blocks turn rank into digit choices**

With `r` digits remaining, all permutations sharing the same next digit form one contiguous lexicographic block of size $(r - 1)!$. The blocks appear in the sorted order of the available digits. Dividing the zero-based rank by the block size therefore selects the exact next digit, while the remainder is the rank within that block.

Removing the chosen digit leaves the identical ranking problem on one fewer position. Repeating the quotient-and-remainder step follows the unique nested blocks containing the requested rank and reconstructs precisely the kth permutation.

#### Complexity detail

There are `n` selections. Removing an arbitrary item from an array of remaining digits costs $O(n)$, so total time is $O(n^2)$; factorial arithmetic itself is linear. The digit list and output use $O(n)$ space.

#### Alternatives and edge cases

- **Generate permutations in order:** may perform $O(k n)$ work and reaches factorial time for large ranks.
- **Repeated next-permutation operations:** avoids storing all permutations but still advances through every earlier rank.
- **Order-statistics tree:** can reduce selection and deletion to $O(\log n)$, but is unnecessary for at most nine digits and substantially more complex.
- $k = 1$ repeatedly selects index zero and returns ascending order; $k = n!$ selects the final blocks and returns descending order.
- The $n \le 9$ constraint lets each symbol fit in one decimal character. A generalized version with larger symbols would need an unambiguous output encoding.

</details>
