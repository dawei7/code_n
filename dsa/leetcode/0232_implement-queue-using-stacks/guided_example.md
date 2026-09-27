# Guided Example: Implement Queue using Stacks

We trace the step-by-step LIFO-to-FIFO dual-stack buffering, lazy transfer mechanics, and amortized $O(1)$ accounting on representative queue operations:

- **Sequential Operations:**
  1. `MyQueue()` (Initialize two stacks: `in_stack = []`, `out_stack = []`)
  2. `push(1)` (`in_stack = [1]`)
  3. `push(2)` (`in_stack = [1, 2]`)
  4. `peek()` $\implies \mathbf{1}$ (Transfers `in_stack` to `out_stack` $\implies \text{out\_stack} = [2, 1]$; peeks top element $1$)
  5. `pop()` $\implies \mathbf{1}$ (Pops top of `out_stack`; remaining $\text{out\_stack} = [2]$)
  6. `empty()` $\implies \mathbf{false}$ (`out_stack` contains $2$)
- **Drain Operation:** `pop()` returns $2 \implies \text{empty}()$ returns `true`

This instance demonstrates implementing First-In-First-Out (FIFO) semantics strictly through Last-In-First-Out (LIFO) stack primitives (push, pop, peek, empty), proves why lazy batch transfers achieve amortized $O(1)$ time per operation, and details why newer elements must wait in `in_stack` until `out_stack` is completely drained.

---

## 1. Instance & Teaching Goal

We trace the operational lifecycle of `MyQueue`:
```text
MyQueue myQueue = new MyQueue();
myQueue.push(1); // Queue is [1]
myQueue.push(2); // Queue is [1, 2] (front is 1)
myQueue.peek();  // returns 1
myQueue.pop();   // returns 1, queue becomes [2]
myQueue.empty(); // returns false
```

### The Inversion Challenge: Stack vs Queue
- A **Stack** provides LIFO (Last-In, First-Out): the most recent element is on top.
- A **Queue** provides FIFO (First-In, First-Out): the oldest element must be served first.
Popping elements from one stack and pushing them onto a second stack reverses their physical order.
If we keep two stacks:
1. `in_stack`: receives new elements via $O(1)$ push.
2. `out_stack`: serves removals from its top, holding elements in reversed order (oldest on top).
By transferring elements from `in_stack` to `out_stack` **only when `out_stack` becomes completely empty**, elements are moved in batches and each element is transferred at most once!

---

## 2. Conceptual Foundation & Invariants

### Dual-Stack Protocol
- **`push(x)`:**
  Always push directly onto `in_stack`:
  $$
  \text{in\_stack}.\text{push}(x)
  $$
  Takes strictly $O(1)$ time.
- **Lazy Transfer Helper (`shift_stacks`):**
  If `out_stack` is empty:
  $$
  \text{while in\_stack is not empty}: \quad \text{out\_stack}.\text{push}(\text{in\_stack}.\text{pop}())
  $$
- **`pop()`:**
  Call `shift_stacks()`.
  $$
  \text{return out\_stack}.\text{pop}()
  $$
- **`peek()`:**
  Call `shift_stacks()`.
  $$
  \text{return out\_stack}.\text{top}()
  $$
- **`empty()`:**
  $$
  \text{return } (\text{len}(\text{in\_stack}) == 0 \text{ and } \text{len}(\text{out\_stack}) == 0)
  $$

### Why Lazy Transfer Preserves FIFO Order
Suppose `out_stack` contains $[2]$ (oldest element waiting) and a new push $3$ occurs.
- $3$ enters `in_stack`.
- If we prematurely dumped $3$ into `out_stack`, $3$ would sit above $2$, and the newer element would be popped before the older element!
- Therefore, elements in `in_stack` must **never** be transferred while `out_stack` still holds older elements.

> **Invariant.** The sequence obtained by reading `out_stack` from top to bottom followed by `in_stack` from bottom to top forms the exact arrival order of all active elements in the queue.

---

## 3. Step-by-Step Worked Execution

We trace the operation sequence:

### Operation 1: `MyQueue()`
- $\text{in\_stack} = [], \quad \text{out\_stack} = []$.

---

### Operation 2: `push(1)`
- Push $1$ onto $\text{in\_stack}$.
- $\text{in\_stack} = [1], \quad \text{out\_stack} = []$.

---

### Operation 3: `push(2)`
- Push $2$ onto $\text{in\_stack}$.
- $\text{in\_stack} = [1, 2], \quad \text{out\_stack} = []$.
- (Top of $\text{in\_stack}$ is $2$; bottom is $1$).

---

### Operation 4: `peek()`
- `out_stack` is currently empty $\implies$ **Trigger `shift_stacks()`!**
  - Pop $2$ from $\text{in\_stack}$, push to $\text{out\_stack}$: $\text{out\_stack} = [2]$.
  - Pop $1$ from $\text{in\_stack}$, push to $\text{out\_stack}$: $\text{out\_stack} = [2, 1]$.
  - $\text{in\_stack}$ is now empty: `[]`.
