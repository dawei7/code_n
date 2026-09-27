# Guided Example: Min Stack

We trace the step-by-step parallel stack synchronization tracking prefix minimums in constant $O(1)$ time across push, pop, and query operations:

- **Input Operations:** `["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]`
- **Arguments:** `[[], [-2], [0], [-3], [], [], [], []]`
- **Required output:** `[null, null, null, null, -3, null, 0, -2]`

This instance demonstrates auxiliary prefix minimum synchronization (recording $\min(\text{val}, \text{min\_stack}[-1])$ on every push), proving why stack pop naturally unwinds minimum history without scanning, comparing twin stacks against single-stack pair encoding, and achieving strictly $O(1)$ time across all operations.

---

## 1. Instance & Teaching Goal

Design a stack that supports `push`, `pop`, `top`, and `getMin` in strictly constant $O(1)$ time:
1. `push(-2)`
2. `push(0)`
3. `push(-3)`
4. `getMin()` $\implies$ returns $-3$
5. `pop()` $\implies$ removes $-3$
6. `top()` $\implies$ returns $0$
7. `getMin()` $\implies$ returns $-2$ (the previous minimum is restored instantly)

In a standard stack, finding the minimum requires an $O(N)$ linear scan.
Using a heap allows $O(1)$ min lookups, but deletion (`pop`) takes $O(N)$ or $O(\log N)$ time because an arbitrary value must be excised.
Because a stack operates strictly in LIFO order, state history is strictly nested: while elements remain below depth $d$, the minimum of that sub-stack never changes.
By maintaining an auxiliary stack `min_stack` where `min_stack[d]` holds the minimum of all values from depth $0$ through $d$, `getMin()` is a simple $O(1)$ stack peek (`min_stack[-1]`), and `pop()` automatically restores the prior minimum in $O(1)$ time.

---

## 2. Conceptual Foundation & Invariants

### Twin-Stack Synchronization Architecture
Maintain two dynamic arrays:
- `val_stack`: stores the actual values in arrival order.
- `min_stack`: stores the running prefix minimum at each depth.

#### Operational Contracts ($O(1)$ Time)
1. **`push(val)`:**
   - Append to value stack:
     $$
     \text{val\_stack.append}(\text{val})
     $$
   - Compute and append new prefix minimum:
     $$
     \text{new\_min} = \min(\text{val}, \, \text{min\_stack}[-1]) \quad (\text{or } \text{val} \text{ if } \text{min\_stack is empty})
     $$
     $$
     \text{min\_stack.append}(\text{new\_min})
     $$
2. **`pop()`:**
   - Pop simultaneously from both stacks:
     $$
     \text{val\_stack.pop()}, \quad \text{min\_stack.pop()}
     $$
     *(Popping `min_stack` exposes the exact minimum of the remaining elements)*.
3. **`top()`:**
   - Return top of value stack: $\text{val\_stack}[-1]$.
4. **`getMin()`:**
   - Return top of minimum stack: $\text{min\_stack}[-1]$.

> **Invariant.** For any depth $d \in [0, |\text{val\_stack}| - 1]$, $\text{min\_stack}[d] = \min_{0 \le i \le d} \text{val\_stack}[i]$.

---

## 3. Step-by-Step Worked Execution

We trace the operations on `MinStack()`:

### Step 1: `MinStack()`
- `val_stack = []`
- `min_stack = []`
- Output: `null`

---

### Step 2: `push(-2)`
- `val = -2`.
- `val_stack.append(-2)`.
- `min_stack` is empty $\implies$ new minimum is $-2$.
- `min_stack.append(-2)`.
- State: `val_stack = [-2]`, `min_stack = [-2]`.
- Output: `null`

---

### Step 3: `push(0)`
- `val = 0`.
- `val_stack.append(0)`.
- Prior min: $\text{min\_stack}[-1] = -2$.
- New min: $\min(0, -2) = -2$.
- `min_stack.append(-2)`.
- State: `val_stack = [-2, 0]`, `min_stack = [-2, -2]`.
- Output: `null`

---

