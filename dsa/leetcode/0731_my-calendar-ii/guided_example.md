# Guided Example: My Calendar II

We trace the step-by-step speculative boundary difference array updates ($+1$ at $start$, $-1$ at $end$), sweep-line prefix sum accumulation ($s \leftarrow s + \delta$), peak concurrency evaluation ($s > 2 \implies \text{Triple Booking}$), atomic state rollback on collision, and valid double-booking interval scheduling on representative calendar event streams:

- **Input:**
  - Operations sequence:
    ```text
    MyCalendarTwo()
    book(10, 20)
    book(50, 60)
    book(10, 40)
    book(5, 15)
    book(5, 10)
    book(25, 55)
    ```
- **Required output:** `[true, true, true, false, true, true]`
  - Booking rules:
    - Events are half-open intervals $[start, end)$.
    - A **triple booking** occurs if there is any moment in time shared by **3 or more events**.
    - Double bookings (2 events overlapping) are **permitted**.
    - If a booking creates a triple booking, it must be rejected without modifying the calendar, returning `false`.
    - If accepted, record the event and return `true`.
    - Lifecycle trace:
      - `book(10, 20)`: Active events = 1 $\implies$ `true`.
      - `book(50, 60)`: Disjoint $\implies$ `true`.
      - `book(10, 40)`: Overlaps $[10, 20)$ on $[10, 20)$ (2 events concurrently) $\implies$ double booking allowed $\implies$ `true`.
      - `book(5, 15)`: Covers $[10, 15)$, where $[10, 20)$ and $[10, 40)$ are already active $\implies 3$ concurrent events! Triple booking detected! Rejected $\implies$ `false`.
      - `book(5, 10)`: Abuts $[10, 20)$ at 10 (half-open, no overlap at 10) $\implies$ max concurrency 2 $\implies$ `true`.
      - `book(25, 55)`: Overlaps $[10, 40)$ on $[25, 40)$ and $[50, 60)$ on $[50, 55)$ (concurrency 2 each) $\implies$ `true`.
- **Sweep-Line Difference Array & Atomic Rollback Invariant:**
  - **The Boundary Delta Representation:**
    - Any interval $[start, end)$ can be represented as a step change in event density:
      - At time $start$, density increments by $+1$: $\delta[start] \leftarrow \delta[start] + 1$.
      - At time $end$, density decrements by $-1$: $\delta[end] \leftarrow \delta[end] - 1$.
  - **Prefix Sum Concurrency Invariant:**
    - If all active boundary points are sorted in ascending order $t_0 < t_1 < \dots < t_k$, the instantaneous concurrency $C(t)$ is given by the running prefix sum:
      $$
      C(t) = \sum_{t_i \le t} \delta[t_i]
      $$
    - The schedule contains no triple booking if and only if:
      $$
      \max_t C(t) \le 2
      $$
  - **Speculative Booking Protocol:**
    1. **Tentative Addition:** Add $+1$ at $start$ and $-1$ at $end$ in the sorted difference structure.
    2. **Sweep-Line Verification:** Sweep through the sorted time points, computing running sum $s$:
       - If $s > 2$ at any point:
         - A triple booking has occurred!
         - **Atomic Rollback:** Undo the additions ($\delta[start] -= 1, \delta[end] += 1$).
         - Return `false`.
    3. **Commit:** If $s \le 2$ across the entire timeline, keep the changes and return `true`.
