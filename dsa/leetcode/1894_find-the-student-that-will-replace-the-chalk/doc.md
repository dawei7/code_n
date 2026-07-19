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

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Remove complete rounds**

Let $S$ be the sum of all values in `chalk`. Every full pass through the class consumes exactly $S$ pieces and returns to student `0`, so complete passes do not affect which student eventually replaces the chalk. Replace `k` with `k % S`.

This remainder is strictly smaller than the cost of one full round, guaranteeing that the replacement occurs during the next single pass. A zero remainder means earlier rounds consumed the chalk exactly and student `0` replaces it.

**Scan the final partial round**

Visit students in order. If the remainder is less than the current requirement, return that index. Otherwise subtract the requirement and continue. Equality must take the subtraction branch because the student has enough chalk to complete the turn.

Modulo removes only whole sequences with identical state before and after, so it preserves the eventual replacement student. During the final pass, each successful subtraction exactly mirrors one real turn; the first failed comparison is therefore the required student.

#### Complexity detail

Summing the $N$ requirements and scanning at most one further pass both take $O(N)$ time. The total, remainder, index, and current requirement use $O(1)$ auxiliary space. Fixed-width implementations should sum in a type wide enough for as much as $10^{10}$ chalk per round.

#### Alternatives and edge cases

- **Literal cyclic simulation:** It follows the process directly but may take work proportional to `k` when requirements are small.
- **Prefix sums and binary search:** After reducing by the round sum, search the first prefix sum strictly greater than the remainder in $O(N+\log N)$ time and $O(N)$ space.
- **Exact round multiple:** A zero remainder means student `0` replaces the chalk.
- **Exact student requirement:** That student completes the turn; the following student may replace it.
- **One student:** The only possible result is index `0`.
- **Large `k`:** Reduce before simulating to avoid billions of turns.

</details>
