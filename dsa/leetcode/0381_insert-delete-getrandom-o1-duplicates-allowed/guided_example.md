# Guided Example: Insert Delete GetRandom O(1) - Duplicates allowed

We trace the step-by-step multiset index-set tracking (`self.m[val] = set()`), tail swap-and-pop removal with position update (`self.l[idx] = self.l[last_idx]`), and frequency-weighted uniform random sampling (`choice(self.l)`) on representative command sequences:

- **Input:** Sequence of operations:
  1. `insert(1)` $\implies \text{true}$ (`l = [1]`, `m = {1: {0}}`, first copy)
  2. `insert(1)` $\implies \text{false}$ (`l = [1, 1]`, `m = {1: {0, 1}}`, duplicate copy)
  3. `insert(2)` $\implies \text{true}$ (`l = [1, 1, 2]`, `m = {1: {0, 1}, 2: {2}}`, first copy)
  4. `getRandom()` $\implies 1$ with probability $2/3$, $2$ with probability $1/3$
  5. `remove(1)` $\implies \text{true}$ (Swap tail $2$ into slot $0$, pop tail: `l = [2, 1]`, `m = {1: {1}, 2: {0}}`)
  6. `getRandom()` $\implies 1$ with probability $1/2$, $2$ with probability $1/2$
- **Required output:** `[true, false, true, 1 or 2, true, 1 or 2]`
- **Single Copy Remaining Removal:** When the last copy of a number is removed, `m.pop(val)` purges the key
- **Tail Self-Removal:** When $idx == last\_idx$, the condition `if idx < last_idx:` correctly avoids re-adding the popped index

This instance demonstrates multiset tracking using dynamic arrays and inverted index-set maps, mathematically proves why sampling directly from the dense occurrence array guarantees exact frequency-proportional selection probabilities, and analyzes $O(1)$ operations and linear space.

---

## 1. Instance & Teaching Goal

Implement the `RandomizedCollection` multiset class:
- `insert(val)`: Inserts an item `val`. Returns `true` if the collection did not already contain `val`, `false` otherwise.
- `remove(val)`: Removes **one occurrence** of item `val` if present. Returns `true` if removed, `false` otherwise.
- `getRandom()`: Returns a random element from the current collection where the probability of selecting an item is **directly proportional to the number of occurrences of that item**.

```text
Collection State: [1, 1, 2] (Size 3)
Multiset Frequencies:
  Value 1: 2 copies -> Probability = 2/3 (66.7%)
  Value 2: 1 copy   -> Probability = 1/3 (33.3%)

By maintaining all copies in a dense list `l = [1, 1, 2]`,
calling random.choice(l) automatically achieves exact frequency weighting!
```

---

## 2. Conceptual Foundation & Invariants

### 1. Data Structures:
- `self.l = []`: Dense array storing every active value occurrence.
- `self.m = {}`: Dictionary mapping each distinct value `val` to a **hash set of its indices** in `self.l`.

### 2. Method Invariants:
1. **`insert(val)`:**
   - Retrieve or create index set: `idx_set = self.m.get(val, set())`.
   - New index is $new\_idx = \text{len}(self.l)$.
   - Add to index set: `idx_set.add(new_idx)`.
   - Append to array: `self.l.append(val)`.
   - Return `True` if this was the first occurrence ($\text{len}(idx\_set) == 1$), else `False`.
2. **`remove(val)`:**
   - If `val not in self.m`: return `False`.
   - Pick an arbitrary index of `val`: `idx = next(iter(self.m[val]))`.
   - Index of last element: $last\_idx = \text{len}(self.l) - 1$.
   - Overwrite slot `idx` with tail element:
     $$
     self.l[idx] \leftarrow self.l[last\_idx]
     $$
   - Remove `idx` from `val`'s set: `self.m[val].remove(idx)`.
   - Update tail element's index set:
     - Remove $last\_idx$ from its set: `self.m[tail].remove(last_idx)`.
     - If $idx < last\_idx$: add $idx$ to its set: `self.m[tail].add(idx)`.
   - If `val` has no remaining copies ($\text{len}(self.m[val]) == 0$): `self.m.pop(val)`.
   - Pop array tail: `self.l.pop()`.
   - Return `True`.
3. **`getRandom()`:**
   - Return `random.choice(self.l)`.

> **Invariant.** Array `self.l` has length $N$ with no gaps, and for every value $v$, `self.m[v]` holds precisely the set of indices where $v$ resides in `self.l`.

---

## 3. Step-by-Step Worked Execution

We trace operations: `insert(1)`, `insert(1)`, `insert(2)`, `getRandom()`, `remove(1)`:

---

### Step 1: `insert(1)`
- Current length: $\text{len}(l) = 0$.
- Add index $0$ to set: `m[1] = {0}`.
- Append to array: `l = [1]`.
- First copy added ($\text{len}(m[1]) == 1$) $\implies$ Return **`true`**.

---

### Step 2: `insert(1)` (Duplicate)
- Current length: $\text{len}(l) = 1$.
- Add index $1$ to set: `m[1] = {0, 1}`.
- Append to array: `l = [1, 1]`.
- Duplicate copy added ($\text{len}(m[1]) = 2 > 1$) $\implies$ Return **`false`**.

---

### Step 3: `insert(2)`
- Current length: $\text{len}(l) = 2$.
- Add index $2$ to set: `m[2] = {2}`.
- Append to array: `l = [1, 1, 2]`.
- First copy of 2 added $\implies$ Return **`true`**.
- State: `l = [1, 1, 2], m = {1: {0, 1}, 2: {2}}`.