- Peek top of `out_stack`:
  $$
  \text{out\_stack}[-1] = \mathbf{1}
  $$
- Return $1$. Stacks unchanged: $\text{in\_stack} = [], \text{out\_stack} = [2, 1]$.

---

### Operation 5: `pop()`
- `out_stack` is not empty (contains $[2, 1]$). No transfer needed!
- Pop from top of $\text{out\_stack}$:
  $$
  \text{result} = \text{out\_stack}.\text{pop}() = \mathbf{1}
  $$
- Stacks state: $\text{in\_stack} = [], \quad \text{out\_stack} = [2]$.
- Return $1$.

---

### Operation 6: `empty()`
- Check emptiness of both stacks:
  - $\text{len}(\text{in\_stack}) = 0$.
  - $\text{len}(\text{out\_stack}) = 1 \ne 0$.
- Result: $\mathbf{false}$.

---

## 4. Complete Execution Trace

```text
1. push(1): in_stack = [1], out_stack = []
2. push(2): in_stack = [1, 2], out_stack = []
3. peek():
   out_stack empty -> transfer in_stack to out_stack:
   pop 2 -> push 2
   pop 1 -> push 1
   out_stack = [2, 1] (Top is 1)
   peek() returns 1
4. pop():
   out_stack not empty -> pop 1 -> returns 1
   out_stack = [2]
5. empty():
   out_stack has [2] -> returns false
```

| Step | Operation Invoked | Argument | `in_stack` (Bottom $\to$ Top) | `out_stack` (Bottom $\to$ Top) | Transfer Triggered? | Returned Value |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | `MyQueue` | - | `[]` | `[]` | No | `null` |
| 2 | `push` | 1 | `[1]` | `[]` | No | `null` |
| 3 | `push` | 2 | `[1, 2]` | `[]` | No | `null` |
| **4** | **`peek`** | - | **`[]`** | **`[2, 1]`** | **Yes ($1, 2$ reversed)** | **`1`** |
| **5** | **`pop`** | - | **`[]`** | **`[2]`** | **No** | **`1`** |
| **6** | **`empty`** | - | **`[]`** | **`[2]`** | **No** | **`false`** |

### 4.1 What Each Transfer Actually Moves

A transfer is the only operation whose cost is not constant, so its internal
sequence deserves its own record. The transfer triggered by `peek` consists of
two independent moves, and their order is what converts LIFO storage into FIFO
service.

| Move number | `in_stack` before | Value popped from `in_stack` | `out_stack` after | Depth of the moved value in `out_stack` |
|:---:|:---:|:---:|:---:|:---:|
| 1 | `[1, 2]` | 2, the newest arrival | `[2]` | 0, at the bottom |
| 2 | `[1]` | 1, the oldest arrival | `[2, 1]` | 1, at the top and therefore the next to leave |
| - | `[]` | none; the loop condition fails and the transfer ends | `[2, 1]` | unreachable during this transfer |

The first move is the counterintuitive one. It lifts the element that arrived
last and places it at the bottom of `out_stack`, where it is now the *hardest*
element to remove. Only after the second move does the oldest arrival sit on top.
This is the complete mechanism by which two reversals of a reversal produce
arrival order: the transfer reverses once, and the pop from `out_stack` reverses
again.

### 4.2 Interleaved Boundary: Pushing While the Output Stack Is Active

The main sequence finishes before any new `push` arrives, so it never tests the
rule that guards against premature transfers. The authored interleaved trial
pushes 3 while `out_stack` is already serving older elements.

| Step | Operation | Argument | `in_stack` (bottom to top) | `out_stack` (bottom to top) | Transfer attempted at this step? | Result |
|:---:|:---|:---:|:---:|:---:|:---|:---|
| 1 | `push` | 1 | `[1]` | `[]` | No; `push` never transfers | - |
| 2 | `push` | 2 | `[1, 2]` | `[]` | No | - |
| 3 | `pop` | - | `[]` | `[2, 1]` after the transfer | Yes, because `out_stack` was empty | 1 |
| 4 | `push` | 3 | `[3]` | `[2]` | No; `out_stack` is non-empty, so 3 waits | - |
| 5 | `peek` | - | `[3]` | `[2]` | No; the helper declines because `out_stack` still holds 2 | 2 |
| 6 | `pop` | - | `[3]` | `[]` after removing 2 | No | 2 |
| 7 | `pop` | - | `[]` | `[3]` after the deferred transfer | Yes, `out_stack` finally ran dry | 3 |
| 8 | `empty` | - | `[]` | `[]` | No | `true` |

