# Number of Ways to Rearrange Sticks With K Sticks Visible

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1866 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/) |

## Problem Description
### Goal
There are $n$ sticks with distinct integer lengths $1$ through $n$. Arrange all
sticks in a row. A stick is visible when viewed from the left exactly when no
longer stick occurs anywhere before it; equivalently, it establishes a new
maximum length while scanning the arrangement from left to right.

Count the permutations in which exactly $k$ sticks are visible. Return the
count modulo $10^9+7$.

### Function Contract
**Inputs**

- `n`: the number of uniquely sized sticks, with $1 \le n \le 1000$.
- `k`: the required number visible from the left, with $1 \le k \le n$.

**Return value**

The number of permutations of lengths $1,\ldots,n$ having exactly $k$ visible
sticks, reduced modulo $1{,}000{,}000{,}007$.

### Examples
**Example 1**

- Input: `n = 3, k = 2`
- Output: `3`

**Example 2**

- Input: `n = 5, k = 5`
- Output: `1`

Only the strictly increasing arrangement exposes every stick.

**Example 3**

- Input: `n = 20, k = 11`
- Output: `647427950`

### Required Complexity
- **Time:** $O(nk)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

Let $D(i,j)$ be the number of arrangements of sticks $1$ through $i$ with
exactly $j$ visible sticks. Begin with $D(0,0)=1$.

**Insert the shortest stick**

Take an arrangement counted for $i-1$ sticks, increase all its lengths by one,
and insert the new shortest stick of length one. If it is inserted at the
front, it is visible and every later visibility decision is unchanged, so this
creates $D(i-1,j-1)$ arrangements with $j$ visible sticks.

At any of the other $i-1$ positions, at least one longer stick precedes the new
shortest stick. It is therefore hidden and does not change the visible count.
Each arrangement counted by $D(i-1,j)$ yields $i-1$ such placements. Hence

$$
D(i,j)=D(i-1,j-1)+(i-1)D(i-1,j).
$$

The front and non-front cases are disjoint and cover every insertion position;
removing the unique shortest stick reverses the construction, so every target
permutation is counted exactly once. Compute rows from smaller to larger $i$,
reducing each state modulo $10^9+7$, and retain only the previous row.

#### Complexity detail

For each of $n$ row sizes, at most $k$ visibility states are evaluated in
constant time, for $O(nk)$ total time. Two arrays of length $k+1$ hold the
previous and current rows, using $O(k)$ space.

#### Alternatives and edge cases

- **Memoized recursion:** it uses the same recurrence and $O(nk)$ time but
  stores $O(nk)$ states and risks recursion-depth failure near $n=1000$.
- **Unmemoized recursion:** it repeats the two subproblems exponentially.
- Exactly one stick is visible only when every later stick is shorter than the
  first; the count is $(n-1)!$.
- All $n$ sticks are visible only in increasing order, so $D(n,n)=1$.
- States with $j>i$ are impossible and remain zero.

</details>
