# Guided Example: Department Top Three Salaries

We trace one payroll through a per-department ranking problem where the qualifying unit is a *distinct salary value*, not an employee. The instance is chosen so that the difference between dense and sparse ranking decides a real employee's fate.

- **Representative relations:** `Employee` = `(1, "Joe", 85000, 1)`, `(2, "Henry", 80000, 2)`, `(3, "Sam", 60000, 2)`, `(4, "Max", 90000, 1)`, `(5, "Janet", 69000, 1)`, `(6, "Randy", 85000, 1)`, `(7, "Will", 70000, 1)`; `Department` = `(1, "IT")`, `(2, "Sales")`.
- **Required result:** `("IT", "Max", 90000)`, `("IT", "Joe", 85000)`, `("IT", "Randy", 85000)`, `("IT", "Will", 70000)`, `("Sales", "Henry", 80000)`, `("Sales", "Sam", 60000)`.
- **Decisive feature:** IT contains four distinct salary values, and the fourth one, `69000`, belongs to `Janet`, who must be excluded — while `Will` at `70000` must be included.

## 1. Instance and Required Outcome

`Employee(id, name, salary, departmentId)` holds one row per employee with `id` as the primary key (a column of unique values) and `departmentId` a foreign key referencing `Department.id`. `Department(id, name)` supplies the names.

| `Employee.id` | `name` | `salary` | `departmentId` |
|:---:|:---|:---:|:---:|
| 1 | `"Joe"` | 85000 | 1 |
| 2 | `"Henry"` | 80000 | 2 |
| 3 | `"Sam"` | 60000 | 2 |
| 4 | `"Max"` | 90000 | 1 |
| 5 | `"Janet"` | 69000 | 1 |
| 6 | `"Randy"` | 85000 | 1 |
| 7 | `"Will"` | 70000 | 1 |

| `Department.id` | `name` |
|:---:|:---|
| 1 | `"IT"` |
| 2 | `"Sales"` |

A "high earner" is an employee whose salary is among the **top three unique salaries** of their department. The word *unique* does real work: a department of six employees with distinct amounts has three high earners, while a department whose top amount is shared by four people has more than three, because all four occupy the same tier. The output schema is `Department`, `Employee`, `Salary`, in any row order.

## 2. Distinct Salary Tiers Inside a Partition

Fix a department $d$ and let $V_d$ be the set of distinct salary values occurring in it, ordered so that

$$
V_d = \{\, v_1 > v_2 > \dots > v_{m_d} \,\}, \qquad m_d = \lvert V_d \rvert .
$$

The *tier index* of a value is its one-based position in that descending order:

$$
r_d(v) = \lvert \{\, u \in V_d \;\mid\; u > v \,\} \rvert + 1 .
$$

The definition uses the strictly greater relation on the *value set*, so ties at the same amount collapse into one tier and the number of tiers is $m_d$ rather than the number of employees. An employee $e$ in department $d$ is a high earner exactly when

$$
r_d(e.\text{salary}) \le 3 ,
$$

equivalently when at most two distinct amounts in the department are strictly larger than the employee's own.

> **Invariant.** An employee row $e$ is emitted if and only if fewer than three distinct salary values in $e$'s own department are strictly greater than $e.\text{salary}$. The threshold compares *values*, not people, so employees tied at the same amount are always classified together.

## 3. The Rank Function: Counting Strictly Greater Distinct Salaries

The tier index is a counting statement, so it is directly computable without any explicit sorting: restrict to the employee's own department, keep the strictly greater salaries, and count the distinct values that remain. The strict inequality implements "top", the deduplication implements "unique", and three is the cutoff.

