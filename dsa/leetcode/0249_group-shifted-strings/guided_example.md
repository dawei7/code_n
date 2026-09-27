# Guided Example: Group Shifted Strings

We trace the step-by-step cyclic alphabet normalization, modular difference hash key generation, and equivalence class grouping on representative shifted string arrays:

- **Input:** $\text{strings} = [\text{"abc"}, \text{"bcd"}, \text{"acef"}, \text{"xyz"}, \text{"az"}, \text{"ba"}, \text{"a"}, \text{"z"}]$
- **Required output:**
  $$
  [[\text{"acef"}], \; [\text{"a"}, \text{"z"}], \; [\text{"abc"}, \text{"bcd"}, \text{"xyz"}], \; [\text{"az"}, \text{"ba"}]]
  $$
- **Single Letter Grouping:** $\text{"a"}$ and $\text{"z"}$ group together ($\Delta = \emptyset$)
- **Wraparound Equivalence:** $\text{"az"}$ and $\text{"ba"}$ group together ($z - a = 25 \equiv a - b = -1 \pmod{26}$)
- **Preserving Duplicates:** Identical strings map to the same key and remain distinct list items

This instance demonstrates modular arithmetic equivalence classes on circular alphabets ($\mathbb{Z}_{26}$), proves why normalizing every string so its first character begins with `'a'` (or using adjacent cyclic difference tuples) forms an invariant canonical hash key, groups elements in $O(L)$ time where $L$ is the total character count, and allocates $O(L)$ auxiliary storage.

---

## 1. Instance & Teaching Goal

Given an array of lowercase strings:
$$
\text{strings} = [\text{"abc"}, \text{"bcd"}, \text{"acef"}, \text{"xyz"}, \text{"az"}, \text{"ba"}, \text{"a"}, \text{"z"}]
$$
Group together all strings that belong to the same **shifting sequence** (where shifting increments every letter cyclically: $\text{'a'} \to \text{'b'} \to \dots \to \text{'z'} \to \text{'a'}$).

Notice the structural shifts:
- `"abc"` $\to$ `"bcd"` $\to \dots \to$ `"xyz"`: each adjacent letter increases by $+1 \pmod{26}$.
- `"az"` $\to$ `"ba"`: from $'a'$ to $'z'$ is $+25 \equiv -1 \pmod{26}$. Shifting both letters right yields $'b'$ and $'a'$, which also has step $-1 \equiv 25 \pmod{26}$.
- `"a"` and `"z"`: single characters can shift into any single character.
- `"acef"`: steps are $+2, +2, +1 \pmod{26}$ (from `'a'` to `'c'`, then `'c'` to `'e'`, then `'e'` to `'f'`).

Comparing every pair of strings takes $O(N^2 \cdot L)$ time.
Instead, we compute a **canonical invariant hash key** for each string that is identical for all members of the same shift family, partitioning strings into a hash table in a single $O(L)$ pass.

### Candidate Methods Compared

| Method | What it compares | Time | Auxiliary space | Tradeoff or failure mode |
|:---|:---|:---:|:---:|:---|
| Pairwise shift test | For each pair of equal length, derive the shift from the first characters and verify every position | $O(N^2 \cdot L)$ | $O(1)$ beyond the input | Correct and simple, but quadratic in the number of strings; with the maximum input size it re-checks the same relation millions of times |
| Order-insensitive fingerprints | Sort the letters of each string and compare the sorted forms | $O(N \cdot L \log L)$ | $O(L)$ per string | Wrong model entirely: sorting ignores positional structure, so `"abc"` and `"bca"` collide even though only the first can be shifted into `"bcd"` |
| Adjacent cyclic differences (Method B) | Hash the tuple of consecutive steps modulo $26$ | $O(L)$ | $O(L)$ for the key of every string | Correct and it never rewrites characters, but the key must stay a tuple or a delimited string; flattening `(1, 2)` and `(12)` into the same characters would merge unrelated shapes |
| Base-`'a'` normalization (Method A, chosen) | Rewrite each string so its first character becomes `'a'`, then hash the rewritten string | $O(L)$ | $O(L)$ for the keys plus the grouped output | One pass per string, key length equals word length so different lengths can never collide, and the wraparound is handled by a single modulo operation |

