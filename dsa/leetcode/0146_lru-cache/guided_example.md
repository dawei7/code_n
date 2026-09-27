# Guided Example: LRU Cache

We trace the step-by-step state evolution of a Least Recently Used (LRU) Cache combining a hash map with a sentinel doubly linked list:

- **Input Operations:**
  `["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]`
- **Arguments:**
  `[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]`
- **Required output:**
  `[null, null, null, 1, null, -1, null, -1, 3, 4]`

This instance demonstrates how a Doubly Linked List paired with a Hash Map satisfies the $O(1)$ time guarantee for both `get` and `put`, showing how dummy sentinels eliminate null-checking edge cases, how node promotion works, and how LRU evictions remove the oldest node in $O(1)$ time.

---

## 1. Instance & Teaching Goal

Design a data structure with positive capacity $C = 2$ supporting:
- `get(key)`: returns value if present, else $-1$. Promotes key to Most Recently Used (MRU).
- `put(key, value)`: updates existing key or inserts new key. If size exceeds capacity, evicts the Least Recently Used (LRU) key.
Both operations must run in strictly $O(1)$ time.

In this instance:
1. `put(1, 1)`: Cache stores key 1.
2. `put(2, 2)`: Cache stores keys 1 and 2 (capacity reached).
3. `get(1)`: Returns $1$, refreshing key 1 to MRU. Key 2 becomes LRU.
4. `put(3, 3)`: Cache exceeds capacity! Evicts LRU key $2$, inserts $3$.
5. `get(2)`: Returns $-1$ because key 2 was evicted.
6. `put(4, 4)`: Evicts LRU key $1$, inserts $4$.
7. `get(1)`: Returns $-1$.
8. `get(3)`: Returns $3$, refreshing 3 to MRU.
9. `get(4)`: Returns $4$, refreshing 4 to MRU.

An array or single-linked list requires $O(N)$ time to shift or locate elements.
A Hash Map provides $O(1)$ key lookup, but has no inherent access ordering.
A Doubly Linked List maintains chronological access order and allows $O(1)$ node removal and head insertion given a direct node reference. Pairing the two yields $O(1)$ performance across all operations.

---

## 2. Conceptual Foundation & Invariants

### Architectural Composition: Map + Doubly Linked List
Each node stores `key`, `value`, `prev`, and `next`.
- **Sentinel Boundaries:**
  A dummy `head` and dummy `tail` sentinel bracket the list:
  $$
  \text{head} \longleftrightarrow \text{Node}_{\text{MRU}} \longleftrightarrow \dots \longleftrightarrow \text{Node}_{\text{LRU}} \longleftrightarrow \text{tail}
  $$
  - The node immediately after `head` (`head.next`) is always the **Most Recently Used (MRU)**.
  - The node immediately before `tail` (`tail.prev`) is always the **Least Recently Used (LRU)**.
  - Sentinels eliminate null-checks during boundary insertions and removals.

### Fundamental Helper Operations ($O(1)$)
1. **Remove Node (`_remove(node)`):**
   $$
   \text{node.prev.next} = \text{node.next}
   $$
   $$
   \text{node.next.prev} = \text{node.prev}
   $$
2. **Insert to Head (`_insert_to_head(node)`):**
   Splice `node` between `head` and `head.next`:
   $$
   \text{node.next} = \text{head.next}
   $$
   $$
   \text{node.prev} = \text{head}
   $$
   $$
   \text{head.next.prev} = \text{node}
   $$
   $$
   \text{head.next} = \text{node}
   $$
3. **Move to Front (`_promote(node)`):**
   `_remove(node)` followed by `_insert_to_head(node)`.

### Operational Contracts
- **`get(key)`:**
  If `key` not in `cache`: return $-1$.
  Retrieve `node = cache[key]`.
  Promote `node` to head (`_promote(node)`).
  Return `node.val`.
- **`put(key, value)`:**
  If `key` in `cache`:
  - Update `node.val = value`.
  - Promote `node` to head.
  Else:
  - Create new `node = Node(key, value)`.
  - Insert `cache[key] = node` and `_insert_to_head(node)`.
  - If `len(cache) > capacity`:
    - Identify LRU node: `lru = tail.prev`.
    - `_remove(lru)`.
    - Delete from map: `del cache[lru.key]`.

> **Invariant.** For every key in `cache`, `cache[key]` points to its corresponding node in the doubly linked list. The list is ordered from `head.next` (MRU) down to `tail.prev` (LRU).

---

## 3. Step-by-Step Worked Execution

We trace the operations on capacity $C = 2$:

### Step 1: `LRUCache(2)`
- Initialize sentinels: `head <-> tail`.
- `cache = {}`.
- Return `null`.

---

### Step 2: `put(1, 1)`
- Key 1 not in cache.
- Allocate `Node(1, 1)`.
- Insert to head: `head <-> [1:1] <-> tail`.
- `cache = {1: Node(1, 1)}`.
- Size $1 \le 2$. Return `null`.

---

### Step 3: `put(2, 2)`
- Key 2 not in cache.
- Allocate `Node(2, 2)`.
- Insert to head: `head <-> [2:2] <-> [1:1] <-> tail`.
- `cache = {1: Node(1), 2: Node(2)}`.
- Size $2 \le 2$. Return `null`.
- Current ordering: MRU is $2$, LRU is $1$.

---

