# Guided Example: Duplicate Emails

We work one small registration table through a grouped aggregation end to end, tracking exactly how rows collapse into email equivalence classes and how the group-size threshold decides which classes survive.

- **Representative relation (`Person`):** rows `(1, "a@b.com")`, `(2, "c@d.com")`, `(3, "a@b.com")`.
- **Required result:** a single-column relation named `Email` containing the value `"a@b.com"`.
- **Contrasting instances used later:** an all-distinct table, which must return no rows, and a triple repetition, which must still return exactly one row.

## 1. Instance and Required Outcome

The source relation is `Person(id, email)`, where `id` is the primary key (a column of unique values) and `email` holds non-null lowercase addresses. The task is to report every address that is registered on more than one row.

| `id` (primary key) | `email` |
|:---:|:---|
| 1 | `"a@b.com"` |
| 2 | `"c@d.com"` |
| 3 | `"a@b.com"` |

The answer is not "the rows that look repeated". It is the set of *address values* whose multiplicity exceeds one. Row 1 and row 3 are different tuples — their `id` values differ — but they carry the same address, so the address they share is a duplicate value. The requested output schema has one column, `Email`, and the value identity that matters is the string itself, never the row it came from.

## 2. What Grouping by Email Actually Computes

Grouping by `email` partitions the full row set into equivalence classes under the relation "carries the same address". A partition has two defining properties that the rest of the argument depends on:

1. **Disjointness.** A row belongs to exactly one class, because a row has exactly one `email` value.
2. **Coverage.** The union of the classes is the whole relation; no row is dropped.

For an address value $e$ define its class and its multiplicity:

$$
G(e) = \{\, r \in \text{Person} \;\mid\; r.\text{email} = e \,\},
\qquad
c(e) = \lvert G(e) \rvert .
$$

Because the statement guarantees `email` is never null, equality is total here: no row escapes classification, and $c(e) \ge 1$ for every class the partition produces. The aggregated relation therefore has exactly one row per distinct address value, and its count attribute equals that class's multiplicity.

| Distinct address $e$ | Class $G(e)$ (contributing `id` values) | Multiplicity $c(e)$ |
|:---|:---|:---:|
| `"a@b.com"` | $\{1, 3\}$ | 2 |
| `"c@d.com"` | $\{2\}$ | 1 |

## 3. Streaming Trace of the Grouping Pass

A hash-based aggregation reads the relation once and keeps one bucket per distinct key, holding the running multiplicity and the contributing `id` values. Nothing about a bucket is final until the scan ends, which is the key observation for the next section.

| Scan step | Tuple examined | Bucket state after the step | Final? |
|:---:|:---|:---|:---:|
| 0 | — (empty bucket table) | — | — |
| 1 | `(1, "a@b.com")` | `"a@b.com"` → $\{1\}$, count 1 | no |
| 2 | `(2, "c@d.com")` | `"a@b.com"` → $\{1\}$, count 1; `"c@d.com"` → $\{2\}$, count 1 | no |
| 3 | `(3, "a@b.com")` | `"a@b.com"` → $\{1,3\}$, count 2; `"c@d.com"` → $\{2\}$, count 1 | yes |

Only one pass over the rows is needed, and every row performs a single constant-time bucket lookup and increment. No ordering of the input is required when hashing is available; a sort-based plan would reach the same partition with cost $O(N \log N)$ instead of the expected $O(N)$.

## 4. Why a Row-Level Filter Cannot Express This Threshold

The qualifying predicate is $c(e) > 1$ — a property of a *class*, not of a *row*. A row-level filter inspects one tuple's own attributes. After step 1 above, the tuple `(1, "a@b.com")` is indistinguishable from a tuple whose address occurs only once; its class membership is still open. Any decision made at that moment could be contradicted by a later row, so the predicate is simply not evaluable at row granularity.

Relational evaluation therefore separates the two stages, and the filter belongs to the second one:

| Stage | Input | Operation | Predicate that may be evaluated here |
|:---:|:---|:---|:---|
| 1 | `Person` rows | Partition the rows by `email` and compute each class size | Row-attribute conditions only — the group sizes do not exist yet |
| 2 | One row per email class, with its count | Retain classes satisfying $c(e) > 1$ | Aggregate conditions such as a group cardinality comparison |
| 3 | Retained classes | Project the address attribute under the header `Email` | None; the schema is fixed at this point |

In relational terms the first stage is the grouping clause, the second is the post-aggregation group-qualification filter, and the third is the projection list. Writing the threshold into a pre-grouping row filter is a semantic error, not a stylistic one: the aggregate function is undefined before the partition exists.

Two identity points matter. Distinctness is value identity, not index identity, so `id` 1 and `id` 3 belong to the same class despite their different keys. And comparison is on the entire address string, not a prefix or a case-folded variant; the statement already guarantees lowercase, so no normalization step is warranted.

## 5. Evaluating the Threshold on This Instance

After the grouping pass completes, each class is tested against the multiplicity threshold and the surviving classes are projected.

