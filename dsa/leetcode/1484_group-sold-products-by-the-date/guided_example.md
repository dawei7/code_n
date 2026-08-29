# Guided Example: Group Sold Products By The Date

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Activities": [{"sell_date": "2020-05-30", "product": "Headphone"}, {"sell_date": "2020-06-01", "product": "Pencil"}, {"sell_date": "2020-06-02", "product": "Mask"}, {"sell_date": "2020-05-30", "product": "Basketball"}, {"sell_date": "2020-06-01", "product": "Bible"}, {"sell_date": "2020-06-02", "product": "Mask"}, {"sell_date": "2020-05-30", "product": "T-Shirt"}]}}`
- **Required output:** `{"columns": ["sell_date", "num_sold", "products"], "rows": [["2020-05-30", 3, "Basketball,Headphone,T-Shirt"], ["2020-06-01", 2, "Bible,Pencil"], ["2020-06-02", 1, "Mask"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table `Activities`:

The objective is to compute `{"columns": ["sell_date", "num_sold", "products"], "rows": [["2020-05-30", 3, "Basketball,Headphone,T-Shirt"], ["2020-06-01", 2, "Bible,Pencil"], ["2020-06-02", 1, "Mask"]]}` from `{"tables": {"Activities": [{"sell_date": "2020-05-30", "product": "Headphone"}, {"sell_date": "2020-06-01", "product": "Pencil"}, {"sell_date": "2020-06-02", "product": "Mask"}, {"sell_date": "2020-05-30", "product": "Basketball"}, {"sell_date": "2020-06-01", "product": "Bible"}, {"sell_date": "2020-06-02", "product": "Mask"}, {"sell_date": "2020-05-30", "product": "T-Shirt"}]}}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: What the query must summarize

The input contains one row for every recorded sale event. Several rows can have the same `sell_date`, and even the same product can appear more than once on one date because the table has no primary key. The result therefore cannot count rows directly. For each distinct date, it must report one output row containing the number of distinct product names and a comma-separated list containing those same distinct names. Finally, result rows must appear in ascending date order.

The stored SQL expresses that work as one grouped query:

1. `GROUP BY sell_date` partitions all input rows into groups. Every group contains exactly the rows whose dates are equal.
2. `COUNT(DISTINCT product)` counts the different product values in the current group and gives that number the output name `num_sold`.
3. `STRING_AGG(DISTINCT product, ',')` removes repeated product values and combines the remaining values with a comma between adjacent names.
4. `ORDER BY sell_date` sorts the completed output rows from the earliest date to the latest date.

It helps to separate two meanings that are easy to mix up. Grouping controls how many result rows exist: there is one row per distinct `sell_date`. The `DISTINCT` inside each aggregate controls which product values contribute within that row. For example, if one date has the input products `Mask`, `Mask`, and `Pencil`, that date still forms one group. The distinct count is two, and the concatenated set contains `Mask` and `Pencil` once each.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Activities": [{"sell_date": "2020-05-30", "product": "Headphone"}, {"sell_date": "2020-06-01", "product": "Pencil"}, {"sell_date": "2020-06-02", "product": "Mask"}, {"sell_date": "2020-05-30", "product": "Basketball"}, {"sell_date": "2020-06-01", "product": "Bible"}, {"sell_date": "2020-06-02", "product": "Mask"}, {"sell_date": "2020-05-30", "product": "T-Shirt"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the two aggregates agree

Both aggregate expressions operate on the same date group and both apply `DISTINCT` to the same `product` column. Consequently, `num_sold` describes the number of names represented by `products` rather than the number of source records. That parallel use of `DISTINCT` is essential. If the count omitted it, duplicated sales would make the number larger than the list. If the string aggregate omitted it, the list could contain repeated names while the count did not.

The separator argument `','` requests commas with no added spaces. A group containing the unique names `Bible` and `Pencil` is therefore represented as `Bible,Pencil`, not as `Bible, Pencil`. A group with one unique product simply produces that product name; no leading or trailing separator is needed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The ordering issue in the exact stored source