| Component of the test | Relation it computes | Consequence if it is wrong |
|:---|:---|:---|
| Restrict the search to the employee's own department | $e'.\text{departmentId} = e.\text{departmentId}$ | Thresholds leak across departments and a strong department inflates its neighbours |
| Require a strictly greater salary | $e'.\text{salary} > e.\text{salary}$ | Using a weak inequality counts the employee's own amount and demotes every tied group by one tier |
| Count distinct amounts rather than rows | $\lvert V_d \cap (e.\text{salary}, \infty) \rvert$ | Co-earners at a higher amount are counted repeatedly and lower tiers are pushed out prematurely |
| Compare the count against the cutoff | count $< 3$ | A cutoff of three or fewer *greater* values would admit a fourth tier |

## 4. Worked Trace of the Department Partitions

**IT** ($d = 1$) contains salaries $90000, 85000, 85000, 70000, 69000$, so $V_1 = \{90000, 85000, 70000, 69000\}$ and $m_1 = 4$.

| Tier $r_1(v)$ | Distinct amount $v$ | Employees at that amount | Qualifies ($r_1 \le 3$)? |
|:---:|:---:|:---|:---:|
| 1 | 90000 | `Max` | yes |
| 2 | 85000 | `Joe`, `Randy` | yes |
| 3 | 70000 | `Will` | yes |
| 4 | 69000 | `Janet` | no — three larger distinct amounts exist |

**Sales** ($d = 2$) contains salaries $80000, 60000$, so $V_2 = \{80000, 60000\}$ and $m_2 = 2 < 3$.

| Tier $r_2(v)$ | Distinct amount $v$ | Employees at that amount | Qualifies? |
|:---:|:---:|:---|:---:|
| 1 | 80000 | `Henry` | yes |
| 2 | 60000 | `Sam` | yes |

Because a department can never expose a tier beyond $m_d$, a department with fewer than three distinct amounts cannot fail the test at all — every one of its employees qualifies automatically.

## 5. Evaluating Every Employee Row

| `name` | Dept | `salary` | Strictly greater distinct amounts in the department | Count | Tier index | Decision |
|:---|:---:|:---:|:---|:---:|:---:|:---|
| `"Max"` | 1 | 90000 | — | 0 | 1 | emitted |
| `"Joe"` | 1 | 85000 | $\{90000\}$ | 1 | 2 | emitted |
| `"Randy"` | 1 | 85000 | $\{90000\}$ | 1 | 2 | emitted |
| `"Will"` | 1 | 70000 | $\{90000, 85000\}$ | 2 | 3 | emitted |
| `"Janet"` | 1 | 69000 | $\{90000, 85000, 70000\}$ | 3 | 4 | not emitted |
| `"Henry"` | 2 | 80000 | — | 0 | 1 | emitted |
| `"Sam"` | 2 | 60000 | $\{80000\}$ | 1 | 2 | emitted |

| `Department` | `Employee` | `Salary` |
|:---|:---|:---:|
| `"IT"` | `"Max"` | 90000 |
| `"IT"` | `"Joe"` | 85000 |
| `"IT"` | `"Randy"` | 85000 |
| `"IT"` | `"Will"` | 70000 |
| `"Sales"` | `"Henry"` | 80000 |
| `"Sales"` | `"Sam"` | 60000 |

## 6. Dense Rank Versus Sparse Rank

A windowed rank over the department, ordered by descending salary, is the natural alternative implementation — but only one flavour of rank computes the tier index. Sparse `RANK` gives the next value the position *after* the whole preceding tie group, so it counts employees above rather than distinct amounts above.

| `name` | Dept | `salary` | Dense tier index | Sparse `RANK` | Sparse verdict at cutoff 3 | Correct verdict |
|:---|:---:|:---:|:---:|:---:|:---|:---|
| `"Max"` | 1 | 90000 | 1 | 1 | keep | keep |
| `"Joe"` | 1 | 85000 | 2 | 2 | keep | keep |
| `"Randy"` | 1 | 85000 | 2 | 2 | keep | keep |
| `"Will"` | 1 | 70000 | 3 | **4** | **wrongly dropped** | keep |
| `"Janet"` | 1 | 69000 | 4 | 5 | drop | drop |
| `"Henry"` | 2 | 80000 | 1 | 1 | keep | keep |
| `"Sam"` | 2 | 60000 | 2 | 2 | keep | keep |

