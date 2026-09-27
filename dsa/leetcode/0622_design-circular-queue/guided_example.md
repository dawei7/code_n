# Guided Example: Design Circular Queue

We trace the step-by-step fixed-capacity ring buffer array allocation ($q$), modular pointer wrapping ($(front + size) \pmod k$), stateful size tracking ($size \in [0, k]$), FIFO insertion and deletion boundaries, full queue rejection, and front/rear element retrieval on representative circular queue operation sequences:

- **Input:**
  - Initialization: $k = 3$ (Capacity is $3$)
  - Operation stream:
    ```text
    MyCircularQueue q = new MyCircularQueue(3);
    q.enQueue(1); // return True
    q.enQueue(2); // return True
    q.enQueue(3); // return True
    q.enQueue(4); // return False (queue is full)
    q.Rear();     // return 3
    q.isFull();   // return True
    q.deQueue();  // return True (removes 1)
    q.enQueue(4); // return True (inserts 4 at wrapped position)
    q.Rear();     // return 4
    ```
- **Required outputs:**
  - `true`, `true`, `true`, `false`, `3`, `true`, `true`, `true`, `4`
  - Ring buffer characteristics:
    - Fixed memory footprint of exactly $k$ slots.
    - Constant time $\mathcal{O}(1)$ for all operations without memory reallocation.
    - Wrap-around reuse of vacated front slots via modular arithmetic.
- **Ring Buffer Mathematical Architecture:**
  - Maintain:
    - Array $q$ of length $k$.
    - Integer `front`: 0-based index of the current head element.
    - Integer `size`: current number of active elements in the queue.
    - Constant `capacity = k`.
  - **Invariants:**
    1. **Empty predicate:** $size == 0$.
    2. **Full predicate:** $size == capacity$.
    3. **Enqueue destination index:**
       $$
       \text{insert\_index} = (front + size) \pmod{capacity}
       $$
    4. **Front element index:** $front$ (valid if not empty).
    5. **Rear element index:**
       $$
       \text{rear\_index} = (front + size - 1) \pmod{capacity}
       $$
    6. **Dequeue step:** $front \leftarrow (front + 1) \pmod{capacity}$, $size \leftarrow size - 1$.
