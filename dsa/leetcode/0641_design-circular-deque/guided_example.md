# Guided Example: Design Circular Deque

We trace the step-by-step fixed-size ring buffer array allocation ($q$), bidirectional pointer wrapping ($(front \pm 1) \pmod k$), stateful size tracking ($size \in [0, k]$), front and rear double-ended insertions and deletions, boundary overflow rejections, and $\mathcal{O}(1)$ element inspections on representative circular deque operation sequences:

- **Input:**
  - Initialization: $k = 3$ (Capacity is $3$)
  - Operation sequence:
    ```text
    MyCircularDeque deque = new MyCircularDeque(3);
    deque.insertLast(1);  // return True, buffer has [1]
    deque.insertLast(2);  // return True, buffer has [1, 2]
    deque.insertFront(3); // return True, wraps front to slot 2, buffer has [3, 1, 2]
    deque.insertFront(4); // return False, buffer is full
    deque.getRear();      // return 2
    deque.isFull();       // return True
    deque.deleteLast();   // return True, removes 2, size becomes 2
    deque.insertFront(4); // return True, wraps front to slot 1, buffer has [4, 3, 1]
    deque.getFront();     // return 4
    ```
- **Required outputs:**
  - `[null, true, true, true, false, 2, true, true, true, 4]`
  - Deque architectural invariants:
    - Fixed memory buffer of length $k$ (zero dynamic reallocations).
    - True $\mathcal{O}(1)$ time complexity for all front/rear push, pop, and peek operations.
    - Symmetric circular modulo addressing in both clockwise (rear) and counter-clockwise (front) directions.
- **Ring Buffer Bidirectional Pointer Architecture:**
  - Maintain:
    - Array $q$ of fixed length $k$.
    - Integer `front`: 0-based index of the current head element.
    - Integer `size`: current number of elements ($0 \le size \le k$).
    - Constant `capacity = k`.
  - **Symmetric Operation Protocols:**
    1. **`insertFront(value)`:**
       - If $size == capacity \implies$ return `false`.
       - If not empty, decrement `front` with modulo wrap:
         $$
         front \leftarrow (front - 1 + capacity) \pmod{capacity}
         $$
       - Assign: $q[front] \leftarrow value$.
       - $size \leftarrow size + 1$. Return `true`.
    2. **`insertLast(value)`:**
       - If $size == capacity \implies$ return `false`.
       - Calculate write slot at rear:
         $$
         idx = (front + size) \pmod{capacity}
         $$
       - Assign: $q[idx] \leftarrow value$.
       - $size \leftarrow size + 1$. Return `true`.
    3. **`deleteFront()`:**
       - If $size == 0 \implies$ return `false`.
       - Advance `front`:
         $$
         front \leftarrow (front + 1) \pmod{capacity}
         $$
       - $size \leftarrow size - 1$. Return `true`.
    4. **`deleteLast()`:**
       - If $size == 0 \implies$ return `false`.
       - Simply reduce count: $size \leftarrow size - 1$. Return `true`.
    5. **`getFront()`:**
       - Return $-1$ if $size == 0$, else $q[front]$.
    6. **`getRear()`:**
       - Return $-1$ if $size == 0$, else $q[(front + size - 1) \pmod{capacity}]$.
