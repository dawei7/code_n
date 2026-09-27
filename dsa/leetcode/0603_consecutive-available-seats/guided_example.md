# Guided Example: Consecutive Available Seats

We trace the step-by-step adjacent neighbor self-join distance predicate ($|a.seat\_id - b.seat\_id| = 1$), mutual availability boolean testing ($a.free \land b.free$), duplicate seat elimination via set projection (`DISTINCT`), and ascending seat identifier ordering on representative cinema seating arrangements:

- **Input:**
  - `Cinema` table:
    | `seat_id` | `free` |
    |:---:|:---:|
    | $1$ | $1$ |
    | $2$ | $0$ |
    | $3$ | $1$ |
    | $4$ | $1$ |
    | $5$ | $1$ |
- **Required output:**
  | `seat_id` |
  |:---:|
  | $3$ |
  | $4$ |
  | $5$ |
  - Business qualification rule: A seat qualifies as a **consecutive available seat** if and only if:
    1. The seat itself is free ($free = 1$).
    2. At least **one immediate neighboring seat** (either $seat\_id - 1$ or $seat\_id + 1$) is also free ($free = 1$).
  - Ordering: Output must be sorted by `seat_id ASC`.
- **Relational Neighbor Adjacency Trace:**
  - Self-join formulation:
    - Join table `Cinema a` with `Cinema b` on the condition:
      $$
      |a.seat\_id - b.seat\_id| = 1 \quad \text{and} \quad a.free = 1 \quad \text{and} \quad b.free = 1
      $$
    - For each seat $a$, this joins with $b$ if either immediate neighbor is also free.
  - **Step-by-Step Row Evaluation:**
    - **Seat $1$ (`free = 1`):**
      - Left neighbor ($seat\_id = 0$): Does not exist.
      - Right neighbor ($seat\_id = 2$): Exists, but has $free = 0$ (Occupied!).
      - Seat $1$ has **no free adjacent neighbors** $\implies$ Disqualified!
    - **Seat $2$ (`free = 0`):**
      - Fails primary condition ($a.free = 0$) $\implies$ Disqualified!
    - **Seat $3$ (`free = 1`):**
      - Left neighbor ($seat\_id = 2$): $free = 0$.
      - Right neighbor ($seat\_id = 4$): $free = 1$ (Available!).
      - Pair $(3, 4)$ satisfies adjacency and availability $\implies \mathbf{Seat\ 3\ Qualifies!}$
    - **Seat $4$ (`free = 1`):**
      - Left neighbor ($seat\_id = 3$): $free = 1$ (Available!).
      - Right neighbor ($seat\_id = 5$): $free = 1$ (Available!).
      - Pairs $(4, 3)$ and $(4, 5)$ both satisfy the join $\implies \mathbf{Seat\ 4\ Qualifies!}$
    - **Seat $5$ (`free = 1`):**
      - Left neighbor ($seat\_id = 4$): $free = 1$ (Available!).
      - Right neighbor ($seat\_id = 6$): Does not exist.
      - Pair $(5, 4)$ satisfies adjacency and availability $\implies \mathbf{Seat\ 5\ Qualifies!}$
  - **Step 2: Deduplication via `DISTINCT`:**
    - Notice that Seat $4$ matched twice: once with Seat $3$ and once with Seat $5$.
    - Applying `SELECT DISTINCT a.seat_id` collapses duplicate matches, ensuring Seat $4$ appears exactly once.
  - **Step 3: Sort Ascending:**
    - Qualified seats: $\{3, 4, 5\}$.
    - In ascending order:
      - $3$
      - $4$
      - $5$
- **Isolated Free Seats Instance ($free = [1, 0, 1, 0, 1]$):**
  - No two free seats are adjacent $\implies$ empty result table.
- **Pair of Free Seats ($free = [1, 1, 0, 0]$):**
  - Both Seat 1 and Seat 2 qualify and are returned $\implies [1, 2]$.

This instance demonstrates adjacent tuple neighborhood joins and relational self-referencing predicates, mathematically proves why absolute index difference $|i - j| = 1$ identifies metric adjacency in linear arrays, and derives $O(N \log N)$ execution time and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a `Cinema` table tracking whether each `seat_id` is `free` (1) or occupied (0):
Find all seats that are part of a run of **consecutive available seats** (meaning the seat is free and at least one adjacent neighbor is free).
Order by `seat_id ASC`.

