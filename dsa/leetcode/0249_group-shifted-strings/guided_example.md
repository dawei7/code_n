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
- `"acef"`: steps are $+2, +3, +1 \pmod{26}$.

Comparing every pair of strings takes $O(N^2 \cdot L)$ time.
Instead, we compute a **canonical invariant hash key** for each string that is identical for all members of the same shift family, partitioning strings into a hash table in a single $O(L)$ pass.

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
- For `"acef"`: $\text{key} = (2, 3, 1)$.

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

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L)$, where $L$ is the total number of characters across all strings in `strings`. Each string of length $m$ is normalized in $O(m)$ time, followed by an $O(m)$ hash map lookup.
- **Auxiliary Space Complexity:** $O(L)$ auxiliary memory to store the hash map keys and output groupings containing all $L$ characters.
