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

### A Seven-Call Trace Where the Two Bounds Interact ($n = 32$)

For $n = 12$ every call still has a non-empty trial range, so it never becomes clear what happens when the lower bound $\text{start}$ overtakes the square-root cap. The power-of-two instance separates the two bounds: the top call has two divisors to explore, and three later calls have no trial factors at all.

| Visit | Call state $(\text{rem}, \text{start}, \text{path})$ | Emitted combination | Divisors found in $[\text{start}, \lfloor\sqrt{\text{rem}}\rfloor]$ | Trial factors rejected | Depth |
|:---:|:---|:---|:---|:---|:---:|
| 1 | $(32, 2, [\,])$ | none: the path is empty, so $[32]$ is correctly suppressed | $2$ and $4$ | $3$ and $5$ do not divide; $6$ exceeds $\lfloor\sqrt{32}\rfloor = 5$ | 0 |
| 2 | $(16, 2, [2])$ | `[2, 16]` | $2$ and $4$ | $3$ does not divide | 1 |
| 3 | $(8, 2, [2, 2])$ | `[2, 2, 8]` | $2$ | $3$ exceeds $\lfloor\sqrt{8}\rfloor = 2$ | 2 |
| 4 | $(4, 2, [2, 2, 2])$ | `[2, 2, 2, 4]` | $2$ | $3$ exceeds $\lfloor\sqrt{4}\rfloor = 2$ | 3 |
| 5 | $(2, 2, [2, 2, 2, 2])$ | `[2, 2, 2, 2, 2]` | none: the range $[2, 1]$ is empty because $\lfloor\sqrt{2}\rfloor = 1$ is below $\text{start}$ | every candidate is excluded by the cap | 4 |
| 6 | $(4, 4, [2, 4])$ | `[2, 4, 4]` | none: the range $[4, 2]$ is empty because $\lfloor\sqrt{4}\rfloor = 2$ is below $\text{start} = 4$ | every candidate is excluded by the lower bound | 2 |
| 7 | $(8, 4, [4])$ | `[4, 8]` | none: the range $[4, 2]$ is empty for the same reason | every candidate is excluded by the lower bound | 1 |

The seven visits emit exactly the six required combinations, in the order `[2, 16]`, `[2, 2, 8]`, `[2, 2, 2, 4]`, `[2, 2, 2, 2, 2]`, `[2, 4, 4]`, `[4, 8]`. Visits 5, 6 and 7 are the interesting ones: a call stops exploring for two different reasons, either because the remainder has become too small to contain a factor (visit 5) or because the non-decreasing lower bound has caught up with the cap (visits 6 and 7), and in both cases the remainder itself is still emitted as the final factor. Note also that visit 4 doubles the factor $2$ rather than advancing to $3$, which is what allows the four-fold repetition in visit 5 to exist at all.

---

## 5. Algorithmic Correctness

**Soundness.** Every emitted list $L = \text{path} + [\text{rem}]$ has product $\prod_{x \in \text{path}} x \times \text{rem} = n$. Because each recursive step enforces $f \ge \text{start}$, and $\text{rem} \ge f$ by the square-root bound $\sqrt{\text{rem}} \ge f$, the elements of $L$ are strictly non-decreasing. Because `path` is required to be non-empty, $L$ contains at least two factors, none of which equals $n$.

**Completeness.** Any valid factorization into non-decreasing factors $f_1 \le f_2 \le \dots \le f_k$ has $f_1 \le \sqrt{n}$. The top-level loop tests all divisors up to $\sqrt{n}$. By induction, every prefix of factors will be explored, and the final factor $f_k$ will be captured as the terminal remainder.

---

## 6. Traps This Instance Exposes

- **Excluding the Single Factor $[n]$:** If the check `if path:` is omitted, the top-level call would emit $[n]$ (e.g. $[12]$), violating the problem requirement that factors must be in $[2, n - 1]$.
- **Square-Root Bound Equality ($f \times f \le \text{rem}$):** The loop must include the square root ($f \le \lfloor \sqrt{\text{rem}} \rfloor$). For square numbers like $16$, testing $f = 4$ generates $[4, 4]$. Using strict inequality ($f < \sqrt{\text{rem}}$) misses symmetric pairs!
- **Allowing Factor Repetition ($f$ vs $f + 1$):** When recursing, the new `start` bound must be $f$, not $f + 1$, allowing prime powers like $[2, 2, 2]$ to be generated.

