# Stone Game VIII

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/stone-game-viii/) |
| Frontend ID | 1872 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Prefix Sum, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Alice and Bob alternate turns on a row of stones, with Alice moving first. While more than one stone remains, the current player chooses a prefix containing at least two stones, removes that prefix, adds its total value to their score, and inserts one new stone with that same total at the left end of the remaining row.

The game ends with one stone. Alice chooses moves to maximize `Alice score - Bob score`, while Bob chooses moves to minimize it. Given the initial stone values, which may be negative, return the final score difference under optimal play. A move may combine any legal prefix, including the entire current row.

### Function Contract

**Inputs**

- `stones`: a list of $N$ integers with $2 \le N \le 10^5$ and $-10^4 \le \texttt{stones[i]} \le 10^4$.

**Return value**

- Return Alice's score minus Bob's score when both players choose optimally.

### Examples

**Example 1**

- Input: `stones = [-1,2,-3,4,-5]`
- Output: `5`

Alice can combine the first four stones for `2`; Bob then combines `[2,-5]` for `-3`, giving difference $2-(-3)=5$.

**Example 2**

- Input: `stones = [7,-6,5,10,5,-2,-6]`
- Output: `13`

Alice can combine the entire row immediately and score its total, `13`.

**Example 3**

- Input: `stones = [-10,-12]`
- Output: `-22`

Only one move is legal, so Alice must score the total `-22`.
