# Guided Example: Design Hit Counter

We trace the step-by-step chronological monotonic append logging (`ts.append(timestamp)`), 300-second sliding expiration boundary computation ($t_{\min} = timestamp - 300 + 1$), binary search prefix pruning (`bisect_left`), and active hit count extraction on representative hit stream sequences:

- **Input:** Sequence of operations:
  1. `hit(1)`
  2. `hit(2)`
  3. `hit(3)`
  4. `getHits(4)` $\implies 3$ (Window $[-295, 4]$ includes hits at $1, 2, 3$)
  5. `hit(300)`
  6. `getHits(300)` $\implies 4$ (Window $[1, 300]$ includes hits at $1, 2, 3, 300$)
  7. `getHits(301)` $\implies 3$ (Window $[2, 301]$ excludes hit at $1$ as expired! Hits at $2, 3, 300$ remain active)
- **Required output:** `[3, 4, 3]`
- **Consecutive Concurrent Hits:** Multiple hits at the exact same second are recorded and counted
- **Strict 300-Second Horizon:** A hit at $t = 1$ is valid up to and including $t = 300$; it expires at $t = 301$ ($301 - 300 + 1 = 2 > 1$)

This instance demonstrates sliding window query algorithms on monotonic time-series data, proves why binary search on sorted chronological arrays computes active counts in logarithmic time without deque eviction overhead, and analyzes performance characteristics.

---

## 1. Instance & Teaching Goal

Design a Hit Counter system that records hits and calculates the total hits received in the past 5 minutes (the most recent 300 seconds):
- `hit(timestamp)`: Records a hit at integer second `timestamp`. Timestamps arrive in monotonically non-decreasing order.
- `getHits(timestamp)`: Returns the total number of hits recorded in the inclusive time window:
  $$
  [\text{timestamp} - 300 + 1, \quad \text{timestamp}]
  $$

```text
Timeline of Hits:
t = 1:   hit(1)
t = 2:   hit(2)
t = 3:   hit(3)
t = 4:   getHits(4)   -> Window [-295, 4]   -> Hits at {1, 2, 3}       -> Total = 3
t = 300: hit(300)
t = 300: getHits(300) -> Window [1, 300]    -> Hits at {1, 2, 3, 300}  -> Total = 4
t = 301: getHits(301) -> Window [2, 301]    -> Hit at t=1 expired!     -> Total = 3
```

---

## 2. Conceptual Foundation & Invariants

### 1. Monotonic Dynamic Array (`ts`)
Because incoming timestamps are guaranteed to arrive in non-decreasing order ($t_1 \le t_2 \le \dots$), the array `self.ts` is **inherently sorted at all times**:
- `hit(timestamp)` executes in $O(1)$ amortized time by appending directly to the end of `self.ts`.

### 2. Active Window Bisection on `getHits(timestamp)`:
All recorded hits in `self.ts` occurred at or before the current query `timestamp`.
To determine how many hits fall within the 300-second window, we identify the earliest timestamp that has **not yet expired**:
$$
\text{cutoff} = \text{timestamp} - 300 + 1
$$
- `bisect_left(self.ts, cutoff)` finds the lowest index $i$ where $\text{ts}[i] \ge \text{cutoff}$.
- All entries $\text{ts}[0 \dots i - 1]$ have expired ($< \text{cutoff}$).
- All entries $\text{ts}[i \dots \text{len}(ts) - 1]$ are active.
- The active hit count is simply:
  $$
  \text{Active Hits} = \text{len}(\text{self.ts}) - i
  $$

> **Invariant.** Array `self.ts` remains monotonically non-decreasing. For any cutoff $C$, `bisect_left(self.ts, C)` partitions the list into expired hits ($< C$) and active hits ($\ge C$).

---

## 3. Step-by-Step Worked Execution

We trace the operational sequence:

---

### Step 1: Record Early Hits (`hit(1), hit(2), hit(3)`)
- Append timestamps to `ts`:
  $$
  ts = [1, \; 2, \; 3]
  $$

---

### Step 2: Query `getHits(4)`
- Compute window cutoff:
  $$
  \text{cutoff} = 4 - 300 + 1 = -295
  $$
- Binary search:
  $$
  i = \text{bisect\_left}([1, 2, 3], \; -295) = \mathbf{0}
  $$
- Compute active count:
  $$
  \text{len}(ts) - i = 3 - 0 = \mathbf{3}
  $$

---

### Step 3: Record Boundary Hit (`hit(300)`)
- Append timestamp $300$:
  $$
  ts = [1, \; 2, \; 3, \; \mathbf{300}]
  $$

