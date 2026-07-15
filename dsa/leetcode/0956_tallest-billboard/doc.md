# Tallest Billboard

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 956 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [tallest-billboard](https://leetcode.com/problems/tallest-billboard/) |

## Problem Description

### Goal

You are installing a billboard that needs two steel supports of equal height, one on each side. The supplied `rods` may be welded end to end, so a support's height is the sum of the rods assigned to it.

Assign any disjoint subsets of rods to the two supports; rods may also remain unused. Among all assignments whose two support sums are equal, return the greatest common height. If no positive equal supports can be built, return `0`.

### Function Contract

Let $N$ be the number of rods and define

$$
S = \sum_{r \in \texttt{rods}} r.
$$

**Inputs**

- `rods`: a list of $N$ positive lengths, where $1 \le N \le 20$, `1 <= rods[i] <= 1000`, and $S \le 5000$.

**Return value**

Return the maximum equal height of two supports formed from disjoint rod subsets, or `0` when no positive equal construction exists.

### Examples

**Example 1**

- Input: `rods = [1,2,3,6]`
- Output: `6`
- Explanation: Weld `1`, `2`, and `3` for one support and use `6` for the other.

**Example 2**

- Input: `rods = [1,2,3,4,5,6]`
- Output: `10`
- Explanation: The subsets `{2,3,5}` and `{4,6}` both total 10.

**Example 3**

- Input: `rods = [1,2]`
- Output: `0`

### Required Complexity

- **Time:** $O(NS)$
- **Space:** $O(S)$

<details>
<summary>Approach</summary>

#### General

**Compress two support totals into their difference.** Maintain a map from a nonnegative height difference to the greatest possible shorter-support height for that difference. The initial state is difference zero with shorter height zero.

**Consider all three choices for each rod.** Copy the current states so leaving the rod unused remains possible. For a state with difference `difference` and shorter height `shorter`, adding the rod to the taller support produces difference `difference + rod` without changing `shorter`. Adding it to the shorter support produces `abs(difference - rod)`; the new shorter height increases by `min(difference, rod)`, because that much of the rod first closes the gap before any excess makes this side taller.

**Keep only the dominant state for each difference.** If two assignments have the same difference, the one with the greater shorter support is always at least as useful: future rods see the same imbalance and can only preserve or increase both resulting heights from the larger baseline. Discarding the smaller state therefore cannot remove an optimum.

After every rod has been considered, difference zero represents equal supports, and its stored shorter height is their common height. Since every rod transition includes unused, left-support, and right-support choices, the DP covers every valid disjoint assignment and returns the tallest one.

#### Complexity detail

Every reachable difference lies from 0 through $S$, so each of $N$ rods updates at most $S+1$ states. This gives $O(NS)$ time. The current and copied difference maps contain $O(S)$ entries and use $O(S)$ space.

#### Alternatives and edge cases

- **Track both support totals:** Store every reachable pair `(left, right)` and transition each rod among unused, left, and right choices. This is correct but can require $O(S^2)$ states and $O(NS^2)$ time.
- **Meet in the middle:** Enumerate three choices per rod in each half and combine compatible differences. This can work for $N \le 20$ but is more intricate and still exponential in half the rod count.
- **Use every rod:** Requiring all rods to participate is incorrect; an optimal equal construction may leave rods unused.
- **One rod:** It cannot form two positive supports, so the answer is zero.
- **Duplicate lengths:** Rods are separate physical items even when their lengths match.
- **Zero difference:** The stored value, not the total assigned length, is the height of either support.

</details>
