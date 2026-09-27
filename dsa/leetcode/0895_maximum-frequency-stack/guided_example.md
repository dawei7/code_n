# Guided Example: Maximum Frequency Stack

We trace the step-by-step priority tuple hierarchy $(\text{frequency}, \text{recency timestamp}, \text{value})$, frequency map tracking, tie-breaking by LIFO recency, and maximum-frequency element extraction on representative operation sequences:

- **Input Operations:**
  $$
  [\text{push}(5), \text{push}(7), \text{push}(5), \text{push}(7), \text{push}(4), \text{push}(5), \text{pop}(), \text{pop}(), \text{pop}(), \text{pop}()]
  $$
- **Required output:** `[5, 7, 5, 4]`
  - Maximum frequency stack rules:
    - `push(val)`: Inserts $val$ onto the stack.
    - `pop()`: Removes and returns the **most frequent element** currently in the stack.
    - **Tie-breaker:** If two or more elements share the same highest frequency, return the element that was **pushed most recently** (standard LIFO stack order).
    - Sequence trace:
      - Push sequence: $5, 7, 5, 7, 4, 5$.
      - Frequencies before popping:
        - $5 \implies$ count $3$ (pushed at timestamps 1, 3, 6).
        - $7 \implies$ count $2$ (pushed at timestamps 2, 4).
        - $4 \implies$ count $1$ (pushed at timestamp 5).
      - **Pop 1:** Highest frequency is $3$ (held by $5$) $\implies$ returns **`5`**. Frequency of $5$ drops to $2$.
      - **Pop 2:** Highest frequency is $2$ (tie between $7$ and $5$).
        - Element $7$ was pushed at timestamp 4.
        - Element $5$ was pushed at timestamp 3.
        - Since $4 > 3$, element $7$ is more recent $\implies$ returns **`7`**. Frequency of $7$ drops to $1$.
      - **Pop 3:** Highest frequency is $2$ (held only by $5$) $\implies$ returns **`5`**. Frequency of $5$ drops to $1$.
      - **Pop 4:** Highest frequency is $1$ (tie between $4$, $7$, and $5$).
        - Timestamps: $4$ at 5, $7$ at 2, $5$ at 1.
        - Most recent is $4$ (timestamp 5) $\implies$ returns **`4`**.
      - Result: **`[5, 7, 5, 4]`**.
- **The Priority Tuple & Frequency Bucket Invariant:**
  - **The Two-Tier Priority Rule:**
    - Priority 1 (Primary): Maximum occurrence frequency $f$.
    - Priority 2 (Secondary Tie-breaker): Maximum push timestamp $t$ (most recent arrival).
    - Every push operation records a state tuple:
      $$
      \text{Entry} = (f, \; t, \; val)
      $$
      where $f = cnt[val]$ after incrementing, and $t$ is the monotonically increasing global counter.
  - **Heap Priority Invariant:**
    - Storing entries in a max-heap keyed by $(-f, -t, val)$ guarantees that `heappop()` will extract precisely the item with the greatest frequency, with exact LIFO tie-breaking on simultaneous peaks!
    - When an element is popped, its current frequency in $cnt$ decrements by $1$.

---

## 1. Instance & Teaching Goal

Given the push sequence $[5, 7, 5, 7, 4, 5]$ followed by 4 pops, trace how frequency and timestamp keys resolve each pop.

```text
Timestamps and Entries Pushed:
  t = 1: push(5) -> freq = 1. Tuple: (1, 1, 5)
  t = 2: push(7) -> freq = 1. Tuple: (1, 2, 7)
  t = 3: push(5) -> freq = 2. Tuple: (2, 3, 5)
  t = 4: push(7) -> freq = 2. Tuple: (2, 4, 7)
  t = 5: push(4) -> freq = 1. Tuple: (1, 5, 4)
  t = 6: push(5) -> freq = 3. Tuple: (3, 6, 5)

Max-Heap Ordered by (freq DESC, timestamp DESC):
  1. (3, 6, 5) -> Pop 1 returns 5! (freq 3)
  2. (2, 4, 7) -> Pop 2 returns 7! (freq 2, timestamp 4 beats 3)
  3. (2, 3, 5) -> Pop 3 returns 5! (freq 2)
  4. (1, 5, 4) -> Pop 4 returns 4! (freq 1, timestamp 5 beats 2 and 1)
```

The teaching goal is to justify how pairing frequency with push-order sequence numbers reduces dual-criteria priority selection to standard lexicographical comparisons.

---

## 2. Conceptual Foundation & Invariants

### 1. State Structures:
- Frequency map: $cnt[v] \to \mathbb{Z}_{\ge 0}$.
- Clock counter: $ts \in \mathbb{N}$ initialized to $0$.
- Priority queue entries: $(-cnt[v], -ts, v)$.

### 2. Operation Specifications:
$$
\text{push}(v): \quad ts \leftarrow ts + 1, \quad cnt[v] \leftarrow cnt[v] + 1, \quad \text{heap.push}((-cnt[v], -ts, v))
$$
$$
\text{pop}(): \quad (f, t, v) \leftarrow \text{heap.pop}(), \quad cnt[v] \leftarrow cnt[v] - 1, \quad \text{return } v
$$

---

## 3. Step-by-Step Worked Execution

We trace the full sequence of operations:

---

