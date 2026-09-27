# Guided Example: Minimum ASCII Delete Sum for Two Strings

We trace the step-by-step 2D dynamic programming grid construction ($f[i][j]$), empty-string boundary prefix accumulation ($\sum \text{ord}(c)$), character equality diagonal transitions ($s_1[i-1] == s_2[j-1] \implies f[i-1][j-1]$), minimum-cost single-character deletion choices ($\min(f[i-1][j] + \text{ord}(s_1), \; f[i][j-1] + \text{ord}(s_2))$), and minimal weighted edit distance convergence on representative string pairs:

- **Input:** $s_1 = \text{"sea"}, \quad s_2 = \text{"eat"}$
- **Required output:** `231`
  - Problem objective:
    - Make strings $s_1$ and $s_2$ identical by deleting characters from either string.
    - Each deleted character incurs a cost equal to its **ASCII numerical value**.
    - Find the **lowest possible total ASCII sum** of deleted characters.
    - For $s_1 = \text{"sea"}$ and $s_2 = \text{"eat"}$:
      - Deleting `'s'` from $s_1$ leaves `"ea"` (cost $= \text{ord}('s') = 115$).
      - Deleting `'t'` from $s_2$ leaves `"ea"` (cost $= \text{ord}('t') = 116$).
      - Both strings become `"ea"`.
      - Total deletion cost: $115 + 116 = \mathbf{231}$.
- **2D Weighted Edit Distance & DP Invariant:**
  - **State Formulation ($f[i][j]$):**
    - Let $f[i][j]$ denote the minimum ASCII deletion sum needed to make the prefixes $s_1[0 \dots i-1]$ and $s_2[0 \dots j-1]$ identical.
  - **Base Cases (Empty Prefix Boundaries):**
    - If $s_2$ is empty ($j = 0$), every character in $s_1[0 \dots i-1]$ must be deleted:
      $$
      f[i][0] = f[i - 1][0] + \text{ord}(s_1[i - 1])
      $$
    - If $s_1$ is empty ($i = 0$), every character in $s_2[0 \dots j-1]$ must be deleted:
      $$
      f[0][j] = f[0][j - 1] + \text{ord}(s_2[j - 1])
      $$
  - **Recurrence Transitions ($i \ge 1, j \ge 1$):**
    - Case 1: The trailing characters match ($s_1[i - 1] == s_2[j - 1]$):
      - Both characters can be retained simultaneously with **zero deletion cost**:
        $$
        f[i][j] = f[i - 1][j - 1]
        $$
    - Case 2: The trailing characters differ ($s_1[i - 1] \ne s_2[j - 1]$):
      - We must delete at least one of them:
        1. Delete $s_1[i - 1]$: pay $\text{ord}(s_1[i - 1])$ and transition from $f[i - 1][j]$.
        2. Delete $s_2[j - 1]$: pay $\text{ord}(s_2[j - 1])$ and transition from $f[i][j - 1]$.
      - Select the minimum cost option:
        $$
        f[i][j] = \min \Big( f[i - 1][j] + \text{ord}(s_1[i - 1]), \; f[i][j - 1] + \text{ord}(s_2[j - 1]) \Big)
        $$
  - **Final Target:**
    $$
    ans = f[m][n]
    $$
