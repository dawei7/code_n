# Maximum XOR With an Element From Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1707 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/) |

## Problem Description
### Goal

You are given a list `nums` of non-negative integers and a list of queries. Each query is `[x, m]` and may use only values `num` from `nums` satisfying $\texttt{num} \le m$. Among those eligible values, maximize the bitwise result `x ^ num`.

Return one answer for each query in its original order. When a query's limit is smaller than every number in `nums`, no eligible choice exists and its answer is `-1`. Numbers and queries may repeat, and equality with the limit is allowed.

### Function Contract
**Inputs**

- `nums`: a list of $n$ non-negative integers
- `queries`: a list of $q$ pairs `[x, m]`
- $1 \le n,q \le 10^5$, and every `nums[j]`, `x`, and `m` lies between $0$ and $10^9$

Let $B = 30$, the number of bits needed to represent values through $10^9$.

**Return value**

A length-$q$ list whose entry for `[x, m]` is the maximum `x ^ num` over all `num <= m`, or `-1` if that eligible set is empty.

### Examples
**Example 1**

- Input: `nums = [0, 1, 2, 3, 4], queries = [[3, 1], [1, 3], [5, 6]]`
- Output: `[3, 3, 7]`

The eligible sets grow with limits `1`, `3`, and `6`; the best partners are `0`, `2`, and `2`, respectively.

**Example 2**

- Input: `nums = [5, 2, 4, 6, 6, 3], queries = [[12, 4], [8, 1], [6, 3]]`
- Output: `[15, -1, 5]`

The middle query has no value at most `1`. The other queries maximize their most significant differing bits among their eligible values.

**Example 3**

- Input: `nums = [1, 7, 9], queries = [[4, 0], [4, 8], [4, 10]]`
- Output: `[-1, 5, 13]`

Increasing the limit admits first `1` and `7`, then also `9`; the final XOR `4 ^ 9` equals `13`.

### Required Complexity

- **Time:** $O((n + q)\log(n + q) + (n + q)B)$
- **Space:** $O(nB + q)$

<details>
<summary>Approach</summary>

#### General

**Turn query limits into a monotone insertion frontier**

Sort `nums` in ascending order. Attach each query's original index and sort the queries by `m`. While processing a query, insert every not-yet-inserted number whose value is at most its limit. Because later limits never decrease, inserted values remain eligible and each number enters the data structure once.

If no number has been inserted, store `-1`. Otherwise the structure contains exactly all values eligible for the current query, independent of the queries' original order. Write the computed result back at the saved index to restore that order.

**Maximize XOR from the most significant bit**

Store inserted values in a binary trie with one level for each of the $B$ bit positions. To query `x`, start at its most significant bit. An XOR bit becomes `1` when the chosen number's bit differs from `x`, so prefer the opposite-bit child whenever it exists. If it does not, follow the same-bit child and accept a zero at that result position.

This greedy choice is final at each level: a `1` at a more significant XOR position outweighs every possible combination of lower bits. After choosing the best available prefix, the trie node restricts the remaining candidates to exactly those with that prefix. Repeating down all levels therefore yields the maximum XOR among all inserted numbers.

The offline limit sweep and trie invariant combine cleanly: the trie controls eligibility, and the bitwise walk controls maximization. Neither concern is approximated.

#### Complexity detail

Sorting numbers and indexed queries takes $O((n + q)\log(n + q))$ time. Each of the $n$ insertions and $q$ trie queries visits exactly $B$ levels, adding $O((n + q)B)$. At most $nB + 1$ trie nodes and $q$ indexed queries or answers are stored, for $O(nB + q)$ space.

#### Alternatives and edge cases

- **Scan every eligible number per query:** direct maximization is correct but takes $O(nq)$ time when every query admits the whole array.
- **Build a fresh trie per query:** this repeats insertions and can also take $O(nqB)$ time.
- **One trie without limit metadata:** inserting every number answers unconstrained XOR but may select a value greater than the query's `m`.
- **Persistent tries by sorted prefix:** versioning one trie per insertion also answers limits efficiently, but uses a more complex persistent structure.
- **No eligible value:** return `-1`, not zero, even when `x ^ 0` would otherwise be meaningful.
- **Limit equality:** values exactly equal to `m` must be inserted before answering that query.
- **Zero:** its all-zero bit path is valid and may be the only eligible choice.
- **Duplicate values and queries:** duplicates do not change a maximum, but processing them must preserve every query output position.
- **Bit width:** include every bit needed for values up to $10^9$; omitting the highest bit can reverse the greedy result.

</details>