- **Step-by-Step Worked Operation Trace:**
  - **Init: `MyCircularQueue(3)`:**
    - Array: $q = [0, 0, 0]$
    - $capacity = 3, \; front = 0, \; size = 0$.
  - **Op 1: `enQueue(1)`:**
    - Is full? $size = 0 < 3 \implies$ No.
    - Calculate insert index:
      $$
      idx = (0 + 0) \pmod 3 = \mathbf{0}
      $$
    - Store: $q[0] = 1$.
    - $size \leftarrow 0 + 1 = \mathbf{1}$.
    - State: $q = [\mathbf{1}, 0, 0]$, $front = 0$, $size = 1$.
    - Returns: **`true`**.
  - **Op 2: `enQueue(2)`:**
    - Insert index: $(0 + 1) \pmod 3 = \mathbf{1}$.
    - Store: $q[1] = 2$.
    - $size \leftarrow 1 + 1 = \mathbf{2}$.
    - State: $q = [1, \mathbf{2}, 0]$, $front = 0$, $size = 2$.
    - Returns: **`true`**.
  - **Op 3: `enQueue(3)`:**
    - Insert index: $(0 + 2) \pmod 3 = \mathbf{2}$.
    - Store: $q[2] = 3$.
    - $size \leftarrow 2 + 1 = \mathbf{3}$.
    - State: $q = [1, 2, \mathbf{3}]$, $front = 0$, $size = 3$.
    - Returns: **`true`**.
  - **Op 4: `enQueue(4)`:**
    - Check capacity: $size = 3 == capacity = 3 \implies \mathbf{isFull() == True}$.
    - Cannot enqueue into a full buffer!
    - Returns: **`false`**.
  - **Op 5: `Rear()`:**
    - Is empty? $size = 3 > 0 \implies$ No.
    - Calculate rear index:
      $$
      rear = (front + size - 1) \pmod 3 = (0 + 3 - 1) \pmod 3 = \mathbf{2}
      $$
    - Returns element $q[2]$:
      $$
      \mathbf{3}
      $$
  - **Op 6: `isFull()`:**
    - $size == 3 == capacity \implies$ Returns **`true`**.
  - **Op 7: `deQueue()`:**
    - Is empty? $size = 3 > 0 \implies$ No.
    - Advance front pointer:
      $$
      front \leftarrow (0 + 1) \pmod 3 = \mathbf{1}
      $$
    - Decrement size:
      $$
      size \leftarrow 3 - 1 = \mathbf{2}
      $$
    - Active queue now spans from index 1 to index 2: $[-, 2, 3]$.
    - Returns: **`true`**.
  - **Op 8: `enQueue(4)`:**
    - Is full? $size = 2 < 3 \implies$ No!
    - Calculate insert index:
      $$
      idx = (front + size) \pmod 3 = (1 + 2) \pmod 3 = 3 \pmod 3 = \mathbf{0}
      $$
    - Notice wrap-around: Slot 0 was vacated by the previous dequeue!
    - Store: $q[0] = 4$.
    - $size \leftarrow 2 + 1 = \mathbf{3}$.
    - State: $q = [\mathbf{4}, 2, 3]$, $front = 1$, $size = 3$.
    - Returns: **`true`**.
  - **Op 9: `Rear()`:**
    - Calculate rear index:
      $$
      rear = (front + size - 1) \pmod 3 = (1 + 3 - 1) \pmod 3 = 3 \pmod 3 = \mathbf{0}
      $$
    - Returns element $q[0]$:
      $$
      \mathbf{4}
      $$
- **Underflow Boundary Handling:**
  - Calling `deQueue()`, `Front()`, or `Rear()` on an empty queue ($size == 0$) safely returns `false` or `-1` without index exceptions.

This instance demonstrates modular ring buffer state transitions, mathematically proves why tracking explicit `size` avoids full/empty pointer ambiguity without wasting an array slot, and derives $O(1)$ runtime and $O(K)$ space bounds.

---

## 1. Instance & Teaching Goal

Implement a **Circular Queue (Ring Buffer)** of fixed size $k$:
Support `enQueue`, `deQueue`, `Front`, `Rear`, `isEmpty`, and `isFull` in strictly $O(1)$ time and memory.

```text
Circular Buffer (Capacity 3):
  1. enQueue(1) -> [ 1,  _,  _ ]  front = 0, size = 1
  2. enQueue(2) -> [ 1,  2,  _ ]  front = 0, size = 2
  3. enQueue(3) -> [ 1,  2,  3 ]  front = 0, size = 3 (Full!)
  4. enQueue(4) -> Rejected! (isFull)
  5. deQueue()  -> [ _,  2,  3 ]  front = 1, size = 2 (Slot 0 freed!)
  6. enQueue(4) -> [ 4,  2,  3 ]  front = 1, size = 3 (Wrapped to 0!)
     Rear is now 4 (at index 0).
```

### Eliminating the "One Slot Waste" Ambiguity
- In classic circular buffers using only `head` and `tail` pointers, `head == tail` can mean either completely empty or completely full, often requiring leaving one slot empty (wasting capacity).
- By maintaining an explicit **`size` integer variable**:
  - Empty is unambiguously $size == 0$.
  - Full is unambiguously $size == capacity$.
  - All $k$ slots can be fully utilized.

---

## 2. Conceptual Foundation & Invariants

### 1. Pointer Calculations:
- Next element to write:
  $$
  idx_{write} = (front + size) \pmod k
  $$
- Element at rear:
  $$
  idx_{rear} = (front + size - 1) \pmod k
  $$
- Next element to remove:
  $$
  idx_{read} = front
  $$

