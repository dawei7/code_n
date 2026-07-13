# Stone Game VIII

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1872 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Prefix Sum, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [stone-game-viii](https://leetcode.com/problems/stone-game-viii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/stone-game-viii/).

### Goal
Players repeatedly choose a prefix of at least two stones, score the sum of that prefix, and replace the prefix with one stone of that sum. Both play optimally. Find Alice's final score minus Bob's final score.

### Function Contract
**Inputs**

- `stones`: a list of integers.

**Return value**

Return the optimal score difference for Alice.

### Examples
**Example 1**

- Input: `stones = [-1,2,-3,4,-5]`
- Output: `5`

**Example 2**

- Input: `stones = [7,-6,5,10,5,-2,-6]`
- Output: `13`

**Example 3**

- Input: `stones = [-10,-12]`
- Output: `-22`

---

## Solution
### Approach
Convert `stones` to prefix sums. If a player chooses prefix ending at `i`, the score gained is `prefix[i]`, and the opponent then faces the suffix state. Work backward maintaining the best achievable difference from later choices: `best = max(best, prefix[i] - best)` for candidate prefix endings.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` besides prefix sums, or `O(1)` extra if prefixing in place

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
