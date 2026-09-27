# Guided Example: Palindrome Pairs

We trace the step-by-step prefix/suffix partition scanning ($w[:j]$ and $w[j:]$), reverse slice dictionary indexing ($O(1)$ complement lookups), asymmetric palindrome core verification ($a == ra$ or $b == rb$), and valid ordered index pair generation on representative string arrays:

- **Input:**
  $$
  \text{words} = [\text{"abcd"}, \text{"dcba"}, \text{"lls"}, \text{"s"}, \text{"sssll"}]
  $$
- **Required output:** `[[0, 1], [1, 0], [3, 2], [2, 4]]`
  - Pair `[0, 1]`: `"abcd" + "dcba" = "abcddcba"` (Equal-length full reversals)
  - Pair `[1, 0]`: `"dcba" + "abcd" = "dcbaabcd"` (Equal-length full reversals)
  - Pair `[3, 2]`: `"s" + "lls" = "slls"` (Short word pairs with prefix of `"lls"`)
  - Pair `[2, 4]`: `"lls" + "sssll" = "llssssll"` (Short word pairs with suffix of `"sssll"`)
- **Empty String Partner Base Case:** If `""` exists in `words`, every word that is itself a palindrome forms two pairs: `[i, empty_idx]` and `[empty_idx, i]`
- **Self-Pairing Guard:** A word cannot pair with itself ($d[ra] \ne i$) even if the word is an internal palindrome (e.g. `"aba"`)

This instance demonstrates word split decomposition for palindrome search, mathematically proves why splitting each word into prefix $a$ and suffix $b$ captures all unequal-length palindrome concatenations in $O(N \cdot K^2)$ time instead of $O(N^2 \cdot K)$, and analyzes $O(N \cdot K)$ auxiliary dictionary memory bounds.

---

## 1. Instance & Teaching Goal

Given an array of unique strings:
$$
\text{words} = [\text{"abcd"}, \text{"dcba"}, \text{"lls"}, \text{"s"}, \text{"sssll"}] \quad (N = 5)
$$
Find all pairs of distinct indices $(i, j)$ ($i \ne j$) such that the concatenated string:
$$
\text{words}[i] + \text{words}[j]
$$
is a palindrome (reads the same forwards and backwards).

```text
Concatenations Formed:
- [0, 1]: "abcd"  + "dcba"  = "abcddcba"   (PALINDROME)
- [1, 0]: "dcba"  + "abcd"  = "dcbaabcd"   (PALINDROME)
- [2, 4]: "lls"   + "sssll" = "llssssll"   (PALINDROME)
- [3, 2]: "s"     + "lls"   = "slls"       (PALINDROME)

All other pairs (e.g. "abcdlls") are non-palindromic.
```

### Why Pairwise Concatenation ($O(N^2 K)$) Fails
- For $N = 30,000$ words of average length $K = 10$, evaluating all $N^2 = 9 \times 10^8$ pairs takes prohibitively long and results in Time Limit Exceeded.
- **The Word-Split Principle:**
  Instead of comparing word $i$ against all other $N-1$ words, we split word $i$ into prefix $a$ and suffix $b$.
  A valid partner must be the reverse of either $a$ or $b$.
  Using a hash table mapping $\text{word} \to \text{index}$, we perform $O(K)$ targeted queries per word!

---

## 2. Conceptual Foundation & Invariants

### 1. Hash Table Initialization
Precompute dictionary $d$:
$$
d = \{w: i \text{ for } i, w \in \text{enumerate}(\text{words})\}
$$

### 2. Prefix and Suffix Decomposition
For each word $w$ of length $L$ at index $i$:
Iterate split point $j \in [0, L]$:
- $a = w[:j]$ (prefix) with reverse $ra = a[::-1]$
- $b = w[j:]$ (suffix) with reverse $rb = b[::-1]$

### 3. The Two Concatenation Configurations:

#### Configuration 1: Word $w$ on the Left ($w + \text{partner}$)
$$
w + ra = a + b + ra
$$
If suffix $b$ is an internal palindrome ($b == rb$) and $ra \in d$ with $d[ra] \ne i$:
- The outer portions $a$ and $ra$ mirror each other.
- The inner portion $b$ mirrors itself.
- Therefore $w + ra$ is a palindrome!
- Action: `ans.append([i, d[ra]])`.

