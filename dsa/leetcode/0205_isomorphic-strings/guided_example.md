# Guided Example: Isomorphic Strings

We trace the step-by-step bidirectional character bijection tracking and collision detection on representative string pairs:

- **Input:** $s = \text{"paper"}, \quad t = \text{"title"}$
- **Required output:** `true` (Valid bijection: $p \leftrightarrow t, \, a \leftrightarrow i, \, e \leftrightarrow l, \, r \leftrightarrow e$)
- **One-to-Many Conflict Instance:** $s = \text{"foo"}, \quad t = \text{"bar"} \implies \text{false}$ (Source character $'o'$ attempts to map to both $'a'$ and $'r'$)
- **Many-to-One Conflict Instance:** $s = \text{"badc"}, \quad t = \text{"baba"} \implies \text{false}$ (Target character $'b'$ is claimed by both $'b'$ and $'d'$)
- **Self-Mapping Instance:** $s = \text{"egg"}, \quad t = \text{"add"} \implies \text{true}$ ($e \leftrightarrow a, \, g \leftrightarrow d$)

This instance demonstrates modeling string isomorphism as a bijective function ($\phi: \Sigma_s \to \Sigma_t$), proves why tracking only a single directional map fails to detect many-to-one collisions, constructs twin hash maps (`s2t` and `t2s`), and operates in $O(N)$ time with $O(|\Sigma|)$ space.

---

## 1. Instance & Teaching Goal

Given two strings $s = \text{"paper"}$ and $t = \text{"title"}$ of equal length $N = 5$:
Determine whether $s$ and $t$ are **isomorphic**.
Two strings are isomorphic if every character in $s$ can be replaced with a character in $t$ such that:
1. Every occurrence of a character $c \in s$ maps to the **exact same** character in $t$.
2. **No two distinct characters** in $s$ map to the same character in $t$ (injectivity).
3. Character order is strictly preserved.

Evaluating the position-by-position alignments:
- Position 0: $s[0] = \text{'p'}, \, t[0] = \text{'t'} \implies \text{'p'} \leftrightarrow \text{'t'}$.
- Position 1: $s[1] = \text{'a'}, \, t[1] = \text{'i'} \implies \text{'a'} \leftrightarrow \text{'i'}$.
- Position 2: $s[2] = \text{'p'}, \, t[2] = \text{'t'} \implies$ Consistent with existing rule $\text{'p'} \leftrightarrow \text{'t'}$.
- Position 3: $s[3] = \text{'e'}, \, t[3] = \text{'l'} \implies \text{'e'} \leftrightarrow \text{'l'}$.
- Position 4: $s[4] = \text{'r'}, \, t[4] = \text{'e'} \implies \text{'r'} \leftrightarrow \text{'e'}$ *(Notice: character `'e'` in $t$ is distinct from `'e'` in $s$)*.
Because every mapped pair is consistent and injective, the strings are isomorphic (`true`).

Now contrast this with $s = \text{"badc"}$ and $t = \text{"baba"}$:
- At index 0: $\text{'b'} \to \text{'b'}$.
- At index 2: $s[2] = \text{'d'}, \, t[2] = \text{'b'}$. Here, source character `'d'` attempts to map to target character `'b'`, but `'b'` has already been claimed by source character `'b'`!
If one only checked $s \to t$, this conflict would be missed. A valid isomorphism requires a **two-way bijection**.

---

## 2. Conceptual Foundation & Invariants

### The Bijective Mapping Invariant
Let $\Sigma$ be the alphabet. An isomorphism is a bijective function $\phi: \Sigma_s \to \Sigma_t$:
- **Consistency ($s \to t$):** If $s[i] == s[j]$, then $t[i]$ must equal $t[j]$.
- **Injectivity ($t \to s$):** If $t[i] == t[j]$, then $s[i]$ must equal $s[j]$.

### Dual Hash Map Protocol:
Maintain two lookup structures:
- `s2t = {}`: tracks the forward mapping $s[i] \to t[i]$.
- `t2s = {}`: tracks the reverse mapping $t[i] \to s[i]$.

For each index $i$ from $0$ to $N - 1$:
Let $u = s[i]$ and $v = t[i]$.
1. **Forward Check:**
   If $u \in \text{s2t}$ and $\text{s2t}[u] \ne v$: return `false` (One-to-many conflict).
2. **Reverse Check:**
   If $v \in \text{t2s}$ and $\text{t2s}[v] \ne u$: return `false` (Many-to-one conflict).
3. **Register Correspondence:**
   $$
   \text{s2t}[u] \leftarrow v, \quad \text{t2s}[v] \leftarrow u
   $$

Return `true` if all characters are processed without conflict.

> **Invariant.** After processing prefix $0 \dots i$, the relation defined by `s2t` and `t2s` is a strictly bijective graph between all characters observed in $s[0 \dots i]$ and $t[0 \dots i]$.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"paper"}$ and $t = \text{"title"}$ ($N = 5$):

