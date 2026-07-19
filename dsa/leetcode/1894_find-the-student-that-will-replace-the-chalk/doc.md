# Find the Student that Will Replace the Chalk

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/) |
| Frontend ID | 1894 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Simulation, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Students are numbered from `0` through $N-1` and solve problems repeatedly in that order. After student $N-1`, the sequence returns to student `0`. Student `i` consumes `chalk[i]` pieces whenever their turn is reached.

The classroom begins with `k` pieces of chalk. If the remaining amount is strictly less than the current student's requirement, that student cannot take the turn and must replace the chalk. If the amounts are equal, the student uses all remaining chalk successfully and the next student replaces it. Return the index of the first student who must replace the chalk.

### Function Contract

**Inputs**

- `chalk`: a length-$N$ array of positive chalk requirements in student order.
- `k`: the positive initial number of chalk pieces.
- $1 \le N \le 10^5$, $1 \le \texttt{chalk[i]} \le 10^5$, and $1 \le k \le 10^9$.

**Return value**

- Return the zero-based index of the first student whose requirement exceeds the remaining chalk.

### Examples

**Example 1**

- Input: `chalk = [5,1,5], k = 22`
- Output: `0`

Two complete rounds consume all `22` pieces, so student `0` replaces the chalk.

**Example 2**

- Input: `chalk = [3,4,1,2], k = 25`
- Output: `1`

After two complete rounds and student `0`'s next turn, only two pieces remain; student `1` needs four.

**Example 3**

- Input: `chalk = [2,3], k = 2`
- Output: `1`

Student `0` uses exactly two pieces, leaving none for student `1`.
