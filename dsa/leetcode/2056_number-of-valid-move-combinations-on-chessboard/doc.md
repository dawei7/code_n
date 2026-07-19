# Number of Valid Move Combinations On Chessboard

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2056 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Backtracking, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/) |

## Problem Description

### Goal

An $8\times8$ chessboard contains up to four distinct pieces, each a rook, bishop, or queen. For every piece, choose a destination reachable in one legal straight direction; choosing its current square is also allowed. All chosen moves begin together at second zero.

At each following second, a piece that has not reached its destination advances exactly one square along its chosen direction, while a finished piece remains still. A move combination is valid only if no two pieces occupy the same square at any integer time. Pieces may swap adjacent squares during one second because they never share a square at either endpoint. Count all valid combinations of destinations.

### Function Contract

**Inputs**

- `pieces`: an array of $p$ values from `"rook"`, `"bishop"`, and `"queen"`, where $1 \le p \le 4$ and at most one value is `"queen"`.
- `positions`: distinct one-based squares `[row, column]`, with both coordinates from $1$ through $8$, corresponding to `pieces`.

**Return value**

- Return the number of simultaneous destination choices that never place two pieces on one square at the same integer second.

### Examples

**Example 1**

- Input: `pieces = ["rook"], positions = [[1,1]]`
- Output: `15`
- Explanation: The rook may stay or choose any of the other fourteen squares in its row or column.

**Example 2**

- Input: `pieces = ["queen"], positions = [[1,1]]`
- Output: `22`

**Example 3**

- Input: `pieces = ["bishop"], positions = [[4,3]]`
- Output: `12`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Encoding a complete move**

For each piece, enumerate staying still plus every reachable destination along each legal direction. Represent a choice by its row step, column step, and travel distance. A rook has at most 15 choices, a bishop at most 14, and the single possible queen at most 28.

**Precomputing pairwise trajectory compatibility**

For every pair of pieces and pair of their moves, simulate seconds zero through seven, since no straight move lasts longer. At second `t`, a piece has traveled `min(t, distance)` steps; after arriving, this keeps it at its destination. Record the move pair as compatible only when their squares differ at every time.

Backtrack through pieces and accept a candidate move only if it is compatible with every move already chosen. Pairwise distinctness is equivalent to no square containing two or more pieces, so a complete backtracking assignment is valid exactly when the simultaneous combination is valid. Crossing or swapping between integer seconds is correctly left valid.

#### Complexity detail

The source domain is fixed: the board has 64 squares, $p\le4$, and at most one queen. The largest move-choice product is at most $28\cdot15^3=94{,}500$; pairwise tables compare at most eight times per move pair, and backtracking explores no more than that product. These are contract-wide constants, so runtime and auxiliary storage are $O(1)$ under the legal domain. The bounded-domain certificate records this finite-work argument.

#### Alternatives and edge cases

- **Incremental backtracking with pairwise trajectory checks:** Reject a new move as soon as it conflicts with an already chosen trajectory. This prunes combinations earlier but requires a more delicate collision predicate.
- **Destination-only validation:** Comparing only final squares is insufficient because pieces can collide while traveling or with a piece that stopped earlier.
- Staying at the starting square is a valid move and can cause later collisions with moving pieces.
- Two adjacent pieces may swap squares in one second; only equal positions at the same integer time are invalid.
- Pieces that finish early remain on their destination for all remaining seconds.

</details>
