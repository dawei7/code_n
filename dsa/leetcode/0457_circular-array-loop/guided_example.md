# Guided Example: Circular Array Loop

We trace the step-by-step modular index stepping ($(i + nums[i]) \pmod n$), Floyd's Tortoise and Hare cycle detection (slow pointer 1 step, fast pointer 2 steps), directional uniformity checking ($nums[a] \times nums[b] > 0$), self-loop elimination ($next(slow) \ne slow$), and in-place zero-marking on representative circular arrays:

- **Input:** $nums = [2, -1, 1, 2, 2]$
- **Required output:** `true`
  - Array length: $n = 5$
  - Modular transition function:
    $$
    next(i) = (i + nums[i] \pmod 5 + 5) \pmod 5
    $$
  - Transition mappings:
    - Index 0 ($nums[0] = 2$): $next(0) = (0 + 2) \pmod 5 = \mathbf{2}$ (Forward, $+2$)
    - Index 1 ($nums[1] = -1$): $next(1) = (1 - 1) \pmod 5 = \mathbf{0}$ (Backward, $-1$)
    - Index 2 ($nums[2] = 1$): $next(2) = (2 + 1) \pmod 5 = \mathbf{3}$ (Forward, $+1$)
    - Index 3 ($nums[3] = 2$): $next(3) = (3 + 2) \pmod 5 = \mathbf{0}$ (Forward, $+2$)
    - Index 4 ($nums[4] = 2$): $next(4) = (4 + 2) \pmod 5 = \mathbf{1}$ (Forward, $+2$)
  - **Trace starting from index 0:**
    - Direction: Forward ($nums[0] = 2 > 0$)
    - Path from 0:
      $$
      0 \xrightarrow{+2} 2 \xrightarrow{+1} 3 \xrightarrow{+2} 0
      $$
    - Cycle detected: $0 \to 2 \to 3 \to 0$
    - Check validity criteria:
      1. Uniform direction: $nums[0] = 2 > 0, \; nums[2] = 1 > 0, \; nums[3] = 2 > 0$ (**All positive!**)
      2. Cycle length $> 1$: cycle contains 3 distinct indices $\{0, 2, 3\}$ (**Not a self-loop!**)
    - A valid circular loop exists $\implies$ Return **`true`**
- **Self-Loop Rejection Instance:** $nums = [-1, -2, -3, -4, -5, 6]$
  - Index 5 ($nums[5] = 6$): $next(5) = (5 + 6) \pmod 6 = 5$. Length 1 cycle (self-loop) $\implies$ **Invalid $\implies$ `false`**
- **Direction Reversal Instance:** $nums = [1, -1] \implies 0 \to 1 \to 0$, but $nums[0] > 0$ and $nums[1] < 0$ $\implies$ Mixed directions $\implies \mathbf{false}$

This instance demonstrates Floyd's cycle-finding pointer technique on modular directed graphs, mathematically proves why direction invariance and cycle length bounds eliminate degenerate loops, and derives $O(N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a circular array of non-zero integers $nums = [2, -1, 1, 2, 2]$:
Determine if there is a **loop** in $nums$.
A loop must satisfy all three conditions:
1. **Connectivity:** It follows the sequence of movements where $nums[i]$ moves forward if positive and backward if negative:
   $$
   next(i) = (i + nums[i]) \pmod n
   $$
2. **Directional Invariance:** Every movement in the loop must follow the **same direction** (all positive steps or all negative steps).
3. **Non-Trivial Length:** The loop must contain **more than one element** (a cycle of length $k = 1$, where a node jumps back onto itself, is disqualified).

```text
Circular Array Transitions (n = 5):
  Index 0 (+2) ----> Index 2
  Index 2 (+1) ----> Index 3
  Index 3 (+2) ----> Index 0

The cycle 0 -> 2 -> 3 -> 0:
  - All values are positive (+2, +1, +2): Direction is strictly forward.
  - Cycle length is 3 > 1: Not a self-loop.

Valid Circular Loop Detected -> true
```

### The Three Structural Traps
1. **Direction Reversal:** A path that switches between forward and backward steps ($1 \to -1$) is not a valid loop.
2. **Self-Loops ($1$-Cycles):** An element where $(i + nums[i]) \pmod n == i$ jumps to itself. Such nodes must not be counted as loops.
3. **Quadratic Repeated Exploration ($O(N^2)$):** If every starting node traverses the same dead-end path, runtime degrades to $O(N^2)$. Once a path is proven cycle-free, marking its nodes with $0$ ensures every node is examined at most twice.

---

## 2. Conceptual Foundation & Invariants

### 1. The Modular Transition Operator:
For any index $i$ in an array of length $n$:
$$
next(i) = ((i + nums[i]) \pmod n + n) \pmod n
$$
The $+ n \pmod n$ arithmetic ensures positive indices even when $nums[i]$ is negative.

### 2. Floyd's Tortoise and Hare Cycle Detection:
For each potential starting index $i$ with $nums[i] \ne 0$:
- Initialize $slow = i$ (moves 1 step at a time).
- Initialize $fast = next(i)$ (moves 2 steps at a time).
- **Directional Guard:** At every step, check that $fast$ and its successor move in the same sign direction as $slow$:
  $$
  nums[slow] \times nums[fast] > 0 \quad \land \quad nums[slow] \times nums[next(fast)] > 0
  $$
  If signs differ, the path changes direction: abort search.
- **Meeting Condition:** If $slow == fast$:
  - If $slow \ne next(slow)$: The loop has length $\ge 2$ and uniform direction. Return `True`!
  - If $slow == next(slow)$: The cycle is a 1-node self-loop. Abort search.

