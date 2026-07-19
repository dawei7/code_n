# The Number of Weak Characters in the Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1996 |
| Difficulty | Medium |
| Topics | Array, Stack, Greedy, Sorting, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/) |

## Problem Description

### Goal

A game contains $N$ characters, each described by two statistics. For character $i$, `properties[i] = [attack_i, defense_i]` gives its attack and defense levels.

Character $i$ is weak when some other character $j$ is strictly better in both statistics:

$$
\textit{attack}_j>\textit{attack}_i
\quad\text{and}\quad
\textit{defense}_j>\textit{defense}_i.
$$

Equality in either statistic is not enough. Count how many characters have at least one such dominating character.

### Function Contract

**Inputs**

- `properties`: an array of $N$ pairs `[attack, defense]`, where $2 \le N \le 10^5$.
- Every attack and defense value is between $1$ and $10^5$ inclusive.

**Return value**

Return the number of characters dominated in both statistics by at least one other character.

### Examples

**Example 1**

- Input: `properties = [[5, 5], [6, 3], [3, 6]]`
- Output: `0`
- Explanation: Each possible comparison loses in at least one statistic.

**Example 2**

- Input: `properties = [[2, 2], [3, 3]]`
- Output: `1`
- Explanation: The character `[3, 3]` has strictly greater attack and defense than `[2, 2]`.

**Example 3**

- Input: `properties = [[1, 5], [10, 4], [4, 3]]`
- Output: `1`
- Explanation: `[10, 4]` dominates `[4, 3]`, while no character has both statistics above `[1, 5]`.

### Required Complexity

- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Turn the two-dimensional comparison into a sweep.** Sort characters by decreasing attack. Every character processed earlier then has attack at least as large as the current one, so a running maximum can summarize their defenses.

**Neutralize equal-attack characters.** Within one attack value, sort defense in increasing order. During the left-to-right sweep, lower defenses from that same group appear first and may raise the running maximum, but they cannot exceed a later defense in their group. Consequently, no equal-attack character is incorrectly declared weak. When the attack decreases, the stored maximum may come from a strictly larger attack, which is exactly what the definition requires.

**Compare against the strongest eligible defense.** Maintain `maximum_defense` over the processed prefix. If the current defense is smaller, an earlier character has both strictly larger attack and strictly larger defense, so count the current character. Otherwise, update the maximum. This is sufficient because only the largest eligible defense matters: if it cannot dominate the current defense, no smaller processed defense can.

#### Complexity detail

Sorting $N$ pairs takes $O(N\log N)$ time, and the sweep takes $O(N)$ time. Python's sort may use $O(N)$ auxiliary space in the worst case; the scan itself uses $O(1)$ additional state.

#### Alternatives and edge cases

- **Compare every pair:** Directly searching for a dominator for each character takes $O(N^2)$ time.
- **Bucket by attack:** Because statistics are bounded, suffix maxima over attack buckets can achieve $O(N+M)$ time for maximum statistic value $M$, at the cost of an $O(M)$ table.
- Characters with equal attack never dominate one another, even when their defenses differ.
- Characters with equal defense never dominate one another, even when their attacks differ.
- Duplicate pairs are separate characters but cannot dominate each other.
- A character needs only one dominator; several possible dominators do not increase its contribution beyond one.

</details>
