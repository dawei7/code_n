# Guided Example: Split Array into Consecutive Subsequences

We trace the step-by-step greedy chain extension protocol, terminal endpoint dictionary mapping ($d[v]$ holding min-heaps of chain lengths), shortest-chain attachment heuristic ($\min(d[v-1]) + 1 \to d[v]$), new chain seeding ($[1] \to d[v]$), minimum length constraint validation ($\forall L: L \ge 3$), and sequence feasibility determination on representative non-decreasing arrays:

- **Input:** $nums = [1, 2, 3, 3, 4, 5]$
- **Required output:** `true`
  - Partition requirements:
    1. Each subsequence must consist of strictly consecutive integers ($x, x+1, x+2, \dots$).
    2. Every created subsequence must achieve a final length of **at least 3** ($L \ge 3$).
    3. All elements from $nums$ must be consumed.
- **Shortest-Chain Greedy Attachment Invariant:**
  - **The Urgency Metric:**
    - If we have multiple active consecutive subsequences ending at $v - 1$, which one should receive the new element $v$?
    - Suppose one subsequence has length 1 ($[v-1]$) and another has length 4 ($[v-4 \dots v-1]$).
    - The subsequence of length 1 is **at extreme risk of violating the $\ge 3$ length rule**! The subsequence of length 4 is already valid ($\ge 3$).
    - Therefore, the optimal greedy strategy is to **always attach $v$ to the shortest available subsequence ending at $v - 1$**!
  - **Data Structure Architecture:**
    - Maintain a dictionary $d$ where $d[val]$ is a min-heap storing the lengths of all active subsequences ending at $val$.
    - For each incoming number $v \in nums$:
      - If $d[v - 1]$ is non-empty:
        - Extract the shortest length $L = \text{pop\_min}(d[v - 1])$.
        - Extend this sequence by $v$: its length becomes $L + 1$, and it now ends at $v$.
        - Insert $L + 1$ into $d[v]$.
      - If $d[v - 1]$ is empty:
        - We cannot extend any existing sequence; start a brand new sequence consisting of $[v]$.
        - Insert length $1$ into $d[v]$.
  - **Final Audit:**
    - After all numbers have been assigned, inspect every length stored in all buckets.
    - If any remaining length is $< 3$ (i.e. length 1 or 2), partition is impossible $\implies \mathbf{False}$.
    - If all lengths are $\ge 3 \implies \mathbf{True}$.
- **Step-by-Step Worked Execution Trace on $[1, 2, 3, 3, 4, 5]$:**
  - Initialize empty endpoint dictionary: $d = \{\}$.
  - **Process $v = 1$:**
    - Check $d[0]$: empty.
    - Start new sequence ending at 1 with length 1:
      $$
      d[1] = [1]
      $$
  - **Process $v = 2$:**
    - Check $d[1]$: has length 1.
    - Pop 1 from $d[1]$ ($d[1]$ becomes empty).
    - Extend sequence: new length is $1 + 1 = 2$, ending at 2:
      $$
      d[2] = [2]
      $$
  - **Process First $v = 3$:**
    - Check $d[2]$: has length 2.
    - Pop 2 from $d[2]$.
    - Extend sequence: new length is $2 + 1 = 3$, ending at 3:
      $$
      d[3] = [3]
      $$
    - Note: This sequence $[1, 2, 3]$ has now reached the required length $\ge 3$!
  - **Process Second $v = 3$:**
    - Check $d[2]$: empty! (No active sequence ends at 2).
    - Cannot extend any sequence; must start a second new sequence with $[3]$:
      $$
      d[3] = [1, \; 3]
      $$
    - Subsequences ending at 3: one of length 1 (the new $[3]$), one of length 3 (the old $[1, 2, 3]$).
  - **Process $v = 4$:**
    - Check $d[3]$: contains lengths $[1, 3]$.
    - Pop the **shortest** length: $\min(1, 3) = \mathbf{1}$.
    - (Attaching 4 to the length-1 sequence upgrades it to length 2: $[3, 4]$!).
    - Update endpoints:
      $$
      d[3] = [3], \quad d[4] = [2]
      $$
  - **Process $v = 5$:**
    - Check $d[4]$: contains length 2.
    - Pop 2 from $d[4]$.
    - Extend sequence: new length is $2 + 1 = \mathbf{3}$, ending at 5.
    - Upgrades $[3, 4]$ into $[3, 4, 5]$:
      $$
      d[4] = [], \quad d[5] = [3]
      $$
  - **Step 6: Final Verification:**
    - All numbers from array consumed.
    - Remaining active subsequences:
      - In $d[3]$: one sequence of length $\mathbf{3}$ ($[1, 2, 3]$)
      - In $d[5]$: one sequence of length $\mathbf{3}$ ($[3, 4, 5]$)
    - All other buckets are empty.
    - Every subsequence has length $\ge 3$.
    - Returns **`true`**.
- **Impossible Partition Instance ($nums = [1, 2, 3, 4, 4, 5]$):**
  - Sequence 1 forms $[1, 2, 3, 4]$.
  - Second 4 starts new sequence of length 1: $[4]$.
  - 5 extends the second sequence to length 2: $[4, 5]$.
  - Resulting subsequences: $[1, 2, 3, 4]$ (length 4) and $[4, 5]$ (length 2).
  - Since length $2 < 3$, partition fails $\implies$ Returns **`false`**.

