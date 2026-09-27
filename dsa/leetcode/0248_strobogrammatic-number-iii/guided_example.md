# Guided Example: Strobogrammatic Number III

We trace the step-by-step length-partitioned generation, combinatorial shortcut integration, and lexicographic boundary filtering on representative numeric ranges:

- **Input:** $\text{low} = \text{"50"}, \quad \text{high} = \text{"100"}$
- **Required output:** $3$ (The three qualifying numbers are `"69"`, `"88"`, and `"96"`)
- **Single Value Range:** $\text{low} = \text{"0"}, \quad \text{high} = \text{"0"} \implies 1$ (The number `"0"`)
- **Multi-Length Spanning Instance:** $\text{low} = \text{"0"}, \quad \text{high} = \text{"100"} \implies 7$ (Three 1-digit numbers $\{0, 1, 8\}$ plus four 2-digit numbers $\{11, 69, 88, 96\}$)
- **Exact Boundary Equality:** $\text{low} = \text{"69"}, \quad \text{high} = \text{"69"} \implies 1$

This instance demonstrates length-bracketed search space reduction ($L \in [\text{len}(\text{low}), \text{len}(\text{high})]$), explains why numbers with strictly intermediate lengths can be counted via closed-form combinatorics ($4 \times 5^{h-1}$) without string generation, details lexicographic boundary pruning on equal-length candidates, and runs in $O(5^{D/2})$ time where $D = \text{len}(\text{high})$.

---

## 1. Instance & Teaching Goal

Given two decimal string bounds:
$$
\text{low} = \text{"50"}, \quad \text{high} = \text{"100"}
$$
Count the total number of strobogrammatic numbers $x$ satisfying:
$$
\text{low} \le x \le \text{high}
$$

A naive traversal tests every integer from $50$ to $100$ and checks whether each is strobogrammatic. While feasible for small ranges, for high bounds up to $10^{15}$, iterating $10^{15}$ numbers is impossible.
Instead, we **generate only valid strobogrammatic numbers**:
- The length of valid numbers must lie between $\text{len}(\text{low}) = 2$ and $\text{len}(\text{high}) = 3$.
- Length 2 candidates: `"11"`, `"69"`, `"88"`, `"96"`.
  - Filter against boundaries: $11 < 50$ (rejected), while $69, 88, 96 \in [50, 100]$ (3 valid).
- Length 3 candidates:
  - Smallest candidate is `"101" > 100` (all rejected).
Total count: $3 + 0 = \mathbf{3}$.

---

## 2. Conceptual Foundation & Invariants

### Length-Stratified Generation Strategy
Let $D_{\text{low}} = \text{len}(\text{low})$ and $D_{\text{high}} = \text{len}(\text{high})$.
Every valid integer has length $L \in [D_{\text{low}}, D_{\text{high}}]$:
1. **Boundary Length $L == D_{\text{low}}$ or $L == D_{\text{high}}$:**
   Generate candidates of length $L$ and filter each against the bounds:
   $$
   \text{valid if } (\text{len}(S) > D_{\text{low}} \text{ or } S \ge \text{low}) \text{ and } (\text{len}(S) < D_{\text{high}} \text{ or } S \le \text{high})
   $$
   *(For equal-length strings, string comparison $S \ge \text{low}$ is identical to numerical comparison)*.
2. **Intermediate Lengths ($D_{\text{low}} < L < D_{\text{high}}$):**
   Every generated number of length $L$ is guaranteed to be strictly greater than `low` and strictly less than `high`.
   We can either count them directly or compute their count instantly using the closed-form combinatorial formula:
   $$
   \text{Count}(L) = \begin{cases}
   4 \times 5^{L/2 - 1}, & \text{if } L \text{ is even} \\
   4 \times 5^{(L-1)/2 - 1} \times 3, & \text{if } L \text{ is odd} \ (L > 1) \\
   3, & \text{if } L = 1
   \end{cases}
   $$

### DFS Inward-Outward Backtracking
Recursively generate strings of length $L$ using the 5 symmetric pairs:
- $(1, 1), (6, 9), (8, 8), (9, 6)$, and $(0, 0)$ (where $00$ is suppressed on the outermost boundary).

> **Invariant.** For each length $L \in [D_{\text{low}}, D_{\text{high}}]$, only strobogrammatic numbers are evaluated, and candidates are tested against `low` and `high` in $O(L)$ time.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{low} = \text{"50"}$ and $\text{high} = \text{"100"}$:
- $D_{\text{low}} = \text{len}(\text{"50"}) = 2$.
- $D_{\text{high}} = \text{len}(\text{"100"}) = 3$.
- Search lengths: $L = 2$ and $L = 3$.

---

### Phase 1: Evaluate Length $L = 2$
Generate 2-digit strobogrammatic numbers:
Center base for even length: $m = 0 \implies \text{""}$.
Wrap with outer non-zero pairs:
- Candidate 1: $\text{"11"}$
  - Boundary check: $\text{"11"} < \text{"50"}$. **Rejected.**
