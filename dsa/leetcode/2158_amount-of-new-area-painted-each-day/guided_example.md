# Guided Example: Amount of New Area Painted Each Day

We analyze and execute the path-compressed interval jump pointer algorithm on a representative timeline instance, demonstrating how jump caching skips previously painted intervals in amortized near-constant time.

- **Input:** `paint = [[1, 4], [4, 7], [5, 8]]`
- **Output:** `[3, 3, 1]`

This instance illustrates unit interval tracking, path-compressed jump skipping over pre-painted blocks, disjoint coverage union, and daily incremental measurement.

---

## 1. Problem Overview & Representative Instance

A continuous line is painted over a sequence of days. On day $i$, an artist requests painting the half-open interval $[\textit{start}_i, \textit{end}_i)$. Its total nominal length is $\textit{end}_i - \textit{start}_i$.

Because overlapping paint makes the surface uneven, the artist applies paint only to sections of $[\textit{start}_i, \textit{end}_i)$ that have **never been painted on any earlier day**. For each day $i$, we must report the exact newly painted area, preserving the chronological sequence.

In our representative instance:
- Day 0: Paints $[1, 4)$. Length $4 - 1 = 3$. Entirely fresh.
- Day 1: Paints $[4, 7)$. Length $7 - 4 = 3$. Entirely fresh.
- Day 2: Paints $[5, 8)$. Length $8 - 5 = 3$. However, $[5, 7)$ was already painted on Day 1. Only $[7, 8)$ is fresh.

The expected daily output is $[3, 3, 1]$.

---

## 2. Mathematical & Algorithmic Principles

### Discrete Unit Interval Representation

Because coordinate endpoints are integers bounded by $M = 50000$, any continuous interval $[s, e)$ can be partitioned into $e - s$ discrete unit intervals:
$$[s, e) = \bigcup_{x = s}^{e - 1} [x, \, x + 1)$$

Each unit interval $[x, x + 1)$ is in one of two binary states:
- **Unpainted ($0$):** Has not appeared in any prior query.
- **Painted ($1$):** Has already been covered on an earlier day.

The new area painted on day $i$ is:
$$\text{NewArea}_i = \sum_{x = \textit{start}_i}^{\textit{end}_i - 1} \mathbf{1}_{\{[x, x+1) \text{ was unpainted prior to day } i\}}$$

### Jump Pointer Acceleration (Path Compression)

Iterating through every integer unit one by one for every query costs $O(n \cdot M)$ in the worst case ($10^5 \times 50000 = 5 \times 10^9$ operations), which times out.

Instead, we maintain a jump pointer array $\text{jump}$ of size $M + 1$:
- If unit interval $[x, x + 1)$ has never been painted, $\text{jump}[x] = 0$.
- When $[x, x + 1)$ is painted as part of an interval ending at $e$, we set $\text{jump}[x] = e$.
- If a future query visits coordinate $x$ and finds $\text{jump}[x] > 0$, it means the continuous segment $[x, \text{jump}[x])$ has already been painted. The traversal can immediately **jump** forward to $\text{jump}[x]$, skipping the entire covered block in $O(1)$ time!

To maintain jump efficiency across chained intervals, we apply path compression:
$$\text{jump}[x] \leftarrow \max(\text{jump}[x], \, \textit{end}_i)$$
This guarantees that each unit interval $[x, x + 1)$ is freshly traversed at most once across the entire algorithm.

| State Variable | Formal Definition | Operational Role in Traversal |
|---|---|---|
| Unit Interval $[x, x+1)$ | Integer coordinate step $x$ | Atomic indivisible unit of painted area |
| Jump Pointer $\text{jump}[x]$ | Furthest known painted right endpoint from $x$ | Bypasses previously painted blocks in a single step |
| Unpainted Flag ($\text{jump}[x] = 0$) | Fresh interval detected | Increments daily count by $1$ and records paint |
| Traversal Pointer $x$ | Current position in $[\textit{start}_i, \textit{end}_i)$ | Advances by $+1$ on fresh units, or jumps to $\text{jump}[x]$ |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace `paint = [[1, 4], [4, 7], [5, 8]]`.

