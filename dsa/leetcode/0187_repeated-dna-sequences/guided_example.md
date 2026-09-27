# Guided Example: Repeated DNA Sequences

We trace the step-by-step fixed-width rolling 10-mer extraction, 2-bit nucleotide encoding, and hash frequency deduplication on representative genomic strings:

- **Input:** $s = \text{"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"}$
- **Required output:** `["AAAAACCCCC", "CCCCCAAAAA"]`
- **Overlapping Repetition Instance:** $s = \text{"AAAAAAAAAAAAA"} \implies \text{["AAAAAAAAAA"]}$ (Length 13 contains 4 identical overlapping 10-mers)
- **Short Input Edge Instance:** $s = \text{"ACGT"} \implies []$ (Length $< 10$ yields zero valid substrings)

This instance demonstrates fixed 10-mer substring evaluation, contrasts raw string set hashing with 20-bit integer rolling masks ($2 \text{ bits/char} \times 10 \text{ chars}$), prevents output duplicates using twin hash sets (`seen` and `repeated`), and executes in $O(N)$ time.

---

## 1. Instance & Teaching Goal

Given a DNA sequence string composed solely of four nucleotides (`'A'`, `'C'`, `'G'`, `'T'`):
$$
s = \text{"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"}
$$
Identify all **10-letter-long substrings** that occur **more than once** in the sequence.

Analyzing substrings of length $L = 10$:
- At index $0$: $s[0:10] = \text{"AAAAACCCCC"}$.
- At index $5$: $s[5:15] = \text{"CCCCCAAAAA"}$.
- At index $10$: $s[10:20] = \text{"AAAAACCCCC"}$ (Identical to substring at index 0 $\implies$ Repeated!).
- At index $15$: $s[15:25] = \text{"CCCCCAAAAA"}$ (Identical to substring at index 5 $\implies$ Repeated!).
- At index $16$: $s[16:26] = \text{"CCCCAAAAAG"}$.
- All other 10-mers appear only once.
Result: `["AAAAACCCCC", "CCCCCAAAAA"]`.

Instead of variable-length window expansion and contraction, this problem requires evaluating a **fixed-width sliding window of length 10**.
Because the alphabet size is $|\Sigma| = 4$, each character can be packed into 2 bits, enabling $O(1)$ bit-shift rolling hash updates without heap-allocated string slicing.

---

## 2. Conceptual Foundation & Invariants

### Method A: Twin Hash Sets (Substring Slicing)
Maintain two sets:
- `seen = set()`: records 10-mers encountered so far.
- `repeated = set()`: records 10-mers that have occurred $\ge 2$ times (ensuring the final list has no duplicates).

For each index $i$ from $0$ to $|s| - 10$:
1. Extract candidate 10-mer: $\text{sub} = s[i : i + 10]$.
2. If $\text{sub} \in \text{seen}$:
   Add to `repeated.add(sub)`.
3. Else:
   `seen.add(sub)`.

Return `list(repeated)`.

### Method B: 20-Bit Rolling Hash (Bit Manipulation)
Map each nucleotide to a 2-bit binary integer:
$$
\text{'A'} \to 00_2 \, (0), \quad \text{'C'} \to 01_2 \, (1), \quad \text{'G'} \to 10_2 \, (2), \quad \text{'T'} \to 11_2 \, (3)
$$
A 10-character window contains $10 \times 2 = 20$ bits, fitting into a single 32-bit integer register.
To slide the window:
1. Shift current hash left by 2 bits: $\text{hash} \ll 2$.
2. Append new character's 2-bit code: $\mid \text{code}$.
3. Mask out the 21st and higher bits using bitmask: $\& \, ((1 \ll 20) - 1)$.

> **Invariant.** `seen` stores every unique 10-mer ending at or before index $i + 9$. `repeated` contains only those 10-mers that have appeared at least twice, avoiding duplicate emissions.

---

## 3. Step-by-Step Worked Execution

We trace the sliding window across $s = \text{"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"}$ ($N = 33$):

### Step 1: Initial 10-mer (Index 0)
- Slice: $s[0:10] = \text{"AAAAACCCCC"}$.
- Check: Not in `seen`.
- Add to `seen`: `seen = {"AAAAACCCCC"}`.

---

### Step 2: Intermediate Substrings (Indices 1 to 4)
- $i = 1$: $s[1:11] = \text{"AAAACCCCCA"}$. Added to `seen`.
- $i = 2$: $s[2:12] = \text{"AAACCCCCAA"}$. Added to `seen`.
- $i = 3$: $s[3:13] = \text{"AACCCCCAAA"}$. Added to `seen`.
- $i = 4$: $s[4:14] = \text{"ACCCCCAAAA"}$. Added to `seen`.