### Index 0: $u = \text{'p'}, \, v = \text{'t'}$
- Check $u \in \text{s2t}$: Not present.
- Check $v \in \text{t2s}$: Not present.
- Register: $\text{s2t}[\text{'p'}] = \text{'t'}, \quad \text{t2s}[\text{'t'}] = \text{'p'}$.

---

### Index 1: $u = \text{'a'}, \, v = \text{'i'}$
- Check $u \in \text{s2t}$: Not present.
- Check $v \in \text{t2s}$: Not present.
- Register: $\text{s2t}[\text{'a'}] = \text{'i'}, \quad \text{t2s}[\text{'i'}] = \text{'a'}$.

---

### Index 2: $u = \text{'p'}, \, v = \text{'t'}$
- Check $u \in \text{s2t}$: Present! Expected target $= \text{s2t}[\text{'p'}] = \text{'t'}$.
  Current target is $\text{'t'}$. Match!
- Check $v \in \text{t2s}$: Present! Expected source $= \text{t2s}[\text{'t'}] = \text{'p'}$.
  Current source is $\text{'p'}$. Match!
- Consistency confirmed. No changes needed.

---

### Index 3: $u = \text{'e'}, \, v = \text{'l'}$
- Check $u \in \text{s2t}$: Not present.
- Check $v \in \text{t2s}$: Not present.
- Register: $\text{s2t}[\text{'e'}] = \text{'l'}, \quad \text{t2s}[\text{'l'}] = \text{'e'}$.

---

### Index 4: $u = \text{'r'}, \, v = \text{'e'}$
- Check $u \in \text{s2t}$: Not present.
- Check $v \in \text{t2s}$: Not present.
- Register: $\text{s2t}[\text{'r'}] = \text{'e'}, \quad \text{t2s}[\text{'e'}] = \text{'r'}$.

All 5 characters pass both validation checks. Return `true`.

---

## 4. Complete Execution Trace

```text
s = "paper", t = "title"

Idx 0: 'p' <-> 't' -> Add s2t['p']='t', t2s['t']='p'
Idx 1: 'a' <-> 'i' -> Add s2t['a']='i', t2s['i']='a'
Idx 2: 'p' <-> 't' -> Verified against existing mapping -> OK
Idx 3: 'e' <-> 'l' -> Add s2t['e']='l', t2s['l']='e'
Idx 4: 'r' <-> 'e' -> Add s2t['r']='e', t2s['e']='r'

Result: true
```

| Index $i$ | Pair $(u, v)$ | Forward Check (`s2t[u] == v`) | Reverse Check (`t2s[v] == u`) | Decision | Active Mappings (`s2t`) |
|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | `('p', 't')` | New key | New key | Register | `{'p': 't'}` |
| 1 | `('a', 'i')` | New key | New key | Register | `{'p': 't', 'a': 'i'}` |
| 2 | `('p', 't')` | Matches `'t'` | Matches `'p'` | Validated | `{'p': 't', 'a': 'i'}` |
| 3 | `('e', 'l')` | New key | New key | Register | `{'p': 't', 'a': 'i', 'e': 'l'}` |
| **4** | **`('r', 'e')`** | **New key** | **New key** | **Register** | **`{'p': 't', 'a': 'i', 'e': 'l', 'r': 'e'}` (True)** |

### Contrast: Conflict in $s = \text{"badc"}, t = \text{"baba"}$
- At index 0: `'b' <-> 'b'`.
- At index 1: `'a' <-> 'a'`.
- At index 2: $u = \text{'d'}, v = \text{'b'}$.
  - $u \notin \text{s2t}$.
  - $v \in \text{t2s}$ with $\text{t2s}[\text{'b'}] = \text{'b'} \ne \text{'d'}$!
  - Conflict detected: `'b'` cannot be produced by both `'b'` and `'d'`!
  - Returns `false` immediately!

The two conflict directions are worth placing side by side, because they fail at different checks. The one-to-many case is caught by the forward map, and the many-to-one case is caught by the reverse map at the very same index position:

| Conflict | Index $i$ | $u = s[i]$ | $v = t[i]$ | Forward check on `s2t` | Reverse check on `t2s` | Outcome |
|:---|:---:|:---:|:---:|:---|:---|:---|
| one-to-many, $s = \text{"foo"}, t = \text{"bar"}$ | 0 | `'f'` | `'b'` | `'f'` is not yet a key | `'b'` is not yet a key | register `'f'` $\leftrightarrow$ `'b'` |
| one-to-many, $s = \text{"foo"}, t = \text{"bar"}$ | 1 | `'o'` | `'a'` | `'o'` is not yet a key | `'a'` is not yet a key | register `'o'` $\leftrightarrow$ `'a'` |
| one-to-many, $s = \text{"foo"}, t = \text{"bar"}$ | 2 | `'o'` | `'r'` | **`s2t['o'] = 'a' \ne 'r'`** | never evaluated | reject at once |
| many-to-one, $s = \text{"badc"}, t = \text{"baba"}$ | 0 | `'b'` | `'b'` | `'b'` is not yet a key | `'b'` is not yet a key | register `'b'` $\leftrightarrow$ `'b'` |
| many-to-one, $s = \text{"badc"}, t = \text{"baba"}$ | 1 | `'a'` | `'a'` | `'a'` is not yet a key | `'a'` is not yet a key | register `'a'` $\leftrightarrow$ `'a'` |
| many-to-one, $s = \text{"badc"}, t = \text{"baba"}$ | 2 | `'d'` | `'b'` | `'d'` is not yet a key | **`t2s['b'] = 'b' \ne 'd'`** | reject at once |

