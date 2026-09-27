# Guided Example: LFU Cache

We trace the step-by-step doubly linked list frequency bucket organization, hash map node routing ($O(1)$ key lookup), access frequency promotion ($freq \to freq + 1$), minimum frequency tracking ($min\_freq$), and least recently used tie-breaking eviction ($remove\_last()$) on representative cache operations:

- **Input:**
  - Initial configuration: `capacity = 2`
  - Sequence of operations:
    1. `put(1, 1)`
    2. `put(2, 2)`
    3. `get(1)`
    4. `put(3, 3)` (triggers eviction)
    5. `get(2)`
    6. `get(3)`
    7. `put(4, 4)` (triggers eviction with frequency tie-break)
    8. `get(1)`
    9. `get(3)`
    10. `get(4)`
- **Required output:** `[null, null, null, 1, null, -1, 3, null, -1, 3, 4]`
- **Execution trace:**
  - Initialize: $map = \{\}, \; freq\_map = \{\}, \; min\_freq = 0, \; capacity = 2$
  - **Op 1: `put(1, 1)`:**
    - Node $(k=1, v=1, freq=1)$ created.
    - Insert into $freq\_map[1]$: $[(1)]$.
    - Update: $min\_freq \leftarrow 1$.
  - **Op 2: `put(2, 2)`:**
    - Node $(k=2, v=2, freq=1)$ created.
    - Prepend to $freq\_map[1]$: $[(2), (1)]$ (Node 2 is MRU within bucket 1).
    - Cache size = 2 (Full). $min\_freq = 1$.
  - **Op 3: `get(1)`:**
    - Node 1 found ($v = 1$). Increment frequency from 1 to 2:
      - Remove Node 1 from $freq\_map[1]$. Remaining in bucket 1: $[(2)]$.
      - Bucket 1 is non-empty, so $min\_freq$ remains $1$.
      - Node 1 gets $freq = 2$. Prepend to $freq\_map[2]$: $[(1)]$.
    - Return **`1`**.
  - **Op 4: `put(3, 3)` (Eviction):**
    - Cache is full ($|map| == 2$). Evict least frequently used:
      - $min\_freq = 1$. Bucket $freq\_map[1]$ contains $[(2)]$.
      - Tail node is Node 2. Evict Node 2! Remove from $map$ and bucket 1.
    - Insert new Node $(3, 3, freq=1)$ into $freq\_map[1]$: $[(3)]$.
    - Reset $min\_freq \leftarrow 1$. Return `null`.
  - **Op 5: `get(2)`:**
    - Key 2 was evicted. Not in $map \implies$ Return **`-1`**.
  - **Op 6: `get(3)`:**
    - Node 3 found ($v = 3$). Increment frequency from 1 to 2:
      - Remove Node 3 from $freq\_map[1]$. Bucket 1 is now empty!
      - Because $freq == min\_freq$ ($1 == 1$), advance $min\_freq \leftarrow 2$.
      - Prepend Node 3 to $freq\_map[2]$: $[(3), (1)]$ (Node 3 is MRU in bucket 2).
    - Return **`3`**.
  - **Op 7: `put(4, 4)` (Eviction with Tie-Break):**
    - Cache full ($|map| == 2$). Evict LFU node:
      - $min\_freq = 2$. Bucket $freq\_map[2]$ has two nodes: $[(3), (1)]$.
      - Both have equal frequency 2. Tie-break rule: evict **least recently used (tail)**!
      - Tail node is Node 1. Evict Node 1!
    - Insert Node $(4, 4, freq=1)$ into $freq\_map[1]$: $[(4)]$.
    - Set $min\_freq \leftarrow 1$. Return `null`.
  - **Op 8: `get(1)`:**
    - Node 1 was evicted $\implies$ Return **`-1`**.
  - **Op 9: `get(3)`:**
    - Node 3 found ($v = 3$). Frequency $2 \to 3$. Return **`3`**.
  - **Op 10: `get(4)`:**
    - Node 4 found ($v = 4$). Frequency $1 \to 2$. Return **`4`**.

This instance demonstrates two-tier linked list bucket indexing, mathematically proves how combining frequency buckets with doubly linked lists achieves strictly $O(1)$ LFU and LRU operations, and derives $O(1)$ runtime per operation and $O(C)$ space bounds.

---

## 1. Instance & Teaching Goal

Design a data structure for a **Least Frequently Used (LFU)** cache of fixed capacity:
- `get(key)`: Gets the value of the key if it exists, otherwise returns $-1$. Increments the access frequency of the key.
- `put(key, value)`: Inserts or updates the value of the key. When the cache reaches capacity, it must **evict the least frequently used key** before inserting a new key. If there is a tie in minimum frequency, it must evict the **least recently used (LRU) key** among them.
- Both operations must run in **strictly $O(1)$ average time**.