---

### Step 3: Candidate 10-mer (Index 5)
- Slice: $s[5:15] = \text{"CCCCCAAAAA"}$.
- Check: Not in `seen`.
- Add to `seen`: `seen = {..., "CCCCCAAAAA"}`.

---

### Step 4: First Duplicate Detected (Index 10)
- Slice: $s[10:20] = \text{"AAAAACCCCC"}$.
- Check: `sub in seen`?
  $$
  \text{"AAAAACCCCC"} \in \text{seen} \implies \mathbf{True!}
  $$
- Add to `repeated`:
  $$
  \text{repeated} = \{\text{"AAAAACCCCC"}\}
  $$

---

### Step 5: Second Duplicate Detected (Index 15)
- Slice: $s[15:25] = \text{"CCCCCAAAAA"}$.
- Check: `sub in seen`?
  $$
  \text{"CCCCCAAAAA"} \in \text{seen} \implies \mathbf{True!}
  $$
- Add to `repeated`:
  $$
  \text{repeated} = \{\text{"AAAAACCCCC"}, \, \text{"CCCCCAAAAA"}\}
  $$

---

### Step 6: Remaining Slices (Indices 16 to 23)
- Substrings such as `"CCCCAAAAAG"`, `"CCCAAAAAGG"`, $\dots$ are encountered for the first time.
- Added to `seen`. No further duplicates found.

Final output: `["AAAAACCCCC", "CCCCCAAAAA"]`.

---

## 4. Complete Execution Trace

```text
Sequence: AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT

Index 0:  "AAAAACCCCC" -> New -> Add to seen
Index 1:  "AAAACCCCCA" -> New -> Add to seen
Index 5:  "CCCCCAAAAA" -> New -> Add to seen
Index 10: "AAAAACCCCC" -> SEEN! -> Add to repeated: {"AAAAACCCCC"}
Index 15: "CCCCCAAAAA" -> SEEN! -> Add to repeated: {"AAAAACCCCC", "CCCCCAAAAA"}

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
```

| Window Index $i$ | 10-mer String $s[i:i+10]$ | Membership in `seen` | Action | Active `repeated` Set |
|:---:|:---|:---:|:---:|:---|
| 0 | `"AAAAACCCCC"` | `False` | Add to `seen` | $\emptyset$ |
| 1 | `"AAAACCCCCA"` | `False` | Add to `seen` | $\emptyset$ |
| 5 | `"CCCCCAAAAA"` | `False` | Add to `seen` | $\emptyset$ |
| **10** | **`"AAAAACCCCC"`** | **`True`** | **Add to `repeated`** | **`{"AAAAACCCCC"}`** |
| **15** | **`"CCCCCAAAAA"`** | **`True`** | **Add to `repeated`** | **`{"AAAAACCCCC", "CCCCCAAAAA"}`** |
| 16 | `"CCCCAAAAAG"` | `False` | Add to `seen` | `{"AAAAACCCCC", "CCCCCAAAAA"}` |

---

## 5. Algorithmic Correctness

**Soundness.** A 10-mer is added to `repeated` if and only if it has already been inserted into `seen` at an earlier index. By using a hash set for `repeated`, strings that appear 3 or more times (e.g. in `"AAAAAAAAAAAAA"`) are recorded only once.

**Completeness.** There are exactly $N - 9$ contiguous substrings of length 10 in a string of length $N$. The loop scans every integer $0 \le i \le N - 10$, evaluating all possible 10-mers.

---

## 6. Traps This Instance Exposes

- **String Slicing Memory Overhead:** Creating $O(N)$ string objects of length 10 creates significant memory allocation. The 20-bit integer rolling hash replaces heap allocations with primitive integer bitwise operations.
- **Overlapping Substrings:** In `"AAAAAAAAAAAAA"` ($N = 13$), there are 4 overlapping substrings at indices $0, 1, 2, 3$, all equal to `"AAAAAAAAAA"`. The output must contain `"AAAAAAAAAA"` only once, requiring a set for `repeated`.
- **Short Input Length:** If $|s| < 10$, the loop range $0 \le i \le |s| - 10$ is empty, correctly returning an empty list `[]`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of string $s$. There are $N - 9$ substrings of length 10. Using rolling hash bit manipulation takes $O(1)$ time per window, totaling $O(N)$ operations.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory to store at most $N$ integers in the `seen` hash table.