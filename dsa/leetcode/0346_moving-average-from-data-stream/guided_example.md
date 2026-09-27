# Guided Example: Moving Average from Data Stream

We trace the step-by-step circular ring buffer modular indexing (`cnt % size`), constant-time rolling sum delta maintenance ($s \mathrel{+}= val - data[i]$), dynamic effective window divisor scaling ($\min(cnt, size)$), and moving average computation on representative data stream sequences:

- **Input:** `size = 3`, stream calls: `next(1), next(10), next(3), next(5)`
- **Required output:** `[1.0, 5.5, 4.666666666666667, 6.0]`
  - Call 1 (`next(1)`):
    - Buffer: `[1, 0, 0]`, window elements: `[1]`
    - Sum: $1$, divisor: $\min(1, 3) = 1 \implies \text{avg} = 1.0$
  - Call 2 (`next(10)`):
    - Buffer: `[1, 10, 0]`, window elements: `[1, 10]`
    - Sum: $11$, divisor: $\min(2, 3) = 2 \implies \text{avg} = 5.5$
  - Call 3 (`next(3)`):
    - Buffer: `[1, 10, 3]`, window elements: `[1, 10, 3]`
    - Sum: $14$, divisor: $\min(3, 3) = 3 \implies \text{avg} = 14 / 3 \approx 4.6667$
  - Call 4 (`next(5)`):
    - Evicts oldest element ($1$ at index $0$) and stores $5$
    - Buffer: `[5, 10, 3]`, window elements: `[10, 3, 5]`
    - Sum: $14 + 5 - 1 = 18$, divisor: $3 \implies \text{avg} = 18 / 3 = 6.0$
- **Single Element Window:** `size = 1 \implies` every call returns the input value itself
- **Negative Integer Stream:** Rolling sum algebraically subtracts negative evicted values without sign distortion

This instance demonstrates circular buffer queue implementations for streaming data, mathematically proves how delta sum updates maintain $O(1)$ constant time per query without summing arrays, and analyzes $O(W)$ auxiliary memory bounds.

---

## 1. Instance & Teaching Goal

Given a stream of integers and a fixed sliding window size $W = 3$:
Compute the moving average of the last $\min(cnt, W)$ values after each incoming element:

```text
Window Size: W = 3
Call 1: next(1)  -> Window: [1]       -> Sum = 1,  Avg = 1 / 1 = 1.0
Call 2: next(10) -> Window: [1, 10]   -> Sum = 11, Avg = 11 / 2 = 5.5
Call 3: next(3)  -> Window: [1, 10, 3]-> Sum = 14, Avg = 14 / 3 = 4.6667
Call 4: next(5)  -> Window: [10, 3, 5]-> Sum = 18, Avg = 18 / 3 = 6.0 (evicted 1!)
```

### Eliminating the $O(W)$ Summation Overhead
- A naive queue that recalculates $\sum_{x \in Q} x$ on every call takes $O(W)$ time per element.
- By maintaining a running sum $s$ and using a circular array of size $W$, the incoming element adds to $s$ while the expiring element at index $cnt \pmod W$ is subtracted in $O(1)$ operations!

---

## 2. Conceptual Foundation & Invariants

### 1. State Variables:
- `data`: Fixed array of length $W$, initialized to `[0] * size`.
- `s`: Running sum of elements currently in the active window.
- `cnt`: Total number of elements processed since stream start.

### 2. Transition Protocol on `next(val)`:
1. **Target Slot Index:**
   $$
   i = cnt \pmod W
   $$
2. **Delta Sum Update:**
   Subtract the value currently in slot $i$ (either $0$ initially or the oldest element) and add the incoming $val$:
   $$
   s \leftarrow s + val - data[i]
   $$
3. **Overwrite Slot:**
   $$
   data[i] \leftarrow val
   $$
4. **Advance Counter:**
   $$
   cnt \leftarrow cnt + 1
   $$
5. **Effective Window Size:**
   Before the buffer fills, the window contains $cnt$ elements; once full, it contains $W$ elements:
   $$
   \text{effective\_size} = \min(cnt, \; W)
   $$
6. **Return Average:**
   $$
   \text{return } \frac{s}{\text{effective\_size}}
   $$

> **Invariant.** At any call $cnt$, slot $cnt \pmod W$ stores the element that arrived exactly $W$ calls earlier, enabling constant-time eviction.

---

## 3. Step-by-Step Worked Execution

We trace `size = 3` with stream elements `[1, 10, 3, 5]`:
Initialized: `data = [0, 0, 0], s = 0, cnt = 0`.

---

### Step 1: `next(1)` ($cnt = 0$)
- Slot index: $i = 0 \pmod 3 = 0$.
- Old value in slot: $data[0] = 0$.
- Delta update:
  $$
  s \leftarrow 0 + 1 - 0 = \mathbf{1}
  $$
- Overwrite: $data[0] = 1$.
- Counter: $cnt \leftarrow 0 + 1 = 1$.
- Divisor: $\min(1, 3) = 1$.
- Average:
  $$
  1 / 1 = \mathbf{1.0}
  $$

---

