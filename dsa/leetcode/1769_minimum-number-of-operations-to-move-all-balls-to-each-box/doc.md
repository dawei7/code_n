# Minimum Number of Operations to Move All Balls to Each Box

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1769 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/) |

## Problem Description

### Goal

A binary string `boxes` describes $n$ boxes arranged in a line. Character `0` means that a box is empty, while `1` means that it initially contains one ball.

One operation moves one ball from its current box to an adjacent box. Several balls may occupy the same box after moves.

For every possible target index, determine the minimum operations needed to bring all balls to that box. Calculate each target independently from the original configuration and return all $n$ costs.

### Function Contract

**Inputs**

- `boxes`: a binary string of length $n$, where $1 \le n \le 2000$.
- `boxes[i] = "1"` means box `i` initially contains one ball; `"0"` means it is empty.

**Return value**

- Return an integer array `answer` of length $n$.
- `answer[i]` is the minimum number of adjacent one-step ball moves required to gather every initially present ball in box `i`.

### Examples

**Example 1**

- Input: `boxes = "110"`
- Output: `[1,1,3]`
- Explanation: Gathering at indices `0` or `1` costs one move; gathering at index `2` costs two moves for the first ball and one for the second.

**Example 2**

- Input: `boxes = "001011"`
- Output: `[11,8,5,4,3,4]`
- Explanation: Each entry sums the distances from the balls initially at indices `2`, `4`, and `5`.

**Example 3**

- Input: `boxes = "0"`
- Output: `[0]`
- Explanation: With no balls present, every required movement cost is zero.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Express a target cost as independent distances**

A ball starting at index $j$ needs exactly $\lvert i-j\rvert$ adjacent moves to reach target $i$. Balls do not obstruct one another and may share a box, so the minimum cost for target $i$ is the sum of these distances over all positions containing a ball.

**Accumulate contributions from the left**

Sweep indices from left to right. Before processing index `i`, let `balls` be the number of balls strictly to its left and `moves` their total distance to `i`. Add `moves` to `answer[i]`. After including a possible ball at `i`, advancing the target one position right increases every seen ball's distance by one, so update `moves` by `balls`.

**Add the symmetric right contribution**

Reset the two counters and sweep from right to left. They now describe balls strictly to the right and their distance to the current index. Add this second `moves` value to the existing answer, include the current ball, and again increase the next position's cost by the number of seen balls.

**Preserve the initial configuration**

Neither sweep moves or removes a ball; both read the same original bits. For each target, the first pass supplies every term with $j<i$ and the second supplies every term with $j>i$. A ball already at the target contributes zero. Together the passes produce the full distance sum, which is the independent minimum required by the contract.

#### Complexity detail

Each sweep visits all $n$ positions once and performs constant work per position, giving $O(n)$ time. The returned answer array uses $O(n)$ space; aside from that required output, the algorithm maintains only four integer counters and loop indices.

#### Alternatives and edge cases

- **Sum distances for every target:** Directly checking every box for each answer is correct but takes $O(n^2)$ time.
- **Store full prefix sums:** Prefix counts and index sums can also answer each target in constant time after linear preprocessing, but two running sweeps use less auxiliary state.
- **No balls:** Both counters remain zero, so every answer is zero.
- **One ball:** The answer is the absolute distance from that ball's initial index.
- **All boxes occupied:** Every index contributes one distance term to every target.
- **Several balls in the destination:** The operation rules allow co-location, so no capacity adjustment is needed.
- **Independent targets:** Computing one answer must not mutate the configuration used for another.
- **Endpoint targets:** A single directional sweep supplies all nonzero contributions at an endpoint.

</details>
