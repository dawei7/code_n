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

### Required Complexity

- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Turn movements into matching distances**

Moving a student from position $a$ to a seat at position $b$ costs
$\lvert a-b\rvert$, regardless of the route taken. The task is therefore a
minimum-cost one-to-one matching between the two position multisets.

**Uncross any pair of assignments**

Suppose two students satisfy $a \le b$ and two seats satisfy $x \le y$. A
crossing assignment sends $a$ to $y$ and $b$ to $x$. On a number line,

$$
\lvert a-x\rvert+\lvert b-y\rvert
\le
\lvert a-y\rvert+\lvert b-x\rvert.
$$

Thus swapping a crossing pair to match left with left and right with right
never increases the cost. Repeating this exchange removes every crossing from
an optimal assignment.

**Pair the two sorted sequences**

Sort both arrays and match equal ranks. This assignment has no crossings, and
the exchange argument shows that some optimum must have exactly this order.
Summing `abs(seat - student)` over the paired sorted positions therefore gives
the minimum. Duplicate positions cause no issue because their separate
occurrences remain separate list entries.

#### Complexity detail

Sorting both length-$N$ arrays takes $O(N\log N)$ time, and the paired distance
sum takes $O(N)$ time. The app-local implementation creates sorted copies,
which use $O(N)$ auxiliary space.

#### Alternatives and edge cases

- **Counting sort by position:** Because positions lie from $1$ through $100$,
  frequency arrays can match students and seats in $O(N+100)$ time and
  $O(100)$ space.
- **Repeated nearest-seat choice:** Assigning each student independently to its
  nearest remaining seat can make a locally attractive choice that forces a
  later student much farther away; it lacks the sorted exchange guarantee.
- Students and seats already sharing the same sorted positions contribute zero
  moves even if the input orders differ.
- Duplicate seats at one coordinate are distinct and may receive different
  students.
- Duplicate students may be sent to different seat positions.
- Each unit of absolute distance is one move, so movements add independently
  across the final matching.

</details>
