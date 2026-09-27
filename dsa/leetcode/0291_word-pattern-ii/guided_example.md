# Guided Example: Word Pattern II

We trace the step-by-step backtracking search over unknown substring boundaries, bidirectional mapping constraint enforcement (`char_to_word` and `seen_words`), suffix length pruning, and deterministic matching on representative string instances:

- **Input:** $\text{pattern} = \text{"abab"}, \quad s = \text{"redblueredblue"}$
- **Required output:** `true` (Valid bijection: $'a' \leftrightarrow \text{"red"}$ and $'b' \leftrightarrow \text{"blue"}$, expanding to $\text{"red"} + \text{"blue"} + \text{"red"} + \text{"blue"} == \text{"redblueredblue"}$)
- **Uniform Characters Instance:** $\text{pattern} = \text{"aaaa"}, \quad s = \text{"asdasdasdasd"} \implies \text{true}$ ($'a' \leftrightarrow \text{"asd"}$)
- **Non-Matching Structure:** $\text{pattern} = \text{"aabb"}, \quad s = \text{"xyzabcxzyabc"} \implies \text{false}$ (No partition yields a valid bijection)
- **Minimum Length Violation:** $\text{len}(s) < \text{len}(\text{pattern}) \implies \text{false}$ (Each pattern character requires at least 1 character in $s$)

This instance demonstrates backtracking over variable-length token partitions, proves why already-mapped characters must be matched deterministically rather than branching ($O(1)$ branch pruning), explains how a `seen_words` set prevents non-injective many-to-one collisions, and details remaining-length suffix bounding.

---

## 1. Instance & Teaching Goal

Given pattern $\text{pattern} = \text{"abab"}$ and continuous string $s = \text{"redblueredblue"}$:
Unlike Word Pattern I, **there are no whitespace delimiters** between words.
We must discover whether there exists a partition of $s$ into non-empty substrings that forms a valid bijection with $\text{pattern}$:

```text
Pattern:    a      b      a      b
String:   [red] [blue] [red] [blue]
           ---   ----   ---   ----
Substrings match pattern structure:
'a' <-> "red"
'b' <-> "blue"
Bijection valid -> True
```

### The Search Space & Branch Pruning
A naive brute-force partition tests all $\binom{N-1}{P-1}$ possible substring segmentations.
We prune this exponential tree drastically:
1. **Deterministic Suffix Verification:** Once a character $c$ is assigned to substring $w$, subsequent occurrences of $c$ do **not** branch; they must match $w$ at the current index of $s$ using `s.startswith(w, s_idx)`.
2. **Injectivity Filtering:** A new candidate substring cannot be chosen if it is already assigned to another character (`cand not in seen_words`).
3. **Remaining Length Bounding:** If remaining characters in $s$ is strictly less than remaining characters in `pattern` ($\text{len}(s) - s\_idx < \text{len}(pattern) - p\_idx$), prune immediately.

---

## 2. Conceptual Foundation & Invariants

### Recursive Backtracking State `dfs(p_idx, s_idx)`
- $p\_idx$: Current pointer in `pattern` ($0 \le p\_idx \le M$).
- $s\_idx$: Current pointer in $s$ ($0 \le s\_idx \le N$).
- `char_to_word`: Dictionary mapping pattern character $c \to \text{str}$.
- `seen_words`: Set of all substrings currently bound to any character.

### Execution Protocol:
1. **Base Case:**
   - If $p\_idx == M$ and $s\_idx == N$: Return `True` (Both strings completely consumed).
   - If $p\_idx == M$ or $s\_idx == N$: Return `False` (One string ended prematurely).
   - If $N - s\_idx < M - p\_idx$: Return `False` (Not enough characters left for remaining pattern symbols).

2. **Case 1: $c = \text{pattern}[p\_idx]$ is Already Bound:**
   Let $w = \text{char\_to\_word}[c]$.
   Check if $s$ starting at $s\_idx$ matches $w$:
   - If $s[s\_idx : s\_idx + \text{len}(w)] \ne w$: Return `False` (Mismatch!).
   - If it matches: Recurse deterministically:
     $$
     \text{return dfs}(p\_idx + 1, \; s\_idx + \text{len}(w))
     $$

