# Guided Example: All O`one Data Structure

We trace the step-by-step doubly linked frequency bucket list management, hash-map key-to-node routing, adjacent bucket insertion and empty-bucket pruning, and constant-time extremum extraction on representative operation sequences:

- **Input:** Operations sequence:
  ```text
  inc("hello"), inc("hello"), getMaxKey(), getMinKey(), inc("leet"), getMaxKey(), getMinKey()
  ```
- **Required output:** `["hello", "hello", "hello", "leet"]`
  - **Operation 1 (`inc("hello")`):**
    - `"hello"` is new $\implies$ Insert `Bucket(cnt=1, keys={"hello"})` after sentinel `root`.
    - Doubly linked list: `root <-> [cnt=1: {"hello"}] <-> root`
    - Mapping: `nodes["hello"] = Bucket(1)`
  - **Operation 2 (`inc("hello")`):**
    - Current count is $1$. Next bucket needs $cnt = 2$.
    - Insert `Bucket(cnt=2, keys={"hello"})` after `Bucket(1)`.
    - Remove `"hello"` from `Bucket(1)`. `Bucket(1)` is now empty $\implies$ **Delete `Bucket(1)`!**
    - Doubly linked list: `root <-> [cnt=2: {"hello"}] <-> root`
    - Mapping: `nodes["hello"] = Bucket(2)`
  - **Operation 3 (`getMaxKey()`):**
    - Tail bucket is `root.prev = Bucket(2)` $\implies$ Return `"hello"`
  - **Operation 4 (`getMinKey()`):**
    - Head bucket is `root.next = Bucket(2)` $\implies$ Return `"hello"`
  - **Operation 5 (`inc("leet")`):**
    - `"leet"` is new $\implies$ Needs $cnt = 1$.
    - Current first bucket has $cnt = 2 > 1$.
    - Insert `Bucket(cnt=1, keys={"leet"})` between `root` and `Bucket(2)`.
    - Doubly linked list: `root <-> [cnt=1: {"leet"}] <-> [cnt=2: {"hello"}] <-> root`
    - Mapping: `nodes["leet"] = Bucket(1)`
  - **Operation 6 (`getMaxKey()`):**
    - Tail bucket: `root.prev = Bucket(2)` $\implies$ Return `"hello"`
  - **Operation 7 (`getMinKey()`):**
    - Head bucket: `root.next = Bucket(1)` $\implies$ Return `"leet"`
- **Empty Structure Instance:** $root.next == root \implies getMaxKey() = \text{""}, \; getMinKey() = \text{""}$
- **Decrement to Zero:** `dec("leet")` removes `"leet"` from `Bucket(1)`. `Bucket(1)` becomes empty and is excised from the doubly linked list.

This instance demonstrates combining a hash map with a sorted doubly linked list of bucket sets, mathematically proves why maintaining contiguous non-empty frequency nodes achieves strictly $O(1)$ worst-case time for all operations, and derives $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Design a data structure that supports storing keys with string identifiers, incrementing/decrementing their frequencies, and querying the key with minimum and maximum frequency in **$O(1)$ worst-case time complexity**:
- `inc(String key)`: Increments the count of `key` by 1. If `key` does not exist, inserts it with count 1.
- `dec(String key)`: Decrements the count of `key` by 1. If the count reaches 0, removes `key`.
- `getMaxKey()`: Returns any key with the highest frequency (or `""` if no keys exist).
- `getMinKey()`: Returns any key with the lowest frequency (or `""` if no keys exist).

```text
Visualizing the Doubly Linked Bucket Architecture:

  +------+    next    +-----------------+    next    +-----------------+    next    +------+
  | root | ---------> | cnt: 1          | ---------> | cnt: 2          | ---------> | root |
  | (0)  | <--------- | keys: {"leet"}  | <--------- | keys: {"hello"} | <--------- | (0)  |
  +------+    prev    +-----------------+    prev    +-----------------+    prev    +------+
     ^                                                                                  ^
     |                                                                                  |
     +--- Min Key: root.next ("leet")            Max Key: root.prev ("hello") ----------+
```

