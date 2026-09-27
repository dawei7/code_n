# Guided Example: Insert Delete GetRandom O(1)

We trace the step-by-step dual data structure synchronization (hash map `d` for indices + dense dynamic array `q` for values), constant-time tail swap-and-pop deletion (`q[i] = q[-1]`, `q.pop()`), and uniform random sampling (`choice(q)`) on representative command sequences:

- **Input:** Sequence of operations:
  1. `insert(1)` $\implies \text{true}$ (`q = [1]`, `d = {1: 0}`)
  2. `remove(2)` $\implies \text{false}$ ($2$ is not present)
  3. `insert(2)` $\implies \text{true}$ (`q = [1, 2]`, `d = {1: 0, 2: 1}`)
  4. `getRandom()` $\implies 1$ or $2$ (each with exact probability $1/2$)
  5. `remove(1)` $\implies \text{true}$ (Swap tail $2$ into slot $0$, pop tail: `q = [2]`, `d = {2: 0}`)
  6. `insert(2)` $\implies \text{false}$ ($2$ already exists)
  7. `getRandom()` $\implies 2$ (only element, probability $1$)
- **Required output:** `[true, false, true, 2, true, false, 2]`
- **Tail Element Deletion:** Deleting the last element directly handles `i == len(q) - 1` without special branches
- **Strict Uniformity:** Every element in array `q` occupies an indexed slot in $[0, \text{len}(q) - 1]$, guaranteeing uniform selection probability $1/N$

This instance demonstrates combining dynamic arrays and hash tables to support average $O(1)$ operations, mathematically proves why swap-with-last avoids $O(N)$ array shifting, and analyzes memory bounds.

---

## 1. Instance & Teaching Goal

Implement the `RandomizedSet` class such that all methods operate in **average $O(1)$ time complexity**:
- `insert(val)`: Inserts item `val` if not already present. Returns `true` if inserted, `false` otherwise.
- `remove(val)`: Removes item `val` if present. Returns `true` if removed, `false` otherwise.
- `getRandom()`: Returns a random element from the current set with each element having **equal probability of being chosen**.

```text
The Fundamental Data Structure Trade-off:
1. Hash Set alone:
   - insert(val) and remove(val) are O(1).
   - getRandom() is O(N) because hash buckets have holes and lack contiguous indexing.
2. Dynamic Array alone:
   - getRandom() is O(1) via random.choice(arr).
   - remove(val) is O(N) because finding val and shifting elements takes linear time.

The Hybrid O(1) Solution:
- Array `q`: Stores values contiguously, enabling O(1) getRandom via index sampling.
- Map `d`: Maps each value `val` to its current index in `q`, enabling O(1) lookup.
- Deletion: Swap target element with the LAST element of `q`, then pop the tail!
```

---

## 2. Conceptual Foundation & Invariants

### 1. State Representation:
- `self.q = []`: Dense dynamic list containing every current element.
- `self.d = {}`: Hash map where `self.d[val]` is the unique index $i$ such that `self.q[i] == val`.

### 2. Method Invariants:
1. **`insert(val: int) -> bool`:**
   - If `val in self.d`: return **`False`**.
   - Record index: `self.d[val] = len(self.q)`.
   - Append to array: `self.q.append(val)`.
   - Return **`True`**.
2. **`remove(val: int) -> bool`:**
   - If `val not in self.d`: return **`False`**.
   - Retrieve index: `i = self.d[val]`.
   - Retrieve last value: `last_val = self.q[-1]`.
   - Overwrite slot $i$ with `last_val`:
     $$
     self.d[last\_val] \leftarrow i
     $$
     $$
     self.q[i] \leftarrow last\_val
     $$
   - Remove tail from array: `self.q.pop()`.
   - Remove `val` from dictionary: `self.d.pop(val)`.
   - Return **`True`**.
3. **`getRandom() -> int`:**
   - Return `random.choice(self.q)`.

> **Invariant.** Array `self.q` is always dense (no null holes), and for every element $v$, `self.q[self.d[v]] == v`.

---

## 3. Step-by-Step Worked Execution

We trace the operational sequence:

---

### Step 1: `insert(1)`
- Check: $1 \in self.d$ is False.
- Index assigned: $self.d[1] = \text{len}(self.q) = 0$.
- Append: $self.q.\text{append}(1) \implies self.q = [1]$.
- State: `q = [1], d = {1: 0}`.
- Return: **`true`**.

---

### Step 2: `remove(2)`
- Check: $2 \in self.d$ is False.
- Element does not exist; no state modification.
- Return: **`false`**.

---

### Step 3: `insert(2)`
- Check: $2 \in self.d$ is False.
- Index assigned: $self.d[2] = \text{len}(self.q) = 1$.
- Append: $self.q.\text{append}(2) \implies self.q = [1, 2]$.
- State: `q = [1, 2], d = {1: 0, 2: 1}`.
- Return: **`true`**.

---

### Step 4: `getRandom()`
- Array has length 2: elements $[1, 2]$.
- Uniform index selection: $idx \in \{0, 1\}$.
- Returns either $1$ or $2$ with equal probability $50\%$.

