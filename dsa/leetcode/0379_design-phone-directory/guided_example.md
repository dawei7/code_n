# Guided Example: Design Phone Directory

We trace the step-by-step pool allocation (`self.available.pop()`), membership availability verification (`number in self.available`), idempotent resource deallocation (`self.available.add(number)`), and exhaustion handling on representative phone directory command streams:

- **Input:** `maxNumbers = 3`, operations:
  1. `get()` $\implies 0$ (Allocated, remaining available: $\{1, 2\}$)
  2. `get()` $\implies 1$ (Allocated, remaining available: $\{2\}$)
  3. `check(2)` $\implies \text{true}$ ($2$ is still unassigned)
  4. `get()` $\implies 2$ (Allocated, remaining available: $\emptyset$)
  5. `check(2)` $\implies \text{false}$ ($2$ is currently in use)
  6. `release(2)` $\implies$ Frees number $2$ back into pool (available: $\{2\}$)
  7. `check(2)` $\implies \text{true}$ ($2$ is available again!)
- **Required output:** `[0, 1, true, 2, false, true]`
- **Exhaustion State:** Calling `get()` when `available` is empty returns $-1$
- **Idempotent Release:** Calling `release(x)` when $x$ is already available leaves the set intact without duplicates

This instance demonstrates resource pool management and object recycling patterns, mathematically proves why hash set / bitset structures guarantee strictly $O(1)$ time complexity for allocation, inspection, and recycling, and analyzes memory bounds.

---

## 1. Instance & Teaching Goal

Design a phone directory that manages numbers from $0$ to $maxNumbers - 1$ ($maxNumbers = 3$):
- `get()`: Provides an unassigned number, marking it as assigned. Returns $-1$ if all numbers are taken.
- `check(number)`: Tests whether `number` is currently available.
- `release(number)`: Frees a previously assigned `number`, making it available again.

```text
Initial Directory: Available Pool = {0, 1, 2}

Operation 1: get()      -> Assigns 0 -> Pool = {1, 2}
Operation 2: get()      -> Assigns 1 -> Pool = {2}
Operation 3: check(2)   -> 2 in Pool? -> TRUE
Operation 4: get()      -> Assigns 2 -> Pool = {} (Empty!)
Operation 5: check(2)   -> 2 in Pool? -> FALSE
Operation 6: release(2) -> Recycles 2 -> Pool = {2}
Operation 7: check(2)   -> 2 in Pool? -> TRUE
```

---

## 2. Conceptual Foundation & Invariants

### 1. The Resource Pool Structure
We maintain a hash set `self.available` initialized with all integers in $[0, maxNumbers - 1]$:
$$
\text{available} = \{0, 1, \dots, maxNumbers - 1\}
$$

### 2. Method Contracts:
1. **`get() -> int`:**
   - If `self.available` is empty:
     $$
     \text{return } \mathbf{-1}
     $$
   - Else: extract and return any element:
     $$
     \text{return } self.available.\text{pop}()
     $$
2. **`check(number: int) -> bool`:**
   - Directly query membership:
     $$
     \text{return } (number \in self.available)
     $$
3. **`release(number: int) -> None`:**
   - Re-insert number into the set:
     $$
     self.available.\text{add}(number)
     $$

> **Invariant.** An integer $x \in [0, maxNumbers - 1]$ belongs to `self.available` if and only if it is currently unassigned and eligible for acquisition.

---

## 3. Step-by-Step Worked Execution

We trace the operational sequence for $maxNumbers = 3$:
Initial state: `available = {0, 1, 2}`.

---

### Step 1: `get()`
- Query pool: `available = {0, 1, 2}` is non-empty.
- Pop element: extract $0$.
- Pool updates:
  $$
  available \leftarrow \{1, 2\}
  $$
- Return: **`0`**.

---

### Step 2: `get()`
- Query pool: `available = {1, 2}` is non-empty.
- Pop element: extract $1$.
- Pool updates:
  $$
  available \leftarrow \{2\}
  $$
