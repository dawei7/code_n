# Guided Example: Customers Who Never Order

We trace a relational anti-join on a four-customer registration table and a two-order ledger, then compare the three standard formulations that express "present in one relation, absent from another" and pin down the exact place where the third of them breaks.

- **Representative relations:** `Customers` = `(1, "Joe")`, `(2, "Henry")`, `(3, "Sam")`, `(4, "Max")`; `Orders` = `(1, 3)`, `(2, 1)`.
- **Required result:** a single-column relation named `Customers` containing `"Henry"` and `"Max"`.
- **Contrasting instances used later:** a ledger covering every customer, which must return no rows, and an empty ledger, which must return all four names.

## 1. Instance and Required Outcome

`Customers(id, name)` holds one row per registered customer, with `id` as the primary key (a column of unique values). `Orders(id, customerId)` holds one row per order, with `id` as its primary key and `customerId` a foreign key referencing `Customers.id`.

| `Customers.id` | `Customers.name` |
|:---:|:---|
| 1 | `"Joe"` |
| 2 | `"Henry"` |
| 3 | `"Sam"` |
| 4 | `"Max"` |

| `Orders.id` | `Orders.customerId` |
|:---:|:---:|
| 1 | 3 |
| 2 | 1 |

The task is to report the name of every customer with no matching order row. Note which relation supplies the *universe of rows to report*: `Customers`, not `Orders`. A customer who ordered twice still produces one output row if reported at all, and a customer who never ordered must not be dropped merely because the right-hand relation has nothing to contribute. The output header must be `Customers`, which differs from the source attribute name `name`.

## 2. The Anti-Join as a Complement of a Semi-Join

Write $C$ and $O$ for the two relations. The natural join on the shared key, projected back onto the customers that do participate, is the *semi-join*

$$
C \ltimes O = \pi_{\text{attrs}(C)}\!\left(C \bowtie_{C.\text{id} = O.\text{customerId}} O\right),
$$

the set of customer tuples that have at least one partner. Selecting the customers who never ordered is then exactly the set difference

$$
C \;\bar{\ltimes}\; O = C \setminus \left(C \ltimes O\right).
$$

This definition is the whole specification. The answer is drawn from $C$, so its cardinality is at most $\lvert C \rvert$ however many orders exist. And membership in $C \ltimes O$ is a *boolean* property of a customer, so the number of orders behind a customer is irrelevant to the complement.

An equivalent way to say the same thing uses a count of partners. For a customer $c$, let

$$
m(c) = \lvert \{\, o \in O \mid o.\text{customerId} = c.\text{id} \,\} \rvert .
$$

Then $c \in C \ltimes O$ if and only if $m(c) \ge 1$, so $c \in C \,\bar{\ltimes}\, O$ if and only if $m(c) = 0$.

> **Invariant.** A customer tuple $c$ is emitted if and only if the partner set $\{\, o \in \text{Orders} \mid o.\text{customerId} = c.\text{id} \,\}$ is empty, and each such customer is emitted exactly once regardless of $m(c)$.

## 3. Presence Testing: Building and Probing the Order Key Set

Before any customer can be classified, the engine must be able to answer "does an order exist for this customer?" quickly. A hash set built from the right-hand key column answers that in expected constant time per probe.

| Step | Operation | Resulting key set / state |
|:---:|:---|:---|
| 0 | Start with an empty probe structure | $\{\}$ |
| 1 | Insert `Orders.customerId` = 3 | $\{3\}$ |
| 2 | Insert `Orders.customerId` = 1 | $\{1, 3\}$ |
| 3 | Probe each `Customers.id` against the finished set | probes for 1, 2, 3, 4 |

The construction is complete only after both order rows are read, which is why the classification of a customer cannot be decided while the ledger is still being scanned. The probe results are what the complement test consumes:

| `Customers.id` | Probe against $\{1, 3\}$ | Membership $m(c) \ge 1$ | Complement condition $m(c) = 0$ |
|:---:|:---:|:---:|:---:|
| 1 | present | true | false |
| 2 | absent | false | **true** |
| 3 | present | true | false |
| 4 | absent | false | **true** |

## 4. Worked Trace of the Retaining Outer Join

The reference formulation keeps every left tuple and pads the right-hand attributes with an unknown marker when no partner exists. Walking the customers in key order shows exactly how the padding arises and how the filter isolates it.

| Customer tuple | Probe for `customerId = id` | Paired order tuple | Right-hand attributes after pairing | Retained by the unknown test |
|:---|:---|:---|:---|:---:|
| `(1, "Joe")` | order `(2, 1)` found | `(2, 1)` | `Orders.id` = 2, `Orders.customerId` = 1 | no — paired, so the right side is known |
| `(2, "Henry")` | no order references 2 | none | `Orders.id` = unknown, `Orders.customerId` = unknown | **yes** |
| `(3, "Sam")` | order `(1, 3)` found | `(1, 3)` | `Orders.id` = 1, `Orders.customerId` = 3 | no — paired |
| `(4, "Max")` | no order references 4 | none | `Orders.id` = unknown, `Orders.customerId` = unknown | **yes** |