```text
Dual-Map Architecture:
  Key Map:       key ----> Node(key, value, freq)
                             ^
                             |
  Frequency Map: freq ---> DoublyLinkedList [ MRU <---> ... <---> LRU ]

Tie-Breaking Principle:
  1. Lowest frequency bucket is selected: min_freq
  2. Inside freq_map[min_freq], the tail node is the Least Recently Used: remove_last()
```

### Why a Heap / Priority Queue Fails $O(1)$
A binary min-heap can track minimum frequencies, but:
- Updating frequency on `get()` requires modifying a node's key in the heap, taking $O(\log N)$ time to sift down/up.
- Finding and evicting the least recently used element on frequency ties requires secondary timestamps and expensive heap reorganization.
To achieve strictly $O(1)$ for both operations:
We partition nodes into **frequency buckets**, where each bucket is a **Doubly Linked List** maintaining recency order.

---

## 2. Conceptual Foundation & Invariants

### 1. Data Structure Components:
1. **Node:** Stores `(key, value, freq, prev, next)`.
2. **DoublyLinkedList:** Sentinel nodes `head` and `tail`:
   - `add_first(node)`: Inserts node at head (marks it as Most Recently Used for that frequency).
   - `remove(node)`: Unlinks node in $O(1)$ pointer steps.
   - `remove_last()`: Removes node at `tail.prev` (the Least Recently Used node in this bucket).
   - `is_empty()`: Checks if `head.next == tail`.
3. **Primary Hash Map (`map`):** Maps `key` $\to$ `Node`.
4. **Frequency Map (`freq_map`):** Maps `freq` $\to$ `DoublyLinkedList`.
5. **Global Minimum Frequency (`min_freq`):** Tracks the smallest active frequency.

### 2. Frequency Promotion Transition (`incr_freq`):
When a node is accessed via `get()` or updated via `put()`:
1. Remove `node` from `freq_map[node.freq]`.
2. If `freq_map[node.freq]` becomes empty:
   - Delete that frequency bucket.
   - If `node.freq == min_freq`: increment $min\_freq \leftarrow min\_freq + 1$ (the only node with the previous minimum frequency was promoted).
3. Increment `node.freq += 1`.
4. Add `node` to `freq_map[node.freq]` via `add_first(node)`.

### 3. Eviction Rule:
When inserting a new key into a full cache:
1. Access the bucket for the lowest frequency: `ls = freq_map[min_freq]`.
2. Evict the LRU node from that bucket: `evicted = ls.remove_last()`.
3. Delete `evicted.key` from `map`.
4. Insert the new node with `freq = 1` and unconditionally reset $min\_freq \leftarrow 1$.

> **$O(1)$ Invariant.** Every dictionary lookup, pointer splice in a doubly linked list, and $min\_freq$ update executes in strictly bounded $O(1)$ machine operations.

---

## 3. Step-by-Step Worked Execution

We trace the representative trace with $capacity = 2$:

---

### Step 1: Initial Inserts
- `put(1, 1)`:
  - Node 1: $(k=1, v=1, freq=1)$.
  - $map = \{1: \text{Node}(1)\}$.
  - $freq\_map[1] = [(1)]$. $min\_freq = 1$.
- `put(2, 2)`:
  - Node 2: $(k=2, v=2, freq=1)$.
  - $map = \{1: \text{Node}(1), 2: \text{Node}(2)\}$.
  - $freq\_map[1] = [(2) \leftrightarrow (1)]$. (Node 2 at head, Node 1 at tail).
  - $min\_freq = 1$. Cache capacity reached ($2/2$).

---

### Step 2: `get(1)` (Promotion)
- Look up `map[1]` $\implies$ found $v = 1$.
- Increment frequency:
  - Remove Node 1 from $freq\_map[1]$. Remaining: $[(2)]$.
  - Bucket 1 is not empty $\implies min\_freq$ stays $1$.
  - Node 1 frequency becomes $2$.
  - Add Node 1 to $freq\_map[2] \implies [(1)]$.
- Returns **`1`**.

---

### Step 3: `put(3, 3)` (Eviction)
- Cache is full ($2 == 2$).
- Find eviction candidate at $min\_freq = 1$:
  - Bucket $freq\_map[1] = [(2)]$.
  - Evict tail: Node 2.
  - Remove key 2 from $map$.
- Create Node 3: $(k=3, v=3, freq=1)$.
- Add Node 3 to $freq\_map[1] \implies [(3)]$.
- Reset $min\_freq \leftarrow 1$.
- State: $map = \{1, 3\}$, $freq\_map = \{1: [(3)], 2: [(1)]\}$.

---

### Step 4: `get(2)` (Cache Miss)
- Key 2 not in $map$.
- Returns **`-1`**.

---