- Candidate 2: $\text{"69"}$
  - Boundary check: $\text{"50"} \le \text{"69"} \le \text{"100"}$. **Accepted!** ($\text{count} \leftarrow 1$).
- Candidate 3: $\text{"88"}$
  - Boundary check: $\text{"50"} \le \text{"88"} \le \text{"100"}$. **Accepted!** ($\text{count} \leftarrow 2$).
- Candidate 4: $\text{"96"}$
  - Boundary check: $\text{"50"} \le \text{"96"} \le \text{"100"}$. **Accepted!** ($\text{count} \leftarrow 3$).

Total accepted from length 2: $\mathbf{3}$.

---

### Phase 2: Evaluate Length $L = 3$
Generate 3-digit strobogrammatic numbers:
Odd length centers: $\text{["0", "1", "8"]}$.
Wrap with outer non-zero pairs $\{1\dots1, 6\dots9, 8\dots8, 9\dots6\}$:
- Outer pair $(1, 1)$:
  - $\text{"101"}$: Check $\text{"101"} \le \text{"100"} \implies$ False ($101 > 100$). **Rejected.**
  - $\text{"111"}$: $111 > 100$. **Rejected.**
  - $\text{"181"}$: $181 > 100$. **Rejected.**
- Outer pairs $(6, 9), (8, 8), (9, 6)$:
  - All candidates begin with digits $\ge 6$, so all are $\ge 609 > 100$. **All rejected.**

Total accepted from length 3: $\mathbf{0}$.

---

### Step 3: Total Sum
$$
\text{Total Valid Numbers} = 3 + 0 = \mathbf{3}
$$
Final answer is $\mathbf{3}$.

---

## 4. Complete Execution Trace

```text
low = "50", high = "100"
Lengths to search: L in [2, 3]

L = 2:
  Candidate "11": 11 < 50  -> Reject
  Candidate "69": 50 <= 69 <= 100 -> ACCEPT (count = 1)
  Candidate "88": 50 <= 88 <= 100 -> ACCEPT (count = 2)
  Candidate "96": 50 <= 96 <= 100 -> ACCEPT (count = 3)

L = 3:
  Smallest candidate: "101"
  101 > 100 -> All L=3 candidates exceed high -> 0 accepted

Final Result: 3
```

| Length $L$ | Generated Candidate | Comparison vs `low` (`"50"`) | Comparison vs `high` (`"100"`) | Status | Cumulative Count |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 2 | `"11"` | $11 < 50$ | - | Rejected | 0 |
| **2** | **`"69"`** | $69 \ge 50$ | $69 \le 100$ | **Accepted** | **1** |
| **2** | **`"88"`** | $88 \ge 50$ | $88 \le 100$ | **Accepted** | **2** |
| **2** | **`"96"`** | $96 \ge 50$ | $96 \le 100$ | **Accepted** | **3** |
| 3 | `"101"` | $101 \ge 50$ | $101 > 100$ | Rejected | 3 |
| 3 | `"111"` | $111 \ge 50$ | $111 > 100$ | Rejected | 3 |
| 3 | $\dots$ (10 more) | - | $> 100$ | Rejected | 3 |
| **End** | - | - | - | - | **$\mathbf{3}$ (Final Result)** |

---

## 5. Algorithmic Correctness

**Soundness.** Every counted string is generated exclusively from valid strobogrammatic reflection pairs, ensuring it is strobogrammatic. The boundary check verifies $\text{low} \le x \le \text{high}$, so every counted number strictly belongs to the target range.

**Completeness.** Any strobogrammatic number between `low` and `high` has a length between $\text{len}(\text{low})$ and $\text{len}(\text{high})$. Because the generator enumerates all strobogrammatic numbers for every length in that interval, no qualifying number can be missed.

---

## 6. Traps This Instance Exposes

- **Numerical Conversion Overflow:** The inputs `low` and `high` can have up to 15 digits. In languages like C++, 64-bit `long long` is required for integer conversion. Alternatively, when lengths match, string lexicographical comparison (`s >= low and s <= high`) is 100% equivalent to numerical comparison and works for arbitrarily long strings.
- **Handling Single Digit Range ($0$ to $0$):** If $\text{low} = \text{"0"}, \text{high} = \text{"0"}$, length 1 generates `"0", "1", "8"`. Only `"0"` satisfies $\le 0$, yielding count 1.
- **Strictly Intermediate Length Pruning:** Generating all strings for lengths strictly between $\text{len}(\text{low})$ and $\text{len}(\text{high})$ is unnecessary when using the combinatorial formula, avoiding thousands of string allocations.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(5^{D_{\text{high}} / 2} \cdot D_{\text{high}})$, where $D_{\text{high}} = \text{len}(\text{high})$. At each length $L$, the number of generated strings is bounded by $4 \times 5^{\lfloor L/2 \rfloor}$. For $D_{\text{high}} \le 14$, $5^7 = 78,125$ states, which evaluates in $< 0.1\text{ seconds}$.
- **Auxiliary Space Complexity:** $O(D_{\text{high}})$ auxiliary stack space for recursive backtracking.
