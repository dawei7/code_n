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

The split `"red"` / `"blue"` is a witness, not the unique answer: $s$ is the square of `"redblue"`, so cutting that half into a non-empty `'a'` part and a non-empty `'b'` part anywhere produces another valid bijection. Section 3 follows the search to whichever witness it reaches first, and section 4 lists all six.

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
`'a'` is unbound, so the loop enumerates candidate substrings starting at index 0 in increasing length. The remaining-length rule caps that length at
$$
k_{\max} = (N - s\_idx) - (M - p\_idx - 1) = 14 - 3 = 11,
$$
because the three later pattern characters still need at least one character each.

- **Candidate 1: $w = \text{"r"}$ (length 1):**
  Bind $'a' \to \text{"r"}$ and descend to $p\_idx = 1, s\_idx = 1$, where `'b'` is unbound.
  Inside this candidate the sweep over `'b'` first tries lengths 1 through 5. Each of those placements puts the later deterministic re-check of `'a'` on an index holding `d`, `b`, `l`, `u` or `e` rather than the `r` at index 7, so all five die. The length-6 candidate `"edblue"` puts that re-check exactly on index 7 and survives, and the search returns `true` from this first candidate without ever generating `"re"` or `"red"`.
- **Candidates 2 and 3 and beyond:** never reached. The search reports the first witness it completes, so the candidate sweep stops here.

---

### Step 2: The Candidate Sweep for `'b'` ($p\_idx = 1, \; s\_idx = 1$)
`'b'` is unbound while `'a'` already holds `"r"`, so each candidate substring of length $L$ is followed by a deterministic re-check of `'a'` at index $1 + L$:

| Candidate $w$ for `'b'` | Slice taken | Length | Re-check of `'a' = "r"` lands at | Character found there | Outcome |
|:---|:---|:---:|:---:|:---:|:---|
| `"e"` | $s[1:2]$ | 1 | index 2 | `d` | Dies: `'a'` requires `r` and cannot branch |
| `"ed"` | $s[1:3]$ | 2 | index 3 | `b` | Dies |
| `"edb"` | $s[1:4]$ | 3 | index 4 | `l` | Dies |
| `"edbl"` | $s[1:5]$ | 4 | index 5 | `u` | Dies |
| `"edblu"` | $s[1:6]$ | 5 | index 6 | `e` | Dies |
| **`"edblue"`** | $s[1:7]$ | 6 | index 7 | `r` | **Survives:** `"edblue" \notin \text{seen\_words}`, so it binds and advances to $p\_idx = 2, s\_idx = 7$ |

Every rejected row costs one binding, one failed re-check and one unbinding; none of them can be skipped by reasoning ahead, because `'a'`'s next occurrence has not been located yet.

---

### Step 3: Third Position ($p\_idx = 2, \; s\_idx = 7, \; c = \text{'a'}$)
`'a'` is **already bound** to `"r"`, so there is no branching: the substring length is fixed at 1 and the only question is whether $s$ has `r` at the current index.
- Does $s[7:8]$ equal `"r"`?
  $$
  s[7:8] == \text{"r"} \quad (\mathbf{\text{True!}})
  $$
- Deterministic advance: $p\_idx \leftarrow 2 + 1 = 3, \quad s\_idx \leftarrow 7 + 1 = 8$.

---

### Step 4: Fourth Position ($p\_idx = 3, \; s\_idx = 8, \; c = \text{'b'}$)
`'b'` is **already bound** to `"edblue"`. Its length is 6, so the search compares exactly six characters.
- Suffix of $s$ from index 8 is `"edblue"`.
- Does $s[8:14]$ equal `"edblue"`?
  $$
  s[8:14] == \text{"edblue"} \quad (\mathbf{\text{True!}})
  $$
- Advance: $p\_idx \leftarrow 3 + 1 = 4, \quad s\_idx \leftarrow 8 + 6 = 14$.

---

### Step 5: Base Case Reached ($p\_idx = 4, \; s\_idx = 14$)
- $p\_idx == M$ ($4 == 4$).
- $s\_idx == N$ ($14 == 14$).
- Both strings completely and accurately consumed!
- **Return `true`**, with the witness $'a' \leftrightarrow \text{"r"}$ and $'b' \leftrightarrow \text{"edblue"}$, which expands to $\text{"r"} + \text{"edblue"} + \text{"r"} + \text{"edblue"} = \text{"redblueredblue"}$.

