# Guided Example: Friend Requests II: Who Has the Most Friends

We trace the step-by-step undirected social graph symmetrization (`UNION ALL`), bidirectional vertex incidence expansion, vertex degree aggregation (`COUNT(1)`), descending degree sorting, top-1 maximum friend count extraction, and relational attribute renaming (`id`, `num`) on representative friendship logs:

- **Input:**
  - `RequestAccepted` table:
    | `requester_id` | `accepter_id` | `accept_date` |
    |:---:|:---:|:---:|
    | $1$ | $2$ | `2016-06-03` |
    | $1$ | $3$ | `2016-06-08` |
    | $2$ | $3$ | `2016-06-08` |
    | $3$ | $4$ | `2016-06-09` |
- **Required output:**
  | `id` | `num` |
  |:---:|:---:|
  | $3$ | $3$ |
  - Problem contract: Find the individual user who has the **highest total number of friends** (`num`), along with their user ID (`id`).
  - Graph symmetry rule: Friendship is bidirectional. If user $u$ sent a request that user $v$ accepted, then $u$ is a friend of $v$ AND $v$ is a friend of $u$.
  - Uniqueness guarantee: The test cases are constructed such that exactly one person has the strict maximum number of friends.
- **Undirected Edge Symmetrization Trace:**
  - In the input table, each friendship edge $(u, v)$ is recorded only once in one arbitrary direction ($requester \to accepter$).
  - If we only count `requester_id`, we miss friendships where the user was the `accepter_id`.
  - To compute each user's true degree (number of friends):
    - Duplicate each edge in both directions using `UNION ALL`:
      $$
      T = \{(u, v) \mid (u, v) \in RequestAccepted\} \cup \{(v, u) \mid (u, v) \in RequestAccepted\}
      $$
  - **Step 1: Symmetrize the Edges:**
    - From $(1, 2) \implies (1, 2)$ and $(2, 1)$
    - From $(1, 3) \implies (1, 3)$ and $(3, 1)$
    - From $(2, 3) \implies (2, 3)$ and $(3, 2)$
    - From $(3, 4) \implies (3, 4)$ and $(4, 3)$
    - The symmetrized relation $T$ contains $8$ directed rows:
      - Rows where user is the primary subject:
        - User $1$: $(1, 2), (1, 3)$
        - User $2$: $(2, 1), (2, 3)$
        - User $3$: $(3, 1), (3, 2), (3, 4)$
        - User $4$: $(4, 3)$
  - **Step 2: Group by User ID and Count Degree:**
    - Group by the first column (`requester_id AS id`):
      - **User 1:** Friends are $\{2, 3\} \implies num = 1 + 1 = \mathbf{2}$.
      - **User 2:** Friends are $\{1, 3\} \implies num = 1 + 1 = \mathbf{2}$.
      - **User 3:** Friends are $\{1, 2, 4\} \implies num = 1 + 1 + 1 = \mathbf{3}$.
      - **User 4:** Friends are $\{3\} \implies num = 1 = \mathbf{1}$.
  - **Step 3: Sort by Total Friends Descending and Slice Top 1:**
    - Ordered degree ranking:
      1. User $3$: $num = 3$ (**Highest!**)
      2. User $1$: $num = 2$
      3. User $2$: $num = 2$
      4. User $4$: $num = 1$
    - Slice the leading record with `LIMIT 1`:
      | `id` | `num` |
      |:---:|:---:|
      | $3$ | $3$ |
- **Single Friendship Graph Instance ($RequestAccepted = [(1, 2)]$):**
  - Edge $(1, 2)$ symmetrizes to $(1, 2)$ and $(2, 1)$.
  - Both users have 1 friend.
- **Hub-and-Spoke Topology (Star Graph):**
  - Center node connected to $K$ spokes $\implies$ Center degree is $K$, all spokes have degree $1 \implies$ Center node extracted in $O(1)$ post-sort.

This instance demonstrates undirected graph degree calculation via relational multiset unions, mathematically proves why `UNION ALL` preserves mutual adjacency reciprocity without duplicate edge loss, and derives $O(E \log V)$ execution time and $O(E)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a table `RequestAccepted` with `requester_id` and `accepter_id`:
Find the person who has the **most friends** and their total friend count.

