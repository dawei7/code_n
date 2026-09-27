# Guided Example: Reach a Number

We trace the step-by-step 1D random walk step sequence ($+i$ or $-i$), destination sign symmetry ($target \leftarrow |target|$), triangular number sum accumulation ($s = k(k+1)/2$), step-reversal parity invariance ($\Delta = s - target \equiv 0 \pmod 2$), odd-difference step extension, and minimal move count determination on representative integer targets:

- **Input:** $target = 2$
- **Required output:** `3`
  - Number line step mechanics:
    - You start at coordinate $0$ on an infinite integer line.
    - On move $i$ (for $i = 1, 2, 3, \dots$), you take exactly $i$ steps, choosing either the **positive direction** ($+i$) or **negative direction** ($-i$).
    - Objective: Reach exact destination coordinate $target$ in the **minimum total number of moves** $k$.
    - For $target = 2$:
      - Move 1 (size 1): $+1 \to$ pos $1$.
      - Move 2 (size 2): $+2 \to$ pos $3$; or $-2 \to$ pos $-1$. (Cannot land on $2$).
      - Move 3 (size 3):
        - If we choose moves $+1, -2, +3$:
          $$
          \text{Final position} = 1 - 2 + 3 = \mathbf{2}
          $$
        - Exactly matches $target = 2$ in $k = 3$ moves!