### 2. State Invariant:
At all times:
$$
0 \le size \le k, \quad 0 \le front < k
$$

> **Toroidal Index Invariant.** Mapping unbounded linear sequence coordinates $t \in \mathbb{N}$ through the projection $t \pmod k$ creates an isometric ring topology with constant cyclic storage.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Enqueue 1, 2, 3
- Enqueue 1: $q[0] = 1, size = 1$.
- Enqueue 2: $q[1] = 2, size = 2$.
- Enqueue 3: $q[2] = 3, size = 3$.

---

### Step 2: Enqueue 4 (Full)
- $size = 3 == k \implies$ Reject $\to \mathbf{false}$.

---

### Step 3: Inspect Rear and Fullness
- `Rear()`: index $(0 + 3 - 1) \pmod 3 = 2 \implies q[2] = \mathbf{3}$.
- `isFull()`: $3 == 3 \implies \mathbf{true}$.

---

### Step 4: Dequeue and Enqueue 4
- `deQueue()`: $front \leftarrow (0 + 1) \pmod 3 = 1, size \leftarrow 2$.
- `enQueue(4)`: write at $(1 + 2) \pmod 3 = 0 \implies q[0] = 4, size = 3$.
- `Rear()`: index $(1 + 3 - 1) \pmod 3 = 0 \implies q[0] = \mathbf{4}$.

---

## 4. Complete Execution Trace

| Call | Arguments | Buffer State $q$ | $front$ | $size$ | Condition Checked | Return Value |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `enQueue` | $1$ | $[1, 0, 0]$ | $0$ | $1$ | $size < 3$ | **`true`** |
| `enQueue` | $2$ | $[1, 2, 0]$ | $0$ | $2$ | $size < 3$ | **`true`** |
| `enQueue` | $3$ | $[1, 2, 3]$ | $0$ | $3$ | $size < 3$ | **`true`** |
| `enQueue` | $4$ | $[1, 2, 3]$ | $0$ | $3$ | $size == 3$ (Full) | **`false`** |
| `Rear` | — | $[1, 2, 3]$ | $0$ | $3$ | Query rear index 2 | **`3`** |
| `isFull` | — | $[1, 2, 3]$ | $0$ | $3$ | $size == 3$ | **`true`** |
| `deQueue` | — | $[1, 2, 3]$ | **$1$** | **$2$** | Advance front to 1 | **`true`** |
| `enQueue` | $4$ | $[4, 2, 3]$ | $1$ | **$3$** | Write wrapped slot 0 | **`true`** |
| `Rear` | — | $[4, 2, 3]$ | $1$ | $3$ | Query rear index 0 | **`4`** |

---

## 5. Boundary Cases & Failure Modes

- **Capacity $k = 1$:** Transitions directly between empty ($size = 0$) and full ($size = 1$).
- **`Front()` / `Rear()` on Empty Queue:** Returns `-1`.
- **`deQueue()` on Empty Queue:** Returns `false`.
- **Many Alternating Enqueue / Dequeue Cycles:** Circular index wraps smoothly indefinitely without buffer overflow.

---

## 6. Traps & Common Anti-Patterns

- **Dynamic Array Resizing (`list.pop(0)`):** Using standard list shifting takes $O(N)$ per dequeue. A circular array must update the `front` pointer in $O(1)$ time without shifting elements.
- **Negative Index on Modulo in Other Languages:** In C++/Java, `(-1) % k` can return a negative number. Using `(front + size - 1 + k) % k` in code avoids negative values.
- **Failing to Wrap `front` on Dequeue:** Forgetting modulo `(front + 1) % capacity` causes `front` to march out of array bounds.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Constructor: $\mathcal{O}(k)$ to initialize the fixed array.
  - `enQueue`, `deQueue`, `Front`, `Rear`, `isEmpty`, `isFull`: strictly $\mathcal{O}(1)$ constant time for every individual operation.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(k)$ space to store the fixed-size ring buffer array. Zero dynamic allocations.
