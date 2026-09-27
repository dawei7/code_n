# Guided Example: Rotated Digits

We trace the step-by-step 180-degree digit rotation mapping, digit validity categorization (valid-neutral vs valid-inverting vs invalid), base-10 digit decomposition, non-identity rotation check ($y \ne x$), and good number counting in the range $[1, n]$ on representative integer intervals:

- **Input:** $n = 10$
- **Required output:** `4`
  - Digit rotation specifications (180-degree rotation):
    - Each digit rotates individually into another digit or becomes invalid:
      1. **Self-Symmetric Digits (Rotate to Themselves):**
         - $0 \to 0$
         - $1 \to 1$
         - $8 \to 8$
      2. **Mutually Inverting Digits (Rotate to a Different Valid Digit):**
         - $2 \leftrightarrow 5$
         - $6 \leftrightarrow 9$
      3. **Invalid Digits (Do Not Form a Valid Digit):**
         - $3, 4, 7 \to \text{Invalid}$
    - **Good Number Definition:**
      - An integer $x$ is **good** if and only if:
        1. **Validity:** Every single digit of $x$ belongs to $\{0, 1, 8, 2, 5, 6, 9\}$ (contains **no** $3, 4, 7$).
        2. **Transformation:** The rotated number $y$ is **strictly different** from $x$ ($y \ne x$).
    - For $n = 10$:
      - $1 \to 1$ (Same $\implies$ Not Good)
      - $2 \to 5$ (Different $\implies$ **Good #1**)
      - $3, 4 \to$ Invalid
      - $5 \to 2$ (Different $\implies$ **Good #2**)
      - $6 \to 9$ (Different $\implies$ **Good #3**)
      - $7 \to$ Invalid
      - $8 \to 8$ (Same $\implies$ Not Good)
      - $9 \to 6$ (Different $\implies$ **Good #4**)
      - $10 \to 10$ (Same $\implies$ Not Good)
      - Total good numbers in $[1, 10]$: **4**.
- **Digit Classification Partition Invariant:**
  - **The Three Digit Subsets:**
    - Partition the ten decimal digits into three disjoint sets:
      $$
      S_{\text{invalid}} = \{3, 4, 7\}
      $$
      $$
      S_{\text{same}} = \{0, 1, 8\}
      $$
      $$
      S_{\text{diff}} = \{2, 5, 6, 9\}
      $$
  - **The Necessary and Sufficient Good Number Rule:**
    - An integer $x$ is good if and only if:
      1. It contains **no digits** from $S_{\text{invalid}}$:
         $$
         \forall d \in \text{digits}(x): \quad d \notin \{3, 4, 7\}
         $$
      2. It contains **at least one digit** from $S_{\text{diff}}$:
         $$
         \exists d \in \text{digits}(x): \quad d \in \{2, 5, 6, 9\}
         $$
    - If a number consists purely of digits from $S_{\text{same}}$ (e.g. $8018$), every digit rotates to itself, so the rotated number equals the original ($y = x$), which fails the non-identity requirement!
- **Step-by-Step Worked Execution Trace on Range $[1, 10]$:**
  - Let rotation lookup map be:
    $$
    d = [0, 1, 5, -1, -1, 2, 9, -1, 8, 6]
    $$
  - Initialize good counter: $ans = 0$.
  - **Evaluate $x = 1$:**
    - Digits: $[1]$. Rotates to $[1]$. $1 == 1 \implies$ Not good.
  - **Evaluate $x = 2$:**
    - Digits: $[2]$. Rotates to $[5]$.
    - Valid and $5 \ne 2 \implies \mathbf{Good\ Number!}$
    - Increment: $ans \leftarrow 0 + 1 = \mathbf{1}$.
  - **Evaluate $x = 3$:**
    - Digit $3 \in S_{\text{invalid}} \implies$ Invalid.
  - **Evaluate $x = 4$:**
    - Digit $4 \in S_{\text{invalid}} \implies$ Invalid.
  - **Evaluate $x = 5$:**
    - Digits: $[5]$. Rotates to $[2]$.
    - Valid and $2 \ne 5 \implies \mathbf{Good\ Number!}$
    - Increment: $ans \leftarrow 1 + 1 = \mathbf{2}$.
  - **Evaluate $x = 6$:**
    - Digits: $[6]$. Rotates to $[9]$.
    - Valid and $9 \ne 6 \implies \mathbf{Good\ Number!}$
    - Increment: $ans \leftarrow 2 + 1 = \mathbf{3}$.
  - **Evaluate $x = 7$:**
    - Digit $7 \in S_{\text{invalid}} \implies$ Invalid.
  - **Evaluate $x = 8$:**
    - Digits: $[8]$. Rotates to $[8]$. $8 == 8 \implies$ Not good.
  - **Evaluate $x = 9$:**
    - Digits: $[9]$. Rotates to $[6]$.
    - Valid and $6 \ne 9 \implies \mathbf{Good\ Number!}$
    - Increment: $ans \leftarrow 3 + 1 = \mathbf{4}$.
  - **Evaluate $x = 10$:**
    - Digits: $1 \to 1, 0 \to 0$. Rotates to $10$.
    - $10 == 10 \implies$ Not good.
  - **Termination:**
    - Range $[1, 10]$ completed.
    - Total good numbers:
      $$
      ans = \mathbf{4}
      $$
- **Multi-Digit Mixed Number Trace ($x = 20$ and $x = 88$):**
  - $x = 20$:
    - Digit 0 rotates to 0.
    - Digit 2 rotates to 5.
    - Rotated number: $50 \ne 20 \implies$ **Good**.
  - $x = 88$:
    - Digit 8 rotates to 8.
    - Rotated number: $88 == 88 \implies$ **Not Good**.
- **Boundaries ($n = 1$):**
  - Only $x = 1$ is tested $\implies$ returns **`0`**.

This instance demonstrates base-10 digit alphabet projection and dihedral rotation symmetry validation, mathematically proves why inclusion of inverting letters without illegal letters partitions the valid formal language, and derives $O(N \log_{10} N)$ runtime and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an integer $n$:
Count how many numbers in $[1, n]$ are **good** (rotate 180 degrees to a valid number that is **different** from the original).

```text
Rotation rules:
  0 -> 0, 1 -> 1, 8 -> 8 (same)
  2 -> 5, 5 -> 2 (differs)
  6 -> 9, 9 -> 6 (differs)
  3, 4, 7 -> INVALID!

Range [1, 10]:
  Good numbers: 2, 5, 6, 9 (all rotate to different valid digits!)
  Not good: 1, 8, 10 (rotate to same number)
  Invalid: 3, 4, 7

Result: 4
```

### The Invariant of the Digit Partition
A number is good $\iff$
1. It contains **no** $\{3, 4, 7\}$.
2. It contains **at least one** $\{2, 5, 6, 9\}$.
3. All other digits are $\{0, 1, 8\}$.

---

## 2. Conceptual Foundation & Invariants

### 1. Digit Rotation Vector:
$$
d = [0, 1, 5, -1, -1, 2, 9, -1, 8, 6]
$$

### 2. Good Number Predicate:
$$
\text{isGood}(x) \iff \Big( \forall c \in x: d[c] \ne -1 \Big) \;\land\; \Big( \text{rotate}(x) \ne x \Big)
$$
$$
ans = \sum_{x = 1}^n \text{isGood}(x)
$$

> **Dihedral Semigroup Action Invariant.** Let $\rho: \mathbb{Z}_{10} \to \mathbb{Z}_{10} \cup \{\bot\}$ be the planar half-turn map. The good words $\mathcal{L}_{\text{good}} \subseteq \mathbb{Z}_{10}^*$ are the regular language $(\{0, 1, 8\} \cup \{2, 5, 6, 9\})^* \setminus \{0, 1, 8\}^*$, decidable in linear time over string length.

---

## 3. Step-by-Step Worked Execution

We trace range $[1, 10]$:

---

### Step 1: Digits 1 to 5
- $1 \to 1$ (Same)
- $2 \to 5$ (Good #1)
- $3, 4$ (Invalid)
- $5 \to 2$ (Good #2)

---

### Step 2: Digits 6 to 10
- $6 \to 9$ (Good #3)
- $7$ (Invalid)
- $8 \to 8$ (Same)
- $9 \to 6$ (Good #4)
- $10 \to 10$ (Same)

---

### Step 3: Output
- Count: **`4`**.

---

## 4. Complete Execution Trace

| Integer $x$ | Digits | Rotated Form $y$ | Valid? | Different? ($x \ne y$) | Good Number? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | `1` | `1` | Yes | No | No |
| $2$ | `2` | `5` | Yes | Yes | **Yes** |
| $3$ | `3` | — | No | — | No |
| $4$ | `4` | — | No | — | No |
| $5$ | `5` | `2` | Yes | Yes | **Yes** |
| $6$ | `6` | `9` | Yes | Yes | **Yes** |
| $7$ | `7` | — | No | — | No |
| $8$ | `8` | `8` | Yes | No | No |
| **$9$** | **`9`** | **`6`** | **Yes** | **Yes** | **Yes** |
| $10$ | `1, 0` | `10` | Yes | No | No |
| **Total** | — | — | — | — | **`4`** |

---

## 5. Boundary Cases & Failure Modes

- **$n = 1$:** 1 rotates to 1 $\implies$ returns 0.
- **Pure Self-Symmetric ($888, 108$):** All digits valid, but rotated number equals original $\implies$ not good.
- **Numbers Containing 3, 4, 7 (e.g. 23):** Contains valid '2', but '3' invalidates the whole number $\implies$ not good.
- **Max $N = 10^4$:** Takes at most $10^4 \times 5$ digit operations; completes in $< 5$ ms.

---

## 6. Traps & Common Anti-Patterns

- **Rotating the Entire Number as a String instead of Individual Digits:** Digits rotate in place; they do not reverse position! (Problem says: "rotate each digit individually by 180 degrees").
- **Counting Self-Symmetric Numbers as Good:** Forgetting condition $y \ne x$ mistakenly counts 1, 8, 11, 88 as good numbers.
- **Digit DP Overkill:** While Digit DP works for $N \le 10^9$, for $N \le 10^4$ direct simulation per integer is simple, bug-free, and runs in $< 5$ ms.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Checking each integer $x \in [1, n]$ takes $\mathcal{O}(\log_{10} x)$ digit extractions.
  - Total Time: $\mathcal{O}(N \log_{10} N)$ where $N \le 10^4 \implies \le 4 \times 10^4$ operations. Completes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space.