- **Step-by-Step Worked Execution Trace on the Sample Sequence:**
  - Initialize empty sorted difference table: $sd = \{\}$.
  - **Operation 1: `book(10, 20)`:**
    - Tentative deltas: $sd[10] = +1, \; sd[20] = -1$.
    - Sweep timeline:
      - At $t = 10$: $s = 0 + 1 = 1 \le 2$.
      - At $t = 20$: $s = 1 - 1 = 0 \le 2$.
    - Peak concurrency = 1. Valid!
    - Commit $\implies \mathbf{true}$.
  - **Operation 2: `book(50, 60)`:**
    - Tentative deltas: $sd[50] = +1, \; sd[60] = -1$.
    - Sweep timeline:
      - $t = 10 \to 1, \; t = 20 \to 0, \; t = 50 \to 1, \; t = 60 \to 0$.
    - Peak concurrency = 1. Valid!
    - Commit $\implies \mathbf{true}$.
  - **Operation 3: `book(10, 40)`:**
    - Tentative deltas:
      - $sd[10] \leftarrow 1 + 1 = 2$.
      - $sd[40] \leftarrow -1$.
    - Sweep timeline:
      - $t = 10$: $s = 0 + 2 = \mathbf{2} \le 2$ (Double booking allowed).
      - $t = 20$: $s = 2 - 1 = 1 \le 2$.
      - $t = 40$: $s = 1 - 1 = 0 \le 2$.
      - $t = 50$: $s = 0 + 1 = 1 \le 2$.
      - $t = 60$: $s = 1 - 1 = 0 \le 2$.
    - Peak concurrency = 2. Valid!
    - Commit $\implies \mathbf{true}$.
  - **Operation 4: `book(5, 15)`:**
    - Tentative deltas:
      - $sd[5] = +1$.
      - $sd[15] = -1$.
    - Sweep timeline:
      - $t = 5$: $s = 0 + 1 = 1$.
      - $t = 10$: $s = 1 + 2 = \mathbf{3} > 2 \implies \mathbf{Triple\ Booking\ Detected!}$
    - Collision identified over $[10, 15)$!
    - **Atomic Rollback:**
      - $sd[5] \leftarrow 1 - 1 = 0$.
      - $sd[15] \leftarrow -1 + 1 = 0$.
    - State restored cleanly.
    - Reject $\implies \mathbf{false}$.
  - **Operation 5: `book(5, 10)`:**
    - Tentative deltas: $sd[5] = +1, \; sd[10] \leftarrow 2 - 1 = 1$.
    - Sweep timeline:
      - $t = 5$: $s = 1$.
      - $t = 10$: $s = 1 + 1 = 2 \le 2$.
      - $t = 20$: $s = 2 - 1 = 1$.
      - $t = 40$: $s = 1 - 1 = 0$.
    - Peak concurrency = 2. Valid!
    - Commit $\implies \mathbf{true}$.
  - **Operation 6: `book(25, 55)`:**
    - Tentative deltas: $sd[25] = +1, \; sd[55] = -1$.
    - Peak concurrency across all timestamps reaches at most 2. Valid!
    - Commit $\implies \mathbf{true}$.
  - **Consolidated Outputs:**
    $$
    [\mathbf{true}, \; \mathbf{true}, \; \mathbf{true}, \; \mathbf{false}, \; \mathbf{true}, \; \mathbf{true}]
    $$
- **Three Identical Bookings ($[10, 20)$ called 3 times):**
  - Call 1: peak concurrency 1 $\implies$ `true`.
  - Call 2: peak concurrency 2 $\implies$ `true`.
  - Call 3: peak concurrency 3 $\implies$ rejected, returns `false`.
- **Touching Intervals at Same Point ($[10, 20)$ and $[20, 30)$):**
  - At $t = 20$: delta is $-1$ (from first) $+1$ (from second) $= 0$.
  - Running sum never exceeds 1 $\implies$ returns `true`.

This instance demonstrates sweep-line event density tracking and speculative transactional rollback state management, mathematically proves why prefix sum maxima over boundary deltas accurately characterize maximum interval intersection cardinality, and derives $O(N)$ sweep verification per booking and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Implement `MyCalendarTwo`:
Accept bookings $[start, end)$ as long as they do not cause a **triple booking** ($\ge 3$ overlapping events).
Double bookings ($\le 2$ events) are explicitly permitted.
If rejected, rollback without modifying state.

```text
Operations:
  book(10, 20) -> accepted (count = 1) -> true
  book(50, 60) -> accepted (count = 1) -> true
  book(10, 40) -> overlaps [10, 20) -> count = 2 -> double booking allowed -> true
  book(5, 15)  -> overlaps [10, 20) and [10, 40) -> count = 3 -> TRIPLE BOOKING! -> false
  book(5, 10)  -> touches at 10 -> count <= 2 -> true

Result: [ true, true, true, false, true, true ]
```

### The Invariant of the Speculative Sweep-Line
- Add $+1$ at $start$ and $-1$ at $end$ in a sorted difference map.
- Sweep through all time points: running sum $s$ tracks instantaneous active event count.
- If $s > 2$, undo the changes and return `false`. Otherwise, keep the booking and return `true`.

---

## 2. Conceptual Foundation & Invariants

