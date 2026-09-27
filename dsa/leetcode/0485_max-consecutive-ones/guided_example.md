# Guided Example: Max Consecutive Ones

We trace the step-by-step single-pass contiguous run counter ($cnt \leftarrow cnt + 1$), zero-triggered reset ($cnt \leftarrow 0$), and running maximum peak tracking ($ans = \max(ans, cnt)$) on representative binary arrays:

- **Input:** $nums = [1, 1, 0, 1, 1, 1]$
- **Required output:** `3`
  - Array length: $N = 6$
  - Objective: Maximum length of contiguous subarray consisting exclusively of $1$s.
- **Single-pass execution trace:**
  - Initial state: $ans = 0, \; cnt = 0$
  - **Index 0 ($x = 1$):**
    - Encountered $1 \implies cnt \leftarrow 0 + 1 = \mathbf{1}$
    - Update peak: $ans \leftarrow \max(0, 1) = \mathbf{1}$
  - **Index 1 ($x = 1$):**
    - Encountered $1 \implies cnt \leftarrow 1 + 1 = \mathbf{2}$
    - Update peak: $ans \leftarrow \max(1, 2) = \mathbf{2}$
  - **Index 2 ($x = 0$):**
    - Encountered $0 \implies$ Contiguous streak broken!
    - Reset current counter: $cnt \leftarrow \mathbf{0}$
    - Peak remains: $ans = 2$
  - **Index 3 ($x = 1$):**
    - Encountered $1 \implies cnt \leftarrow 0 + 1 = \mathbf{1}$
    - Peak remains: $ans = \max(2, 1) = 2$
  - **Index 4 ($x = 1$):**
    - Encountered $1 \implies cnt \leftarrow 1 + 1 = \mathbf{2}$
    - Peak: $ans = \max(2, 2) = 2$
  - **Index 5 ($x = 1$):**
    - Encountered $1 \implies cnt \leftarrow 2 + 1 = \mathbf{3}$
    - Update peak: $ans \leftarrow \max(2, 3) = \mathbf{3}$
  - End of array reached.
  - Final maximum consecutive ones: **`3`**
- **Alternating Ones and Zeroes:** $nums = [1, 0, 1, 1, 0, 1] \implies$ Streaks are of lengths $1, 2, 1 \implies \mathbf{2}$
- **All Zeroes:** $nums = [0, 0, 0] \implies cnt$ never increments $\implies \mathbf{0}$
- **All Ones:** $nums = [1, 1, 1, 1] \implies cnt$ reaches $4 \implies \mathbf{4}$

This instance demonstrates linear state accumulation and reset invariants, mathematically proves why updating the maximum upon each increment avoids missing trailing streaks, and derives $O(N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a binary array $nums = [1, 1, 0, 1, 1, 1]$:
Find the **maximum number of consecutive `1`s** in the array.

```text
Array:        [ 1,  1,  0,  1,  1,  1 ]
Run Lengths:  |-- 2 --|     |--- 3 ---|
                             ^
                         Global Max = 3
```

### The Accumulator and Reset State Machine
The problem models a two-state finite state machine:
1. **Accumulation State ($x == 1$):**
   Extend the current streak of ones:
   $$
   cnt \leftarrow cnt + 1
   $$
   Record the new maximum:
   $$
   ans \leftarrow \max(ans, cnt)
   $$
2. **Reset State ($x == 0$):**
   The streak of ones terminates:
   $$
   cnt \leftarrow 0
   $$

---

## 2. Conceptual Foundation & Invariants

### 1. Invariant of the Current Streak:
At any step $i$:
$$
cnt = \text{length of the contiguous block of 1s ending at index } i
$$
If $nums[i] == 0$, no block of 1s ends at $i$, so $cnt = 0$.

### 2. Invariant of the Global Maximum:
At any step $i$:
$$
ans = \max_{0 \le j \le i} (\text{length of any contiguous block of 1s in } nums[0 \dots j])
$$

> **Immediate Peak Update.** Updating $ans = \max(ans, cnt)$ whenever $cnt$ increments ensures that if the array ends with a sequence of 1s (no terminating zero), the trailing streak is already captured without requiring post-loop checks.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 1, 0, 1, 1, 1]$:

