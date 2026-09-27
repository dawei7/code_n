# Guided Example: Middle of the Linked List

We trace the step-by-step fast and slow pointer (tortoise and hare) traversal, speed ratio invariant ($2:1$), termination parity on odd and even lengths, second-middle tie-breaking rules, and in-place reference return on representative singly-linked lists:

- **Input:**
  $$
  head = [1, 2, 3, 4, 5]
  $$
- **Required output:** `[3, 4, 5]`
  - Middle node rules:
    - Given the head of a singly linked list, return the middle node.
    - If there are two middle nodes (which occurs whenever the list length $n$ is even), return the **second middle node**.
    - For $head = [1, 2, 3, 4, 5]$:
      - Length $n = 5$ (odd).
      - Indices (0-indexed): $0, 1, 2, 3, 4$.
      - Exact middle index: $\lfloor 5 / 2 \rfloor = 2$, which holds value $3$.
      - Returning node $3$ yields sublist $[3, 4, 5]$.
      - Result: **`[3, 4, 5]`**.
    - For even list $head = [1, 2, 3, 4, 5, 6]$:
      - Length $n = 6$ (even).
      - Middle indices: $2$ (value $3$) and $3$ (value $4$).
      - Second middle node is index $3$ (value $4$).
      - Result: `[4, 5, 6]`.
- **The $2:1$ Velocity Ratio Invariant:**
  - **Tortoise and Hare Dynamics:**
    - Initialize two pointers at the head: $slow \leftarrow head, \; fast \leftarrow head$.
    - In each step:
      $$
      slow \leftarrow slow.next \quad (1\text{ step})
      $$
      $$
      fast \leftarrow fast.next.next \quad (2\text{ steps})
      $$
    - Because $fast$ moves at exactly twice the speed of $slow$, the distance traveled by $fast$ is always twice that of $slow$:
      $$
      \text{dist}(fast) = 2 \times \text{dist}(slow)
      $$
  - **Termination Parity:**
    - **Odd Length ($n = 2m + 1$):**
      - After $m$ steps, $fast$ lands exactly on the last node (index $2m$), where $fast.next == \text{null}$.
      - $slow$ has taken $m$ steps, reaching index $m$, which is the exact unique middle node!
    - **Even Length ($n = 2m$):**
      - After $m$ steps, $fast$ steps past the tail to $\text{null}$ (index $2m$).
      - $slow$ has taken $m$ steps, reaching index $m$, which is the second of the two middle nodes!
    - Therefore, the single loop guard `fast and fast.next` correctly resolves both odd and even lengths in one pass without counting the length.

---

## 1. Instance & Teaching Goal

Given $head = [1, 2, 3, 4, 5]$, trace the advancement of $slow$ and $fast$ until the middle node is isolated.

```text
Step 0:  [1] -> [2] -> [3] -> [4] -> [5] -> null
        slow
        fast

Step 1:  [1] -> [2] -> [3] -> [4] -> [5] -> null
                slow   fast

Step 2:  [1] -> [2] -> [3] -> [4] -> [5] -> null
                        slow         fast (fast.next is null -> STOP!)

Return slow: Node 3 (Sublist [3, 4, 5])
```

The teaching goal is to demonstrate how relative speed guarantees optimal midpoint convergence in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space without counting the list length.

---

## 2. Conceptual Foundation & Invariants

### 1. Pointer Position Equations:
Let $k$ denote the number of iterations completed:
$$
\text{index}(slow_k) = k
$$
$$
\text{index}(fast_k) = 2k
$$

### 2. Termination Predicate:
The loop continues while:
$$
fast \ne \text{null} \quad \land \quad fast.next \ne \text{null}
$$
- On odd length $n$: terminates when $\text{index}(fast) = n - 1$, so $2k = n - 1 \implies k = \frac{n - 1}{2}$.
- On even length $n$: terminates when $fast = \text{null}$, so $2k = n \implies k = \frac{n}{2}$.

---

## 3. Step-by-Step Worked Execution

We trace $head = [1, 2, 3, 4, 5]$:
Initial: $slow = \text{Node } 1$, $fast = \text{Node } 1$.

---

