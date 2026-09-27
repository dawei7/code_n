# Guided Example: Word Pattern

We trace the step-by-step bidirectional hash mapping, character-to-word bijection verification ($c \leftrightarrow w$), cardinality pre-check ($\text{len}(p) == \text{len}(ws)$), and injectivity enforcement on representative pattern matching instances:

- **Input:** $\text{pattern} = \text{"abba"}, \quad s = \text{"dog cat cat dog"}$
- **Required output:** `true` (Valid bijection: $'a' \leftrightarrow \text{"dog"}$ and $'b' \leftrightarrow \text{"cat"}$)
- **Forward Inconsistency:** $\text{pattern} = \text{"abba"}, \quad s = \text{"dog cat cat fish"} \implies \text{false}$ (Character $'a'$ maps to both `"dog"` and `"fish"`)
- **Reverse Inconsistency (Non-Injective):** $\text{pattern} = \text{"abba"}, \quad s = \text{"dog dog dog dog"} \implies \text{false}$ (Both $'a'$ and $'b'$ attempt to claim `"dog"`)
- **Cardinality Mismatch:** $\text{pattern} = \text{"aaa"}, \quad s = \text{"aa aa aa aa"} \implies \text{false}$ (Pattern length $3 \ne$ word count $4$)

This instance demonstrates bidirectional dictionary synchronization, explains why a single one-directional map fails to detect many-to-one collisions, formalizes the bijection definition between discrete alphabet characters and whitespace-delimited words, and operates in strictly $O(N + M)$ linear time and space.

---

## 1. Instance & Teaching Goal

Given a pattern string $\text{pattern} = \text{"abba"}$ and space-separated sentence $s = \text{"dog cat cat dog"}$:
Determine whether $s$ follows the pattern via a mathematical **bijection** (a one-to-one and onto mapping) between pattern characters and words:
```text
Pattern:  a     b     b     a
Words:   dog   cat   cat   dog
          |     |     |     |
Map:    a<->dog b<->cat b<->cat a<->dog
All pairings consistent in both directions -> True
```

### The Pitfall of One-Way Mapping
Consider $\text{pattern} = \text{"abba"}$ with $s = \text{"dog dog dog dog"}$:
- Forward map $c \to w$:
  - Index 0: $'a' \to \text{"dog"}$
  - Index 1: $'b' \to \text{"dog"}$
  - Index 2: $'b' \to \text{"dog"}$
  - Index 3: $'a' \to \text{"dog"}$
If only a single forward map is checked, every character maps consistently to its recorded word!
However, this is **not a bijection**: both $'a'$ and $'b'$ map to `"dog"` (violating injectivity).
To guarantee a true bijection, we must enforce consistency in **both directions simultaneously**:
1. Forward: Each character $c$ maps to exactly one word $w$.
2. Reverse: Each word $w$ maps to exactly one character $c$.

---

## 2. Conceptual Foundation & Invariants

### Algorithmic Execution Protocol
1. **Tokenization & Cardinality Check:**
   Split string $s$ by whitespace into word list $W = [w_0, w_1, \dots, w_{k-1}]$.
   If $\text{len}(\text{pattern}) \ne \text{len}(W)$:
   $$
   \text{return False}
   $$
2. **Dual-Map State:**
   Maintain two hash tables:
   - $d_1: \text{char} \to \text{str}$ (Forward map: pattern character to word)
   - $d_2: \text{str} \to \text{char}$ (Reverse map: word to pattern character)
3. **Sequential Pair Inspection:**
   For each aligned pair $(c, w) \in \text{zip}(\text{pattern}, W)$:
   - **Forward Check:** If $c \in d_1$ and $d_1[c] \ne w \implies \text{return False}$.
   - **Reverse Check:** If $w \in d_2$ and $d_2[w] \ne c \implies \text{return False}$.
   - **Binding:**
     $$
     d_1[c] \leftarrow w, \quad d_2[w] \leftarrow c
     $$
4. If all pairs process without conflict, return `True`.

> **Invariant.** After processing index $i$, the mapping established between the prefix $\text{pattern}[0 \dots i]$ and word prefix $W[0 \dots i]$ is an exact bijection.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{pattern} = \text{"abba"}$ and $s = \text{"dog cat cat dog"}$:

### Step 1: Tokenization and Length Check
- Pattern length: $\text{len}(\text{"abba"}) = 4$.
- Split words: $W = [\text{"dog"}, \text{"cat"}, \text{"cat"}, \text{"dog"}]$.
- Word count: $\text{len}(W) = 4$.
- Lengths match ($4 == 4$). Proceed.
- Initialize maps: $d_1 = \{\}, \quad d_2 = \{\}$.

---

### Step 2: Index 0 ($c = \text{'a'}, \; w = \text{"dog"}$)
- Forward check: $\text{'a'} \notin d_1$.
- Reverse check: $\text{"dog"} \notin d_2$.
- Bind:
  $$
  d_1[\text{'a'}] = \text{"dog"}, \quad d_2[\text{"dog"}] = \text{'a'}
  $$
- Maps:
  - $d_1 = \{\text{'a'}: \text{"dog"}\}$
  - $d_2 = \{\text{"dog"}: \text{'a'}\}$

---