```text
Cinema Seats:
  Seat 1: Free (Neighbor 2 is Occupied -> Isolated, Not consecutive)
  Seat 2: Occupied
  Seat 3: Free (Neighbor 4 is Free -> Consecutive!)
  Seat 4: Free (Neighbors 3 & 5 are Free -> Consecutive!)
  Seat 5: Free (Neighbor 4 is Free -> Consecutive!)

Output: 3, 4, 5
```

### Neighborhood Joining Logic
- A seat $a$ is consecutive available if there exists a seat $b$ such that:
  1. $b$ is immediately adjacent to $a$: $|a.seat\_id - b.seat\_id| = 1$.
  2. Both $a$ and $b$ are free: $a.free = 1 \land b.free = 1$.
- Because middle seats (like Seat 4) match with both their left and right neighbors, `DISTINCT` is required to prevent duplicate rows.

---

## 2. Conceptual Foundation & Invariants

### 1. The Adjacency Join:
```sql
SELECT DISTINCT a.seat_id
FROM Cinema AS a
JOIN Cinema AS b
    ON ABS(a.seat_id - b.seat_id) = 1
   AND a.free = 1
   AND b.free = 1
ORDER BY a.seat_id;
```

### 2. Alternative Window Function Form (`LAG` / `LEAD`):
- A seat qualifies if:
  $$
  free = 1 \quad \text{AND} \quad (\text{LAG}(free) = 1 \lor \text{LEAD}(free) = 1)
  $$
- Both methods capture the exact same geometric property.

> **Adjacency Equivalence Invariant.** A seat has a free neighbor if and only if it belongs to a contiguous run of free seats of length at least 2.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Self-Join Matching
- Seat 1 (free):
  - Neighbor 2 is not free $\implies$ No match.
- Seat 2 (not free):
  - Fails $free = 1 \implies$ No match.
- Seat 3 (free):
  - Neighbor 4 is free $\implies$ Match `(3, 4)`.
- Seat 4 (free):
  - Neighbor 3 is free $\implies$ Match `(4, 3)`.
  - Neighbor 5 is free $\implies$ Match `(4, 5)`.
- Seat 5 (free):
  - Neighbor 4 is free $\implies$ Match `(5, 4)`.

---

### Step 2: Deduplicate
- Matched `a.seat_id` values: $[3, 4, 4, 5]$.
- `DISTINCT` produces: $[3, 4, 5]$.

---

### Step 3: Order Ascending
- Result:
  $$
  \mathbf{[3, 4, 5]}
  $$

---

## 4. Complete Execution Trace

| Seat $a$ | $a.free$ | Neighbor $b$ Checked | $b.free$ | Valid Pair? | Added to `DISTINCT a.seat_id`? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $1$ | $2$ | $0$ | No | No |
| $2$ | $0$ | — | — | No | No |
| **$3$** | **$1$** | **$4$** | **$1$** | **Yes** | **Yes (`3`)** |
| **$4$** | **$1$** | **$3, 5$** | **$1, 1$** | **Yes (both)** | **Yes (`4`)** |
| **$5$** | **$1$** | **$4$** | **$1$** | **Yes** | **Yes (`5`)** |

---

## 5. Boundary Cases & Failure Modes

- **No Adjacent Available Seats:** Returns empty result table with column header `seat_id`.
- **All Seats Available ($1 \dots N$):** All seats qualify and are returned in order.
- **Seat Run of Length Exactly 2 ($[1, 1, 0]$):** Both seats 1 and 2 qualify $\implies [1, 2]$.
- **Non-Contiguous Seat IDs:** If IDs have gaps (e.g. 1, 3, 5), $|a - b| = 1$ correctly rejects them because they are not adjacent.

---

## 6. Traps & Common Anti-Patterns

- **Forgetting `DISTINCT`:** A middle seat in a run of 3 or more available seats matches with both neighbors, generating duplicate rows unless `DISTINCT` is used.
- **Assuming Consecutive Means 3 or More:** In this problem, consecutive available means **at least 2** adjacent seats (a pair).
- **Joining on `a.seat_id = b.seat_id - 1` Without Symmetrizing:** Only checking right neighbor ($b = a + 1$) causes the rightmost seat of a valid pair to be dropped unless a two-way join or `OR` condition is used. `ABS(a - b) = 1` handles both directions symmetrically.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Self-join on indexed `seat_id`: $\mathcal{O}(N)$ (each seat checks at most 2 neighbors).
  - Sorting the qualified seats: $\mathcal{O}(K \log K)$ where $K \le N$.
  - Total Time: $\mathcal{O}(N \log N)$. Completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(K)$ space to store deduplicated qualified seat IDs.
