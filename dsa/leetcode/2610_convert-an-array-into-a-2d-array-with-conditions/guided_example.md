# Guided Example: Convert an Array Into a 2D Array With Conditions

## 1. The instance, its multiplicities, and the required outcome

The representative input is `nums = [1,3,4,1,2,3,1]`, an array of seven integers. The task is to distribute every element of `nums` into rows so that

1. nothing outside `nums` appears anywhere,
2. each row contains **distinct** integers, and
3. the number of rows is as small as possible.

Any valid arrangement achieving the minimum is accepted; row order, element order inside a row, and unequal row lengths are all free. The required row count for this instance is $3$, and one accepted arrangement is `[[1,3,4,2],[1,3],[1]]`.

Everything the method needs is the multiplicity of each value.

| Value $v$ | Positions in `nums` | Frequency $f(v)$ | Rows it must occupy |
|---|---|---|---|
| 1 | 0, 3, 6 | 3 | three distinct rows |
| 3 | 1, 5 | 2 | two distinct rows |
| 4 | 2 | 1 | one row |
| 2 | 4 | 1 | one row |

The decisive quantity is the largest frequency,

$$F = \max_{v} f(v) = f(1) = 3,$$

and the whole lesson is the argument that the minimal number of rows equals $F$ exactly, never more and never fewer.

## 2. What "each row contains distinct integers" forces

The distinctness rule is a capacity limit on every row: a row may hold at most one copy of any particular value. A value that occurs $f(v)$ times therefore needs $f(v)$ *different* rows, because no two of its copies can share one. Applying this to the most frequent value gives an unconditional lower bound.

**Pigeonhole bound.** Every valid arrangement uses at least $F$ rows. Here value `1` occurs three times, so its three copies must land in three separate rows, and no arrangement can use fewer than three rows.

This bound is the reason a greedy "pack as tightly as possible" instinct is not by itself an answer: tightness must be measured against the bound, and the bound is a property of the frequencies, not of the packing order.

The bound also shows why neither of two nearby quantities is the answer. The number of distinct values is $4$, but that is an upper bound on how *full* a row can be, not a lower bound on the row count. The length of `nums` is $7$, which is again irrelevant. Only the maximum multiplicity decides.

## 3. The level construction that attains the bound

The bound is attainable, and the construction is a level assignment. Write $f(v)$ for the frequency of value $v$ and imagine the copies of $v$ labelled $1, 2, \dots, f(v)$. Send copy number $i$ of value $v$ to row $i$.

Read by rows instead of by values, row $i$ is exactly the set of distinct values whose frequency is at least $i$:

$$\text{row}_i = \{\, v : f(v) \ge i \,\}, \qquad 1 \le i \le F.$$

Three facts follow immediately. Row $i$ contains distinct values by construction, since it is a *set* of values. Every copy of every value is placed, because copy $i$ exists only for $i \le f(v)$ and is sent to row $i$. And the number of rows is $F$, since row $F$ is non-empty — it contains any value attaining the maximum — while row $F+1$ would contain only values with frequency above $F$, of which there are none.

Combining this construction with the pigeonhole bound from Section 2 gives the exact optimum:

$$\text{minimal rows} = F = \max_{v} f(v).$$

It is worth seeing the same object as a partition. If the distinct values have frequencies $f_1 \ge f_2 \ge \dots \ge f_d$, the multiset is described by the partition $\lambda = (f_1, \dots, f_d)$ of $n$, and the construction produces rows whose sizes are the conjugate partition $\lambda'$. The number of rows is the largest part $f_1$, and the total number of cells is still $\sum_i i \cdot \lambda'_i = n$, which is a useful consistency check on any candidate answer.

## 4. Executing the construction on the instance

The frequency profile of `[1,3,4,1,2,3,1]` is $f(1) = 3$, $f(3) = 2$, $f(4) = 1$, $f(2) = 1$. Labelling the copies and routing copy $i$ of each value to row $i$ gives the following placement.

| Value $v$ | Copy 1 goes to | Copy 2 goes to | Copy 3 goes to |
|---|---|---|---|
| 1 | row 1 | row 2 | row 3 |
| 3 | row 1 | row 2 | — |
| 4 | row 1 | — | — |
| 2 | row 1 | — | — |

Reading the same routing by rows yields the answer directly.

| Row $i$ | Values with $f(v) \ge i$ | Row content | Length |
|---|---|---|---|
| 1 | $\{1, 2, 3, 4\}$ | `[1,3,4,2]` | 4 |
| 2 | $\{1, 3\}$ | `[1,3]` | 2 |
| 3 | $\{1\}$ | `[1]` | 1 |

The three rows use exactly $4 + 2 + 1 = 7$ cells, matching the length of `nums`, and every value appears in exactly $f(v)$ rows. The row lengths $4, 2, 1$ are the conjugate partition of the frequency partition $(3, 2, 1, 1)$: the largest frequency contributes the number of parts, and each level contributes one cell per value that reaches it.

