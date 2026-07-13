# Flip Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 293 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/flip-game/) |

## Problem Description
### Goal
Given a string containing only `+` and `-`, one legal move selects two adjacent plus signs and changes that pair from `"++"` to `"--"`. Every other character remains in its original position and state.

Return all states reachable by making exactly one legal move, in any order. Overlapping pairs represent different choices and may produce different states. Do not include the unchanged input or states requiring several moves. When no adjacent plus pair exists, return an empty list. The output strings retain the same length as the input.

### Function Contract
**Inputs**

- `currentState`: the current row of plus and minus symbols

**Return value**

A list containing one next-state string for each flippable adjacent pair, in left-to-right pair order.

### Examples
**Example 1**

- Input: `currentState = "++++"`
- Output: `["--++", "+--+", "++--"]`

**Example 2**

- Input: `currentState = "+"`
- Output: `[]`

**Example 3**

- Input: `currentState = "++"`
- Output: `["--"]`

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**A move is determined by one index**

There is no game-tree search in this problem: only the immediate next states are requested. A legal move is completely identified by the left index `i` of an adjacent `++` pair. Scan those possible starts from left to right.

Only after confirming a pair is legal, construct
`currentState[:i] + "--" + currentState[i+2:]`. This changes exactly two symbols and preserves every other position. Since every legal move has one such left index, the scan produces all and only the requested states.

**Overlap is intentional**

In `+++`, the pairs beginning at zero and one overlap, but they represent different single moves and must both appear. Advancing the scan by one position handles this naturally. By contrast, a string shorter than two characters or one without `++` produces no states.

#### Complexity detail

There are at most $n - 1$ moves, and each returned immutable string has length `n`. Merely materializing the worst-case answer therefore needs $O(n^2)$ time and space. Building strings at every index before checking legality wastes that cost on non-moves; checking first keeps sparse-output inputs efficient.

#### Alternatives and edge cases

- Constructing a candidate at every index is correct but performs quadratic work even when only one pair is legal.
- Overlapping pairs are distinct moves and must not be skipped after the first match.
- Inputs shorter than two characters, or inputs with no `++`, return an empty list.

</details>