Step 4 is the whole point of the trial. Had the implementation transferred 3
immediately, `out_stack` would have become `[2, 3]`, step 5 would have returned 3,
and the queue would have served a newer element before an older one. Step 7 shows
the cost of waiting: the deferred element is transferred only after the last
older element leaves, which is exactly the batching that makes the amortized
bound hold.

---

## 5. Algorithmic Correctness

**Soundness.** Suppose elements arrive in order $e_1, e_2, \dots, e_m$. They are pushed onto `in_stack` with $e_1$ at the bottom and $e_m$ at the top. When `shift_stacks` pops `in_stack` and pushes onto `out_stack`, $e_m$ lands at the bottom of `out_stack` and $e_1$ lands at the top. Future pops from `out_stack` remove $e_1, e_2, \dots, e_m$ in strictly FIFO order.

**Completeness.** Any new element pushed while `out_stack` is active resides safely in `in_stack`. Because `shift_stacks` transfers them only after `out_stack` is empty, no element can bypass an older element.

---

## 6. Traps This Instance Exposes

- **Transferring on Every Operation:** Moving elements back and forth between `in_stack` and `out_stack` on every single operation degrades time complexity to $O(N)$ per operation ($O(N^2)$ overall).
- **Overwriting `out_stack`:** Transferring elements from `in_stack` while `out_stack` still contains items reverses the relative order between the older and newer elements, destroying FIFO semantics.
- **Premature Emptiness:** Checking only `len(in_stack) == 0` for `empty()` returns `true` even when elements are waiting in `out_stack`. Both stacks must be empty.

### 6.1 Lifetime Accounting for Every Element

The amortized claim is easy to state and easy to misapply, so it is worth
following each element of the traced sequence from arrival to departure. Every
movement below is one stack primitive on one element.

| Element | Pushed onto `in_stack` | Popped from `in_stack` during a transfer | Pushed onto `out_stack` | Popped from `out_stack` by a removal | Total movements | Which operation paid for the transfer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 1 | 1 | 1 | 1 | 4 | The `peek` at step 4 of the main sequence, costing 2 moves |
| 2 | 1 | 1 | 1 | 1 | 4 | The same `peek` that moved element 1, and the earlier `pop` that removed 1 |
| 3 (interleaved trial) | 1 | 1 | 1 | 1 | 4 | The `pop` at step 7 of the trial, which is the first removal after `out_stack` emptied |

The total is four primitive operations per element over its entire lifetime, and
no element is ever moved more than once in each direction. That is the arithmetic
behind the amortized bound: a sequence of $M$ operations moves at most $M$
elements through at most four primitives each, so the aggregate work is linear in
$M$ even though a single `pop` can cost $O(N)$ when it happens to trigger a large
transfer.

### 6.2 Alternatives Compared on This Instance

| Approach | Cost of `push` | Cost of `pop` and `peek` | Auxiliary space | Tradeoff or failure mode |
|:---|:---:|:---:|:---:|:---|
| Two stacks with lazy transfer (traced above) | $O(1)$ worst case | Amortized $O(1)$, worst case $O(N)$ | $O(N)$ across both stacks | Chosen. The expensive step is rare and bounded in aggregate, and no element is ever moved twice in the same direction |
| Two stacks that transfer eagerly on every operation | $O(1)$ | $O(N)$ every time | $O(N)$ | Simple to describe, but repeatedly shuffles elements that are already ordered, degrading a sequence of $M$ operations to $O(M \cdot N)$ |
| One stack plus a recursion or temporary buffer | $O(1)$ | $O(N)$ with extra temporary storage | $O(N)$ | Correct order is recoverable, yet each removal rebuilds the container, so the amortized argument no longer applies |
| A single-ended list used as a queue | $O(1)$ amortized append | $O(N)$ to remove the front | $O(N)$ | Not a stack-based solution at all; removing the front shifts every remaining element, and the interface required here exposes only stack primitives |
| Two stacks with a front pointer cached | $O(1)$ | $O(1)$ for `peek` after the first transfer | $O(N)$ | A legitimate micro-optimization: caching the front element spares repeated `peek` calls the helper check, but it adds state that must be invalidated on every transfer |

The first row is the only one whose worst-case spike is amortized away. The
second row is the classic mistake the problem is designed to catch, and the
fourth row is the reminder that the solution must be expressed through the stack
operations the contract provides rather than through a different container that
happens to be easier.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `push(x)`: strictly $O(1)$ worst-case.
  - `empty()`: strictly $O(1)$ worst-case.
  - `pop()` / `peek()`: amortized $O(1)$ time.
  - *Amortized Proof (Potential Method):* Each element is pushed to `in_stack` once ($O(1)$), popped from `in_stack` once ($O(1)$), pushed to `out_stack` once ($O(1)$), and popped from `out_stack` once ($O(1)$). Total lifetime cost per element is 4 operations. Thus, over any sequence of $M$ operations, total time is $O(M)$, giving amortized $O(1)$ per operation.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary space to store $N$ elements across the two stacks.