This instance demonstrates greedy heuristic scheduling on ordered integer streams, mathematically proves why prioritising minimal-length prefix chains prevents premature termination defects, and derives $O(N \log K)$ runtime and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a non-decreasing sorted array $nums$:
Split $nums$ into consecutive increasing subsequences of **length $\ge 3$**.

```text
nums = [ 1, 2, 3, 3, 4, 5 ]

Step 1: 1 -> starts seq A: [ 1 ]             (len 1)
Step 2: 2 -> extends seq A: [ 1, 2 ]          (len 2)
Step 3: 3 -> extends seq A: [ 1, 2, 3 ]       (len 3, valid!)
Step 4: 3 -> cannot extend, starts seq B: [ 3 ] (len 1)
Step 5: 4 -> attaches to SHORTEST seq (seq B): [ 3, 4 ] (len 2)
Step 6: 5 -> attaches to seq B: [ 3, 4, 5 ]    (len 3, valid!)

Two valid subsequences of length 3: [1, 2, 3] and [3, 4, 5].
Result: true
```

### The Invariant of Shortest-Chain Priority
- Attaching $v$ to the shortest existing sequence ending at $v - 1$ gives endangered short sequences the highest priority to reach length $\ge 3$.

---

## 2. Conceptual Foundation & Invariants

### 1. The Greedy Decision Rule:
For each $v \in nums$:
- If $d[v - 1]$ has items:
  $$
  L = \text{pop\_min}(d[v - 1])
  $$
  $$
  \text{push}(d[v], \; L + 1)
  $$
- Else:
  $$
  \text{push}(d[v], \; 1)
  $$

### 2. The Acceptance Invariant:
$$
\forall v, \; \forall L \in d[v]: \quad L \ge 3
$$

> **Bottleneck Slackness Invariant.** In any optimal feasible partition, prioritizing the extension of sequences with the smallest current cardinality maximizes the probability that all active chains satisfy the boundary threshold constraint $L \ge 3$.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 2, 3, 3, 4, 5]$:

---

### Step 1: Elements 1, 2, 3
- $1 \implies d[1] = [1]$.
- $2 \implies d[1] = [], d[2] = [2]$.
- $3 \implies d[2] = [], d[3] = [3]$.

---

### Step 2: Second 3
- $d[2]$ empty $\implies$ start new: $d[3] = [1, 3]$.

---

### Step 3: Element 4
- $d[3]$ has lengths $1$ and $3$. Pick shortest: $1$.
- New length $1 + 1 = 2 \implies d[3] = [3], d[4] = [2]$.

---

### Step 4: Element 5
- $d[4]$ has length 2.
- New length $2 + 1 = 3 \implies d[4] = [], d[5] = [3]$.

---

### Step 5: Final Check
- $d[3]$ has $3 \ge 3$.
- $d[5]$ has $3 \ge 3$.
- Return **`true`**.

---

## 4. Complete Execution Trace

| Incoming Value $v$ | Available at $v - 1$ | Action Taken | Sequence Modified | Resulting $d[v]$ |
|:---:|:---:|:---:|:---:|:---:|
| $1$ | $d[0] = \emptyset$ | Start new sequence | `[1]` (len 1) | $d[1] = [1]$ |
| $2$ | $d[1] = [1]$ | Extend len 1 | `[1, 2]` (len 2) | $d[2] = [2]$ |
| $3$ (first) | $d[2] = [2]$ | Extend len 2 | `[1, 2, 3]` (len 3) | $d[3] = [3]$ |
| **$3$ (second)** | $d[2] = \emptyset$ | **Start new sequence** | **`[3]` (len 1)** | **$d[3] = [1, 3]$** |
| $4$ | $d[3] = [1, 3]$ | **Extend shortest (len 1)** | `[3, 4]` (len 2) | $d[4] = [2]$ |
| $5$ | $d[4] = [2]$ | Extend len 2 | `[3, 4, 5]` (len 3) | $d[5] = [3]$ |
| **Audit** | All heaps | All $L \ge 3$ | Valid partition | **`true`** |

---

## 5. Boundary Cases & Failure Modes

- **Length $< 3$ Array ($[1, 2]$):** Can never form length $\ge 3 \implies$ returns `false`.
- **Large Frequency at Single Value ($[1, 1, 1, 2, 2, 2, 3, 3, 3]$):** Spawns 3 separate sequences simultaneously; all reach length 3 $\implies$ `true`.
- **Gapped Input ($[1, 2, 3, 6, 7, 8]$):** Forms two disjoint valid sequences $\implies$ `true`.
- **Dead End ($[1, 2, 3, 4, 4, 5]$):** Leaves $[4, 5]$ stuck at length 2 $\implies$ `false`.

---

## 6. Traps & Common Anti-Patterns

- **Extending the Longest Chain First:** If you attach 4 to $[1, 2, 3]$ (making it length 4) instead of $[3]$ (which needed it), $[3]$ is starved and fails the length requirement. Always attach to the **shortest** chain.
- **Frequency Map Counting Without Heap ($O(N)$ Greedy):** While count-based greedy works, using min-heaps handles arbitrary overlapping sequences without complicated case analyses.
- **Checking Only Total Count:** Having $N \ge 3$ elements is not sufficient; the consecutive continuity constraint must be respected.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - For each element, heap operations (`heappop`, `heappush`) take $\mathcal{O}(\log K)$ where $K$ is the number of simultaneous sequences ending at that value ($K \le N$).
  - Total Time: $\mathcal{O}(N \log K)$. For $N = 10^4$, completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to store the heaps across all dictionary keys.