### Boundary instances and the shape of the trial range

Every row is a separate input, and the third column reports the complete result so the effect of the square-root cap can be seen directly.

| Instance | Top-level trial range $[\text{start}, \lfloor\sqrt{n}\rfloor]$ | Complete result | Which boundary it fixes |
|:---|:---|:---|:---|
| $n = 1$ | $[2, 1]$, empty | `[]` | no factor $\ge 2$ exists at all, so the loop never starts and the empty path never emits |
| $n = 2$ | $[2, 1]$, empty | `[]` | the smallest prime must not emit the forbidden single factor $[2]$ |
| $n = 4$ | $[2, 2]$ | `[[2, 2]]` | equality at the cap is required: $2 \times 2$ is the only split |
| $n = 16$ | $[2, 4]$ | `[[2, 8], [2, 2, 4], [2, 2, 2, 2], [4, 4]]` | equality at $f = 4$ produces $[4, 4]$, and repetition produces the length-four chain |
| $n = 49$ | $[2, 7]$ | `[[7, 7]]` | an odd perfect square emits its equal pair, so the cap is not an even-number artefact |
| $n = 37$ | $[2, 6]$ | `[]` | the full scan of $2, 3, 4, 5, 6$ finds no divisor, so a prime above the small range also returns empty |
| $n = 30$ | $[2, 5]$ | `[[2, 15], [2, 3, 5], [3, 10], [5, 6]]` | distinct primes combine at two different lengths, and $f = 4$ is tested and rejected |

The $n = 16$ and $n = 49$ rows together show why the cap is inclusive: dropping equality would lose $[4, 4]$ and $[7, 7]$, and those are the only outputs for $n = 49$. The $n = 1$ and $n = 2$ rows show the same range collapsing from the other side, where $\lfloor\sqrt{n}\rfloor$ falls below $\text{start} = 2$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\sqrt{n} + K \cdot L)$, where $K$ is the number of factor combinations and $L \le \log_2 n$ is the maximum combination length. The recursion tree branches only at actual divisors of $n$, and trial division at each state checks at most $\sqrt{\text{rem}}$ candidates.
- **Auxiliary Space Complexity:** $O(\log n)$ auxiliary stack memory. Since each factor is $\ge 2$, the maximum recursion depth is bounded by $\log_2 n$.

### Cost of the alternatives

The counts below are the exact totals for the two worked instances, so the deduplication saving is measurable rather than asymptotic.

| Strategy | Mechanism | Work on $n = 12$ | Work on $n = 32$ | Cost or failure mode |
|:---|:---|:---|:---|:---|
| Ordered permutation search with a deduplication set | generate every ordering of every factor multiset, then canonicalise and discard repeats | $7$ ordered sequences collapse to $3$ multisets | $15$ ordered sequences collapse to $6$ multisets | correct only after deduplication, and it does $2.3$ to $2.5$ times the generation work here; the waste grows with the number of repeated factors |
| Non-decreasing search with a square-root cap (the method used) | one canonical order, trial factors capped at $\lfloor\sqrt{\text{rem}}\rfloor$ | $3$ emissions from $4$ calls in total: the top call plus three descents | $6$ emissions from $7$ calls | each multiset is generated exactly once, so no deduplication structure is needed |
| Precompute every divisor of $n$, then recurse over that list | build the divisor list once, then treat the same problem as a combination search over it | divisor list $[2, 3, 4, 6]$ | divisor list $[2, 4, 8, 16]$ | removes the modulo tests, but stores the divisor list and still needs the non-decreasing rule to avoid duplicates |
| Explicit stack instead of recursion | push and pop call frames manually | same $3$ emissions in the same order | same $6$ emissions in the same order | identical results with no call-stack depth, at the price of managing $\text{rem}$, $\text{start}$ and the path by hand |

The recursion depth stays small in both instances: the deepest call for $n = 32$ is visit 5 at depth $4$, comfortably inside the $\log_2 32 = 5$ bound, which is why the recursive formulation is not a practical risk and the explicit stack is only a stylistic alternative.
