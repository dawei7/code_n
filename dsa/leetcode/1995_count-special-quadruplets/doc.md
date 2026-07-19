# Count Special Quadruplets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1995 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/count-special-quadruplets/) |

## Problem Description

### Goal

Given a zero-indexed integer array `nums`, count the distinct quadruplets of indices $(a,b,c,d)$ whose values satisfy

$$
\texttt{nums[a]}+\texttt{nums[b]}+\texttt{nums[c]}=\texttt{nums[d]}.
$$

The four positions must also occur in strict order: $a<b<c<d$. Quadruplets are distinguished by their indices, so repeated array values may participate in several different valid choices.

### Function Contract

**Inputs**

- `nums`: an array of length $N$, where $4 \le N \le 50$ and $1 \le \texttt{nums[i]} \le 100$.
- Let $V$ denote the number of possible differences `nums[d] - nums[c]` under the value constraints.

**Return value**

Return the number of ordered index quadruplets satisfying both the value equation and $a<b<c<d$.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3, 6]`
- Output: `1`
- Explanation: Only $(0,1,2,3)$ works because $1+2+3=6$.

**Example 2**

- Input: `nums = [3, 3, 6, 4, 5]`
- Output: `0`

**Example 3**

- Input: `nums = [1, 1, 1, 3, 5]`
- Output: `4`
- Explanation: One quadruplet ends at the value `3`, and three index-distinct choices of two earlier ones accompany `3` to produce `5`.

### Required Complexity

- **Time:** $O(N^2)$
- **Space:** $O(V)$

<details>
<summary>Approach</summary>

#### General

**Split the equation into two ordered pairs.** Rearranging the required equality gives

$$
\texttt{nums[a]}+\texttt{nums[b]}
=
\texttt{nums[d]}-\texttt{nums[c]}.
$$

This suggests matching an earlier pair sum against a later pair difference while preserving the boundary $b<c$.

**Move the boundary from right to left.** Let `second` represent $b$ and visit it from $N-3$ down to $1$. Before counting earlier pairs for this boundary, set $c=b+1$ and add every difference `nums[d] - nums[c]` for $d>c$ to a frequency map. Differences added during previous iterations already represent larger values of $c$, so the map now contains exactly all later pairs with $b<c<d$.

**Match every possible first index.** For each $a<b$, look up `nums[a] + nums[b]` in the difference map and add its frequency. Every counted match satisfies the equation and index order by construction. Conversely, a valid quadruplet is counted when the sweep reaches its particular $b$: its $(c,d)$ difference has entered the map, and its $a$ is queried. No other boundary can reproduce the same four indices.

#### Complexity detail

Each ordered pair is inserted into or queried from the frequency map once across the sweep, giving $O(N^2)$ expected time. The map stores at most $V$ distinct differences, so it uses $O(V)$ space. With values from $1$ through $100$, $V$ is bounded independently of $N$.

#### Alternatives and edge cases

- **Enumerate all four indices:** Four nested loops are straightforward but take $O(N^4)$ time.
- **Enumerate triples with a suffix frequency table:** Counting possible `nums[d]` values after each $c$ reduces the direct method to $O(N^3)$ time, but still repeats work for every earlier pair.
- Equal values at different positions must be counted separately because quadruplets are index-distinct.
- A numerically valid combination in the wrong positional order does not count.
- The smallest legal input has exactly one possible quadruplet, which may still fail the value equation.
- A difference may be negative; a general frequency map handles the complete legal range without special indexing.

</details>
