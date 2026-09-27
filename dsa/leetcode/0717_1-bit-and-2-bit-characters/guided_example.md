# Guided Example: 1-bit and 2-bit Characters

We trace the step-by-step prefix code tokenization, deterministic branch step stride ($i \leftarrow i + bits[i] + 1$), 1-bit character single advance ($bits[i] = 0 \implies +1$), 2-bit character double advance ($bits[i] = 1 \implies +2$), terminal index alignment ($i == n - 1$), and trailing character type verification on representative binary arrays:

- **Input:** $bits = [1, 0, 0]$
- **Required output:** `true`
  - Encoding rules:
    - There are only two types of valid characters:
      1. **1-bit character:** represented by bit `0`.
      2. **2-bit character:** represented by `10` or `11` (any character starting with bit `1`).
    - The array is guaranteed to end with bit `0`.
    - Objective: Determine whether the final `0` at index $n - 1$ must be decoded as an independent 1-bit character, or if it was consumed as the second half of a preceding 2-bit character (`10`).
    - For $[1, 0, 0]$:
      - First character: starts with `1`, consumes two bits `[1, 0]`.
      - Final character: leaves single bit `[0]`, which is a 1-bit character.
      - Return **`true`**.
- **Prefix Code Determinism & Stride Invariant:**
  - **The Prefix-Free Decoding Guarantee:**
    - Notice that no 1-bit character starts with `1`, and every 2-bit character starts with `1`.
    - Therefore, inspecting the leading bit $bits[i]$ unambiguously dictates the character length:
      - If $bits[i] == 0$: The character is of length 1.
      - If $bits[i] == 1$: The character is of length 2.
    - Stride formula for index advancement:
      $$
      \text{stride}(i) = bits[i] + 1 = \begin{cases} 1 & \text{if } bits[i] = 0 \\ 2 & \text{if } bits[i] = 1 \end{cases}
      $$
  - **Terminal Position Invariant:**
    - Traverse the array starting at $i = 0$ while $i < n - 1$:
      $$
      i \leftarrow i + bits[i] + 1
      $$
    - Because the loop terminates as soon as $i \ge n - 1$:
      1. If the loop stops at **$i == n - 1$**:
         - The traversal pointer landed precisely on the final bit.
         - The final bit stands alone as an independent 1-bit character $\implies$ **`true`**.
      2. If the loop jumps to **$i == n$**:
         - A 2-bit character started at index $n - 2$ and consumed the final bit as its second half.
         - The final character is part of a 2-bit token $\implies$ **`false`**.
- **Step-by-Step Worked Execution Trace on $bits = [1, 0, 0]$ ($n = 3$):**
  - Array indices: $0, 1, 2$. Final target index: $n - 1 = 2$.
  - Initialize pointer: $i = 0$.
  - **Step 1 ($i = 0, bits[0] = 1$):**
    - Inspect leading bit: $bits[0] = 1$.
    - Interpretation: Must be a 2-bit character (`10` or `11`).
    - Compute step stride:
      $$
      \text{stride} = bits[0] + 1 = 1 + 1 = \mathbf{2}
      $$
    - Advance pointer:
      $$
      i \leftarrow 0 + 2 = \mathbf{2}
      $$
    - Tokens parsed so far: `[1, 0]`.
  - **Step 2: Loop Termination Check:**
    - Test loop condition:
      $$
      i < n - 1 \iff 2 < 2 \quad \mathbf{(False)}
      $$
    - Loop terminates!
  - **Step 3: Evaluate Final Landing Position:**
    - Inspect pointer position:
      $$
      i = 2 == n - 1 \quad \mathbf{(Landed\ Exactly\ on\ Final\ Bit!)}
      $$
    - The final bit $bits[2] = 0$ is decoded as an independent 1-bit character.
    - Return **`true`**.
- **Two-Bit Final Consumption Trace ($bits = [1, 1, 1, 0]$, $n = 4$):**
  - Final target index: $n - 1 = 3$.
  - **Step 1 ($i = 0, bits[0] = 1$):**
    - $bits[0] = 1 \implies$ 2-bit character `[1, 1]`.
    - $i \leftarrow 0 + 2 = \mathbf{2}$.
  - **Step 2 ($i = 2, bits[2] = 1$):**
    - $bits[2] = 1 \implies$ 2-bit character `[1, 0]`.
    - $i \leftarrow 2 + 2 = \mathbf{4}$.
  - **Step 3: Termination:**
    - $i = 4 \ge n - 1$ ($3$).
    - Inspect position:
      $$
      i = 4 \ne n - 1 \implies \mathbf{Final\ Zero\ Swallowed\ by\ 2-Bit\ Token!}
      $$
    - Return **`false`**.
