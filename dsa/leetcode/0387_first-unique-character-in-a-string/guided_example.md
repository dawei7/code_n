# Guided Example: First Unique Character in a String

We trace the step-by-step two-pass hash map frequency counting (`Counter(s)`), left-to-right index scanning (`for i, c in enumerate(s)`), first-occurrence condition verification (`cnt[c] == 1`), and sentinel failure resolution (`-1`) on representative string instances:

- **Input:** $s = \text{"loveleetcode"}$
- **Required output:** $2$
  - Pass 1 (Global frequency computation):
    - Frequencies: `{'l': 2, 'o': 2, 'v': 1, 'e': 4, 't': 1, 'c': 1, 'd': 1}`
  - Pass 2 (Left-to-right positional scan):
    - $i = 0, c = \text{'l'} \implies cnt[\text{'l'}] = 2 \ne 1$ (Repeated)
    - $i = 1, c = \text{'o'} \implies cnt[\text{'o'}] = 2 \ne 1$ (Repeated)
    - $i = 2, c = \text{'v'} \implies cnt[\text{'v'}] = 1 == 1$ (Unique!)
  - Earliest unique character index is $\mathbf{2}$ (`'v'`)
- **First-Character Unique:** $s = \text{"leetcode"} \implies cnt[\text{'l'}] = 1 \implies 0$
- **No Unique Characters:** $s = \text{"aabb"} \implies$ all counts $\ge 2 \implies -1$

This instance demonstrates decoupling global property aggregation (multiplicity) from order-dependent positional selection (minimum index), avoids quadratic string re-scanning, and achieves $O(N)$ linear time and $O(|\Sigma|) = O(1)$ space complexity.

---

## 1. Instance & Teaching Goal

Given a string $s = \text{"loveleetcode"}$ of lowercase English letters:
Find the **first non-repeating character** in it and return its 0-based index. If none exists, return $-1$:

```text
Input: "loveleetcode"
Indices: 0 1 2 3 4 5 6 7 8 9 10 11
Chars:   l o v e l e e t c o d  e

Character Counts:
  'e': 4,  'l': 2,  'o': 2  (Repeating)
  'v': 1,  't': 1,  'c': 1,  'd': 1  (Unique Candidates)

Left-to-right check:
  Index 0: 'l' -> count 2 -> skip
  Index 1: 'o' -> count 2 -> skip
  Index 2: 'v' -> count 1 -> FIRST UNIQUE FOUND! Return 2
```

### Why a Single Pass Cannot Determine Uniqueness
When inspecting index 0 (`'l'`), an algorithm has seen `'l'` only once so far, but cannot declare it unique because a second `'l'` appears at index 4. Global multiplicity requires scanning the entire string. Separating the process into two passes cleanly solves the problem in $O(N)$ time.

---

## 2. Conceptual Foundation & Invariants

### 1. Two-Pass Architecture:
- **Pass 1 (Aggregation):**
  Scan $s$ from left to right and construct character histogram $cnt$:
  $$
  cnt[c] = \sum_{j=0}^{N-1} \mathbb{I}(s[j] == c) \quad \text{for all } c \in \Sigma
  $$
- **Pass 2 (Earliest Index Selection):**
  Iterate $i$ from $0$ to $N - 1$:
  - If $cnt[s[i]] == 1$:
    Return $i$ immediately.
- **Default Sentinel:**
  If the loop completes without finding any character with count 1, return $-1$.

> **Invariant.** During Pass 2, when visiting index $i$, no prior index $j < i$ satisfied $cnt[s[j]] == 1$. Therefore, the first index satisfying $cnt[s[i]] == 1$ is provably the globally minimal index of a non-repeating character.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"loveleetcode"}$ ($N = 12$):

---

### Step 1: Pass 1 — Frequency Histogram Construction
Traverse $s = \text{"loveleetcode"}$:
- Count occurrences:
  $$
  cnt = \{\text{'e'}: 4, \; \text{'l'}: 2, \; \text{'o'}: 2, \; \text{'v'}: 1, \; \text{'t'}: 1, \; \text{'c'}: 1, \; \text{'d'}: 1\}
  $$