| Class key $e$ | Members | $c(e)$ | $c(e) > 1$ | Decision | Projected row |
|:---|:---|:---:|:---:|:---|:---|
| `"a@b.com"` | `{1, 3}` | 2 | true | **retained** | `"a@b.com"` |
| `"c@d.com"` | `{2}` | 1 | false | discarded | — |

| `Email` |
|:---|
| `"a@b.com"` |

The surviving set is independent of the physical scan order, because a multiplicity is a property of the whole table; the statement accepts the answer in any order.

## 6. Correctness of the Grouping-and-Threshold Method

**Soundness.** Suppose an address $e$ is emitted. It comes from a class with $c(e) > 1$, so $G(e)$ contains at least two rows. Since `id` is the primary key, two distinct rows cannot share a key, so those two rows are genuinely different tuples of `Person` that both carry $e$. The emitted value is therefore a real duplicate.

**Completeness.** Every row of `Person` belongs to exactly one class by disjointness and coverage. Consequently every address value present in the table has its multiplicity measured, and any value with $c(e) > 1$ satisfies the retained predicate. No duplicate address can be missed.

**Uniqueness of the output.** The grouping stage emits one row per class, so a repeated address can never appear twice in the answer. A separate duplicate-elimination pass over the projection is therefore unnecessary.

**Monotonicity.** Bucket counts only increase as the scan proceeds, so no class can be prematurely discarded and later need reinstating; there is no backtracking, and a single forward pass suffices.

**Ties and higher multiplicities.** Nothing in the argument depends on the multiplicity being exactly two. See the boundary table below, where a multiplicity of three still yields one emitted row rather than three or two.

## 7. Boundary and Multiplicity Traps

| Instance | Input shape | Expected result | Why it is a trap |
|:---|:---|:---|:---|
| All addresses distinct | `(1, "a@x")`, `(2, "b@x")` | empty relation | Both classes have multiplicity 1, so the strict threshold rejects both; returning "the most frequent address" is wrong |
| Triple repetition | `(1, "x@y")`, `(2, "x@y")`, `(3, "x@y")` | one row: `"x@y"` | A counting scheme that emitted once per repeated pair would return several rows; the class is a single output unit |
| Several duplicated values | five rows over three distinct addresses, two of them duplicated | one row per duplicated address | The threshold is applied per class independently; the result is a set, not a single winner |
| Large repeated group | an address on many rows | one row | Cost grows with the number of distinct keys, not with the largest multiplicity, when hashing is used |
| Null addresses | excluded by the statement guarantee | undefined | Equality-based grouping of nulls is a distinct SQL semantic; the guarantee removes the case entirely |

The null row of the table is moot in practice: because every `email` is guaranteed present, no class ever forms around an unknown value.

## 8. Alternative Formulations and Their Costs

| Formulation | Relational shape | Cost on a class of size $k$ | Verdict |
|:---|:---|:---|:---|
| Grouped aggregation plus a group-cardinality filter | One pass partitions rows, then one row per class is tested | $O(k)$ for the class's bucket | Preferred: one pass, one output row per class, no post-processing |
| Self-join of the relation with itself on equal address and differing key | Pairs every row with every other row sharing its address | $\Theta(k^2)$ ordered pairs survive the join, before any duplicate elimination | Wasteful: multiplicities are inflated, and a further projection with duplicate removal is required to recover one row per class |
| Windowed count over an address partition, then a row-level test | Sort or hash by address, accumulate a running partition count | $O(k)$ accumulation, but $O(N \log N)$ if implemented by sorting | Correct but heavier: the partition count is materialized on every row and then re-filtered, duplicating group state per row |

The first formulation is the one the invariant describes directly. The self-join is the tempting alternative and the one this instance is built to rule out: with the two-row class `"a@b.com"` it happens to produce the right answer after deduplication, but its intermediate size grows quadratically in the largest multiplicity, which no output ever needs.

> **Invariant.** An address $e$ appears in the result set if and only if $\lvert\{\, r \in \text{Person} \mid r.\text{email} = e \,\}\rvert \ge 2$, and each qualifying address appears exactly once.

## 9. Complexity Derivation

Let $N$ be the number of rows in `Person` and $U$ the number of distinct address values, with $U \le N$.

**Time.** The grouping pass performs one bucket lookup and one increment per row, which is expected $O(1)$ per row under hashing, giving $O(N)$ for the scan. The threshold filter then tests exactly one row per class, adding $O(U) \subseteq O(N)$. The projection is $O(U)$. The expected bound is therefore

$$
T(N) = O(N) + O(U) = O(N).
$$

A plan that groups by sorting instead pays

$$
T_{\text{sort}}(N) = O(N \log N),
$$

which is asymptotically worse but same-order in memory and equally correct. The self-join alternative pays at least

$$
T_{\text{join}}(N) = O\!\left(\sum_{e} c(e)^2\right),
$$

which degrades to $O(N^2)$ when a single address dominates the table — the case the multiplicity trap is designed to expose.

**Auxiliary space.** The aggregation state holds one bucket per distinct key, so

$$
S(N) = O(U) \subseteq O(N),
$$

plus the retained output, which is at most one row per class. The self-join formulation instead materializes $\Theta\!\left(\sum_e c(e)^2\right)$ intermediate pairs, which can be quadratic.