# Guided Example: Reorganize String

We trace the step-by-step character frequency distribution analysis, Pigeonhole Principle feasibility threshold evaluation ($mx \le \lfloor (n+1)/2 \rfloor$), impossibility detection ($mx > \lfloor (n+1)/2 \rfloor \implies \text{""}$), most-common frequency priority ordering, even-then-odd index interleaving ($0, 2, \dots$ then $1, 3, \dots$), and non-adjacent character string assembly on representative anagrams:

- **Input:** $s = \text{"aab"}$
- **Required output:** `"aba"`
  - Reorganization specifications:
    - Rearrange the characters of $s$ so that **no two adjacent characters are identical**:
      $$
      ans[i] \ne ans[i + 1] \quad \forall i \in [0, n - 2]
      $$
    - If such a rearrangement is mathematically impossible, return the empty string `""`.
    - For $s = \text{"aab"}$ (length $n = 3$):
      - Frequencies: `'a'` appears 2 times, `'b'` appears 1 time.
      - Most frequent character: `'a'` with $count = 2$.
      - Maximum allowed frequency for non-adjacent placement in length 3:
        $$
        \lfloor (3 + 1) / 2 \rfloor = \mathbf{2}
        $$
      - Since $2 \le 2$, a valid arrangement exists.
      - Placing `'a'` on alternating positions: index 0 and index 2.
      - Placing `'b'` in the gap: index 1.
      - Resulting string `"aba"` has adjacent pairs `('a', 'b')` and `('b', 'a')` with zero collisions!
- **Pigeonhole Feasibility & Stride-2 Interleaving Invariant:**
  - **The Pigeonhole Impossibility Bound:**
    - In any string of length $n$, the maximum number of mutually non-adjacent positions that any single character can occupy is:
      $$
      \text{Cap}_{\max} = \left\lceil \frac{n}{2} \right\rceil = \left\lfloor \frac{n + 1}{2} \right\rfloor
      $$
    - If any character has frequency $mx > \lfloor (n + 1) / 2 \rfloor$:
      - By the Pigeonhole Principle, at least two copies of this character must be adjacent in **every conceivable permutation**.
      - In this case, return `""` immediately.
  - **Even-Odd Phase Filling Guarantee:**
    - When $mx \le \lfloor (n + 1) / 2 \rfloor$:
      - Sort all characters in descending order of frequency (`most_common`).
      - Place characters into the output array by advancing with stride 2:
        $$
        \text{Phase 1 (Even Positions): } 0, \; 2, \; 4, \; \dots
        $$
        $$
        \text{Phase 2 (Odd Positions): } 1, \; 3, \; 5, \; \dots
        $$
      - Because the dominant character has count $\le \lfloor (n + 1) / 2 \rfloor$, it will fit completely into the even slots.
      - It can never spill into the odd slots, eliminating any possibility of self-adjacency!
- **Step-by-Step Worked Execution Trace on $s = \text{"aab"}$:**
  - String length: $n = 3$. Output buffer: $ans = [\_, \_, \_]$.
  - **Phase 0: Count Frequencies & Test Feasibility:**
    - Frequency map:
      $$
      cnt = \{ \text{'a'}: 2, \; \text{'b'}: 1 \}
      $$
    - Dominant frequency: $mx = 2$.
    - Upper bound:
      $$
      \lfloor (3 + 1) / 2 \rfloor = \mathbf{2}
      $$
    - Verification: $mx \le 2 \iff 2 \le 2 \implies \mathbf{Feasible!}$
  - **Phase 1: Interleaved Placement (Stride 2):**
    - Ordered characters: $(\text{'a'}, 2)$, followed by $(\text{'b'}, 1)$.
    - Pointer starts at first even position: $i = 0$.
    - **Place Character `'a'` (Count = 2):**
      - Place 1st `'a'` at index $i = 0$:
        $$
        ans[0] \leftarrow \mathbf{\text{'a'}}
        $$
        Advance: $i \leftarrow 0 + 2 = 2$.
      - Place 2nd `'a'` at index $i = 2$:
        $$
        ans[2] \leftarrow \mathbf{\text{'a'}}
        $$
        Advance: $i \leftarrow 2 + 2 = 4$.
      - Pointer exceeds length ($4 \ge 3$): wrap to first odd position:
        $$
        i \leftarrow \mathbf{1}
        $$
    - **Place Character `'b'` (Count = 1):**
      - Place `'b'` at index $i = 1$:
        $$
        ans[1] \leftarrow \mathbf{\text{'b'}}
        $$
        Advance: $i \leftarrow 1 + 2 = 3$.
  - **Phase 2: Final String Compilation:**
    - Output array:
      $$
      ans = [\text{'a'}, \; \text{'b'}, \; \text{'a'}]
      $$
    - Joined string:
      $$
      ans = \mathbf{\text{"aba"}}
      $$
- **Impossible Dominant Character Trace ($s = \text{"aaab"}$):**
  - Length $n = 4$.
  - Frequency: `'a'` appears 3 times.
  - Threshold: $\lfloor (4 + 1) / 2 \rfloor = 2$.
  - $mx = 3 > 2 \implies \mathbf{Impossible!}$
  - Returns empty string **`""`**.