- **Step-by-Step Worked Operation Trace:**
  - **Init: `MyCircularDeque(3)`:**
    - Buffer: $q = [0, 0, 0]$, $front = 0, \; size = 0, \; capacity = 3$.
  - **Op 1: `insertLast(1)`:**
    - Is full? $0 < 3$.
    - Write index: $(0 + 0) \pmod 3 = \mathbf{0}$.
    - Store: $q[0] = 1$.
    - $size \leftarrow 1$. State: $q = [\mathbf{1}, 0, 0], front = 0, size = 1$.
    - Returns: **`true`**.
  - **Op 2: `insertLast(2)`:**
    - Write index: $(0 + 1) \pmod 3 = \mathbf{1}$.
    - Store: $q[1] = 2$.
    - $size \leftarrow 2$. State: $q = [1, \mathbf{2}, 0], front = 0, size = 2$.
    - Returns: **`true`**.
  - **Op 3: `insertFront(3)`:**
    - Buffer is not full ($2 < 3$).
    - Queue is not empty ($size = 2 > 0$): decrement `front` counter-clockwise:
      $$
      front \leftarrow (0 - 1 + 3) \pmod 3 = 2 \pmod 3 = \mathbf{2}
      $$
    - Store: $q[2] = 3$.
    - $size \leftarrow 2 + 1 = \mathbf{3}$.
    - Buffer physical layout:
      $$
      q = [1, \; 2, \; \mathbf{3}], \quad front = 2, \quad size = 3
      $$
    - Logical order (front to rear): $3$ (at index 2) $\to 1$ (at index 0) $\to 2$ (at index 1).
    - Returns: **`true`**.
  - **Op 4: `insertFront(4)`:**
    - Check capacity: $size = 3 == capacity \implies \mathbf{isFull() == True}$.
    - Cannot insert into full deque!
    - Returns: **`false`**.
  - **Op 5: `getRear()`:**
    - Calculate rear index:
      $$
      rear = (front + size - 1) \pmod 3 = (2 + 3 - 1) \pmod 3 = 4 \pmod 3 = \mathbf{1}
      $$
    - Read $q[1]$:
      $$
      \mathbf{2}
      $$
  - **Op 6: `isFull()`:**
    - $size == 3 == capacity \implies$ Returns **`true`**.
  - **Op 7: `deleteLast()`:**
    - $size = 3 > 0 \implies$ Not empty.
    - Simply decrement size:
      $$
      size \leftarrow 3 - 1 = \mathbf{2}
      $$
    - Active deque now has elements at indices $2$ and $0$ (values $3$ and $1$).
    - Returns: **`true`**.
  - **Op 8: `insertFront(4)`:**
    - Is full? $size = 2 < 3 \implies$ Not full!
    - Decrement `front`:
      $$
      front \leftarrow (2 - 1 + 3) \pmod 3 = 4 \pmod 3 = \mathbf{1}
      $$
    - Notice wrap-around reuse: Slot 1 (freed by `deleteLast`) now receives the new front element!
    - Store: $q[1] = 4$.
    - $size \leftarrow 2 + 1 = \mathbf{3}$.
    - Buffer state: $q = [1, \mathbf{4}, 3], front = 1, size = 3$.
    - Returns: **`true`**.
  - **Op 9: `getFront()`:**
    - Read element at $front = 1$:
      $$
      q[1] = \mathbf{4}
      $$

This instance demonstrates symmetric ring buffer pointer mechanics, mathematically proves why explicit size tracking decouples boundary collisions under bidirectional insertion, and derives $O(1)$ runtime and $O(K)$ space bounds.

---

## 1. Instance & Teaching Goal

Implement a **Circular Double-Ended Queue (Deque)** of fixed size $k$:
Support `insertFront`, `insertLast`, `deleteFront`, `deleteLast`, `getFront`, `getRear`, `isEmpty`, `isFull` in strictly $O(1)$ time and memory.

```text
Capacity k = 3:
  1. insertLast(1)  -> [ 1,  _,  _ ]  front = 0, size = 1
  2. insertLast(2)  -> [ 1,  2,  _ ]  front = 0, size = 2
  3. insertFront(3) -> [ 1,  2,  3 ]  front = 2, size = 3 (Full!)
  4. insertFront(4) -> REJECTED (Full)
  5. deleteLast()   -> removes 2 -> size = 2 (front still 2, elements are 3 and 1)
  6. insertFront(4) -> [ 1,  4,  3 ]  front = 1, size = 3 (Wrapped to 1!)
     getFront() returns 4
```

### Bidirectional Circular Wrapping
- Advancing right (clockwise): $(idx + 1) \pmod k$.
- Advancing left (counter-clockwise): $(idx - 1 + k) \pmod k$.
- Adding $k$ before modulo prevents negative index values in languages with truncating division.

