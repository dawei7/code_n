# Guided Example: Find the Closest Palindrome

We trace the step-by-step 5-point candidate generation space, prefix extraction ($left = \lfloor (l+1)/2 \rfloor$), three-variant prefix reflection ($left - 1, left, left + 1$), boundary length-shift transitions ($10^{l-1} - 1, 10^l + 1$), self-exclusion ($res.\text{discard}(x)$), and minimal distance tie-breaking ($\min |t - x|, \min t$) on representative integer strings:

- **Input:** $n = \text{"123"}$
- **Required output:** `"121"`
  - Problem objective: Find the palindromic integer closest in numerical value to $n$ (excluding $n$ itself).
  - Tie-breaking: If two distinct palindromes have the identical absolute difference $|t - x|$, select the **smaller** palindrome.
- **The 5 Candidate Palindrome Classes:**
  - Let $l = \text{len}(n)$ and $x = \text{int}(n)$.
  - Any palindrome minimizing $|t - x|$ must belong to one of 5 canonical candidates:
    1. **Boundary Below (Length $l - 1$):** $10^{l-1} - 1$ (e.g. $99$ for $l = 3$). Handles downward digit-length collapses (like $1000 \to 999$).
    2. **Boundary Above (Length $l + 1$):** $10^l + 1$ (e.g. $1001$ for $l = 3$). Handles upward digit-length expansions (like $999 \to 1001$).
    3. **Same Prefix Reflected:** Mirroring the first $\lceil l/2 \rceil$ digits directly.
    4. **Decremented Prefix Reflected ($left - 1$):** Handles cases where decreasing the center produces a closer lower palindrome (e.g. $120 \to 111$).
    5. **Incremented Prefix Reflected ($left + 1$):** Handles cases where increasing the center produces a closer higher palindrome (e.g. $129 \to 131$).
- **Candidate Evaluation Trace on $n = \text{"123"}$ ($l = 3, \; x = 123$):**
  - **Step 1: Prefix Extraction:**
    - Prefix length: $\lceil 3 / 2 \rceil = 2$ digits.
    - First two digits:
      $$
      left = 12
      $$
  - **Step 2: Generate Reflected Prefix Variants ($left - 1, left, left + 1$):**
    - Since $l = 3$ is odd, the middle digit (the last digit of $left$) is shared and not repeated in the mirror:
      - **Variant A ($left - 1 = 11$):**
        - Middle digit: $1$. Suffix to mirror: $1$.
        - Number formed: $11 \cdot 1 \implies \mathbf{111}$.
      - **Variant B ($left = 12$):**
        - Middle digit: $2$. Suffix to mirror: $1$.
        - Number formed: $12 \cdot 1 \implies \mathbf{121}$.
      - **Variant C ($left + 1 = 13$):**
        - Middle digit: $3$. Suffix to mirror: $1$.
        - Number formed: $13 \cdot 1 \implies \mathbf{131}$.
  - **Step 3: Generate Boundary Candidates:**
    - Boundary below ($l - 1 = 2$ digits):
      $$
      10^{3-1} - 1 = 10^2 - 1 = \mathbf{99}
      $$
    - Boundary above ($l + 1 = 4$ digits):
      $$
      10^3 + 1 = 1000 + 1 = \mathbf{1001}
      $$
  - **Step 4: Form Candidate Pool & Exclude $x$:**
    $$
    res = \{99, \; 111, \; 121, \; 131, \; 1001\}
    $$
    - Self-exclusion: $123 \notin res$ (no deletion needed).
  - **Step 5: Compare Distances to Target $x = 123$:**
    - For $t = 99$: $|99 - 123| = 24$
    - For $t = 111$: $|111 - 123| = 12$
    - For $t = 121$: $|121 - 123| = \mathbf{2}$ (**Minimal distance!**)
    - For $t = 131$: $|131 - 123| = 8$
    - For $t = 1001$: $|1001 - 123| = 878$
  - The closest palindrome is $121$ with an absolute difference of $2$.
  - Return: **`"121"`**.
- **Tie-Breaking Demonstration ($n = \text{"1"}$):**
  - $x = 1, l = 1$.
  - Candidates: $10^0 - 1 = 0$, $10^1 + 1 = 11$, and $left \pm 1 \implies \{0, 2\}$.
  - Discard $1 \implies res = \{0, 2, 11\}$.
  - Distances: $|0 - 1| = 1$, $|2 - 1| = 1$.
  - Both differences equal $1$. Tie-break chooses the **smaller value**: $\min(0, 2) = \mathbf{\text{"0"}}$.
- **All Nines Boundary Crossing ($n = \text{"99"}$):**
  - $x = 99$. Discarding $99$ leaves candidates $9$ and $101$.
  - $|9 - 99| = 90$, $|101 - 99| = 2 \implies \mathbf{\text{"101"}}$.

This instance demonstrates candidate set bounding in combinatorial arithmetic, mathematically proves why exactly 5 structural palindrome classes cover all possible minimum-distance scenarios, and derives $O(L)$ runtime and $O(L)$ space bounds (where $L \le 18$ is string length).

---

## 1. Instance & Teaching Goal

Given a string $n$ representing an integer $x$:
Find the **closest palindromic integer** to $n$ (excluding $n$ itself).
If there is a tie, return the **smaller** palindrome.

```text
Input: n = "123"

Five Candidates Evaluated:
  1. Boundary below:  99       (diff: |99 - 123| = 24)
  2. Prefix - 1:     111      (diff: |111 - 123| = 12)
  3. Prefix mirrored: 121      (diff: |121 - 123| = 2)  <-- Closest!
  4. Prefix + 1:     131      (diff: |131 - 123| = 8)
  5. Boundary above: 1001     (diff: |1001 - 123| = 878)

Output: "121"
```

