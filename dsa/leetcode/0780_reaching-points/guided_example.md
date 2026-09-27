# Guided Example: Reaching Points

We trace the step-by-step 2D lattice vector transition operations ($(x, y) \to (x+y, y)$ or $(x, x+y)$), reverse deterministic Euclidean ancestor reduction ($(tx, ty) \to (tx \bmod ty, ty)$), branching tree asymmetry, boundary alignment condition ($tx == sx$ or $ty == sy$), modular congruence residual check ($(ty - sy) \bmod tx == 0$), and reachability decidability on representative coordinate pairs:

- **Input:**
  - Starting point: $(sx, sy) = (1, 1)$
  - Target point: $(tx, ty) = (3, 5)$
- **Required output:** `true`
  - Forward transition mechanics:
    - From any point $(x, y)$, exactly two moves are permissible:
      1. Move 1: $(x, y) \implies (x + y, \; y)$
      2. Move 2: $(x, y) \implies (x, \; x + y)$
    - All coordinates remain strictly positive integers.
    - Objective: Determine if there exists a valid sequence of moves transforming $(sx, sy)$ into $(tx, ty)$.
    - For $(1, 1)$ and $(3, 5)$:
      - Step 0: $(1, 1)$
      - Step 1: $(1, 1 + 1) = (1, 2)$
      - Step 2: $(1 + 2, 2) = (3, 2)$
      - Step 3: $(3, 2 + 3) = (3, 5)$
      - Target reached in 3 moves $\implies$ return **`true`**.
- **Reverse Determinism & Euclidean Modulo Invariant:**
  - **The Curse of Forward Branching:**
    - Moving forward from $(sx, sy)$ produces an exponential binary tree of depth up to $10^9$ with $2^{10^9}$ states, rendering forward search impossible.
  - **The Deterministic Reverse Predecessor:**
    - Examine the target point $(tx, ty)$:
      - If $tx > ty$, the last operation **must have been** $(tx - ty, ty) \to (tx, ty)$ because adding positive coordinates to $y$ could never produce a larger $x$.
      - If $ty > tx$, the last operation **must have been** $(tx, ty - tx) \to (tx, ty)$.
      - If $tx == ty$, no valid previous positive integer state exists.
    - Thus, moving backward from $(tx, ty)$ has a branching factor of **strictly 1**!
  - **Euclidean Modulo Acceleration:**
    - If $tx \gg ty$, repeatedly subtracting $ty$ from $tx$ takes $\lfloor tx / ty \rfloor$ steps.
    - We can execute all of these subtractions in a single $\mathcal{O}(1)$ modulo step:
      $$
      tx \leftarrow tx \pmod{ty}
      $$
    - This is identical to the classic Euclidean Greatest Common Divisor (GCD) algorithm!
  - **Boundary Alignment Invariant:**
    - Once one coordinate reaches the start level (e.g. $tx == sx$):
      - We can no longer subtract $tx$ indiscriminately without undershooting $sx$.
      - The remaining coordinate $ty$ must reduce to $sy$ purely by subtracting multiples of $tx$.
      - This is possible if and only if:
        $$
        ty \ge sy \quad \text{and} \quad (ty - sy) \pmod{tx} == 0
        $$
