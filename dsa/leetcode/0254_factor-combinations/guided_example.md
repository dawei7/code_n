# Guided Example: Factor Combinations

We trace the step-by-step non-decreasing factor constraint, quotient remainder decomposition, and square-root branching bound on representative integer factorization instances:

- **Input:** $n = 12$
- **Required output:** $[[2, 6], [2, 2, 3], [3, 4]]$ (All non-trivial factorizations of 12 into factors in $[2, n - 1]$)
- **Prime Input Instance:** $n = 37 \implies []$ (No non-trivial factors exist)
- **Base Input Instance:** $n = 1 \implies []$ (No factors $\ge 2$)
- **Power of Two Instance:** $n = 32 \implies [[2, 16], [2, 2, 8], [2, 2, 2, 4], [2, 2, 2, 2, 2], [2, 4, 4], [4, 8]]$

This instance demonstrates recursive backtracking with monotonic factor ordering, proves why restricting the search to $f \le \lfloor \sqrt{\text{rem}} \rfloor$ combined with a non-decreasing lower bound $f \ge \text{start}$ eliminates duplicate permutations (such as $[2, 6]$ vs $[6, 2]$) at generation time, dynamically emits quotient terminations, and operates with logarithmic stack depth.

---

## 1. Instance & Teaching Goal

Given an integer $n = 12$, find all combinations of factors in $[2, n - 1]$ whose product equals $n$:
```text
12 = 2 * 6
12 = 2 * 2 * 3
12 = 3 * 4
Output: [[2, 6], [2, 2, 3], [3, 4]]
```

- A naive recursive generator testing all divisor permutations would find both $[2, 6]$ and $[6, 2]$, requiring an expensive deduplication set.
- By enforcing that factors are chosen in **non-decreasing order** ($f_1 \le f_2 \le \dots \le f_k$), each factorization is generated in exactly one canonical sorted form.
- By capping trial divisors at $\lfloor \sqrt{\text{rem}} \rfloor$, the complementary quotient $\text{rem} / f$ is guaranteed to be $\ge f$, immediately yielding a valid final factor.

---

## 2. Conceptual Foundation & Invariants

### Canonical Non-Decreasing Factor Invariant
A factorization $n = f_1 \times f_2 \times \dots \times f_k$ is valid if:
$$
2 \le f_1 \le f_2 \le \dots \le f_k < n
$$
Because the factors are sorted, each multiset of factors appears exactly once.

### Backtracking Protocol: `backtrack(rem, start, path)`
1. **Emit Remainder as Final Factor:**
   If `path` is not empty (guaranteeing at least two factors in the complete combination):
   Since all previous factors were $\le \text{start}$, if $\text{rem} \ge \text{start}$:
   $$
   \text{results}.\text{append}(\text{path} + [\text{rem}])
   $$
