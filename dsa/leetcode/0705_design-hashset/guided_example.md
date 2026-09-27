# Guided Example: Design HashSet

We trace the step-by-step key space mapping ($key \in [0, 10^6]$), direct-address boolean bitmask indexing ($data[key] \in \{0, 1\}$), bucket hashing with separate chaining ($h(key) = key \pmod M$), insertion idempotency ($add(k)$), safe absent deletion ($remove(k)$), and constant-time membership querying ($contains(k)$) on representative hash set lifecycle events:

- **Input:**
  - Operations sequence:
    ```text
    MyHashSet()
    add(1)
    contains(1)
    remove(1)
    contains(1)
    ```
- **Required output:** `[true, false]`
  - Hash Set operations:
    - `add(key)`: Inserts $key$ into the set. If $key$ already exists, the set remains unchanged (idempotence).
    - `contains(key)`: Returns `true` if $key$ is currently in the set, otherwise `false`.
    - `remove(key)`: Removes $key$ from the set. If $key$ is not present, performs no action.
    - Lifecycle trace:
      - Initially empty.
      - `add(1)`: Value $1$ is registered.
      - `contains(1)`: Value $1$ is present $\implies$ returns `true`.
      - `remove(1)`: Value $1$ is unregistered.
      - `contains(1)`: Value $1$ is absent $\implies$ returns `false`.
      - Results: `[true, false]`.
- **Direct-Address & Chaining Architecture Invariants:**
  - **1. Direct-Address Table (Fixed Upper Bound):**
    - The problem constraints guarantee $0 \le key \le 10^6$.
    - A direct boolean array $data$ of length $1000001$ maps every integer directly to its dedicated slot:
      $$
      data[key] = \begin{cases} \text{true} & \text{if } key \in \text{Set} \\ \text{false} & \text{if } key \notin \text{Set} \end{cases}
      $$
    - Every operation (`add`, `remove`, `contains`) executes as a single memory dereference in strictly deterministic $O(1)$ time with zero collision handling needed.
  - **2. Bucket Chaining Alternative ($M$ Buckets):**
    - When memory conservation is prioritized, allocate $M$ buckets (e.g. prime $M = 769$).
    - Hash function:
      $$
      h(key) = key \pmod M
      $$
    - Each bucket maintains a small linked list or dynamic list of keys mapped to that hash residue.
    - Resolves collisions via separate chaining.
- **Step-by-Step Worked Execution Trace on the Lifecycle Operations:**
  - Initialize table:
    $$
    data = [\text{false}, \text{false}, \dots] \quad (\text{length } 1000001)
    $$
  - **Operation 1: `add(1)`:**
    - Target key: $1$.
    - Dereference slot: $data[1]$.
    - Set boolean flag:
      $$
      data[1] \leftarrow \mathbf{true}
      $$
    - Returns: `None`.
  - **Operation 2: `contains(1)`:**
    - Target key: $1$.
    - Query slot:
      $$
      data[1] == \mathbf{true}
      $$
    - Emit output:
      $$
      ans \leftarrow \mathbf{true}
      $$
  - **Operation 3: `remove(1)`:**
    - Target key: $1$.
    - Dereference slot: $data[1]$.
    - Reset boolean flag:
      $$
      data[1] \leftarrow \mathbf{false}
      $$
    - Returns: `None`.
  - **Operation 4: `contains(1)`:**
    - Target key: $1$.
    - Query slot:
      $$
      data[1] == \mathbf{false}
      $$
    - Emit output:
      $$
      ans \leftarrow \mathbf{false}
      $$
  - **Step 5: Consolidated Response:**
    $$
    [\mathbf{true}, \; \mathbf{false}]
    $$
- **Chaining Collision & Multi-Key Trace ($M = 5$):**
  - Insert keys $2, 7, 12$:
    - $h(2) = 2 \pmod 5 = 2 \implies bucket[2] = [2]$.
    - $h(7) = 7 \pmod 5 = 2 \implies bucket[2] = [2, 7]$ (Collision resolved by appending).
    - $h(12) = 12 \pmod 5 = 2 \implies bucket[2] = [2, 7, 12]$.
  - `contains(7)`: Scans $bucket[2]$, finds 7 $\implies$ returns `true`.
  - `remove(7)`: Deletes 7 from $bucket[2] \implies bucket[2] = [2, 12]$.
  - `contains(7)`: Scans $bucket[2]$, not found $\implies$ returns `false`.