### Step 4: `push(-3)`
- `val = -3`.
- `val_stack.append(-3)`.
- Prior min: $-2$.
- New min: $\min(-3, -2) = -3$.
- `min_stack.append(-3)`.
- State: `val_stack = [-2, 0, -3]`, `min_stack = [-2, -2, -3]`.
- Output: `null`

---

### Step 5: `getMin()`
- Inspect top of `min_stack`: $\text{min\_stack}[-1] = \mathbf{-3}$.
- Output: $\mathbf{-3}$

---

### Step 6: `pop()`
- Pop top element from both stacks:
  - `val_stack.pop()` $\implies$ removes $-3$.
  - `min_stack.pop()` $\implies$ removes $-3$.
- State:
  - `val_stack = [-2, 0]`
  - `min_stack = [-2, -2]`
- Output: `null`

---

### Step 7: `top()`
- Inspect top of `val_stack`: $\text{val\_stack}[-1] = \mathbf{0}$.
- Output: $\mathbf{0}$

---

### Step 8: `getMin()`
- Inspect top of `min_stack`: $\text{min\_stack}[-1] = \mathbf{-2}$.
- Prior minimum $-2$ is restored in $O(1)$ time!
- Output: $\mathbf{-2}$

---

## 4. Complete Execution Trace

```text
Operation    val_stack              min_stack             Return Value
push(-2):    [-2]                   [-2]                  null
push(0):     [-2, 0]                [-2, -2]              null
push(-3):    [-2, 0, -3]            [-2, -2, -3]          null
getMin():    [-2, 0, -3]            [-2, -2, -3]          -3
pop():       [-2, 0]                [-2, -2]              null
top():       [-2, 0]                [-2, -2]              0
getMin():    [-2, 0]                [-2, -2]              -2
```

| Step | Operation | Input Value | `val_stack` State | `min_stack` State | Current Minimum | Emitted Result |
|:---:|:---:|:---:|:---|:---|:---:|:---:|
| 1 | `MinStack` | - | `[]` | `[]` | - | `null` |
| 2 | `push` | -2 | `[-2]` | `[-2]` | -2 | `null` |
| 3 | `push` | 0 | `[-2, 0]` | `[-2, -2]` | -2 | `null` |
| 4 | `push` | -3 | `[-2, 0, -3]` | `[-2, -2, -3]` | -3 | `null` |
| **5** | **`getMin`** | - | `[-2, 0, -3]` | `[-2, -2, -3]` | **-3** | **-3** |
| 6 | `pop` | - | `[-2, 0]` | `[-2, -2]` | -2 | `null` |
| **7** | **`top`** | - | `[-2, 0]` | `[-2, -2]` | -2 | **0** |
| **8** | **`getMin`** | - | `[-2, 0]` | `[-2, -2]` | **-2** | **-2** |

---

## 5. Algorithmic Correctness

**Soundness.** For any sequence of elements $[v_0, v_1, \dots, v_k]$, the minimum is defined recursively as $\min(v_k, \min_{0 \le i < k} v_i)$. Because `min_stack` stores this exact recursive recurrence at every depth, the top of `min_stack` is mathematically guaranteed to equal the minimum of the active elements.

**Completeness.** Popping a value also pops its corresponding prefix minimum entry. Since earlier entries in `min_stack` were computed when those earlier elements were added, popping exposes the historical minimum without recalculation.

---

## 6. Traps This Instance Exposes

- **Failing to Store Duplicate Minima:** In optimization attempts that only push onto `min_stack` when `val < current_min`, duplicate minima (e.g. pushing $-2$ twice) will only record one $-2$. Popping the first $-2$ would erroneously delete the minimum marker, corrupting future `getMin()` calls! Either duplicate the minimum entry or use `val <= current_min`.
- **Calling Operations on Empty Stack:** The problem specification guarantees that `pop`, `top`, and `getMin` are called only on non-empty stacks, avoiding underflow handling.
- **Space Optimization with Pairs:** Storing tuples `(val, min_val)` in a single stack accomplishes identical functionality with a single array allocation.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$ time for every operation (`push`, `pop`, `top`, `getMin`). Each operation performs scalar comparisons and $O(1)$ array append/pop operations.
- **Auxiliary Space Complexity:** $O(N)$, where $N$ is the number of elements currently in the stack, storing one value and one minimum entry per level.
