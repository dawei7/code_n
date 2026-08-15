# Construct String with Minimum Cost

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3213 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Dynamic Programming, Suffix Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/construct-string-with-minimum-cost/) |

## Problem Description

### Goal

Start with an empty string `s`. The arrays `words` and `costs` have equal length; choosing index `i` appends the entire string `words[i]` to the end of `s` and adds `costs[i]` to the total cost.

An index may be chosen any number of times, so dictionary words may be reused. Appends cannot overlap, skip target positions, or be undone: the selected words in order must concatenate to exactly `target`.

Return the minimum total cost of any exact construction. If no sequence of available words forms `target`, return `-1`.

### Function Contract

**Inputs**

- `target`: A nonempty lowercase string of length $N$, with $1 \le N \le 5\cdot10^4$.
- `words`: A nonempty list of lowercase strings paired positionally with `costs`. Each word length is between $1$ and $N$.
- `costs`: Positive operation costs, each at most $10^4$.

Let $S$ be the sum of all word lengths and $D$ the number of distinct word lengths. Both $N$ and $S$ are at most $5\cdot10^4$.

**Return value**

- The minimum cost of concatenating dictionary words into `target`, or `-1` when no construction exists.

### Examples

#### Example 1

- **Input:** `target = "abcdef", words = ["abdef","abc","d","def","ef"], costs = [100,1,1,10,5]`
- **Output:** `7`
- **Explanation:** Append `"abc"`, `"d"`, and `"ef"` for costs $1+1+5$.

#### Example 2

- **Input:** `target = "aaaa", words = ["z","zz","zzz"], costs = [1,10,100]`
- **Output:** `-1`
- **Explanation:** No available word can match the required prefix.