Row 3 and row 6 use the same pair of positions and differ only in which dictionary objects. That is the whole argument for keeping both: with the forward map alone, row 6 would register `'d'` $\leftrightarrow$ `'b'` and wrongly return `true`, because nothing in the forward direction forbids two source characters from sharing one target.

---

## 5. Algorithmic Correctness

**Soundness.** A pair $(u, v)$ is registered only when neither $u$ nor $v$ has been bound to a different partner. If an existing binding exists, the algorithm verifies that the current character pair agrees with it. This directly checks the mathematical axioms of injectivity and functional well-definedness.

**Completeness.** The algorithm checks all character pairs from index $0$ to $N - 1$. If any violation exists, it is detected at the first offending index.

---

## 6. Traps This Instance Exposes

- **Single Dictionary Trap:** Using only `s2t` checks that each source character maps to a unique target, but fails to check that multiple source characters do not map to the same target (e.g. $s = \text{"ab"}, t = \text{"aa"}$ returns `true` with one dictionary). Two maps are required.
- **Index-of Transformation:** Replacing strings with their first-occurrence index patterns (e.g. `[s.find(c) for c in s] == [t.find(c) for c in t]`) is valid, but calling `.find()` inside a loop runs in $O(N^2)$ time! Dual hash maps achieve strictly $O(N)$.
- **Fixed Alphabet Size:** For standard ASCII, fixed 256-integer arrays `map_s[256]` and `map_t[256]` initialized to $-1$ achieve $O(1)$ space and zero hash overhead.

The alternatives below all decide the same predicate, so the choice is really about which structural fact each one makes available and what it gives up:

| Approach | What is stored | Time | Auxiliary space | Cost or failure mode |
|:---|:---|:---:|:---:|:---|
| Two maps, one per direction (used here) | The forward relation and its inverse | $O(N)$ | $O(\lvert \Sigma \rvert)$ | none; both axioms are tested at every index |
| One forward map only | $s[i] \to t[i]$ | $O(N)$ | $O(\lvert \Sigma \rvert)$ | accepts many-to-one collisions: `"ab"` against `"aa"` is wrongly reported isomorphic |
| First-occurrence index patterns | The first position at which each character appears | $O(N)$ with a map, $O(N^2)$ if each position is found by rescanning | $O(N)$ for the two pattern lists | correct answers, but the rescanning form repeats work on every index |
| Two 256-entry arrays | Direct-indexed slots initialised to a sentinel | $O(N)$ | $512$ fixed slots | hash-free and correct, but it presumes the alphabet is bounded by $256$, which the ASCII constraint supplies |

Every authored pair is also a boundary probe. The rows below list them with the exact index at which the method stops, so a reader can predict the decision before running anything:

| Pair | Pairs examined | First conflict | Result | What it isolates |
|:---|:---:|:---|:---:|:---|
| `"paper"` / `"title"` | $5$ | none | `true` | a repeated source character that must map to the same target twice |
| `"egg"` / `"add"` | $3$ | none | `true` | the shortest fully consistent non-trivial pair |
| `"foo"` / `"bar"` | $3$ | index $2$: `'o'` is bound to `'a'`, not `'r'` | `false` | one-to-many — a single source character demanding two targets |
| `"f11"` / `"b23"` | $3$ | index $2$: `'1'` is bound to `'2'`, not `'3'` | `false` | digits are ordinary ASCII symbols, with no special treatment |
| `"badc"` / `"baba"` | $3$ | index $2$: target `'b'` is already claimed by source `'b'` | `false` | many-to-one — invisible to the forward map alone |
| `"ab"` / `"aa"` | $2$ | index $1$: target `'a'` is already claimed by source `'a'` | `false` | the minimal many-to-one collision |
| `"eee"` / `"add"` | $3$ | index $1$: `'e'` is bound to `'a'`, not `'d'` | `false` | one source character repeated three times with shifting targets |
| `"e"` / `"add"` | $1$ | none | `true` | unequal lengths, outside the stated contract $t.\text{length} = s.\text{length}$: only the shared prefix is paired, so the extra `'d'` is never inspected |

The last row is a contract violation rather than a legitimate input, and it is instructive for exactly that reason: pairing stops as soon as the shorter string is exhausted, so a length mismatch silently truncates the comparison instead of raising an error.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of string $s$. The loop visits each character pair once, performing $O(1)$ hash table lookups and insertions.
- **Auxiliary Space Complexity:** $O(|\Sigma|)$ auxiliary space, where $|\Sigma|$ is the alphabet size (at most $256$ entries for extended ASCII, or bounded constant memory).