There are two independent ordering requirements. The outer `ORDER BY sell_date` handles the order of result rows, and the stored query satisfies that part. The product names inside each aggregated string also have to be lexicographically sorted. The exact stored expression is `STRING_AGG(DISTINCT product, ',')`, with no ordering clause inside the aggregate. Grouping and `DISTINCT` define membership, but they do not define the order in which an SQL engine feeds those members to `STRING_AGG`. An outer date sort cannot repair this because it rearranges whole result rows, not text inside `products`.

Therefore, the stored query reliably produces the correct groups, distinct counts, and distinct membership, but standard SQL semantics do not guarantee that its `products` string is lexicographically ordered. It may happen to look sorted for a particular execution plan or dataset, but that is not a correctness guarantee. In a PostgreSQL-style dialect, the intended deterministic expression would put an ordering term inside the aggregate, such as `STRING_AGG(DISTINCT product, ',' ORDER BY product)`. In a MySQL-style dialect, the corresponding facility is usually `GROUP_CONCAT` with an internal `ORDER BY`. This documentation does not silently attribute that missing behavior to the exact source.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["sell_date", "num_sold", "products"], "rows": [["2020-05-30", 3, "Basketball,Headphone,T-Shirt"], ["2020-06-01", 2, "Bible,Pencil"], ["2020-06-02", 1, "Mask"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Activities": [{"sell_date": "2020-05-30", "product": "Headphone"}, {"sell_date": "2020-06-01", "product": "Pencil"}, {"sell_date": "2020-06-02", "product": "Mask"}, {"sell_date": "2020-05-30", "product": "Basketball"}, {"sell_date": "2020-06-01", "product": "Bible"}, {"sell_date": "2020-06-02", "product": "Mask"}, {"sell_date": "2020-05-30", "product": "T-Shirt"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["sell_date", "num_sold", "products"], "rows": [["2020-05-30", 3, "Basketball,Headphone,T-Shirt"], ["2020-06-01", 2, "Bible,Pencil"], ["2020-06-02", 1, "Mask"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Ordered string aggregation:** Put `ORDER BY product` inside the string aggregate. This is the direct repair because it preserves the one-pass grouped structure while making the required lexicographic order explicit and deterministic.
- **Deduplicating subquery:** First select distinct `sell_date` and `product` pairs, then group that smaller relation. This makes the logical stages very visible, although the database may already perform equivalent work for the two distinct aggregates.
- **Window functions:** Windowed counts can annotate rows, but an additional distinct-and-collapse stage is still needed to return one row per date. They add complexity without improving this grouped result.
- **Application-side grouping:** Fetching all rows and grouping them in application code can implement the rules, but it moves data unnecessarily and gives up the database engine's aggregation strengths.
- **Duplicate source rows:** Repeated copies of the same date-product pair must affect neither `num_sold` nor the product list. The two `DISTINCT` modifiers handle this correctly.
- **One product on a date:** The count is one and the aggregate string is just that name, with no comma.
- **Several dates with the same products:** Dates are independent groups. The same name can validly appear in several result rows.
- **Lexicographic case behavior:** The exact ordering of uppercase, lowercase, and accented text depends on the database collation. An internal `ORDER BY product` follows that configured collation unless a specific collation is requested.
- **Null products:** The reference describes product names as sale data but does not state null behavior. Standard count and string aggregates commonly ignore nulls; if nulls were permitted and needed special treatment, the contract would have to specify it.
- **Outer versus inner order:** `ORDER BY sell_date` sorts rows only. It never guarantees the ordering of product names within an aggregated string.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(P)$. Let $R$ be the number of rows in `Activities` and let $P$ be the total number of distinct date-product pairs. Also let $D$ be the number of distinct dates. Any execution must at least inspect the relevant input rows, which contributes $O(R)$ work.
- **Auxiliary Space Complexity:** $O(P)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
