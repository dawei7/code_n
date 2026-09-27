# Guided Example: Third Maximum Number

We trace the step-by-step distinct top-three tracking, ripple-shift cascading, duplicate suppression, and fallback extraction on representative numerical arrays:

- **Input:** $nums = [2, 2, 3, 1]$
- **Required output:** `1`
  - Initialize top three distinct registers:
    $$
    m_1 = -\infty, \quad m_2 = -\infty, \quad m_3 = -\infty
    $$
  - Step 1 (Process $x = 2$):
    - $2 > m_1 (-\infty) \implies$ Cascade: $m_3 \leftarrow -\infty, m_2 \leftarrow -\infty, m_1 \leftarrow 2$
    - Registers: $(m_1, m_2, m_3) = (2, -\infty, -\infty)$
  - Step 2 (Process $x = 2$):
    - $2 \in \{m_1, m_2, m_3\} \implies 2 == m_1 \implies$ **Duplicate suppressed!**
    - Registers unchanged: $(2, -\infty, -\infty)$
  - Step 3 (Process $x = 3$):
    - $3 > m_1 (2) \implies$ Cascade: $m_3 \leftarrow -\infty, m_2 \leftarrow 2, m_1 \leftarrow 3$
    - Registers: $(m_1, m_2, m_3) = (3, 2, -\infty)$
  - Step 4 (Process $x = 1$):
    - $1 \notin \{3, 2, -\infty\}$
    - $1 < m_1 (3)$ and $1 < m_2 (2)$, but $1 > m_3 (-\infty)$
    - Set $m_3 \leftarrow 1$
    - Registers: $(m_1, m_2, m_3) = (3, 2, 1)$
  - Result extraction:
    - $m_3 \ne -\infty \implies$ Return $m_3 = \mathbf{1}$
- **Fallback Instance ($< 3$ distinct values):** $nums = [1, 2] \implies (m_1, m_2, m_3) = (2, 1, -\infty) \implies m_3 == -\infty \implies$ Return $m_1 = \mathbf{2}$
- **All Duplicates Instance:** $nums = [5, 5, 5] \implies (m_1, m_2, m_3) = (5, -\infty, -\infty) \implies$ Return $m_1 = \mathbf{5}$

This instance demonstrates constant-memory top-$k$ tracking, mathematically proves why duplicate suppression must precede magnitude comparisons, and establishes $O(N)$ runtime and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums = [2, 2, 3, 1]$:
Find the **third distinct maximum** number in the array. If the third distinct maximum does not exist, return the **maximum** number:

```text
Input: [2,  2,  3,  1]

Distinct Values Present:
  Set: {1, 2, 3}
  Sorted Descending: [3, 2, 1]
                      |  |  |
                     1st 2nd 3rd

Third Distinct Maximum: 1
```

### The Distinctness and Fallback Contract
1. **Strict Distinctness:** Duplicates of an existing maximum do not occupy subsequent ranks. In $[2, 2, 3, 1]$, the two $2$'s belong to the same rank ($2$nd maximum).
2. **Fallback Rule:** If fewer than 3 distinct values exist across the entire array (such as $[1, 2]$ or $[1, 1, 1]$), the answer falls back to the **global maximum** ($m_1$).
3. **Linear Time Requirement:** Finding the top 3 distinct values must take $O(N)$ time and $O(1)$ auxiliary memory, without sorting the whole array in $O(N \log N)$ or allocating a hash set of size $O(N)$.

---

## 2. Conceptual Foundation & Invariants

### 1. Three Ordered Registers:
Maintain three variables representing the 1st, 2nd, and 3rd distinct maxima seen so far:
$$
m_1 > m_2 > m_3
$$
Initialize all three to $-\infty$ (or sentinel objects `None`).

### 2. The Insertion & Shift Logic:
For each incoming number $x$:
1. **Duplicate Guard:**
   If $x == m_1$ or $x == m_2$ or $x == m_3$:
   Ignore $x$. It provides no new information about distinct values.
2. **First Place Insertion ($x > m_1$):**
   $x$ surpasses the current maximum. Shift all ranks down:
   $$
   m_3 \leftarrow m_2, \quad m_2 \leftarrow m_1, \quad m_1 \leftarrow x
   $$
3. **Second Place Insertion ($x > m_2$):**
   $x$ sits between the 1st and 2nd maxima. Shift rank 2 down:
   $$
   m_3 \leftarrow m_2, \quad m_2 \leftarrow x
   $$
4. **Third Place Insertion ($x > m_3$):**
   $x$ sits between the 2nd and 3rd maxima. Replace rank 3:
   $$
   m_3 \leftarrow x
   $$
5. **Below Ranks ($x < m_3$):**
   $x$ is smaller than all three current distinct maxima. Discard $x$.

> **Invariant.** After processing any prefix of the array, $(m_1, m_2, m_3)$ contains the top three distinct values of that prefix in strictly descending order, padded with $-\infty$ if fewer than three distinct values exist.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [2, 2, 3, 1]$:
Initial state: $m_1 = -\infty, \; m_2 = -\infty, \; m_3 = -\infty$.

---

### Step 1: Element $x = 2$
- Duplicate check: $2 \notin \{-\infty\}$.
- Magnitude comparison:
  - $2 > m_1 (-\infty)$ (**Triggers First Place Cascade**)
