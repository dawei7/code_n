# Guided Example: Customer Placing the Largest Number of Orders

We trace one aggregation whose result is a single scalar drawn from a ranking. The
instance is chosen because it exposes the difference between a *count* and the
*identity of the thing that was counted*: one customer wins with two orders while
the remaining two customers are tied at one, so the answer is decided by a strict
margin but the ordering of everything below the winner is not.

- **Input relation** `Orders`, keyed by `order_number`:

    | `order_number` | `customer_number` |
    |:---:|:---:|
    | $1$ | $1$ |
    | $2$ | $2$ |
    | $3$ | $3$ |
    | $4$ | $3$ |

- **Required output** — the identifier of the customer with the most orders:

    | `customer_number` |
    |:---:|
    | $3$ |

The contract adds a guarantee that makes the answer unique: the test data are
generated so that **exactly one** customer has placed more orders than any other
customer. This instance realises that guarantee with a margin of exactly one
order, which is the tightest margin the guarantee permits.

---

## 1. Instance & Teaching Goal

Report the `customer_number` of the customer who has placed the largest number of
orders. The contract is guaranteed to admit a unique winner, so the result is a
single row containing a single identifier.

The lesson is the two-step nature of the problem. The count of orders is
computed *per customer*, which requires grouping; the selection of the winner is
then a *maximum over the group sizes*, which requires a ranking. A method that
performs only the first step has a table of counts and no answer, and a method
that performs only the second has nothing to rank.

### Counting and identifying are different columns

It is essential to keep the grouping key and the aggregate separate:

| Quantity | Meaning | Value for customer $1$ | Value for customer $2$ | Value for customer $3$ | Role in the answer |
|:---|:---|:---:|:---:|:---:|:---|
| `customer_number` | the group identity | $1$ | $2$ | $3$ | what must be returned |
| group size | number of orders in the group | $1$ | $1$ | $2$ | what must be compared |
| `order_number` values | the members of the group | $1$ | $2$ | $3, 4$ | witness that the count is right |

The returned value is a label, not a quantity. A method that ranks correctly but
projects the group size returns $2$ instead of $3$ — a plausible-looking number
that fails the schema.

---

## 2. The Grouping and Ranking Invariant

Let $G_k = \{\, o \in \texttt{Orders} : o.\texttt{customer\_number} = k \,\}$ be
the set of orders belonging to customer $k$, and let $n_k = \lvert G_k \rvert$ be
that customer's order count.

> **Partition-and-rank invariant.** Grouping by `customer_number` partitions
> `Orders` into disjoint sets, one per distinct customer, so
> $\sum_k n_k = N$ where $N = \lvert \texttt{Orders} \rvert$. The maximum order
> count is therefore $\max_k n_k$, and the winner is the unique $k^\star$ with
> $n_{k^\star} = \max_k n_k$.

Three properties of this invariant drive the whole method.

1. **The partition is exhaustive and disjoint.** Every order belongs to exactly
   one customer, so every order is counted once and no order is counted twice.
   This is why the sum of the group sizes recovers the input size exactly.
2. **The comparison is over group sizes, not over the rows.** The ranking must be
   applied after aggregation; comparing raw `order_number` values would compare
   transaction identifiers, which carry no information about volume.
3. **The maximiser is unique by contract.** Because exactly one customer attains
   the maximum, the ranking is a total order at its head and any tie-breaking
   policy is vacuous. Without that guarantee the answer would be a *set* of
   customers, and the method would have to change.

### Why the maximum must be a strict maximum here

The instance has two customers tied at one order each. That tie is below the
winner, so it does not threaten the answer — but it does illustrate the
boundary. If the guarantee were removed and two customers both had two orders,
then selecting the first row of a count-ordered list would return an arbitrary
one of them, and the choice could depend on scan order. Under the stated
guarantee, no such ambiguity exists:

| Distribution of order counts | Unique maximiser? | Correct output shape |
|:---|:---:|:---|
| $(2, 1, 1)$ — this instance | Yes, customer $3$ | one row |
| $(3, 1, 1, 1)$ | Yes, the customer with $3$ | one row |
| $(2, 2, 1)$ | No | every customer attaining the maximum |
| $(1)$ | Yes, the sole customer | one row |

### Relational formulation