---

## 2. Conceptual Foundation & Invariants

### Method A: Base-'a' Canonical Normalization
To make all strings in a shifting family identical:
Shift the entire string backward by $\text{offset} = (\text{ord}(s[0]) - \text{ord('a')}) \pmod{26}$, forcing the first character to become `'a'`:
For each character $c$ in $s$:
$$
c_{\text{norm}} = \text{chr}\Big(\big(\text{ord}(c) - \text{ord('a')} - \text{offset}\big) \pmod{26} + \text{ord('a')}\Big)
$$
- For `"abc"`: $\text{offset} = 0 \implies \text{"abc"}$.
- For `"bcd"`: $\text{offset} = 1 \implies \text{"abc"}$.
- For `"xyz"`: $\text{offset} = 23 \implies \text{"abc"}$.
- For `"az"`: $\text{offset} = 0 \implies \text{"az"}$.
- For `"ba"`: $\text{offset} = 1 \implies \text{"az"}$ (since $(0 - 1) \pmod{26} = 25 \implies \text{'z'}$).

### Method B: Adjacent Difference Tuple
Compute the cyclic step between adjacent characters:
$$
\text{key} = \Big( (\text{ord}(s[i]) - \text{ord}(s[i-1])) \pmod{26} \quad \text{for } i = 1 \dots \text{len}(s)-1 \Big)
$$
- For single-character strings (`"a"`, `"z"`): $\text{key} = ()$.
- For `"abc"`, `"bcd"`, `"xyz"`: $\text{key} = (1, 1)$.
- For `"az"`, `"ba"`: $\text{key} = (25,)$.
- For `"acef"`: $\text{key} = (2, 2, 1)$.

> **Invariant.** Two strings $s_1$ and $s_2$ belong to the same shifting sequence if and only if their normalized forms (or difference tuples) are identical.

---

## 3. Step-by-Step Worked Execution

We trace the canonical normalization on $\text{strings} = [\text{"abc"}, \text{"bcd"}, \text{"acef"}, \text{"xyz"}, \text{"az"}, \text{"ba"}, \text{"a"}, \text{"z"}]$:

### 1. String `"abc"`
- Offset: $\text{ord('a')} - \text{ord('a')} = 0$.
- Normalized: `"abc"`.
- Group map: `{"abc": ["abc"]}`.

---

### 2. String `"bcd"`
- Offset: $\text{ord('b')} - \text{ord('a')} = 1$.
- Shift each char left by $1$:
  - $'b' - 1 = 'a'$
  - $'c' - 1 = 'b'$
  - $'d' - 1 = 'c'$
- Normalized: `"abc"`.
- Match existing group `"abc"`!
- Group map: `{"abc": ["abc", "bcd"]}`.

---

### 3. String `"acef"`
- Offset: $\text{ord('a')} - \text{ord('a')} = 0$.
- Normalized: `"acef"`.
- Group map: `{"abc": ["abc", "bcd"], "acef": ["acef"]}`.

---

### 4. String `"xyz"`
- Offset: $\text{ord('x')} - \text{ord('a')} = 23$.
- Shift left by $23$ (or right by $3$):
  - $'x' \to 'a'$
  - $'y' \to 'b'$
  - $'z' \to 'c'$
- Normalized: `"abc"`.
- Match existing group `"abc"`!
- Group map: `{"abc": ["abc", "bcd", "xyz"], ...}`.

---

### 5. String `"az"`
- Offset: $\text{ord('a')} - \text{ord('a')} = 0$.
- Normalized: `"az"`.
- Group map: `{"az": ["az"], ...}`.

---

### 6. String `"ba"`
- Offset: $\text{ord('b')} - \text{ord('a')} = 1$.
- Shift left by $1$:
  - $'b' - 1 = 'a'$
  - $'a' - 1 = -1 \equiv 25 \pmod{26} = 'z'$ (Wraparound!).
- Normalized: `"az"`.
- Match existing group `"az"`!
- Group map: `{"az": ["az", "ba"], ...}`.

---