---

### Step 4: `getRandom()`
- Array `l = [1, 1, 2]`.
- Selection probabilities:
  $$
  P(1) = \frac{2}{3}, \quad P(2) = \frac{1}{3}
  $$
- Returns $1$ with probability $66.7\%$ and $2$ with probability $33.3\%$.

---

### Step 5: `remove(1)` — Swap Tail to Deleted Slot
- Target value: $val = 1$.
- Choose an index from `m[1]`: $idx = 0$.
- Tail index: $last\_idx = \text{len}(l) - 1 = 3 - 1 = \mathbf{2}$.
- Tail value: $tail = l[2] = \mathbf{2}$.
- **Step A: Overwrite slot 0 with tail value 2:**
  $$
  l[0] \leftarrow 2 \implies l = [2, \; 1, \; 2]
  $$
- **Step B: Remove index 0 from `m[1]`:**
  $$
  m[1] = \{0, 1\} \setminus \{0\} = \{1\}
  $$
- **Step C: Update tail element's index set `m[2]`:**
  - Remove old index: $m[2] = \{2\} \setminus \{2\} = \emptyset$.
  - Add new slot ($idx = 0 < 2$): $m[2] = \emptyset \cup \{0\} = \{0\}$.
- **Step D: Pop tail from array:**
  $$
  l.\text{pop}() \implies l = [2, \; 1]
  $$
- Final State:
  $$
  l = [2, 1], \quad m = \{1: \{1\}, \; 2: \{0\}\}
  $$
- Return: **`true`**.

---

### Step 6: `getRandom()` After Removal
- Array is now `l = [2, 1]`.
- Equal copies: $P(1) = 1/2, P(2) = 1/2$.
- Uniform $50\%$ distribution between $1$ and $2$.

---

## 4. Complete Execution Trace

```text
RandomizedCollection State Evolution:
1. insert(1) -> l=[1],       m={1:{0}}           -> True
2. insert(1) -> l=[1, 1],    m={1:{0, 1}}        -> False
3. insert(2) -> l=[1, 1, 2], m={1:{0, 1}, 2:{2}} -> True
4. getRandom()-> choice([1, 1, 2])               -> 1 (prob 2/3), 2 (prob 1/3)
5. remove(1) -> target idx=0, tail=2 at idx=2
                l[0]=2, m[1]={1}, m[2]={0}
                l.pop() -> l=[2, 1]              -> True
6. getRandom()-> choice([2, 1])                  -> 1 (prob 1/2), 2 (prob 1/2)
```

| Step | Operation | Parameter | Array `l` State | Index Map `m` State | Condition Evaluated | Return Value |
|:---:|:---:|:---:|:---|:---|:---:|:---:|
| 1 | `insert` | 1 | `[1]` | `{1: {0}}` | First occurrence | **`true`** |
| 2 | `insert` | 1 | `[1, 1]` | `{1: {0, 1}}` | Duplicate | **`false`** |
| 3 | `insert` | 2 | `[1, 1, 2]` | `{1: {0, 1}, 2: {2}}` | First occurrence | **`true`** |
| 4 | `getRandom` | - | `[1, 1, 2]` | `{1: {0, 1}, 2: {2}}` | Samples uniformly from `l` | **$1$ ($2/3$) or $2$ ($1/3$)** |
| **5** | **`remove`** | **1** | **`[2, 1]`** | **`{1: {1}, 2: {0}}`** | **Tail 2 swapped into slot 0** | **`true`** |
| 6 | `getRandom` | - | `[2, 1]` | `{1: {1}, 2: {0}}` | Samples uniformly from `l` | **$1$ ($1/2$) or $2$ ($1/2$)** |

---

## 5. Algorithmic Correctness

**Soundness.** When `remove(val)` is invoked, an occurrence of `val` is swapped with the last element of `l`, and the array is popped. The tail element's index in `m` is updated to the freed slot, preserving bijection between `l` and `m`. Because only one copy of `val` is removed, the remaining multiplicity of `val` is decremented by exactly 1.

**Completeness.** Since all copies are stored in `l`, an element with multiplicity $k$ occupies exactly $k$ out of $N$ positions in `l`. By the definition of uniform random discrete choice, the probability of selecting an element with multiplicity $k$ is $k/N$, satisfying the exact proportional probability requirement.

---

## 6. Traps This Instance Exposes

- **Tail Self-Removal ($idx == last\_idx$):** When removing an element that is already at the end of `l`, swapping it with itself and blindly adding $idx$ back to its set would erroneously resurrect the deleted index! The condition `if idx < last_idx:` prevents this bug.
- **Removing from `last_idx_set` before `idx_set`:** Updating the index set of the moved tail element must account for cases where $val == l[last\_idx]$ (i.e. removing a duplicate when another duplicate of the same value is at the tail).
- **Index Set Extraction:** Extracting an arbitrary element from a hash set using `next(iter(s))` runs in $O(1)$ average time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `insert(val)`: $O(1)$ average time for set insertion and list append.
  - `remove(val)`: $O(1)$ average time for set lookup, tail swap, and array pop.
  - `getRandom()`: $O(1)$ time to sample a random index.
- **Auxiliary Space Complexity:** $O(N)$, where $N$ is the total number of element occurrences, storing array `l` and index sets in `m`.
