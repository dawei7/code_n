# Guided Example: Friend Requests I: Overall Acceptance Rate

We trace the step-by-step distinct sender-receiver request pair deduplication (`COUNT(DISTINCT (sender_id, send_to_id))`), distinct requester-accepter acceptance pair deduplication (`COUNT(DISTINCT (requester_id, accepter_id))`), division-by-zero null coalescing (`COALESCE(..., 0)`), two-decimal rounded ratio evaluation, and conversion rate reporting on representative social network logs:

- **Input:**
  - `FriendRequest` table:
    | `sender_id` | `send_to_id` | `request_date` |
    |:---:|:---:|:---:|
    | $1$ | $2$ | `2016/06/01` |
    | $1$ | $3$ | `2016/06/01` |
    | $1$ | $4$ | `2016/06/01` |
    | $2$ | $3$ | `2016/06/02` |
    | $3$ | $4$ | `2016/06/09` |
  - `RequestAccepted` table:
    | `requester_id` | `accepter_id` | `accept_date` |
    |:---:|:---:|:---:|
    | $1$ | $2$ | `2016/06/03` |
    | $1$ | $3$ | `2016/06/08` |
    | $2$ | $3$ | `2016/06/08` |
    | $3$ | $4$ | `2016/06/09` |
    | $3$ | $4$ | `2016/06/10` |
- **Required output:**
  | `accept_rate` |
  |:---:|
  | $0.80$ |
  - Business metric definition:
    $$
    \text{Overall Acceptance Rate} = \frac{\text{Total distinct accepted requests}}{\text{Total distinct friend requests}}
    $$
  - Duplicate policy: Multiple requests or acceptances between the same pair of users count as **one single distinct event**.
  - Zero denominator policy: If there are no friend requests recorded (requests $= 0$), the acceptance rate is defined as $0.00$.
  - Formatting: Round the final rate to $2$ decimal places.
- **Relational Deduplication & Ratio Trace:**
  - **Step 1: Count Distinct Sent Requests ($N_{req}$):**
    - Unique sender-receiver pairs in `FriendRequest`:
      - Pair $(1, 2)$
      - Pair $(1, 3)$
      - Pair $(1, 4)$
      - Pair $(2, 3)$
      - Pair $(3, 4)$
    - Total distinct requests:
      $$
      N_{req} = \mathbf{5}
      $$
  - **Step 2: Count Distinct Accepted Requests ($N_{acc}$):**
    - Unique requester-accepter pairs in `RequestAccepted`:
      - Pair $(1, 2)$
      - Pair $(1, 3)$
      - Pair $(2, 3)$
      - Pair $(3, 4)$ *(appears twice on 06/09 and 06/10, deduplicated to 1)*
    - Total distinct acceptances:
      $$
      N_{acc} = \mathbf{4}
      $$
  - **Step 3: Calculate Acceptance Ratio:**
    - Ratio formula:
      $$
      \text{Rate} = \frac{N_{acc}}{N_{req}} = \frac{4}{5} = \mathbf{0.80}
      $$
  - **Step 4: Division-by-Zero and Rounding Guard:**
    - If $N_{req} == 0$, division in SQL evaluates to `NULL` (or raises divide-by-zero error).
    - Wrapping the calculation in `COALESCE(..., 0)` guarantees a safe fallback of $0$.
    - Rounding to 2 decimal places:
      $$
      \text{ROUND}(0.80, \; 2) = \mathbf{0.80}
      $$
- **Empty Requests Table ($N_{req} = 0$):**
  - No requests sent $\implies$ denominator is 0 $\implies \text{COALESCE}(\dots, 0)$ evaluates to $\mathbf{0.00}$.
- **Duplicate Acceptance Entries:**
  - User 3 and User 4 accepted on two different dates (June 9 and June 10).
  - Deduplicating via `DISTINCT (requester_id, accepter_id)` ensures the relationship is counted exactly once.
- **Perfect Conversion ($100\%$ accepted):**
  - If 5 requests are sent and all 5 are accepted $\implies 5 / 5 = \mathbf{1.00}$.

This instance demonstrates distinct dyadic event counting and guarded ratio division in relational databases, mathematically proves why pair-level deduplication is invariant to repeated timestamps, and derives $O(R + A)$ execution time and $O(R + A)$ space bounds.

---

## 1. Instance & Teaching Goal

