# Guided Example: Delete Greatest Value in Each Row

We are given an $m \times n$ matrix `grid` of positive integers and one repeated
operation: while any cell remains, take the greatest value from every row,
remove those $m$ cells, and add the largest of the $m$ removed values to a
running total. Each round removes exactly one cell per row, so the matrix sheds
one column per round and the process terminates after exactly $n$ rounds.

The instructive question is not how to simulate the rounds — that is
mechanical — but how much of the apparent choice actually matters. When a row
contains several copies of its greatest value, the operation lets us delete
*any* of those tied cells. This lesson shows that the deleted **values** are
never a matter of choice, only the deleted **cells** are, and that the final
total is therefore forced. Once that is clear, the entire answer can be read off
the rows after each row has been sorted exactly once.

## 1. What a single round does to a row

Focus on one row of length $n$. A round removes the greatest value currently
present in that row. Because nothing is ever added back, the row loses one
element per round, and the value it loses is the maximum of its surviving
elements.

Write the row's values in non-increasing order $a_1 \ge a_2 \ge \dots \ge a_n$.
Before the first round the surviving set is all of them, so the first round
removes a cell holding $a_1$. Before the second round the surviving set is
$\{a_2, \dots, a_n\}$, whose maximum is $a_2$, so the second round removes a
cell holding $a_2$. Continuing, the $r$-th round removes a cell holding $a_r$.
The tie rule ("if multiple such elements exist, delete any of them") decides
only which physical cell disappears; the value $a_r$ is the same for every tied
choice. This is the value-identity versus index-identity distinction that the
rest of the lesson rests on.

## 2. The representative instance

Trace the first official example, `grid = [[1,2,4],[3,3,1]]`: two rows and three
columns, hence three rounds. Row 1 contains two copies of the value 3, which is
exactly the tie the operation permits us to resolve arbitrarily.

| Row index $i$ | Values in row $i$ | Row maximum | Ties in row |
|:---:|:---|:---:|:---|
| 0 | 1, 2, 4 | 4 | none |
| 1 | 3, 3, 1 | 3 | the value 3 appears twice |

## 3. Round-by-round trace

Row 1's first deletion may take either of its two 3-valued cells. Fix the second
one for concreteness; the accumulated answer is unaffected by that choice.

| Round | Removed from row 0 | Removed from row 1 | Maximum of the two | Cumulative answer |
|:---:|:---:|:---:|:---:|:---:|
| 1 | 4 | 3 | 4 | 4 |
| 2 | 2 | 3 | 3 | 7 |
| 3 | 1 | 1 | 1 | 8 |

The matrix is empty after round 3, and the reported answer is $8$. Note that
round 1 could just as well have removed the *other* 3-valued cell in row 1:
the removed multiset would be identical, so the maximum added in that round is
still 3 and the running total still reaches 8.

## 4. The order-statistic invariant

The trace above is not special. For every row $i$, let

$$
a_1^{(i)} \ge a_2^{(i)} \ge \dots \ge a_n^{(i)}
$$

be its values in non-increasing order. Section 1 shows, by induction on the
round number, that round $r$ removes a cell of value $a_r^{(i)}$ from row $i$,
for every round $r \in \{1, \dots, n\}$. The induction step needs only one
fact: deleting a cell cannot create a new maximum, because the surviving set is
a subset of the previous one.

Two consequences follow immediately.

- The value removed from a row is determined before the round begins; only the
  identity of the cell is free.
- Row $i$ therefore contributes its own values $a_1^{(i)}, \dots, a_n^{(i)}$
  to the $n$ rounds in that fixed order, one per round.

Because each round adds the maximum over rows of the values removed in that
round, the answer is

$$
\text{answer} = \sum_{r=1}^{n} \max_{1 \le i \le m} a_r^{(i)}.
$$

| Round $r$ | Row 0 takes | Value | Row 1 takes | Value | Round maximum |
|:---:|:---|:---:|:---|:---:|:---:|
| 1 | 1st largest | 4 | 1st largest | 3 | 4 |
| 2 | 2nd largest | 2 | 2nd largest | 3 | 3 |
| 3 | 3rd largest | 1 | 3rd largest | 1 | 1 |

## 5. Reading the answer off sorted columns

Sorting a row into non-decreasing order reverses the order statistics: the entry
at position $j$ of the sorted row, counting from $0$, is the $(n-j)$-th largest
value of that row. Round $r$ uses the $r$-th largest value, which sits at index
$n-r$ in the sorted row. Running $r$ from $1$ to $n$ therefore sweeps the sorted
columns from index $n-1$ down to $0$, and

$$
\text{answer} = \sum_{j=0}^{n-1} \max_{1 \le i \le m} \bigl(\text{sorted row } i\bigr)[j].
$$

In words: sort every row ascending, then add the maximum of each resulting
column. For the traced instance the sorted rows are `[1,2,4]` and `[1,3,3]`.

| Column index $j$ | Row 0 sorted | Row 1 sorted | Column maximum | Contribution to the answer |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | 1 | 1 | 1 |
| 1 | 2 | 3 | 3 | 3 |
| 2 | 4 | 3 | 4 | 4 |

The column maxima are $1, 3, 4$ in ascending column order, i.e. exactly the
round maxima $4, 3, 1$ read backwards, and their sum is $8$. This also explains
why sorting ascending and scanning columns left to right is equivalent to
simulating the rounds: the column sweep is the round order reversed.

## 6. Correctness: why no schedule beats this total