### The $O(1)$ Extremum Challenge
- A standard Hash Map can increment and decrement in $O(1)$ time, but finding min/max frequency takes $O(K)$ time by scanning all keys.
- A Heap (Priority Queue) finds min/max in $O(1)$ time, but updating an arbitrary key's frequency takes $O(\log K)$ time.
- **Dual Structure Synthesis:** We group all keys sharing the exact same frequency into a **Bucket Node** holding a hash set of keys. All non-empty buckets are linked together in a **circular doubly linked list sorted by frequency**. A secondary hash map maps each key directly to its containing bucket node.

---

## 2. Conceptual Foundation & Invariants

### 1. The Bucket Node Specification:
Each node in the doubly linked list contains:
- `cnt`: The integer frequency shared by all keys in this bucket.
- `keys`: A hash set of string keys having frequency `cnt`.
- `prev, next`: Pointers to adjacent bucket nodes in the frequency chain.

### 2. Sentinel Node Invariant:
A sentinel node `root` acts as both head and tail:
- `root.next`: The bucket with the **strictly minimum** frequency.
- `root.prev`: The bucket with the **strictly maximum** frequency.
- If `root.next == root`: The data structure is empty. `getMaxKey()` and `getMinKey()` return `""`.

### 3. Transition Rules for `inc(key)`:
Let `curr` be `nodes[key]` (or `root` if `key` is new):
1. Target frequency is $curr.cnt + 1$.
2. Check if the adjacent node `curr.next` has count equal to $curr.cnt + 1$:
   - If yes: add `key` to `curr.next.keys`.
   - If no: allocate a new `Bucket(curr.cnt + 1)` and splice it between `curr` and `curr.next`.
3. Update `nodes[key] = target_bucket`.
4. If `key` already existed in `curr`: remove `key` from `curr.keys`. If `curr.keys` is now empty, excise `curr` from the doubly linked list.

> **Contiguity Invariant.** Every bucket node in the linked list has a strictly positive, non-zero number of keys, and bucket frequencies are strictly increasing: $root.next.cnt < \dots < root.prev.cnt$.

---

## 3. Step-by-Step Worked Execution

We trace the sample sequence of 7 operations:

---

### Step 1: `inc("hello")`
- `"hello"` not in `nodes`.
- `curr = root` ($cnt = 0$). Target count is $1$.
- `root.next` is `root` (no bucket with $cnt = 1$ exists).
- Create `B1 = Node(cnt=1, keys={"hello"})`. Splice between `root` and `root`.
- State: `root <-> B1(cnt=1: {"hello"}) <-> root`.
- `nodes["hello"] = B1`.

---

### Step 2: `inc("hello")`
- `"hello"` is in $B1$ ($cnt = 1$). Target count is $2$.
- Next node $B1.next$ is `root` ($cnt \ne 2$).
- Create `B2 = Node(cnt=2, keys={"hello"})`. Splice after $B1$.
- Remove `"hello"` from $B1$. $B1.keys$ becomes empty $\implies$ **Delete $B1$!**
- Spliced state: `root <-> B2(cnt=2: {"hello"}) <-> root`.
- `nodes["hello"] = B2`.

---

### Step 3: `getMaxKey()`
- Maximum bucket is `root.prev` $= B2$.
- Emits any key from $B2.keys$: **`"hello"`**.

---

### Step 4: `getMinKey()`
- Minimum bucket is `root.next` $= B2$.
- Emits any key from $B2.keys$: **`"hello"`**.

---

### Step 5: `inc("leet")`
- `"leet"` not in `nodes`. Target count is $1$.
- `root.next` is $B2$ ($cnt = 2 > 1$).
- Bucket with $cnt = 1$ does not exist.
- Create `B1 = Node(cnt=1, keys={"leet"})`. Splice between `root` and $B2$.
- Spliced state:
  $$
  root \rightleftharpoons B1(1: \{\text{"leet"}\}) \rightleftharpoons B2(2: \{\text{"hello"}\}) \rightleftharpoons root
  $$