Given two tables `FriendRequest` and `RequestAccepted`:
Find the **overall acceptance rate** of friend requests:
$$
\text{Rate} = \frac{\text{Count of unique accepted pairs}}{\text{Count of unique requested pairs}}
$$
Round the result to 2 decimal places. If there are no requests, return `0.00`.

```text
Friend Requests (Unique Pairs):
  (1, 2), (1, 3), (1, 4), (2, 3), (3, 4) -> Total = 5

Requests Accepted (Unique Pairs):
  (1, 2), (1, 3), (2, 3), (3, 4)         -> Total = 4

Rate = 4 / 5 = 0.80
```

### Clarifying Independent Deduplication
- A requester and accepter can send multiple requests and acceptances across different days.
- The metric specifically measures the **fraction of requested relationships that converted into accepted friendships**, ignoring duplicate transmissions.
- Both numerator and denominator must apply `COUNT(DISTINCT (user1, user2))`.

---

## 2. Conceptual Foundation & Invariants

### 1. The SQL Query Formulation:
```sql
SELECT
    ROUND(
        COALESCE(
            (SELECT COUNT(DISTINCT (requester_id, accepter_id)) * 1.0 FROM RequestAccepted) /
            (SELECT COUNT(DISTINCT (sender_id, send_to_id)) FROM FriendRequest),
            0
        ),
        2
    ) AS accept_rate;
```

### 2. Guarding Edge Cases:
- Multiplying by `1.0` or using numeric types prevents integer division truncation.
- `COALESCE(..., 0)` catches both `NULL` resulting from an empty `FriendRequest` table and division-by-zero.

> **Dyadic Idempotence Invariant.** Duplicate relationship pings across distinct timestamps collapse under set projection into a single undirected dyadic event.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Distinct Requests
- Unique pairs in `FriendRequest`:
  - $(1, 2), (1, 3), (1, 4), (2, 3), (3, 4)$
- Count = 5.

---

### Step 2: Distinct Acceptances
- Unique pairs in `RequestAccepted`:
  - $(1, 2), (1, 3), (2, 3), (3, 4)$
- Note: $(3, 4)$ occurs twice; counted once.
- Count = 4.

---

### Step 3: Compute and Round
$$
\text{Rate} = \frac{4.0}{5} = 0.80
$$
$$
\text{ROUND}(0.80, 2) = \mathbf{0.80}
$$

---

## 4. Complete Execution Trace

| Metric | Raw Table Rows | Distinct User Pairs | Scalar Count |
|:---:|:---:|:---:|:---:|
| **Requests** | $5$ rows | $(1,2), (1,3), (1,4), (2,3), (3,4)$ | $N_{req} = 5$ |
| **Acceptances** | $5$ rows | $(1,2), (1,3), (2,3), (3,4)$ | $N_{acc} = 4$ |
| **Fraction** | — | $4 / 5$ | $0.80$ |
| **Output** | — | `ROUND(0.80, 2)` | **`accept_rate: 0.80`** |

---

## 5. Boundary Cases & Failure Modes

- **Zero Requests ($N_{req} = 0$):** Denominator is 0 $\implies$ returns $0.00$.
- **Zero Acceptances ($N_{acc} = 0$):** Numerator is 0 $\implies 0 / N = 0.00$.
- **More Acceptances Than Requests:** Possible if acceptances occurred from offline/historical channels not in `FriendRequest`; ratio computes normally.
- **Repeated Re-requests:** Handled by `DISTINCT`.

---

## 6. Traps & Common Anti-Patterns

- **Joining Tables on User IDs:** Joining `FriendRequest` with `RequestAccepted` computes a relational intersection, which drops accepted pairs not present in requests and alters counts. The two tables must be counted as independent aggregates.
- **Counting Raw Rows Without `DISTINCT`:** Duplicate request logs artificially inflate the denominator, yielding an inaccurate acceptance rate.
- **Integer Division Truncation:** Evaluating $4 / 5$ in PostgreSQL/SQL Server produces integer $0$. Casting to float/numeric preserves the decimal.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Distinct hash set insertion for `FriendRequest`: $\mathcal{O}(R)$ where $R$ is request count.
  - Distinct hash set insertion for `RequestAccepted`: $\mathcal{O}(A)$ where $A$ is accept count.
  - Scalar division and rounding: $\mathcal{O}(1)$.
  - Total Time: strictly linear $\mathcal{O}(R + A)$. Completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(R + A)$ space to build the hash sets of unique user pairs.
