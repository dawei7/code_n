# Guided Example: Classes With at Least 5 Students

The `Courses` relation stores one row per enrollment: the student's name in `student` and the class they joined in `class`, with the pair `(student, class)` declared as the primary key. That declaration matters more than it first appears — it certifies that one student contributes at most one row to any single class, so a class's row count already equals its distinct-student count. The task is to report every class whose enrollment reaches the inclusive threshold of five, in any order.

We work through the registry of the official example. It is small enough to enumerate by hand, yet it already contains the decisive shape of the problem: one class clears the bar comfortably while three others miss it by a wide margin. The real lesson is not "count to five" but *where in the evaluation pipeline that count becomes available*.

## 1. Instance, Contract, and Outcome

The registry and its required output:

| `student` | `class` |
|:---:|:---|
| `A` | `Math` |
| `B` | `English` |
| `C` | `Math` |
| `D` | `Biology` |
| `E` | `Math` |
| `F` | `Computer` |
| `G` | `Math` |
| `H` | `Math` |
| `I` | `Math` |

| `class` | Why it appears in the result |
|:---:|:---|
| `Math` | Its six enrollment rows reach the inclusive threshold of five |

Nine enrollment rows, four distinct class values, one surviving class.

### What the contract fixes, and what it leaves open

- **Input space.** `Courses(student, class)`, with `(student, class)` as the primary key. A student may legitimately appear in several classes; it is the pair, not the student, that is unique.
- **Output space.** A one-column relation named `class`. Because the required order is "any order", no ranking or tie-breaking rule is needed.
- **Threshold semantics.** "At least five" is inclusive: five enrollments qualify, four do not.

## 2. Why Row-Level Filtering Cannot Answer This Question

The instinctive first move is to discard uninteresting rows with a row predicate and then project what remains. That move fails here, and the failure is structural rather than a matter of taste.

| Evaluation stage | Unit it examines | Quantities in scope | Can it test the threshold? |
|:---|:---|:---|:---|
| Row filter | one enrollment row | `student` and `class` of that row | No — a lone row carries no group size |
| Grouping | all rows sharing a `class` value | the member roster of one class | Yes — the roster length *is* the group size |
| Group filter | one assembled group | that group's aggregate values | Yes — this is the correct layer |
| Projection | surviving groups | the grouping key | Not applicable — the decision is already made |

The table records an ordering constraint: a class's cardinality does not exist until all rows of that class have been gathered. Any predicate that mentions a count must therefore be evaluated at or after the grouping stage. A row-level predicate is evaluated before grouping, so it can never observe the quantity the problem is about.

## 3. Cardinality Threshold Invariant

Define the partition that the grouping key induces. For a class value $k$, let

$$
G(k) = \{\, r \in \text{Courses} \;\mid\; r.\text{class} = k \,\},
\qquad
C(k) = \lvert G(k) \rvert .
$$

These $G(k)$ partition the relation, so the group sizes must account for every row exactly once:

$$
\sum_{k \,\in\, \Pi(\text{class})} C(k) = N,
\qquad N = \lvert \text{Courses} \rvert ,
$$

where $\Pi(\text{class})$ is the set of distinct class values in the relation.

> **Threshold invariant.** A class value $k$ appears in the projected result if and only if $C(k) \ge 5$. Every other attribute of the enrollment rows — student identity, insertion order, physical row position — is irrelevant to that decision.

Two consequences follow at once. First, the result is a set of grouping keys, so each class can appear at most once however many rows it owns; duplicate suppression is automatic rather than an extra step. Second, the answer is invariant under any permutation of the input rows, because a partition is defined by value equality and not by position.

## 4. Worked Evaluation of the Official Registry

**Step 1 — Partition the enrollments by `class`.** One pass over the nine rows routes each row into the bucket named by its `class` value.

| Class $k$ | Member roster $G(k)$ | Cardinality $C(k)$ |
|:---|:---|:---:|
| `Math` | `A`, `C`, `E`, `G`, `H`, `I` | $6$ |
| `English` | `B` | $1$ |
| `Biology` | `D` | $1$ |
| `Computer` | `F` | $1$ |