The formula is both an upper bound and an achievable value, which is what makes
it the answer rather than a heuristic.

**Upper bound.** Fix any legal run of the operation. At the start of round $r$,
row $i$ has already lost $r-1$ cells, so its surviving set has $n-r+1$ elements
drawn from its $n$ original values. The maximum of any $n-r+1$ elements of a
multiset is at most the $r$-th largest element of the whole multiset, so the
value removed from row $i$ in round $r$ satisfies

$$
\text{removed}_r^{(i)} \le a_r^{(i)}.
$$

Taking maxima over rows preserves the inequality, and summing over the $n$
rounds bounds the total by $\sum_r \max_i a_r^{(i)}$ for **every** legal run.
The argument never uses the tie rule, because that rule cannot change a removed
value at all.

**Achievability.** The run that always deletes the current row maximum — which
the operation mandates anyway, and which ties never make ambiguous in value —
attains $\text{removed}_r^{(i)} = a_r^{(i)}$ in every round. Its total is
exactly the bound, so the bound is the optimum.

**Uniqueness of the total.** Since the upper bound holds for all runs and one
run achieves it, every legal run produces the same total. The arbitrary tie
choice is therefore immaterial to the result: it permutes equal values, not the
multiset of deleted values. A second instance confirms the arithmetic against
the authored expectations.

| Row index $i$ | Input row | Sorted row | Order statistics taken |
|:---:|:---|:---|:---|
| 0 | 7, 1, 3, 6 | 1, 3, 6, 7 | 7, 6, 3, 1 |
| 1 | 2, 9, 8, 4 | 2, 4, 8, 9 | 9, 8, 4, 2 |
| 2 | 5, 5, 5, 5 | 5, 5, 5, 5 | 5, 5, 5, 5 |

Round maxima are $\max(7,9,5) = 9$, $\max(6,8,5) = 8$, $\max(3,4,5) = 5$, and
$\max(1,2,5) = 5$, giving $9 + 8 + 5 + 5 = 27$, matching the authored expected
output for `grid = [[7,1,3,6],[2,9,8,4],[5,5,5,5]]`. Equivalently, the column
maxima of the sorted rows are $5, 5, 8, 9$.

## 7. Traps this instance exposes

| Situation | What a careless reading assumes | What actually happens |
|:---|:---|:---|
| Duplicate maxima in a row | the tie choice changes the answer | only the cell identity changes; the deleted value is fixed, so the total is fixed |
| Several rows sharing a maximum | rounds can skip rows that already lost their maximum | every round deletes one cell from *every* row, so all rows stay the same length and there are exactly $n$ rounds |
| A single row, $m = 1$ | only the largest value counts | that row supplies the round maximum in all $n$ rounds, so the answer is the sum of the whole row |
| A single column, $n = 1$ | the process needs several rounds | there is exactly one round, so the answer is the maximum of the single column |
| Rectangular matrix with $m \neq n$ | the number of rounds equals the number of rows | rounds are governed by the column count $n$, not the row count $m$ |
| Sorting a row in place | sorting changes which values get deleted | sorting only reorders a row; the multiset of values, and hence every round maximum, is unchanged |

Two boundary checks from the authored cases follow the same reasoning. For
`grid = [[4],[9],[2]]` there is one round and the answer is
$\max(4,9,2) = 9$. For a $3 \times 5$ matrix whose every entry is $100$, each of
the five rounds adds $100$, so the total is $500$.

## 8. Complexity: time and auxiliary space

Let $m$ be the number of rows and $n$ the number of columns of `grid`.

**Time.** Sorting one row of $n$ entries costs $O(n \log n)$ comparisons, and
there are $m$ rows, so the sorting phase costs $O(m n \log n)$. The column sweep
then visits each of the $mn$ cells once while maintaining $n$ running maxima,
costing $O(mn)$. The sort dominates: $O(mn) \subseteq O(m n \log n)$ for
$n \ge 2$, and for $n = 1$ both reduce to $O(m)$. The total is
$O(m n \log n)$.

**Auxiliary space.** The running total and the current column maximum need
$O(1)$ extra storage. Sorting the rows in place adds only the temporary buffer
the sorting routine requires; a merge-based sort may allocate up to $\Theta(n)$
scratch entries for one row, while an in-place exchange sort needs none. The
honest bound on top of the input is therefore $O(n)$ auxiliary space in the
worst case, and $O(1)$ if the implementation relies on an in-place sort.
Scaled against the constraints $1 \le m, n \le 50$, both are negligible.

Regardless of the method, every cell must be examined at least once, so the time
is $\Omega(mn)$: no entry can be ruled out in advance, since any row may supply
a round maximum.

| Method | Time | Auxiliary space | Comment |
|:---|:---:|:---:|:---|
| Sort every row, then sum column maxima | $O(m n \log n)$ | $O(n)$ worst case for the sort buffer | simplest and clearly correct; the order-statistic reading stays explicit |
| Priority queue per row, pop once per round | $O(m n \log n)$ | $O(mn)$ for the queues | same asymptotics with more bookkeeping, but works when rows are consumed lazily |
| Literal simulation, rescanning each row for its maximum | $O(m n^2)$ | $O(1)$ beyond the input | correct but needlessly slow; quadratic in the column count |
| Counting sort per row using the value bound $100$ | $O(mn + 100m)$ | $O(100)$ counters per row | exploits the small value range and is linear when that range is a constant, at the cost of extra code |