- **Alternating Pairs Trace ($s = \text{"aabb"}$):**
  - Length $n = 4$. Frequencies: `'a': 2, 'b': 2$.
  - Even indices $0, 2$ filled with `'a'`: `ans = ['a', _, 'a', _]`.
  - Odd indices $1, 3$ filled with `'b'`: `ans = ['a', 'b', 'a', 'b']`.
  - Returns **`"abab"`**.

This instance demonstrates Pigeonhole threshold partitioning and stride-2 bipartite array interleaving, mathematically proves why sorting by frequency prevents wrap-around adjacency over cyclically separated index subsets, and derives $O(N)$ runtime and $O(|\Sigma|)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a string $s$:
Rearrange characters so **no two adjacent characters are identical**.
Return any valid string, or `""` if impossible.

```text
s = "aab"

Counts: 'a': 2, 'b': 1 (n = 3)
Max frequency: 2 <= (3 + 1) // 2 = 2 -> POSSIBLE!

Fill even positions first (0, 2):
  ans[0] = 'a'
  ans[2] = 'a'
Wrap to odd positions (1):
  ans[1] = 'b'

Result: "aba"
```

### The Invariant of Stride-2 Placement
- The most frequent character cannot exceed $\lfloor (n + 1) / 2 \rfloor$. If it does, adjacent collisions are mathematically inevitable $\implies$ return `""`.
- Placing characters sorted by frequency descending into indices $0, 2, 4 \dots$ then $1, 3, 5 \dots$ guarantees the dominant character never meets itself.

---

## 2. Conceptual Foundation & Invariants

### 1. Pigeonhole Feasibility Test:
$$
\text{Feasible} \iff \max_{c} \text{count}(c) \le \left\lfloor \frac{n + 1}{2} \right\rfloor
$$
$$
\text{if } \max_c \text{count}(c) > \left\lfloor \frac{n + 1}{2} \right\rfloor \implies \text{return } \text{""}
$$

### 2. Stride-2 Interleaving Schedule:
Sort characters by frequency: $(c_1, v_1), (c_2, v_2), \dots$
$$
\text{Indices sequence: } (0, 2, 4, \dots) \text{ followed by } (1, 3, 5, \dots)
$$

> **Bipartite Independent Placement Invariant.** The line graph path $P_n$ is bipartite with independent sets $V_0 = \{2k\}$ and $V_1 = \{2k+1\}$. The maximal independent set has cardinality $\lceil n/2 \rceil = \lfloor (n+1)/2 \rfloor$. Assigning identical symbols exclusively to independent vertex subsets preserves edge-proper vertex coloring.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"aab"}$:

---

### Step 1: Feasibility
- $n = 3$, counts: `'a': 2, 'b': 1$.
- $2 \le (3 + 1) // 2 = 2 \implies$ Valid.

---

### Step 2: Interleave Even Indices
- Index 0 $\to$ `'a'`.
- Index 2 $\to$ `'a'`.

---

### Step 3: Wrap to Odd Indices
- Index 1 $\to$ `'b'`.

---

### Step 4: Output
$$
\mathbf{\text{"aba"}}
$$

---

## 4. Complete Execution Trace

| Step | Placed Character | Frequency Remaining | Target Array Index $i$ | Wrap to Odd? | Buffer State $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | `'a'` | $1$ | $0$ | No | `['a', _, _]` |
| $2$ | `'a'` | $0$ | $2$ | Yes ($i \ge 3 \to 1$) | `['a', _, 'a']` |
| **$3$** | **`'b'`** | **$0$** | **$1$** | **No** | **`['a', 'b', 'a']`** |
| **Final** | — | — | — | — | **`"aba"`** |

---

## 5. Boundary Cases & Failure Modes

- **Impossible Case ($"aaab"$):** Max frequency $3 > 2 \implies$ returns `""`.
- **All Unique ($"abcdef"$):** $mx = 1 \implies$ valid under any ordering.
- **Length 1 ($"a"$):** Returns `"a"`.
- **Even Length with Tied Max ($"aabb"$):** Stride-2 produces `"abab"`.

---

## 6. Traps & Common Anti-Patterns

- **Using a Priority Queue / Max-Heap When Stride-2 Suffices:** A max-heap with pop-two-push-back works in $O(N \log |\Sigma|)$, but sorting frequencies once and placing characters with stride 2 runs in strictly $O(N)$ and requires no heap overhead.
- **Placing Low-Frequency Characters First:** If you place rare characters on even indices first, the dominant character will spill over from even to odd indices and collide with itself. The most frequent character **must be placed first**.
- **Off-By-One on Feasibility Formula:** Using $n // 2$ instead of $(n + 1) // 2$ incorrectly rejects odd-length strings like `"aab"` where $n = 3$ and $mx = 2$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Counting character frequencies: $\mathcal{O}(N)$.
  - Sorting alphabet frequencies: $\mathcal{O}(|\Sigma| \log |\Sigma|)$ where $|\Sigma| \le 26$ is constant $\mathcal{O}(1)$.
  - Filling the $N$-character array with stride 2: $\mathcal{O}(N)$.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 0.1$ ms for $N = 500$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for the output character array.
