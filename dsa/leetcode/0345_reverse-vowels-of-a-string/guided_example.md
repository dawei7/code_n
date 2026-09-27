# Guided Example: Reverse Vowels of a String

We trace the step-by-step two-pointer inward consonant skipping (`not in vowels`), bidirectional pointer convergence, case-sensitive character swapping ($cs[i], cs[j] = cs[j], cs[i]$), and mutable list reconstruction on representative string instances:

- **Input:** $s = \text{"IceCreAm"}$
- **Required output:** $\text{"AceCreIm"}$
  - Identified vowels:
    - Index $0$: `'I'`
    - Index $2$: `'e'`
    - Index $5$: `'e'`
    - Index $6$: `'A'`
    - Extracted vowel sequence: `['I', 'e', 'e', 'A']`
  - Reversed vowel sequence: `['A', 'e', 'e', 'I']`
  - Re-inserted into vowel positions while consonants (`'c', 'C', 'r', 'm'`) remain stationary:
    - Index 0: `'A'`
    - Index 2: `'e'`
    - Index 5: `'e'`
    - Index 6: `'I'`
  - Final string: $\text{"AceCreIm"}$
- **All Lowercase Instance:** $s = \text{"leetcode"} \implies \text{"leotcede"}$ (vowels: `'e', 'e', 'o', 'e'` reversed to `'e', 'o', 'e', 'e'`)
- **No Vowels Present:** $s = \text{"bcdfg"} \implies \text{"bcdfg"}$ (zero swaps performed)
- **Single Vowel Base Case:** $s = \text{"a"} \implies \text{"a"}$

This instance demonstrates selective in-place two-pointer swapping with predicate filtering, mathematically proves why advancing past consonants maintains strict $O(N)$ linear time without quadratic string slicing, and operates in $O(N)$ buffer space.

---

## 1. Instance & Teaching Goal

Given a string $s = \text{"IceCreAm"}$ ($N = 8$):
Reverse **only the vowels** (`'a', 'e', 'i', 'o', 'u'` in both lowercase and uppercase) while keeping all consonant characters in their original positions:

```text
Original String:  "IceCreAm"
Vowel Positions:   ^ ^  ^^
                   0 2  56
Vowels:           'I', 'e', 'e', 'A'
Reversed Vowels:  'A', 'e', 'e', 'I'

Final Rebuilt:    "AceCreIm"
```

### Character Set Invariant
The vowel domain contains exactly 10 ASCII characters:
$$
\text{vowels} = \text{"aeiouAEIOU"}
$$
Case sensitivity must be strictly preserved during character swapping (e.g. uppercase `'I'` and `'A'` retain their capitalization after being swapped).

---

## 2. Conceptual Foundation & Invariants

### 1. Mutable Character Buffer
Because Python strings are immutable, convert $s$ into a character list:
$$
cs = \text{list}(s)
$$

### 2. Dual Boundary Pointers:
Initialize: $i = 0, \quad j = \text{len}(s) - 1$.
While $i < j$:
1. **Advance Left Pointer:**
   While $i < j$ and $cs[i]$ is not a vowel:
   $$
   i \leftarrow i + 1
   $$
2. **Retreat Right Pointer:**
   While $i < j$ and $cs[j]$ is not a vowel:
   $$
   j \leftarrow j - 1
   $$
3. **Swap Vowels:**
   If $i < j$:
   $$
   cs[i], \; cs[j] = cs[j], \; cs[i]
   $$
   $$
   i \leftarrow i + 1, \quad j \leftarrow j - 1
   $$

Return `"".join(cs)`.

> **Invariant.** At every stage, all vowels strictly outside the interval $[i, j]$ have been correctly paired and inverted, while all consonants remain at their initial indices.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"IceCreAm"}$ ($N = 8$):
Initialized: $cs = [\text{'I'}, \text{'c'}, \text{'e'}, \text{'C'}, \text{'r'}, \text{'e'}, \text{'A'}, \text{'m'}]$, $i = 0, j = 7$.

---

### Step 1: First Vowel Pair ($i = 0, j = 7$)
- **Scan Left:**
  - $cs[0] = \text{'I'} \in vowels \implies$ left pointer stays at $i = 0$.
- **Scan Right:**
  - $cs[7] = \text{'m'} \notin vowels \implies j \leftarrow 7 - 1 = 6$.
  - $cs[6] = \text{'A'} \in vowels \implies$ right pointer stops at $j = 6$.
- **Swap:**
  - $i < j \iff 0 < 6$ (**True**).
  - Swap $cs[0]$ (`'I'`) and $cs[6]$ (`'A'`):
    $$
    cs[0], cs[6] \leftarrow \text{'A'}, \text{'I'}
    $$
  - Array state: $[\mathbf{\text{'A'}}, \text{'c'}, \text{'e'}, \text{'C'}, \text{'r'}, \text{'e'}, \mathbf{\text{'I'}}, \text{'m'}]$.
- Advance pointers:
  $$
  i \leftarrow 0 + 1 = 1, \quad j \leftarrow 6 - 1 = 5
  $$

---