### 7. Strings `"a"` and `"z"`
- `"a"`: length 1, offset 0 $\implies$ normalized: `"a"`.
- `"z"`: length 1, offset 25 $\implies$ $'z' - 25 = 'a' \implies$ normalized: `"a"`.
- Match group `"a"`!
- Group map: `{"a": ["a", "z"], ...}`.

---

## 4. Complete Execution Trace

```text
strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]

"abc"  -> offset = 0  -> key = "abc"  -> groups["abc"]  = ["abc"]
"bcd"  -> offset = 1  -> key = "abc"  -> groups["abc"]  = ["abc", "bcd"]
"acef" -> offset = 0  -> key = "acef" -> groups["acef"] = ["acef"]
"xyz"  -> offset = 23 -> key = "abc"  -> groups["abc"]  = ["abc", "bcd", "xyz"]
"az"   -> offset = 0  -> key = "az"   -> groups["az"]   = ["az"]
"ba"   -> offset = 1  -> key = "az"   -> groups["az"]   = ["az", "ba"]
"a"    -> offset = 0  -> key = "a"    -> groups["a"]    = ["a"]
"z"    -> offset = 25 -> key = "a"    -> groups["a"]    = ["a", "z"]

Result: [["abc", "bcd", "xyz"], ["acef"], ["az", "ba"], ["a", "z"]]
```

| Word $s$ | First Char | Shift Offset ($s[0] - \text{'a'}$) | Derived Normalized Key | Assigned Equivalence Group |
|:---:|:---:|:---:|:---:|:---|
| `"abc"` | `'a'` | 0 | `"abc"` | `["abc"]` |
| `"bcd"` | `'b'` | 1 | `"abc"` | `["abc", "bcd"]` |
| `"acef"` | `'a'` | 0 | `"acef"` | `["acef"]` |
| `"xyz"` | `'x'` | 23 | `"abc"` | `["abc", "bcd", "xyz"]` |
| `"az"` | `'a'` | 0 | `"az"` | `["az"]` |
| `"ba"` | `'b'` | 1 | `"az"` | `["az", "ba"]` |
| `"a"` | `'a'` | 0 | `"a"` | `["a"]` |
| `"z"` | `'z'` | 25 | `"a"` | `["a", "z"]` |

### Both Canonical Keys Side by Side

The two keys are computed by different routes, so it is worth seeing them agree on every member of the sample. Letter indices use the convention `'a'` $= 0$ and `'z'` $= 25$:

| Word | Letter indices | Cyclic steps modulo $26$ | Method B key | Method A key | Family |
|:---|:---|:---|:---:|:---:|:---:|
| `"abc"` | $0, 1, 2$ | $1, 1$ | $(1, 1)$ | `"abc"` | $G_1$ |
| `"bcd"` | $1, 2, 3$ | $1, 1$ | $(1, 1)$ | `"abc"` | $G_1$ |
| `"xyz"` | $23, 24, 25$ | $1, 1$ | $(1, 1)$ | `"abc"` | $G_1$ |
| `"acef"` | $0, 2, 4, 5$ | $2, 2, 1$ | $(2, 2, 1)$ | `"acef"` | $G_2$ |
| `"az"` | $0, 25$ | $25$ | $(25)$ | `"az"` | $G_3$ |
| `"ba"` | $1, 0$ | $25$ | $(25)$ | `"az"` | $G_3$ |
| `"a"` | $0$ | none, a single letter has no step | `()` | `"a"` | $G_4$ |
| `"z"` | $25$ | none | `()` | `"a"` | $G_4$ |

The families are $G_1 = \{\text{"abc"}, \text{"bcd"}, \text{"xyz"}\}$, $G_2 = \{\text{"acef"}\}$, $G_3 = \{\text{"az"}, \text{"ba"}\}$ and $G_4 = \{\text{"a"}, \text{"z"}\}$. Reading down either key column gives exactly the same partition: rows that share a step tuple share a normalized string, and vice versa. The wraparound is visible as the single step $25$ shared by `"az"` and `"ba"`, which is the same cyclic distance $(\text{'a'} - \text{'b'}) \bmod 26$ that Method A realises by rewriting `'a'` as `'z'`. The empty tuple is a genuine key rather than a special case, which is exactly why `"a"` and `"z"` — offsets $0$ and $25$ — still meet in $G_4$.

---

