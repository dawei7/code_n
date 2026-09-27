# Guided Example: Custom Sort String

We trace the step-by-step priority map construction from custom ordering permutations ($d[c] = rank$), non-comparative bucket counting frequency accumulation, ranked character stream projection, unranked character fallback collection, and custom sorted string reconstruction on representative character sequences:

- **Input:**
  $$
  order = \text{"cba"}, \quad s = \text{"abcd"}
  $$
- **Required output:**
  $$
  \text{"cbad"}
  $$
  *(Any permutation preserving the relative order of characters in $order$ is valid)*
  - Custom ordering requirements:
    - All characters in $order$ are unique and specify a custom priority hierarchy.
    - If character $x$ appears before $y$ in $order$, then all occurrences of $x$ in $s$ must precede all occurrences of $y$ in the reconstructed string.
    - Characters in $s$ that do not appear in $order$ have no ordering constraints and may appear in any position (e.g. at the end).
    - For $order = \text{"cba"}$ and $s = \text{"abcd"}$:
      - Ranked characters present in $s$: `'c'`, `'b'`, `'a'`.
      - Required relative sequence: `'c'` must appear first, then `'b'`, then `'a'`.
      - Unranked characters: `'d'`.
      - Reconstructed string: `"cbad"`.
- **Character Rank Mapping & Bucket Assembly Invariant:**
  - **The Total Preorder Formulation:**
    - Build an index rank table for characters in $order$:
      $$
      \text{rank}(order[i]) = i \quad \forall i \in [0, |order| - 1]
      $$
    - For characters not appearing in $order$, assign an indifferent rank (e.g. $0$ or $\infty$).
  - **Bucket Count Approach ($O(N + M)$):**
    - Count the frequency of every character in $s$:
      $$
      cnt[c] = \text{occurrences of } c \text{ in } s
      $$
    - Phase 1 (Ranked Characters):
      - Iterate through characters $c$ in the exact sequence given by $order$:
      - Append $c$ exactly $cnt[c]$ times.
      - Set $cnt[c] \leftarrow 0$.
    - Phase 2 (Unranked Characters):
      - Append any characters with remaining count $cnt[c] > 0$ in any order.
    - This achieves strict linear time without comparison sorting!
- **Step-by-Step Worked Execution Trace on $order = \text{"cba"}, s = \text{"abcd"}$:**
  - **Phase 0: Priority Mapping:**
    $$
    d = \{ \text{'c'}: 0, \; \text{'b'}: 1, \; \text{'a'}: 2 \}
    $$
  - **Phase 1: Frequency Counting of $s$:**
    $$
    cnt = \{ \text{'a'}: 1, \; \text{'b'}: 1, \; \text{'c'}: 1, \; \text{'d'}: 1 \}
    $$
  - **Phase 2: Emit in Sequence of $order$:**
    - Step 2A: Character `'c'` (Rank 0):
      - $cnt[\text{'c'}] = 1 \implies$ append `'c'` $\times 1$.
      - Output buffer: `["c"]`.
      - Clear: $cnt[\text{'c'}] \leftarrow 0$.
    - Step 2B: Character `'b'` (Rank 1):
      - $cnt[\text{'b'}] = 1 \implies$ append `'b'` $\times 1$.
      - Output buffer: `["c", "b"]`.
      - Clear: $cnt[\text{'b'}] \leftarrow 0$.
    - Step 2C: Character `'a'` (Rank 2):
      - $cnt[\text{'a'}] = 1 \implies$ append `'a'` $\times 1$.
      - Output buffer: `["c", "b", "a"]`.
      - Clear: $cnt[\text{'a'}] \leftarrow 0$.
  - **Phase 3: Emit Remaining Unranked Characters:**
    - Check remaining entries in $cnt$:
      - $cnt[\text{'d'}] = 1 \implies$ append `'d'`.
      - Output buffer: `["c", "b", "a", "d"]`.
  - **Phase 4: String Assembly:**
    $$
    ans = \text{"cbad"}
    $$
- **Partial Alphabet Order Trace ($order = \text{"bcafg"}, s = \text{"abcd"}$):**
  - Characters in $order$ present in $s$: `'b'`, `'c'`, `'a'`.
  - Emitted: `"b"` then `"c"` then `"a"` $\implies \text{"bca"}$.
  - Unranked: `'d'` appended $\implies \text{"bcad"}$.
  - Letters `'f'`, `'g'` in $order$ have count 0 in $s$, so they are skipped without error.
- **Multiple Duplicate Characters Trace ($order = \text{"ba"}, s = \text{"aababb"}$):**
  - Counts: $cnt[\text{'b'}] = 3, cnt[\text{'a'}] = 3$.
  - Emit all `'b'`s first, then all `'a'`s:
  - Output: `"bbbaaa"`.

