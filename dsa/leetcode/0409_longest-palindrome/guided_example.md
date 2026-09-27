# Guided Example: Longest Palindrome

We trace the step-by-step multiset frequency aggregation (`Counter(s)`), maximal symmetric pair harvesting ($v \mathbin{//} 2 \times 2$), center pivot allocation ($ans < |s| \implies +1$), and case-sensitive parity algebra on representative string instances:

- **Input:** $s = \text{"abccccdd"}$
- **Required output:** `7`
  - Total string length: $|s| = 8$
  - Step 1 (Count character frequencies):
    - `'a'`: $1$
    - `'b'`: $1$
    - `'c'`: $4$
    - `'d'`: $2$
  - Step 2 (Harvest paired contributions $v \mathbin{//} 2 \times 2$):
    - `'a'`: $\lfloor 1 / 2 \rfloor \times 2 = 0$
    - `'b'`: $\lfloor 1 / 2 \rfloor \times 2 = 0$
    - `'c'`: $\lfloor 4 / 2 \rfloor \times 2 = 4$
    - `'d'`: $\lfloor 2 / 2 \rfloor \times 2 = 2$
    - Paired sum: $ans = 0 + 0 + 4 + 2 = \mathbf{6}$
  - Step 3 (Center odd pivot check):
    - Total characters used in pairs: $6$
    - Total available characters: $|s| = 8$
    - Since $ans < |s|$ ($6 < 8$), at least one unused character exists (either `'a'` or `'b'`)
    - One character can sit at the exact center of the palindrome
    - Center bonus: $ans \leftarrow 6 + 1 = \mathbf{7}$
  - Longest palindrome length: $\mathbf{7}$ (e.g. `"dccaccd"`)
- **All Characters Paired:** $s = \text{"aabb"} \implies ans = 4, |s| = 4 \implies$ no center $\implies \mathbf{4}$
- **Single Character:** $s = \text{"a"} \implies ans = 0, |s| = 1 \implies 0 + 1 = \mathbf{1}$
- **Case Sensitivity:** $s = \text{"Aa"} \implies \text{counts } A:1, a:1 \implies$ paired $= 0$, center $= 1 \implies \mathbf{1}$

This instance demonstrates multiset parity optimization, mathematically proves why all even components can be mirrored bilaterally around at most one central odd element, and derives $O(N)$ runtime and $O(|\Sigma|)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string $s = \text{"abccccdd"}$ containing lowercase and uppercase English letters:
Find the length of the **longest palindrome** that can be constructed by rearranging its characters:

```text
Available Characters:
  'a': 1   'b': 1   'c': 4   'd': 2

Symmetric Assembly:
  Left Wing:   d  c  c
  Center:         a        (or 'b')
  Right Wing:  c  c  d

Full Palindrome: "dccaccd" (Length 7)
```

### The Palindrome Symmetry Invariant
A string is a palindrome if and only if it reads identically forwards and backwards.
- Every position $i$ must match position $L - 1 - i$.
- For any character not at the exact center, each occurrence on the left side must be matched by a corresponding identical occurrence on the right side. Thus, characters must be consumed in **pairs** of two.
- If the palindrome has odd length, exactly **one single character** can occupy the center without a matching partner.

---

## 2. Conceptual Foundation & Invariants

### 1. The Paired Capacity Formula:
For any character with frequency $v$:
- The number of complete pairs is $\lfloor v / 2 \rfloor$.
- The number of characters that can be placed symmetrically is:
  $$
  \text{paired}(v) = \lfloor v / 2 \rfloor \times 2 = v - (v \bmod 2)
  $$
- Summing over all distinct characters in the alphabet gives the maximum even-length palindrome:
  $$
  ans = \sum_{c \in \Sigma} \left( \lfloor \text{count}(c) / 2 \rfloor \times 2 \right)
  $$

### 2. The Center Pivot Rule:
- If $ans < |s|$, at least one character had an odd frequency and was left over ($v \bmod 2 = 1$).
- Any single leftover character can be placed at the center of the palindrome:
  $$
  ans \leftarrow ans + 1
  $$
- If $ans == |s|$, every single character in the input string was already matched into pairs. No leftover character exists to serve as an additional center.

> **Invariant.** The length of the longest palindrome equals the sum of all maximal even sub-frequencies, augmented by 1 if and only if at least one character has an odd frequency.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"abccccdd"}$:
Total length: $|s| = 8$.

---

### Step 1: Count Frequencies
Construct frequency histogram:
$$
cnt = \{\text{'a'}: 1, \; \text{'b'}: 1, \; \text{'c'}: 4, \; \text{'d'}: 2\}
$$

---

### Step 2: Sum Even Paired Contributions
Evaluate each character's contribution $\lfloor v / 2 \rfloor \times 2$:
- Character `'a'` ($v = 1$):
  $$
  1 \mathbin{//} 2 \times 2 = 0 \times 2 = \mathbf{0}
  $$
- Character `'b'` ($v = 1$):
  $$
  1 \mathbin{//} 2 \times 2 = 0 \times 2 = \mathbf{0}
  $$
- Character `'c'` ($v = 4$):
  $$
  4 \mathbin{//} 2 \times 2 = 2 \times 2 = \mathbf{4}
  $$
- Character `'d'` ($v = 2$):
  $$
  2 \mathbin{//} 2 \times 2 = 1 \times 2 = \mathbf{2}
  $$
Aggregate even baseline:
$$
ans = 0 + 0 + 4 + 2 = \mathbf{6}
$$

---

### Step 3: Evaluate Center Availability
Compare $ans$ with total string length $|s|$:
$$
ans < \text{len}(s) \iff 6 < 8 \quad (\mathbf{True})
$$
- Converting Boolean `True` to integer yields `1`.
- Add central pivot:
  $$
  ans \leftarrow 6 + 1 = \mathbf{7}
  $$

---

### Step 4: Termination
Return:
$$
\mathbf{7}
$$

---

## 4. Complete Execution Trace

```text
s = "abccccdd", len(s) = 8

Frequencies: {'a': 1, 'b': 1, 'c': 4, 'd': 2}

'a': 1 // 2 * 2 = 0
'b': 1 // 2 * 2 = 0
'c': 4 // 2 * 2 = 4
'd': 2 // 2 * 2 = 2

Even Sum ans = 0 + 0 + 4 + 2 = 6
Condition ans < len(s): 6 < 8 (True -> 1)
ans = 6 + 1 = 7

Output: 7
```

| Character | Frequency $v$ | Full Pairs $\lfloor v/2 \rfloor$ | Paired Letters Added ($v \mathbin{//} 2 \times 2$) | Leftover Odd Letter? | Running Paired Sum |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `'a'` | 1 | 0 | 0 | Yes (1 leftover) | 0 |
| `'b'` | 1 | 0 | 0 | Yes (1 leftover) | 0 |
| `'c'` | 4 | 2 | 4 | No | 4 |
| `'d'` | 2 | 1 | 2 | No | 6 |
| **Pivot** | - | - | **$+1$ (Center)** | - | **$\mathbf{7}$ (Final)** |

---

## 5. Algorithmic Correctness

**Soundness.** Every character paired by $\lfloor v / 2 \rfloor \times 2$ can be placed symmetrically on opposite sides of the string. A palindrome can contain at most one character with odd multiplicity (the center). Thus, taking all available pairs plus at most one single central character achieves the theoretical upper bound on palindrome length.

**Completeness.** Every character in $s$ is processed. The condition $ans < |s|$ holds if and only if $\sum (v \bmod 2) > 0$. If any odd character exists, choosing any one of them as the center is valid, guaranteeing that the maximum possible length is achieved.

---

## 6. Traps This Instance Exposes

- **Case Sensitivity:** `'A'` and `'a'` are distinct characters. Treating them as identical would falsely combine them into a pair. Using Python's `Counter(s)` preserves exact ASCII character keys.
- **Multiple Odd Characters:** If multiple characters have odd counts (e.g. `'a': 1, 'b': 1`), only **ONE** of them can be used in the center. The remaining odd characters can only contribute their even parts ($\lfloor v / 2 \rfloor \times 2$).
- **Permutation vs Substring:** The problem allows reordering characters arbitrarily (subsequence multiset), NOT finding a contiguous substring. Generating permutations or searching substrings would cause severe time-limit errors.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = \text{len}(s)$.
  - Counting characters in $s$ takes $O(N)$ time.
  - Summing over the hash table values takes $O(|\Sigma|)$ time, where $|\Sigma| \le 52$ (26 lowercase + 26 uppercase English letters).
  - Total time is strictly $O(N + |\Sigma|) = O(N)$, finishing in $< 0.1$ ms.
- **Auxiliary Space Complexity:** $O(|\Sigma|) = O(1)$ constant memory, storing at most 52 frequency entries in `Counter(s)`.
