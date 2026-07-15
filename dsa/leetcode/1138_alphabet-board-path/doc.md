# Alphabet Board Path

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1138 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/alphabet-board-path/) |

## Problem Description

### Goal

The alphabet board is `['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy', 'z']`. A cursor begins on `a` at position `(0, 0)`. `U`, `D`, `L`, and `R` move one cell in the corresponding direction when that destination exists, and `!` appends the letter under the cursor to the answer.

Given a lowercase string `target`, return a minimum-length sequence of moves and selections whose appended letters equal `target`. Every move must remain on a lettered cell; in particular, the last row contains only `z` at column zero. When several minimum paths are valid, any one may be returned.

### Function Contract

**Inputs**

- `target`: a string of lowercase English letters with $1 \le \lvert\texttt{target}\rvert \le 100$.

Let $L=\lvert\texttt{target}\rvert$.

**Return value**

A minimum-length valid command string that selects the letters of `target` in order.

### Examples

**Example 1**

- Input: `target = "leet"`
- Output: `"DDR!UURRR!!DDD!"`

**Example 2**

- Input: `target = "code"`
- Output: `"RR!DDRR!UUL!R!"`

### Required Complexity

- **Time:** $O(L)$
- **Space:** $O(L)$

<details>
<summary>Approach</summary>

#### General

**Convert letters to coordinates.** For a letter with zero-based alphabet index `index`, its board position is `row, column = divmod(index, 5)`. Track the cursor's current row and column, initially `(0, 0)`, and compute the target coordinates for each character.

**Use Manhattan-shortest moves in a safe order.** Any route between two cells needs at least the absolute row difference plus the absolute column difference. Emit exactly that many moves: move up first, then left, then right, and finally down. This ordering matters only around `z`. When leaving `z`, the upward moves reach the full rectangular part before any horizontal move. When entering `z`, leftward movement reaches column zero before the final downward move. Consequently the route never visits a nonexistent cell in row five.

Append `!` after reaching each target coordinate, then retain that coordinate for the next letter. Each segment uses exactly its Manhattan distance and therefore is shortest. Since selections are mandatory and segment endpoints are fixed by consecutive target letters, concatenating these shortest valid segments yields a globally minimum command length.

#### Complexity detail

Each target character requires at most nine directional moves on this fixed board plus one selection. Building command fragments and joining them therefore takes $O(L)$ time. The returned command string and fragment list contain $O(L)$ characters, so auxiliary output-building space is $O(L)$.

#### Alternatives and edge cases

- **Breadth-first search per letter:** BFS finds a shortest board route but repeatedly explores a fixed graph when coordinate differences give the route directly.
- **Horizontal movement before vertical movement:** This works on the five complete rows but can step into a nonexistent cell when entering or leaving `z`.
- **Target letter `z`:** Reach column zero before moving down into the one-cell final row.
- **Current letter `z`:** Move up out of the final row before moving right toward another letter.
- **Repeated letter:** No directional move is needed; append only `!` for each repeated occurrence.
- **Minimum requirement:** Extra detours may still spell the target, but they do not satisfy the requested minimum number of moves.

</details>
