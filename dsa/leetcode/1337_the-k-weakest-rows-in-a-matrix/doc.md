# The K Weakest Rows in a Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1337 |
| Difficulty | Easy |
| Topics | Array, Binary Search, Sorting, Heap (Priority Queue), Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/) |

## Problem Description
### Goal
An $m\times n$ binary matrix represents soldiers with 1 and civilians with 0. Within every row, all soldiers stand before all civilians, so each row consists of a prefix of 1s followed by a suffix of 0s.

Row $i$ is weaker than row $j$ when it has fewer soldiers. If their soldier counts are equal, the row with the smaller index is weaker.

Return the indices of the `k` weakest rows, ordered from weakest to strongest under that comparison.

### Function Contract
**Inputs**

- `mat`: an $m\times n$ binary matrix, where $2\le m,n\le100$, and every row has all its 1s before its 0s.
- `k`: the number of row indices to return, where $1\le k\le m$.

**Return value**

An array containing exactly the `k` weakest row indices in increasing strength order, breaking equal-strength ties by smaller index.

### Examples
**Example 1**

- Input: `mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]`, `k = 3`
- Output: `[2,0,3]`

**Example 2**

- Input: `mat = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]`, `k = 2`
- Output: `[0,2]`

**Example 3**

- Input: `mat = [[0,0],[0,0],[1,1]]`, `k = 2`
- Output: `[0,1]`
- Explanation: Rows 0 and 1 both contain no soldiers, so their indices decide their order.

### Required Complexity
- **Time:** $O(m\log n+m\log m)$
- **Space:** $O(m)$

<details>
<summary>Approach</summary>

#### General

**Locate each row's boundary**

Because every row changes at most once from 1 to 0, its soldier count is the position of its first 0. Use binary search over the half-open interval from 0 through $n$: when the middle cell is 1, move the lower boundary right; otherwise move the upper boundary left. The converged position is 0 for an all-civilian row and $n$ for an all-soldier row.

Pair that count with the row index. Sorting the pairs lexicographically first compares soldier counts and then indices, exactly matching the definition of weaker. Return the indices from the first `k` pairs.

Binary search yields the exact prefix length because positions before the boundary are 1 and positions at or after it are 0. The sorted pair order therefore represents every row's true strength and applies the required tie rule, making its first `k` entries precisely the requested rows.

#### Complexity detail

Binary search costs $O(\log n)$ for each of $m$ rows, and sorting the $m$ pairs costs $O(m\log m)$. The total is $O(m\log n+m\log m)$. The strength pairs and returned indices use $O(m)$ space.

#### Alternatives and edge cases

- **Sum every row:** Since cells are binary, `sum(row)` obtains the same strength simply, but reads all $mn$ cells and takes $O(mn+m\log m)$ time.
- **Size-$k$ heap:** Maintaining only the weakest candidates can reduce ordering work when $k$ is much smaller than $m$, at the cost of more involved tie handling.
- **All civilians:** Binary search returns a strength of zero.
- **All soldiers:** The boundary falls just after the final column, giving strength $n$.
- **Equal strengths:** The smaller row index must appear first.
- **Return every row:** When $k=m$, the result is the complete strength ordering.

</details>
