# Guided Example: Implement Stack using Queues

We trace the step-by-step FIFO-to-LIFO order inversion, single-queue rotational reorganization, and dual-queue buffer swapping on representative stack operations:

- **Sequential Operations:**
  1. `MyStack()` (Initialize queue)
  2. `push(1)` ($q = [1]$)
  3. `push(2)` (Enqueues 2, then rotates 1 to back $\implies q = [2, 1]$)
  4. `top()` $\implies \mathbf{2}$ (Inspects front of queue)
  5. `pop()` $\implies \mathbf{2}$ (Dequeues front; remaining $q = [1]$)
  6. `empty()` $\implies \mathbf{false}$ ($q$ contains 1)
- **Empty State After Drain:** `pop()` returns $1 \implies \text{empty}()$ returns `true`

This instance demonstrates implementing Last-In-First-Out (LIFO) semantics strictly through First-In-First-Out (FIFO) queue primitives (push-to-back, pop-from-front, size, and is-empty), details the elegant single-queue rotation pattern ($N - 1$ steps), and achieves $O(1)$ pop and top with $O(N)$ push.

---

## 1. Instance & Teaching Goal

We trace the operational lifecycle of `MyStack`:
```text
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top();   // return 2
myStack.pop();   // return 2
myStack.empty(); // return False
```

### The Inversion Challenge: FIFO vs LIFO
- A **Queue** operates on FIFO (First-In, First-Out): elements leave in the exact order they entered.
- A **Stack** operates on LIFO (Last-In, First-Out): the most recently inserted element must leave first.
To make a queue behave like a stack, either `push` or `pop` must reverse the element ordering.
Making `push` reorder the queue so that the **newest element always sits at the front** guarantees that:
- `pop()` is simply a standard queue dequeue (`popleft()`) in $O(1)$ time.
- `top()` is simply a queue front inspection in $O(1)$ time.

---

## 2. Conceptual Foundation & Invariants

### Method A: Single-Queue Rotation (Optimal Follow-Up)
Maintain a single FIFO queue $Q$:
- **`push(x)` Protocol:**
  1. Enqueue $x$ to the back of $Q$:
     $$
     Q.\text{append}(x)
     $$
  2. Let $N$ be the size of $Q$ after adding $x$.
  3. Rotate the preceding $N - 1$ elements by popping from the front and appending to the back:
     $$
     \text{for } i = 1 \dots N - 1: \quad Q.\text{append}(Q.\text{popleft}())
     $$
  Now $x$ is at the front of $Q$, and all older elements are queued behind it in strict reverse-arrival order.
- **`pop()`:**
  $$
  \text{return } Q.\text{popleft}()
  $$
- **`top()`:**
  $$
  \text{return } Q[0]
  $$
- **`empty()`:**
  $$
  \text{return } (\text{len}(Q) == 0)
  $$

### Method B: Dual-Queue Swapping (`q1`, `q2`)
1. Enqueue $x$ into empty helper queue `q2`.
2. Move all elements from `q1` to `q2` one by one.
3. Swap reference identities: $\text{q1}, \text{q2} = \text{q2}, \text{q1}$.

> **Invariant.** At the start and end of every public operation, the queue's front element is strictly identical to the top element of the logical LIFO stack.

---

## 3. Step-by-Step Worked Execution

We trace the single-queue rotation across the operation sequence:

### Operation 1: `MyStack()`
- Initialize $Q = []$.

---

### Operation 2: `push(1)`
1. Enqueue $1$: $Q = [1]$.
2. Elements to rotate: $N - 1 = 1 - 1 = 0$.
3. Queue state: $Q = [1]$ (Front is $1$).

---

### Operation 3: `push(2)`
1. Enqueue $2$ to back:
   $$
   Q = [1, 2] \quad (\text{Size } N = 2)
   $$
2. Rotate $N - 1 = 1$ element:
   - Pop front element $1$: $Q.\text{popleft}() \to 1$.
   - Append $1$ to back: $Q.\text{append}(1)$.
3. Queue state after rotation:
   $$
   Q = [2, 1] \quad (\text{Front is } \mathbf{2})
   $$
   The newest element $2$ is now at the queue front!

---