Two stages suffice. The first groups the order relation by the customer
identifier and computes, per group, the number of member rows — a cardinality
aggregate over the grouping key. The second orders those aggregated groups by
their cardinality from greatest to least and retains only the leading group,
projecting the customer identifier and discarding the count. In prose: *partition
by customer, count rows per partition, take the argmax*. The concrete spelling of
the aggregation and the truncation belongs to the Reference workflow.

An equivalent single-pass formulation tracks, for each customer, a running count
in a map and remembers the best-so-far key. That view makes the linear-time
character of the computation explicit, since it never materialises the sorted
list of groups.

---

## 3. Step-by-Step Worked Execution

### Step 1 — Partition the orders by customer

| Scan order | `order_number` | `customer_number` | Destination group |
|:---:|:---:|:---:|:---|
| $1$ | $1$ | $1$ | $G_1$ |
| $2$ | $2$ | $2$ | $G_2$ |
| $3$ | $3$ | $3$ | $G_3$ |
| $4$ | $4$ | $3$ | $G_3$ |

After the scan the partition is

$$
G_1 = \{1\}, \qquad G_2 = \{2\}, \qquad G_3 = \{3, 4\}.
$$

### Step 2 — Compute the cardinality of each group

| Customer $k$ | Group $G_k$ | $\lvert G_k \rvert = n_k$ |
|:---:|:---|:---:|
| $1$ | $\{1\}$ | $1$ |
| $2$ | $\{2\}$ | $1$ |
| $3$ | $\{3, 4\}$ | $2$ |

The counts sum to $1 + 1 + 2 = 4 = N$, confirming that the partition accounts for
every order exactly once.

### Step 3 — Rank the groups by cardinality, descending

| Rank | Customer $k$ | $n_k$ | Retained? |
|:---:|:---:|:---:|:---|
| $1$ | $3$ | $2$ | Yes — the maximiser |
| $2$ | $1$ | $1$ | No — truncated |
| $3$ | $2$ | $1$ | No — truncated |

Customers $1$ and $2$ are tied; the secondary order between them is immaterial
because the truncation keeps only rank $1$, and the guarantee ensures rank $1$ is
not shared.

### Step 4 — Project the group identity

The leading group's identity is customer $3$, and the count $2$ is working state
rather than output:

| `customer_number` |
|:---:|
| $3$ |

---

## 4. Why the Reasoning Is Correct

**Every customer's count is exact.** Grouping compares `customer_number` by
equality, so two orders fall in the same group precisely when their customer
identifiers are equal. Each group therefore contains exactly the orders placed by
one customer, and its cardinality is that customer's order volume. The partition
is disjoint, so no order contributes to two groups, and exhaustive, so no order
is left uncounted.

**The ranked head is the maximum.** Ordering the groups by cardinality from
greatest to least places a group with the largest count first. If several groups
shared the largest count, they would occupy adjacent leading positions, and the
guarantee that the maximiser is unique makes the leading position unambiguous.

**The projected value is the winner's identifier.** The retained group is the one
belonging to the maximiser, and its grouping key is the winning
`customer_number`. Projecting the key rather than the cardinality yields the
required identifier; this is the step where a correct ranking can still produce a
wrong answer if the wrong column is projected.

**The method does not depend on order of appearance.** The count of a group is a
set cardinality, invariant under permutation of the input rows, and the ranking
compares counts rather than positions. A winner that appears only in the final
row of the relation is found exactly as quickly, which matters because the
generator may place the winner anywhere.

**Ties below the winner are harmless.** The instance contains a genuine tie at
one order. Because the truncation keeps only the leading position and the
maximiser is strictly ahead, the tie never reaches the output. Under the stated
guarantee this is sound; without it, a single-row output would be unjustified.

---

## 5. Boundary and Degenerate Cases

| Instance | Group cardinalities | Output | Teaching point |
|:---|:---|:---|:---|
| Single order in the relation | $(1)$ | the only `customer_number` | Aggregation over one group is still aggregation; the ranking is vacuous |
| Several customers, all with one order each | all $1$ | ill-defined under a single-row contract | The guarantee forbids this input; the method relies on it |
| One customer with $2$ orders, all others with $1$ | $(2, 1, \dots, 1)$ | the customer with $2$ | The guarantee is satisfied with the smallest possible margin |
| One dominant customer ahead by many orders | $(m, 1, \dots, 1)$ | the dominant customer | Margin size is irrelevant to correctness |
| Customer identifiers sparse, e.g. `2`, `40`, `100` | unchanged | the largest-count key, whatever its numeric size | Keys are labels; magnitude carries no meaning and creates no bias |
| Winner placed last in the relation | unchanged | the winner | Counting is order-insensitive |
| A tie for the maximum | two or more equal maxima | contract violated | The correct general method must return all tied customers |