- **Triangular Sum & Even Parity Invariant:**
  - **Symmetry of Target Sign:**
    - Reaching $+target$ and reaching $-target$ are mirror images (simply invert every move's direction).
    - Hence, we can take $target \leftarrow |target|$.
  - **Maximum Reachable Distance (All-Positive Path):**
    - If all $k$ steps are taken to the right, the accumulated distance is the $k$-th triangular number:
      $$
      s = \sum_{i=1}^k i = \frac{k(k + 1)}{2}
      $$
    - To have any hope of reaching $target$, we must take enough moves such that:
      $$
      s \ge target
      $$
  - **The Step Reversal Parity Invariant:**
    - Suppose we flip a single move $j \in [1, k]$ from $+j$ to $-j$.
    - The new position becomes:
      $$
      s' = s - 2j
      $$
    - The net reduction is $2j$, which is **always an even number**!
    - More generally, flipping any subset of moves $\{j_1, j_2, \dots\}$ reduces the total sum by:
      $$
      2 \sum j_m \quad \mathbf{(strictly\ even)}
      $$
    - Therefore, the difference between the all-positive sum $s$ and our desired $target$ must be **even**:
      $$
      (s - target) \equiv 0 \pmod 2
      $$
    - If $s \ge target$ and $(s - target)$ is even, we can always choose a subset of moves whose sum is $(s - target)/2$ and negate them, landing exactly on $target$!
    - If $(s - target)$ is odd, we must advance $k$ further until the parity difference becomes even.
- **Step-by-Step Worked Execution Trace on $target = 2$:**
  - Standardize target: $|target| = 2$.
  - Initialize: $k = 0, \; s = 0$.
  - **Move $k = 1$:**
    - Add move: $s \leftarrow 0 + 1 = \mathbf{1}$.
    - Check condition:
      - $s < target$ ($1 < 2$) $\implies$ Target not yet reachable.
      - Advance to next move.
  - **Move $k = 2$:**
    - Add move: $s \leftarrow 1 + 2 = \mathbf{3}$.
    - Check condition:
      - Magnitude bound: $s \ge target$ ($3 \ge 2$) $\implies$ Satisfied!
      - Parity test:
        $$
        s - target = 3 - 2 = \mathbf{1} \quad \mathbf{(Odd!)}
        $$
        - Flipping any move subtracts an even number.
        - $3 - 2j = 2 \implies 2j = 1 \implies$ no integer move $j$ exists!
        - Target cannot be formed with $k = 2$.
      - Advance to next move.
  - **Move $k = 3$:**
    - Add move: $s \leftarrow 3 + 3 = \mathbf{6}$.
    - Check condition:
      - Magnitude bound: $s \ge target$ ($6 \ge 2$) $\implies$ Satisfied!
      - Parity test:
        $$
        s - target = 6 - 2 = \mathbf{4} \quad \mathbf{(Even!)}
        $$
        - Since $4$ is even, we need a subset of $\{1, 2, 3\}$ summing to $4 / 2 = \mathbf{2}$.
        - Flipping move $j = 2$:
          $$
          +1 - 2 + 3 = \mathbf{2}
          $$
        - Lands exactly on $target = 2$!
  - **Termination:**
    - Both conditions satisfied:
      $$
      ans = k = \mathbf{3}
      $$
- **Exact Triangular Number Trace ($target = 3$):**
  - $k = 1: s = 1 < 3$.
  - $k = 2: s = 3 \ge 3$. Difference $3 - 3 = 0$ is even.
  - Returns $k = \mathbf{2}$ ($+1 + 2 = 3$).
- **Two Step Parity Extension ($target = 4$):**
  - $k = 1: s = 1$
  - $k = 2: s = 3$
  - $k = 3: s = 6 \ge 4$; difference $6 - 4 = 2$ is even $\implies$ returns $k = \mathbf{3}$ ($+1 + 2 - 3 \dots$ wait, $2/2 = 1 \implies -1 + 2 + 3 = 4$).

This instance demonstrates arithmetic parity analysis and triangular subset partition reduction, mathematically proves why sign inversion induces an invariant congruence modulo 2 over step sequences, and derives $O(\sqrt{target})$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a $target$:
On step $i$, take $i$ steps left or right.
Find the **minimum moves $k$ to reach $target$**.

```text
target = 2

k = 1: sum = 1 < 2
k = 2: sum = 3 >= 2, but sum - target = 3 - 2 = 1 (ODD! cannot flip)
k = 3: sum = 6 >= 2, and sum - target = 6 - 2 = 4 (EVEN! flip step 4/2 = 2)

Moves: +1 - 2 + 3 = 2
Minimum moves: 3
Result: 3
```

### The Invariant of the Even Parity Gap
- Moving all right yields sum $s = k(k+1)/2$.
- Flipping any step $+j$ to $-j$ reduces the sum by $2j$ (an **even** amount).
- We can reach $target$ if and only if $s \ge |target|$ and $(s - |target|)$ is **even**.

---

## 2. Conceptual Foundation & Invariants

### 1. Triangular Sum Accumulation:
$$
s_k = \sum_{i=1}^k i = \frac{k(k + 1)}{2}
$$

### 2. Reachability Criteria:
$$
k_{\min} = \min \{ k \in \mathbb{N} \mid s_k \ge |target| \ \land \ (s_k - |target|) \equiv 0 \pmod 2 \}
$$

> **Signed Step Invariance Modulo 2.** For any sign configuration $\epsilon \in \{-1, +1\}^k$, the endpoint $X = \sum_{i=1}^k \epsilon_i i$ satisfies $X \equiv \sum_{i=1}^k i \pmod 2$. Hence $X = target$ implies $(s_k - target) \equiv 0 \pmod 2$.

---

## 3. Step-by-Step Worked Execution

We trace $target = 2$:

---

### Step 1: $k = 1$
- $s = 1 < 2$.

---

### Step 2: $k = 2$
- $s = 3 \ge 2$, but $3 - 2 = 1$ (odd).

---

### Step 3: $k = 3$
- $s = 6 \ge 2$, and $6 - 2 = 4$ (even).
- Flip step $4 / 2 = 2 \implies 1 - 2 + 3 = 2$.
- Valid!

---

### Step 4: Output
$$
k = \mathbf{3}
$$

---

## 4. Complete Execution Trace

| Move $k$ | Triangular Sum $s_k$ | Condition $s_k \ge target$? | Parity Gap $(s_k - target)$ | Even Parity? | Valid Configuration Found? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $1$ | No ($1 < 2$) | — | — | No |
| $2$ | $3$ | Yes ($3 \ge 2$) | $3 - 2 = 1$ | No (Odd) | No |
| **$3$** | **$6$** | **Yes ($6 \ge 2$)** | **$6 - 2 = 4$** | **Yes (Even)** | **Yes ($+1 - 2 + 3 = 2$)** |
| **Result** | — | — | — | — | **`3`** |

---

## 5. Boundary Cases & Failure Modes

- **$target = 0$:** Requires 0 moves $\implies$ returns 0.
- **Negative Target ($target = -2$):** Standardized via $|target| = 2 \implies$ returns 3.
- **Exact Triangular Number ($target = 6$):** $s_3 = 6 \implies 6 - 6 = 0$ (even) $\implies$ returns 3.
- **Odd Gap Extension:** If gap is odd, adding $k + 1$ or $(k + 1) + (k + 2)$ changes parity to even in at most 2 additional steps.

---

## 6. Traps & Common Anti-Patterns

- **Simulating All Sign Combinations ($2^k$):** For $target = 10^9$, $k \approx 45,000$. Brute force search $2^k$ is impossible. The algebraic parity check solves it in $\mathcal{O}(\sqrt{target})$.
- **Stopping at $s \ge target$ without Parity Check:** Just reaching or exceeding $target$ is insufficient; if $s - target$ is odd, landing on $target$ is mathematically impossible with that $k$.
- **Negative Sign Handling:** Forgetting `target = abs(target)` will cause an infinite loop if $target < 0$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - $s \approx k^2 / 2 \ge target \implies k \approx \sqrt{2 \cdot target}$.
  - The while loop runs at most $\mathcal{O}(\sqrt{target}) + 2$ iterations.
  - For $target = 10^9$, $k \le 45,000$, completing in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ space using only scalar loop accumulators $k, s$.