```text
Friendships (Undirected Edges):
  1 --- 2
  | \   |
  |   \ |
  4 --- 3

Friends per person:
  User 1: [2, 3]    -> 2 friends
  User 2: [1, 3]    -> 2 friends
  User 3: [1, 2, 4] -> 3 friends  <-- Most friends!
  User 4: [3]       -> 1 friend

Result: id = 3, num = 3
```

### The Symmetrization Technique
- Relational tables store edges in an asymmetric format (one user is the requester, one is the accepter).
- Friendship is an **undirected edge**: $(u, v)$ implies $u$ is connected to $v$, and $v$ is connected to $u$.
- By selecting both `(requester, accepter)` and `(accepter, requester)` with `UNION ALL`, each person's total connections can be measured with a simple `GROUP BY`.

---

## 2. Conceptual Foundation & Invariants

### 1. The Symmetrization Query:
```sql
WITH T AS (
    SELECT requester_id, accepter_id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id, requester_id FROM RequestAccepted
)
SELECT requester_id AS id, COUNT(1) AS num
FROM T
GROUP BY requester_id
ORDER BY num DESC
LIMIT 1;
```

### 2. Why `UNION ALL` Instead of `UNION`?
- `UNION` deduplicates identical rows.
- Since each friendship is stored once in `RequestAccepted`, reversing the columns produces completely disjoint pairs $(u, v) \ne (v, u)$.
- `UNION ALL` avoids an expensive sort-based deduplication pass, executing much faster.

> **Degree Conservation Invariant.** Every undirected edge contributes exactly $+1$ to the degree of each of its two endpoints, conserving total incident degree $2|E|$ across the graph.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Symmetrize with `UNION ALL`
- Direct edges: $(1, 2), (1, 3), (2, 3), (3, 4)$.
- Reversed edges: $(2, 1), (3, 1), (3, 2), (4, 3)$.
- Union table $T$ contains 8 rows.

---

### Step 2: Group by First Column
- User 1: $(1, 2), (1, 3) \implies count = 2$.
- User 2: $(2, 1), (2, 3) \implies count = 2$.
- User 3: $(3, 1), (3, 2), (3, 4) \implies count = 3$.
- User 4: $(4, 3) \implies count = 1$.

---

### Step 3: Order by `num DESC` and `LIMIT 1`
- Rank 1: `id = 3, num = 3`.
- Sliced output:
  $$
  (3, 3)
  $$

---

## 4. Complete Execution Trace

| User ID | Friends in Forward Edges | Friends in Reverse Edges | Total Degree `num` | Degree Rank | Top 1 Selected? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $2, 3$ | None | $2$ | $2$ | No |
| $2$ | $3$ | $1$ | $2$ | $2$ | No |
| **$3$** | **$4$** | **$1, 2$** | **$3$** | **$1$ (Max)** | **Yes (`(3, 3)`)** |
| $4$ | None | $3$ | $1$ | $4$ | No |

---

## 5. Boundary Cases & Failure Modes

- **Single Friendship in Database:** Both users have 1 friend; problem guarantees unique maximum.
- **User Only Sends Requests:** All appearances in `requester_id`; correctly accumulated by first SELECT.
- **User Only Accepts Requests:** All appearances in `accepter_id`; correctly accumulated by second SELECT.
- **Large Social Network ($10^5$ rows):** Hash grouping aggregates the $2E$ rows in a single streaming scan.

---

## 6. Traps & Common Anti-Patterns

- **Counting Only `requester_id`:** Misses all friendships where the user was the receiver, drastically undercounting total friends.
- **Using Full Outer Joins Instead of `UNION ALL`:** Joining `requester_id` with `accepter_id` creates cumbersome null handling. `UNION ALL` flattens all connections into a single uniform column.
- **Forgetting Column Aliases:** The problem explicitly requires output columns named `id` and `num`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $E$ be the number of rows in `RequestAccepted` and $V$ be the number of unique users.
  - Symmetrizing with `UNION ALL`: $\mathcal{O}(E)$.
  - Hash grouping on $2E$ rows: $\mathcal{O}(E)$.
  - Sorting degrees with `LIMIT 1`: $\mathcal{O}(V \log V)$ (or $\mathcal{O}(V)$ with top-1 min-heap).
  - Total Time: $\mathcal{O}(E + V \log V)$. Completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(E)$ space for the intermediate union CTE $T$.
