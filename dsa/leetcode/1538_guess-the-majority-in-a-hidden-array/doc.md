# Guess the Majority in a Hidden Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1538 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Interactive |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/guess-the-majority-in-a-hidden-array/) |

## Problem Description
### Goal
A hidden array `nums` contains only `0` and `1`. You cannot read its entries directly. Instead, an `ArrayReader` exposes its length and lets you query four distinct indices in strictly increasing order.

For indices $a < b < c < d$, `reader.query(a, b, c, d)` reports only the distribution of the four hidden bits: it returns `4` when all four are equal, `2` when one bit differs from the other three, and `0` when the group contains two zeros and two ones. At most $2n$ calls to `query` are allowed, where $n$ is the hidden-array length.

Return any index containing the more frequent bit. If zeros and ones occur equally often, return `-1`.

### Function Contract
**Inputs**

- `reader`: an `ArrayReader` for a hidden binary array of length $n$, where $5 \le n \le 10^5$.
- `reader.length()` returns $n$.
- `reader.query(a, b, c, d)` requires $0 \le a < b < c < d < n$ and returns `4`, `2`, or `0` according to the four-bit distribution above.

**Return value**

Any valid index of the majority bit, or `-1` when the two bit counts tie. The solution may make at most $2n$ queries.

### Examples
**Example 1**

- Hidden input: `nums = [0, 0, 1, 0, 1, 1, 1, 1]`
- Output: `5`
- Explanation: Ones are more frequent, so any index containing `1`, including `2`, `4`, `5`, `6`, or `7`, is valid.

**Example 2**

- Hidden input: `nums = [0, 0, 1, 1, 0]`
- Output: `0`
- Explanation: Zeros form the majority, and index zero contains a zero.

**Example 3**

- Hidden input: `nums = [1, 0, 1, 0, 1, 0, 1, 0]`
- Output: `-1`
- Explanation: Each bit occurs four times.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count equivalence to one reference bit**

The actual identities of zero and one are unnecessary. It is enough to divide every index into those holding the same bit as index `3` and those holding the opposite bit. Whichever class is larger contains the array's majority value.

Let `baseline = reader.query(0, 1, 2, 3)`. For every index `i` from `4` onward, compare `reader.query(0, 1, 2, i)` with `baseline`. The two queries share indices `0`, `1`, and `2`; they differ only by replacing index `3` with `i`. Their distribution reports are equal exactly when those two replaced bits are equal. Count index `i` with the reference class if the results match, and with the opposite class otherwise.

**Recover the first three classifications**

The scan above cannot put an index smaller than `3` into the fourth query position. Use index `4` as a legal anchor. Store `comparison = reader.query(0, 1, 2, 4)`, then make these three comparisons:

- `reader.query(0, 1, 3, 4)` replaces index `2` with reference index `3`;
- `reader.query(0, 2, 3, 4)` replaces index `1` with index `3`;
- `reader.query(1, 2, 3, 4)` replaces index `0` with index `3`.

Each result equals `comparison` precisely when the replaced index belongs to the reference class. This classifies indices `0`, `1`, and `2` without ever learning whether the reference bit is zero or one.

**Choose an index, not a bit value**

Keep index `3` as the representative of the reference class and remember the most recent index classified as different. If the two class counts tie, return `-1`. If the reference class is larger, return `3`; otherwise return the remembered opposite-class index. Because the two classes are exactly the zero positions and one positions, the larger class always represents the most frequent hidden value.

The method performs two initial queries, one query for every index from `5` through `n - 1`, and three final queries, for exactly $n$ calls. Thus it stays within the $2n$ API limit.

#### Complexity detail

There is one constant-time query and constant local work per hidden position, giving $O(n)$ time and $n$ total query calls. The counters, stored query results, and representative indices use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Reconstruct every bit:** pairwise relative classifications can recover an array up to global complement, but storing all classifications uses $O(n)$ space even though only two counts and representatives are needed.
- **Query arbitrary groups independently:** distribution values from unrelated four-index sets cannot be oriented reliably; sharing three anchor indices is what makes equality comparisons meaningful.
- For the minimum legal length $n = 5$, the main loop is empty, but the two anchor queries and three replacement queries still classify every index.
- When the counts tie, no returned array index can satisfy the contract; return `-1` exactly in that case.
- Either zero or one may be the majority. The relative-class method is deliberately symmetric and never assumes which value index `3` contains.
- Multiple output indices may be correct, so validation must check whether the returned position contains the majority value rather than require one fixed representative.

</details>