The cardinalities sum to $6 + 1 + 1 + 1 = 9 = N$, so no row was lost or counted twice while routing.

**Step 2 — Evaluate the threshold on each assembled group, never on individual rows.**

| Class $k$ | $C(k)$ | Test $C(k) \ge 5$ | Verdict |
|:---|:---:|:---:|:---|
| `Math` | $6$ | $6 \ge 5$, true | Survives the group filter |
| `English` | $1$ | $1 \ge 5$, false | Rejected |
| `Biology` | $1$ | $1 \ge 5$, false | Rejected |
| `Computer` | $1$ | $1 \ge 5$, false | Rejected |

**Step 3 — Project the surviving grouping key.** Exactly one group survives, so the projected relation holds the single row `Math`.

Note what did *not* happen: no row of `Math` was inspected individually to reach the verdict. The six-member roster was measured as one object. That shift from per-row to per-group reasoning is the entire technique.

## 5. Boundary Analysis

Since the predicate is one comparison against a constant, all interesting behaviour lives at the boundary. The next table varies only the cardinality of a single class and records the verdict.

| $C(k)$ | Test $C(k) \ge 5$ | Verdict | Situation it models |
|:---:|:---:|:---|:---|
| $0$ | false | The class never appears | A class name mentioned nowhere in the relation |
| $4$ | $4 \ge 5$, false | Rejected | One enrollment short of the bar |
| $5$ | $5 \ge 5$, true | Included | Exactly at the inclusive boundary |
| $6$ | $6 \ge 5$, true | Included | The `Math` group of this instance |
| $10^5$ | true | Included | Bulk enrollment; cardinality alone decides |

Replacing the inclusive comparison with a strict one shifts the boundary by exactly one student and would silently drop the $C(k) = 5$ case — precisely the case the threshold wording protects. When no class qualifies, the projection still returns a well-formed relation: zero rows beneath the `class` column, not `NULL` and not an error.

## 6. Elimination of Tempting Alternatives

| Alternative | Why it attracts | Why it fails or costs more |
|:---|:---|:---|
| Testing the count in a row-level predicate | Mirrors the English requirement literally | Aggregate values do not exist yet at that stage; the predicate cannot be evaluated |
| A strict comparison against five | Guards against "more than five" | Misreads "at least five" and loses classes with exactly five students |
| Counting distinct students explicitly | Looks safer against duplicate rows | Redundant under the primary key, since the row count already equals the distinct-student count. It would only matter if the key were removed |
| Filtering in an enclosing query over a grouped subquery | Reaches the same answer | Correct, but forces the intermediate group table to be named and projected, adding a nesting level for no gain over a group-level filter |
| Sorting the relation before grouping | Feels like a prerequisite | A full sort costs $\Theta(N \log N)$ and buys nothing; hash grouping reaches the same partitions in one pass |

## 7. Cost of the Method

Let $N$ be the number of enrollment rows and $K$ the number of distinct classes, so $K \le N$ and the partition identity gives $\sum_k C(k) = N$.

**Time complexity.** Hash grouping performs one probe-and-increment per row, which is $O(N)$ expected. Applying the threshold touches each of the $K$ assembled groups once, at $O(K)$. Projection emits at most $K$ keys, also $O(K)$. Since $K \le N$,

$$
O(N) + O(K) + O(K) = O(N).
$$

A sort-based grouping implementation would instead pay $O(N \log N)$ for its ordering pass; the hash path avoids that. Crucially, the cost does not grow with group *sizes*: measuring a group of $10^5$ rows costs no more than measuring a group of two, because only the counter is inspected. Nor does the cost depend on the threshold value, since comparing against a constant is $O(1)$ per group.

**Auxiliary-space complexity.** One counter per live group is retained, so aggregation state is $O(K)$. The $O(N)$ figure that is sometimes quoted describes the size of the relation being read, not extra working memory that grows with class cardinality: the method never materializes a class's member list in order to measure it, and it does not buffer the projected result before emitting it. Peak auxiliary space is therefore $O(K)$, degrading to $O(N)$ only in the degenerate case where every row belongs to its own class.