2. **Explore Deeper Decompositions:**
   For trial factor $f$ from $\text{start}$ up to $\lfloor \sqrt{\text{rem}} \rfloor$:
   If $\text{rem} \pmod f == 0$:
   - Choose factor: $\text{path}.\text{append}(f)$
   - Recurse with remainder $\text{rem} / f$ and lower bound $f$:
     $$
     \text{backtrack}(\text{rem} // f, \; f, \; \text{path})
     $$
   - Backtrack: $\text{path}.\text{pop}()$

*(Notice: Stopping trial factors at $\lfloor \sqrt{\text{rem}} \rfloor$ avoids symmetric redundant splits. Any divisor above $\sqrt{\text{rem}}$ corresponds to a paired divisor below $\sqrt{\text{rem}}$ that was already evaluated)*.

> **Invariant.** Inside `backtrack(rem, start, path)`, `rem` equals $n / \prod_{x \in \text{path}} x$, and every future factor candidate satisfies $f \ge \text{start} \ge \text{path}[-1]$.

---

## 3. Step-by-Step Worked Execution

We trace `backtrack(rem = 12, start = 2, path = [])`:

### Top-Level Call: $\text{rem} = 12, \, \text{start} = 2, \, \text{path} = []$
- `path` is empty (the single factor $[12]$ is forbidden by the problem statement).
- Search range for $f$: from $\text{start} = 2$ up to $\lfloor \sqrt{12} \rfloor = 3$.

---

### Branch 1: Choose $f = 2$
- $12 \pmod 2 == 0$. Append $2 \implies \text{path} = [2]$.
- **Sub-call: `backtrack(rem = 6, start = 2, path = [2])`**
  1. `path` is non-empty! Remainder $6 \ge \text{start} = 2$.
     - **Record result:** $\text{path} + [6] = \mathbf{[2, 6]}$.
  2. Search for next factor $f \in [2 \dots \lfloor \sqrt{6} \rfloor = 2]$:
     - Test $f = 2$: $6 \pmod 2 == 0$. Append $2 \implies \text{path} = [2, 2]$.
     - **Sub-call: `backtrack(rem = 3, start = 2, path = [2, 2])`**
       - `path` non-empty! Remainder $3 \ge \text{start} = 2$.
       - **Record result:** $\text{path} + [3] = \mathbf{[2, 2, 3]}$.
       - Search range: $f \in [2 \dots \lfloor \sqrt{3} \rfloor = 1]$ $\implies$ empty!
       - Return.
     - Backtrack: $\text{path}.\text{pop}() \implies [2]$.
  3. Loop finishes. Return.
- Backtrack: $\text{path}.\text{pop}() \implies []$.

---

### Branch 2: Choose $f = 3$
- $12 \pmod 3 == 0$. Append $3 \implies \text{path} = [3]$.
- **Sub-call: `backtrack(rem = 4, start = 3, path = [3])`**
  1. `path` is non-empty! Remainder $4 \ge \text{start} = 3$.
     - **Record result:** $\text{path} + [4] = \mathbf{[3, 4]}$.
  2. Search for next factor $f \in [3 \dots \lfloor \sqrt{4} \rfloor = 2]$ $\implies$ range is empty ($3 > 2$).
  3. Return.
- Backtrack: $\text{path}.\text{pop}() \implies []$.

---

### End of Top-Level Loop
Collected results:
$$
\mathbf{[[2, 6], [2, 2, 3], [3, 4]]}
$$

---

## 4. Complete Execution Trace

```text
n = 12

backtrack(12, 2, [])
  f = 2: path = [2]
    backtrack(6, 2, [2])
      Record: [2, 6]
      f = 2: path = [2, 2]
        backtrack(3, 2, [2, 2])
          Record: [2, 2, 3]
          f in [2..1] -> stop
        pop -> path = [2]
      f in [2..2] done -> return
    pop -> path = []

  f = 3: path = [3]
    backtrack(4, 3, [3])
      Record: [3, 4]
      f in [3..2] -> stop
    pop -> path = []

Output: [[2, 6], [2, 2, 3], [3, 4]]
```

| Depth | $\text{rem}$ | $\text{start}$ | Current `path` | Trial Range $f \in [\text{start}, \sqrt{\text{rem}}]$ | Emitted Combination ($\text{path} + [\text{rem}]$) | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 12 | 2 | `[]` | $[2 \dots 3]$ | - (Top-level excluded) | Explore $f = 2$ |
| 1 | 6 | 2 | `[2]` | $[2 \dots 2]$ | **`[2, 6]`** | Explore $f = 2$ |
| 2 | 3 | 2 | `[2, 2]` | Empty ($2 > 1$) | **`[2, 2, 3]`** | Backtrack to depth 1 |
| 0 | 12 | 2 | `[]` | $[2 \dots 3]$ | - | Explore $f = 3$ |
| 1 | 4 | 3 | `[3]` | Empty ($3 > 2$) | **`[3, 4]`** | Backtrack to depth 0 |
| **End** | - | - | `[]` | - | **`[[2, 6], [2, 2, 3], [3, 4]]`** | Completed |

---

## 5. Algorithmic Correctness

**Soundness.** Every emitted list $L = \text{path} + [\text{rem}]$ has product $\prod_{x \in \text{path}} x \times \text{rem} = n$. Because each recursive step enforces $f \ge \text{start}$, and $\text{rem} \ge f$ by the square-root bound $\sqrt{\text{rem}} \ge f$, the elements of $L$ are strictly non-decreasing. Because `path` is required to be non-empty, $L$ contains at least two factors, none of which equals $n$.

**Completeness.** Any valid factorization into non-decreasing factors $f_1 \le f_2 \le \dots \le f_k$ has $f_1 \le \sqrt{n}$. The top-level loop tests all divisors up to $\sqrt{n}$. By induction, every prefix of factors will be explored, and the final factor $f_k$ will be captured as the terminal remainder.

---

## 6. Traps This Instance Exposes

- **Excluding the Single Factor $[n]$:** If the check `if path:` is omitted, the top-level call would emit $[n]$ (e.g. $[12]$), violating the problem requirement that factors must be in $[2, n - 1]$.
- **Square-Root Bound Equality ($f \times f \le \text{rem}$):** The loop must include the square root ($f \le \lfloor \sqrt{\text{rem}} \rfloor$). For square numbers like $16$, testing $f = 4$ generates $[4, 4]$. Using strict inequality ($f < \sqrt{\text{rem}}$) misses symmetric pairs!
- **Allowing Factor Repetition ($f$ vs $f + 1$):** When recursing, the new `start` bound must be $f$, not $f + 1$, allowing prime powers like $[2, 2, 2]$ to be generated.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\sqrt{n} + K \cdot L)$, where $K$ is the number of factor combinations and $L \le \log_2 n$ is the maximum combination length. The recursion tree branches only at actual divisors of $n$, and trial division at each state checks at most $\sqrt{\text{rem}}$ candidates.
- **Auxiliary Space Complexity:** $O(\log n)$ auxiliary stack memory. Since each factor is $\ge 2$, the maximum recursion depth is bounded by $\log_2 n$.
