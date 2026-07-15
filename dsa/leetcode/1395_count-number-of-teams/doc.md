# Count Number of Teams

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1395 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Binary Indexed Tree, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/count-number-of-teams/) |

## Problem Description

### Goal

Soldiers stand in a row, and `rating[i]` gives the distinct rating of the soldier at position `i`. A team consists of three soldiers selected at indices $i < j < k$, so their order in the row must be preserved.

The team is valid when its ratings are strictly increasing, with $\texttt{rating[i]} < \texttt{rating[j]} < \texttt{rating[k]}$, or strictly decreasing, with $\texttt{rating[i]} > \texttt{rating[j]} > \texttt{rating[k]}$. Return the number of valid teams. A soldier may participate in more than one team.

### Function Contract

**Inputs**

- `rating`: an array of $n$ pairwise distinct ratings, where $3 \le n \le 1000$ and $1 \le \texttt{rating[i]} \le 10^5$.

**Return value**

- The number of increasing or decreasing index-ordered triples.

### Examples

**Example 1**

- Input: `rating = [2,5,3,4,1]`
- Output: `3`

**Example 2**

- Input: `rating = [2,1,3]`
- Output: `0`

**Example 3**

- Input: `rating = [1,2,3,4]`
- Output: `4`

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Choose the middle soldier first.** For each index `j`, count four groups relative to `rating[j]`: smaller and greater ratings to its left, and smaller and greater ratings to its right.

An increasing team with middle index `j` is formed by choosing one smaller left rating and one greater right rating, giving `left_smaller * right_greater` teams. A decreasing team similarly contributes `left_greater * right_smaller`. Add both products for every possible middle index.

Every counted choice has indices in the required order because its members come from the left side, `j`, and the right side. The comparison groups enforce one of the two strict rating orders. Conversely, every valid triple has one unique middle index and belongs to exactly one of those products, so no team is omitted or counted twice.

#### Complexity detail

For each of $n$ middle positions, the two side scans inspect $O(n)$ ratings, for $O(n^2)$ time. Only four counters and the total are stored, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Enumerate all triples:** Testing every $i < j < k$ is correct but costs $O(n^3)$ time.
- **Fenwick trees:** Coordinate-compressed prefix and suffix counts reduce time to $O(n\log n)$ but add data-structure complexity and $O(n)$ space.
- **Exactly three soldiers:** The result is either one or zero depending on their strict order.
- **Strict comparisons:** Equal ratings would not qualify, though the contract guarantees all ratings are distinct.
- **Monotone array:** Every choice of three indices is valid, so the answer is $\binom{n}{3}$.
- **Mixed directions:** A triple that rises and then falls, or falls and then rises, contributes nothing.

</details>
