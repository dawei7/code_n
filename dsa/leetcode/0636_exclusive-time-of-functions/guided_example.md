# Guided Example: Exclusive Time of Functions

We trace the step-by-step single-threaded execution stack tracking (`stk`), inclusive time-slice boundary accounting (`start` at beginning of timestamp vs `end` at close of timestamp), preemptive interruption credit allocation ($cur - pre$), function pop and closure accumulation ($cur - pre + 1$), and exclusive CPU execution time profiling on representative nested call graphs:

- **Input:**
  - Function count: $n = 2$ (IDs $0$ and $1$)
  - Execution log stream:
    $$
    logs = [\text{"0:start:0"}, \; \text{"1:start:2"}, \; \text{"1:end:5"}, \; \text{"0:end:6"}]
    $$
- **Required output:** `[3, 4]`
  - Timing conventions:
    - `"start:t"`: The function begins execution at the **very beginning** of second $t$ ($t.0$).
    - `"end:t"`: The function finishes execution at the **very end** of second $t$ (inclusive of the entire duration $[t, t+1)$).
    - Exclusive time definition: The total CPU time spent actively executing inside that function, **excluding any time spent inside other nested functions it called**.
- **Call-Stack State Accounting Architecture:**
  - Single-threaded CPU invariant: At any given moment, the function actively executing is the **top of the call stack** (`stk[-1]`).
  - Maintain:
    - Call stack `stk`: IDs of active functions in the current call chain.
    - Integer `pre`: The starting point of the current unassigned interval of time.
    - Array `ans` of size $n$: Total accumulated exclusive seconds per function.
  - **State Transitions on Log Events:**
    - **Event: `i:start:cur`**
      - If `stk` is non-empty, the function currently at `stk[-1]` was running from time `pre` up to the beginning of `cur`.
      - Credit the interrupted parent:
        $$
        ans[stk[-1]] \leftarrow ans[stk[-1]] + (cur - pre)
        $$
      - Push new function $i$ onto stack: `stk.append(i)`.
      - Set next segment start: $pre \leftarrow cur$.
    - **Event: `i:end:cur`**
      - The function finishing is at the top of the stack (`stk.pop()`).
      - It ran from time `pre` through the end of timestamp `cur` (a total duration of $(cur - pre + 1)$ units).
      - Credit the terminating function:
        $$
        ans[i] \leftarrow ans[i] + (cur - pre + 1)
        $$
      - Advance next segment start past the end of second `cur`:
        $$
        pre \leftarrow cur + 1
        $$
- **Step-by-Step Worked Execution Trace:**
  - Initial state:
    $$
    stk = [], \quad ans = [0, 0], \quad pre = 0
    $$
  - **Log 0: `"0:start:0"` ($i = 0, op = \text{start}, cur = 0$):**
    - Stack is empty (no previously running function to credit).
    - Push Function 0:
      $$
      stk = [0]
      $$
    - Update start pointer:
      $$
      pre = cur = \mathbf{0}
      $$
  - **Log 1: `"1:start:2"` ($i = 1, op = \text{start}, cur = 2$):**
    - Stack top is Function 0.
    - Function 0 was executing uninterrupted from $pre = 0$ to $cur = 2$.
    - Credit Function 0:
      $$
      duration = cur - pre = 2 - 0 = \mathbf{2}
      $$
      $$
      ans[0] \leftarrow 0 + 2 = \mathbf{2}
      $$
    - Push Function 1 onto stack:
      $$
      stk = [0, \; 1]
      $$
    - Update start pointer:
      $$
      pre = cur = \mathbf{2}
      $$
  - **Log 2: `"1:end:5"` ($i = 1, op = \text{end}, cur = 5$):**
    - Pop Function 1 from stack:
      $$
      stk = [0]
      $$
    - Function 1 executed from $pre = 2$ through the end of second $5$:
      $$
      duration = cur - pre + 1 = 5 - 2 + 1 = \mathbf{4} \quad (\text{seconds 2, 3, 4, 5})
      $$
      $$
      ans[1] \leftarrow 0 + 4 = \mathbf{4}
      $$
    - Update start pointer for the resumed parent:
      $$
      pre = cur + 1 = 5 + 1 = \mathbf{6}
      $$
  - **Log 3: `"0:end:6"` ($i = 0, op = \text{end}, cur = 6$):**
    - Pop Function 0 from stack:
      $$
      stk = []
      $$
    - Function 0 resumed at $pre = 6$ and executed through the end of second $6$:
      $$
      duration = cur - pre + 1 = 6 - 6 + 1 = \mathbf{1} \quad (\text{second 6})
      $$
      $$
      ans[0] \leftarrow 2 + 1 = \mathbf{3}
      $$
    - Update start pointer:
      $$
      pre = 6 + 1 = \mathbf{7}
      $$
  - **Final Output Verification:**
    - Function 0 exclusive time: $2 + 1 = \mathbf{3}$ seconds (seconds $0, 1$, and $6$).
    - Function 1 exclusive time: $\mathbf{4}$ seconds (seconds $2, 3, 4, 5$).
    - Total CPU time: $3 + 4 = 7$ seconds (spans seconds $0 \dots 6$).
    - Result:
      $$
      ans = \mathbf{[3, 4]}
      $$
