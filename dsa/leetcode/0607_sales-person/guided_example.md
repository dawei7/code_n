# Guided Example: Sales Person

Three relations cooperate here. `SalesPerson` is the roster, keyed by `sales_id`; `Company` is the client directory, keyed by `com_id`; and `Orders` is the transaction ledger, keyed by `order_id`, with `com_id` referencing `Company` and `sales_id` referencing `SalesPerson`. The question asks for the names of salespeople who *did not have any orders related to the company named* `"RED"`.

That phrasing is a negative requirement, and negative requirements invite the wrong tool. The instance below is the official ledger, and it is an unusually good teacher because it contains all four seller profiles at once: a pure RED seller, a mixed seller who also sold elsewhere, a seller with a non-RED order only, and two sellers with no orders at all.

## 1. Instance, Contract, and the Complement Question

The roster:

| `sales_id` | `name` | `salary` | `commission_rate` | `hire_date` |
|:---:|:---|:---:|:---:|:---|
| $1$ | `John` | $100000$ | $6$ | `4/1/2006` |
| $2$ | `Amy` | $12000$ | $5$ | `5/1/2010` |
| $3$ | `Mark` | $65000$ | $12$ | `12/25/2008` |
| $4$ | `Pam` | $25000$ | $25$ | `1/1/2005` |
| $5$ | `Alex` | $5000$ | $10$ | `2/3/2007` |

The client directory:

| `com_id` | `name` | `city` |
|:---:|:---|:---|
| $1$ | `RED` | `Boston` |
| $2$ | `ORANGE` | `New York` |
| $3$ | `YELLOW` | `Boston` |
| $4$ | `GREEN` | `Austin` |

The ledger:

| `order_id` | `order_date` | `com_id` | `sales_id` | `amount` |
|:---:|:---|:---:|:---:|:---:|
| $1$ | `1/1/2014` | $3$ | $4$ | $10000$ |
| $2$ | `2/1/2014` | $4$ | $5$ | $5000$ |
| $3$ | `3/1/2014` | $1$ | $1$ | $50000$ |
| $4$ | `4/1/2014` | $1$ | $4$ | $25000$ |

The required output, in any order:

| `name` | Profile |
|:---|:---|
| `Amy` | No orders at all |
| `Mark` | No orders at all |
| `Alex` | One order, with `GREEN` — never with `RED` |

### What the contract fixes

- **Input space.** The three relations above, with `com_id` and `sales_id` acting as foreign keys from `Orders` into the directory and the roster.
- **Output space.** A single column `name`, restricted to the sellers that never appear in a `RED`-company order.
- **Order.** Any order is acceptable, so no ranking or determinism requirement attaches to the result.
- **Negative semantics.** The requirement is about *absence*. A seller must be judged on the company attached to their orders, not on whether they have orders at all.

## 2. Building the RED-Tainted Seller Set

The negative requirement is easiest to handle by computing its complement first. Attach each order to its company, keep the orders whose company is `RED`, and project the seller:

$$
S_{\text{RED}} \;=\; \bigl\{\, o.\text{sales\_id} \;\bigm|\; o \in \text{Orders},\; c \in \text{Company},\; o.\text{com\_id} = c.\text{com\_id},\; c.\text{name} = \text{"RED"} \,\bigr\}.
$$

This is a join on the shared key `com_id` followed by a selection and a projection. The join is what makes the set meaningful: `Orders` alone knows only `com_id` values, so without consulting `Company` there is no way to know which client is called `RED`.

The exclusion set is a *set of identifiers*, not a set of orders. That distinction is essential: a seller with four separate `RED` orders contributes one element to $S_{\text{RED}}$, and the size of the set is bounded by the number of sellers, never by the number of orders.

## 3. Complement Invariant and the Null Trap

Let $s$ range over the roster. The seller $s$ qualifies exactly when their order set intersects the RED order set in nothing:

$$
s \notin S_{\text{RED}}
\;\Longleftrightarrow\;
\{\, o \in \text{Orders} \;\mid\; o.\text{sales\_id} = s \,\} \;\cap\; \{\, o \in \text{Orders} \;\mid\; \text{company}(o) = \text{"RED"} \,\} \;=\; \emptyset .
$$

> **Complement invariant.** "Never sold to RED" is the set difference $\text{SalesPerson} \setminus S_{\text{RED}}$. A seller with an empty order history has an empty intersection with the RED order set, so the difference retains them automatically — no special case is needed.

That automatic retention is the pedagogical heart of the problem. Because the criterion is emptiness of an intersection, the *absence* of orders satisfies it. Any formulation that requires an order to exist before judging it will violate the invariant.

> **Null-safety caveat.** Complement membership is tested with three-valued logic. If the exclusion set could contain a null identifier, an equality test against it evaluates to *unknown* rather than *true*, and a negated test built on it would reject every row. The set in this instance is projected from the seller column of joined orders, so it holds real identifiers; but the caveat matters whenever the exclusion set is built from a nullable source.

## 4. Worked Evaluation of the Official Sales Ledger

**Step 1 — Attach each order to its company.**