### Operation 4: `top()`
- Peek at front of $Q$:
  $$
  Q[0] = \mathbf{2}
  $$
- Return $2$. Queue unchanged: $Q = [2, 1]$.

---

### Operation 5: `pop()`
- Remove and return front of $Q$:
  $$
  \text{result} = Q.\text{popleft}() = \mathbf{2}
  $$
- Remaining queue state: $Q = [1]$.

---

### Operation 6: `empty()`
- Check size of $Q$:
  $$
  \text{len}(Q) = 1 \ne 0 \implies \mathbf{false}
  $$

---

### Method B on the Same Operation Sequence

Method B reaches the identical observable behaviour by building the inverted order in the helper queue and then exchanging the two queue identities.

| Operation | `q1` before the step | `q2` after enqueuing the argument | Elements moved from `q1` to `q2` | After the identity swap | Returned |
|:---|:---|:---|:---|:---|:---:|
| `push(1)` | `[]` | `[1]` | none, because `q1` was empty | `q1 = [1]`, `q2 = []` | - |
| `push(2)` | `[1]` | `[2]` | one element, the `1`, appended behind the `2`, giving `q2 = [2, 1]` | `q1 = [2, 1]`, `q2 = []` | - |
| `top()` | `[2, 1]` | `[]` | none: reading never moves elements | `q1 = [2, 1]`, `q2 = []` | `2` |
| `pop()` | `[2, 1]` | `[]` | none: the newest element is already at the front | `q1 = [1]`, `q2 = []` | `2` |
| `empty()` | `[1]` | `[]` | none | `q1 = [1]`, `q2 = []` | `false` |
| `pop()` then `empty()` | `[1]` | `[]` | none | `q1 = []`, `q2 = []` | `1`, then `true` |

Both methods do exactly the same amount of work: one dequeue-and-enqueue pair per older element, performed during the push that inserts the new element. The difference is that Method B must move every older element into a second container and then exchange which container is "the stack", so a swap that copies instead of exchanging leaves `q2` non-empty and breaks the next push's requirement that the helper start empty.

---

## 4. Complete Execution Trace

```text
1. push(1):
   Q: [] -> append 1 -> [1] -> rotate 0 -> Q: [1]

2. push(2):
   Q: [1] -> append 2 -> [1, 2]
   Rotate 1 element: pop 1, append 1 -> Q: [2, 1] (Front = 2)

3. top():
   Peek front of [2, 1] -> 2

4. pop():
   Dequeue front of [2, 1] -> 2
   Q becomes [1]

5. empty():
   len(Q) == 1 -> false
```

| Step | Operation Invoked | Argument | Queue State (Front $\to$ Back) | Rotation Steps | Returned Value |
|:---:|:---|:---:|:---:|:---:|:---:|
| 1 | `MyStack` | - | `[]` | - | `null` |
| 2 | `push` | 1 | `[1]` | 0 | `null` |
| **3** | **`push`** | **2** | **`[2, 1]`** | **1 ($1 \to \text{back}$)** | **`null`** |
| **4** | **`top`** | - | `[2, 1]` | 0 | **`2`** |
| **5** | **`pop`** | - | `[1]` | 0 | **`2`** |
| **6** | **`empty`** | - | `[1]` | 0 | **`false`** |

---

## 5. Algorithmic Correctness

**Soundness.** In a queue containing elements in LIFO order $[e_k, e_{k-1}, \dots, e_1]$, appending a new element $x$ yields $[e_k, e_{k-1}, \dots, e_1, x]$. Dequeuing and re-enqueuing all $k$ older elements moves $x$ to the front while preserving the exact relative order of the older elements: $[x, e_k, e_{k-1}, \dots, e_1]$. Thus, the front element is always the most recently pushed element.

**Completeness.** `pop` removes the front element, leaving the second most recently pushed element at the new front. All LIFO axioms are strictly satisfied.

**Boundary states of this lifecycle.** The drained stack is the state the sequence ends in, and the remaining rows are the shapes that most often break a queue-only implementation.