- **Step-by-Step Worked Execution Trace on $(sx, sy) = (1, 1), (tx, ty) = (3, 5)$:**
  - Initial target state: $(tx, ty) = (3, 5)$. Source: $(sx, sy) = (1, 1)$.
  - **Round 1:**
    - Compare coordinates: $tx = 3, ty = 5$.
    - $ty > tx \iff 5 > 3 \implies$ last move added $x$ to $y$.
    - Reduce $ty$ modulo $tx$:
      $$
      ty \leftarrow 5 \pmod 3 = \mathbf{2}
      $$
    - New target state: $(tx, ty) = (\mathbf{3}, \; \mathbf{2})$.
    - Verify against source: $tx > sx$ ($3 > 1$) and $ty > sy$ ($2 > 1$). Continue loop.
  - **Round 2:**
    - Compare coordinates: $tx = 3, ty = 2$.
    - $tx > ty \iff 3 > 2 \implies$ last move added $y$ to $x$.
    - Reduce $tx$ modulo $ty$:
      $$
      tx \leftarrow 3 \pmod 2 = \mathbf{1}
      $$
    - New target state: $(tx, ty) = (\mathbf{1}, \; \mathbf{2})$.
    - Verify against source: $tx == sx = 1$.
    - Loop terminates because $tx$ is no longer strictly greater than $sx$.
  - **Round 3: Boundary Alignment Evaluation:**
    - We have $tx == sx = 1$, and $ty = 2$ while $sy = 1$.
    - Can $ty = 2$ reach $sy = 1$ by subtracting $tx = 1$?
      1. Condition 1: $ty \ge sy \iff 2 \ge 1 \implies \mathbf{True.}$
      2. Condition 2: Modular alignment:
         $$
         (ty - sy) \pmod{tx} = (2 - 1) \pmod 1 = 1 \pmod 1 = \mathbf{0}
         $$
      - Exactly $(2 - 1) / 1 = 1$ step of subtracting $tx = 1$ converts $(1, 2)$ to $(1, 1)$!
  - **Final Output:**
    $$
    ans = \mathbf{true}
    $$
- **Unreachable Equal Target Trace ($(sx, sy) = (1, 1), (tx, ty) = (2, 2)$):**
  - $tx == ty = 2$.
  - Neither coordinate can be strictly greater than the other; no prior positive state exists.
  - $tx \ne sx$ ($2 \ne 1$) and $ty \ne sy$ ($2 \ne 1$).
  - Returns **`false`**.
- **Large Coordinate Leap Trace ($(1, 1) \to (1, 10^9)$):**
  - $tx == sx = 1$.
  - $(10^9 - 1) \pmod 1 = 0 \implies$ True in $\mathcal{O}(1)$ time!
  - Naive subtraction would take $10^9$ loops; modulo handles it instantly.

This instance demonstrates backward induction on monoid action orbits and Euclidean division ring contraction, mathematically proves why determinism of the inverse linear transition $T^{-1}$ collapses search tree branching from $2^d$ to 1, and derives $O(\log(\max(tx, ty)))$ runtime and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given start point $(sx, sy)$ and target point $(tx, ty)$:
You can move $(x, y) \to (x + y, y)$ or $(x, x + y)$.
Determine if $(sx, sy)$ can reach $(tx, ty)$.

```text
Start: (1, 1), Target: (3, 5)

Work BACKWARDS from (3, 5):
  Since 5 > 3, previous must be (3, 5 - 3) = (3, 2).
  Since 3 > 2, previous must be (3 - 2, 2) = (1, 2).
  At (1, 2), x matches start x (1 == 1).
  Remaining difference: (2 - 1) is a multiple of 1 -> REACHABLE!

Result: true
```

### The Invariant of the Deterministic Reverse Step
- Moving forward branches into 2 choices at every step ($2^d$ explosion).
- Moving **backward** is completely deterministic:
  - If $tx > ty$, the only possible predecessor is $(tx - ty, ty)$.
  - If $ty > tx$, the only possible predecessor is $(tx, ty - tx)$.
- Replacing repeated subtraction with modulo ($tx \pmod{ty}$) runs in logarithmic Euclidean time.

---

## 2. Conceptual Foundation & Invariants

### 1. Reverse Euclidean Reduction:
$$
\text{while } tx > sx \ \land \ ty > sy \ \land \ tx \ne ty:
$$
$$
\quad \text{if } tx > ty \implies tx \leftarrow tx \bmod ty \quad \text{else } ty \leftarrow ty \bmod tx
$$