The reason the unknown test is sound depends on a fact stated in the contract: `Orders.id` is a primary key, so it is guaranteed present in every genuine order tuple. A padded row is therefore the only way an unknown value can appear in the right-hand `id` attribute, and the test "the right-hand key is unknown" is exactly the test "no partner was found". Projecting `Customers.name` under the header `Customers` yields:

| `Customers` |
|:---|
| `"Henry"` |
| `"Max"` |

The retaining join pairs each left tuple only with matching right tuples, so a customer with three orders contributes three paired rows here and fails the unknown test every time. The complement formulation below avoids that multiplier.

## 5. Three Equivalent Formulations and Their Failure Modes

| Formulation | How absence is detected | Work per customer | Failure mode to know |
|:---|:---|:---|:---|
| Retaining outer join, then an unknown test on a right-hand key | Unmatched left tuples are padded, and the padded key is the sentinel for "no partner" | One probe, one row emitted | Needs a key column guaranteed present in real right-hand rows; testing a nullable attribute that can legitimately be unknown would misclassify paired rows |
| Correlated existence test | A search of the right relation is requested per customer, and the result is negated | One probe, with early exit at the first partner found | Correct in all cases, but re-executing it per customer repeats index traversal; a semi-join plan removes the repetition |
| Complement membership test against the projected right-hand key set | The customer key is tested for absence from the set of ordering customer keys | One set probe, $O(1)$ expected | Three-valued logic: if the projected set contains even one unknown value, every absence test becomes unknown rather than true and the answer silently collapses to the empty relation |

The third formulation hides the sharpest trap. Under SQL's three-valued logic a comparison against an unknown value is neither true nor false but *unknown*, and a row filter keeps a row only when its condition is definitely true. If `Orders.customerId` were ever unknown, the projected set would resemble $\{1, 3, \text{unknown}\}$; every absence test would then evaluate to unknown and the answer would collapse to the empty relation, even for customers that plainly never ordered. The foreign-key contract keeps the column known, so the hazard is latent rather than active — but the other two formulations are preferred because they do not rely on that guarantee.

## 6. Why Exactly the Order-Free Customers Are Emitted

**Soundness.** Suppose a customer name is emitted. The tuple it came from survived a test that is true only when no order row carries its `id` as `customerId`, established by primary-key non-nullness in the outer-join formulation or by a direct existence probe in the other two. Hence $m(c) = 0$.

**Completeness.** The retaining outer join emits every tuple of the left relation at least once, so no customer is discarded before the test is applied; only the paired ones are removed, and paired means $m(c) \ge 1$. Every customer with $m(c) = 0$ therefore reaches the projection.

**No spurious duplication.** A left tuple with no partner is padded exactly once, so a never-ordering customer contributes exactly one output row. Right-hand multiplicity only affects customers that the filter then removes, which is why the answer's cardinality is bounded by $\lvert C \rvert$ rather than by $\lvert O \rvert$. Every condition also compares a fixed customer key against a fixed set of order keys, so the result is a set and any presentation order is acceptable.

## 7. Boundary Instances and Logic Traps

| Instance | Input shape | Expected result | Why it matters |
|:---|:---|:---|:---|
| Everyone ordered | `Orders.customerId` covers 1, 2, 3, 4 | empty relation | The complement of a semi-join is empty exactly when the semi-join is the whole left relation |
| Nobody ordered | `Orders` is empty | all four names | An empty right relation must not eliminate the left universe; an inner join would wrongly return nothing |
| One customer with many orders | customer 1 has five orders | customer 1 still absent from the result | Absence is decided by the boolean $m(c) \ge 1$, not by any count of rows |
| Order for an unknown customer | `Orders.customerId` = 99 with no such customer | unchanged result | The join direction is anchored on `Customers`; an orphan right-hand tuple can never create an output row |
| Right-hand key can be unknown | `customerId` unknown in some order | risks an empty result under the complement formulation | Presence of a single unknown in the projected key set turns every absence test into unknown |
| Repeated customer names | two customers share a name | both names reported when both never ordered | Output identity is the customer row, not the string; the two rows are distinct primary keys |

The fourth row is the join-direction trap, and the fifth separates a robust formulation from a fragile one.

## 8. Complexity Derivation

Let $C = \lvert \text{Customers} \rvert$ and $O = \lvert \text{Orders} \rvert$, and let $K \le O$ be the number of distinct ordering customer keys.

**Time.** Building the probe structure from the order keys costs

$$
T_{\text{build}} = O(O)
$$

with one insertion per order row. Classifying customers costs one expected-constant probe each, giving

$$
T_{\text{probe}} = O(C),
$$

and the projection costs at most $O(C)$ because at most one row per customer is produced. The expected total is

$$
T(C, O) = O(C) + O(O) = O(C + O),
$$

which is linear in the combined input size and therefore optimal up to the cost of reading the input. Without a hash structure the probes degrade: $O(C \log O)$ if each is a binary search over sorted order keys, $O(C \cdot O)$ if each performs a full ledger scan — the correlated formulation's naive cost.

**Auxiliary space.** The probe structure stores one entry per distinct ordering key, and the result buffer holds at most one row per customer, so

$$
S(C, O) = O(K) + O(C) = O(C + O).
$$