### Step 4: `get(1)`
- Key 1 found in cache!
- Promote Node 1 to head:
  - Detach Node 1: `head <-> [2:2] <-> tail`.
  - Insert at head: `head <-> [1:1] <-> [2:2] <-> tail`.
- Ordering updated: MRU is $1$, LRU is $2$.
- Return value: $\mathbf{1}$.

---

### Step 5: `put(3, 3)`
- Key 3 not in cache.
- Allocate `Node(3, 3)`.
- Insert at head: `head <-> [3:3] <-> [1:1] <-> [2:2] <-> tail`.
- `cache = {1: Node(1), 2: Node(2), 3: Node(3)}`.
- Size is $3 > 2 \implies$ **Eviction Triggered!**
  - Identify LRU: `tail.prev = Node(2, 2)`.
  - Remove from list: `head <-> [3:3] <-> [1:1] <-> tail`.
  - Remove from hash map: `del cache[2]`.
- Return `null`.

---

### Step 6: `get(2)`
- Key 2 is not in `cache` (evicted in Step 5).
- Return: $\mathbf{-1}$.

---

### Step 7: `put(4, 4)`
- Key 4 not in cache.
- Allocate `Node(4, 4)`.
- Insert at head: `head <-> [4:4] <-> [3:3] <-> [1:1] <-> tail`.
- Size is $3 > 2 \implies$ **Eviction Triggered!**
  - Identify LRU: `tail.prev = Node(1, 1)`.
  - Remove from list: `head <-> [4:4] <-> [3:3] <-> tail`.
  - Remove from hash map: `del cache[1]`.
- Return `null`.

---

### Step 8: `get(1)`
- Key 1 is not in `cache` (evicted in Step 7).
- Return: $\mathbf{-1}$.

---

### Step 9: `get(3)`
- Key 3 found in cache!
- Promote Node 3 to head:
  - `head <-> [3:3] <-> [4:4] <-> tail`.
- Return value: $\mathbf{3}$.

---

### Step 10: `get(4)`
- Key 4 found in cache!
- Promote Node 4 to head:
  - `head <-> [4:4] <-> [3:3] <-> tail`.
- Return value: $\mathbf{4}$.

---

## 4. Complete Execution Trace

```text
head <-> [MRU] <-> ... <-> [LRU] <-> tail
put(1,1): head <-> [1:1] <-> tail
put(2,2): head <-> [2:2] <-> [1:1] <-> tail
get(1):   head <-> [1:1] <-> [2:2] <-> tail           (Returns 1, 1 promoted)
put(3,3): head <-> [3:3] <-> [1:1] <-> tail           (2 evicted as LRU)
get(2):   Not in cache                                (Returns -1)
put(4,4): head <-> [4:4] <-> [3:3] <-> tail           (1 evicted as LRU)
get(1):   Not in cache                                (Returns -1)
get(3):   head <-> [3:3] <-> [4:4] <-> tail           (Returns 3)
get(4):   head <-> [4:4] <-> [3:3] <-> tail           (Returns 4)
```

| Step | Operation | Input Args | Cache Keys (MRU $\to$ LRU) | Evicted Key | Return Value |
|:---:|:---:|:---:|:---|:---:|:---:|
| 1 | `LRUCache` | `[2]` | `[]` | - | `null` |
| 2 | `put` | `[1, 1]` | `[1]` | - | `null` |
| 3 | `put` | `[2, 2]` | `[2, 1]` | - | `null` |
| **4** | `get` | `[1]` | `[1, 2]` (1 promoted) | - | **1** |
| **5** | `put` | `[3, 3]` | `[3, 1]` | **2** | `null` |
| **6** | `get` | `[2]` | `[3, 1]` | - | **-1** |
| **7** | `put` | `[4, 4]` | `[4, 3]` | **1** | `null` |
| **8** | `get` | `[1]` | `[4, 3]` | - | **-1** |
| **9** | `get` | `[3]` | `[3, 4]` (3 promoted) | - | **3** |
| **10** | `get` | `[4]` | `[4, 3]` (4 promoted) | - | **4** |

---

## 5. Algorithmic Correctness

**Soundness.** Hash map keys map 1-to-1 with doubly linked list nodes. Every access (`get` or `put`) detaches the accessed node and splices it directly after `head`, ensuring that the most recently touched node is at the front. The least recently touched node naturally drifts backward to `tail.prev`. Thus, evicting `tail.prev` strictly evicts the true LRU element.

**Completeness.** Sentinel nodes `head` and `tail` ensure that every valid node has non-null `prev` and `next` pointers. Insertions, removals, and promotions are executed in $O(1)$ pointer operations without traversing the list.

---

## 6. Traps This Instance Exposes

- **Storing Key in Node Object:** A node must store both `key` and `value` (not just `value`)! When evicting `tail.prev`, the algorithm must delete the key from the hash map via `del cache[lru.key]`. Without storing `key` on the node, looking up the map key from the node would require an $O(N)$ scan.
- **Forgetting Promotion on `put` Update:** If `put(key, value)` is called on an *existing* key, updating the value is not enough; the node must also be promoted to MRU.
- **Sentinel Boundary Dangling:** Failing to initialize `head.next = tail` and `tail.prev = head` causes null pointer exceptions on the very first insertion.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$ time for both `get` and `put`. Hash map lookup and insertion take $O(1)$ average time. Doubly linked list removal and insertion take $O(1)$ pointer rewires.
- **Auxiliary Space Complexity:** $O(C)$, where $C$ is the cache capacity. The hash map and linked list each store at most $C$ nodes and entries simultaneously.