### 1. Difference Array Concurrency Representation:
$$
\delta[start] \leftarrow \delta[start] + 1, \quad \delta[end] \leftarrow \delta[end] - 1
$$
$$
C(t) = \sum_{t_i \le t} \delta[t_i]
$$

### 2. Transactional Rollback Protocol:
$$
\text{If } \exists t: C(t) > 2 \implies \begin{cases} \delta[start] \leftarrow \delta[start] - 1 \\ \delta[end] \leftarrow \delta[end] + 1 \\ \text{return } \mathbf{False} \end{cases}
$$

> **Borel Measure Density Invariant.** The event density function $\rho(t) = \sum_k \mathbf{1}_{[s_k, e_k)}(t)$ is uniquely represented by its distributional derivative $\rho' = \sum_k (\delta_{s_k} - \delta_{e_k})$, where the capacity constraint $\|\rho\|_\infty \le 2$ is verifiable via sequential summation over atomic mass supports.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: `book(10, 20)`
- Deltas: $10 \to +1, 20 \to -1$. Max $s = 1 \le 2 \implies$ **`true`**.

---

### Step 2: `book(10, 40)`
- Deltas: $10 \to +2, 20 \to -1, 40 \to -1$. Max $s = 2 \le 2 \implies$ **`true`**.

---

### Step 3: `book(5, 15)`
- Add $5 \to +1, 15 \to -1$.
- At $t = 10$, $s = 1 + 2 = 3 > 2 \implies$ Triple Booking!
- Rollback $5 \to 0, 15 \to 0$. Return **`false`**.

---

### Step 4: `book(5, 10)`
- Add $5 \to +1, 10 \to -1$. Max $s = 2 \le 2 \implies$ **`true`**.

---

### Step 5: Output
$$
[\mathbf{true}, \; \mathbf{true}, \; \mathbf{true}, \; \mathbf{false}, \; \mathbf{true}, \; \mathbf{true}]
$$

---

## 4. Complete Execution Trace

| Call | Interval $[s, e)$ | Tentative Deltas Added | Timeline Sweep Running Sum $s$ | Peak $s$ | Conflict? | Final State Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `book(10, 20)` | $[10, 20)$ | $10: +1, 20: -1$ | $10 \to 1, 20 \to 0$ | $1$ | No | Commit |
| `book(50, 60)` | $[50, 60)$ | $50: +1, 60: -1$ | Max $s = 1$ | $1$ | No | Commit |
| `book(10, 40)` | $[10, 40)$ | $10: +2, 40: -1$ | $10 \to 2, 20 \to 1, 40 \to 0$ | $2$ | No | Commit |
| `book(5, 15)` | $[5, 15)$ | $5: +1, 15: -1$ | $5 \to 1, 10 \to \mathbf{3}$ | **$3$** | **Yes** | **Rollback & Reject** |
| `book(5, 10)` | $[5, 10)$ | $5: +1, 10: -1$ | $5 \to 1, 10 \to 2, 20 \to 1$ | $2$ | No | Commit |

---

## 5. Boundary Cases & Failure Modes

- **Triple Overlap at Single Point:** Detected immediately when $s$ hits 3.
- **Abutting Endpoints ($[5, 10)$ and $[10, 20)$):** At $t = 10$, $+1$ and $-1$ cancel out $\implies$ no false overlap.
- **Empty Calendar:** First booking always accepted.
- **Large Coordinates ($10^9$):** Coordinates used directly as keys in sorted map; space depends only on number of bookings $N \le 1000$.

---

## 6. Traps & Common Anti-Patterns

- **Not Rolling Back on Failure:** Leaving the tentative $+1$ and $-1$ in the calendar after returning `false` corrupts future queries. Always cleanly subtract the tentative deltas upon rejection.
- **Off-By-One on Endpoint:** Half-open interval $[start, end)$ ends strictly before $end$. Subtract at $end$, not $end - 1$.
- **Treating Double Bookings as Errors:** Unlike Calendar I where any overlap is rejected, Calendar II allows overlaps of 2 events. Only reject when concurrency $> 2$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - For each of the $N$ booking calls, iterates through at most $2N$ boundary points in the sorted map: $\mathcal{O}(N)$.
  - Total Time across $N$ calls: $\mathcal{O}(N^2)$. For $N = 1000$, total operations $\approx 10^6$, completing in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ memory to store the boundary keys in the sorted dictionary.