- **Single Element Array ($bits = [0]$, $n = 1$):**
  - $n - 1 = 0$.
  - Loop condition $0 < 0$ is false immediately.
  - $i = 0 == n - 1 \implies$ Returns **`true`**.

This instance demonstrates instantaneous prefix code parsing and deterministic finite automaton traversal, mathematically proves why leading-bit prefix-freeness forces a unique left-to-right factorization, and derives $O(N)$ execution time and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a binary array $bits$ ending with 0:
Characters are either `0` (1-bit) or `10` / `11` (2-bit).
Determine if the **last character must be a 1-bit character**.

```text
bits = [ 1, 0, 0 ]

Scan from left:
  Index 0 has bit 1 -> MUST be a 2-bit character -> consumes [1, 0] -> advance by 2
  Pointer lands at Index 2!

Index 2 is the LAST index (n - 1).
It stands alone as a 1-bit character.
Result: true
```

### The Invariant of the Unambiguous Stride
- Because no 1-bit character starts with 1, any token starting with 1 **must** be 2 bits long.
- Stride is always $bits[i] + 1$ (1 if 0, 2 if 1).
- If the pointer lands on $n - 1$, the last character is 1-bit (`true`). If it jumps to $n$, the last 0 was swallowed (`false`).

---

## 2. Conceptual Foundation & Invariants

### 1. Pointer Update Recurrence:
While $i < n - 1$:
$$
i \leftarrow i + bits[i] + 1
$$

### 2. Termination Classifier:
$$
ans = (i == n - 1)
$$

> **Prefix-Free Unique Factorization Invariant.** The code alphabet $\mathcal{C} = \{0, 10, 11\}$ satisfies the Kraft-McMillan prefix condition, ensuring that any word $w \in \mathcal{C}^*$ admits a unique left-to-right deterministic token factorization.

---

## 3. Step-by-Step Worked Execution

We trace $bits = [1, 0, 0]$:

---

### Step 1: Index 0
- $bits[0] = 1 \implies$ stride $= 1 + 1 = 2$.
- $i \leftarrow 0 + 2 = 2$.

---

### Step 2: Loop Check
- $i = 2 \not< 3 - 1 \implies$ Loop halts.

---

### Step 3: Classification
- $i = 2 == 3 - 1 \implies$ **`true`**.

---

## 4. Complete Execution Trace

| Step | Pointer Index $i$ | Current Bit $bits[i]$ | Decoded Token Type | Advance Stride | New Pointer Position | Loop Continues? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $0$ | $1$ | 2-bit token (`10`) | $+2$ | $2$ | No ($2 < 2$ is False) |
| **End** | **$2$** | **$0$** | **1-bit token (`0`)** | — | — | **Result: `true`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Element ($[0]$):** Loop doesn't execute $\implies i = 0 == n - 1 \implies$ `true`.
- **Alternating Twos ($[1, 0, 1, 0]$):** Consumes $[1, 0]$, then $[1, 0] \implies i = 4 \ne 3 \implies$ `false`.
- **All Zeros ($[0, 0, 0]$):** Steps by $+1$ each time $\implies$ lands at $2 \implies$ `true`.
- **Maximum Length ($N = 1000$):** Single pass with scalar addition executes in $< 0.05$ ms.

---

## 6. Traps & Common Anti-Patterns

- **Right-to-Left Ambiguity:** Parsing from right to left is ambiguous because a preceding 1 could either be a 1-bit (impossible) or part of a 2-bit token. Parsing from left to right is strictly deterministic.
- **Counting Trailing Ones Trick without Validation:** While counting consecutive ones before the final 0 works ($parity(count)$), stepping forward from index 0 is universally simpler, less error-prone, and runs in the exact same $O(N)$ time.
- **Array Out of Bounds:** Using `while i < n - 1:` guarantees $bits[i]$ is never evaluated at or beyond the last index.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Traverses the array in a single pass of at most $N$ steps.
  - In each step, performs constant bitwise addition: $\mathcal{O}(1)$.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 0.1$ ms for $N = 1000$.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (only scalar pointers $i$ and $n$).
