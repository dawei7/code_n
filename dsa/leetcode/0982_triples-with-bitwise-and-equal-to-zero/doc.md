# Triples with Bitwise AND Equal To Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 982 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/) |

## Problem Description

### Goal

Given an integer array `nums`, count its AND triples. An AND triple is an ordered triple of indices `(i, j, k)` for which `nums[i] & nums[j] & nums[k] == 0`.

Each of `i`, `j`, and `k` may independently be any valid array index. The indices do not need to be distinct, and changing their order creates a different triple when the ordered index tuple changes. Return the total number of tuples satisfying the zero bitwise-AND condition.

### Function Contract

**Inputs**

- `nums`: a list of $N$ integers, where $1\le N\le1000$ and $0\le\texttt{nums[i]}<2^{16}$.

Let $D$ be the number of distinct input values and $U$ the number of distinct masks produced by ANDing ordered pairs. Both are at most $N$ and $\min(N^2,2^{16})$, respectively.

**Return value**

- The number of ordered index triples whose three selected values have bitwise AND equal to zero.

### Examples

**Example 1**

- Input: `nums = [2, 1, 3]`
- Output: `12`
- Explanation: twelve ordered choices of `(i, j, k)` produce zero after the two bitwise-AND operations.

**Example 2**

- Input: `nums = [0, 0, 0]`
- Output: `27`
- Explanation: all $3^3$ ordered triples qualify.

### Required Complexity

- **Time:** $O(N^2+DU)$
- **Space:** $O(U)$

<details>
<summary>Approach</summary>

#### General

**Aggregate the first two indices:** Count every ordered pair `(i, j)` by the mask `nums[i] & nums[j]`. This takes quadratic time but compresses all pairs with the same remaining set bits into one frequency.

**Test only masks that occur:** For a third value $x$, a pair mask $p$ completes a valid triple exactly when $p\mathbin{\&}x=0$. Iterate over the distinct pair masks and add the stored frequency of each compatible one. Cache this compatible-pair total for every distinct input value so repeated occurrences of $x$ reuse the same result.

Every ordered pair is counted once in its exact AND bucket. A bucket contributes to the cached total for $x$ exactly when its mask AND $x$ is zero. Multiplying that total by the frequency of $x$ as the third selected value counts every valid ordered triple once and no invalid triple.

#### Complexity detail

Building ordered pair frequencies costs $O(N^2)$. Checking all $U$ occurring pair masks for each of the $D$ distinct values costs $O(DU)$, giving $O(N^2+DU)$ time. The pair-frequency map and cached totals use $O(U+D)=O(U)$ space because every input value also occurs as a self-AND pair mask.

#### Alternatives and edge cases

- **Enumerate all triples:** Three nested index loops are direct and correct but require $O(N^3)$ time.
- **Dense subset-sum transform:** A sum-over-subsets transform gives $O(N^2+B2^B)$ time for a fixed $B$-bit universe, but eagerly visiting all $2^{16}$ masks is wasteful when few pair masks occur.
- **Zero value:** Any ordered triple containing a selected zero has combined AND zero.
- **Repeated indices:** Tuples such as `(i, i, i)` are legal and must not be filtered out.
- **Ordered counting:** Permutations of three indices are separate tuples even when they select equal values.

</details>