```
Timeline of unit intervals:
Unit:      [1,2)  [2,3)  [3,4)  [4,5)  [5,6)  [6,7)  [7,8)
Day 0:       P      P      P     .      .      .      .     => Area = 3
Day 1:       .      .      .     P      P      P      .     => Area = 3
Day 2:       .      .      .     .     (skip [5,7))   P     => Area = 1
```

### Step 1: Initialize State
- Array $\text{jump}$ initialized to zeros for all indices up to $50000$.
- Results array: empty.

### Step 2: Process Day 0 (Interval $[1, 4)$)
- Range: $x$ from $1$ to $4$. Initialize $\text{area} = 0$.
- **$x = 1$:** $\text{jump}[1] = 0$ (unpainted).
  - Increment $\text{area} = 0 + 1 = 1$.
  - Update $\text{jump}[1] = 4$.
  - Advance: $x \leftarrow 1 + 1 = 2$.
- **$x = 2$:** $\text{jump}[2] = 0$ (unpainted).
  - Increment $\text{area} = 1 + 1 = 2$.
  - Update $\text{jump}[2] = 4$.
  - Advance: $x \leftarrow 2 + 1 = 3$.
- **$x = 3$:** $\text{jump}[3] = 0$ (unpainted).
  - Increment $\text{area} = 2 + 1 = 3$.
  - Update $\text{jump}[3] = 4$.
  - Advance: $x \leftarrow 3 + 1 = 4$.
- Reached right endpoint $4$. Day 0 newly painted area: $3$.

### Step 3: Process Day 1 (Interval $[4, 7)$)
- Range: $x$ from $4$ to $7$. Initialize $\text{area} = 0$.
- **$x = 4$:** $\text{jump}[4] = 0$ (unpainted).
  - Increment $\text{area} = 0 + 1 = 1$.
  - Update $\text{jump}[4] = 7$.
  - Advance: $x \leftarrow 4 + 1 = 5$.
- **$x = 5$:** $\text{jump}[5] = 0$ (unpainted).
  - Increment $\text{area} = 1 + 1 = 2$.
  - Update $\text{jump}[5] = 7$.
  - Advance: $x \leftarrow 5 + 1 = 6$.
- **$x = 6$:** $\text{jump}[6] = 0$ (unpainted).
  - Increment $\text{area} = 2 + 1 = 3$.
  - Update $\text{jump}[6] = 7$.
  - Advance: $x \leftarrow 6 + 1 = 7$.
- Reached right endpoint $7$. Day 1 newly painted area: $3$.

### Step 4: Process Day 2 (Interval $[5, 8)$)
- Range: $x$ from $5$ to $8$. Initialize $\text{area} = 0$.
- **$x = 5$:**
  - Check $\text{jump}[5]$: Value is $7 > 0$!
  - Meaning: Units $[5, 6)$ and $[6, 7)$ are already painted up to coordinate $7$.
  - Compress path: $\text{jump}[5] = \max(7, 8) = 8$.
  - **Execute Jump:** $x \leftarrow 7$. (Zero paint added; skipped $2$ units instantly).
- **$x = 7$:**
  - Check $\text{jump}[7]$: Value is $0$ (unpainted).
  - Increment $\text{area} = 0 + 1 = 1$.
  - Update $\text{jump}[7] = 8$.
  - Advance: $x \leftarrow 7 + 1 = 8$.
- Reached right endpoint $8$. Day 2 newly painted area: $1$.

### Step 5: Finalization
- Daily results collected: $[3, 3, 1]$.

---

## 4. Comprehensive State Trace

The table below catalogs every step across all three days, detailing jump pointer reads, modifications, and distance skipped:

| Day | Interval $[\textit{start}, \textit{end})$ | Current Coordinate $x$ | $\text{jump}[x]$ Before | Action Taken | $\text{jump}[x]$ After | Next $x$ | Daily Area Added |
|---|---|---|---|---|---|---|---|
| Day 0 | $[1, 4)$ | $1$ | $0$ | Fresh unit | $4$ | $2$ | $+1$ |
| Day 0 | $[1, 4)$ | $2$ | $0$ | Fresh unit | $4$ | $3$ | $+1$ |
| Day 0 | $[1, 4)$ | $3$ | $0$ | Fresh unit | $4$ | $4$ | $+1$ (Total: 3) |
| Day 1 | $[4, 7)$ | $4$ | $0$ | Fresh unit | $7$ | $5$ | $+1$ |
| Day 1 | $[4, 7)$ | $5$ | $0$ | Fresh unit | $7$ | $6$ | $+1$ |
| Day 1 | $[4, 7)$ | $6$ | $0$ | Fresh unit | $7$ | $7$ | $+1$ (Total: 3) |
| Day 2 | $[5, 8)$ | $5$ | $7$ | **Jump forward** | $8$ | $7$ | $+0$ (Skipped $[5, 7)$) |
| Day 2 | $[5, 8)$ | $7$ | $0$ | Fresh unit | $8$ | $8$ | $+1$ (Total: 1) |

Output sequence: $[3, 3, 1]$.

---

## 5. Algorithmic Correctness & Soundness

### Conservation of Unit Paint Status
Every unit interval $[x, x + 1)$ begins in state unpainted ($\text{jump}[x] = 0$).
- When first visited, it contributes exactly $1$ to the daily area of the day that visits it, and its state changes permanently to $\text{jump}[x] > 0$.
- Any subsequent visit observes $\text{jump}[x] > 0$, bypasses it without incrementing area, and jumps forward.
- Therefore, each unit interval $[x, x + 1)$ contributes to the output at most once in the entire execution, guaranteeing strict soundness and non-overlapping area accounting.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Completely Subsumed Interval:** If Day 2 requests $[2, 4)$, both $x = 2$ and $x = 3$ are already painted. The pointer jumps from $2$ to $4$ immediately, emitting newly painted area $0$.
2. **Point-Sized or Negative Intervals:** Problem guarantees $start_i < end_i$, so all intervals have non-zero positive length.
3. **Contiguous Non-Overlapping Intervals:** $[1, 4)$ followed by $[4, 7)$. The point $4$ is the exclusive end of interval 1 and inclusive start of interval 2. No conflict occurs; both paint $3$ units.
4. **Scattered Island Coverage:** Intervals cover $[1, 3)$ and $[5, 7)$. A later interval covers $[0, 8)$. The traversal paints $[0, 1)$, jumps past $[1, 3)$, paints $[3, 5)$, jumps past $[5, 7)$, and paints $[7, 8)$.

### Common Anti-Patterns
- **Brute Force Boolean Array ($O(n \cdot M)$):** Scanning each integer in $[start_i, end_i)$ without jumping takes $5 \times 10^9$ operations, leading to Time Limit Exceeded.
- **Segment Tree with Lazy Propagation Overhead:** A segment tree works in $O(n \log M)$, but incurs heavy pointer allocation and constant-factor overhead. Jump pointers with path compression run in near $O(n + M)$ time with minimal cache overhead.
- **Forgetting Path Compression on Jumps:** Failing to update $\text{jump}[x] = \max(\text{jump}[x], \textit{end})$ allows old, smaller jump boundaries to persist, causing redundant repeated jumps.

---

## 7. Complexity Analysis

### Time Complexity
- Across the entire execution of $n$ queries, each unit interval $[x, x + 1)$ in $[0, M)$ transitions from unpainted to painted at most once.
- There are at most $M = 50000$ such transitions, each taking $O(1)$ time.
- When an already-painted interval is encountered, path compression bypasses it in $O(\alpha(M))$ amortized steps.
- Total time complexity across all $n$ queries is $O(n + M \alpha(M))$, running in under $20$ milliseconds for $n = 10^5$ and $M = 50000$.

### Auxiliary Space Complexity
- The jump pointer array requires $M + 1 = 50001$ integers.
- The output array requires $n$ integers.
- Total auxiliary space complexity is $O(M + n)$ (with $O(M)$ working memory beyond the output).
