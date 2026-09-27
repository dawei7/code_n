# Guided Example: Sort Characters By Frequency

We trace the step-by-step character frequency histogramming, frequency-descending pair ordering, multi-occurrence character expansion ($c \times count$), and string reconstruction on representative string inputs:

- **Input:** $s = \text{"tree"}$
- **Required output:** `"eert"` (or `"eetr"`)
- **Execution trace:**
  - Step 1: Compute character frequency histogram:
    - Char `'t'`: count $1$
    - Char `'r'`: count $1$
    - Char `'e'`: count $2$
    - Frequency map: $\{\text{'e'}: 2, \; \text{'t'}: 1, \; \text{'r'}: 1\}$
  - Step 2: Sort unique characters by frequency descending:
    - Pair 1: $(\text{'e'}, 2)$
    - Pair 2: $(\text{'t'}, 1)$ (or $(\text{'r'}, 1)$)
    - Pair 3: $(\text{'r'}, 1)$
  - Step 3: Emit characters multiplied by their counts:
    - For $(\text{'e'}, 2) \implies \text{'e'} \times 2 = \text{"ee"}$
    - For $(\text{'t'}, 1) \implies \text{'t'} \times 1 = \text{"t"}$
    - For $(\text{'r'}, 1) \implies \text{'r'} \times 1 = \text{"r"}$
    - Concatenation: $\text{"ee"} + \text{"t"} + \text{"r"} = \mathbf{\text{"eetr"}}$ (or $\text{"eert"}$)
- **Tied Frequencies Instance:** $s = \text{"cccaaa"} \implies \text{count('c')} = 3, \text{count('a')} = 3 \implies \mathbf{\text{"cccaaa"}}$ (or `"aaaccc"`)
- **Case-Sensitivity Instance:** $s = \text{"Aabb"} \implies \text{count('b')} = 2, \text{count('a')} = 1, \text{count('A')} = 1 \implies \mathbf{\text{"bbAa"}}$ (`'A'` and `'a'` are treated as distinct characters)

This instance demonstrates counting-based sorting and bucket sorting, mathematically proves why characters with identical frequencies can be output in arbitrary relative order, and derives $O(N + K \log K)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string $s = \text{"tree"}$:
Sort it in **decreasing order** based on the frequency of the characters.
The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple valid answers, return any of them.

```text
Original String: "tree"
Character Frequencies:
  'e' -> 2
  't' -> 1
  'r' -> 1

Sorted by Frequency (Descending):
  'e' (2) -> "ee"
  'r' (1) -> "r"
  't' (1) -> "t"

Output: "eert" (or "eetr")
```

### The Grouping Invariant
All identical characters must appear together in a contiguous block of length equal to their frequency.
A character with frequency $f_1$ must appear before any character with frequency $f_2$ whenever $f_1 > f_2$.
Characters with equal frequencies ($f_1 == f_2$) may be ordered arbitrarily.

---

## 2. Conceptual Foundation & Invariants

### 1. Histogram Frequency Mapping:
Map each unique character $c \in s$ to its occurrence count:
$$
cnt[c] = \sum_{i=0}^{|s|-1} \mathbf{1}[s[i] == c]
$$

### 2. Frequency Sorting:
Extract all unique key-value pairs $(c, cnt[c])$:
Sort pairs in non-increasing order of their count $cnt[c]$:
$$
cnt[c_1] \ge cnt[c_2] \ge \dots \ge cnt[c_K]
$$
Where $K \le |\Sigma|$ is the number of distinct characters in $s$.

### 3. String Assembly:
Concatenate repeated character sequences:
$$
\text{Output} = \prod_{i=1}^K c_i^{cnt[c_i]}
$$

> **Frequency Invariant.** In the emitted string, for any two distinct characters $a$ and $b$, if $cnt[a] > cnt[b]$, then every occurrence of $a$ precedes every occurrence of $b$.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"tree"}$ ($N = 4$):

---

### Step 1: Frequency Histogram
Count occurrences:
- `'t'`: 1
- `'r'`: 1
- `'e'`: 2
Map: $\{\text{'e'}: 2, \; \text{'t'}: 1, \; \text{'r'}: 1\}$.

---

### Step 2: Sort by Frequency Descending
Sort unique character pairs by count:
1. $(\text{'e'}, 2)$
2. $(\text{'t'}, 1)$
3. $(\text{'r'}, 1)$

---

### Step 3: Reconstruct Compressed String
- From $(\text{'e'}, 2)$: emit `'e'` twice $\implies \text{"ee"}$.
- From $(\text{'t'}, 1)$: emit `'t'` once $\implies \text{"t"}$.
- From $(\text{'r'}, 1)$: emit `'r'` once $\implies \text{"r"}$.
Join all segments:
$$
\text{"ee"} + \text{"t"} + \text{"r"} = \mathbf{\text{"eetr"}}
$$

---

## 4. Complete Execution Trace

| Character $c$ | Total Count in $s$ | Frequency Rank | Segment Generated | Output Prefix |
|:---:|:---:|:---:|:---:|:---|
| `'e'` | $2$ | **1st** | `"ee"` | `"ee"` |
| `'t'` | $1$ | 2nd | `"t"` | `"eet"` |
| `'r'` | $1$ | 3rd | `"r"` | `"eetr"` |

---

## 5. Boundary Cases & Failure Modes

- **Case Sensitivity ($s = \text{"Aabb"}):$** `'A'` (count 1) and `'a'` (count 1) are distinct ASCII characters. Group `'b'` (count 2) appears first $\implies \text{"bbAa"}$ or $\text{"bbaA"}$.
- **All Unique Characters ($s = \text{"abc"}):$** All frequencies are 1 $\implies$ any permutation is valid.
- **All Identical Characters ($s = \text{"aaaa"}):$** Only 1 unique character $\implies \text{"aaaa"}$.
- **Single Character ($s = \text{"z"}):$** Output is $\text{"z"}$.

---

## 6. Traps & Common Anti-Patterns

- **Case Flattening:** Converting to lowercase with `s.lower()` corrupts the output when the problem requires case-sensitive distinction between `'A'` and `'a'`.
- **String Concatenation in Loops:** Repeatedly writing `res += char * count` inside a loop in quadratic memory environments creates garbage string allocations. Using `''.join(...)` on a list of string chunks is linear in total characters.
- **Sorting the Entire String of Length $N$:** Sorting the entire string takes $O(N \log N)$ time. Sorting only the $K \le 62$ distinct alphanumeric characters takes $O(K \log K)$ time, which is constant $O(1)$ relative to $N$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Counting character frequencies takes $O(N)$ time.
  - The number of distinct characters $K$ is bounded by the alphabet size $|\Sigma| \le 128$.
  - Sorting $K$ unique pairs takes $O(K \log K)$ time.
  - Reconstructing the string of length $N$ takes $O(N)$ time.
  - Total Time: $\mathcal{O}(N + K \log K) = \mathcal{O}(N)$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(K) = \mathcal{O}(1)$ for the frequency map, and $O(N)$ for the returned string.
