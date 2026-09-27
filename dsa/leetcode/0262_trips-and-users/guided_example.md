# Guided Example: Trips and Users

We trace the step-by-step dual foreign key user filtering, inclusive date interval partitioning, and daily cancellation rate aggregation on representative ride hailing database tables:

- **Input:**
  - `Trips` table with request records across client, driver, status, and dates
  - `Users` table designating banned status (`'Yes'` vs `'No'`)
- **Required output:**
  ```text
  +------------+-------------------+
  | Day        | Cancellation Rate |
  +------------+-------------------+
  | 2013-10-01 | 0.50              |
  | 2013-10-02 | 0.00              |
  | 2013-10-03 | 1.00              |
  +------------+-------------------+
  ```
- **Banned User Elimination:** Trips involving a banned client or banned driver are discarded before computing daily totals
- **Status Classification:** `cancelled_by_client` and `cancelled_by_driver` count as cancellations; `completed` counts as successful
- **Rounding:** Rounded to two decimal digits (`ROUND(rate, 2)`)

This instance demonstrates relational multi-join filtering on identical source tables (`Users` joined as both client and driver), Boolean indicator aggregation (`SUM(status != 'completed') / COUNT(*)`), date-window grouping, and handling days with zero cancellations.

---

## 1. Instance & Teaching Goal

Given two relational tables:
`Trips`:
| id | client_id | driver_id | city_id | status | request_at |
|:---:|:---:|:---:|:---:|:---|:---:|
| 1 | 1 | 10 | 1 | `completed` | `2013-10-01` |
| 2 | 2 | 11 | 1 | `cancelled_by_driver` | `2013-10-01` |
| 3 | 3 | 10 | 1 | `completed` | `2013-10-02` |
| 4 | 1 | 11 | 1 | `cancelled_by_client` | `2013-10-03` |

`Users`:
| users_id | banned | role |
|:---:|:---:|:---|
| 1 | `No` | `client` |
| 2 | `No` | `client` |
| 3 | `No` | `client` |
| 10 | `No` | `driver` |
| 11 | `No` | `driver` |

Compute the **cancellation rate** of requests with **unbanned users** (both client and driver must not be banned) each day between `"2013-10-01"` and `"2013-10-03"`, rounded to two decimal places:
$$
\text{Cancellation Rate} = \frac{\text{Canceled Trips with Unbanned Users}}{\text{Total Trips with Unbanned Users}}
$$

---

## 2. Conceptual Foundation & Invariants

### 1. The Dual-Role User Join
Each trip references two separate users:
- `client_id` references `Users.users_id`
- `driver_id` references `Users.users_id`
A trip is eligible **if and only if** both the client is unbanned AND the driver is unbanned:
```sql
JOIN Users c ON t.client_id = c.users_id AND c.banned = 'No'
JOIN Users d ON t.driver_id = d.users_id AND d.banned = 'No'
```
If either user is banned (`banned = 'Yes'`), the inner join eliminates the trip entirely from both the numerator and denominator.

### 2. Date Filtering
The problem restricts the analysis to a fixed 3-day window:
```sql
WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
```

### 3. Indicator Aggregation
The status enum consists of three values:
- `'completed'` (Success)
- `'cancelled_by_client'` (Canceled)
- `'cancelled_by_driver'` (Canceled)
The condition `status != 'completed'` evaluates to `1` for both cancellation types and `0` for completed trips.
The daily cancellation rate is computed as:
$$
\text{Rate} = \text{ROUND}\left(\frac{\sum (\text{status} \ne \text{'completed'})}{\text{COUNT}(*)}, \; 2\right) = \text{ROUND}(\text{AVG}(\text{status} \ne \text{'completed'}), \; 2)
$$

> **Invariant.** For each day, only trips where $\text{banned}_{\text{client}} = \text{'No'}$ and $\text{banned}_{\text{driver}} = \text{'No'}$ contribute to the grouped count.

---

## 3. Step-by-Step Worked Execution

We trace the relational operations across the sample data:

### Step 1: Filter and Join
Every trip has date in `['2013-10-01', '2013-10-02', '2013-10-03']`.
All users in the sample table have `banned = 'No'`, so all four trips qualify:
- **Trip 1:** Date $= \text{2013-10-01}$, Client 1 (`No`), Driver 10 (`No`), Status: `completed` $\implies$ Valid, Indicator $= 0$.
- **Trip 2:** Date $= \text{2013-10-01}$, Client 2 (`No`), Driver 11 (`No`), Status: `cancelled_by_driver` $\implies$ Valid, Indicator $= 1$.
- **Trip 3:** Date $= \text{2013-10-02}$, Client 3 (`No`), Driver 10 (`No`), Status: `completed` $\implies$ Valid, Indicator $= 0$.
- **Trip 4:** Date $= \text{2013-10-03}$, Client 1 (`No`), Driver 11 (`No`), Status: `cancelled_by_client` $\implies$ Valid, Indicator $= 1$.

---

### Step 2: Group by Day and Compute Rates

#### Day 1: `'2013-10-01'`
- Trips present: Trip 1 (indicator $0$), Trip 2 (indicator $1$).
- Total eligible trips: $2$.
- Canceled trips: $1$.
- Ratio:
  $$
  \text{Cancellation Rate} = \text{ROUND}\left(\frac{1}{2}, \; 2\right) = \mathbf{0.50}
  $$

#### Day 2: `'2013-10-02'`
- Trips present: Trip 3 (indicator $0$).
- Total eligible trips: $1$.
- Canceled trips: $0$.
- Ratio:
  $$
  \text{Cancellation Rate} = \text{ROUND}\left(\frac{0}{1}, \; 2\right) = \mathbf{0.00}
  $$

#### Day 3: `'2013-10-03'`
- Trips present: Trip 4 (indicator $1$).
- Total eligible trips: $1$.
- Canceled trips: $1$.
- Ratio:
  $$
  \text{Cancellation Rate} = \text{ROUND}\left(\frac{1}{1}, \; 2\right) = \mathbf{1.00}
  $$

---

## 4. Complete Execution Trace

```text
Table Filtering:
Trip 1 (2013-10-01): Client 1 (Unbanned), Driver 10 (Unbanned), completed -> keep (0)
Trip 2 (2013-10-01): Client 2 (Unbanned), Driver 11 (Unbanned), cancelled -> keep (1)
Trip 3 (2013-10-02): Client 3 (Unbanned), Driver 10 (Unbanned), completed -> keep (0)
Trip 4 (2013-10-03): Client 1 (Unbanned), Driver 11 (Unbanned), cancelled -> keep (1)

Group by Day:
2013-10-01: 1 cancelled / 2 total = 0.50
2013-10-02: 0 cancelled / 1 total = 0.00
2013-10-03: 1 cancelled / 1 total = 1.00
```

| Date (`Day`) | Eligible Trip IDs | Status Indicators | Canceled Sum | Total Count | Computed Rate | Rounded Result |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `2013-10-01` | 1, 2 | `[0, 1]` | 1 | 2 | $1 / 2 = 0.5$ | **0.50** |
| `2013-10-02` | 3 | `[0]` | 0 | 1 | $0 / 1 = 0.0$ | **0.00** |
| `2013-10-03` | 4 | `[1]` | 1 | 1 | $1 / 1 = 1.0$ | **1.00** |

---

## 5. Algorithmic Correctness

**Soundness.** The query joins `Users` twice: once on `client_id` and once on `driver_id`, enforcing `banned = 'No'` on both aliases. This ensures that trips with banned participants are filtered out at the join stage. Using `ROUND(AVG(status != 'completed'), 2)` divides the count of non-completed trips by the total number of unbanned trips for that day, matching the problem definition.

**Completeness.** `GROUP BY request_at` partitions all matching trips by day, and the `BETWEEN` clause guarantees that all days in the requested window with at least one eligible trip are included.

---

## 6. Traps This Instance Exposes

- **Filtering Only Client or Only Driver:** Banning either party invalidates the trip! Joining `Users` only once or forgetting to check `d.banned = 'No'` leaves banned drivers in the statistics.
- **Handling Dates with Zero Cancellations:** When all trips on a day are completed, the rate must evaluate to `0.00`, not `NULL`. `SUM(status != 'completed')` evaluates to `0`, producing `0.00` correctly.
- **Decimal Precision Formatting:** The problem requires rounding to two decimal places. `ROUND(..., 2)` ensures standard formatting.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(T \log U)$ or $O(T)$ with hash joins, where $T$ is the number of rows in `Trips` and $U$ is the number of rows in `Users`. The primary key index on `Users.users_id` allows $O(1)$ index lookups for each trip. Sorting into date groups takes $O(T \log D)$ where $D \le 3$ is the date count.
- **Auxiliary Space Complexity:** $O(T)$ temporary space for hash join tables and group aggregation buffers.