### Why Only 5 Candidates Suffice
- A palindrome is completely determined by its **first half** (the prefix).
- The closest palindrome to $x$ must either:
  1. Have the exact same length as $x$: In this case, altering the most significant digits makes the number deviate drastically. The closest numbers are formed by keeping the prefix identical, decremented by 1, or incremented by 1.
  2. Have a different number of digits:
     - One digit fewer: The largest palindrome of length $l - 1$ is $99\dots9 = 10^{l-1} - 1$.
     - One digit more: The smallest palindrome of length $l + 1$ is $100\dots01 = 10^l + 1$.
- No other palindrome can be closer than the best among these 5 candidates!

---

## 2. Conceptual Foundation & Invariants

### 1. The 5 Candidates:
Let $l = \text{len}(n)$ and $left = \text{int}(n[:\lfloor (l+1)/2 \rfloor])$:
1. $10^{l-1} - 1$ (all 9s of length $l - 1$)
2. $10^l + 1$ ($100\dots01$ of length $l + 1$)
3. Mirror of $left - 1$
4. Mirror of $left$
5. Mirror of $left + 1$

### 2. Suffix Mirroring Rules:
- If $l$ is even: reverse the entire prefix into the suffix ($12 \to 1221$).
- If $l$ is odd: drop the last digit of the prefix before reversing into the suffix ($12 \to 121$).

### 3. Selection Metric:
From the candidate set $res \setminus \{x\}$:
Find $t$ that minimizes $|t - x|$.
If $|t_1 - x| == |t_2 - x|$, choose $\min(t_1, t_2)$.

> **Exclusion Invariant.** The target integer $x$ itself must always be discarded from the candidate pool, ensuring the answer is strictly a distinct closest neighbor.

---

## 3. Step-by-Step Worked Execution

We trace $n = \text{"123"}$:

---

### Step 1: Initialize Candidate Pool
- Length $l = 3$.
- $10^{3-1} - 1 = 99$.
- $10^3 + 1 = 1001$.
- Pool: $\{99, 1001\}$.

---

### Step 2: Mirror Prefix Variants
- Prefix length: $(3 + 1) // 2 = 2 \implies left = 12$.
- Variants $i \in [11, 12, 13]$:
  - $i = 11$: odd length $\implies$ drop last digit $\to 1 \implies 111$.
  - $i = 12$: drop last digit $\to 1 \implies 121$.
  - $i = 13$: drop last digit $\to 1 \implies 131$.
- Pool: $\{99, 1001, 111, 121, 131\}$.

---

### Step 3: Remove $x = 123$
$123$ is not a palindrome, so no element is removed.

---

### Step 4: Compare Differences
- $t = 99$: $|99 - 123| = 24$
- $t = 111$: $|111 - 123| = 12$
- $t = \mathbf{121}$: $|121 - 123| = \mathbf{2}$
- $t = 131$: $|131 - 123| = 8$
- $t = 1001$: $|1001 - 123| = 878$
Minimal difference is $2$, achieved by $121$.

---

### Step 5: Emit Output
$$
\mathbf{\text{"121"}}
$$

---

## 4. Complete Execution Trace

| Candidate $t$ | Origin / Class | Absolute Difference $\lvert t - 123 \rvert$ | Current Best $ans$ |
|:---:|:---:|:---:|:---:|
| $99$ | Boundary $10^{l-1}-1$ | $24$ | $99$ |
| $111$ | Mirror $(left - 1)$ | $12$ | $111$ |
| **$121$** | **Mirror $(left)$** | **$2$** | **`121`** |
| $131$ | Mirror $(left + 1)$ | $8$ | $121$ |
| $1001$ | Boundary $10^l+1$ | $878$ | $121$ |
| **Final Result** | — | — | **`"121"`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Digit Input ($n = \text{"1"}$):** Discards $1$; candidates $\{0, 2\}$. Tie-break selects smaller $\implies \mathbf{\text{"0"}}$.
- **Input is Already a Palindrome ($n = \text{"121"}$):** Mirroring $left$ produces $121$, which is discarded by `res.discard(x)`. Candidates $111$ (diff 10) and $131$ (diff 10) tie $\implies$ tie-break selects $\mathbf{\text{"111"}}$.
- **Powers of 10 ($n = \text{"1000"}$):** $left-1$ collapses digits $\implies 999$ (diff 1) beats $1001$ (diff 1) $\implies \mathbf{\text{"999"}}$.
- **Large Numbers ($n$ up to $10^{18}$):** Fits within standard 64-bit signed integers; evaluates all 5 candidates in $< 1$ microsecond.

---

## 6. Traps & Common Anti-Patterns

- **Searching by Incrementing/Decrementing by 1:** Testing $x - 1, x + 1, x - 2 \dots$ until a palindrome is found runs in $O(10^{L/2})$ time, causing catastrophic TLE for 18-digit numbers.
- **Forgetting Length Transitions ($10^{l-1}-1$ and $10^l+1$):** For $n = 100$, the closest palindrome is $99$. Prefix variations alone would only generate $101, 111, 99$ (if handled carefully). Explicit boundary formulas prevent missing cross-decade palindromes.
- **Returning Self When Input is a Palindrome:** The problem requires the closest palindrome *not including itself*. Always discard $x$ before comparison.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Prefix extraction and string conversion: $O(L)$ where $L = \text{len}(n) \le 18$.
  - Exactly 5 candidates are generated and evaluated with constant-time arithmetic.
  - Total Time: $\mathcal{O}(L)$. Runs in $< 5$ microseconds.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(L)$ auxiliary space to store candidate strings and digits.
