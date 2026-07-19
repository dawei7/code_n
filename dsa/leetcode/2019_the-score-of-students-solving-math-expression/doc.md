# The Score of Students Solving Math Expression

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2019 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Math, String, Dynamic Programming, Stack, Memoization |
| Official Link | [LeetCode](https://leetcode.com/problems/the-score-of-students-solving-math-expression/) |

## Problem Description

### Goal

An expression contains single-digit operands and only `+` and `*` operators.
Its correct value follows ordinary precedence: perform multiplications from
left to right, then additions from left to right.

Grade every submitted answer independently. A correct value earns five points.
Otherwise, a value earns two points when some full parenthesization of the same
operands and operators can produce it using correct arithmetic but an
incorrect operation order. Every other answer earns zero. If a mistaken
parenthesization happens to equal the correct value, the answer still earns
five points. Return the total score.

### Function Contract

Let $M$ be the number of operands, $A$ the number of submitted answers, and
$V=1001$ the count of retained values from $0$ through $1000$.

**Inputs**

- `s`: a valid alternating expression of length from $3$ through $31$ with at
  most $15$ operators and operands from $0$ through $9$.
- `answers`: $A$ integers from $0$ through $1000$, where
  $1\le A\le10^4$.

**Return value**

Return the sum of the five-, two-, and zero-point grades.

### Examples

**Example 1**

- Input: `s = "7+3*1*2", answers = [20, 13, 42]`
- Output: `7`
- Explanation: `13` is correct for five points, while `20` is produced by
  `((7+3)*1)*2` for two.

**Example 2**

- Input: `s = "3+5*2", answers = [13, 0, 10, 13, 13, 16, 16]`
- Output: `19`
- Explanation: Three correct answers earn fifteen points and two
  parenthesized values of `16` earn four.

**Example 3**

- Input: `s = "6+0*1", answers = [12, 9, 6, 4, 8, 6]`
- Output: `10`
- Explanation: Both occurrences of the correct value `6` earn five points,
  even though `(6+0)*1` also produces `6`.

### Required Complexity

- **Time:** $O(M^3V^2+A)$
- **Space:** $O(M^2V)$

<details>
<summary>Approach</summary>

#### General

**Evaluate the correct precedence separately.** Parse the digit operands and
operators. Maintain the product of the current multiplication group; when `+`
appears, add that product to the total and begin the next group. This produces
the unique five-point value without relying on arbitrary evaluation.

**Enumerate all parenthesized values with interval DP.** Let `possible[i][j]`
be the set of results obtainable by fully parenthesizing operands `i` through
`j`. A single operand contributes itself. For every longer interval, try each
operator as the final split, combine every left and right result with that
operator, and retain values no larger than $1000$, since submitted answers
cannot exceed that bound.

Every full binary parenthesization has one final operator separating a left
and right subexpression, so the corresponding split reconstructs its result
from smaller DP intervals. Conversely, each DP combination corresponds to a
valid parenthesization using the original operator order. The final set
therefore contains exactly the plausible two-point values. Grade each answer
by checking the correct value first, then membership in that set.

#### Complexity detail

There are $O(M^2)$ operand intervals and $O(M)$ splits per interval. Each split
can combine up to $V^2$ value pairs, giving $O(M^3V^2)$ DP time; grading adds
$O(A)$. Storing up to $V$ results per interval uses $O(M^2V)$ space. In legal
inputs $M\le16$ and $V=1001$, while actual set sizes depend strongly and
non-monotonically on the operators and digits.

#### Alternatives and edge cases

- **Enumerate parenthesization trees:** Generating every Catalan-structured
  evaluation repeats identical subexpressions and grows exponentially.
- **Use unrestricted `eval`:** It can obtain the correct precedence value but
  neither enumerates mistaken parenthesizations nor provides an appropriate
  parser boundary.
- Correct answers always receive five points, even if also reachable through
  a wrong operation order.
- Duplicate submissions are graded separately and multiply their points.
- Zero can collapse many multiplication results, so DP sets must deduplicate
  values rather than paths.

</details>
