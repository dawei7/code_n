# Guided Example: Nth Highest Salary

This request generalises the rank question: a database routine receives a positive integer $N$ and must return the $N$-th highest **distinct** salary, or `null` when fewer than $N$ distinct salaries exist. Because the routine returns a single scalar value, both the missing-rank case and the short-table case produce `null` rather than an empty relation.

## 1. The Instance and the Requested Rank

The worked call uses the three-employee relation with $N = 2$.

| `id` | `salary` |
|:---:|:---:|
| 1 | 100 |
| 2 | 200 |
| 3 | 300 |

The distinct salary set is $\{100, 200, 300\}$, and the value at rank 2 is $200$, emitted under the column label `getNthHighestSalary`.

Four contrasting instances sharpen the contract, and every one of them is a case the routine must handle without special-casing:

| Instance | $N$ | Distinct values, largest first | Required result |
|:---|:---:|:---|:---|
| `[(1,100),(2,200),(3,300)]` | 2 | $[300, 200, 100]$ | `200` |
| `[(1,100)]` | 2 | $[100]$ | `null` |
| `[(1,300),(2,300),(3,200)]` | 2 | $[300, 200]$ | `200` |
| `[(1,10),(2,30),(3,20)]` | 1 | $[30, 20, 10]$ | `30` |

## 2. One-Based Ranks and Zero-Based Skip Counts

Requested ranks are one-based, while positional access into an ordered sequence is zero-based. The two conventions must be reconciled before any lookup happens, because the arithmetic of the correction depends on which convention each step uses.

| Rank requested $N$ | Meaning | Distinct values strictly greater | Rows to skip before reading | Zero-based position read |
|:---:|:---|:---:|:---:|:---:|
| 1 | highest | 0 | 0 | 0 |
| 2 | second highest | 1 | 1 | 1 |
| 3 | third highest | 2 | 2 | 2 |
| $k$ | $k$-th highest | $k-1$ | $k-1$ | $k-1$ |

The translation is therefore a single shift:

$$ \text{skip} = N - 1, \qquad \text{position} = N - 1 . $$

Treating the routine as "decrement the requested rank once, then read one value at that skip distance" keeps one source of truth for the off-by-one correction. Two independent adjustments — one while counting distinct values and one while reading — are the classic source of the error this instance exposes.

## 3. Dense Ordering of the Distinct Salary Set

Duplicates must collapse before the rank is read; otherwise a repeated salary consumes several rank slots and every later rank shifts.

| `id` | `salary` | Enters the distinct set? | Distinct set after this row | Dense rank of this row's value |
|:---:|:---:|:---:|:---|:---:|
| 1 | 100 | yes | $[100]$ | 3 |
| 2 | 200 | yes | $[200, 100]$ | 2 |
| 3 | 300 | yes | $[300, 200, 100]$ | 1 |

The same reading on a table whose maximum is duplicated shows why deduplication is a semantic requirement rather than an optimisation.

| `id` | `salary` | Enters the distinct set? | Distinct set after this row | Dense rank of this row's value |
|:---:|:---:|:---:|:---|:---:|
| 1 | 300 | yes | $[300]$ | 1 |
| 2 | 300 | no — already present | $[300]$ | 1 |
| 3 | 200 | yes | $[300, 200]$ | 2 |

In the second table rank 2 belongs to $200$, not to the duplicate $300$. Skipping deduplication would fill rank 2 with a second copy of $300$, and the routine would silently answer a different question.

## 4. Step-by-Step Evaluation of the Call

Tracing $N = 2$ over `[(1,100),(2,200),(3,300)]`:

| Step | Requested rank and state | Operation on the relation | Result |
|:---:|:---|:---|:---|
| 1 | $N = 2$ | shift the requested rank once: $N \leftarrow N - 1$ | skip distance $1$ |
| 2 | skip distance $1$ | deduplicate the salary column | $S = \{100, 200, 300\}$ |
| 3 | skip distance $1$ | order $S$ from largest to smallest | $[300, 200, 100]$ |
| 4 | skip distance $1$ | skip 1 row, retain 1 row | $200$ |
| 5 | — | return the retained value as the routine's scalar result | `200` |

