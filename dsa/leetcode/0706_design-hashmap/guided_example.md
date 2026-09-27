# Guided Example: Design HashMap

We trace the step-by-step key-value dictionary mapping, direct-address array indexing with sentinel initialization ($data[key] = -1$), overwrite mutation semantics ($put(k, v)$), absent-key lookup detection ($get(k) = -1$), safe idempotent key deletion ($remove(k) \implies data[k] \leftarrow -1$), and constant-time key retrieval on representative associative map operations:

- **Input:**
  - Operations sequence:
    ```text
    MyHashMap()
    put(1, 10)
    get(1)
    get(2)
    ```
- **Required output:** `[10, -1]`
  - Map operational requirements:
    - `put(key, value)`: Associates $key$ with $value$. If $key$ already exists, the old value is overwritten with the new value.
    - `get(key)`: Retrieves the value associated with $key$. If $key$ is not currently mapped, returns $-1$.
    - `remove(key)`: Deletes the key-value association. If $key$ does not exist, performs no action.
    - Lifecycle trace:
      - `put(1, 10)`: Stores mapping $(1 \mapsto 10)$.
      - `get(1)`: Key 1 exists $\implies$ returns $10$.
      - `get(2)`: Key 2 has never been inserted $\implies$ returns $-1$.
      - Query answers: `[10, -1]`.
- **Direct-Address & Sentinel Initialization Invariant:**
  - **1. Direct-Address Table ($0 \le key \le 10^6$):**
    - The problem constraints guarantee all keys fall within the integer range $[0, 10^6]$.
    - A direct integer array $data$ of length $1000001$ maps each integer key to its exact memory index.
  - **2. The $-1$ Empty Sentinel Invariant:**
    - Initialize every entry in $data$ to $-1$:
      $$
      data[i] = -1 \quad \forall 0 \le i \le 10^6
      $$
    - Valid values are non-negative ($value \ge 0$).
    - Therefore, $data[key] == -1$ uniquely and unambiguously signifies that $key$ is **unmapped**.
  - **3. In-Place Overwrites and Removal:**
    - `put(key, value)`: Directly executes $data[key] \leftarrow value$, seamlessly handling both new insertions and overwriting existing keys in $O(1)$ time.
    - `get(key)`: Directly returns $data[key]$, which automatically evaluates to either the stored value or $-1$ for absent keys.
    - `remove(key)`: Resets $data[key] \leftarrow -1$.
- **Step-by-Step Worked Execution Trace on the Sample Operations:**
  - Initialize table:
    $$
    data = [-1, -1, \dots, -1] \quad (\text{length } 1000001)
    $$
  - **Operation 1: `put(1, 10)`:**
    - Key: $1$, Value: $10$.
    - Dereference slot: $data[1]$.
    - Store mapping:
      $$
      data[1] \leftarrow \mathbf{10}
      $$
    - Returns: `None`.
  - **Operation 2: `get(1)`:**
    - Target key: $1$.
    - Inspect slot:
      $$
      data[1] = 10
      $$
    - Since $data[1] \ne -1$, key is present.
    - Emit output:
      $$
      ans \leftarrow \mathbf{10}
      $$
  - **Operation 3: `get(2)`:**
    - Target key: $2$.
    - Inspect slot:
      $$
      data[2] = -1
      $$
    - Since $data[2] == -1$, key is absent.
    - Emit output:
      $$
      ans \leftarrow \mathbf{-1}
      $$
  - **Step 4: Consolidated Response:**
    $$
    [\mathbf{10}, \; \mathbf{-1}]
    $$
- **Key Overwrite and Removal Lifecycle Trace:**
  - Start with empty map.
  - `put(1, 1)`: $data[1] = 1$.
  - `put(2, 2)`: $data[2] = 2$.
  - `get(1)`: returns $1$.
  - `get(3)`: returns $-1$ (absent).
  - `put(2, 1)`: overwrites $data[2] \leftarrow 1$.
  - `get(2)`: returns $1$ (updated value).
  - `remove(2)`: sets $data[2] \leftarrow -1$.
  - `get(2)`: returns $-1$ (now absent).