### Step 5: `get(3)` (Promotion & Min-Freq Advance)
- Look up `map[3]` $\implies$ found $v = 3$.
- Remove Node 3 from $freq\_map[1]$. Bucket 1 is now **empty**!
- Because bucket 1 is empty and was $min\_freq$, advance:
  $$
  min\_freq \leftarrow 1 + 1 = \mathbf{2}
  $$
- Node 3 frequency becomes $2$.
- Add Node 3 to $freq\_map[2]$:
  $$
  freq\_map[2] = [(3) \leftrightarrow (1)]
  $$
  (Node 3 is MRU at head; Node 1 is LRU at tail).
- Returns **`3`**.

---

### Step 6: `put(4, 4)` (Frequency Tie-Break Eviction)
- Cache is full ($2 == 2$).
- Evict from $min\_freq = 2$:
  - Bucket $freq\_map[2] = [(3) \leftrightarrow (1)]$.
  - Both nodes have frequency 2!
  - Evict tail (least recently used): Node 1!
  - Remove key 1 from $map$.
- Create Node 4: $(k=4, v=4, freq=1)$.
- Add Node 4 to $freq\_map[1] \implies [(4)]$.
- Reset $min\_freq \leftarrow 1$.
- State: $map = \{3, 4\}$, $freq\_map = \{1: [(4)], 2: [(3)]\}$.

---

### Step 7: Verification Queries
- `get(1)`: Evicted $\implies$ **`-1`**.
- `get(3)`: Found $\implies$ **`3`** ($freq \to 3$).
- `get(4)`: Found $\implies$ **`4`** ($freq \to 2$).

---

## 4. Complete Execution Trace

| Operation | Target Key | Cache Size | $min\_freq$ | Frequency Buckets State | Evicted Key | Return Value |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|
| `put(1, 1)` | 1 | $1/2$ | $1$ | Freq 1: `[1]` | — | `null` |
| `put(2, 2)` | 2 | $2/2$ | $1$ | Freq 1: `[2, 1]` | — | `null` |
| `get(1)` | 1 | $2/2$ | $1$ | Freq 1: `[2]`, Freq 2: `[1]` | — | **`1`** |
| `put(3, 3)` | 3 | $2/2$ | $1$ | Freq 1: `[3]`, Freq 2: `[1]` | **Node 2** | `null` |
| `get(2)` | 2 | $2/2$ | $1$ | Freq 1: `[3]`, Freq 2: `[1]` | — | **`-1`** |
| `get(3)` | 3 | $2/2$ | **$2$** | Freq 2: `[3, 1]` | — | **`3`** |
| `put(4, 4)` | 4 | $2/2$ | $1$ | Freq 1: `[4]`, Freq 2: `[3]` | **Node 1 (Tie LRU)** | `null` |
| `get(1)` | 1 | $2/2$ | $1$ | Freq 1: `[4]`, Freq 2: `[3]` | — | **`-1`** |
| `get(3)` | 3 | $2/2$ | $1$ | Freq 1: `[4]`, Freq 3: `[3]` | — | **`3`** |
| `get(4)` | 4 | $2/2$ | $2$ | Freq 2: `[4]`, Freq 3: `[3]` | — | **`4`** |

---

## 5. Boundary Cases & Failure Modes

- **Zero Capacity ($capacity = 0$):** `get()` always returns `-1`; `put()` does nothing immediately without raising errors.
- **Capacity = 1:** Evicts the existing element on every insert of a new key.
- **Updating Existing Key (`put` with existing key):** Updates value, increments frequency (promotes to higher bucket), but does not trigger eviction or alter capacity count.
- **All Elements Evicted and Re-inserted:** Resetting $min\_freq = 1$ on fresh insertions keeps minimum pointer accurate.

---

## 6. Traps & Common Anti-Patterns

- **Searching for $min\_freq$ Linearly ($O(N)$):** Searching through all frequencies to find the new minimum after an eviction takes $O(N)$ time. Because fresh nodes start at frequency 1 ($min\_freq = 1$) and accessed nodes only increase frequency by $+1$ ($min\_freq += 1$), maintaining $min\_freq$ incrementally is strictly $O(1)$.
- **Using a Single LRU Linked List:** A single list cannot separate frequency ranking from recency ranking. Separate linked lists per frequency bucket are necessary to achieve independent LFU and LRU prioritization.
- **Forgetting to Clean Up Empty Buckets:** Leaving empty linked lists in $freq\_map$ can cause memory leaks and confuse $min\_freq$ checks. Deleting empty frequency buckets maintains dictionary integrity.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `get(key)`: Hash map lookup ($O(1)$), linked list node removal and head insertion ($O(1)$). Total: $\mathcal{O}(1)$.
  - `put(key, value)`: Hash map lookup ($O(1)$), tail eviction ($O(1)$), and node insertion ($O(1)$). Total: $\mathcal{O}(1)$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(C)$ where $C = capacity$. The primary hash map and all doubly linked lists collectively store at most $C$ node structures.
