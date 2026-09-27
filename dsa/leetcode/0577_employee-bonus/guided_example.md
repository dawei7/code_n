# Guided Example: Employee Bonus

"Which employees received a bonus below 1000?" sounds like a single filter, but the data model makes it two questions in one. `Bonus` is keyed by employee and is *optional*: a row either exists or it does not, and the statement declares that a missing bonus also satisfies the condition. The qualifying set is therefore a union of two very different populations — employees with a small recorded bonus and employees with no record at all — and the work lies in making one filter see both without inventing a bonus that was never recorded.

## 1. The Instance and the Required Outcome

| `empId` | `name` | `supervisor` | `salary` |
|:---:|:---:|:---:|:---:|
| 3 | `Brad` | absent | 4000 |
| 1 | `John` | 3 | 1000 |
| 2 | `Dan` | 3 | 2000 |
| 4 | `Thomas` | 3 | 4000 |

| `empId` | `bonus` |
|:---:|:---:|
| 2 | 500 |
| 4 | 2000 |

Three of the four employees qualify. `Dan` has a recorded bonus of 500, below the threshold. `Brad` and `John` have no row in `Bonus` at all. `Thomas` has 2000, above the threshold, and is excluded. The required result carries the `name` and `bonus` of every qualifying employee, in any order:

| `name` | `bonus` |
|:---:|:---:|
| `Brad` | absent |
| `John` | absent |
| `Dan` | 500 |

The `absent` entries are not placeholders for zero. The contract asks for the bonus amount, and for an employee with no record that amount is the null value; `Dan`'s row reports the real recorded 500. Emitting 0 in place of the null would change the reported data even though it would not change which rows are selected.

## 2. Two Ways to Qualify

Write $E$ for the employee relation and $B$ for the bonus relation, and let $\mathrm{rec}(e)$ be the bonus recorded for employee $e$, defined only when $B$ holds a row keyed by $e$. The qualifying set is the disjoint union

$$
Q = \underbrace{\{\,e \in E : \mathrm{rec}(e) \text{ is undefined}\,\}}_{\text{no bonus record}}
\;\cup\;
\underbrace{\{\,e \in E : \mathrm{rec}(e) < 1000\,\}}_{\text{small recorded bonus}} .
$$

| Employee class | `Bonus` row exists? | Recorded value | In $Q$? | Reported `bonus` |
|:---|:---:|:---:|:---:|:---:|
| Small recorded bonus | yes | below 1000 | yes | the recorded value |
| Large recorded bonus | yes | 1000 or more | no | not reported |
| No record | no | undefined | yes | the null value |

Only one of the two predicates can hold for a given employee, so the task reduces to finding a single test that is true for the first and third classes. That test cannot be the natural one, `bonus` below 1000, for the reason the next two sections develop.

> **Coverage invariant.** Every employee appears exactly once in the joined relation built from `Employee` and `Bonus`, whether or not a bonus record exists. None can be lost, and none can be duplicated.

## 3. The Outer Join and the Emergence of a Missing Value

An inner join pairs employees with bonus records and discards everything else; here it would keep only `Dan` and `Thomas`, silently deleting the two employees the statement names as qualifying. The join must therefore preserve the left relation in full, which is the defining property of a left outer join: every row of `Employee` survives, and columns taken from `Bonus` carry the null value wherever no partner row exists.

| `empId` | `name` | Joined `bonus` | Origin of the value |
|:---:|:---:|:---:|:---|
| 3 | `Brad` | null | no partner row in `Bonus` |
| 1 | `John` | null | no partner row in `Bonus` |
| 2 | `Dan` | 500 | partner row `(empId = 2, bonus = 500)` |
| 4 | `Thomas` | 2000 | partner row `(empId = 4, bonus = 2000)` |

The row count equals the employee count, and that equality rests on a declared guarantee: `empId` is the unique column of `Bonus`, so a left row matches at most one right row. Without uniqueness an employee with several bonus records would fan out and the one-row-per-employee invariant would fail. This is the property that makes an outer join safe for *preserving* rows rather than multiplying them.

## 4. Three-Valued Logic and Why the Natural Filter Fails

Comparisons involving the null value yield neither true nor false but an unknown third result, and a filter keeps only rows whose predicate is definitely true. The comparison `bonus` below 1000 is unknown precisely for `Brad` and `John` — exactly the employees with no bonus record:

| `bonus` in the joined row | Below 1000? | Is the null value? | Disjunction of the two | Substituted comparison |
|:---:|:---:|:---:|:---:|:---:|
| 500 (`Dan`) | true | false | true | true |
| 2000 (`Thomas`) | false | false | false | false |
| 1000 (hypothetical) | false | false | false | false |
| null (`Brad`, `John`) | **unknown** | true | true | true |

Two repairs agree on every class: disjoining "no record" with the threshold test, or substituting a default value that is itself below the threshold so the comparison becomes decidable. The substitute must lie strictly below 1000 — substituting 1000 would drop `Brad` and `John` and reproduce the failure the outer join was introduced to avoid — and it must stay inside the predicate, because the projected `bonus` column still carries the original null. The reported amount is a fact about the data; the substitute is only an analytical device.

## 5. Worked Trace of the Official Instance

