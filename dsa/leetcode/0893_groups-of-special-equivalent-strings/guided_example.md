# Guided Example: Groups of Special-Equivalent Strings

We trace the step-by-step index parity decomposition (even vs odd coordinates), symmetric group permutation orbits, canonical character multisets, signature hashing, and equivalence class counting on representative word sets:

- **Input:**
  $$
  words = [\text{"abcd"}, \text{"cdab"}, \text{"cbad"}, \text{"xyzz"}, \text{"zzxy"}, \text{"zzyx"}]
  $$
- **Required output:** `3`
  - Special-equivalent move rules:
    - A move consists of choosing two indices $i$ and $j$ of the **same parity** ($i \equiv j \pmod 2$) and swapping $word[i]$ and $word[j]$.
    - Two strings $S$ and $T$ are **special-equivalent** if $S$ can be converted to $T$ through any sequence of valid swaps.
    - A group is an equivalence class of strings under this relation.
    - Objective: Return the number of distinct groups of special-equivalent strings.
    - For $words = [\text{"abcd"}, \text{"cdab"}, \text{"cbad"}, \text{"xyzz"}, \text{"zzxy"}, \text{"zzyx"}]$:
      - Group 1: $\{\text{"abcd"}, \text{"cdab"}, \text{"cbad"}\}$
        - In `"abcd"`, even indices $\{0, 2\}$ hold $\{a, c\}$; odd indices $\{1, 3\}$ hold $\{b, d\}$.
        - In `"cdab"`, even indices hold $\{c, a\}$; odd indices hold $\{d, b\}$.
        - In `"cbad"`, even indices hold $\{c, a\}$; odd indices hold $\{b, d\}$.
        - All share sorted even letters `"ac"` and sorted odd letters `"bd"`.
      - Group 2: $\{\text{"xyzz"}, \text{"zzxy"}\}$
        - In `"xyzz"`, even indices hold $\{x, z\}$; odd indices hold $\{y, z\}$.
        - In `"zzxy"`, even indices hold $\{z, x\}$; odd indices hold $\{z, y\}$.
        - Both share sorted even `"xz"` and sorted odd `"yz"`.
      - Group 3: $\{\text{"zzyx"}\}$
        - Even indices hold $\{z, y\}$; odd indices hold $\{z, x\}$.
        - Sorted even `"yz"` and sorted odd `"xz"`.
      - Total distinct groups: **`3`**.
- **The Parity Decomposition & Canonical Orbit Invariant:**
  - **The Parity Separation Theorem:**
    - Any swap is restricted to indices of identical parity ($0 \leftrightarrow 2, 1 \leftrightarrow 3, \dots$).
    - Characters at even positions can **never migrate to odd positions**, and characters at odd positions can **never migrate to even positions**.
    - Furthermore, within any set of indices of the same parity, any sequence of swaps can generate **every possible permutation** of those characters (the symmetric group $\mathcal{S}_k$).
    - Therefore, two strings are special-equivalent **if and only if**:
      1. Their multiset of characters at even indices is identical.
      2. Their multiset of characters at odd indices is identical.
  - **Canonical Normal Form:**
    - For any word $w$, extract:
      $$
      \text{even}(w) = \text{sorted}(w[0], w[2], w[4], \dots)
      $$
      $$
      \text{odd}(w) = \text{sorted}(w[1], w[3], w[5], \dots)
      $$
    - The composite tuple $\text{signature}(w) = (\text{even}(w), \text{odd}(w))$ acts as a **unique canonical identifier** for the entire equivalence class.
    - The number of special-equivalent groups is simply the number of **unique signatures** stored in a hash set:
      $$
      \text{Groups} = |\text{set}(\text{signatures})|
      $$

---

## 1. Instance & Teaching Goal

Given 6 words of length 4, project each word into its even/odd multiset signature to count unique classes.

```text
Words Analysis:
  "abcd":
    Even indices (0, 2): 'a', 'c' -> sorted: "ac"
    Odd  indices (1, 3): 'b', 'd' -> sorted: "bd"
    Signature: "ac_bd"

  "cdab":
    Even: 'c', 'a' -> "ac"
    Odd:  'd', 'b' -> "bd"
    Signature: "ac_bd"  (Group 1)

  "cbad":
    Even: 'c', 'a' -> "ac"
    Odd:  'b', 'd' -> "bd"
    Signature: "ac_bd"  (Group 1)

  "xyzz":
    Even: 'x', 'z' -> "xz"
    Odd:  'y', 'z' -> "yz"
    Signature: "xz_yz"  (Group 2)

  "zzxy":
    Even: 'z', 'x' -> "xz"
    Odd:  'z', 'y' -> "yz"
    Signature: "xz_yz"  (Group 2)

  "zzyx":
    Even: 'z', 'y' -> "yz"
    Odd:  'z', 'x' -> "xz"
    Signature: "yz_xz"  (Group 3)

Distinct Signatures: {"ac_bd", "xz_yz", "yz_xz"}
Total Groups = 3
```

The teaching goal is to justify why parity-constrained swapping collapses the graph of words into independent multiset equality checks.

---

## 2. Conceptual Foundation & Invariants

### 1. Parity Slices:
For string $w$ of length $L$:
$$
w_{\text{even}} = [w[2k] \mid 0 \le 2k < L]
$$
$$
w_{\text{odd}} = [w[2k+1] \mid 0 \le 2k+1 < L]
$$

