# Number of Ways to Stay in the Same Place After Some Steps

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1269 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/) |

## Problem Description

### Goal

A pointer starts at index $0$ of an array containing `arrLen` positions. One step may move the pointer one position left, move it one position right, or leave it at its current position. Every intermediate position must remain inside the array, so a move left from index $0$ or right from index `arrLen - 1` is not allowed.

Given `steps` and `arrLen`, count the distinct sequences of exactly `steps` moves that finish with the pointer back at index $0$. Because this count can be large, return it modulo $10^9+7$.

### Function Contract

**Inputs**

- `steps`: the exact number of moves, with $1 \le \texttt{steps} \le 500$.
- `arrLen`: the number of array positions, with $1 \le \texttt{arrLen} \le 10^6$.

Let

$$
w = \min\left(\texttt{arrLen}, \left\lfloor\frac{\texttt{steps}}{2}\right\rfloor+1\right)
$$

be the number of positions that can still participate in a walk returning to index $0$.

**Return value**

- Return the number of valid move sequences that end at index $0$ after exactly `steps` moves, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `steps = 3, arrLen = 2`
- Output: `4`

**Example 2**

- Input: `steps = 2, arrLen = 4`
- Output: `2`

**Example 3**

- Input: `steps = 4, arrLen = 2`
- Output: `8`

### Required Complexity

- **Time:** $O(\texttt{steps}\,w)$
- **Space:** $O(w)$

<details>
<summary>Approach</summary>

#### General

**Only a short prefix of the array is relevant**

Reaching index $j$ and then returning to index $0$ requires at least $2j$ moves. Consequently, no successful walk can visit an index greater than $\lfloor\texttt{steps}/2\rfloor$. Even when `arrLen` is as large as $10^6$, only the first $w$ positions can contribute to the answer.

**Count walks after each exact number of moves**

Maintain `dp[position]` as the number of valid walks that occupy `position` after the moves processed so far. Initially only `dp[0]` is one. For each new move, the count at position $j$ is the sum of the previous counts at $j$ itself, $j-1$, and $j+1$, omitting neighbors outside the retained prefix. Reduce every sum modulo $10^9+7$.

This transition considers the final action of every walk exactly once: it was respectively a stay, a move right, or a move left. Conversely, appending that action to any counted predecessor produces a legal walk at $j$. Induction over the number of processed moves therefore shows that every state count is exact. After all `steps` transitions, `dp[0]` is precisely the requested number of walks.

Use a fresh one-dimensional array for each transition. This prevents counts written for the current move from being reused as though they belonged to the previous move.

#### Complexity detail

There are `steps` transition rounds and at most $w$ relevant positions per round, so the running time is $O(\texttt{steps}\,w)$. The previous and next state arrays each hold $w$ integers; reusing their roles keeps auxiliary space at $O(w)$.

#### Alternatives and edge cases

- **Full-array dynamic programming:** Updating all `arrLen` positions is correct, but it can take $O(\texttt{steps}\,\texttt{arrLen})$ time and space despite most positions being unable to return.
- **Two-dimensional dynamic programming:** Storing every move layer makes the recurrence easy to inspect but increases auxiliary space to $O(\texttt{steps}\,w)$ without changing the result.
- **Memoized recursion:** The same states can be evaluated top-down, though recursion bookkeeping is heavier and depth reaches `steps`.
- **Single-position array:** Every step must stay at index $0$, so exactly one sequence is valid.
- **One step:** The only returning sequence is to stay, regardless of the array length.
- **Array boundary:** Missing left and right predecessors contribute zero; an invalid move is never counted and then repaired later.
- **Modulo arithmetic:** Reduction is applied throughout the recurrence so intermediate counts remain bounded while preserving the final residue.

</details>