## 5. Algorithmic Correctness

**Soundness.** Suppose two strings $s$ and $t$ belong to the same shifting sequence. Then there exists an integer $k \in [0, 25]$ such that $t[i] \equiv (s[i] + k) \pmod{26}$ for all $i$. Let $\text{offset}_s = s[0] - \text{'a'}$ and $\text{offset}_t = t[0] - \text{'a'} = (s[0] + k) - \text{'a'} \equiv \text{offset}_s + k \pmod{26}$.
For every position $i$:
$$
t[i] - \text{offset}_t \equiv (s[i] + k) - (\text{offset}_s + k) \equiv s[i] - \text{offset}_s \pmod{26}
$$
The offset shifts cancel out completely, proving the normalized strings are identical.

**Completeness.** Conversely, if two strings have the same normalized key, shifting the first string by $(t[0] - s[0]) \pmod{26}$ produces the second string at every position, proving they belong to the same shift orbit.

---

## 6. Traps This Instance Exposes

- **Modulo with Negative Numbers in C++ vs Python:** In Python, `-1 % 26 = 25` natively. In C/C++, `-1 % 26 = -1`. In C++, one must write `(diff + 26) % 26` to guarantee a non-negative modulo index.
- **Length Invariance:** Two strings with different lengths cannot belong to the same shift sequence. Normalizing base-'a' naturally preserves string length (e.g. `"a"` has length 1, `"aa"` has length 2), preventing accidental collisions.
- **Tuples vs Strings as Keys:** When using adjacent differences, using a Python `tuple` of differences or a delimited string (e.g. `"1#2"`) is required. Storing as raw digits (e.g. `"12"`) could cause ambiguity between difference 1 followed by 2, versus a single difference of 12! Base-'a' normalized strings completely bypass delimiter issues.

### Boundary Behaviour of the Grouping

| Boundary scenario | Concrete input | Required result | Why the key produces it |
|:---|:---|:---|:---|
| Smallest possible input | `["a"]` | `[["a"]]` | One insertion yields one family; the empty step tuple is a valid key, so no separate branch is needed for a lone string |
| Wraparound in both directions | `["az", "ba", "yx", "ab", "za"]` | `[["az", "ba", "yx"], ["ab", "za"]]` | Leftward steps of $25$ group `"az"`, `"ba"` and `"yx"` together, while `"ab"` and `"za"` share the rightward step $1$; the modulo keeps both directions non-negative |
| Length separates identical shapes | `["a", "aa", "b", "bb", "abc", "bcd"]` | `[["a", "b"], ["aa", "bb"], ["abc", "bcd"]]` | `"a"` and `"b"` share the empty tuple, `"aa"` and `"bb"` share the step $(0)$, and the three families stay apart because tuples of different lengths are never equal |
| Constant letters versus reversing steps | `["aaa", "bbb", "ccc", "aba", "bcb", "yzy"]` | `[["aaa", "bbb", "ccc"], ["aba", "bcb", "yzy"]]` | The flat shape has steps $(0, 0)$ while the second shape has steps $(1, 25)$; non-uniform steps are perfectly legal, and the $25$ is the wrap from `'a'` back to the previous letter |
| Duplicate entries | `["abc", "abc", "bcd", "acef", "acef"]` | `[["abc", "abc", "bcd"], ["acef", "acef"]]` | Grouping collects occurrences, not distinct values, so repeated inputs are reported with their multiplicity rather than deduplicated |
| Maximum number of strings | $200$ single-character strings | one family containing all $200$ | Every single-character string has the same empty signature, so the entire input collapses into one equivalence class no matter which letters appear |
| Maximum string length | two $50$-character strings of one repeated letter, plus a $50$-character alphabet cycle and its one-step shift | two families of two | The repeated-letter pair shares the all-zero step tuple, and the cycle pair agrees at all $49$ positions, including the step that wraps from `'z'` back to `'a'` |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L)$, where $L$ is the total number of characters across all strings in `strings`. Each string of length $m$ is normalized in $O(m)$ time, followed by an $O(m)$ hash map lookup.
- **Auxiliary Space Complexity:** $O(L)$ auxiliary memory to store the hash map keys and output groupings containing all $L$ characters.