- `nodes["leet"] = B1`.

---

### Step 6: `getMaxKey()`
- Maximum bucket is `root.prev` $= B2$ ($cnt = 2$).
- Emits: **`"hello"`**.

---

### Step 7: `getMinKey()`
- Minimum bucket is `root.next` $= B1$ ($cnt = 1$).
- Emits: **`"leet"`**.

---

## 4. Complete Execution Trace

| Op # | Call | Key | Target Count | Bucket Action | Doubly Linked List Structure | Output |
|:---:|:---|:---:|:---:|:---|:---|:---:|
| **1** | `inc` | `"hello"` | $1$ | Insert $B_1$ after `root` | `root <-> B1(1: {hello}) <-> root` | — |
| **2** | `inc` | `"hello"` | $2$ | Insert $B_2$, delete empty $B_1$ | `root <-> B2(2: {hello}) <-> root` | — |
| **3** | `getMaxKey`| — | — | Inspect `root.prev` | `root.prev = B2` | **`"hello"`** |
| **4** | `getMinKey`| — | — | Inspect `root.next` | `root.next = B2` | **`"hello"`** |
| **5** | `inc` | `"leet"` | $1$ | Insert $B_1$ between `root` and $B_2$ | `root <-> B1(1: {leet}) <-> B2(2: {hello}) <-> root` | — |
| **6** | `getMaxKey`| — | — | Inspect `root.prev` | `root.prev = B2` | **`"hello"`** |
| **7** | `getMinKey`| — | — | Inspect `root.next` | `root.next = B1` | **`"leet"`** |

---

## 5. Boundary Cases & Failure Modes

- **Empty Structure Queries:** When no keys exist, `root.next == root`. `getMaxKey()` and `getMinKey()` detect this condition and return `""`.
- **All Keys Decremented to Zero:** Decrementing the last remaining key deletes its bucket, returning the list to `root.next == root`. Subsequent queries return `""`.
- **Multiple Keys with Identical Frequencies:** Multiple keys coexist in the same bucket's hash set `keys`. `getMaxKey()` returns any key from the set in $O(1)$ time via `next(iter(keys))`.
- **Non-Consecutive Frequencies:** Frequencies do not need to be contiguous (e.g. $B_1$ has $cnt=1$ and $B_2$ has $cnt=100$). Incrementing a key in $B_1$ inserts a new bucket $B_{new}(cnt=2)$ directly between $B_1$ and $B_2$.

---

## 6. Traps & Common Anti-Patterns

- **Memory Leak from Empty Buckets:** Failing to remove a bucket node when its `keys` set becomes empty causes obsolete nodes with count $>0$ to persist, leading to wrong answers on `getMinKey()` and `getMaxKey()`.
- **Allocating Linear Arrays for Frequencies:** Using an array indexed by frequency requires unbounded memory if a key is incremented $10^5$ times. The doubly linked list allocates nodes strictly proportional to distinct frequencies present.
- **Hash Set Iteration Overhead:** In Python, calling `list(keys)[0]` takes $O(|keys|)$ time because it copies all elements. Using `next(iter(keys))` extracts a single element in guaranteed $O(1)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `inc(key)`: Hash map lookup, hash set add/discard, and doubly linked list pointer splicing take $O(1)$ time.
  - `dec(key)`: Symmetrical $O(1)$ pointer and map updates.
  - `getMaxKey()`: Reading `root.prev` and fetching one element takes $O(1)$ time.
  - `getMinKey()`: Reading `root.next` and fetching one element takes $O(1)$ time.
  - All operations run in strictly $\mathcal{O}(1)$ worst-case time.
- **Auxiliary Space Complexity:**
  - The number of bucket nodes is bounded by the number of unique frequencies ($\le K$, where $K$ is the number of distinct keys).
  - The hash map and key sets store each unique string once.
  - Total Auxiliary Space: $\mathcal{O}(K)$.