- **Step-by-Step Worked Execution Trace on $s_1 = \text{"sea"}, s_2 = \text{"eat"}$:**
  - ASCII Values:
    - For $s_1$: $\text{'s'} = 115, \; \text{'e'} = 101, \; \text{'a'} = 97$.
    - For $s_2$: $\text{'e'} = 101, \; \text{'a'} = 97, \; \text{'t'} = 116$.
  - Dimensions: $m = 3, n = 3$. Table size $4 \times 4$.
  - **Step 1: Initialize Boundary Rows & Columns ($f[i][0]$ and $f[0][j]$):**
    - $f[0][0] = 0$.
    - Row 0 ($s_1 = \text{""}$):
      - $f[0][1] = 0 + \text{ord}('e') = 101$.
      - $f[0][2] = 101 + \text{ord}('a') = 101 + 97 = 198$.
      - $f[0][3] = 198 + \text{ord}('t') = 198 + 116 = 314$.
    - Col 0 ($s_2 = \text{""}$):
      - $f[1][0] = 0 + \text{ord}('s') = 115$.
      - $f[2][0] = 115 + \text{ord}('e') = 115 + 101 = 216$.
      - $f[3][0] = 216 + \text{ord}('a') = 216 + 97 = 313$.
  - **Step 2: Fill Row $i = 1$ ($s_1[0] = \text{'s'}$, ASCII 115):**
    - Cell $(1, 1)$ vs $s_2[0] = \text{'e'}$ ($'s' \ne 'e'$):
      $$
      f[1][1] = \min(f[0][1] + 115, \; f[1][0] + 101) = \min(101 + 115, \; 115 + 101) = \mathbf{216}
      $$
    - Cell $(1, 2)$ vs $s_2[1] = \text{'a'}$ ($'s' \ne 'a'$):
      $$
      f[1][2] = \min(f[0][2] + 115, \; f[1][1] + 97) = \min(198 + 115, \; 216 + 97) = \min(313, 313) = \mathbf{313}
      $$
    - Cell $(1, 3)$ vs $s_2[2] = \text{'t'}$ ($'s' \ne 't'$):
      $$
      f[1][3] = \min(f[0][3] + 115, \; f[1][2] + 116) = \min(314 + 115, \; 313 + 116) = \min(429, 429) = \mathbf{429}
      $$
  - **Step 3: Fill Row $i = 2$ ($s_1[1] = \text{'e'}$, ASCII 101):**
    - Cell $(2, 1)$ vs $s_2[0] = \text{'e'}$ ($\mathbf{'e' == 'e' \implies Match!}$):
      $$
      f[2][1] = f[1][0] = \mathbf{115} \quad (\text{Delete only 's' from } s_1)
      $$
    - Cell $(2, 2)$ vs $s_2[1] = \text{'a'}$ ($'e' \ne 'a'$):
      $$
      f[2][2] = \min(f[1][2] + 101, \; f[2][1] + 97) = \min(313 + 101, \; 115 + 97) = \min(414, \mathbf{212}) = \mathbf{212}
      $$
    - Cell $(2, 3)$ vs $s_2[2] = \text{'t'}$ ($'e' \ne 't'$):
      $$
      f[2][3] = \min(f[1][3] + 101, \; f[2][2] + 116) = \min(429 + 101, \; 212 + 116) = \min(530, \mathbf{328}) = \mathbf{328}
      $$
  - **Step 4: Fill Row $i = 3$ ($s_1[2] = \text{'a'}$, ASCII 97):**
    - Cell $(3, 1)$ vs $s_2[0] = \text{'e'}$ ($'a' \ne 'e'$):
      $$
      f[3][1] = \min(f[2][1] + 97, \; f[3][0] + 101) = \min(115 + 97, \; 313 + 101) = \min(212, 414) = \mathbf{212}
      $$
    - Cell $(3, 2)$ vs $s_2[1] = \text{'a'}$ ($\mathbf{'a' == 'a' \implies Match!}$):
      $$
      f[3][2] = f[2][1] = \mathbf{115} \quad (\text{Subsequence "ea" retained with zero cost!})
      $$
    - Cell $(3, 3)$ vs $s_2[2] = \text{'t'}$ ($'a' \ne 't'$):
      $$
      f[3][3] = \min(f[2][3] + 97, \; f[3][2] + 116) = \min(328 + 97, \; 115 + 116) = \min(425, \mathbf{231}) = \mathbf{231}
      $$
  - **Step 5: Output:**
    $$
    ans = f[3][3] = \mathbf{231}
    $$
- **Weighted Alignment Trace ($s_1 = \text{"delete"}, s_2 = \text{"leet"}$):**
  - Common preserved subsequence is `"leet"` or `"eet"`:
  - Keeping `"eet"` requires deleting `'d', 'l', 'e'` from $s_1$ and `'l'` from $s_2$ (cost: $100 + 108 + 101 + 108 = 417$).
  - Keeping `"let"` requires deleting `'d', 'e', 'e'` from $s_1$ and `'e'` from $s_2$ (cost: $100 + 101 + 101 + 101 = \mathbf{403}$).
  - Output is **`403`**.
- **Identical Strings ($s_1 == s_2$):**
  - Every character matches diagonally without deletion $\implies$ returns **`0`**.