### Step 2: Second Vowel Pair ($i = 1, j = 5$)
- **Scan Left:**
  - $cs[1] = \text{'c'} \notin vowels \implies i \leftarrow 1 + 1 = 2$.
  - $cs[2] = \text{'e'} \in vowels \implies$ left pointer stops at $i = 2$.
- **Scan Right:**
  - $cs[5] = \text{'e'} \in vowels \implies$ right pointer stays at $j = 5$.
- **Swap:**
  - $i < j \iff 2 < 5$ (**True**).
  - Swap $cs[2]$ (`'e'`) and $cs[5]$ (`'e'`):
    $$
    cs[2], cs[5] \leftarrow \text{'e'}, \text{'e'}
    $$
  - Array state: $[\text{'A'}, \text{'c'}, \mathbf{\text{'e'}}, \text{'C'}, \text{'r'}, \mathbf{\text{'e'}}, \text{'I'}, \text{'m'}]$.
- Advance pointers:
  $$
  i \leftarrow 2 + 1 = 3, \quad j \leftarrow 5 - 1 = 4
  $$

---

### Step 3: Pointers Cross Between Consonants ($i = 3, j = 4$)
- **Scan Left:**
  - $cs[3] = \text{'C'} \notin vowels \implies i \leftarrow 3 + 1 = 4$.
  - Now $i == j == 4$, inner loop exits.
- **Scan Right:**
  - $cs[4] = \text{'r'} \notin vowels$ and $i \not< j \implies$ inner loop skips.
- Check condition: $i < j \iff 4 < 4$ (**False**).
- No swap performed.
- Outer loop terminates ($i \not< j$).

---

### Step 4: String Reconstruction
Reassemble the character list:
$$
\text{"".join}(cs) = \mathbf{\text{"AceCreIm"}}
$$

---

## 4. Complete Execution Trace

```text
s = "IceCreAm", cs = ['I', 'c', 'e', 'C', 'r', 'e', 'A', 'm']
i = 0, j = 7

Pair 1:
  cs[0] is 'I' (vowel) -> i = 0
  cs[7] is 'm' -> j = 6 ('A' is vowel)
  swap cs[0] and cs[6] -> ['A', 'c', 'e', 'C', 'r', 'e', 'I', 'm']
  i = 1, j = 5

Pair 2:
  cs[1] is 'c' -> i = 2 ('e' is vowel)
  cs[5] is 'e' (vowel) -> j = 5
  swap cs[2] and cs[5] -> ['A', 'c', 'e', 'C', 'r', 'e', 'I', 'm']
  i = 3, j = 4

Pair 3:
  cs[3] is 'C' -> i = 4
  i < j is False -> terminate

Result: "AceCreIm"
```

| Step | Left Index $i$ | Right Index $j$ | Left Char $cs[i]$ | Right Char $cs[j]$ | Action Taken | Array State After Step |
|:---:|:---:|:---:|:---:|:---:|:---|:---|
| Init | 0 | 7 | `'I'` | `'m'` | Initial state | `['I', 'c', 'e', 'C', 'r', 'e', 'A', 'm']` |
| 1 | 0 | 6 | `'I'` | `'A'` | Swap $cs[0] \leftrightarrow cs[6]$ | `['A', 'c', 'e', 'C', 'r', 'e', 'I', 'm']` |
| 2 | 2 | 5 | `'e'` | `'e'` | Swap $cs[2] \leftrightarrow cs[5]$ | `['A', 'c', 'e', 'C', 'r', 'e', 'I', 'm']` |
| **Exit** | **4** | **4** | `'r'` | `'r'` | **$i \ge j \implies$ Terminate** | **`"AceCreIm"`** |

---

## 5. Algorithmic Correctness

**Soundness.** The inner `while` loops skip consonants without mutating them, ensuring non-vowel characters stay strictly at their original positions. Swapping occurs only between confirmed vowels at indices $i < j$. Because each swap mirrors symmetric vowel occurrences from opposite ends of the string, the vowel subsequence is strictly reversed.

**Completeness.** Pointers $i$ and $j$ start at the extreme ends of the string and move monotonically towards each other. Each vowel in the string is visited by exactly one pointer before $i$ and $j$ cross. Since no vowels are skipped, the entire set of vowels is guaranteed to be inverted.

---

## 6. Traps This Instance Exposes

- **Missing Uppercase Vowels:** Forgetting uppercase characters (`'A', 'E', 'I', 'O', 'U'`) in the vowel set causes uppercase vowels to be treated as consonants and skipped.
- **Inner Loop Pointer Out-of-Bounds:** If a string contains no vowels (e.g. `"bcdfg"`), an unconstrained `while cs[i] not in vowels` would increment $i$ past the array length. The guard `while i < j and ...` prevents out-of-bounds errors.
- **Double Swap Guard:** Checking `if i < j:` before swapping is necessary because the inner increments can cause $i$ and $j$ to cross inside the loop body.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = \text{len}(s)$. Converting to a list is $O(N)$. Pointers $i$ and $j$ together visit each index at most once during their inward journey. Rejoining takes $O(N)$. Overall time is strictly $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary space for the mutable character list `cs`.
