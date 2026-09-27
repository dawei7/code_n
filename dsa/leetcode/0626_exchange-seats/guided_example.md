# Guided Example: Exchange Seats

We trace the step-by-step consecutive student seat permutation ($2k - 1 \leftrightarrow 2k$), modular parity testing ($id \pmod 2$), odd-length terminal boundary retention (last odd seat preservation), bitwise involution index swapping ($((id - 1) \oplus 1) + 1$), null-safe partner fallback (`COALESCE`), and ordered result projection on representative classroom seating assignments:

- **Input:**
  - `Seat` table:
    | `id` | `student` |
    |:---:|:---:|
    | $1$ | `Abbot` |
    | $2$ | `Doris` |
    | $3$ | `Emerson` |
    | $4$ | `Green` |
    | $5$ | `Jeames` |
- **Required output:**
  | `id` | `student` |
  |:---:|:---:|
  | $1$ | `Doris` |
  | $2$ | `Abbot` |
  | $3$ | `Green` |
  | $4$ | `Emerson` |
  | $5$ | `Jeames` |
  - Business rules:
    - Swap the seating positions of every pair of consecutive students ($1 \leftrightarrow 2$, $3 \leftrightarrow 4$, etc.).
    - If total students $N$ is odd, the last student cannot be paired and **retains their original seat**.
    - Output must be ordered by `id ASC`.
- **Involution Permutation & Partner Mapping:**
  - Let $target(id)$ denote the ID of the student who should sit at seat $id$:
    - For an odd seat $id$:
      - If a successor $id + 1$ exists in the table, seat $id$ takes student from $id + 1$.
      - If $id$ is the last seat ($id = N$), student remains unchanged.
    - For an even seat $id$:
      - Seat $id$ takes student from predecessor $id - 1$.
  - **The Bitwise XOR Pairing Trick:**
    - Convert to 0-based indexing: $idx = id - 1$.
    - In 0-based indexing, the pairs are $(0, 1), (2, 3), (4, 5), \dots$.
    - Notice that toggling the lowest bit via XOR 1 ($\oplus 1$) swaps every pair:
      $$
      0 \oplus 1 = 1, \quad 1 \oplus 1 = 0
      $$
      $$
      2 \oplus 1 = 3, \quad 3 \oplus 1 = 2
      $$
      $$
      4 \oplus 1 = 5, \quad 5 \oplus 1 = 4
      $$
    - Shifting back to 1-based indexing:
      $$
      partner\_id = ((id - 1) \oplus 1) + 1
      $$
    - If $partner\_id$ does not exist (e.g. $id = 5 \implies partner\_id = 6$, which is absent), a `LEFT JOIN` returns `null`.
    - Wrapping in `COALESCE(s2.student, s1.student)` automatically falls back to the original student for the lone trailing seat!
- **Step-by-Step Worked Execution Trace on 5 Students:**
  - Table size $N = 5$.
  - **Seat $1$ (Odd):**
    - Desired partner: $((1 - 1) \oplus 1) + 1 = (0 \oplus 1) + 1 = 1 + 1 = \mathbf{2}$.
    - Look up student at ID 2: `Doris`.
    - Seat 1 receives:
      $$
      \mathbf{\text{"Doris"}}
      $$
  - **Seat $2$ (Even):**
    - Desired partner: $((2 - 1) \oplus 1) + 1 = (1 \oplus 1) + 1 = 0 + 1 = \mathbf{1}$.
    - Look up student at ID 1: `Abbot`.
    - Seat 2 receives:
      $$
      \mathbf{\text{"Abbot"}}
      $$
  - **Seat $3$ (Odd):**
    - Desired partner: $((3 - 1) \oplus 1) + 1 = (2 \oplus 1) + 1 = 3 + 1 = \mathbf{4}$.
    - Look up student at ID 4: `Green`.
    - Seat 3 receives:
      $$
      \mathbf{\text{"Green"}}
      $$
  - **Seat $4$ (Even):**
    - Desired partner: $((4 - 1) \oplus 1) + 1 = (3 \oplus 1) + 1 = 2 + 1 = \mathbf{3}$.
    - Look up student at ID 3: `Emerson`.
    - Seat 4 receives:
      $$
      \mathbf{\text{"Emerson"}}
      $$
  - **Seat $5$ (Last Odd):**
    - Desired partner: $((5 - 1) \oplus 1) + 1 = (4 \oplus 1) + 1 = 5 + 1 = \mathbf{6}$.
    - Look up student at ID 6:
      - ID 6 does not exist in the table (`null`).
    - Apply fallback: `COALESCE(null, s1.student) = s1.student`.
    - Seat 5 receives its original student:
      $$
      \mathbf{\text{"Jeames"}}
      $$
  - **Step 2: Emit Complete Seating Chart:**
    | `id` | `student` |
    |:---:|:---:|
    | $1$ | `Doris` |
    | $2$ | `Abbot` |
    | $3$ | `Green` |
    | $4$ | `Emerson` |
    | $5$ | `Jeames` |
- **Even Number of Students ($N = 4$):**
  - All students have valid reciprocal partners: $(1, 2) \leftrightarrow (2, 1)$ and $(3, 4) \leftrightarrow (4, 3)$. Zero nulls.