- **Zero Key Handling ($key = 0, value = 0$):**
  - $data[0] = 0$.
  - `get(0)` returns $0 \ne -1$. The sentinel $-1$ cleanly distinguishes stored value $0$ from unmapped status.

This instance demonstrates associative array abstraction and bounded key-space direct indexing, mathematically proves why sentinel initialization eliminates secondary presence-tracking bits, and derives $O(1)$ operation time and $O(U)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a sequence of operations:
Implement a **HashMap** supporting `put(key, value)`, `get(key)`, and `remove(key)` without using built-in hash table libraries.
Unmapped keys return $-1$.

```text
Operations:
  put(1, 10) -> maps 1 to 10
  get(1)     -> returns 10
  get(2)     -> key 2 not present -> returns -1

Result: [ 10, -1 ]
```

### The Invariant of the Sentinel Initialized Table
- Pre-allocating an array of size $10^6 + 1$ with default value $-1$ allows keys to act as direct array indices.
- Because valid values are $\ge 0$, the value $-1$ uniquely indicates an empty slot.
- All operations execute in strictly 1 memory access.

---

## 2. Conceptual Foundation & Invariants

### 1. Operations Specification:
$$
\text{put}(k, v): \quad data[k] \leftarrow v
$$
$$
\text{get}(k): \quad \text{return } data[k]
$$
$$
\text{remove}(k): \quad data[k] \leftarrow -1
$$

### 2. Functional Mapping Invariance:
For any key $k$, at any point in time:
$$
data[k] = \begin{cases} v & \text{if } (k \mapsto v) \in \text{Map} \\ -1 & \text{if } k \notin \text{Map} \end{cases}
$$

> **Direct Addressing Total Injection Invariant.** The identity function $id: K \to [0, U]$ injects the finite key space into contiguous memory, transforming partial function evaluation $f: K \rightharpoonup V$ into a total array lookup $A \in (V \cup \{-1\})^{U+1}$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: `put(1, 10)`
- $data[1] \leftarrow 10$.

---

### Step 2: `get(1)`
- Read $data[1] = 10 \implies$ Return **`10`**.

---

### Step 3: `get(2)`
- Read $data[2] = -1 \implies$ Return **`-1`**.

---

### Step 4: Output
$$
[\mathbf{10}, \; \mathbf{-1}]
$$

---

## 4. Complete Execution Trace

| Step | Operation Called | Key $k$ | Argument Value $v$ | Array Slot $data[k]$ | Output Returned |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | `put(1, 10)` | $1$ | $10$ | $data[1] \leftarrow 10$ | — |
| **$2$** | **`get(1)`** | **$1$** | — | **$10$** | **`10`** |
| **$3$** | **`get(2)`** | **$2$** | — | **$-1$** | **`-1`** |

---

## 5. Boundary Cases & Failure Modes

- **Key Zero ($key = 0, value = 0$):** Stored at $data[0] = 0$; distinguishable from empty sentinel $-1$.
- **Maximum Key ($key = 10^6$):** Fits inside array of size $10^6 + 1$.
- **Overwriting Existing Key:** Subsequent `put(k, new_val)` cleanly overwrites `data[k]`.
- **Removing Absent Key:** Setting `data[k] = -1` when already $-1$ is a safe no-op.

---

## 6. Traps & Common Anti-Patterns

- **Confusing Value 0 with Absent Key:** If an empty slot is initialized to 0, storing `put(5, 0)` makes it impossible to distinguish between stored 0 and empty. Initializing to $-1$ is required.
- **Dynamic List Appending ($O(N)$):** Searching a list of pairs `[(k, v), ...]` takes $O(N)$ per query, resulting in Time Limit Exceeded. Direct addressing runs in guaranteed $O(1)$.
- **Using Built-in `dict`:** Prohibited by the problem statement.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `put(key, value)`: $\mathcal{O}(1)$ constant time array write.
  - `get(key)`: $\mathcal{O}(1)$ constant time array read.
  - `remove(key)`: $\mathcal{O}(1)$ constant time array write.
  - Total Time: strictly $\mathcal{O}(1)$ per operation. Completes $10^4$ operations in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(U)$ where $U = 10^6$ slots ($\approx 4$ MB of memory).
