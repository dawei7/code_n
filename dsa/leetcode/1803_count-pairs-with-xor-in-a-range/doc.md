# Count Pairs With XOR in a Range

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/count-pairs-with-xor-in-a-range/) |
| Frontend ID | 1803 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Given a positive integer array `nums` and two bounds `low` and `high`, a pair of indices $(i,j)$ is considered valid when $i<j$ and the bitwise XOR of their values lies in the inclusive interval $[\texttt{low},\texttt{high}]$.

Count all valid index pairs. Equal values at different indices remain distinct pair participants, and each unordered pair must be counted once.

### Function Contract

**Inputs**

- `nums`: a list of $n$ positive integers, where $1 \le n \le 2\cdot10^4$ and $1 \le \texttt{nums[i]} \le 2\cdot10^4$.
- `low` and `high`: inclusive XOR bounds satisfying $1 \le \texttt{low}\le\texttt{high}\le2\cdot10^4$.
- Let $B=15$, the number of bits needed for all legal values and bounds.

**Return value**

- Return the number of pairs $(i,j)$ satisfying $i<j$ and $\texttt{low}\le\texttt{nums[i]}\oplus\texttt{nums[j]}\le\texttt{high}$.

### Examples

**Example 1**

- Input: `nums = [1,4,2,7], low = 2, high = 6`
- Output: `6`

Every one of the six index pairs has an XOR in the requested interval.

**Example 2**

- Input: `nums = [9,8,4,2,1], low = 5, high = 14`
- Output: `8`

Eight of the ten possible index pairs satisfy the inclusive bounds.

**Example 3**

- Input: `nums = [1,2,3], low = 1, high = 2`
- Output: `2`

The pair XOR values are `3`, `2`, and `1`.

### Required Complexity

- **Time:** $O(nB)$
- **Space:** $O(nB)$

<details>
<summary>Approach</summary>

#### General

**Turn the inclusive interval into two prefixes**

Let $F(L)$ count pairs whose XOR is strictly less than $L$. The requested inclusive count is $F(\texttt{high}+1)-F(\texttt{low})$. It is therefore enough to answer one strict upper-bound query.

**Compare XOR prefixes inside a binary trie**

Scan bits from most significant to least significant while comparing `value XOR previous` with limit $L$. If the current limit bit is zero, the XOR bit must also be zero to keep the prefix tied. If the limit bit is one, choosing XOR bit zero makes the result permanently smaller, so every value in that trie branch can be added immediately; choosing XOR bit one keeps the prefix tied and continues the search.

Trie nodes store how many previously inserted values pass through them. At each bit, XOR zero follows the child equal to the current value bit, while XOR one follows the opposite child.

**Insert only after querying**

For each array value, first count compatible values already in the trie and only then insert the current value. The trie therefore contains exactly the indices smaller than the current index. Every valid pair is counted when its right endpoint is processed, and no pair is counted twice.

The bit-prefix decisions enumerate exactly the prior values whose XOR is below the limit. Subtracting the two strict-prefix counts preserves precisely the inclusive interval, proving the final result.

#### Complexity detail

Each of the $n$ values performs two trie queries and two insertions across $B=15$ bits, taking $O(nB)$ time. At most $O(nB)$ trie nodes are created, so auxiliary space is $O(nB)$.

#### Alternatives and edge cases

- **All index pairs:** Directly testing every XOR is simple and correct but takes $O(n^2)$ time.
- **Frequency table over the entire value domain:** Convolution-style approaches are possible because values are bounded, but they add substantial machinery and do not naturally enforce incremental pair counting.
- **Inclusive upper bound:** Query strict inequality with `high + 1`; querying `high` would omit pairs equal to the upper boundary.
- **Equal values:** Their XOR is zero, which is below every legal positive `low`, but the duplicate indices must still be represented independently in trie counts.
- **Exact lower bound:** Subtract only XOR values strictly below `low`, leaving values equal to `low` included.
- **Single element:** No pair exists, so both prefix counts are zero.
- **Repeated trie path:** Store a count at every node so duplicate values contribute their full multiplicity.

</details>