| `order_id` | `com_id` | Company `name` | `sales_id` | Seller | Company is `RED`? |
|:---:|:---:|:---|:---:|:---|:---:|
| $1$ | $3$ | `YELLOW` | $4$ | `Pam` | No |
| $2$ | $4$ | `GREEN` | $5$ | `Alex` | No |
| $3$ | $1$ | `RED` | $1$ | `John` | Yes |
| $4$ | $1$ | `RED` | $4$ | `Pam` | Yes |

**Step 2 — Keep the RED rows and project the seller.** Rows $3$ and $4$ survive the selection, giving

$$
S_{\text{RED}} = \{1,\; 4\},
$$

the identifiers of `John` and `Pam`. Note that `Pam` enters the set through a single order even though she also appears in row $1$ for `YELLOW`; the set records that she sold to `RED` at least once.

**Step 3 — Take the complement against the full roster and project names.**

| `sales_id` | `name` | Orders in the ledger | In $S_{\text{RED}}$? | Verdict |
|:---:|:---|:---|:---:|:---|
| $1$ | `John` | order $3$ (`RED`) | Yes | Excluded |
| $2$ | `Amy` | none | No | **Included** |
| $3$ | `Mark` | none | No | **Included** |
| $4$ | `Pam` | orders $1$ (`YELLOW`) and $4$ (`RED`) | Yes | Excluded |
| $5$ | `Alex` | order $2$ (`GREEN`) | No | **Included** |

Every seller was examined, including the two who never appear in the ledger. The result is `Amy`, `Mark`, and `Alex`, and the answer does not depend on which order the scan happened to visit first.

## 5. Retaining Sellers With No Orders

The two included sellers with empty order histories are not a curiosity; they are the reason the naive formulation fails. The next table contrasts the three ways a seller can relate to `RED`.

| Seller profile | Any order with `RED`? | Intersection with RED orders | Verdict | Example here |
|:---|:---:|:---|:---|:---|
| Pure RED seller | Yes | Non-empty | Excluded | `John` |
| Mixed seller: some RED, some other | Yes | Non-empty | Excluded | `Pam` |
| Non-RED seller | No | Empty | Included | `Alex` |
| Seller with no orders | No — vacuously | Empty | Included | `Amy`, `Mark` |

The last two rows are why the criterion is emptiness of an intersection rather than the existence of a "clean" order. A seller either has a RED order or they do not; having *other* orders is irrelevant in both directions. `Pam` cannot be rescued by her `YELLOW` order, and `Alex` needs no protection from his `GREEN` order.

## 6. Elimination of Tempting Alternatives

| Alternative | Why it attracts | Why it fails or costs more |
|:---|:---|:---|
| Join the roster to the ledger and keep rows whose company is not `RED` | One join and one inequality, no subquery | Drops sellers with no orders entirely, and — worse — matches `Pam`'s `YELLOW` order and wrongly includes her |
| Require an order to exist before the RED test | Feels necessary to "check" the seller | Violates the complement invariant: the absent intersection is exactly what qualifies a seller with no orders |
| Negate membership against a nullable exclusion set | Natural once the set is built from a nullable column | Three-valued logic makes the negated test unknown for every row, so the result is silently empty |
| Group the left-joined ledger and keep groups with zero RED orders | Correct, and a single pass | Requires an outer join plus a grouped aggregation, and forces a careful treatment of the null company produced for orderless sellers |
| Build the complement with a correlated existence test | Reads directly as "no RED order exists for this seller" | Correct and equivalent in cost; the correlated form is simply a different spelling of the same set difference |
| Set difference over the projected seller identifiers | Closest to the mathematical statement | Correct only if the intermediate projections are de-duplicated; without that, a seller with several RED orders appears multiple times in the intermediate relation |

The first row is the trap this instance is built to expose, and `Pam` is the proof: she has a qualifying non-RED order, so any rule that tests orders one at a time will misclassify her.

## 7. Cost of the Method

Let $S$, $C$, and $O$ be the row counts of `SalesPerson`, `Company`, and `Orders`, and let $K = \lvert S_{\text{RED}} \rvert \le S$ be the size of the exclusion set.

**Time complexity.** Locating the client named `RED` is a single filtered scan of `Company`, at $O(C)$; with an index on the company name it is faster, but the linear bound is the safe one. Pairing the ledger to the directory on `com_id` is a hash join costing $O(C + O)$ expected, and the selection and projection add nothing beyond a constant per joined row. Building the exclusion set as a hash set is $O(O)$ in the worst case. The final complement test probes the set once per roster row, at $O(S)$ expected. Total:

$$
O(C) + O(C + O) + O(O) + O(S) \;=\; O(S + O + C).
$$

Notice that the cost does not depend on how many orders a single seller has, because the exclusion set stores identifiers rather than orders. It also does not depend on the number of RED orders: a seller with a thousand RED orders is stored once.

**Auxiliary-space complexity.** The intermediate joined relation, if materialized, holds one row per ledger row, so $O(O)$; a streaming hash join needs only the build-side table, $O(\min(C, O))$. The exclusion set holds at most one identifier per seller that ever sold to `RED`, so $O(K) \le O(S)$. The output itself is $O(S)$ in the worst case, when no seller ever sold to `RED`. The binding term is therefore $O(O + S)$ whenever the join is materialized, and $O(S)$ of state beyond the output when it is streamed.