---

## 2. Conceptual Foundation & Invariants

### 1. Pointer Formulas:
- Insert Front:
  $$
  front_{new} = (front - 1 + k) \pmod k
  $$
- Insert Rear:
  $$
  idx_{write} = (front + size) \pmod k
  $$
- Delete Front:
  $$
  front_{new} = (front + 1) \pmod k
  $$
- Inspect Rear:
  $$
  idx_{rear} = (front + size - 1) \pmod k
  $$

### 2. State Invariants:
$$
0 \le size \le k, \quad 0 \le front < k
$$

> **Toroidal Ring Duality Invariant.** Clockwise and counter-clockwise pointer steps are group inverses in $\mathbb{Z}_k$, establishing bidirectional FIFO and LIFO operations over a shared modular array.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: `insertLast(1)`, `insertLast(2)`
- $q[0] = 1, q[1] = 2$.
- $front = 0, size = 2$.

---

### Step 2: `insertFront(3)`
- $front \leftarrow (0 - 1 + 3) \pmod 3 = 2$.
- $q[2] = 3$.
- $size = 3$.

---

### Step 3: `deleteLast()`
- $size \leftarrow 2$.
- Active range: indices 2 and 0.

---

### Step 4: `insertFront(4)`
- $front \leftarrow (2 - 1 + 3) \pmod 3 = 1$.
- $q[1] = 4, size = 3$.
- `getFront()` reads $q[1] = \mathbf{4}$.

---

## 4. Complete Execution Trace

| Call | Value | Buffer $q$ | $front$ | $size$ | Operation Detail | Result |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `insertLast` | $1$ | $[1, 0, 0]$ | $0$ | $1$ | Write index 0 | **`true`** |
| `insertLast` | $2$ | $[1, 2, 0]$ | $0$ | $2$ | Write index 1 | **`true`** |
| `insertFront` | $3$ | $[1, 2, 3]$ | **$2$** | **$3$** | Step front to 2, write $q[2]$ | **`true`** |
| `insertFront` | $4$ | $[1, 2, 3]$ | $2$ | $3$ | $size == 3$ (Full) | **`false`** |
| `getRear` | — | $[1, 2, 3]$ | $2$ | $3$ | Index $(2+3-1)\%3 = 1$ | **`2`** |
| `deleteLast` | — | $[1, 2, 3]$ | $2$ | **$2$** | Decrement size | **`true`** |
| `insertFront` | $4$ | $[1, 4, 3]$ | **$1$** | **$3$** | Step front to 1, write $q[1]$ | **`true`** |
| `getFront` | — | $[1, 4, 3]$ | $1$ | $3$ | Read $q[front] = q[1]$ | **`4`** |

---

## 5. Boundary Cases & Failure Modes

- **Capacity $k = 1$:** Flips between size 0 and size 1.
- **Empty Inspections (`getFront` / `getRear` on empty):** Safely returns $-1$.
- **Empty Deletions:** Returns `false`.
- **Many Reversals (Front push, Rear pop, Front pop, Rear push):** Modulo indices maintain consistent circular topology indefinitely.

---

## 6. Traps & Common Anti-Patterns

- **Negative Modulo in C++/Java:** In C++, `(-1) % k` produces `-1`, which causes an array out-of-bounds crash. Always add `k`: `(front - 1 + k) % k`.
- **Moving `front` on First Element Insert:** If $size == 0$, inserting at front should set $q[front] = value$ without decrementing `front` beforehand, or maintain consistent conventions throughout.
- **Using Dynamic List Shifting:** Python `list.insert(0)` is $O(N)$. Ring buffer implementation must be strictly $O(1)$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Constructor: $\mathcal{O}(k)$ to initialize array.
  - All 8 operations (`insertFront`, `insertLast`, `deleteFront`, `deleteLast`, `getFront`, `getRear`, `isEmpty`, `isFull`): strictly $\mathcal{O}(1)$ constant time.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(k)$ auxiliary space for the fixed array.