### 2. Canonical Orbit Function:
$$
\Phi(w) = \text{sort}(w_{\text{even}}) \;\|\; \text{sort}(w_{\text{odd}})
$$
$$
w_1 \sim w_2 \iff \Phi(w_1) = \Phi(w_2)
$$

---

## 3. Step-by-Step Worked Execution

We trace $words = [\text{"abcd"}, \text{"cdab"}, \text{"cbad"}, \text{"xyzz"}, \text{"zzxy"}, \text{"zzyx"}]$:
Initialize hash set $S = \emptyset$.

---

### Step 1: Word `"abcd"`
- Even characters: $w[0] = \text{'a'}, w[2] = \text{'c'}$. Sorted: `"ac"`.
- Odd characters: $w[1] = \text{'b'}, w[3] = \text{'d'}$. Sorted: `"bd"`.
- Combined signature: `"acbd"`.
- Insert into set: $S = \{\text{"acbd"}\}$.

---

### Step 2: Word `"cdab"`
- Even characters: $w[0] = \text{'c'}, w[2] = \text{'a'}$. Sorted: `"ac"`.
- Odd characters: $w[1] = \text{'d'}, w[3] = \text{'b'}$. Sorted: `"bd"`.
- Combined signature: `"acbd"`.
- Already present in $S$. Set size remains $1$.

---

### Step 3: Word `"cbad"`
- Even characters: $w[0] = \text{'c'}, w[2] = \text{'a'}$. Sorted: `"ac"`.
- Odd characters: $w[1] = \text{'b'}, w[3] = \text{'d'}$. Sorted: `"bd"`.
- Combined signature: `"acbd"`.
- Already present in $S$. Set size remains $1$.

---

### Step 4: Word `"xyzz"`
- Even characters: $w[0] = \text{'x'}, w[2] = \text{'z'}$. Sorted: `"xz"`.
- Odd characters: $w[1] = \text{'y'}, w[3] = \text{'z'}$. Sorted: `"yz"`.
- Combined signature: `"xzyz"`.
- Insert into set: $S = \{\text{"acbd"}, \text{"xzyz"}\}$. Set size $= 2$.

---

### Step 5: Word `"zzxy"`
- Even characters: $w[0] = \text{'z'}, w[2] = \text{'x'}$. Sorted: `"xz"`.
- Odd characters: $w[1] = \text{'z'}, w[3] = \text{'y'}$. Sorted: `"yz"`.
- Combined signature: `"xzyz"`.
- Already present in $S$. Set size remains $2$.

---

### Step 6: Word `"zzyx"`
- Even characters: $w[0] = \text{'z'}, w[2] = \text{'y'}$. Sorted: `"yz"`.
- Odd characters: $w[1] = \text{'z'}, w[3] = \text{'x'}$. Sorted: `"xz"`.
- Combined signature: `"yzxz"`.
- Insert into set: $S = \{\text{"acbd"}, \text{"xzyz"}, \text{"yzxz"}\}$. Set size $= 3$.

---

### Termination:
All words evaluated.
- **Unique group count:** $|S| = \mathbf{3}$.

---

## 4. Complete Execution Trace

| Word | Raw Even Characters | Sorted Even | Raw Odd Characters | Sorted Odd | Canonical Signature | Discovered in Set? | Equivalence Group |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `"abcd"` | `['a', 'c']` | `"ac"` | `['b', 'd']` | `"bd"` | `"acbd"` | New | Group 1 |
| `"cdab"` | `['c', 'a']` | `"ac"` | `['d', 'b']` | `"bd"` | `"acbd"` | Duplicate | Group 1 |
| `"cbad"` | `['c', 'a']` | `"ac"` | `['b', 'd']` | `"bd"` | `"acbd"` | Duplicate | Group 1 |
| `"xyzz"` | `['x', 'z']` | `"xz"` | `['y', 'z']` | `"yz"` | `"xzyz"` | New | Group 2 |
| `"zzxy"` | `['z', 'x']` | `"xz"` | `['z', 'y']` | `"yz"` | `"xzyz"` | Duplicate | Group 2 |
| **`"zzyx"`** | **`['z', 'y']`** | **`"yz"`** | **`['z', 'x']`** | **`"xz"`** | **`"yzxz"`** | **New** | **`Group 3`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Word in Array:** Signature is added once $\implies$ returns $1$.
- **Odd Length Strings (e.g. length 3: `"abc"`):**
  - Even characters (indices 0, 2): length 2 (`"ac"`).
  - Odd characters (index 1): length 1 (`"b"`).
  - Parity slices handle uneven lengths naturally.
- **All Words Identical:** All share the same signature $\implies$ returns $1$.

---

## 6. Traps & Common Anti-Patterns

- **Sorting the Entire String:** Sorting the full string ignores parity constraints. For example, `"xyzz"` and `"zzyx"` both sort to `"xyzz"`, but they belong to different groups because `'y'` is at an odd index in `"xyzz"` and an even index in `"zzyx"`.
- **Graph BFS/DFS Over Pairs:** Trying to find connected components by testing pairs with BFS/DFS takes $\mathcal{O}(N^2 \cdot L)$ time; canonical signatures reduce clustering to $\mathcal{O}(N \cdot L \log L)$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $N$ be the number of words, and $L$ be the length of each word.
  - For each word, extracting and sorting even/odd characters takes $\mathcal{O}(L \log L)$ time.
  - Inserting into hash set takes $\mathcal{O}(L)$ time.
  - Total Time: strictly $\mathcal{O}(N \cdot L \log L)$. For $N \le 1000, L \le 20$, executes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - Hash set storing $N$ signatures: $\mathcal{O}(N \cdot L)$ space.