- **Safe Removal of Absent Key:**
  - `remove(99)` when 99 was never inserted:
    - $data[99] = \text{false} \implies data[99] \leftarrow \text{false}$ (Harmless no-op).

This instance demonstrates foundational dictionary membership abstractions and collision-free direct address table indexing, mathematically proves why bounded key domains allow $O(1)$ worst-case bitwise set membership without hashing overhead, and derives $O(1)$ operation time and $O(U)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a sequence of operations:
Implement a **HashSet** supporting `add(key)`, `remove(key)`, and `contains(key)` without using built-in hash table libraries.

```text
Operations:
  add(1)      -> 1 is inserted
  contains(1) -> returns true
  remove(1)   -> 1 is removed
  contains(1) -> returns false

Result: [ true, false ]
```

### The Invariant of Direct Address Mapping
- Because key values are bounded by $10^6$, a direct boolean array gives guaranteed $O(1)$ operations:
  - `data[key] = True` (insert)
  - `data[key] = False` (delete)
  - `return data[key]` (lookup)
- No collisions, no hash recalculation, no pointer chasing.

---

## 2. Conceptual Foundation & Invariants

### 1. Operations Definition:
$$
\text{add}(k): \quad data[k] \leftarrow \mathbf{True}
$$
$$
\text{remove}(k): \quad data[k] \leftarrow \mathbf{False}
$$
$$
\text{contains}(k): \quad \text{return } data[k]
$$

### 2. Set Multiplicity Invariance:
For all $k$:
$$
|\{k\} \cap \text{Set}| \in \{0, 1\}
$$
Inserting an already present key leaves the set state identical.

> **Characteristic Function Isomorphism Invariant.** Any subset $S \subseteq \{0, 1, \dots, U\}$ is uniquely characterized by its indicator vector $\mathbf{1}_S \in \{0, 1\}^{U+1}$, enabling complete set algebra via direct component-wise boolean assignment.

---

## 3. Step-by-Step Worked Execution

We trace the sample operations:

---

### Step 1: `add(1)`
- $data[1] \leftarrow \text{True}$.

---

### Step 2: `contains(1)`
- $data[1]$ is $\text{True} \implies$ Return **`true`**.

---

### Step 3: `remove(1)`
- $data[1] \leftarrow \text{False}$.

---

### Step 4: `contains(1)`
- $data[1]$ is $\text{False} \implies$ Return **`false`**.

---

### Step 5: Output
$$
[\mathbf{true}, \; \mathbf{false}]
$$

---

## 4. Complete Execution Trace

| Step | Method Invocation | Key Tested | Internal Slot $data[key]$ | State Change | Query Return |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | `add(1)` | $1$ | $data[1] \leftarrow \text{True}$ | Unset $\to$ Set | — |
| **$2$** | **`contains(1)`** | **$1$** | **$data[1] == \text{True}$** | None | **`true`** |
| $3$ | `remove(1)` | $1$ | $data[1] \leftarrow \text{False}$ | Set $\to$ Unset | — |
| **$4$** | **`contains(1)`** | **$1$** | **$data[1] == \text{False}$** | None | **`false`** |

---

## 5. Boundary Cases & Failure Modes

- **Key Zero ($key = 0$):** Valid index $data[0] \implies$ handled normally.
- **Maximum Key ($key = 10^6$):** Size $10^6 + 1$ covers up to $data[1000000]$.
- **Removing Absent Key:** Setting `data[key] = False` when already `False` is completely safe.
- **Duplicate Additions:** Setting `data[key] = True` multiple times maintains idempotency.

---

## 6. Traps & Common Anti-Patterns

- **Array Sizing Off-by-One:** An array of size $10^6$ crashes on index $10^6$. Array must have size at least $10^6 + 1$.
- **Searching an Unsorted List ($O(N)$):** Appending keys to a list and scanning linearly for `contains` produces $O(N)$ per query, resulting in Time Limit Exceeded.
- **Using Built-in Hash Sets (`set`):** The problem explicitly requires designing the structure from scratch without using language hash tables.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `add(key)`: $\mathcal{O}(1)$ direct array write.
  - `remove(key)`: $\mathcal{O}(1)$ direct array write.
  - `contains(key)`: $\mathcal{O}(1)$ direct array read.
  - All operations run in deterministic strictly constant time $\mathcal{O}(1)$. Completes $10^4$ operations in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(U)$ where $U = 10^6$ boolean flags ($\approx 1$ MB of memory).