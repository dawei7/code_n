# Guided Example: Meeting Rooms II

We trace the step-by-step chronological event sweeping, min-heap room reallocation, and peak concurrency tracking on representative meeting schedules:

- **Input:** $\text{intervals} = [[0, 30], [5, 10], [15, 20]]$
- **Required output:** $2$ (At time $t = 5$, two meetings overlap simultaneously; meeting $[15, 20]$ reuses the room vacated at $t = 10$)
- **Disjoint Schedule Instance:** $\text{intervals} = [[7, 10], [2, 4]] \implies 1$ (Sequential meetings; single room suffices)
- **Touching Boundary Instance:** $\text{intervals} = [[1, 3], [3, 5]] \implies 1$ (Vacating at $t = 3$ allows immediate room reuse at $t = 3$)
- **Complete Concurrency Instance:** $\text{intervals} = [[1, 10], [2, 9], [3, 8]] \implies 3$ (Three nested overlapping meetings)

This instance demonstrates interval concurrency maximization, explains why the minimum rooms required is mathematically equivalent to the maximum number of simultaneous overlapping meetings, details the two-pointer sweep line over separated start and end times, and operates in $O(N \log N)$ time with $O(N)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given an array of meeting time intervals:
$$
\text{intervals} = [[0, 30], [5, 10], [15, 20]]
$$
Find the **minimum number of conference rooms** needed to host all meetings without conflict.

```text
Timeline:
t = 0:  Meeting [0, 30] begins               -> Room 1 occupied (1 active)
t = 5:  Meeting [5, 10] begins               -> Room 2 occupied (2 active)  <- PEAK!
t = 10: Meeting [5, 10] ends                 -> Room 2 freed    (1 active)
t = 15: Meeting [15, 20] begins (Reuses Room 2) -> Room 2 occupied (2 active)
t = 20: Meeting [15, 20] ends                -> Room 2 freed    (1 active)
t = 30: Meeting [0, 30] ends                 -> Room 1 freed    (0 active)

Peak Simultaneous Meetings = 2
```

### The Min-Rooms Equivalence Theorem
By Dilworth's Theorem for interval orders, the minimum number of rooms needed to partition an interval set without conflict is **strictly equal to the maximum number of mutually overlapping intervals at any instant in time** (the maximum clique size).
We do not need to simulate concrete physical room IDs; we only need to track the peak count of concurrently active meetings.

---

## 2. Conceptual Foundation & Invariants

### Method A: Separated Start/End Two-Pointer Sweep
Separate start times and end times into two independent sorted arrays:
$$
\text{starts} = \text{sorted}([I[0] \text{ for } I \in \text{intervals}]) = [0, 5, 15]
$$
$$
\text{ends} = \text{sorted}([I[1] \text{ for } I \in \text{intervals}]) = [10, 20, 30]
$$
Pointers $s = 0$ (next start) and $e = 0$ (next end).
While $s < N$:
1. If $\text{starts}[s] < \text{ends}[e]$:
   A new meeting begins before the earliest ongoing meeting finishes.
   Allocate a room: $\text{active\_rooms} \mathrel{+}= 1$.
   Advance start pointer: $s \leftarrow s + 1$.
2. Else ($\text{starts}[s] \ge \text{ends}[e]$):
   An ongoing meeting has ended! Its room becomes free for reuse.
   Release room: $\text{active\_rooms} \mathrel{-}= 1$.
   Advance end pointer: $e \leftarrow e + 1$.
3. Update peak: $\text{max\_rooms} = \max(\text{max\_rooms}, \text{active\_rooms})$.

*(Boundary Rule: If $\text{starts}[s] == \text{ends}[e]$, the meeting ends at the exact same instant the next begins. The room is freed immediately, so $\text{starts}[s] \ge \text{ends}[e]$ executes first, correctly avoiding phantom room allocations)*.

### Method B: Min-Heap of Active End Times
Sort intervals by start time. A min-heap stores the end times of rooms currently in use.
For interval $[s, e]$:
- If $\text{heap}[0] \le s$: a room has become available; pop $\text{heap}[0]$.
- Push $e$ onto the heap.
- Peak size of the heap is the answer.

> **Invariant.** At any moment in the two-pointer sweep, $\text{active\_rooms}$ is strictly equal to the number of ongoing meetings whose start has occurred ($\text{start} \le t$) but whose end has not yet arrived ($\text{end} > t$).

---

## 3. Step-by-Step Worked Execution

We trace the two-pointer sweep on $\text{intervals} = [[0, 30], [5, 10], [15, 20]]$ ($N = 3$):
Sorted starts: $\text{starts} = [0, 5, 15]$.
Sorted ends: $\text{ends} = [10, 20, 30]$.
Initial state: $s = 0, \quad e = 0, \quad \text{active\_rooms} = 0, \quad \text{max\_rooms} = 0$.

---

### Step 1: Compare $\text{starts}[0]$ vs $\text{ends}[0]$
- $\text{starts}[0] = 0, \quad \text{ends}[0] = 10$.
- $0 < 10 \implies$ Meeting starts!
- $\text{active\_rooms} \leftarrow 0 + 1 = \mathbf{1}$.
- $\text{max\_rooms} \leftarrow \max(0, 1) = \mathbf{1}$.
- Advance: $s \leftarrow 0 + 1 = 1$.