- **Single Student in Class ($N = 1$):**
  - ID 1 attempts partner 2 $\implies$ not found $\implies$ retains original student $\implies (1, \text{student})$.

This instance demonstrates permutation involutions and boundary coalescing in relational queries, mathematically proves why bitwise XOR index toggling establishes pairwise transpositions over contiguous integer blocks, and derives $O(N)$ execution time and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a `Seat` table with consecutive IDs $1 \dots N$:
Swap every two consecutive students ($1 \leftrightarrow 2, 3 \leftrightarrow 4$).
If $N$ is odd, the last student remains in their original seat.
Order by `id ASC`.

```text
Original:
  1 Abbot
  2 Doris
  3 Emerson
  4 Green
  5 Jeames (Last, odd)

Swapped:
  1 Doris   (from seat 2)
  2 Abbot   (from seat 1)
  3 Green   (from seat 4)
  4 Emerson (from seat 3)
  5 Jeames  (unpaired, stays)
```

### The Invariant of Bitwise Pair Involution
- For any 0-based index $k$:
  $k \oplus 1$ toggles between $2m$ and $2m + 1$.
- This gives a completely uniform formula for finding the exchange partner without any `IF-ELSE` branches:
  $$
  partner\_id = ((id - 1) \oplus 1) + 1
  $$
- A simple `LEFT JOIN` and `COALESCE` handles the unmatched trailing odd student.

---

## 2. Conceptual Foundation & Invariants

### 1. The Relational Self-Join Query:
```sql
SELECT s1.id, COALESCE(s2.student, s1.student) AS student
FROM Seat AS s1
LEFT JOIN Seat AS s2
    ON (s1.id + 1) ^ 1 - 1 = s2.id
ORDER BY s1.id;
```
*(Where `(s1.id + 1) ^ 1 - 1` is algebraic shorthand for 1-based XOR swap)*.

### 2. Alternative Window Function Form:
```sql
SELECT
    id,
    CASE
        WHEN id % 2 = 1 AND id = (SELECT COUNT(*) FROM Seat) THEN student
        WHEN id % 2 = 1 THEN LEAD(student) OVER (ORDER BY id)
        ELSE LAG(student) OVER (ORDER BY id)
    END AS student
FROM Seat;
```

> **Transposition Involution Invariant.** The mapping $\pi(x) = ((x - 1) \oplus 1) + 1$ satisfies $\pi(\pi(x)) = x$ for all $x$, forming an involution composed of disjoint 2-cycles.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Map Partners for Each Seat
- Seat 1: partner is 2 $\implies$ Doris.
- Seat 2: partner is 1 $\implies$ Abbot.
- Seat 3: partner is 4 $\implies$ Green.
- Seat 4: partner is 3 $\implies$ Emerson.
- Seat 5: partner is 6 $\implies$ Not found (`null`).

---

### Step 2: Apply `COALESCE`
- Seat 5 receives `COALESCE(null, 'Jeames') = 'Jeames'`.

---

### Step 3: Project in Ascending ID Order
Emit pairs: `(1, Doris), (2, Abbot), (3, Green), (4, Emerson), (5, Jeames)`.

---

## 4. Complete Execution Trace

| Seat ID $s_1.id$ | Partner ID Target | Partner Found in $s_2$? | $s_2.student$ | Final Student Assigned |
|:---:|:---:|:---:|:---:|:---:|
| $1$ | $2$ | **Yes** | `Doris` | **`Doris`** |
| $2$ | $1$ | **Yes** | `Abbot` | **`Abbot`** |
| $3$ | $4$ | **Yes** | `Green` | **`Green`** |
| $4$ | $3$ | **Yes** | `Emerson` | **`Emerson`** |
| **$5$** | **$6$** | **No (`null`)** | `null` | **`Jeames` (Self)** |

---

## 5. Boundary Cases & Failure Modes

- **Single Seat ($N = 1$):** Partner is 2 (absent) $\implies$ student stays in seat 1.
- **Even Number of Seats ($N = 2$ or $N = 4$):** All seats cleanly transpose; 0 fallbacks occur.
- **Large Class ($10^5$ students):** Hash or merge join executes in $O(N)$ time.
- **Ascending ID Requirement:** Query concludes with `ORDER BY 1`.

---

## 6. Traps & Common Anti-Patterns

- **Swapping the `id` Column Directly Without Sorting:** If you change `id` to $partner\_id$ and don't re-sort, rows will output in jumbled order: `[2, 1, 4, 3, 5]`. Always sort by `id ASC`.
- **Inner Join Dropping the Last Student:** An `INNER JOIN` drops seat 5 because partner 6 does not exist. A `LEFT JOIN` is mandatory.
- **Overcomplicating the Last Odd Check:** Testing `id = (SELECT COUNT(*))` requires an extra table scan; the bitwise join with `COALESCE` handles it automatically.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Self-join on indexed primary key `id`: $\mathcal{O}(N)$.
  - Sifting output with `COALESCE`: $\mathcal{O}(N)$.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary memory (streaming join pipeline).