| Situation | Queue state (front $\to$ back) | `top()` and `pop()` behaviour | `empty()` | What the row establishes |
|:---|:---|:---|:---:|:---|
| Freshly constructed stack | `[]` | Undefined by the contract: the operations are only issued on a non-empty stack, so a queue-only implementation needs no guard for them | `true` | The invariant "front equals top" holds vacuously before any push |
| After the two pushes of this trace | `[2, 1]` | `top()` returns `2` and leaves the queue untouched; `pop()` returns `2` and shrinks it to `[1]` | `false` | The newest element is at the front, which is the whole point of the rotation |
| Fully drained (the sequence's declared end) | `[]` | Both operations are again undefined; the two pops returned `2` then `1` in strict LIFO order | `true` | Draining in LIFO order empties the queue exactly, leaving no residue |
| Push, push, pop, then push again | `[1]` then `[3, 1]` | After `push(3)` the queue is `[1, 3]` before rotation and `[3, 1]` after it, so `top()` returns `3` | `false` | A pop in the middle of the sequence does not disturb the rotation: the surviving element is the one that must sit behind the new front |
| The same value pushed twice | `[5, 5]` | `top()` and both `pop()` calls return `5`, and the second pop empties the queue | `false`, then `true` | The queue's printed contents cannot distinguish one copy of a value from two; only the size can, so value identity is not element identity |

The last row is the trap that value-based reasoning hides: `[5, 5]` after the second push looks exactly like the state after the first push, yet it holds two stack elements rather than one, and only the recorded size reveals this.

---

## 6. Traps This Instance Exposes

- **Using Non-Queue Primitives:** In Python, calling `pop()` on a `deque` removes from the *back*, which acts as an ordinary stack and defeats the purpose of the exercise! The queue constraint requires that removals happen strictly from the *front* (`popleft()`).
- **Expensive Pop Alternative:** An alternative implementation performs $O(1)$ push and $O(N)$ pop by transferring elements on every pop. The $O(N)$ push with $O(1)$ pop approach is generally superior when reads (`top`/`pop`) predominate.
- **Rotation Count Off-by-One:** The loop must rotate exactly $N - 1$ elements, not $N$. Rotating $N$ times cycles the queue back to its original order with $x$ at the tail.

**The four queue-only designs, and where each one pays.** No design makes every operation constant; each one chooses exactly one operation to make linear in the stack size.

| Design | `push(x)` | `pop()` | `top()` | Auxiliary space | Where the cost lands, and the failure mode |
|:---|:---:|:---:|:---:|:---:|:---|
| Single queue, rotate on push (this lesson) | $O(N)$ | $O(1)$ | $O(1)$ | $O(N)$ for the elements, $O(1)$ beyond that | The rotation count must be exactly $N - 1$ measured after the new element is appended; rotating $N$ times restores the arrival order with $x$ at the back |
| Two queues, swap identities on push (Method B) | $O(N)$ | $O(1)$ | $O(1)$ | $O(N)$ spread across both queues | The same number of moves, but the helper queue must be empty before the new element is enqueued; a swap that copies rather than exchanges leaves it occupied and corrupts the next ordering |
| Two queues, transfer on pop | $O(1)$ | $O(N)$ | $O(1)$ only when the newest value is cached in a field, otherwise $O(N)$ | $O(N)$ | Ideal when pushes dominate reads, but a FIFO queue cannot inspect its own back element, so constant-time `top()` demands remembering the most recent push separately |
| Single queue, rotate on pop | $O(1)$ | $O(N)$ | $O(N)$ | $O(N)$ | The mirror image of this lesson: the queue keeps arrival order and is rotated $N - 1$ times on each removal, which forces `top()` to rotate as well, because the newest element waits at the back |

The pattern is unavoidable rather than incidental: turning FIFO storage into LIFO retrieval costs one full pass over the elements for whichever operation must invert the order, so at least one of `push` or `pop` is linear in the stack size.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `push(x)`: $O(N)$, where $N$ is the number of elements in the stack. Exactly $N - 1$ pop-and-push queue rotations are executed.
  - `pop()`: $O(1)$ constant time (single queue dequeue).
  - `top()`: $O(1)$ constant time (front queue inspection).
  - `empty()`: $O(1)$ constant time.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory to store elements in the queue. Only $O(1)$ extra space beyond the queue itself.