The row count is $3$, matching both the pigeonhole bound and the required outcome. Notice that the answer is not the only valid one — `[[1,3,4,2],[3,1],[1]]` and `[[1,3,4,2],[1,3],[1]]` describe the same rows, and reordering values inside a row changes nothing that the conditions measure.

The same construction reproduces every authored instance without modification.

| Instance | Frequencies (largest first) | $F$ | Row lengths produced | Rows required |
|---|---|---|---|---|
| `[1,3,4,1,2,3,1]` | 3, 2, 1, 1 | 3 | 4, 2, 1 | 3 |
| `[1,2,3,4]` | 1, 1, 1, 1 | 1 | 4 | 1 |
| `[2,2,2,2]` | 4 | 4 | 1, 1, 1, 1 | 4 |
| `[1,2,3,1,2,3]` | 2, 2, 2 | 2 | 3, 3 | 2 |
| `[4,1,4,2,1,4,3,2]` | 3, 2, 2, 1 | 3 | 4, 3, 1 | 3 |
| `[5,1,5,4,3,2,4]` | 2, 2, 1, 1, 1 | 2 | 5, 2 | 2 |

## 5. Invariant and correctness of the frequency criterion

**Invariant of the level assignment.** After every value has been routed, level $i$ holds one copy of each value with $f(v) \ge i$ and nothing else. Consequently a level contains no repeated value, no copy is left unassigned, and no foreign integer is introduced. The invariant is restored value by value: routing value $v$ touches only levels $1$ through $f(v)$, and each of those levels receives $v$ at most once.

**Soundness.** The arrangement produced by the construction satisfies all three conditions at once. Completeness of the element set follows from copy $i$ existing only when $i \le f(v)$; distinctness follows because each level is a set; minimality follows from the count of levels equalling $F$.

**Optimality.** The lower bound and the construction meet. Any valid arrangement uses at least $F$ rows because the $F$ copies of a maximum-frequency value occupy $F$ distinct rows, and the construction uses exactly $F$ rows, so no arrangement can use fewer. The criterion is therefore both necessary and sufficient, and it certifies the row count of the example as $3$.

**Uniqueness of the count, not of the arrangement.** The optimum row count is unique, but the arrangement is not. The set of valid answers is closed under permuting rows, permuting values within a row, and moving a value between rows as long as no row gains a duplicate and no row is emptied. This is why the package evaluates the answer by its conditions rather than by exact equality with one printed arrangement, and why a method should aim at the count $F$ rather than at reproducing a particular listing.

## 6. Traps and boundary behaviour

| Situation | Instance | Criterion says | Why the tempting alternative fails |
|---|---|---|---|
| All values distinct | `[1,2,3,4]` | 1 row of length 4 | counting duplicates gives the right answer here by accident; there are none |
| One value repeated | `[2,2,2,2]` | 4 rows of length 1 | "one row per distinct value" predicts 1 row, but four copies cannot share a row |
| Equal frequencies | `[1,2,3,1,2,3]` | 2 rows of length 3 | the levels are identical sets, so both rows are full; no slack remains |
| Staggered frequencies | `[4,1,4,2,1,4,3,2]` | 3 rows of lengths 4, 3, 1 | a greedy that fills row 1 completely is fine, but only because the bound is 3 |
| Single element | `[1]` | 1 row of length 1 | the minimum input must not be special-cased to an empty result |

Two further traps are contractual rather than algorithmic. First, rows may have different lengths, and padding a short row with extra copies of an already-present value — or with any integer not in `nums` — breaks the conditions even though it makes the answer look tidier. Second, the values are bounded by $\text{nums.length} \le 200$, so a frequency array indexed by value is legal and removes any need for hashing; a method that assumes values are dense from $1$ upward must still size that array by the largest value present or by `nums.length`, whichever bound it trusts.

The alternatives that were considered and eliminated are summarized below.

| Method | Rows produced | Always minimal | Weakness |
|---|---|---|---|
| One row per distinct value, duplicates appended | more than $F$ whenever some $f(v) > 1$ | no | violates distinctness or drops elements |
| Sort, then split into chunks of the largest frequency | not determined by frequencies | no | an equal chunking ignores which values repeat and can duplicate inside a row |
| First-fit greedy: send a value to the first row lacking it | at most $F$ | yes | correct, but minimality still has to be argued from the pigeonhole bound |
| Level assignment by copy index | exactly $F$ | yes | none; it is optimal by construction |

## 7. Complexity of the frequency method

Let $n$ be the length of `nums` and $V$ the number of distinct values, so $V \le n$ with $n \le 200$ here. Building the frequency profile costs one pass over the input, hence $O(n)$ time. Emitting row $i$ for every value with $f(v) \ge i$ writes each of the $n$ elements exactly once, so the construction is also $O(n)$ time, and the total is

$$O(n).$$

A comparison-based sort of the values, by contrast, would cost $O(n \log n)$ and would not improve the bound, which depends only on multiplicities.

The auxiliary space is $O(n)$: the frequency structure holds at most $n$ counters, and the output itself holds $n$ cells. Excluding the returned array — which is required output rather than workspace — the extra storage is one counter per distinct value, and with the value bound in this contract that can be a plain array of length $n + 1$ rather than a hash map.