---

## 4. Complete Execution Trace

```text
pattern = "abab", s = "redblueredblue"

dfs(p=0, s=0, c='a'): 'a' unbound, candidate lengths 1..11
  Candidate 'a' -> "r" (length 1):
    dfs(p=1, s=1, c='b'): 'b' unbound, candidate lengths 1..11
      'b' -> "e":      dfs(p=2, s=2, c='a'): 'a' is "r", s[2] is 'd' -> dead, unbind
      'b' -> "ed":     'a' re-check at index 3 sees 'b'  -> dead, unbind
      'b' -> "edb":    'a' re-check at index 4 sees 'l'  -> dead, unbind
      'b' -> "edbl":   'a' re-check at index 5 sees 'u'  -> dead, unbind
      'b' -> "edblu":  'a' re-check at index 6 sees 'e'  -> dead, unbind
      'b' -> "edblue": dfs(p=2, s=7, c='a'): 'a' is "r", s[7:8] == "r" -> matches
        dfs(p=3, s=8, c='b'): 'b' is "edblue", s[8:14] == "edblue" -> matches
          dfs(p=4, s=14): both strings consumed -> SUCCESS!

Result: true
Witness found first: 'a' <-> "r", 'b' <-> "edblue"
```

| Recursion Step | $p\_idx$ | $s\_idx$ | Char $c$ | Current State of $c$ | Action Taken / Substring Tested | Target Slice Checked | Result / Next State |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|:---|
| 1 | 0 | 0 | `'a'` | Unbound | Enumerate candidates, length capped at 11 | - | Candidate `"r"` taken, $k = 1$ |
| 2 | 1 | 1 | `'b'` | Unbound | Candidate `"e"` | `'a'` re-check at index 2 | Downstream mismatch, unbound |
| 3 | 1 | 1 | `'b'` | Unbound | Candidates `"ed"`, `"edb"`, `"edbl"`, `"edblu"` | `'a'` re-check at indices 3, 4, 5, 6 | All mismatch, unbound |
| **4** | **1** | **1** | **`'b'`** | **Unbound** | **Bind `'b' \to \text{"edblue"}`** | $s[1:7]$ | **Advances to $p=2, s=7$** |
| **5** | **2** | **7** | **`'a'`** | **Bound to `"r"`** | **Deterministic Match** | $s[7:8] == \text{"r"}$ | **Advances to $p=3, s=8$** |
| **6** | **3** | **8** | **`'b'`** | **Bound to `"edblue"`** | **Deterministic Match** | $s[8:14] == \text{"edblue"}$ | **Advances to $p=4, s=14$** |
| **7** | **4** | **14** | - | - | **Base Case Verification** | $p == 4, s == 14$ | **`true` (Complete Match)** |

---

### Why the Witness Is Not Unique

The search returned $'a' \leftrightarrow \text{"r"}$, but the string is the square of $W = \text{"redblue"}$, and every way of cutting $W$ into a non-empty `'a'` part and a non-empty `'b'` part satisfies the pattern:

| Cut of $W = \text{"redblue"}$ | `'a'` | `'b'` | Expansion | Valid witness? |
|:---|:---|:---|:---|:---|
| after 1 character | `"r"` | `"edblue"` | `"r" + "edblue" + "r" + "edblue"` | Yes — the one this search returns |
| after 2 characters | `"re"` | `"dblue"` | `"re" + "dblue" + "re" + "dblue"` | Yes — never generated here |
| after 3 characters | `"red"` | `"blue"` | `"red" + "blue" + "red" + "blue"` | Yes — the witness named in the statement's explanation |
| after 4 characters | `"redb"` | `"lue"` | `"redb" + "lue" + "redb" + "lue"` | Yes — never generated here |
| after 5 characters | `"redbl"` | `"ue"` | `"redbl" + "ue" + "redbl" + "ue"` | Yes — never generated here |
| after 6 characters | `"redblu"` | `"e"` | `"redblu" + "e" + "redblu" + "e"` | Yes — never generated here |

Since $a + b + a + b = (a + b)^2$ whenever $s = abab$, the two halves of $s$ must be equal, so the half is always $\text{"redblue"}$ and the only freedom is where to cut it. Every cut yields two substrings of different lengths, so $'a'$ and $'b'$ never collide and the mapping is injective; the question posed is existence, not uniqueness, so returning the first witness is enough.