3. **Case 2: $c = \text{pattern}[p\_idx]$ is NOT Yet Bound:**
   Explore all non-empty candidate substrings $w = s[s\_idx : k]$ for $k \in [s\_idx + 1, N - (M - p\_idx - 1)]$:
   - If $w \in \text{seen\_words}$: Skip (Injectivity violation).
   - Bind:
     $$
     \text{char\_to\_word}[c] = w, \quad \text{seen\_words.add}(w)
     $$
   - Recurse: If `dfs(p_idx + 1, k) == True`, return `True`.
   - Backtrack (Unbind):
     $$
     \text{del char\_to\_word}[c], \quad \text{seen\_words.remove}(w)
     $$
   Return `False` if no choice succeeds.

> **Invariant.** At any point in the recursion, `char_to_word` and `seen_words` maintain a strict bijection between consumed pattern prefix characters and their allocated substrings.

---

## 3. Step-by-Step Worked Execution

We trace the backtracking on $\text{pattern} = \text{"abab"}$ ($M = 4$) and $s = \text{"redblueredblue"}$ ($N = 14$):

---

### Step 1: Root State ($p\_idx = 0, \; s\_idx = 0, \; c = \text{'a'}$)
`'a'` is unbound. Try candidate substrings starting at index 0:

- **Candidate 1: $w = \text{"r"}$ ($k = 1$):**
  Bind $'a' \to \text{"r"}$.
  - Next state: $p\_idx = 1, s\_idx = 1, c = \text{'b'}$.
  - Try $w = \text{"e"}$ ($'b' \to \text{"e"}$).
  - Next state: $p\_idx = 2, s\_idx = 2, c = \text{'a'}$.
  - $'a'$ is bound to `"r"`. Does $s[2:]$ (`"dblueredblue"`) start with `"r"`? **No!**
  - Branch fails and backtracks.
- **Candidate 2: $w = \text{"re"}$ ($k = 2$):**
  Bind $'a' \to \text{"re"}$.
  - Later, when $c = \text{'a'}$ is checked again at index 2, $s$ does not match `"re"`. Backtracks.
- **Candidate 3: $w = \text{"red"}$ ($k = 3$):**
  Bind $'a' \to \text{"red"}$. Add `"red"` to `seen_words`. Proceed to $p\_idx = 1, s\_idx = 3$.

---

### Step 2: Second Position ($p\_idx = 1, \; s\_idx = 3, \; c = \text{'b'}$)
`'b'` is unbound. Suffix of $s$ from index 3 is `"blueredblue"`.
Try candidate substrings starting at index 3:

- **Candidate 1: $w = \text{"b"}$:** Fails later at $p\_idx = 3$.
- **Candidate 2: $w = \text{"bl"}$:** Fails later.
- **Candidate 3: $w = \text{"blu"}$:** Fails later.
- **Candidate 4: $w = \text{"blue"}$ ($k = 7$):**
  Check $\text{"blue"} \notin \text{seen\_words}$ (**True**; `seen_words = {"red"}`).
  Bind $'b' \to \text{"blue"}$. Add `"blue"` to `seen_words`.
  Proceed to $p\_idx = 2, s\_idx = 7$.

---

### Step 3: Third Position ($p\_idx = 2, \; s\_idx = 7, \; c = \text{'a'}$)
`'a'` is **already bound** to `"red"`.
- Required substring: `"red"`. Length $= 3$.
- Suffix of $s$ from index 7 is `"redblue"`.
- Does $s[7:10]$ equal `"red"`?
  $$
  s[7:10] == \text{"red"} \quad (\mathbf{\text{True!}})
  $$
- Deterministic advance! No branching needed.
- Advance: $p\_idx \leftarrow 2 + 1 = 3, \quad s\_idx \leftarrow 7 + 3 = 10$.

---

### Step 4: Fourth Position ($p\_idx = 3, \; s\_idx = 10, \; c = \text{'b'}$)
`'b'` is **already bound** to `"blue"`.
- Required substring: `"blue"`. Length $= 4$.
- Suffix of $s$ from index 10 is `"blue"`.
- Does $s[10:14]$ equal `"blue"`?
  $$
  s[10:14] == \text{"blue"} \quad (\mathbf{\text{True!}})
  $$
- Advance: $p\_idx \leftarrow 3 + 1 = 4, \quad s\_idx \leftarrow 10 + 4 = 14$.

---

### Step 5: Base Case Reached ($p\_idx = 4, \; s\_idx = 14$)
- $p\_idx == M$ ($4 == 4$).
- $s\_idx == N$ ($14 == 14$).
- Both strings completely and accurately consumed!
- **Return `true`**.