The follow-up question in the source asks exactly about the last row: what if more
than one customer has the largest number of orders. The answer is that the
truncation step must be replaced by a comparison against the computed maximum —
retain every group whose cardinality equals $\max_k n_k$. That change turns a
top-one selection into a selection by value and makes the output cardinality
data-dependent.

---

## 6. Traps This Instance Exposes

- **Projecting the count instead of the customer:** Ranking correctly and then
  returning the group size yields $2$, not $3$. The schema requires an
  identifier.
- **Ordering ascending:** Ranking by cardinality from least to greatest puts the
  winner last and, after a single-row truncation, returns a customer with one
  order.
- **Ranking raw rows instead of groups:** Comparing `order_number` values
  compares transaction identifiers, not volumes, and would be right on this
  instance only by coincidence.
- **Grouping by the wrong column:** Grouping by `order_number` makes every group
  a singleton, so every customer appears to have one order and the winner cannot
  be found at all.
- **Computing the maximum in a nested aggregate:** Deriving the maximum count in
  one pass and then filtering the groups in a second is correct but easy to write
  in a way that rescans the relation per group, degrading a linear aggregation
  into quadratic work on large inputs.
- **Relying on `LIMIT 1` without a deterministic order:** Truncation without a
  ranking keeps an arbitrary group, so the answer would depend on plan choice
  rather than on the data.
- **Assuming the winner is the numerically largest identifier:** Customer $3$
  wins here while customer $2$ does not; identifier magnitude is unrelated to
  order volume.
- **Distinct-counting the orders:** Every order number is unique because it is the
  primary key, so counting distinct values of either column gives the wrong
  quantity — the requirement is the number of order rows per customer.

---

## 7. Complexity Derivation

Let $N = \lvert \texttt{Orders} \rvert$ and let $K$ be the number of distinct
`customer_number` values, so $K \le N$.

**Aggregation.** A hash-based grouping maintains one counter per distinct
customer and updates it once per order row, so it costs expected $\Theta(N)$ and
never inspects any customer twice. A comparison-sort-based grouping instead
orders the relation by the grouping key and then collapses runs, costing
$\Theta(N \log N)$.

**Ranking and truncation.** The aggregated relation has $K$ rows. A full
comparison sort of those $K$ rows costs $\Theta(K \log K)$. Because only the
leading row survives, a top-one selection needs no full sort: a single scan that
tracks the best count seen so far costs $\Theta(K)$ and uses $\Theta(1)$ extra
state.

**Total.** With hash aggregation and a top-one scan,

$$
T(N, K) \;=\; \underbrace{\Theta(N)}_{\text{group and count}} \;+\;
\underbrace{\Theta(K)}_{\text{top-one scan}} \;=\; \Theta(N + K) \;=\; \Theta(N),
$$

since $K \le N$. If the engine sorts both stages, the bound rises to

$$
T(N, K) = \Theta(N \log N + K \log K) = \Theta(N \log N),
$$

which is the conservative bound quoted for the relational formulation because
window and ordering operators are typically sort-based. Either way the growth is
at most quasi-linear in the input size, and there is no inner scan over groups:
the method never compares a group against every other group, so it never reaches
$\Theta(N^2)$.

On the worked instance $N = 4$ and $K = 3$: four counter updates, three group
comparisons for the maximum.

**Auxiliary space.** The grouping keeps one accumulator per distinct customer, so
the map holds $K$ entries. A full sort of the groups buffers $K$ rows, whereas
the top-one scan keeps only the current best pair:

$$
M(N, K) \;=\; \Theta(K) \le \Theta(N) \quad \text{(map)}, \qquad
M = \Theta(1) \quad \text{(beyond the map, top-one scan)} .
$$

The output is a single row, so it contributes constant space and does not affect
the bound.