---

### Step 4: Query `getHits(300)`
- Compute window cutoff:
  $$
  \text{cutoff} = 300 - 300 + 1 = \mathbf{1}
  $$
- Binary search:
  $$
  i = \text{bisect\_left}([1, 2, 3, 300], \; 1) = \mathbf{0}
  $$
- Compute active count:
  $$
  \text{len}(ts) - i = 4 - 0 = \mathbf{4}
  $$
- *Observation: The hit at $t = 1$ is still active because $1 \ge 1$.*

---

### Step 5: Query `getHits(301)` — Expiration Triggered!
- Compute window cutoff:
  $$
  \text{cutoff} = 301 - 300 + 1 = \mathbf{2}
  $$
- Binary search:
  $$
  i = \text{bisect\_left}([1, 2, 3, 300], \; 2) = \mathbf{1}
  $$
- Elements at indices $< 1$ (namely $ts[0] = 1$) are strictly $< 2$ and expired!
- Compute active count:
  $$
  \text{len}(ts) - i = 4 - 1 = \mathbf{3}
  $$
- *Hits at $t = 2, 3, 300$ are active; hit at $t = 1$ is excluded.*

---

## 4. Complete Execution Trace

```text
HitCounter Operations:
hit(1)   -> ts = [1]
hit(2)   -> ts = [1, 2]
hit(3)   -> ts = [1, 2, 3]

getHits(4):
  cutoff = 4 - 300 + 1 = -295
  bisect_left(ts, -295) = 0 -> active = 3 - 0 = 3

hit(300) -> ts = [1, 2, 3, 300]

getHits(300):
  cutoff = 300 - 300 + 1 = 1
  bisect_left(ts, 1) = 0 -> active = 4 - 0 = 4

getHits(301):
  cutoff = 301 - 300 + 1 = 2
  bisect_left(ts, 2) = 1 -> active = 4 - 1 = 3

Result Stream: [3, 4, 3]
```

| Operation | Input Timestamp | Cutoff ($t - 299$) | Binary Search Index $i$ | Expired Elements | Active Hits Count | Emitted Result |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `hit(1)` | 1 | - | - | - | - | - |
| `hit(2)` | 2 | - | - | - | - | - |
| `hit(3)` | 3 | - | - | - | - | - |
| **`getHits(4)`** | 4 | $-295$ | 0 | None | $3 - 0 = 3$ | **3** |
| `hit(300)` | 300 | - | - | - | - | - |
| **`getHits(300)`** | 300 | $1$ | 0 | None | $4 - 0 = 4$ | **4** |
| **`getHits(301)`** | 301 | $2$ | 1 | $ts[0] = 1$ | $4 - 1 = 3$ | **3** |

---

## 5. Algorithmic Correctness

**Soundness.** Because timestamps arrive in non-decreasing order, `self.ts` is guaranteed to be sorted. The binary search `bisect_left` locates the unique partition boundary where all elements to the left are $< cutoff$ and all elements to the right are $\ge cutoff$. Since the window is defined as $[timestamp - 299, timestamp]$, every element at or after index $i$ occurred within the required 300-second interval.

**Completeness.** No active hit is omitted because `bisect_left` returns the earliest index satisfying $\text{ts}[i] \ge cutoff$. Duplicate timestamps occurring at the same second are clustered together, and `bisect_left` correctly identifies the first occurrence among duplicate values.

---

## 6. Traps This Instance Exposes

- **Window Interval Off-by-One:** The past 5 minutes means exactly 300 seconds. If a hit occurred at $t = 1$, it is still valid at $t = 300$ ($300 - 1 = 299 < 300$). It expires at $t = 301$ ($301 - 1 = 300 \ge 300$). The formula `timestamp - 300 + 1` correctly captures this boundary.
- **Concurrent Hits at Same Second:** If 10,000 hits occur at the same second, logging individual integers can lead to high memory consumption. For huge scale, a circular bucket array of length 300 storing `(timestamp, count)` pairs bounds space to $O(300) = O(1)$.
- **`bisect_left` vs `bisect_right`:** We must include elements that are equal to the cutoff. `bisect_left` places the pointer before the first instance of `cutoff`, ensuring hits with timestamp equal to `cutoff` are counted as active.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `hit(timestamp)`: $O(1)$ amortized time for dynamic list append.
  - `getHits(timestamp)`: $O(\log N)$ where $N$ is the total number of hits recorded in `self.ts`, using binary search `bisect_left`.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory to store the array of hit timestamps.