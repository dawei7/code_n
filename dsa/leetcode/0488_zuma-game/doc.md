# Zuma Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 488 |
| Difficulty | Hard |
| Topics | String, Dynamic Programming, Stack, Breadth-First Search, Memoization |
| Official Link | [LeetCode](https://leetcode.com/problems/zuma-game/) |

## Problem Description
### Goal
You have one row of colored balls on the board and a small collection of balls in your hand. On each turn, choose one hand ball and insert it between two board balls or at either end. Whenever three or more consecutive balls of one color form a group, that group is removed; the resulting neighbors may form another removable group, and this reaction continues until the row is stable.

Return the minimum number of inserted balls needed to remove every ball from the board, or `-1` when it is impossible to clear the row with the available hand. Each hand occurrence may be used at most once, insertion order matters, and clearing a group can be useful because it joins formerly separated colors for a later chain reaction.

### Function Contract
**Inputs**

- `board`: the current row using `R`, `Y`, `B`, `G`, and `W`
- `hand`: the available multiset of balls encoded with the same letters

**Return value**

- The minimum number of insertions needed to empty the board, or `-1`

### Examples
**Example 1**

- Input: `board = "WRRBBW", hand = "RB"`
- Output: `-1`

**Example 2**

- Input: `board = "WWRRBBWW", hand = "WRBRW"`
- Output: `2`

**Example 3**

- Input: `board = "G", hand = "GGGGG"`
- Output: `2`

### Required Complexity

- **Time:** $O((n + h)^{h + 1})$
- **Space:** $O((n + h)^h)$

<details>
<summary>Approach</summary>

#### General

**Canonicalize every board by collapsing it**

After each insertion, repeatedly remove all runs of length at least three until no further group disappears. Equivalent chain reactions therefore produce the same stable board state.

**Search by number of inserted balls**

Breadth-first states contain the stable board and the five remaining color counts. Each edge inserts one available ball and collapses the result. The first empty board is optimal because all states using `k` balls are processed before states using $k + 1$.

**Generate every useful insertion once**

An insertion is useful when it joins the same color or inserts a different color between an equal pair. The second form is an essential setup move for later cascades. An insertion with neither property creates an isolated ball and can be postponed until it becomes useful. Equivalent positions inside one same-color run are skipped.

**Deduplicate converging histories**

Different insertion orders can reach the same stable board with identical hand counts. A visited set retains only the shallowest occurrence. If the queue empties, no legal sequence can clear the row.

#### Complexity detail

With initial board length $n$ and hand length $h$, there are at most $O((n + h)^h)$ conservatively bounded states. Generating and collapsing successors costs another $O(n + h)$ factor, yielding $O((n + h)^{h + 1})$ time and $O((n + h)^h)$ space.

#### Alternatives and edge cases

- **Memoized depth-first search:** can return the minimum remaining cost from each complete state.
- **Search without a visited set:** is correct but repeats states reached by different insertion orders.
- **Complete existing runs only:** is incomplete because setup insertions between equal balls may be necessary.
- **Try every position and color:** is complete but creates many isolated and duplicate moves.
- **Immediate cascade:** always stabilize before choosing another insertion.
- **Insufficient hand:** exhausted states remain failures.
- **Empty board:** requires zero additional balls.
- **Duplicate hand colors:** counts make their order irrelevant.

</details>