---

## 4. Complete Execution Trace

```text
pattern = "abab", s = "redblueredblue"

dfs(p=0, s=0, c='a'):
  Try 'a' -> "r":
    dfs(p=1, s=1, c='b'): try 'b' -> "e":
      dfs(p=2, s=2, c='a'): 'a' is "r", but s[2:] is "db..." -> Mismatch!
  Try 'a' -> "re":
    dfs(p=1, s=2, c='b'): ... -> Mismatch!
  Try 'a' -> "red":
    dfs(p=1, s=3, c='b'):
      Try 'b' -> "blue":
        dfs(p=2, s=7, c='a'): 'a' is "red", s[7:10] == "red" -> Matches!
          dfs(p=3, s=10, c='b'): 'b' is "blue", s[10:14] == "blue" -> Matches!
            dfs(p=4, s=14): p == 4 and s == 14 -> SUCCESS!

Result: true
```

| Recursion Step | $p\_idx$ | Char $c$ | Current State of $c$ | Action Taken / Substring Tested | Target Slice Checked | Result / Next State |
|:---:|:---:|:---:|:---:|:---|:---:|:---|
| 1 | 0 | `'a'` | Unbound | Try candidate `"r"` | - | Downstream Mismatch |
| 2 | 0 | `'a'` | Unbound | Try candidate `"re"` | - | Downstream Mismatch |
| **3** | **0** | **`'a'`** | **Unbound** | **Bind `'a' \to \text{"red"}`** | $s[0:3]$ | **Advances to $p=1, s=3$** |
| 4 | 1 | `'b'` | Unbound | Try `"b"`, `"bl"`, `"blu"` | - | Downstream Mismatches |
| **5** | **1** | **`'b'`** | **Unbound** | **Bind `'b' \to \text{"blue"}`** | $s[3:7]$ | **Advances to $p=2, s=7$** |
| **6** | **2** | **`'a'`** | **Bound to `"red"`** | **Deterministic Match** | $s[7:10] == \text{"red"}$ | **Advances to $p=3, s=10$** |
| **7** | **3** | **`'b'`** | **Bound to `"blue"`** | **Deterministic Match** | $s[10:14] == \text{"blue"}$ | **Advances to $p=4, s=14$** |
| **8** | **4** | - | - | **Base Case Verification** | $p == 4, s == 14$ | **`true` (Complete Match)** |

---

## 5. Algorithmic Correctness

**Soundness.** Every accepted assignment binds each distinct pattern character to a non-empty substring. The `seen_words` set guarantees injectivity (no two characters share the same substring), while the single-value dictionary guarantees functionality (no character maps to two different substrings). Both strings are consumed in their entirety, ensuring a mathematically exact bijection.

**Completeness.** For any unbound pattern character, backtracking systematically tries all possible prefix lengths $k$. If a valid bijection exists, at least one branch of the search tree will encounter the correct boundary splits and return `True`.

---

## 6. Traps This Instance Exposes

- **Branching on Already Bound Characters:** When $c$ is already in `char_to_word`, trying different substring lengths for $c$ is redundant and destroys runtime efficiency. A character with an established binding must be matched deterministically using `s.startswith`.
- **Omitting the Injectivity Set (`seen_words`):** If only `char_to_word` is used, $\text{pattern} = \text{"ab"}$ and $s = \text{"redred"}$ would bind `'a' \to \text{"red"}` and `'b' \to \text{"red"}` and falsely report `True`. Enforcing `cand not in seen_words` prevents non-injective bindings.
- **Suffix Length Underflow:** If $\text{len}(s) - s\_idx < \text{len}(pattern) - p\_idx$, it is impossible to complete the match because every remaining pattern character needs at least 1 character in $s$. Pruning immediately avoids futile deep branches.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot 2^N)$ in the worst case, where $N = \text{len}(s)$. Partitioning $s$ across $N - 1$ possible cut points corresponds to $2^{N-1}$ partitions. However, deterministic matching of repeated characters, injectivity filtering, and suffix length checks prune the practical search space to a fraction of the theoretical worst case.
- **Auxiliary Space Complexity:** $O(M + N)$, where $M = \text{len}(\text{pattern})$ and $N = \text{len}(s)$. The recursion stack depth is at most $M$, and the dictionary and set store at most $\min(M, 26)$ substrings.