---

### Step 5: `remove(1)` — The Tail Swap Mechanism
- Check: $1 \in self.d$ is True.
- Target index: $i = self.d[1] = \mathbf{0}$.
- Tail element: $last\_val = self.q[-1] = \mathbf{2}$.
- **Step A:** Update dictionary mapping for tail element:
  $$
  self.d[2] \leftarrow 0
  $$
- **Step B:** Overwrite slot $0$ in array with tail element:
  $$
  self.q[0] \leftarrow 2 \implies self.q = [2, 2]
  $$
- **Step C:** Pop tail element from array:
  $$
  self.q.\text{pop}() \implies self.q = [2]
  $$
- **Step D:** Delete target from dictionary:
  $$
  self.d.\text{pop}(1) \implies self.d = \{2: 0\}
  $$
- Return: **`true`**.

---

### Step 6: `insert(2)`
- Check: $2 \in self.d$ is True (already present at index 0).
- Insertion rejected.
- Return: **`false`**.

---

### Step 7: `getRandom()`
- Array has length 1: $self.q = [2]$.
- Unique outcome: **`2`** with probability $100\%$.

---

## 4. Complete Execution Trace

```text
RandomizedSet Operations:
1. insert(1) -> d={1:0}, q=[1]       -> True
2. remove(2) -> 2 not in d           -> False
3. insert(2) -> d={1:0, 2:1}, q=[1,2] -> True
4. getRandom()-> choice([1, 2])       -> 1 or 2
5. remove(1) -> swap 2 into slot 0
                q.pop() -> q=[2]
                d.pop(1)-> d={2:0}   -> True
6. insert(2) -> 2 already in d       -> False
7. getRandom()-> choice([2])          -> 2

Result Stream: [true, false, true, 2, true, false, 2]
```

| Step | Operation | Parameter | State Before (`q`, `d`) | Action Taken | State After (`q`, `d`) | Return Value |
|:---:|:---:|:---:|:---|:---|:---|:---:|
| 1 | `insert` | 1 | `[], {}` | Append 1 at index 0 | `[1], {1: 0}` | **`true`** |
| 2 | `remove` | 2 | `[1], {1: 0}` | Not found | `[1], {1: 0}` | **`false`** |
| 3 | `insert` | 2 | `[1], {1: 0}` | Append 2 at index 1 | `[1, 2], {1: 0, 2: 1}` | **`true`** |
| 4 | `getRandom` | - | `[1, 2], {1: 0, 2: 1}` | Sample index 0 or 1 | Unchanged | **$1$ or $2$** |
| **5** | **`remove`** | **1** | **`[1, 2], {1: 0, 2: 1}`** | **Swap tail 2 to slot 0, pop tail** | **`[2], {2: 0}`** | **`true`** |
| 6 | `insert` | 2 | `[2], {2: 0}` | Duplicate check | `[2], {2: 0}` | **`false`** |
| 7 | `getRandom` | - | `[2], {2: 0}` | Sample index 0 | Unchanged | **`2`** |

---

## 5. Algorithmic Correctness

**Soundness.** Swapping the element to be deleted with the last element of `self.q` preserves the set of remaining elements while ensuring the deletion target is at the end of the array. Popping the last element from a dynamic array requires no elements to be shifted, ensuring strictly $O(1)$ time. Updating `self.d[self.q[-1]] = i` maintains the invariant that the moved element's stored index accurately reflects its new position.

**Completeness.** Because `self.q` is kept strictly dense (contains exactly all $N$ valid elements at indices $0 \dots N - 1$ without holes), calling `random.choice(self.q)` picks each element with probability exactly $1/N$, fulfilling the uniform distribution requirement.

---

## 6. Traps This Instance Exposes

- **Order of Deletion Steps:** If the target value is already the last element (i.e. $val == q[-1]$), setting `d[q[-1]] = i` assigns `d[val] = i`, and the subsequent `d.pop(val)` immediately removes it. However, if dictionary deletion were performed *before* updating `d[q[-1]]`, deleting the tail element could re-insert `val` into `d`! The sequence `d[q[-1]] = i` followed by `d.pop(val)` is strictly required.
- **Tombstone Overhead:** Marking deleted slots as `None` in the array avoids shifting but causes holes. Over time, `getRandom()` would need rejection sampling, degrading runtime when many deletions occur.
- **Python Random Choice:** `random.choice(q)` internally generates a random integer in $[0, \text{len}(q) - 1]$ and indexes the array in $O(1)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `insert(val)`: $O(1)$ average time for dictionary lookup, assignment, and list append.
  - `remove(val)`: $O(1)$ average time for dictionary lookup, array slot overwrite, `q.pop()`, and `d.pop()`.
  - `getRandom()`: $O(1)$ time to sample a random integer index and retrieve `q[idx]`.
- **Auxiliary Space Complexity:** $O(N)$, where $N$ is the number of elements currently stored in the set, for list `q` and hash map `d`.