#### Configuration 2: Word $w$ on the Right ($\text{partner} + w$)
$$
rb + w = rb + a + b
$$
If prefix $a$ is an internal palindrome ($a == ra$) and $rb \in d$ with $d[rb] \ne i$:
- The outer portions $rb$ and $b$ mirror each other.
- The inner portion $a$ mirrors itself.
- Therefore $rb + w$ is a palindrome!
- Guard: Check $j > 0$ to prevent duplicate pair addition when $j = 0$ (handled by Configuration 1).
- Action: `ans.append([d[rb], i])`.

> **Invariant.** For every split position $j$, whenever a sub-slice is a self-contained palindrome, the only string that can complete the palindrome is the reverse of the remaining sub-slice.

---

## 3. Step-by-Step Worked Execution

We trace words: `["abcd", "dcba", "lls", "s", "sssll"]`:
Dictionary $d = \{\text{"abcd"}: 0, \text{"dcba"}: 1, \text{"lls"}: 2, \text{"s"}: 3, \text{"sssll"}: 4\}$.

---

### Step 1: $i = 0, w = \text{"abcd"}$
Length $L = 4$.
- At $j = 4$:
  - $a = \text{"abcd"}, b = \text{""}$.
  - $ra = \text{"dcba"}, rb = \text{""}$.
  - Suffix $b = \text{""}$ is a palindrome ($b == rb$).
  - Is $ra = \text{"dcba"} \in d$? **Yes!** $d[\text{"dcba"}] = 1 \ne 0$.
  - **Pair found:** `[0, 1]` (`"abcd" + "dcba" = "abcddcba"`).

---

### Step 2: $i = 1, w = \text{"dcba"}$
Length $L = 4$.
- At $j = 4$:
  - $a = \text{"dcba"}, b = \text{""}$.
  - $ra = \text{"abcd"}, rb = \text{""}$.
  - Suffix $b = \text{""}$ is a palindrome.
  - Is $ra = \text{"abcd"} \in d$? **Yes!** $d[\text{"abcd"}] = 0 \ne 1$.
  - **Pair found:** `[1, 0]` (`"dcba" + "abcd" = "dcbaabcd"`).

---

### Step 3: $i = 2, w = \text{"lls"}$
Length $L = 3$.
- At $j = 2$:
  - $a = \text{"ll"}, b = \text{"s"}$.
  - $ra = \text{"ll"}, rb = \text{"s"}$.
  - Check Config 1: $b = \text{"s"}$ is palindrome ($b == rb$). But $ra = \text{"ll"} \notin d$.
  - Check Config 2 ($j = 2 > 0$):
    - Is prefix $a = \text{"ll"}$ a palindrome? **Yes!** $a == ra$.
    - Is $rb = \text{"s"} \in d$? **Yes!** $d[\text{"s"}] = 3 \ne 2$.
    - **Pair found:** `[d[rb], i] = [3, 2]`!
    - Validation: $\text{words}[3] + \text{words}[2] = \text{"s"} + \text{"lls"} = \text{"slls"}$ (Palindrome!).

---

### Step 4: $i = 3, w = \text{"s"}$
Length $L = 1$.
- $j = 0$ and $j = 1$ find reverse `"s"`, which is $i = 3$ (self-match $d[ra] == i$, skipped).

---

### Step 5: $i = 4, w = \text{"sssll"}$
Length $L = 5$.
- At $j = 2$:
  - $a = \text{"ss"}, b = \text{"sll"}$.
  - $ra = \text{"ss"}, rb = \text{"lls"}$.
  - Check Config 2 ($j = 2 > 0$):
    - Is prefix $a = \text{"ss"}$ a palindrome? **Yes!** $a == ra$.
    - Is $rb = \text{"lls"} \in d$? **Yes!** $d[\text{"lls"}] = 2 \ne 4$.
    - **Pair found:** `[d[rb], i] = [2, 4]`!
    - Validation: $\text{words}[2] + \text{words}[4] = \text{"lls"} + \text{"sssll"} = \text{"llssssll"}$ (Palindrome!).

---