This instance demonstrates weighted longest common subsequence duality and optimal sequence alignment dynamic programming, mathematically proves why character equality preserves optimal substructure across diagonal transitions, and derives $O(M \cdot N)$ runtime and $O(M \cdot N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given two strings $s_1$ and $s_2$:
Find the **minimum ASCII sum of deleted characters** to make both strings equal.

```text
s1 = "sea", s2 = "eat"

Delete 's' from s1: cost = ASCII('s') = 115  (leaves "ea")
Delete 't' from s2: cost = ASCII('t') = 116  (leaves "ea")

Both strings become "ea"!
Total deletion cost = 115 + 116 = 231
Result: 231
```

### The Invariant of the Weighted LCS
- Minimizing the ASCII sum of deleted characters is mathematically equivalent to maximizing the ASCII sum of the **common subsequence**.
- If $s_1[i-1] == s_2[j-1]$, no characters need to be deleted: $f[i][j] = f[i-1][j-1]$.
- Otherwise, take the cheaper option between deleting from $s_1$ or deleting from $s_2$.

---

## 2. Conceptual Foundation & Invariants

### 1. The Dynamic Programming Table $f[i][j]$:
Base states:
$$
f[i][0] = \sum_{k=0}^{i-1} \text{ord}(s_1[k]), \quad f[0][j] = \sum_{k=0}^{j-1} \text{ord}(s_2[k])
$$
Recurrence:
$$
f[i][j] = \begin{cases} f[i - 1][j - 1] & \text{if } s_1[i - 1] == s_2[j - 1] \\ \min(f[i - 1][j] + \text{ord}(s_1[i - 1]), \; f[i][j - 1] + \text{ord}(s_2[j - 1])) & \text{otherwise} \end{cases}
$$

> **Metric Subsequence Duality Invariant.** For any weight function $w: \Sigma \to \mathbb{R}_{>0}$, the shortest deletion distance $d_w(u, v)$ satisfies $d_w(u, v) = w(u) + w(v) - 2 \max_{z \in \text{CS}(u, v)} w(z)$, yielding an exact additive duality with the maximum-weight common subsequence.

---

## 3. Step-by-Step Worked Execution

We trace $s_1 = \text{"sea"}, s_2 = \text{"eat"}$:

---

### Step 1: Base Borders
- $f[0] = [0, 101, 198, 314]$.
- $f[i][0] = [0, 115, 216, 313]^T$.

---

### Step 2: Row 1 ($s_1[0] = \text{'s'}$)
- $f[1] = [115, 216, 313, 429]$.

---

### Step 3: Row 2 ($s_1[1] = \text{'e'}$)
- At $(2, 1)$, $'e' == 'e' \implies f[2][1] = f[1][0] = 115$.
- $f[2] = [216, 115, 212, 328]$.

---

### Step 4: Row 3 ($s_1[2] = \text{'a'}$)
- At $(3, 2)$, $'a' == 'a' \implies f[3][2] = f[2][1] = 115$.
- At $(3, 3)$, $'a' \ne 't' \implies \min(328 + 97, 115 + 116) = \mathbf{231}$.

---

### Step 5: Output
$$
\mathbf{231}
$$

---

## 4. Complete Execution Trace

| DP Table $f[i][j]$ | Empty $s_2$ | `'e'` (101) | `'a'` (97) | `'t'` (116) |
|:---:|:---:|:---:|:---:|:---:|
| **Empty $s_1$** | $0$ | $101$ | $198$ | $314$ |
| **`'s'` (115)** | $115$ | $216$ | $313$ | $429$ |
| **`'e'` (101)** | $216$ | **$115$** (Match) | $212$ | $328$ |
| **`'a'` (97)** | $313$ | $212$ | **$115$** (Match) | **`231`** |

---

## 5. Boundary Cases & Failure Modes

- **One String Empty:** Deletes all characters of the other string $\implies$ sum of all ASCII values.
- **Identical Strings:** 0 deletions needed $\implies$ returns 0.
- **Completely Disjoint Characters ($s_1 = \text{"a"}, s_2 = \text{"b"}$):** Deletes both $\implies \text{ord}('a') + \text{ord}('b') = 97 + 98 = 195$.
- **Single Character Match:** Keeps the shared character, deletes all others.

---

## 6. Traps & Common Anti-Patterns

- **Standard LCS (Unweighted):** Finding the longest common subsequence by character count does not always minimize the ASCII sum, because a longer subsequence of heavy characters might be better than a shorter one of light characters. The DP must weight transitions by $\text{ord}(c)$.
- **Greedy Character Deletions:** Greedy deletion fails when multiple identical characters appear in different configurations; dynamic programming guarantees global optimality.
- **Array Off-By-One:** Ensure table dimensions are $(m + 1) \times (n + 1)$ with base cases filled for empty prefixes.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Standard 2D table of size $(M + 1) \times (N + 1)$.
  - Each cell computes a constant number of comparisons: $\mathcal{O}(1)$.
  - Total Time: strictly $\mathcal{O}(M \cdot N)$. For $M, N = 1000$, executes in $< 20$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M \cdot N)$ for the full 2D table, or $\mathcal{O}(N)$ using two alternating 1D rows.