This instance demonstrates total preorder linearization and finite-alphabet bucket sort, mathematically proves why partitioning characters into ordered and unordered equivalence fibers preserves partial order consistency, and derives $O(|order| + |s|)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a priority string $order$ and a string $s$:
Sort $s$ such that characters appearing in $order$ follow their relative order in $order$.
Unranked characters can appear anywhere.

```text
order = "cba"
s     = "abcd"

Order specifies: 'c' < 'b' < 'a'
Characters in s:
  'c' appears 1 time  -> "c"
  'b' appears 1 time  -> "cb"
  'a' appears 1 time  -> "cba"
  'd' (unranked)      -> "cbad"

Result: "cbad"
```

### The Invariant of the Bucket Count Sort
- Count frequencies of all characters in $s$.
- Traverse $order$: for each character, append it $cnt[c]$ times.
- Append any leftover characters not in $order$.
- Guarantees $O(|s| + |order|)$ execution time.

---

## 2. Conceptual Foundation & Invariants

### 1. Alphabet Ranking Homomorphism:
$$
\text{rank}: \Sigma \to \mathbb{N}, \quad \text{rank}(order[i]) = i
$$

### 2. Frequency Projection & Emission:
$$
\text{Reconstruct}(order, s) = \left( \prod_{c \in order} c^{cnt[c]} \right) \cdot \left( \prod_{c \notin order} c^{cnt[c]} \right)
$$

> **Preorder Linearization Invariant.** The string $order$ defines a linear extension of a partial order on the alphabet $\Sigma$. Bucket sorting along this linear extension satisfies the projection property $\pi_{order}(s') = order_{|\text{alph}(s)}$ in optimal $O(|\Sigma| + |s|)$ time.

---

## 3. Step-by-Step Worked Execution

We trace $order = \text{"cba"}, s = \text{"abcd"}$:

---

### Step 1: Count Frequencies in $s$
- $cnt[\text{'a'}] = 1, cnt[\text{'b'}] = 1, cnt[\text{'c'}] = 1, cnt[\text{'d'}] = 1$.

---

### Step 2: Emit Ranked
- Character `'c'` $\implies$ append `"c"`.
- Character `'b'` $\implies$ append `"b"`.
- Character `'a'` $\implies$ append `"a"`.
- Current: `"cba"`.

---

### Step 3: Emit Leftovers
- Character `'d'` $\implies$ append `"d"`.

---

### Step 4: Output
$$
\mathbf{\text{"cbad"}}
$$

---

## 4. Complete Execution Trace

| Step | Source Character | In $order$? | Frequency in $s$ | Emitted Fragment | Current String Buffer |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | `'c'` | Yes (Rank 0) | $1$ | `"c"` | `"c"` |
| $2$ | `'b'` | Yes (Rank 1) | $1$ | `"b"` | `"cb"` |
| $3$ | `'a'` | Yes (Rank 2) | $1$ | `"a"` | `"cba"` |
| **$4$** | **`'d'`** | **No (Leftover)** | **$1$** | **`"d"`** | **`"cbad"`** |

---

## 5. Boundary Cases & Failure Modes

- **$s$ Contains Only Unranked Characters ($order = \text{"xyz"}, s = \text{"abc"}$):** Preserves original or any valid grouping $\implies$ `"abc"`.
- **$order$ Contains Unused Characters:** Characters in $order$ with $cnt[c] = 0$ are skipped without writing.
- **Identical Repeated Characters ($s = \text{"aaaa"}$):** Emits `"aaaa"`.
- **Empty $order$:** All characters emitted as leftovers.

---

## 6. Traps & Common Anti-Patterns

- **General Comparison Sorting with Key Function ($O(N \log N)$):** Sorting with `key=lambda x: d.get(x, 0)` is valid in Python, but counting buckets in $O(N)$ avoids $O(N \log N)$ overhead and guarantees deterministic linear time.
- **Repeated String Concatenation (`s += c`):** Recreating strings in a loop in immutable string languages causes $O(N^2)$ quadratic copying. Use a list buffer `"".join(...)`.
- **Overwriting Counts:** Decrement or clear counts after emission to prevent duplicate emission in the leftover pass.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Frequency counting of $s$: $\mathcal{O}(|s|)$.
  - Iterating over $order$ of length $\le 26$: $\mathcal{O}(|order|)$.
  - Emitting leftover characters from alphabet ($\le 26$): $\mathcal{O}(|\Sigma|)$.
  - Total Time: strictly linear $\mathcal{O}(|s| + |order|)$ where $|s| \le 200$. Completes in $< 0.05$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(|\Sigma|) \le 26$ auxiliary space for frequency table.
