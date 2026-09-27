# Guided Example: The Skyline Problem

We trace the step-by-step sweep-line critical event generation, priority queue maximum height tracking, and lazy boundary eviction on representative multi-building silhouettes:

- **Input:** $\text{buildings} = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]$
- **Required output:** $[[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]$
- **Touching Buildings Instance:** $\text{buildings} = [[0, 2, 3], [2, 5, 3]] \implies [[0, 3], [5, 0]]$ (Contiguous equal-height segments merge into one)
- **Nested Building Instance:** Shorter building completely enclosed under a taller building produces zero additional key points
- **Separated Islands Instance:** Buildings separated by a gap return to ground level $[x_{\text{end}}, 0]$ before rising again

This instance demonstrates geometric sweep-line algorithms, explains event sorting conventions that prevent spurious zero-height drops when buildings touch, implements lazy heap deletion of expired right boundaries ($R \le x$), and achieves strictly $O(N \log N)$ runtime.

---

## 1. Instance & Teaching Goal

Given 5 rectangular buildings $[L_i, R_i, H_i]$:
1. $B_1 = [2, 9, 10]$
2. $B_2 = [3, 7, 15]$
3. $B_3 = [5, 12, 12]$
4. $B_4 = [15, 20, 10]$
5. $B_5 = [19, 24, 8]$

Extract the **skyline key points**: the coordinates $[x, y]$ marking the top-left vertex of each horizontal segment on the outer visible silhouette.
When viewed collectively:
- At $x = 2$: Building 1 starts, raising the skyline from $0$ to $10 \implies [2, 10]$.
- At $x = 3$: Building 2 starts, raising the skyline from $10$ to $15 \implies [3, 15]$.
- At $x = 5$: Building 3 starts with height $12$, but Building 2 ($H = 15$) is taller $\implies$ No change!
- At $x = 7$: Building 2 ends. The skyline drops to Building 3's height ($12$) $\implies [7, 12]$.
- At $x = 9$: Building 1 ends ($H = 10$). Building 3 ($H = 12$) is still active $\implies$ No change!
- At $x = 12$: Building 3 ends. No buildings active $\implies$ Drops to ground level $0 \implies [12, 0]$.
- At $x = 15$: Building 4 starts $\implies [15, 10]$.
- At $x = 19$: Building 5 starts ($H = 8$). Building 4 ($H = 10$) is taller $\implies$ No change!
- At $x = 20$: Building 4 ends. Skyline drops to Building 5 ($H = 8$) $\implies [20, 8]$.
- At $x = 24$: Building 5 ends $\implies [24, 0]$.

Skyline: $[[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]$.

---

## 2. Conceptual Foundation & Invariants

### The Sweep-Line Event Model
The visible skyline height can change **only at critical $x$-coordinates**: the left edge ($L$) where a building starts or the right edge ($R$) where it ends.

For each building $[L, R, H]$, generate two events:
1. **Left Boundary Event:** $(L, -H, R)$ (Using negative height $-H$ sorts taller buildings first and distinguishes start events from end events).
2. **Right Boundary Event:** $(R, 0, 0)$ (Signaling an evaluation point at coordinate $R$).

### Event Sorting Tie-Breaker Invariants:
When sorting events by coordinate $x$:
- If two left edges share the same $x$: process the **taller building first** (more negative $-H$), establishing the true peak immediately.
- If two right edges share the same $x$: process the shorter building first.
- If a left edge and a right edge share the same $x$: process the **left edge first** (since $-H < 0$), ensuring that continuous or touching buildings do not falsely dip to 0!

### Priority Queue Max-Height Tracking (with Lazy Deletion):
Store active building tuples $(-\text{height}, \text{right})$ in a min-heap:
- Ground baseline: always keep $(0, \infty)$ in the heap.
- At event coordinate $x$:
  - If it is a start event: push $(-H, R)$ into the heap.
  - **Lazy Eviction:** Pop all elements from the top of the heap whose right boundary has expired ($\text{right} \le x$).
  - Measure the current maximum visible height: $\text{curr\_height} = -\text{heap}[0][0]$.
  - If $\text{curr\_height} \ne \text{prev\_height}$:
    A key point is formed! Record $[x, \text{curr\_height}]$ and update $\text{prev\_height} \leftarrow \text{curr\_height}$.

> **Invariant.** At any coordinate $x$, after evicting all expired buildings from the heap top, $-\text{heap}[0][0]$ strictly equals the maximum height of all buildings covering the half-open interval $[x, x + \epsilon)$.

---

## 3. Step-by-Step Worked Execution

We trace the sweep-line across the events of $\text{buildings}$:

### Initial State:
- Heap contains ground level: $[(0, \infty)]$.
- $\text{prev\_height} = 0$.
- $\text{skyline} = []$.

---

### Event $x = 2$ (Start $B_1$, $H=10, R=9$):
- Push $(-10, 9)$ into heap.
- Heap top: $(-10, 9) \implies \text{curr\_height} = 10$.
- $10 \ne 0 \implies$ **Emit Key Point $[2, 10]$**.
- $\text{prev\_height} = 10$.

---

### Event $x = 3$ (Start $B_2$, $H=15, R=7$):
- Push $(-15, 7)$ into heap.
- Heap top: $(-15, 7) \implies \text{curr\_height} = 15$.
- $15 \ne 10 \implies$ **Emit Key Point $[3, 15]$**.
- $\text{prev\_height} = 15$.

---

### Event $x = 5$ (Start $B_3$, $H=12, R=12$):
- Push $(-12, 12)$ into heap.
- Heap top: $(-15, 7) \implies \text{curr\_height} = 15$.
- $15 == 15 \implies$ No change. No key point emitted.

---

### Event $x = 7$ (Evaluation / End $B_2$):
- Evict expired buildings: $(-15, 7)$ has $R = 7 \le 7 \implies$ Pop!
- New heap top: $(-12, 12) \implies \text{curr\_height} = 12$.
- $12 \ne 15 \implies$ **Emit Key Point $[7, 12]$**.
- $\text{prev\_height} = 12$.

---

### Event $x = 9$ (Evaluation / End $B_1$):
- Heap top is $(-12, 12)$ with $R = 12 > 9$ (Active).
- $(-10, 9)$ is buried inside the heap; lazy deletion skips it until it surfaces.
- $\text{curr\_height} = 12 == 12 \implies$ No change.

---

### Event $x = 12$ (Evaluation / End $B_3$):
- Evict expired buildings:
  - $(-12, 12)$ has $R = 12 \le 12 \implies$ Pop!
  - $(-10, 9)$ has $R = 9 \le 12 \implies$ Pop!
- New heap top: $(0, \infty) \implies \text{curr\_height} = 0$.
- $0 \ne 12 \implies$ **Emit Key Point $[12, 0]$**.
- $\text{prev\_height} = 0$.

---

### Event $x = 15$ (Start $B_4$, $H=10, R=20$):
- Push $(-10, 20)$.
- Heap top: $(-10, 20) \implies \text{curr\_height} = 10$.
- $10 \ne 0 \implies$ **Emit Key Point $[15, 10]$**.
- $\text{prev\_height} = 10$.

---

### Event $x = 19$ (Start $B_5$, $H=8, R=24$):
- Push $(-8, 24)$.
- Heap top: $(-10, 20) \implies \text{curr\_height} = 10 == 10$. No change.

---

### Event $x = 20$ (Evaluation / End $B_4$):
- Evict $(-10, 20)$ with $R = 20 \le 20 \implies$ Pop!
- New heap top: $(-8, 24) \implies \text{curr\_height} = 8$.
- $8 \ne 10 \implies$ **Emit Key Point $[20, 8]$**.
- $\text{prev\_height} = 8$.

---

### Event $x = 24$ (Evaluation / End $B_5$):
- Evict $(-8, 24)$ with $R = 24 \le 24 \implies$ Pop!
- New heap top: $(0, \infty) \implies \text{curr\_height} = 0$.
- $0 \ne 8 \implies$ **Emit Key Point $[24, 0]$**.
- $\text{prev\_height} = 0$.

All events processed.

---

## 4. Complete Execution Trace

```text
Buildings:
B1: [2, 9, 10]
B2: [3, 7, 15]
B3: [5, 12, 12]
B4: [15, 20, 10]
B5: [19, 24, 8]

Events Chronology:
x = 2:  Add B1(10) -> max: 10 -> [2, 10]
x = 3:  Add B2(15) -> max: 15 -> [3, 15]
x = 5:  Add B3(12) -> max: 15 -> (no change)
x = 7:  End B2(15) -> max: 12 -> [7, 12]
x = 9:  End B1(10) -> max: 12 -> (no change)
x = 12: End B3(12) -> max: 0  -> [12, 0]
x = 15: Add B4(10) -> max: 10 -> [15, 10]
x = 19: Add B5(8)  -> max: 10 -> (no change)
x = 20: End B4(10) -> max: 8  -> [20, 8]
x = 24: End B5(8)  -> max: 0  -> [24, 0]
```

| Event $x$ | Event Trigger | Active Max-Heap Top | New Visible Height | Previous Height | Key Point Emitted |
|:---:|:---|:---:|:---:|:---:|:---:|
| **2** | Start $B_1$ ($H=10$) | $(10, 9)$ | 10 | 0 | **`[2, 10]`** |
| **3** | Start $B_2$ ($H=15$) | $(15, 7)$ | 15 | 10 | **`[3, 15]`** |
| 5 | Start $B_3$ ($H=12$) | $(15, 7)$ | 15 | 15 | None |
| **7** | Evict $B_2$ ($R=7$) | $(12, 12)$ | 12 | 15 | **`[7, 12]`** |
| 9 | End $B_1$ ($R=9$) | $(12, 12)$ | 12 | 12 | None |
| **12** | Evict $B_3$ ($R=12$) | $(0, \infty)$ | 0 | 12 | **`[12, 0]`** |
| **15** | Start $B_4$ ($H=10$) | $(10, 20)$ | 10 | 0 | **`[15, 10]`** |
| 19 | Start $B_5$ ($H=8$) | $(10, 20)$ | 10 | 10 | None |
| **20** | Evict $B_4$ ($R=20$) | $(8, 24)$ | 8 | 10 | **`[20, 8]`** |
| **24** | Evict $B_5$ ($R=24$) | $(0, \infty)$ | 0 | 8 | **`[24, 0]`** |

---

## 5. Algorithmic Correctness

**Soundness.** A key point is emitted at coordinate $x$ if and only if the maximum visible building height changes from $\text{prev\_height}$ to $\text{curr\_height}$. The event ordering sorts start events before end events at the same coordinate, which guarantees that touching buildings of equal height maintain continuity without producing an erroneous zero-height dip.

**Completeness.** Since building heights are piecewise constant on intervals between boundary coordinates, any change in the skyline contour must occur at an endpoint $L_i$ or $R_i$. Because all $2N$ boundary events are processed in sorted order, no contour transition can be missed.

---

## 6. Traps This Instance Exposes

- **Touching Buildings of Equal Height:** For $[[0, 2, 3], [2, 5, 3]]$, processing the start of the second building before the end of the first maintains height $3$ across $x = 2$, correctly emitting $[[0, 3], [5, 0]]$ without an intermediate $[2, 0]$.
- **Immediate Eager Heap Deletion:** Deleting arbitrary elements from a binary heap takes $O(N)$ time, degrading total runtime to $O(N^2)$. Lazy deletion only removes expired elements when they reach the top of the heap, ensuring $O(\log N)$ amortized cost per operation.
- **Adjacent Duplicate Points:** Consecutive segments of equal height must not generate redundant points. Verifying $\text{curr\_height} \ne \text{prev\_height}$ automatically filters out redundant horizontal markers.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log N)$, where $N$ is the number of buildings. Creating and sorting the $2N$ events takes $O(N \log N)$ time. Each building is pushed into the heap once and popped at most once ($2N$ heap operations $\times O(\log N)$). Total runtime is strictly $O(N \log N)$.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary space for the event list and the priority queue.