---

### Step 2: Pass 2 — Sequential Index Scan

- **Index $i = 0$, $c = \text{'l'}$:**
  - Query histogram: $cnt[\text{'l'}] = 2$.
  - Condition $cnt[\text{'l'}] == 1$ is **False** ($2 \ne 1$).
  - Advance.

- **Index $i = 1$, $c = \text{'o'}$:**
  - Query histogram: $cnt[\text{'o'}] = 2$.
  - Condition $cnt[\text{'o'}] == 1$ is **False** ($2 \ne 1$).
  - Advance.

- **Index $i = 2$, $c = \text{'v'}$:**
  - Query histogram: $cnt[\text{'v'}] = 1$.
  - Condition $cnt[\text{'v'}] == 1$ is **True**!
  - Character `'v'` is non-repeating throughout the entire string, and index $2$ is the smallest such index.
  - Return:
    $$
    \mathbf{2}
    $$

---

## 4. Complete Execution Trace

```text
s = "loveleetcode"
cnt = Counter({'e': 4, 'l': 2, 'o': 2, 'v': 1, 't': 1, 'c': 1, 'd': 1})

Pass 2:
i=0, c='l', cnt['l']=2 -> continue
i=1, c='o', cnt['o']=2 -> continue
i=2, c='v', cnt['v']=1 -> MATCH FOUND -> Return 2
```

| Pass 2 Index $i$ | Character $s[i]$ | Global Count $cnt[s[i]]$ | Status | Condition $cnt[c] == 1$ | Action Taken |
|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | `'l'` | 2 | Duplicate | False | Skip to $i = 1$ |
| 1 | `'o'` | 2 | Duplicate | False | Skip to $i = 2$ |
| **2** | **'v'** | **1** | **Unique** | **True** | **Terminate & Return `2`** |

---

### Comparison: Sentinel Exit Trace ($s = \text{"aabb"}$)

```text
s = "aabb"
cnt = {'a': 2, 'b': 2}

i=0, c='a', cnt=2 -> continue
i=1, c='a', cnt=2 -> continue
i=2, c='b', cnt=2 -> continue
i=3, c='b', cnt=2 -> continue
Loop exhausted -> Return -1
```

---

## 5. Algorithmic Correctness

**Soundness.** A character is non-repeating if and only if its total frequency in the string is 1. The condition $cnt[s[i]] == 1$ accurately identifies all indices corresponding to unique characters. Because Pass 2 checks indices $i$ in strictly increasing order ($0, 1, 2, \dots$), returning upon the first match guarantees that the returned index is the minimal valid index.

**Completeness.** If a unique character exists, its index will be tested during Pass 2. If no unique character exists, all characters will have $cnt[c] \ge 2$, the loop will terminate naturally, and the function will return $-1$, ensuring complete coverage of all inputs.

---

## 6. Traps This Instance Exposes

- **Repeated Linear Search (`s.count(c)`):** Writing `if s.count(c) == 1:` inside a loop scans the string for each character, resulting in $O(N^2)$ quadratic runtime, which TLEs on large strings.
- **Fixed Array vs Hash Table:** Because the alphabet is limited to 26 lowercase English letters, a fixed array `int[26]` indexed by `ord(c) - ord('a')` runs with zero dynamic allocation overhead.
- **Returning the Character vs Returning the Index:** The problem explicitly requires returning the **index** $i$, not the character $c$ itself.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of string $s$.
  - Pass 1 takes $O(N)$ time to count frequencies.
  - Pass 2 takes at most $O(N)$ time to find the first unique character.
  - Overall time is strictly $O(N)$, running in under 5 ms for $N \le 10^5$.
- **Auxiliary Space Complexity:** $O(|\Sigma|) = O(1)$, where $|\Sigma| \le 26$ for the lowercase English alphabet, requiring constant extra memory.