### Phase 1: Push Operations
- **Op 1 (`push(5)`):** $ts = 1, cnt[5] = 1$. Push $(1, 1, 5)$.
- **Op 2 (`push(7)`):** $ts = 2, cnt[7] = 1$. Push $(1, 2, 7)$.
- **Op 3 (`push(5)`):** $ts = 3, cnt[5] = 2$. Push $(2, 3, 5)$.
- **Op 4 (`push(7)`):** $ts = 4, cnt[7] = 2$. Push $(2, 4, 7)$.
- **Op 5 (`push(4)`):** $ts = 5, cnt[4] = 1$. Push $(1, 5, 4)$.
- **Op 6 (`push(5)`):** $ts = 6, cnt[5] = 3$. Push $(3, 6, 5)$.

Active frequency counts: $cnt[5] = 3, cnt[7] = 2, cnt[4] = 1$.

---

### Phase 2: Pop Operations

---

#### Step 1: First `pop()`
- Heap entries ranked by $(-f, -t)$:
  - Peak entry: $(f=3, t=6, val=\mathbf{5})$.
- Pop $(3, 6, 5)$.
- Decrement count: $cnt[5] \leftarrow 3 - 1 = 2$.
- **Return: `5`**.

---

#### Step 2: Second `pop()`
- Remaining candidates at top of heap:
  - $(f=2, t=4, val=\mathbf{7})$
  - $(f=2, t=3, val=5)$
- Both have frequency $2$.
- Secondary comparison: timestamp $4 > 3$.
- Peak entry: $(2, 4, 7)$.
- Pop $(2, 4, 7)$.
- Decrement count: $cnt[7] \leftarrow 2 - 1 = 1$.
- **Return: `7`**.

---

#### Step 3: Third `pop()`
- Remaining candidate with frequency $2$:
  - $(f=2, t=3, val=\mathbf{5})$.
- Pop $(2, 3, 5)$.
- Decrement count: $cnt[5] \leftarrow 2 - 1 = 1$.
- **Return: `5`**.

---

#### Step 4: Fourth `pop()`
- Remaining candidates all have frequency $1$:
  - $(f=1, t=5, val=\mathbf{4})$
  - $(f=1, t=2, val=7)$
  - $(f=1, t=1, val=5)$
- Tie-breaker on timestamp: $\max(5, 2, 1) = 5$.
- Peak entry: $(1, 5, 4)$.
- Pop $(1, 5, 4)$.
- Decrement count: $cnt[4] \leftarrow 1 - 1 = 0$.
- **Return: `4`**.

---

### Termination:
Popped sequence: `[5, 7, 5, 4]`.

---

## 4. Complete Execution Trace

| Step | Operation | Value | Timestamp $ts$ | New Element Freq $cnt[v]$ | Entry Added to Pool $(f, t, v)$ | Action / Extracted Element | Current $cnt$ Map |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---|
| $1$ | `push` | $5$ | $1$ | $1$ | $(1, 1, 5)$ | Stored | $\{5: 1\}$ |
| $2$ | `push` | $7$ | $2$ | $1$ | $(1, 2, 7)$ | Stored | $\{5: 1, 7: 1\}$ |
| $3$ | `push` | $5$ | $3$ | $2$ | $(2, 3, 5)$ | Stored | $\{5: 2, 7: 1\}$ |
| $4$ | `push` | $7$ | $4$ | $2$ | $(2, 4, 7)$ | Stored | $\{5: 2, 7: 2\}$ |
| $5$ | `push` | $4$ | $5$ | $1$ | $(1, 5, 4)$ | Stored | $\{5: 2, 7: 2, 4: 1\}$ |
| $6$ | `push` | $5$ | $6$ | $3$ | $(3, 6, 5)$ | Stored | $\{5: 3, 7: 2, 4: 1\}$ |
| **$7$** | **`pop`** | — | — | — | — | **Extract $(3, 6, 5) \implies \mathbf{5}$** | $\{5: 2, 7: 2, 4: 1\}$ |
| **$8$** | **`pop`** | — | — | — | — | **Extract $(2, 4, 7) \implies \mathbf{7}$** | $\{5: 2, 7: 1, 4: 1\}$ |
| **$9$** | **`pop`** | — | — | — | — | **Extract $(2, 3, 5) \implies \mathbf{5}$** | $\{5: 1, 7: 1, 4: 1\}$ |
| **$10$** | **`pop`** | — | — | — | — | **Extract $(1, 5, 4) \implies \mathbf{4}$** | $\{5: 1, 7: 1, 4: 0\}$ |

---

## 5. Boundary Cases & Failure Modes

- **Single Push Followed by Pop:** Pushes $(1, 1, v)$ and immediately pops $v$. Frequency returns to $0$.
- **All Unique Elements (Frequencies all $1$):** Degrades cleanly to a standard LIFO stack, popping in reverse push order based on timestamps.
- **Identical Elements Pushed Repeatedly:** Frequencies climb $1, 2, 3 \dots$. Pops remove the highest frequency first, descending in order.

---

## 6. Traps & Common Anti-Patterns

- **Storing Only One Entry Per Element in the Heap:** Updating an existing heap entry's frequency in-place requires an $\mathcal{O}(N)$ heap search or complex indexed priority queue. Pushing a new entry $(f, t, v)$ on every push naturally layers past instances without mutation.
- **Neglecting the Timestamp Tie-Breaker:** Using only frequency causes non-deterministic pop behavior when frequencies collide, violating the required LIFO tie-breaking guarantee.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `push(val)`: Hash map update $\mathcal{O}(1)$ + heap insertion $\mathcal{O}(\log N)$.
  - `pop()`: Heap extraction $\mathcal{O}(\log N)$ + hash map decrement $\mathcal{O}(1)$.
  - Total Time: strictly $\mathcal{O}(\log N)$ per operation (or $\mathcal{O}(1)$ amortized using frequency bucket stacks). For $2 \times 10^4$ operations, finishes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - Frequency hash map and heap storing $N$ push entries: $\mathcal{O}(N)$ space.