---

### Step 1: Element at Index 0 ($x = 1$)
- $x = 1$:
  $$
  cnt \leftarrow 0 + 1 = 1
  $$
  $$
  ans \leftarrow \max(0, 1) = 1
  $$

---

### Step 2: Element at Index 1 ($x = 1$)
- $x = 1$:
  $$
  cnt \leftarrow 1 + 1 = 2
  $$
  $$
  ans \leftarrow \max(1, 2) = 2
  $$

---

### Step 3: Element at Index 2 ($x = 0$)
- $x = 0$:
  $$
  cnt \leftarrow 0
  $$
- $ans$ unchanged ($2$).

---

### Step 4: Element at Index 3 ($x = 1$)
- $x = 1$:
  $$
  cnt \leftarrow 0 + 1 = 1
  $$
  $$
  ans \leftarrow \max(2, 1) = 2
  $$

---

### Step 5: Element at Index 4 ($x = 1$)
- $x = 1$:
  $$
  cnt \leftarrow 1 + 1 = 2
  $$
  $$
  ans \leftarrow \max(2, 2) = 2
  $$

---

### Step 6: Element at Index 5 ($x = 1$)
- $x = 1$:
  $$
  cnt \leftarrow 2 + 1 = 3
  $$
  $$
  ans \leftarrow \max(2, 3) = \mathbf{3}
  $$

---

### Termination:
Loop completes. Output: **`3`**.

---

## 4. Complete Execution Trace

| Index $i$ | Current Value $nums[i]$ | State Transition | Streak Counter $cnt$ | Global Peak $ans$ | Note |
|:---:|:---:|:---:|:---:|:---:|:---|
| **$0$** | $1$ | Increment | $1$ | $1$ | First 1 |
| **$1$** | $1$ | Increment | $2$ | $2$ | Streak of two |
| **$2$** | $0$ | Reset | $0$ | $2$ | Zero encountered |
| **$3$** | $1$ | Increment | $1$ | $2$ | New streak begins |
| **$4$** | $1$ | Increment | $2$ | $2$ | Streak of two |
| **$5$** | $1$ | Increment | $3$ | **$3$** | New peak recorded |
| **Final** | — | — | — | **$3$** | **Result: $3$** |

---

## 5. Boundary Cases & Failure Modes

- **Single Element Zero ($nums = [0]$):** Loop runs once with reset $\implies \mathbf{0}$.
- **Single Element One ($nums = [1]$):** Loop runs once with increment $\implies \mathbf{1}$.
- **All Ones ($nums = [1, 1, 1]$):** Never resets $\implies cnt = N \implies \mathbf{N}$.
- **All Zeroes ($nums = [0, 0, 0]$):** Resets every step $\implies cnt = 0 \implies \mathbf{0}$.

---

## 6. Traps & Common Anti-Patterns

- **Updating Peak Only on Zero:** Updating $ans = \max(ans, cnt)$ only inside the `else` branch forgets to record the peak if the longest streak reaches the very end of the array ($[1, 1, 1]$ would return $0$). Updating on every increment handles arbitrary endings cleanly.
- **String Splitting (`"".join(map(str, nums)).split('0')`):** Converting a $10^5$-element array to string and splitting creates unnecessary heap allocations and string parsing overhead. A simple integer accumulator is orders of magnitude faster.
- **Off-by-One Reset Values:** Setting $cnt = 1$ on zero incorrectly carries a non-zero count into the next element. The streak of ones after a zero must strictly reset to 0.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The loop performs a single linear pass over $N$ elements.
  - Each element requires $O(1)$ scalar comparisons and increments.
  - Total Time: $\mathcal{O}(N)$. For $N = 10^5$, executes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ extra space using two integer variables ($cnt$ and $ans$).
