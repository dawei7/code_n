# Check if Word Can Be Placed In Crossword

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2018 |
| Difficulty | Medium |
| Topics | Array, Matrix, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/) |

## Problem Description

### Goal

The crossword board contains lowercase letters, spaces representing empty
cells, and `#` characters representing blocked cells.

Determine whether `word` can occupy one horizontal or vertical slot, in either
forward or backward order. Every occupied cell must be non-blocked and either
blank or already contain the required letter. The cells immediately before
and after the word along its direction must be outside the board or blocked;
therefore, the word must fill an entire maximal non-blocked slot rather than
only part of a longer run.

### Function Contract

Let $R$ and $C$ be the board's row and column counts.

**Inputs**

- `board`: an $R\times C$ matrix whose cells are spaces, `#`, or lowercase
  English letters, with $1\le RC\le2\cdot10^5$.
- `word`: a lowercase string of length from $1$ through $\max(R,C)$.

**Return value**

Return `true` if at least one complete horizontal or vertical slot accepts the
word in either direction; otherwise return `false`.

### Examples

**Example 1**

- Input: `board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc"`
- Output: `true`
- Explanation: The word fits vertically from top to bottom.

**Example 2**

- Input: `board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word = "ac"`
- Output: `false`
- Explanation: Each possible vertical run is longer than the word or contains
  incompatible letters.

**Example 3**

- Input: `board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca"`
- Output: `true`
- Explanation: The word fits horizontally from right to left.

### Required Complexity

- **Time:** $O(RC)$
- **Space:** $O(\max(R,C))$

<details>
<summary>Approach</summary>

#### General

**Treat blockers and board edges as slot boundaries.** Traverse every row and
every column. Accumulate cells until `#` or the line's end is reached; that
accumulation is one maximal non-blocked segment. A segment whose length differs
from `word` cannot be a legal slot because an adjacent non-blocked cell would
remain outside the placed word.

**Check both orientations with the same segment.** For an equal-length
segment, compare its cells with `word`, accepting a cell when it is blank or
matches the corresponding letter. Repeat against the reversed word. Return
immediately when either orientation matches.

Every horizontal or vertical placement belongs to exactly one maximal
non-blocked row or column segment. The boundary rule makes equal segment and
word lengths necessary, and the cellwise predicate is exactly the remaining
compatibility rule. Conversely, any segment passing one orientation check
provides an unblocked, fully bounded legal placement. Inspecting all row and
column segments is therefore complete.

#### Complexity detail

Each of the $RC$ cells is visited once in its row and once in its column.
Compatibility checks across disjoint segments inspect at most the same total
number of cells, so time is $O(RC)$. The current segment stores at most
$\max(R,C)$ cells, giving $O(\max(R,C))$ space.

#### Alternatives and edge cases

- **Try every start and direction:** Rechecking up to the word length from
  every cell is correct with boundary validation but can take
  $O(RC\lvert\texttt{word}\rvert)$ time.
- **Materialize a transposed board:** This simplifies shared row logic but uses
  $O(RC)$ additional space; column iterators avoid the copy.
- A matching prefix inside a longer unblocked run is invalid.
- Existing letters must match exactly, while spaces accept any letter.
- A one-cell word may occupy a one-cell slot bounded by edges or blockers.

</details>
