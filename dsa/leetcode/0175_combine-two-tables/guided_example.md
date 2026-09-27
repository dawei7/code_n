# Guided Example: Combine Two Tables

We trace the step-by-step relational evaluation of a SQL Left Outer Join preserving all records from the primary relation on representative relational tables:

- **Input Tables:**
  - `Person`: `[(1, "Wang", "Allen"), (2, "Alice", "Bob")]`
  - `Address`: `[(1, 2, "New York City", "New York"), (2, 3, "Leetcode", "California")]`
- **Required output:**
  - `[["Allen", "Wang", null, null], ["Bob", "Alice", "New York City", "New York"]]`

This instance demonstrates relational algebra outer joins, explains why an `INNER JOIN` fails by silently discarding persons without registered addresses, models the tuple matching and `NULL` generation for unmatched left rows, and executes in $O(P + A)$ linear time.

---

## 1. Instance & Teaching Goal

Given two relational tables:
1. `Person` table with primary key `personId`:
   $$
   \begin{array}{|c|c|c|}
   \hline
   \textbf{personId} & \textbf{lastName} & \textbf{firstName} \\
   \hline
   1 & \text{Wang} & \text{Allen} \\
   2 & \text{Alice} & \text{Bob} \\
   \hline
   \end{array}
   $$
2. `Address` table with foreign key `personId`:
   $$
   \begin{array}{|c|c|c|c|}
   \hline
   \textbf{addressId} & \textbf{personId} & \textbf{city} & \textbf{state} \\
   \hline
   1 & 2 & \text{New York City} & \text{New York} \\
   2 & 3 & \text{Leetcode} & \text{California} \\
   \hline
   \end{array}
   $$
Report the `firstName`, `lastName`, `city`, and `state` for **each person** in the `Person` table. If the address of a person is not present, report `null` for `city` and `state`.

### Why an Inner Join Fails
An `INNER JOIN` evaluates the conjunction $P.\text{personId} = A.\text{personId}$.
Because person $1$ (`"Allen Wang"`) does not appear in `Address`, the join predicate evaluates to false, completely dropping Allen from the result set!
A `LEFT JOIN` (Left Outer Join) preserves **all** rows from the left table (`Person`), regardless of whether a matching record exists in the right table (`Address`).

---

## 2. Conceptual Foundation & Invariants

### Relational Left Outer Join Semantics
The relational algebra expression:
$$
\text{Result} = \pi_{\text{firstName}, \text{lastName}, \text{city}, \text{state}} \left( \text{Person} \mathbin{\text{LEFT JOIN}}_{P.\text{personId} = A.\text{personId}} \text{Address} \right)
$$

For every tuple $p \in \text{Person}$:
1. Search for matching tuples in $\text{Address}$ where $A.\text{personId} = p.\text{personId}$.
2. **Case A: Match Found ($p.\text{personId} \in \text{Address}$):**
   Emit joined tuple:
   $$
   (p.\text{firstName}, \, p.\text{lastName}, \, a.\text{city}, \, a.\text{state})
   $$
3. **Case B: No Match ($p.\text{personId} \notin \text{Address}$):**
   Emit tuple padded with `NULL`s for all columns from $\text{Address}$:
   $$
   (p.\text{firstName}, \, p.\text{lastName}, \, \text{NULL}, \, \text{NULL})
   $$

### Relational Formulation
Reaching the required relation takes exactly two operations over the shared key `personId`: a join predicate that pairs every `Person` tuple with its matching `Address` tuples while retaining left tuples that have no partner, followed by a projection onto the four required attributes `firstName`, `lastName`, `city`, and `state`. Which join type delivers the retention guarantee is the decisive choice this instance teaches; the concrete query belongs to the Reference workflow.

> **Invariant.** The number of rows emitted in the result set is at least equal to $|\text{Person}|$. Every person in `Person` appears in the output with their exact name, regardless of address presence.

---

## 3. Step-by-Step Worked Execution

We trace the join evaluation row by row across `Person`:

### Row 1: Person $p_1 = (1, \text{"Wang"}, \text{"Allen"})$
- Scan `Address` table looking for $A.\text{personId} == 1$:
  - Row 1 ($A_1$): $\text{personId} = 2 \ne 1$.
  - Row 2 ($A_2$): $\text{personId} = 3 \ne 1$.