The sparse ranking is off by exactly the number of co-earners above the current amount. `Will` sits at tier 3 but has four employees at or above his amount, so sparse rank calls him fourth. A positional rank that numbers each row separately is no better: it breaks ties arbitrarily and likewise pushes `Will` to the fourth position. On a department whose top amounts are all distinct the dense and sparse ranks agree, which is why this instance — with a two-way tie at `85000` — is the one worth tracing.

## 7. Correctness of the Tier-Count Test

**Soundness.** Suppose the test admits an employee. At most two distinct amounts in that department exceed the employee's salary, so the employee's amount occupies one of the first three tiers and qualifies as a high earner.

**Completeness.** Suppose an employee is a high earner, so their amount is one of the top three distinct amounts of the department. Any amount strictly greater than it must also be among those top three, and there are at most two such amounts. The count is therefore at most two, and the test admits the employee.

**Tie preservation.** Two employees with equal salary in the same department examine exactly the same set of greater amounts, so they always receive the same verdict. The tie group is never split, which is why `Joe` and `Randy` are both emitted and why a co-earning top group can exceed three rows.

**Monotone degradation with tier.** The count is non-decreasing as salary decreases within a department, since lowering the salary can only enlarge the set of strictly greater amounts. The qualifying set is therefore a prefix of the department's tiers, and no lower tier can be admitted while a higher one is rejected.

## 8. Boundary and Semantic Traps

| Instance | Input shape | Expected result | Why it matters |
|:---|:---|:---|:---|
| Tie in the middle of the ranking | IT has two employees at 85000 | both emitted | Sparse ranking drops the tier below them; dense counting does not |
| Fewer than three distinct amounts | Sales has only 80000 and 60000 | both employees | A department cannot fail a cutoff it cannot reach |
| Tie at the third tier | three employees at the third distinct amount | all three | Tier membership, not row position, decides; the answer may exceed three rows |
| Fourth distinct amount | IT has 69000 below 70000 | excluded | The cutoff is on distinct amounts, so one more value is enough to push a group out |
| Counting rows instead of amounts | two employees above a candidate | risks premature exclusion | Duplicate higher amounts inflate the count and skip a tier |
| Weak inequality in the count | candidate's own amount compared against itself | shifts every tier by one | "Strictly greater" is what makes the tier index one-based and correct |
| Unique triple constraint | no two employees share name, salary and department | tie groups stay distinguishable | Guarantees distinct output rows without extra deduplication |
| Department with no employees | a `Department` row with no matching employee | no output rows for it | Tiers come from `Employee`, so an empty department has no tiers |

## 9. Complexity Derivation

Let $E = \lvert \text{Employee} \rvert$, $D = \lvert \text{Department} \rvert$, and let $E_d$ be the number of employees in department $d$, so that $\sum_d E_d = E$.

**Time.** The windowed formulation orders the employee rows by department and descending salary, costing

$$
T_{\text{sort}}(E) = O(E \log E),
$$

then makes one streaming pass that assigns each row its tier index at $O(1)$ amortized per row, costing $O(E)$. The total is $O(E \log E)$, dominated by the ordering. The counting formulation instead probes the department for each employee; done naively that is

$$
T_{\text{naive}}(E) = \sum_{d} E_d^2 = O(E^2),
$$

acceptable only when departments are small, and $O(E \log E)$ when each department's salaries are sorted once and reused for all of its members. Either way $E \log E$ is the practical target, and the department relation contributes $O(D)$ for key lookups.

**Auxiliary space.** The windowed form keeps one partition's working order plus one rank attribute per employee, so

$$
S(E, D) = O(E) + O(D).
$$

The counting form needs only the sorted value set of the department currently being processed if it groups the scan, or one value set per department otherwise — $O(E)$ in the worst case, matching the windowed bound.