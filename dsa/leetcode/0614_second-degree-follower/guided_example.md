# Guided Example: Second-Degree Follower

We trace the step-by-step 2-hop directed graph path expansion (`Follow f1 JOIN Follow f2 ON f1.follower = f2.followee`), dual-role condition verification (acting both as a follower and as a followee), distinct follower degree aggregation (`COUNT(DISTINCT followee)`), and alphabetical ordering on representative social network follow graphs:

- **Input:**
  - `Follow` table:
    | `followee` | `follower` |
    |:---:|:---:|
    | `Alice` | `Bob` |
    | `Bob` | `Cena` |
    | `Bob` | `Donald` |
    | `Donald` | `Edward` |
- **Required output:**
  | `follower` | `num` |
  |:---:|:---:|
  | `Bob` | $2$ |
  | `Donald` | $1$ |
  - Business definition of a **second-degree follower**:
    - A user $u$ who:
      1. Follows at least one user ($u$ exists in the `follower` column).
      2. Is followed by at least one user ($u$ exists in the `followee` column).
    - For each such qualifying user, count the number of users who follow them (`num`).
    - Output schema: Label the qualifying user's name under column header `follower`, and their follower count under `num`.
    - Ordering: Sort by `follower ASC`.
- **2-Hop Relational Path Formulation:**
  - If user $u$ is a second-degree follower:
    - There exists an edge: $u$ follows someone $\implies (X, u) \in Follow$.
    - There exists an edge: someone follows $u \implies (u, Y) \in Follow$.
  - Joining `Follow f1` with `Follow f2` on `f1.follower = f2.followee`:
    - `f1.followee` is the person that $u$ follows ($X$).
    - `f1.follower` is the target user $u$ (our candidate).
    - `f2.followee` is also $u$.
    - `f2.follower` is the person who follows $u$ ($Y$).
  - This join matches only users who simultaneously satisfy both criteria!
- **Step-by-Step Worked Execution Trace:**
  - Given directed edges $(followee, follower)$:
    - $e_1 = (\text{Alice}, \text{Bob})$
    - $e_2 = (\text{Bob}, \text{Cena})$
    - $e_3 = (\text{Bob}, \text{Donald})$
    - $e_4 = (\text{Donald}, \text{Edward})$
  - **Step 1: Perform Self-Join on $f_1.follower = f_2.followee$:**
    - Match $e_1$ (`follower = Bob`) with $e_2$ (`followee = Bob`):
      - Path: Alice $\leftarrow$ **Bob** $\leftarrow$ Cena
      - Record: `(follower: Bob, followee: Cena)`
    - Match $e_1$ (`follower = Bob`) with $e_3$ (`followee = Bob`):
      - Path: Alice $\leftarrow$ **Bob** $\leftarrow$ Donald
      - Record: `(follower: Bob, followee: Donald)`
    - Match $e_3$ (`follower = Donald`) with $e_4$ (`followee = Donald`):
      - Path: Bob $\leftarrow$ **Donald** $\leftarrow$ Edward
      - Record: `(follower: Donald, followee: Edward)`
    - What about `Alice`?
      - Alice is in `followee`, but never appears in `follower` (she follows no one).
      - Zero join matches for Alice $\implies$ Correctly omitted.
    - What about `Cena` and `Edward`?
      - They follow people, but nobody follows them (never appear in `followee`).
      - Zero join matches $\implies$ Correctly omitted.
  - **Step 2: Aggregate Follower Counts per Second-Degree User:**
    - Intermediate pairs:
      - `Bob`: `Cena`, `Donald`
      - `Donald`: `Edward`
    - **Group `follower = 'Bob'`:**
      - Distinct people following Bob: $\{\text{Cena}, \text{Donald}\}$
      - Count:
        $$
        num = \mathbf{2}
        $$
    - **Group `follower = 'Donald'`:**
      - Distinct people following Donald: $\{\text{Edward}\}$
      - Count:
        $$
        num = \mathbf{1}
        $$
  - **Step 3: Sort Alphabetically by `follower`:**
    1. `Bob` with count $2$
    2. `Donald` with count $1$
- **Isolated Directed Chains:**
  - A user at the root of a follow tree (followed by others but following nobody) or a leaf (following others but followed by nobody) is excluded.
- **Cycles in Following ($A \to B \to A$):**
  - Both $A$ and $B$ follow and are followed $\implies$ both qualify as second-degree followers.