---

## 5. Algorithmic Correctness

**Soundness.** Every accepted assignment binds each distinct pattern character to a non-empty substring. The `seen_words` set guarantees injectivity (no two characters share the same substring), while the single-value dictionary guarantees functionality (no character maps to two different substrings). Both strings are consumed in their entirety, ensuring a mathematically exact bijection.

**Completeness.** For any unbound pattern character, backtracking systematically tries all possible prefix lengths $k$. If a valid bijection exists, at least one branch of the search tree will encounter the correct boundary splits and return `True`.

---

## 6. Traps This Instance Exposes

- **Branching on Already Bound Characters:** When $c$ is already in `char_to_word`, trying different substring lengths for $c$ is redundant and destroys runtime efficiency. A character with an established binding must be matched deterministically using `s.startswith`.
- **Omitting the Injectivity Set (`seen_words`):** If only `char_to_word` is used, $\text{pattern} = \text{"ab"}$ and $s = \text{"aa"}$ has exactly one partition into two non-empty pieces, `'a' \to \text{"a"}` and `'b' \to \text{"a"}`, and a version without the set would accept it. The two characters would share one substring, so the relation is not injective; enforcing `cand not in seen_words` rejects that single candidate and correctly returns `false`. Note that $s = \text{"redred"}$ is *not* an instance of this trap: it matches `"ab"` genuinely, through `'a' \to \text{"r"}` and `'b' \to \text{"edred"}`.
- **Suffix Length Underflow:** If $\text{len}(s) - s\_idx < \text{len}(pattern) - p\_idx$, it is impossible to complete the match because every remaining pattern character needs at least 1 character in $s$. Pruning immediately avoids futile deep branches.

The boundaries below are the ones the search must survive, and each is decided by one of the three pruning rules rather than by a special case:

| Boundary | Instance | Which rule decides it | Result | Why |
|:---|:---|:---|:---:|:---|
| Pattern of a single character | `"a"` with `"red"` | Lengths 1, 2 and 3 are all inside the bound, and only length 3 reaches the base case | `true` | One symbol can absorb the whole string, so the first two candidates die on the base-case test rather than on a mismatch |
| Fewer characters in $s$ than symbols in the pattern | `"abc"` with `"ab"` | Remaining-length rule fires at the root: $2 < 3$ | `false` | Three non-empty substrings cannot fit inside two characters; the test is necessary but not sufficient on its own |
| Exactly one partition, and it is not injective | `"ab"` with `"aa"` | Injectivity filter: the only candidate `"a"` is already in `seen_words` when `'b'` is considered | `false` | A functional partition exists, but both characters would claim one substring |
| A repeated single symbol | `"aaaa"` with `"asdasdasdasd"` | Deterministic re-check at every position after the first | `true` | $\lvert s \rvert = 12 = 4 \times 3$, so $s$ is the fourth power of the bound substring `"asd"` |
| A structurally impossible pattern | `"aabb"` with `"xyzabcxzyabc"` | Exhaustive candidate sweep: every choice for `'a'` fails, because $a + a$ would have to be a square and no even-length prefix of $s$ is one | `false` | The pattern forces $s = a\,a\,b\,b$, so $s$ must begin with a square of even total length |
| A string with many valid witnesses | `"abab"` with `"redblueredblue"` | The first candidate completes, so the sweep never advances | `true` | The question is existence, so stopping at the first witness is sound even though six witnesses exist |
| One symbol over a long string | `"a"` with `"aaaaaa"` | The bound allows the whole remaining length and the base case accepts it | `true` | A single unbound symbol may take any positive length up to the remaining characters |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot 2^N)$ in the worst case, where $N = \text{len}(s)$. Partitioning $s$ across $N - 1$ possible cut points corresponds to $2^{N-1}$ partitions. However, deterministic matching of repeated characters, injectivity filtering, and suffix length checks prune the practical search space to a fraction of the theoretical worst case.
- **Auxiliary Space Complexity:** $O(M + N)$, where $M = \text{len}(\text{pattern})$ and $N = \text{len}(s)$. The recursion stack depth is at most $M$, and the dictionary and set store at most $\min(M, 26)$ substrings.