### 2. Single-Axis Residual Alignment:
$$
\text{if } tx == sx \implies \text{return } (ty \ge sy \ \land \ (ty - sy) \bmod tx == 0)
$$
$$
\text{if } ty == sy \implies \text{return } (tx \ge sx \ \land \ (tx - sx) \bmod ty == 0)
$$

> **Free Monoid Orbit Invariant.** The forward transitions generate the orbit of the action of $SL_2(\mathbb{N})$ on $\mathbb{N}^2$. By the uniqueness of the continued fraction decomposition (Euclidean algorithm), each element has a unique ancestor under the inverse transformation $T^{-1}$.

---

## 3. Step-by-Step Worked Execution

We trace $(1, 1) \to (3, 5)$:

---

### Step 1: $(3, 5)$
- $ty > tx \iff 5 > 3 \implies ty = 5 \bmod 3 = 2 \implies (3, 2)$.

---

### Step 2: $(3, 2)$
- $tx > ty \iff 3 > 2 \implies tx = 3 \bmod 2 = 1 \implies (1, 2)$.

---

### Step 3: Check Boundary $tx == sx$
- $tx = 1 == sx = 1$.
- Check $ty$: $2 \ge 1$ and $(2 - 1) \bmod 1 = 0 \implies$ Valid!

---

### Step 4: Output
$$
\mathbf{true}
$$

---

## 4. Complete Execution Trace

| State $(tx, ty)$ | Comparison | Reduction Applied | New State | Loop Termination Condition? |
|:---:|:---:|:---:|:---:|:---:|
| $(3, 5)$ | $ty > tx$ ($5 > 3$) | $ty \leftarrow 5 \bmod 3$ | $(3, 2)$ | No |
| $(3, 2)$ | $tx > ty$ ($3 > 2$) | $tx \leftarrow 3 \bmod 2$ | $(1, 2)$ | Yes ($tx == sx = 1$) |
| **Residual** | **$tx == sx$** | **$(ty - sy) \bmod tx$** | **$(2 - 1) \bmod 1 = 0$** | **Result: `true`** |

---

## 5. Boundary Cases & Failure Modes

- **Start Equals Target ($sx == tx, sy == ty$):** Returns `true` immediately.
- **Target Below Start ($tx < sx$ or $ty < sy$):** Coordinates can only increase $\implies$ returns `false`.
- **Target Coordinates Equal ($tx == ty$ with $tx > sx$):** No positive integer step can produce equal coordinates $\implies$ returns `false`.
- **Large Step Gap ($(1, 1) \to (1, 10^9)$):** Modulo handles $10^9$ subtraction steps in a single operation without TLE.

---

## 6. Traps & Common Anti-Patterns

- **Searching Forward (BFS / DFS / Recursion):** Forward search branches exponentially and TLEs immediately on coordinates up to $10^9$. Reverse search is deterministic with 0 branching.
- **Using Subtraction Instead of Modulo (`tx -= ty`):** If $tx = 10^9$ and $ty = 1$, subtracting $ty$ takes $10^9$ iterations, causing TLE. Modulo `tx %= ty` computes all subtractions in $O(1)$.
- **Modulo Over-Shooting $sx$:** You cannot blindly do `tx %= ty` when $ty == sy$, because it could reduce $tx$ below $sx$. That is why the loop stops when $tx \le sx$ or $ty \le sy$, switching to the residual check `(tx - sx) % ty == 0`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - At each step, either $tx$ or $ty$ is reduced modulo the other.
  - By Euclidean algorithm properties, the larger coordinate is reduced by at least a factor of 2 every two steps: $\mathcal{O}(\log(\max(tx, ty)))$.
  - Total Time: strictly logarithmic $\mathcal{O}(\log(\max(tx, ty)))$ where coordinates $\le 10^9 \implies \le 30$ operations. Completes in $< 0.01$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (only scalar coordinate updates).
