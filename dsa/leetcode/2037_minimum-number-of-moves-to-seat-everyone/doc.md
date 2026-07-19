# Minimum Number of Moves to Seat Everyone

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2037 |
| Difficulty | Easy |
| Topics | Array, Greedy, Sorting, Counting Sort |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/) |

## Problem Description

### Goal

There are $N$ students and $N$ available seats positioned along a number line.
The arrays `students` and `seats` give their respective starting positions.
Several students may initially share a position, and several distinct seats may
also occupy the same position.

One move shifts one student by exactly one position to the left or right.
Move every student onto a seat so that each seat receives at most one student,
and return the minimum total number of moves. Each student must ultimately be
matched to a distinct seat occurrence, even when positions are duplicated.

### Function Contract

Let $N$ be the common length of the two arrays.

**Inputs**

- `seats`: the positions of $N$ distinct seat occurrences.
- `students`: the starting positions of $N$ students.

The constraints are $1 \le N \le 100$, with every position from $1$ through
$100$.

**Return value**

- The minimum sum of unit moves needed to assign every student to a distinct
  seat.

### Examples

**Example 1**

- Input: `seats = [3, 1, 5], students = [2, 7, 4]`
- Output: `4`
- Explanation: The sorted matches cost `1`, `1`, and `2` moves.

**Example 2**

- Input: `seats = [4, 1, 5, 9], students = [1, 3, 2, 6]`
- Output: `7`

**Example 3**

- Input: `seats = [2, 2, 6, 6], students = [1, 3, 2, 6]`
- Output: `4`
- Explanation: Both seats at position `2` and both seats at position `6` are
  separate assignable occurrences.