- Shift registers:
  $$
  m_3 \leftarrow m_2 = -\infty
  $$
  $$
  m_2 \leftarrow m_1 = -\infty
  $$
  $$
  m_1 \leftarrow x = \mathbf{2}
  $$
- State: $(m_1, m_2, m_3) = (2, -\infty, -\infty)$.

---

### Step 2: Element $x = 2$
- Duplicate check:
  $$
  x == m_1 \quad (2 == 2)
  $$
- **Duplicate detected.**
- Skip all comparisons and register shifts.
- State: $(m_1, m_2, m_3) = (2, -\infty, -\infty)$.

---

### Step 3: Element $x = 3$
- Duplicate check: $3 \notin \{2, -\infty\}$.
- Magnitude comparison:
  - $3 > m_1 (2)$ (**Triggers First Place Cascade**)
- Shift registers:
  $$
  m_3 \leftarrow m_2 = -\infty
  $$
  $$
  m_2 \leftarrow m_1 = 2
  $$
  $$
  m_1 \leftarrow x = \mathbf{3}
  $$
- State: $(m_1, m_2, m_3) = (3, 2, -\infty)$.

---

### Step 4: Element $x = 1$
- Duplicate check: $1 \notin \{3, 2, -\infty\}$.
- Magnitude comparison:
  - $1 > m_1 (3)$? False.
  - $1 > m_2 (2)$? False.
  - $1 > m_3 (-\infty)$? **True!** (**Triggers Third Place Insertion**)
- Update register:
  $$
  m_3 \leftarrow x = \mathbf{1}
  $$
- State: $(m_1, m_2, m_3) = (3, 2, 1)$.

---

### Step 5: Terminal Evaluation
- Check $m_3$:
  $$
  m_3 = 1 \ne -\infty
  $$
- Exactly three distinct maxima exist. Return $m_3 = \mathbf{1}$.

---

## 4. Complete Execution Trace

| Step | Element $x$ | Duplicate Test ($x \in \{m_1, m_2, m_3\}$) | Condition Triggered | Register $m_1$ | Register $m_2$ | Register $m_3$ | Current Top 3 Ranking |
|:---:|:---:|:---:|:---|:---:|:---:|:---:|:---|
| **Init** | — | — | — | $-\infty$ | $-\infty$ | $-\infty$ | None |
| **1** | $2$ | False | $x > m_1$ (Shift all) | $2$ | $-\infty$ | $-\infty$ | $[2]$ |
| **2** | $2$ | **True ($x == m_1$)** | Suppress duplicate | $2$ | $-\infty$ | $-\infty$ | $[2]$ |
| **3** | $3$ | False | $x > m_1$ (Shift all) | $3$ | $2$ | $-\infty$ | $[3, 2]$ |
| **4** | $1$ | False | $x > m_3$ (Update $m_3$) | $3$ | $2$ | $1$ | $[3, 2, 1]$ |
| **Done** | — | — | $m_3 \ne -\infty \implies m_3$ | **$3$** | **$2$** | **$1$** | **Output = 1** |

---

## 5. Boundary Cases & Failure Modes

- **Fewer Than Three Elements ($nums = [1, 2]$):** Registers become $(2, 1, -\infty)$. At the end, $m_3 == -\infty$, so the fallback triggers: return $m_1 = \mathbf{2}$.
- **Only One Element ($nums = [10]$):** Registers become $(10, -\infty, -\infty)$. Returns $m_1 = \mathbf{10}$.
- **Negative Numbers ($nums = [-1, -2, -3, -4]$):** Correctly cascades negative integers: $(-1, -2, -3)$, returning $-3$. Using a numerical sentinel like $0$ or $-2^{31}$ would fail if numbers in the array equal the sentinel. Using $-\infty$ (or Python `None`) correctly handles any 32-bit signed integer.
- **Array with Integer Min Value (`-2147483648`):** If an element is $-2^{31}$, numerical sentinels initialized to $-2^{31}$ mistake the real value for an empty slot. Using floating-point $-\infty$ avoids sentinel collisions.

---

## 6. Traps & Common Anti-Patterns

- **Duplicate Check After Shift:** If the duplicate check is not performed first, an incoming duplicate equal to $m_1$ could fail $x > m_1$, proceed to $x > m_2$, and overwrite $m_2$ with a duplicate copy of $m_1$ (e.g. $[3, 3, 2] \to m_1=3, m_2=3$). Filtering $x \in \{m_1, m_2, m_3\}$ at the top of the loop prevents register corruption.
- **Sorting the Whole Array:** Calling `sort()` takes $O(N \log N)$ time. For $N = 10^5$, linear scan is significantly faster and satisfies the strict $O(N)$ problem specification.
- **Using a Full Hash Set:** Storing all $N$ elements in a `set` consumes $O(N)$ auxiliary memory. The register method strictly uses $O(1)$ space.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The array of $N$ elements is iterated through once.
  - In each iteration, at most 3 equality checks and 3 numerical comparisons are evaluated in $O(1)$ time.
  - Total Time: $\mathcal{O}(N)$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$. Memory is strictly bounded to three scalar registers ($m_1, m_2, m_3$).