### Step 3: Index 1 ($c = \text{'b'}, \; w = \text{"cat"}$)
- Forward check: $\text{'b'} \notin d_1$.
- Reverse check: $\text{"cat"} \notin d_2$.
- Bind:
  $$
  d_1[\text{'b'}] = \text{"cat"}, \quad d_2[\text{"cat"}] = \text{'b'}
  $$
- Maps:
  - $d_1 = \{\text{'a'}: \text{"dog"}, \; \text{'b'}: \text{"cat"}\}$
  - $d_2 = \{\text{"dog"}: \text{'a'}, \; \text{"cat"}: \text{'b'}\}$

---

### Step 4: Index 2 ($c = \text{'b'}, \; w = \text{"cat"}$)
- Forward check: $\text{'b'} \in d_1$. Check $d_1[\text{'b'}] == \text{"cat"}$ (**True**; matches existing binding).
- Reverse check: $\text{"cat"} \in d_2$. Check $d_2[\text{"cat"}] == \text{'b'}$ (**True**; matches existing binding).
- Consistent! No map modification needed.

---

### Step 5: Index 3 ($c = \text{'a'}, \; w = \text{"dog"}$)
- Forward check: $\text{'a'} \in d_1$. Check $d_1[\text{'a'}] == \text{"dog"}$ (**True**; matches existing binding).
- Reverse check: $\text{"dog"} \in d_2$. Check $d_2[\text{"dog"}] == \text{'a'}$ (**True**; matches existing binding).
- Consistent!

---

### Loop Completion
All 4 pairs satisfied both forward and reverse consistency.
**Return `true`**.

---

## 4. Complete Execution Trace

```text
pattern = "abba", s = "dog cat cat dog"
words = ["dog", "cat", "cat", "dog"]

i = 0: c = 'a', w = "dog" -> new binding: 'a' <-> "dog"
i = 1: c = 'b', w = "cat" -> new binding: 'b' <-> "cat"
i = 2: c = 'b', w = "cat" -> matches existing 'b' <-> "cat"
i = 3: c = 'a', w = "dog" -> matches existing 'a' <-> "dog"

Result: true
```

| Index $i$ | Pattern Char $c$ | Word $w$ | Forward Check ($d_1[c]$) | Reverse Check ($d_2[w]$) | Action Taken | Current Bijective Bindings |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | `'a'` | `"dog"` | Not in $d_1$ | Not in $d_2$ | Bind `'a' \leftrightarrow \text{"dog"}$ | `{'a': "dog"}` |
| 1 | `'b'` | `"cat"` | Not in $d_1$ | Not in $d_2$ | Bind `'b' \leftrightarrow \text{"cat"}$ | `{'a': "dog", 'b': "cat"}` |
| 2 | `'b'` | `"cat"` | Matches (`"cat"`) | Matches (`'b'`) | Validated | `{'a': "dog", 'b': "cat"}` |
| 3 | `'a'` | `"dog"` | Matches (`"dog"`) | Matches (`'a'`) | Validated | `{'a': "dog", 'b': "cat"}` |
| **End** | - | - | - | - | - | **`true` (Valid Bijection)** |

---

### Failure Trace Contrast: Non-Injective Instance (`pattern = "abba", s = "dog dog dog dog"`)
- $i = 0$: $c = \text{'a'}, w = \text{"dog"}$. Binds $d_1[\text{'a'}] = \text{"dog"}, \; d_2[\text{"dog"}] = \text{'a'}$.
- $i = 1$: $c = \text{'b'}, w = \text{"dog"}$.
  - Forward check: $\text{'b'} \notin d_1$ (OK).
  - Reverse check: $\text{"dog"} \in d_2$, but $d_2[\text{"dog"}] = \text{'a'} \ne \text{'b'}$!
  - Conflict detected! Immediate return **`false`**.

---

## 5. Algorithmic Correctness

**Soundness.** A string follows the pattern if there exists a bijection between characters and words. The forward check ensures functionality (no character maps to two different words), while the reverse check ensures injectivity (no two characters map to the same word). Because both domains have equal length, the mapping is also surjective, guaranteeing a true bijection.

**Completeness.** Every pair $(c_i, w_i)$ is examined. If any inconsistency exists, it is detected either at the moment a previously mapped character encounters a different word, or when a previously mapped word encounters a different character. If no conflict arises across all pairs, the bijection is complete.

---

## 6. Traps This Instance Exposes

- **Missing Reverse Map (One-Way Mapping Trap):** Checking only `d[c] == w` fails on `"abba"` with `"dog dog dog dog"`. Using two dictionaries or a dictionary plus a `seen_words` set is mandatory to guarantee injectivity.
- **Unequal Token Counts:** `zip(pattern, s.split())` in Python stops at the length of the shorter sequence. For `pattern = "aaa"` and `s = "aa aa aa aa"`, `zip` evaluates only the first 3 tokens and would falsely return `True`. Checking `len(pattern) == len(words)` upfront is critical.
- **Non-String / Number Tokens:** In loosely-typed environments, words that look like numbers or booleans might be cast. Maintaining pure strings prevents type coercion mismatches.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N + M)$, where $N$ is the length of `pattern` and $M$ is the length of string `s`. Splitting `s` into words takes $O(M)$ time. The verification loop iterates $N$ times, performing $O(\text{len}(w))$ hash computations per word. Total time is strictly linear in input size.
- **Auxiliary Space Complexity:** $O(N + M)$ auxiliary memory to store the split words and hash maps $d_1$ and $d_2$.