### Step 2: `next(10)` ($cnt = 1$)
- Slot index: $i = 1 \pmod 3 = 1$.
- Old value in slot: $data[1] = 0$.
- Delta update:
  $$
  s \leftarrow 1 + 10 - 0 = \mathbf{11}
  $$
- Overwrite: $data[1] = 10$.
- Counter: $cnt \leftarrow 1 + 1 = 2$.
- Divisor: $\min(2, 3) = 2$.
- Average:
  $$
  11 / 2 = \mathbf{5.5}
  $$

---

### Step 3: `next(3)` ($cnt = 2$)
- Slot index: $i = 2 \pmod 3 = 2$.
- Old value in slot: $data[2] = 0$.
- Delta update:
  $$
  s \leftarrow 11 + 3 - 0 = \mathbf{14}
  $$
- Overwrite: $data[2] = 3$.
- Counter: $cnt \leftarrow 2 + 1 = 3$.
- Divisor: $\min(3, 3) = 3$.
- Average:
  $$
  14 / 3 = \mathbf{4.666666666666667}
  $$

---

### Step 4: `next(5)` ($cnt = 3$ — Eviction Triggered!)
- Slot index: $i = 3 \pmod 3 = 0$ (Wraps back to index 0!).
- Old value to evict: $data[0] = \mathbf{1}$.
- Delta update:
  $$
  s \leftarrow 14 + 5 - 1 = \mathbf{18}
  $$
- Overwrite: $data[0] = 5$. Buffer is now `[5, 10, 3]`.
- Counter: $cnt \leftarrow 3 + 1 = 4$.
- Divisor: $\min(4, 3) = 3$.
- Average:
  $$
  18 / 3 = \mathbf{6.0}
  $$

---

## 4. Complete Execution Trace

```text
MovingAverage(size = 3)
data = [0, 0, 0], s = 0, cnt = 0

next(1):  i=0, s =  0 + 1 - 0 =  1, data[0]=1,  cnt=1 -> 1 / 1 = 1.0
next(10): i=1, s =  1 +10 - 0 = 11, data[1]=10, cnt=2 -> 11 / 2 = 5.5
next(3):  i=2, s = 11 + 3 - 0 = 14, data[2]=3,  cnt=3 -> 14 / 3 = 4.6667
next(5):  i=0, s = 14 + 5 - 1 = 18, data[0]=5,  cnt=4 -> 18 / 3 = 6.0

Output Stream: [1.0, 5.5, 4.666666666666667, 6.0]
```

| Call | Incoming $val$ | Circular Index $i$ | Evicted $data[i]$ | Updated Sum $s$ | New Buffer State | Count $cnt$ | Window Divisor | Average Returned |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Init | - | - | - | 0 | `[0, 0, 0]` | 0 | - | - |
| 1 | 1 | 0 | 0 | $0 + 1 - 0 = 1$ | `[1, 0, 0]` | 1 | 1 | **1.0** |
| 2 | 10 | 1 | 0 | $1 + 10 - 0 = 11$ | `[1, 10, 0]` | 2 | 2 | **5.5** |
| 3 | 3 | 2 | 0 | $11 + 3 - 0 = 14$ | `[1, 10, 3]` | 3 | 3 | **$4.6667$** |
| **4** | **5** | **0** | **1** | **$14 + 5 - 1 = 18$** | **`[5, 10, 3]`** | **4** | **3** | **$\mathbf{6.0}$** |

---

## 5. Algorithmic Correctness

**Soundness.** Let $x_0, x_1, \dots, x_{m-1}$ be the sequence of stream elements. For $m \le W$, the sum includes all elements $x_0 \dots x_{m-1}$, and dividing by $m$ gives the exact arithmetic mean. For $m > W$, the element inserted at step $m - W$ is stored at $(m - W) \pmod W = m \pmod W$. Subtracting $data[i]$ removes exactly the element that fell outside the window $W$, ensuring $s$ strictly equals $\sum_{k=m-W}^{m-1} x_k$.

**Completeness.** Circular indexing ensures every slot is reused sequentially. The modulo operation prevents memory growth, allowing infinite streaming without buffer reallocation or index overflow.

---

## 6. Traps This Instance Exposes

- **Floating-Point vs Integer Division:** Dividing two integers in Python (`/`) naturally produces a float. In languages like Java or C++, integer division (`/`) truncates decimals unless one operand is explicitly cast to `double`.
- **Pre-Full Window Divisor:** Before $W$ elements arrive, dividing by $W$ yields an incorrectly deflated average. Sizing by $\min(cnt, W)$ ensures correct early averages.
- **Queue Memory Leak:** Using a standard growing list without deletion retains all historical stream values, causing memory usage to scale with $O(M)$ where $M$ is total stream length. A fixed-size circular array bounds memory to $O(W)$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `__init__(size)`: $O(W)$ to allocate a fixed-size list of zeros.
  - `next(val)`: $O(1)$ constant time involving a few scalar arithmetic and modulo operations.
- **Auxiliary Space Complexity:** $O(W)$ strictly bounded memory to store $W$ elements in the circular buffer `data`.
