# Kth Smallest Instructions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1643 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/kth-smallest-instructions/) |

## Problem Description
### Goal
Starting at cell $(0,0)$, reach `destination = [row, column]` using only right and down moves. Encode a rightward horizontal move as `H` and a downward vertical move as `V`, so every valid instruction contains exactly `column` copies of `H` and `row` copies of `V`.

Sort all valid instruction strings lexicographically, with the usual character ordering in which `H` precedes `V`. Return the 1-indexed `k`th string in that ordering.

### Function Contract
**Inputs**

- `destination`: `[row, column]`, where $1 \le \texttt{row},\texttt{column} \le 15$.
- `k`: a 1-indexed rank satisfying

$$
1 \le k \le \binom{\texttt{row}+\texttt{column}}{\texttt{row}}.
$$

**Return value**

Return the `k`th lexicographically smallest instruction string that reaches the destination.

### Examples
**Example 1**

- Input: `destination = [2,3], k = 1`
- Output: `"HHHVV"`

**Example 2**

- Input: `destination = [2,3], k = 2`
- Output: `"HHVHV"`

**Example 3**

- Input: `destination = [2,3], k = 3`
- Output: `"HHVVH"`

### Required Complexity
- **Time:** $O(r+c)$
- **Space:** $O(r+c)$

<details>
<summary>Approach</summary>

#### General

**Count the block beginning with `H`.** Suppose $h$ horizontal and $v$ vertical moves remain. If the next character is `H`, the suffix contains $h-1$ horizontal moves and $v$ vertical moves in any order, giving

$$
\binom{h+v-1}{v}
$$

strings. Because `H` is lexicographically smaller than `V`, those strings form the first contiguous block among all instructions for the current state.

**Unrank one character at a time.** If `k` does not exceed the `H`-block size, append `H` and reduce $h$. Otherwise skip that entire block, append `V`, reduce $v$, and subtract the block size from `k`. Once either move type is exhausted, append every remaining move of the other type.

At each step, the block count partitions the current lexicographic range exactly into strings beginning with `H` and strings beginning with `V`. Selecting the block containing `k` and translating the rank within that block preserves the requested 1-indexed rank. Repeating until the path is complete therefore returns exactly the `k`th instruction.

#### Complexity detail

The algorithm emits one character for each of the $r+c$ required moves and stores the result, taking $O(r+c)$ time and $O(r+c)$ output space. Binomial coefficients involve at most 29 remaining positions under the source constraints. Because the complete legal output length is bounded by 30, the package uses a bounded-domain certificate with independent exhaustive rank checks on small grids and maximum-boundary checks rather than a misleading runtime trend.

#### Alternatives and edge cases

- **Pascal-triangle dynamic programming:** Precompute every binomial count through $r+c$ and perform the same unranking. It is correct but uses $O((r+c)^2)$ time and space unnecessarily.
- **Generate and sort every instruction:** Enumeration requires $\binom{r+c}{r}$ strings and is infeasible near the boundary.
- **Depth-first search with rank pruning:** Subtree counts lead back to the same combinatorial unranking; without them, DFS may visit exponentially many earlier paths.
- Rank 1 always places all `H` moves before all `V` moves.
- The maximum valid rank places every `V` before every `H`.
- `k` remains 1-indexed after choosing the `H` block; it is reduced only when the entire `H` block is skipped.
- Both destination coordinates are positive, but the final append still handles either move type becoming exhausted first.

</details>