- Return: **`1`**.

---

### Step 3: `check(2)`
- Query membership: $2 \in \{2\}$.
- Result: **`true`** ($2$ is free).

---

### Step 4: `get()`
- Query pool: `available = {2}`.
- Pop element: extract $2$.
- Pool updates:
  $$
  available \leftarrow \emptyset
  $$
- Return: **`2`**.

---

### Step 5: `check(2)`
- Query membership: $2 \in \emptyset$.
- Result: **`false`** ($2$ is currently assigned).

---

### Step 6: `release(2)`
- Add number back to available pool:
  $$
  available.\text{add}(2) \implies available = \{2\}
  $$
- No return value.

---

### Step 7: `check(2)`
- Query membership: $2 \in \{2\}$.
- Result: **`true`** ($2$ is restored to available status).

---

## 4. Complete Execution Trace

```text
PhoneDirectory(3): available = {0, 1, 2}

Call 1: get()      -> pop 0 -> available = {1, 2} -> returns 0
Call 2: get()      -> pop 1 -> available = {2}    -> returns 1
Call 3: check(2)   -> 2 in {2}                    -> returns True
Call 4: get()      -> pop 2 -> available = {}     -> returns 2
Call 5: check(2)   -> 2 in {}                     -> returns False
Call 6: release(2) -> add 2 -> available = {2}    -> None
Call 7: check(2)   -> 2 in {2}                    -> returns True

Result Stream: [0, 1, true, 2, false, true]
```

| Step | Operation Called | Parameter | Available Pool State Before | Set Action Performed | Available Pool State After | Return Value |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | `get()` | - | $\{0, 1, 2\}$ | `pop()` $\implies 0$ | $\{1, 2\}$ | **`0`** |
| 2 | `get()` | - | $\{1, 2\}$ | `pop()` $\implies 1$ | $\{2\}$ | **`1`** |
| 3 | `check(2)` | 2 | $\{2\}$ | $2 \in available$ | $\{2\}$ | **`true`** |
| 4 | `get()` | - | $\{2\}$ | `pop()` $\implies 2$ | $\emptyset$ | **`2`** |
| 5 | `check(2)` | 2 | $\emptyset$ | $2 \in available$ | $\emptyset$ | **`false`** |
| 6 | `release(2)` | 2 | $\emptyset$ | `add(2)` | $\{2\}$ | - |
| 7 | `check(2)` | 2 | $\{2\}$ | $2 \in available$ | $\{2\}$ | **`true`** |

---

## 5. Algorithmic Correctness

**Soundness.** Because a hash set stores unique elements, extracting an element via `.pop()` removes it from the pool, preventing it from being returned again until explicitly freed. Checking `number in self.available` returns `True` if and only if the number has not been allocated (or was re-added).

**Completeness.** Initializing with `set(range(maxNumbers))` contains all valid phone numbers. Because `.add()` is idempotent, releasing a number that was already free causes no corruption or duplicates.

---

## 6. Traps This Instance Exposes

- **Linear Scanning on `get()`:** Maintaining a boolean array `used[i]` and scanning from $0$ to $maxNumbers - 1$ on each `get()` takes $O(N)$ time per call. Storing available numbers in a set or queue guarantees $O(1)$ retrieval.
- **Duplicate Releases:** If `release(x)` is called multiple times on the same number, an ordinary queue would enqueue duplicate copies of $x$. A hash set or a boolean guard array `if used[x]: used[x] = False; queue.append(x)` prevents duplicates.
- **Order of Allocation:** The problem does not require assigning numbers in strict numerical order; any available number satisfies `get()`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `__init__(maxNumbers)`: $O(N)$, where $N = maxNumbers$, to construct the initial set.
  - `get()`: $O(1)$ average time to pop an element from the hash set.
  - `check(number)`: $O(1)$ average time for set lookup.
  - `release(number)`: $O(1)$ average time to insert into the hash set.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory to store up to $N$ integers in `self.available`.