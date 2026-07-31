# Number of Student Replacements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3616 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-student-replacements/) |

## Problem Description
### Goal

Students arrive in the order given by `ranks`, where `ranks[i]` is the rank of the $i$th arriving student. A smaller integer represents a better rank. The first arriving student is selected initially and does not count as a replacement.

For every later arrival, replace the selected student only when the new student's rank is strictly better than the current selected rank. Equal or larger rank values leave the selection unchanged. Return the total number of replacements made after processing the complete arrival sequence.

### Function Contract

**Inputs**

- `ranks`: The students' positive integer ranks in arrival order.

The constraints are $1 \le \lvert\texttt{ranks}\rvert \le 10^5$ and $1 \le \texttt{ranks[i]} \le 10^5$.

**Return value**

Return the number of later students whose strictly smaller rank replaces the currently selected student.

### Examples

**Example 1**

- Input: `ranks = [4, 1, 2]`
- Output: `1`
- Explanation: Rank 1 replaces rank 4; rank 2 is not better than rank 1.

**Example 2**

- Input: `ranks = [2, 2, 3]`
- Output: `0`
- Explanation: Equality is not strictly better, and rank 3 is worse.

**Example 3**

- Input: `ranks = [5, 4, 3, 2, 1]`
- Output: `4`
- Explanation: Every arrival after the first establishes a new best rank.