| Employee | Outer join outcome | Compared quantity | Below 1000? | Included? | Emitted row |
|:---:|:---|:---:|:---:|:---:|:---|
| `Brad` (`empId` 3) | no partner row, bonus is null | 0 | true | **yes** | `("Brad", null)` |
| `John` (`empId` 1) | no partner row, bonus is null | 0 | true | **yes** | `("John", null)` |
| `Dan` (`empId` 2) | partner `(2, 500)` | 500 | true | **yes** | `("Dan", 500)` |
| `Thomas` (`empId` 4) | partner `(4, 2000)` | 2000 | false | no | — |

Three rows survive; the fourth is rejected on its recorded value, not on a missing record. Under the natural filter the outcome is entirely different: the predicate is undecidable for `Brad` and `John`, so they are removed and only `Dan` is returned. That filter is not merely incomplete — it drops precisely the employees the statement added a clause to protect, which is what makes missing-value semantics the central idea of the problem rather than an edge case.

## 6. Correctness of the Null-Safe Qualification

The method is correct if the rows it keeps are exactly the members of $Q$.

*Every employee is represented once.* The outer join retains every left row and attaches at most one right row, by uniqueness of `Bonus.empId`, so the joined relation is in bijection with `Employee`.

*The predicate is decidable and faithful.* For an employee with a recorded value $b$, the substitution returns $b$ itself, so the test is the original comparison and agrees with the second branch of $Q$. For an employee with no record it returns 0, and $0 < 1000$ is true, so the test agrees with the first branch. Because 0 is strictly below the threshold, that direction is guaranteed rather than incidental.

*No member of $Q$ is lost and no non-member survives.* A qualifying employee has either an undefined recorded value, where the test is true, or a recorded value below 1000, where the test is that value's own comparison and is true. An employee with a recorded value of 1000 or more makes the test false — exactly 1000 fails because the requirement is strict — and an employee outside $Q$ always has a defined value that is not below the threshold. The substitute is confined to the comparison, so an absent record is still reported as the null value and a present record is reported unchanged.

## 7. Boundary Cases and the Clause-Placement Trap

| Situation | Behaviour | Result |
|:---|:---|:---|
| Recorded bonus exactly 1000 | the comparison is strict, so the test is false | excluded, correctly |
| `Bonus` completely empty | every joined row carries null and every substituted quantity is 0 | all employees reported with a null bonus |
| Every recorded bonus at least 1000 | no row satisfies the comparison | an empty result, which the contract permits |
| An employee with no bonus and no supervisor | the bonus logic ignores unrelated null columns | the employee is still reported |
| Two employees sharing a `name` | the join and the filter key on `empId` | both are preserved as distinct employees |
| Threshold attached to the join condition instead of the filter | a large recorded bonus finds no partner row, so it becomes null and then qualifies | `Thomas` would be wrongly reported with a null bonus |
| Null replaced before projection | the reported amount becomes 0 rather than null | the row set is right but the reported facts are wrong |

The clause-placement trap produces exactly the wrong row set while looking structurally similar to the correct method. If the threshold is attached to the join condition, `Thomas` finds no partner row because his 2000 fails the condition, so the outer join emits a null for him and the substitution then admits him. Four rows appear where three are correct, and every row looks plausible because it carries a null bonus just like a legitimate absent-record row. A left outer join decides only which rows pair up; the filter decides which rows are reported, and mixing the two turns a value test into a presence test.

## 8. Alternative Strategies and Their Trade-offs

| Strategy | Relational shape | Cost | Assessment |
|:---|:---|:---|:---|
| Outer join, then a null-safe comparison | preserve every employee, substitute inside the predicate | $\Theta(E + B)$ with a hash table on the bonus key | the method traced above; one pass over each relation |
| Inner join plus a separate absent-bonus branch | pair matches, then union in the employees with no row | at least two passes plus duplicate elimination | correct only with the explicit union, which is more machinery for the same rows |
| Anti-join union with a filtered join | find employees with no partner, union the small-bonus employees | two scans plus a set union | correct and explicit, but reasons about each employee twice |
| Correlated existence test per employee | probe for a matching record and its value | $\Theta(E \log B)$ with an index, $\Theta(E \cdot B)$ without | cost is driven by employees times probes rather than by relation sizes |
| Aggregate each employee's records first, then join | collapse bonus records to one value per employee | $\Theta(B + E)$ | redundant work unless duplicates are possible |

The last alternative isolates the role of key uniqueness. If `Bonus.empId` were not unique, collapsing each employee's records to one value would be necessary before the filter could apply at all; with the declared guarantee that collapse is pure overhead, so the choice depends on a schema fact rather than on taste.

## 9. Complexity Derivation

Let $E$ be the number of rows in `Employee` and $B$ the number of rows in `Bonus`.

- **Time.** The outer join builds a lookup structure on the bonus key and probes it once per employee, costing $\Theta(E + B)$ expected time. The predicate is one comparison per joined row, $\Theta(E)$, and the projection is proportional to the reported rows. Total: $\Theta(E + B)$, strictly linear in the combined input size. No ordering is needed because any output order is accepted.
- **Auxiliary space.** The join maintains its lookup structure over `Bonus`, which is $\Theta(B)$; the employee relation can be streamed. The result holds up to $E$ rows, but the working memory beyond the output is $\Theta(B)$.

For the official instance $E = 4$ and $B = 2$: six rows are read, four joined rows are tested, and three are reported. The cost is dominated by reading the inputs, not by the null handling.