- **Recursive Self-Call Instance ($n = 1, logs = [\text{"0:start:0"}, \text{"0:start:2"}, \text{"0:end:5"}, \text{"0:end:6"}]$):**
  - Outer 0 runs $0 \to 2$ ($+2$).
  - Inner 0 runs $2 \to 5$ ($+4$).
  - Outer 0 resumes $6 \to 6$ ($+1$).
  - Total for Function 0: $2 + 4 + 1 = \mathbf{7}$ seconds $\implies [7]$.

This instance demonstrates execution call stack instrumentation and temporal interval partitioning, mathematically proves why tracking the transition anchor $pre$ correctly amortizes sub-call durations without recursive subtraction trees, and derives $O(L)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given $n$ functions and a sequential event log:
Calculate the **exclusive CPU time** spent in each function.
A function does not earn credit for time spent inside sub-routines it called.

```text
Logs:
  0:start:0 -> Function 0 starts at t=0
  1:start:2 -> Function 1 starts at t=2 (Preempts 0; 0 ran for 2-0 = 2 units)
  1:end:5   -> Function 1 ends at t=5   (1 ran for 5-2+1 = 4 units: seconds 2,3,4,5)
  0:end:6   -> Function 0 ends at t=6   (0 resumes at t=6, runs 6-6+1 = 1 unit: second 6)

Totals:
  Function 0: 2 + 1 = 3 units
  Function 1: 4 units
```

### The Invariant of the Running Head
- We do not need to know the total duration of a function when it starts.
- At every log event (whether start or end), the **interval since the last event** $[pre, cur]$ is uniquely attributable to the function currently sitting at the top of the stack.

---

## 2. Conceptual Foundation & Invariants

### 1. Inclusive Endpoint Arithmetic:
- A `start` event occurs at time $T$. Time elapsed since $pre$ is $T - pre$.
- An `end` event concludes at the **close** of time $T$. Time elapsed since $pre$ is $T - pre + 1$.
- Next segment start after an `end` event begins at $T + 1$.

### 2. State Invariant:
At all times:
$$
\sum_{i=0}^{n-1} ans[i] + \text{active\_span} = \text{current\_time}
$$

> **LIFO Preemption Invariant.** The call stack represents the active path of the runtime tree, ensuring that all elapsed CPU intervals are credited to the lowest common ancestor in the call chain.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Initialize
- $stk = [], ans = [0, 0], pre = 0$.

---

### Step 2: `"0:start:0"`
- $stk = [0], pre = 0$.

---

### Step 3: `"1:start:2"`
- Stack top is 0. Credit 0 with $2 - 0 = 2$.
- $ans[0] = 2$.
- Push 1: $stk = [0, 1], pre = 2$.

---

### Step 4: `"1:end:5"`
- Pop 1. Credit 1 with $5 - 2 + 1 = 4$.
- $ans[1] = 4$.
- $stk = [0], pre = 5 + 1 = 6$.

---

### Step 5: `"0:end:6"`
- Pop 0. Credit 0 with $6 - 6 + 1 = 1$.
- $ans[0] = 2 + 1 = 3$.
- Return **`[3, 4]`**.

---

## 4. Complete Execution Trace

| Log Line | Action | Interrupted Function | Interval Credited | Running $ans[0]$ | Running $ans[1]$ | Stack After | Next $pre$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:start:0` | Start 0 | None (Empty) | — | $0$ | $0$ | `[0]` | $0$ |
| `1:start:2` | Start 1 | Function 0 | $2 - 0 = 2$ | **$2$** | $0$ | `[0, 1]` | $2$ |
| `1:end:5` | End 1 | Function 1 | $5 - 2 + 1 = 4$ | $2$ | **$4$** | `[0]` | $6$ |
| `0:end:6` | End 0 | Function 0 | $6 - 6 + 1 = 1$ | **`3`** | $4$ | `[]` | $7$ |
| **Output** | — | — | — | **`3`** | **`4`** | — | — |

---

## 5. Boundary Cases & Failure Modes

- **Recursive Calls (Same ID nested):** Handled identically; separate stack frames track each level.
- **Immediate Start and End (`0:start:3`, `0:end:3`):** Duration $3 - 3 + 1 = 1$ unit.
- **Multiple Sequential (Non-Nested) Calls:** Stack empties and refills; $pre$ advances smoothly.
- **Deep Nesting:** Stack depth grows up to $N$.

---

## 6. Traps & Common Anti-Patterns

- **Forgetting the $+1$ on `end` Events:** `end:5` means through second 5.999..., so it occupies the entire slot 5. Using $cur - pre$ instead of $cur - pre + 1$ undercounts by 1 on every function return.
- **Forgetting to Advance $pre$ to $cur + 1$ After `end`:** If you set $pre = cur$ after `end:5`, the next function will double-count second 5.
- **Reconstructing the Call Tree Explicitly:** Storing children nodes and subtracting child sums is complex and error-prone; the online linear stack scan is optimal.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $L$ be the number of log entries in $logs$.
  - Each log entry is processed with a split and single stack push/pop in $\mathcal{O}(1)$ time.
  - Total Time: strictly linear $\mathcal{O}(L)$. Completes in $< 3$ ms for $L = 10^4$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for the call stack and the answer array.
