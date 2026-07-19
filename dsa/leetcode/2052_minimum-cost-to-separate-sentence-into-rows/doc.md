# Minimum Cost to Separate Sentence Into Rows

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2052 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-to-separate-sentence-into-rows/) |

## Problem Description

### Goal

A sentence contains lowercase words separated by single spaces. Insert line breaks only between words so that every row contains at most `k` characters. Words must remain intact, appear exactly once in their original order, and retain one space between adjacent words placed on the same row; rows have no leading or trailing spaces.

For a non-final row of length $r$, pay $(k-r)^2$. The last row contributes no cost, regardless of its unused capacity. Return the minimum total cost over every valid placement of line breaks. Every individual word is guaranteed to fit within the row width.

### Function Contract

**Inputs**

- `sentence`: a nonempty string of lowercase words separated by one space, with total length at most $5000$.
- `k`: the maximum row length, where $1 \le k \le 5000$ and every word's length is at most `k`.

Let $w$ be the number of words.

**Return value**

- Return the minimum sum of squared unused widths over all rows except the final row.

### Examples

**Example 1**

- Input: `sentence = "i love leetcode", k = 12`
- Output: `36`
- Explanation: Rows `"i love"` and `"leetcode"` cost $(12-6)^2+0=36$.

**Example 2**

- Input: `sentence = "apples and bananas taste great", k = 7`
- Output: `21`
- Explanation: Each word occupies its own row; only the first four contribute costs.

**Example 3**

- Input: `sentence = "a", k = 5`
- Output: `0`
- Explanation: The only row is also the last row, whose cost is excluded.

### Required Complexity

- **Time:** $O(w^2)$
- **Space:** $O(w)$

<details>
<summary>Approach</summary>

#### General

**Choosing the final word of each row**

Let `best[i]` be the least cost for placing the first `i` words, with `best[0] = 0`. For every possible row start, extend its end one word at a time while maintaining the row length. Adding the first word contributes its letters; each later word contributes one separating space plus its letters. Stop extending as soon as the width exceeds `k`.

**Charging every row except the last**

For each valid interval from `start` through `end`, relax `best[end + 1]` from `best[start]`. Its added cost is `(k - row_length) ** 2`, except when `end` is the sentence's final word, in which case it is zero. Incremental length maintenance avoids reconstructing or rejoining the same word intervals.

Every legal layout ends its first row at some enumerated word and leaves the same optimization problem on the remaining suffix. Conversely, each relaxation appends one width-valid row to an already valid optimal prefix. Considering every possible end therefore covers all layouts, and taking the minimum at each prefix yields the global optimum.

#### Complexity detail

There are $w$ possible row starts and at most $w$ ends examined from each start, so the running time is $O(w^2)$. The dynamic-programming array contains $w+1$ values and uses $O(w)$ space.

#### Alternatives and edge cases

- **Top-down memoization:** Recursing on the next word with memoized suffix costs has the same state space, but a sentence with many short words can exceed Python's recursion depth.
- **Rebuild each candidate row:** Calling a join or summing a slice for every start/end pair preserves correctness but adds another factor of $w$, producing $O(w^3)$ time.
- The last row always costs zero; applying the squared penalty to it changes the optimization.
- A space is counted only between two words on the same row, never at either row boundary.
- A single word produces cost zero because its row is necessarily final.

</details>
