# Maximum Compatibility Score Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1947 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-compatibility-score-sum/) |

## Problem Description
### Goal
A survey has $Q$ binary questions. The response rows in `students` belong to
$M$ students, and the rows in `mentors` belong to $M$ mentors. The compatibility
score of one student-mentor pair is the number of question positions at which
their answers are equal.

Assign every student to exactly one mentor and every mentor to exactly one
student. Among all one-to-one assignments, return the maximum possible sum of
the $M$ pair compatibility scores.

### Function Contract
**Inputs**

- `students`: $M$ rows of $Q$ binary answers.
- `mentors`: $M$ rows of $Q$ binary answers.
- The dimensions satisfy $1 \le M,Q \le 8$; every entry is either 0 or 1.

**Return value**

- The largest total compatibility score over all bijective assignments from
  students to mentors.

### Examples
**Example 1**

- Input:
  `students = [[1, 1, 0], [1, 0, 1], [0, 0, 1]], mentors = [[1, 0, 0], [0, 0, 1], [1, 1, 0]]`
- Output: `8`

**Example 2**

- Input:
  `students = [[0, 0], [0, 0], [0, 0]], mentors = [[1, 1], [1, 1], [1, 1]]`
- Output: `0`

**Example 3**

- Input: `students = [[1, 0]], mentors = [[0, 1]]`
- Output: `0`

### Required Complexity
- **Time:** $O(M^2Q+M2^M)$
- **Space:** $O(M^2+2^M)$

<details>
<summary>Approach</summary>

#### General

**Precompute every pair score**

Build an $M$ by $M$ table where entry `(student, mentor)` counts equal answers
across the $Q$ questions. Once this table exists, assignment transitions need
only constant-time score lookups.

**Represent assigned mentors with a mask**

Use an $M$-bit mask. A set bit means that mentor has already been assigned.
If a mask contains $K$ set bits, it represents an optimal assignment for the
first $K$ students; therefore the next student index is
`mask.bit_count()`.

Let `dp[mask]` be the greatest score for that partial assignment. Start with
`dp[0] = 0`. For every unused mentor $j$, set bit $j$ and update

$$
\operatorname{dp}[\textit{mask}\cup\{j\}]
=
\max\left(
\operatorname{dp}[\textit{mask}\cup\{j\}],
\operatorname{dp}[\textit{mask}]
+\operatorname{score}[K][j]
\right).
$$

Every partial one-to-one assignment has exactly one used-mentor mask and one
score. Extending it by any unused mentor generates every valid assignment for
the next student. Keeping only the maximum for each mask is safe because all
future choices depend on which mentors remain, not on the order that produced
the mask. Induction on $K$ therefore makes the all-ones state the optimum over
all complete assignments.

#### Complexity detail

Computing all $M^2$ pair scores examines $Q$ answers per pair, costing
$O(M^2Q)$. There are $2^M$ masks and at most $M$ mentor transitions per mask,
adding $O(M2^M)$ time. The score table uses $O(M^2)$ space and the dynamic
program uses $O(2^M)$ space.

#### Alternatives and edge cases

- **Enumerate mentor permutations:** Score every one-to-one assignment
  directly. This is simple but costs $O(M!\,MQ)$ time without precomputation,
  or $O(M!\,M)$ after pair scores are built.
- **Backtracking with memoization:** Recurse by student and used-mentor mask.
  It has the same asymptotic complexity as iterative bitmask DP but adds call
  stack overhead.
- A single student has only one possible mentor, so the answer is that pair's
  score.
- Completely opposite response rows may contribute zero.
- Identical student or mentor rows remain separate people and must each be
  assigned exactly once.
- Several assignments may tie for the maximum; only the score is returned.
- The maximum possible result is $MQ$, achieved when every assigned pair
  agrees on all questions.

</details>
