# Flip Game II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 294 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Backtracking, Memoization, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/flip-game-ii/) |

## Problem Description
### Goal
Two players alternate turns on a string containing only `+` and `-`. A legal move changes one adjacent `"++"` pair into `"--"`, permanently removing that pair as plus signs. The first player moves from the supplied initial state.

Assuming optimal play, return `True` when the first player can choose moves that guarantee the opponent eventually faces a state with no legal move. Return `False` when the opponent can force that outcome against every first choice, including when the initial state already has no flippable pair. The result is strategic existence, not a list of winning moves or game states.

### Function Contract
**Inputs**

- `currentState`: the initial row of plus and minus symbols

**Return value**

`True` exactly when the first player has a winning strategy.

### Examples
**Example 1**

- Input: `currentState = "++++"`
- Output: `true`

**Example 2**

- Input: `currentState = "+"`
- Output: `false`

**Example 3**

- Input: `currentState = "++"`
- Output: `true`

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Minus signs reveal the game's structure**

A minus sign never becomes plus again, so play in one maximal run of pluses cannot affect another run. The board is therefore a sum of independent impartial games rather than one indivisible string state.

**What a move does to one run**

Consider a plus run of length `L`. Flipping the pair beginning after `i` pluses leaves two independent runs:

- a left run of length `i`;
- a right run of length $L - i - 2$.

Those are every possible move from the run. Runs of length zero or one have no move.

**Turn the recurrence into Grundy numbers**

Let $g(L)$ be the Grundy value for a run of length $L$. A move at split $i$ reaches the combined value
$g(i) \oplus g(L-i-2)$. Collect these values for all $i$, then set $g(L)$ to their minimum excluded nonnegative integer (mex). Because every child run is shorter than $L$, the table can be filled from small lengths upward.

For example, $g(2) = 1$: its only move reaches two empty runs with xor zero. A four-plus run can reach xor values zero and one, so its mex is two.

**Decide the entire board with xor**

Sprague-Grundy theory combines independent games by xor. Xor `g[length]` for every plus run. A zero total is losing; a nonzero total is winning because a move exists that makes the total zero. Thus `++--++` loses—the two identical value-one games cancel—while `++++--++` wins.

#### Complexity detail

Computing all run lengths through `n` examines $O(n^2)$ split positions. The Grundy table and the reachable-value set for one length use $O(n)$ space.

#### Alternatives and edge cases

- Memoizing complete strings avoids duplicate recursion but still distinguishes exponentially many combinations of flipped pairs.
- Unmemoized minimax revisits those states and grows even faster.
- Runs of length zero or one contribute Grundy value zero; an input without `++` is therefore losing immediately.

</details>