This instance demonstrates 2-hop path aggregation over directed relational graphs, mathematically proves why joining predecessor and successor relations isolates vertices with both in-degree $\ge 1$ and out-degree $\ge 1$, and derives $O(E \log V)$ execution time and $O(E)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a `Follow` table tracking directed follow edges:
Find all **second-degree followers** (users who follow at least one person AND are followed by at least one person).
Report each user's name (`follower`) and how many people follow them (`num`).
Order alphabetically by user name.

```text
Follow Graph:
  Alice <--- Bob <--- Cena
              ^
              |
            Donald <--- Edward

Roles:
  Alice:  Followed by Bob, but follows no one -> Excluded
  Bob:    Follows Alice, Followed by Cena & Donald -> QUALIFIED! (num = 2)
  Donald: Follows Bob, Followed by Edward -> QUALIFIED! (num = 1)
  Cena:   Follows Bob, followed by no one -> Excluded
  Edward: Follows Donald, followed by no one -> Excluded

Output:
  Bob: 2
  Donald: 1
```

### Clarifying the Output Schema
- Note the schema convention: the subject user being reported is placed under the column name `follower`.
- The count of distinct incoming followers is named `num`.

---

## 2. Conceptual Foundation & Invariants

### 1. The 2-Hop Self-Join:
```sql
WITH T AS (
    SELECT f1.follower AS follower, f2.follower AS followee
    FROM Follow AS f1
    JOIN Follow AS f2 ON f1.follower = f2.followee
)
SELECT follower, COUNT(DISTINCT followee) AS num
FROM T
GROUP BY follower
ORDER BY follower;
```

### 2. Graph Invariant:
A user $u$ is included if and only if:
$$
\text{in-degree}(u) \ge 1 \quad \text{AND} \quad \text{out-degree}(u) \ge 1
$$
Their reported `num` equals $\text{in-degree}(u)$.

> **Two-Sided Degree Invariant.** An entity is an interior node in a directed path of length $\ge 2$ if and only if its incident in-edge and out-edge intersection is non-empty.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Join on `f1.follower = f2.followee`
- `f1` edge `(Alice, Bob)` has `follower = Bob`.
  - Matches `f2` edge `(Bob, Cena)` where `followee = Bob` $\implies$ `(Bob, Cena)`.
  - Matches `f2` edge `(Bob, Donald)` where `followee = Bob` $\implies$ `(Bob, Donald)`.
- `f1` edge `(Bob, Donald)` has `follower = Donald`.
  - Matches `f2` edge `(Donald, Edward)` where `followee = Donald` $\implies$ `(Donald, Edward)`.

---

### Step 2: Group by Target User
- `Bob`: followers are `Cena` and `Donald` $\implies num = 2$.
- `Donald`: follower is `Edward` $\implies num = 1$.

---

### Step 3: Sort Alphabetically
- Bob
- Donald

---

## 4. Complete Execution Trace

| Edge $f_1$ (`followee`, `follower`) | Edge $f_2$ (`followee`, `follower`) | Matched User | Person Following User | Aggregated `num` |
|:---:|:---:|:---:|:---:|:---:|
| `(Alice, Bob)` | `(Bob, Cena)` | `Bob` | `Cena` | — |
| `(Alice, Bob)` | `(Bob, Donald)` | `Bob` | `Donald` | **$2$** |
| `(Bob, Donald)` | `(Donald, Edward)` | `Donald` | `Edward` | **$1$** |
| **Output** | — | **`Bob (2), Donald (1)`** | — | — |

---

## 5. Boundary Cases & Failure Modes

- **Nobody Follows Anybody Who Follows Others (Disjoint Stars):** Join yields 0 rows $\implies$ empty table.
- **Multiple Redundant Follows:** Deduplicated by `COUNT(DISTINCT followee)`.
- **Single Mutual Follow Pair ($A \leftrightarrow B$):** Both $A$ and $B$ are reported with count $1$.
- **Large Social Graph:** Indexed join on `followee` and `follower` completes in linear time.

---

## 6. Traps & Common Anti-Patterns

- **Misinterpreting the Column Headers:** Putting the follower count on the followee instead of the target user creates reversed relationships.
- **Not Counting `DISTINCT` Followers:** If a duplicate row exists in the source, `COUNT(followee)` can overcount without `DISTINCT`.
- **Filtering with Subqueries Instead of Joins:** `WHERE follower IN (SELECT followee FROM Follow)` works, but joining directly produces a cleaner execution plan.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Self-join on indexed columns: $\mathcal{O}(E)$.
  - Hash grouping and counting: $\mathcal{O}(V)$.
  - Sorting results: $\mathcal{O}(K \log K)$ where $K \le V$.
  - Total Time: $\mathcal{O}(E + K \log K)$. Completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(E)$ space for intermediate 2-hop edges.