### 3. In-Place Zero-Marking (Pruning):
When a path from $i$ fails to produce a valid loop, all reachable nodes in that same directional component can never participate in any other valid loop.
Trace from $i$ and set $nums[j] \leftarrow 0$, eliminating redundant future visits.

> **Cycle Invariant.** Floyd's algorithm guarantees that in any finite functional graph with uniform edge directions, the fast pointer will catch the slow pointer within at most $C$ steps, where $C \le n$ is the cycle length.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [2, -1, 1, 2, 2]$ ($n = 5$):

---

### Step 1: Evaluate Starting Node $i = 0$
- $nums[0] = 2 > 0$. Direction: positive (forward).
- Initialize pointers:
  $$
  slow = 0, \quad fast = next(0) = 2
  $$

---

### Step 2: Floyd's Iteration 1
- Check directions:
  - $nums[slow] = nums[0] = 2 > 0$
  - $nums[fast] = nums[2] = 1 > 0 \implies 2 \times 1 > 0$ (Pass)
  - $next(fast) = next(2) = 3$
  - $nums[3] = 2 > 0 \implies 2 \times 2 > 0$ (Pass)
- Test pointer meeting:
  $$
  slow = 0 \ne fast = 2
  $$
- Advance pointers:
  - $slow \leftarrow next(0) = \mathbf{2}$
  - $fast \leftarrow next(next(2)) = next(3) = \mathbf{0}$
- State after Iteration 1: $slow = 2, \; fast = 0$.

---

### Step 3: Floyd's Iteration 2
- Check directions:
  - $nums[slow] = nums[2] = 1 > 0$
  - $nums[fast] = nums[0] = 2 > 0 \implies 1 \times 2 > 0$ (Pass)
  - $next(fast) = next(0) = 2$
  - $nums[2] = 1 > 0 \implies 1 \times 1 > 0$ (Pass)
- Test pointer meeting:
  $$
  slow = 2 \ne fast = 0
  $$
- Advance pointers:
  - $slow \leftarrow next(2) = \mathbf{3}$
  - $fast \leftarrow next(next(0)) = next(2) = \mathbf{3}$
- State after Iteration 2: $slow = 3, \; fast = 3$.

---

### Step 4: Pointers Collide ($slow == fast == 3$)
- Meeting point reached at index $3$!
- Check cycle length:
  $$
  next(slow) = next(3) = 0 \ne 3
  $$
- Since $next(slow) \ne slow$, the cycle has length $> 1$.
- Direction remained strictly positive throughout.
- All three criteria are satisfied.
- Return **`true`**.

---

## 4. Complete Execution Trace

| Round | Slow Pointer | $nums[slow]$ | Fast Pointer | $nums[fast]$ | Fast Next | Collision? $slow == fast$ | Direction Valid? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Init** | $0$ | $+2$ | $2$ | $+1$ | $3$ ($+2$) | No ($0 \ne 2$) | Yes (All $> 0$) |
| **1** | $2$ | $+1$ | $0$ | $+2$ | $2$ ($+1$) | No ($2 \ne 0$) | Yes (All $> 0$) |
| **2** | $3$ | $+2$ | $3$ | $+2$ | $0$ ($+2$) | **Yes ($3 == 3$)** | **Yes (All $> 0$)** |
| **Test**| $slow = 3$ | — | — | — | $next(3) = 0$ | $next(3) \ne 3$ | **Valid Loop: True** |

---

## 5. Boundary Cases & Failure Modes

- **Single-Node Array ($nums = [1]$):** $next(0) = (0 + 1) \pmod 1 = 0$. $next(slow) == slow \implies$ Self-loop $\implies \mathbf{false}$.
- **Mixed Direction Alternation ($nums = [1, -1]$):** $nums[0] > 0$ while $nums[1] < 0$. Condition $nums[slow] \times nums[fast] > 0$ fails $\implies \mathbf{false}$.
- **All Self-Loops ($nums = [-1, -2, -3, -4, -5, 6]$ with $n=6$):** Index 5 moves $5 + 6 \equiv 5 \pmod 6$ (self-loop). Detected by $slow == next(slow) \implies$ rejected.
- **Multiple Disconnected Components:** Outer loop iterates over all $i \in [0, n-1]$. If component 1 has no cycle, it zeroes its nodes and tests component 2.

---

## 6. Traps & Common Anti-Patterns

- **Negative Modulo Handling in C++ / Java:** In Python, `-1 % 5 == 4`. In C++ and Java, `-1 % 5 == -1`. To ensure non-negative indices in all languages, always write `((i + nums[i]) % n + n) % n`.
- **Forgetting Direction Reversal Check on $next(fast)$:** Only checking $nums[slow] \times nums[fast] > 0$ misses a reversal that occurs on the intermediate jump between $fast$ and $next(fast)$. Testing both jumps guarantees direction consistency.
- **Not Marking Visited Nodes ($O(N^2)$):** If cycle detection fails and nodes are not marked, repeatedly traversing the same paths results in quadratic runtime. Overwriting visited non-loop nodes with `0` guarantees each node is visited at most twice.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - With in-place zero marking, each index is traversed by at most one successful or failing Floyd search.
  - Every node is visited $O(1)$ times.
  - Total Time: $\mathcal{O}(N)$. For $N = 5000$, finishes in under 5 ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$. Requires only scalar pointers (`slow`, `fast`, `j`), modifying the array in-place without auxiliary sets or recursion stacks.