### Step 6: Final Pairs Extracted
$$
\mathbf{[[0, 1], [1, 0], [3, 2], [2, 4]]}
$$

---

## 4. Complete Execution Trace

```text
words = ["abcd", "dcba", "lls", "s", "sssll"]
d = {"abcd": 0, "dcba": 1, "lls": 2, "s": 3, "sssll": 4}

w = "abcd" (i=0):
  j = 4: a="abcd", b="", ra="dcba" in d -> ans.append([0, 1])

w = "dcba" (i=1):
  j = 4: a="dcba", b="", ra="abcd" in d -> ans.append([1, 0])

w = "lls" (i=2):
  j = 2: a="ll", b="s", a is pal ("ll"), rb="s" in d -> ans.append([3, 2])

w = "sssll" (i=4):
  j = 2: a="ss", b="sll", a is pal ("ss"), rb="lls" in d -> ans.append([2, 4])

Result: [[0, 1], [1, 0], [3, 2], [2, 4]]
```

| Active Word $w$ | Word Index $i$ | Split $j$ | Prefix $a$ | Suffix $b$ | Palindrome Sub-slice | Matching Reverse in $d$? | Partner Index | Pair Appended | Concatenated String |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| `"abcd"` | 0 | 4 | `"abcd"` | `""` | $b = \text{""}$ | `"dcba"` | 1 | `[0, 1]` | `"abcddcba"` |
| `"dcba"` | 1 | 4 | `"dcba"` | `""` | $b = \text{""}$ | `"abcd"` | 0 | `[1, 0]` | `"dcbaabcd"` |
| `"lls"` | 2 | 2 | `"ll"` | `"s"` | $a = \text{"ll"}$ | $rb = \text{"s"}$ | 3 | `[3, 2]` | `"slls"` |
| `"sssll"` | 4 | 2 | `"ss"` | `"sll"` | $a = \text{"ss"}$ | $rb = \text{"lls"}$ | 2 | `[2, 4]` | `"llssssll"` |

---

## 5. Algorithmic Correctness

**Soundness.** For two strings $w_1$ and $w_2$ to concatenate into a palindrome $w_1 + w_2$, one string must be shorter than or equal to the other. If $w_1$ is longer, it can be decomposed as $w_1 = a + b$, where $a = \text{reverse}(w_2)$ and $b$ is a standalone palindrome. If $w_2$ is longer, it decomposes as $w_2 = b + c$, where $c = \text{reverse}(w_1)$ and $b$ is a standalone palindrome. Testing all prefix/suffix splits of every word exhaustively evaluates both geometric orientations.

**Completeness.** Every word is split at all possible boundary positions $j \in [0, \text{len}(w)]$. Any valid pair $(i, j)$ in the input satisfies either $|w_i| \le |w_j|$ or $|w_j| \le |w_i|$. Since the longer word's split loop encounters the required sub-palindrome slice, looking up the remaining slice's reverse in hash table $d$ guarantees discovering every valid pair without omissions or duplicates.

---

## 6. Traps This Instance Exposes

- **Duplicate Pair from $j = 0$:** When $j = 0$, $a = \text{""}$. If both Config 1 and Config 2 were evaluated without the $j > 0$ check, the same equal-length reverse pair would be added twice. The condition `if j and ...` prevents duplicate entries.
- **Self-Pairing with Palindromes:** Words like `"aba"` or `"s"` have $ra == w$. Checking $d[ra] \ne i$ ensures a word does not pair with itself.
- **Empty String Word:** If `""` is present, it matches any word that is itself a palindrome. Splitting at $j = 0$ and $j = L$ naturally discovers both `[i, empty]` and `[empty, i]`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot K^2)$, where $N = \text{len}(words)$ and $K$ is the maximum word length.
  - Building dictionary $d$: $O(N \cdot K)$.
  - Outer loop runs $N$ times.
  - Inner split loop runs $K + 1$ times. Slicing and checking palindrome properties take $O(K)$ per split.
  - Total runtime is $O(N \cdot K^2)$, which is vastly faster than $O(N^2 \cdot K)$ for large $N$.
- **Auxiliary Space Complexity:** $O(N \cdot K)$ auxiliary memory to store words in hash table $d$ and substrings during slice operations.