- No matching address exists in `Address`!
- **Left Outer Join Rule:** Preserve person row, pad address columns with SQL `NULL`:
  - `firstName` = `"Allen"`
  - `lastName` = `"Wang"`
  - `city` = `NULL`
  - `state` = `NULL`
- Emit row: `["Allen", "Wang", null, null]`.

---

### Row 2: Person $p_2 = (2, \text{"Alice"}, \text{"Bob"})$
- Scan `Address` table looking for $A.\text{personId} == 2$:
  - Row 1 ($A_1$): $\text{personId} = 2 == 2$. Match found!
- Extract matching address columns:
  - `city` = `"New York City"`
  - `state` = `"New York"`
- Combine attributes:
  - `firstName` = `"Bob"`
  - `lastName` = `"Alice"`
  - `city` = `"New York City"`
  - `state` = `"New York"`
- Emit row: `["Bob", "Alice", "New York City", "New York"]`.

---

### Orphan Check: Address $A_2 = (2, 3, \text{"Leetcode"}, \text{"California"})$
- In `Address`, person ID $3$ exists, but person $3$ is **not in the `Person` table**.
- Because the join is a `LEFT JOIN` on `Person`, unmatched rows in `Address` are **ignored** and discarded.

Result set complete!

---

## 4. Complete Execution Trace

| Tuple | Source Relation | Join Decision | Retained? |
|:---|:---|:---|:---|
| `(1, "Wang", "Allen")` | `Person` | No `Address` tuple has `personId = 1`, so the join predicate produces no pairing | Yes, padded with `null` address columns |
| `(2, "Alice", "Bob")` | `Person` | The `Address` tuple `(1, 2, "New York City", "New York")` satisfies $P.\text{personId} = A.\text{personId}$ | Yes, with the matched address attributes |
| `(2, 3, "Leetcode", "California")` | `Address` | Right-side tuple whose `personId = 3` never appears in `Person` | No, a left outer join ignores unmatched right-side tuples |

The projected result set, in `Person` order, is:

| `firstName` | `lastName` | `city` | `state` |
|:---|:---|:---|:---|
| `"Allen"` | `"Wang"` | `null` | `null` |
| `"Bob"` | `"Alice"` | `"New York City"` | `"New York"` |

| Source `Person` Row | `personId` | Address Match Condition | Address Row Matched | Result Columns (`firstName, lastName, city, state`) |
|:---|:---:|:---:|:---:|:---|
| `(1, "Wang", "Allen")` | 1 | No match in `Address` | None | `["Allen", "Wang", null, null]` |
| `(2, "Alice", "Bob")` | 2 | $A.\text{personId} == 2$ | `(1, 2, "New York City", "New York")` | `["Bob", "Alice", "New York City", "New York"]` |

---

## 5. Algorithmic Correctness

**Soundness.** A left outer join on $P.\text{personId} = A.\text{personId}$ guarantees that every tuple from the left relation appears in the output. Projecting explicitly (`p.firstName`, `p.lastName`, `a.city`, `a.state`) discards the surrogate primary keys `personId` and `addressId`, strictly matching the required schema.

**Completeness.** Since the left table `Person` defines the universe of individuals to report, every person is represented once. The `ON` condition matches all existing addresses and defaults to `NULL` whenever an address record is missing.

---

## 6. Traps This Instance Exposes

- **Using `INNER JOIN` Instead of `LEFT JOIN`:** An inner join discards `"Allen Wang"` because he has no address record, returning only 1 row instead of 2.
- **Using `RIGHT JOIN` with Table Order Swapped:** `Address RIGHT JOIN Person` works logically but is discouraged in SQL style guides because reading left-to-right is clearer and standard across database engines.
- **`WHERE` Clause Null Filtering:** Adding a `WHERE a.city IS NOT NULL` would unintentionally convert the outer join back into an inner join, filtering out valid `NULL` address records.
- **Ambiguous Column Selection (`SELECT *`):** Writing `SELECT *` leaks `personId` and `addressId` into the result set and fails schema validation.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(P + A)$, where $P$ is the number of rows in `Person` and $A$ is the number of rows in `Address`. The database query engine builds a hash table on `Address` (or probes an index on `Address.personId`) in $O(1)$ lookup time per person row.
- **Auxiliary Space Complexity:** $O(P + A)$ working memory to execute the hash join and buffer the returned result set.