Both the ordering and the retention are independent of the parameter; only the skip distance is derived from $N$. That is precisely why the shift can be performed once, before the lookup, instead of being recomputed inside it.

## 5. Out-of-Range Requests and the Null Fallback

| Requested $N$ | Distinct values available | Rows skipped | Value found | Emitted |
|:---:|:---|:---:|:---:|:---:|
| 1 | $[300, 200, 100]$ | 0 | $300$ | `300` |
| 2 | $[300, 200, 100]$ | 1 | $200$ | `200` |
| 3 | $[300, 200, 100]$ | 2 | $100$ | `100` |
| 4 | $[300, 200, 100]$ | 3 | none | `null` |
| 2 | $[100]$ | 1 | none | `null` |

The last two rows describe the same situation: the skip distance walks past the end of the ordered sequence, the lookup yields no value, and the routine's scalar return type converts "no value" into `null`. This is why the routine must return through an expression rather than through a filtered relation — a relation would produce zero rows, while the contract demands a single `null` scalar.

## 6. Why the Reasoning Is Correct

**Invariant.** Let $S = \{s_1 > s_2 > \dots > s_d\}$ be the distinct salaries ordered from largest to smallest, and let $N \ge 1$. The routine returns $s_N$ when $N \le d$, and `null` when $N > d$.

*Soundness.* Position $N - 1$ of the descending sequence holds $s_N$ by construction, and $s_N$ is exceeded by exactly $N - 1$ distinct values, which is the definition of the $N$-th highest distinct salary. The shifted skip distance names that position exactly, so the value read is the value requested.

*Completeness.* Deduplication is applied before the rank is read, so every distinct value occupies exactly one position and no rank is consumed twice. The skip-then-retain lookup reads the demanded position whenever that position exists; when it does not exist, the scalar coercion of the empty lookup produces the required `null`. Hence every legal $N$ is answered, and no illegal $N$ produces a spurious salary.

## 7. Boundary Conditions This Instance Exposes

| Scenario | Instance | Required result | Reason |
|:---|:---|:---|:---|
| $N$ exceeds the number of distinct values | `[(1,100)]`, $N = 2$ | `null` | A skip distance of 1 exists in no sequence of length 1. |
| Duplicate maximum | `[(1,300),(2,300),(3,200)]`, $N = 2$ | `200` | The duplicate shares rank 1, so rank 2 is $200$. |
| $N = 1$ | `[(1,10),(2,30),(3,20)]`, $N = 1$ | `30` | A skip distance of 0 reads the largest value. |
| $N$ equals the number of distinct values | `[(1,9),(2,7),(3,8),(4,9)]`, $N = 3$ | `7` | The distinct set is $\{9, 8, 7\}$ and the final position holds $7$. |
| $N$ is not positive | any table, $N \le 0$ | `null` or an explicit rejection | Positional access is undefined for negative skip distances, so the value must be validated before the lookup. |
| Single row, $N = 1$ | `[(1,42)]` | `42` | The only distinct value occupies rank 1. |

## 8. Complexity Derivation

Let $M$ be the number of rows in `Employee` and $d \le M$ the number of distinct salaries.

| Stage | Cost |
|:---|:---|
| Deduplicate $M$ rows | $O(M)$ expected with hashing, $O(M \log M)$ if the ordering itself is used to collapse duplicates |
| Order $d$ distinct values from largest to smallest | $O(d \log d)$, or $O(d)$ when an index on `salary` already supplies the order |
| Read one position at skip distance $N - 1$ | $O(1)$ once the ordered sequence exists |
| Total | $O(M \log M)$ worst case; $O(M)$ expected with hashing plus a bounded-size selection |

Every row must be inspected at least once to know whether its salary is a new distinct value, so $\Omega(M)$ is a genuine lower bound for the deduplication step alone.

**Auxiliary space.** The straightforward formulation buffers the $d$ distinct ordered values, giving $O(d) \le O(M)$ auxiliary memory. A streaming implementation that keeps only the largest $N$ distinct values needs $O(N)$ auxiliary memory, which is strictly better when the requested rank is small and fixed, as in the sample call $N = 2$.