### Step 1: Iteration 1
- Current state:
  - $slow$: Node $1$ (index $0$).
  - $fast$: Node $1$ (index $0$).
- Loop condition check:
  - $fast$ is Node $1 \ne \text{null}$.
  - $fast.next$ is Node $2 \ne \text{null}$. Condition satisfied.
- Advance pointers:
  - $slow \leftarrow slow.next = \text{Node } 2$ (index $1$).
  - $fast \leftarrow fast.next.next = \text{Node } 3$ (index $2$).

---

### Step 2: Iteration 2
- Current state:
  - $slow$: Node $2$ (index $1$).
  - $fast$: Node $3$ (index $2$).
- Loop condition check:
  - $fast$ is Node $3 \ne \text{null}$.
  - $fast.next$ is Node $4 \ne \text{null}$. Condition satisfied.
- Advance pointers:
  - $slow \leftarrow slow.next = \text{Node } 3$ (index $2$).
  - $fast \leftarrow fast.next.next = \text{Node } 5$ (index $4$).

---

### Step 3: Loop Termination Check
- Current state:
  - $slow$: Node $3$ (index $2$).
  - $fast$: Node $5$ (index $4$).
- Loop condition check:
  - $fast$ is Node $5 \ne \text{null}$.
  - $fast.next$ is $\text{null}$!
- Condition $fast.next \ne \text{null}$ fails.
- Loop terminates.

---

### Return Value:
- Pointer $slow$ points to **Node 3**.
- Linked list from Node 3 onwards: `[3, 4, 5]`.
- **Return: `Node 3`**.

---

## 4. Complete Execution Trace & Parity Contrast

### Odd List $[1, 2, 3, 4, 5]$:
| Iteration | $slow$ Node (Value) | $fast$ Node (Value) | $fast.next$ Value | Loop Guard ($fast \land fast.next$) |
|:---:|:---:|:---:|:---:|:---:|
| Start ($0$) | Node $1$ ($1$) | Node $1$ ($1$) | Node $2$ | True |
| $1$ | Node $2$ ($2$) | Node $3$ ($3$) | Node $4$ | True |
| **$2$** | **Node $3$ ($3$)** | **Node $5$ ($5$)** | **`null`** | **`False -> Halt`** |

### Even List $[1, 2, 3, 4, 5, 6]$:
| Iteration | $slow$ Node (Value) | $fast$ Node (Value) | $fast.next$ Value | Loop Guard ($fast \land fast.next$) |
|:---:|:---:|:---:|:---:|:---:|
| Start ($0$) | Node $1$ ($1$) | Node $1$ ($1$) | Node $2$ | True |
| $1$ | Node $2$ ($2$) | Node $3$ ($3$) | Node $4$ | True |
| $2$ | Node $3$ ($3$) | Node $5$ ($5$) | Node $6$ | True |
| **$3$** | **Node $4$ ($4$)** | **`null`** | — | **`False -> Halt`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Node List ($[1]$):** $fast.next$ is null on iteration 0. Loop never runs; returns Node 1 immediately.
- **Two Node List ($[1, 2]$):** After 1 step, $slow$ is at Node 2 and $fast$ is null. Returns Node 2 (second middle node).
- **Three Node List ($[1, 2, 3]$):** After 1 step, $fast$ is at Node 3 with null next. Returns Node 2.

---

## 6. Traps & Common Anti-Patterns

- **Null Pointer Dereference on $fast.next.next$:** If the loop guard only checks `fast`, accessing `fast.next.next` when $fast.next$ is null throws an unhandled exception. The compound check `fast and fast.next` ensures safety.
- **Two-Pass Traversal Overhead:** Counting total nodes in pass 1 and walking $n/2$ nodes in pass 2 requires traversing $1.5 \times N$ nodes; the fast/slow pointer method finishes in a single pass of $N$ node visits.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - $fast$ pointer traverses the list of length $N$ in steps of 2, making $\lfloor N/2 \rfloor$ iterations: $\mathcal{O}(N)$.
  - Total Time: strictly $\mathcal{O}(N)$, completing in $< 1$ ms for $N \le 100$.
- **Auxiliary Space Complexity:**
  - Exactly two pointer variables ($slow, fast$): strictly $\mathcal{O}(1)$ space.
