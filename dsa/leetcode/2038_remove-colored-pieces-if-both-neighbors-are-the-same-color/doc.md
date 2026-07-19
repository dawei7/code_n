# Remove Colored Pieces if Both Neighbors are the Same Color

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2038 |
| Difficulty | Medium |
| Topics | Math, String, Greedy, Game Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/) |

## Problem Description

### Goal

A line contains pieces colored either `"A"` or `"B"`, represented in order by
the string `colors`. Alice and Bob alternate turns, with Alice moving first.
Alice may remove only an `"A"` piece whose immediate left and right neighbors
are both `"A"`; Bob has the corresponding rule for `"B"`.

Neither player may remove a piece at an edge of the current line. A player who
has no legal removal on their turn loses immediately. Assuming both players
play optimally, return whether Alice wins.

### Function Contract

Let $N$ be the length of `colors`.

**Inputs**

- `colors`: a string of only `"A"` and `"B"`, with
  $1 \le N \le 10^5$.

**Return value**

- `true` if Alice wins under optimal play; otherwise `false`.

### Examples

**Example 1**

- Input: `colors = "AAABABB"`
- Output: `true`
- Explanation: Alice removes the middle piece from the initial `"AAA"` run,
  after which Bob has no legal move.

**Example 2**

- Input: `colors = "AA"`
- Output: `false`
- Explanation: Neither piece has two neighbors, so Alice loses immediately.

**Example 3**

- Input: `colors = "ABBBBBBBAAA"`
- Output: `false`
- Explanation: Alice has one available removal, while Bob has more than one.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count the removable interior of each run**

In a maximal same-color run of length $L$, only the pieces excluding its two
endpoints initially have equal-colored neighbors. Removing any such interior
piece shortens the same run by one without changing its color boundaries.
Consequently, the run supplies exactly

$$
\max(L-2,0)
$$

legal moves before only its two protected endpoints remain.

**The two move budgets cannot interfere**

A legal removal is strictly inside one monochromatic run. It cannot delete a
run boundary, split the run, merge it with another run, or change any run of
the other color. Thus Alice's total number of possible moves is fixed by all
`"A"` runs, and Bob's is independently fixed by all `"B"` runs. The position
chosen within a run cannot improve or reduce either final budget.

Rather than build runs explicitly, scan each interior index. Every occurrence
whose previous, current, and next characters are all `"A"` contributes one to
Alice's budget; the analogous `"BBB"` triple contributes one to Bob's. A
length-$L$ run contains exactly $L-2$ such centered triples.

**Compare the budgets in turn order**

Alice and Bob each consume one move from their own fixed budget per turn. If
the budgets are equal, Bob can answer Alice's last move and Alice then loses.
If Alice has more moves, Bob exhausts his budget first. Therefore Alice wins
exactly when her counted budget is strictly greater than Bob's.

#### Complexity detail

The scan examines each of the $N$ characters at most once and performs constant
work per index, for $O(N)$ time. Two counters use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Simulate each removal:** Repeatedly searching for a legal triple and
  rebuilding the string is correct but can take $O(N^2)$ time.
- **Explicit run-length encoding:** Summing $\max(L-2,0)$ for each run is also
  linear and makes the fixed-budget interpretation direct.
- Strings shorter than three characters offer no legal move.
- A run of exactly three pieces contributes one move; a run of two contributes
  none.
- Equal move counts favor Bob because Alice moves first and is the first unable
  to continue.
- Alternating colors contain no same-color triple, so Alice loses immediately.
- Long runs at a string edge still contribute interior removals; only the
  current line's outermost pieces themselves are forbidden.

</details>