---

### Step 2: Compare $\text{starts}[1]$ vs $\text{ends}[0]$
- $\text{starts}[1] = 5, \quad \text{ends}[0] = 10$.
- $5 < 10 \implies$ Second meeting starts before the first ends!
- $\text{active\_rooms} \leftarrow 1 + 1 = \mathbf{2}$.
- $\text{max\_rooms} \leftarrow \max(1, 2) = \mathbf{2}$.
- Advance: $s \leftarrow 1 + 1 = 2$.

---

### Step 3: Compare $\text{starts}[2]$ vs $\text{ends}[0]$
- $\text{starts}[2] = 15, \quad \text{ends}[0] = 10$.
- $15 \ge 10 \implies$ Meeting ends at time $10$! Room freed.
- $\text{active\_rooms} \leftarrow 2 - 1 = \mathbf{1}$.
- Advance: $e \leftarrow 0 + 1 = 1$.
- (Notice: $s$ remains at index $2$).

---

### Step 4: Compare $\text{starts}[2]$ vs $\text{ends}[1]$
- $\text{starts}[2] = 15, \quad \text{ends}[1] = 20$.
- $15 < 20 \implies$ Third meeting starts at $15$ (occupies the vacated room).
- $\text{active\_rooms} \leftarrow 1 + 1 = \mathbf{2}$.
- $\text{max\_rooms} \leftarrow \max(2, 2) = \mathbf{2}$.
- Advance: $s \leftarrow 2 + 1 = 3$.

---

### Step 5: Termination
- $s = 3 == N$. All meeting starts have been scheduled!
- Final maximum simultaneous rooms: $\mathbf{2}$.

---

## 4. Complete Execution Trace

```text
intervals = [[0, 30], [5, 10], [15, 20]]
starts = [0, 5, 15]
ends   = [10, 20, 30]

Step 1: starts[0]=0  < ends[0]=10 -> Room allocated -> active=1, max=1, s=1
Step 2: starts[1]=5  < ends[0]=10 -> Room allocated -> active=2, max=2, s=2
Step 3: starts[2]=15 >= ends[0]=10 -> Room released   -> active=1, e=1
Step 4: starts[2]=15 < ends[1]=20 -> Room allocated -> active=2, max=2, s=3
s reaches end -> Finished. Max Rooms: 2
```

| Step | Chronological Action | Event Time | Active Comparison | $\text{active\_rooms}$ | Peak $\text{max\_rooms}$ | Next Pointers $(s, e)$ |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| **1** | Meeting Starts | $t = 0$ | $\text{starts}[0] < \text{ends}[0]$ ($0 < 10$) | 1 | 1 | $(1, 0)$ |
| **2** | Meeting Starts | $t = 5$ | $\text{starts}[1] < \text{ends}[0]$ ($5 < 10$) | **2** | **2 (Peak)** | $(2, 0)$ |
| **3** | Meeting Ends | $t = 10$ | $\text{starts}[2] \ge \text{ends}[0]$ ($15 \ge 10$) | 1 | 2 | $(2, 1)$ |
| **4** | Meeting Starts | $t = 15$ | $\text{starts}[2] < \text{ends}[1]$ ($15 < 20$) | **2** | **2** | $(3, 1)$ |
| **Finish** | All Starts Handled | - | $s = N = 3$ | - | **2** | Terminal |

---

## 5. Algorithmic Correctness

**Soundness.** Every time $\text{starts}[s] < \text{ends}[e]$, there are strictly $s - e + 1$ meetings currently in progress that have not yet reached their respective ending times. Since they all share the time instant $\text{starts}[s]$, they must occupy distinct conference rooms.

**Completeness.** Whenever a meeting ends ($\text{ends}[e] \le \text{starts}[s]$), that room is freed and made available for future meetings. The peak value $\text{max\_rooms}$ captures the exact maximum number of overlapping intervals across the continuous timeline $[0, \infty)$, guaranteeing that sufficient rooms are available at all times.

---

## 6. Traps This Instance Exposes

- **Sorting Starts and Ends Independently:** It may seem counterintuitive that start times and end times can be sorted separately, losing their original interval pairings. This is valid because conference rooms are fungible: any room that becomes free can be reused by any waiting meeting, regardless of which meeting vacated it!
- **Simultaneous Boundary Tie-Breaking:** If meeting A ends at time 10 and meeting B starts at time 10, does room count increase? No. The room is freed at 10 and reused at 10. The condition $\text{starts}[s] < \text{ends}[e]$ ensures that when $\text{starts}[s] == \text{ends}[e]$, the end event is processed first ($\ge$), preventing a false spike in active rooms.
- **Difference Array vs Two-Pointer Sweep:** An alternative approach uses a difference array over timeline coordinates. However, if meeting end times reach $10^6$ or $10^9$, allocating a dense array consumes excessive memory. Sorting the $N$ endpoints takes $O(N \log N)$ time and $O(N)$ space regardless of how large coordinates are.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log N)$, where $N$ is the number of intervals. Extracting and sorting `starts` and `ends` takes $2 \times O(N \log N)$ time. The two-pointer sweep advances $s$ and $e$ at most $N$ times each, taking $O(N)$ time. Total runtime is strictly bounded by $O(N \log N)$.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory to store the sorted `starts` and `ends` arrays.
