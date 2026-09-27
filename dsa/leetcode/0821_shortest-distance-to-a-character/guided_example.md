# Guided Example: Shortest Distance to a Character

We trace the step-by-step 1D discrete Euclidean nearest neighbor search, two-pass left/right prefix/suffix sweep, nearest predecessor distance tracking ($i - pre$), nearest successor distance tracking ($suf - i$), coordinate minimum relaxation ($\min(ans[i], suf - i)$), and global distance profile extraction on representative character sequences:

- **Input:**
  $$
  s = \text{"loveleetcode"}, \quad c = \text{'e'}
  $$
- **Required output:**
  $$
  [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
  $$
  - Target character proximity rules:
    - We are given a string $s$ of length $n$ and a character $c$ that appears at least once in $s$.
    - For every index $i \in [0, n - 1]$, we want the minimum distance $|i - j|$ to an index $j$ where $s[j] = c$.
    - The closest occurrence of $c$ to index $i$ must lie either:
      1. To the left ($j \le i$, nearest predecessor), with distance $i - pre$.
      2. To the right ($j \ge i$, nearest successor), with distance $suf - i$.
    - Objective: Return an array of distances $[dist_0, dist_1, \dots, dist_{n-1}]$.
    - For $s = \text{"loveleetcode"}$ and $c = \text{'e'}$:
      - Occurrences of `'e'` are at indices: **3**, **5**, **6**, and **11**.
      - Index 0 ('l'): nearest `'e'` is at index 3 $\implies |0 - 3| = \mathbf{3}$.
      - Index 1 ('o'): nearest `'e'` is at index 3 $\implies |1 - 3| = \mathbf{2}$.
      - Index 2 ('v'): nearest `'e'` is at index 3 $\implies |2 - 3| = \mathbf{1}$.
      - Index 3 ('e'): is `'e'` itself $\implies \mathbf{0}$.
      - Index 4 ('l'): between 3 and 5 $\implies \min(|4 - 3|, |4 - 5|) = \mathbf{1}$.
      - Index 5 ('e'): is `'e'` $\implies \mathbf{0}$.
      - Index 6 ('e'): is `'e'` $\implies \mathbf{0}$.
      - Index 7 ('t'): between 6 and 11 $\implies \min(|7 - 6|, |7 - 11|) = \min(1, 4) = \mathbf{1}$.
      - Index 8 ('c'): $\min(|8 - 6|, |8 - 11|) = \min(2, 3) = \mathbf{2}$.
      - Index 9 ('o'): $\min(|9 - 6|, |9 - 11|) = \min(3, 2) = \mathbf{2}$.
      - Index 10 ('d'): $\min(|10 - 6|, |10 - 11|) = \min(4, 1) = \mathbf{1}$.
      - Index 11 ('e'): is `'e'` $\implies \mathbf{0}$.
      - Output: `[3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]`.
- **Two-Pass Bidirectional Sweep Invariant:**
  - **Decomposition of Distance:**
    - The closest distance is the minimum of two 1D directional distances:
      $$
      ans[i] = \min \left( \min_{j \le i, \, s[j] = c} (i - j), \; \min_{j \ge i, \, s[j] = c} (j - i) \right)
      $$
  - **Pass 1 (Left-to-Right Predecessor Sweep):**
    - Maintain $pre$, the index of the most recent occurrence of $c$ seen so far.
    - Initialize $pre = -\infty$.
    - For $i = 0 \dots n - 1$:
      - If $s[i] = c$, update: $pre \leftarrow i$.
      - Record forward distance:
        $$
        ans[i] \leftarrow i - pre
        $$
  - **Pass 2 (Right-to-Left Successor Sweep):**
    - Maintain $suf$, the index of the closest occurrence of $c$ ahead.
    - Initialize $suf = +\infty$.
    - For $i = n - 1 \dots 0$:
      - If $s[i] = c$, update: $suf \leftarrow i$.
      - Relax with backward distance:
        $$
        ans[i] \leftarrow \min(ans[i], \; suf - i)
        $$
  - After both passes, every cell holds the exact minimum distance.
- **Step-by-Step Worked Execution Trace on $s = \text{"loveleetcode"}$ ($n = 12$):**
  - **Forward Sweep (Left to Right):**
    - Initial $pre = -\infty$.
    - $i = 0$ ('l'): $pre = -\infty \implies ans[0] = \infty$.
    - $i = 1$ ('o'): $ans[1] = \infty$.
    - $i = 2$ ('v'): $ans[2] = \infty$.
    - $i = 3$ ('e'): $s[3] = \text{'e'} \implies pre \leftarrow 3$. $ans[3] = 3 - 3 = \mathbf{0}$.
    - $i = 4$ ('l'): $ans[4] = 4 - 3 = \mathbf{1}$.
    - $i = 5$ ('e'): $pre \leftarrow 5$. $ans[5] = 5 - 5 = \mathbf{0}$.
    - $i = 6$ ('e'): $pre \leftarrow 6$. $ans[6] = 6 - 6 = \mathbf{0}$.
    - $i = 7$ ('t'): $ans[7] = 7 - 6 = \mathbf{1}$.
    - $i = 8$ ('c'): $ans[8] = 8 - 6 = \mathbf{2}$.
    - $i = 9$ ('o'): $ans[9] = 9 - 6 = \mathbf{3}$.
    - $i = 10$ ('d'): $ans[10] = 10 - 6 = \mathbf{4}$.
    - $i = 11$ ('e'): $pre \leftarrow 11$. $ans[11] = 11 - 11 = \mathbf{0}$.
    - State after Pass 1:
      $$
      ans = [\infty, \; \infty, \; \infty, \; 0, \; 1, \; 0, \; 0, \; 1, \; 2, \; 3, \; 4, \; 0]
      $$
  - **Backward Sweep (Right to Left):**
    - Initial $suf = +\infty$.
    - $i = 11$ ('e'): $s[11] = \text{'e'} \implies suf \leftarrow 11$. $ans[11] = \min(0, 11 - 11) = \mathbf{0}$.
    - $i = 10$ ('d'): $suf - i = 11 - 10 = 1$. $ans[10] = \min(4, 1) = \mathbf{1}$.
    - $i = 9$ ('o'): $suf - i = 11 - 9 = 2$. $ans[9] = \min(3, 2) = \mathbf{2}$.
    - $i = 8$ ('c'): $suf - i = 11 - 8 = 3$. $ans[8] = \min(2, 3) = \mathbf{2}$.
    - $i = 7$ ('t'): $suf - i = 11 - 7 = 4$. $ans[7] = \min(1, 4) = \mathbf{1}$.
    - $i = 6$ ('e'): $suf \leftarrow 6$. $ans[6] = \min(0, 6 - 6) = \mathbf{0}$.
    - $i = 5$ ('e'): $suf \leftarrow 5$. $ans[5] = \min(0, 5 - 5) = \mathbf{0}$.
    - $i = 4$ ('l'): $suf - i = 5 - 4 = 1$. $ans[4] = \min(1, 1) = \mathbf{1}$.
    - $i = 3$ ('e'): $suf \leftarrow 3$. $ans[3] = \min(0, 3 - 3) = \mathbf{0}$.
    - $i = 2$ ('v'): $suf - i = 3 - 2 = 1$. $ans[2] = \min(\infty, 1) = \mathbf{1}$.
    - $i = 1$ ('o'): $suf - i = 3 - 1 = 2$. $ans[1] = \min(\infty, 2) = \mathbf{2}$.
    - $i = 0$ ('l'): $suf - i = 3 - 0 = 3$. $ans[0] = \min(\infty, 3) = \mathbf{3}$.
  - **Assembly of Final Output Vector:**
    $$
    ans = [3, \; 2, \; 1, \; 0, \; 1, \; 0, \; 0, \; 1, \; 2, \; 2, \; 1, \; 0]
    $$
- **Single Occurrence at Endpoint ($s = \text{"aaab"}, c = \text{'b'}$):**
  - Left pass sees no 'b' until index 3.
  - Right pass sets $suf = 3$, propagating distances $3 - i$:
    - $ans = [3, 2, 1, 0]$.
- **All Matching Characters ($s = \text{"aaaa"}, c = \text{'a'}$):**
  - Every index is the character $\implies [0, 0, 0, 0]$.

This instance demonstrates metric projection onto closed subsets of 1D integer lattices, mathematically proves why two monotonic coordinate sweeps compute exact Voronoi cell boundaries in linear time, and derives $O(N)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given string $s$ and target character $c$:
Find the **shortest distance** from each index to any occurrence of $c$.

```text
s = "loveleetcode",  c = 'e'
Occurrences of 'e' at indices: [ 3, 5, 6, 11 ]

Distances:
  Index 0 ('l'): distance to 3 = 3
  Index 1 ('o'): distance to 3 = 2
  Index 2 ('v'): distance to 3 = 1
  Index 3 ('e'): distance to 3 = 0
  Index 4 ('l'): distance to 3 or 5 = 1
  Index 5 ('e'): distance to 5 = 0
  Index 6 ('e'): distance to 6 = 0
  ...

Result: [ 3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0 ]
```

### The Invariant of Two-Pass Sweeping
- Left pass: computes distance to the closest occurrence of $c$ on the left ($i - pre$).
- Right pass: computes distance to the closest occurrence of $c$ on the right ($suf - i$).
- Taking the minimum across both passes gives the global shortest distance for each index.

---

## 2. Conceptual Foundation & Invariants

### 1. Directional Nearest Neighbor:
$$
\text{dist}_{\text{left}}(i) = i - \max \{ j \le i \mid s[j] = c \}
$$
$$
\text{dist}_{\text{right}}(i) = \min \{ j \ge i \mid s[j] = c \} - i
$$

### 2. Metric Unification:
$$
ans[i] = \min(\text{dist}_{\text{left}}(i), \; \text{dist}_{\text{right}}(i))
$$

> **Voronoi Cell Invariant.** The occurrences of $c$ partition the index line $[0, n - 1]$ into 1D Voronoi cells. Each cell midpoint between consecutive occurrences $p_k$ and $p_{k+1}$ defines the watershed where left-proximity transitions to right-proximity.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"loveleetcode"}, c = \text{'e'}$:

---

### Step 1: Forward Pass (Left to Right)
- Record distance from last seen `'e'`:
  - `[inf, inf, inf, 0, 1, 0, 0, 1, 2, 3, 4, 0]`.

---

### Step 2: Backward Pass (Right to Left)
- Record distance to next seen `'e'` and take $\min$:
  - Index 10: $\min(4, 11 - 10 = 1) = \mathbf{1}$.
  - Index 9: $\min(3, 11 - 9 = 2) = \mathbf{2}$.
  - Index 8: $\min(2, 11 - 8 = 3) = \mathbf{2}$.
  - Index 2: $\min(\infty, 3 - 2 = 1) = \mathbf{1}$.
  - Index 1: $\min(\infty, 3 - 1 = 2) = \mathbf{2}$.
  - Index 0: $\min(\infty, 3 - 0 = 3) = \mathbf{3}$.

---

### Step 3: Output
$$
[3, \; 2, \; 1, \; 0, \; 1, \; 0, \; 0, \; 1, \; 2, \; 2, \; 1, \; 0]
$$

---

## 4. Complete Execution Trace

| Index $i$ | Character $s[i]$ | Left Pass Distance ($i - pre$) | Right Pass Distance ($suf - i$) | Final Distance $\min$ |
|:---:|:---:|:---:|:---:|:---:|
| $0$ | `'l'` | $\infty$ | $3 - 0 = 3$ | **$3$** |
| $1$ | `'o'` | $\infty$ | $3 - 1 = 2$ | **$2$** |
| $2$ | `'v'` | $\infty$ | $3 - 2 = 1$ | **$1$** |
| $3$ | `'e'` | $0$ | $0$ | **$0$** |
| $4$ | `'l'` | $4 - 3 = 1$ | $5 - 4 = 1$ | **$1$** |
| $5$ | `'e'` | $0$ | $0$ | **$0$** |
| $6$ | `'e'` | $0$ | $0$ | **$0$** |
| $7$ | `'t'` | $7 - 6 = 1$ | $11 - 7 = 4$ | **$1$** |
| $8$ | `'c'` | $8 - 6 = 2$ | $11 - 8 = 3$ | **$2$** |
| $9$ | `'o'` | $9 - 6 = 3$ | $11 - 9 = 2$ | **$2$** |
| $10$ | `'d'` | $10 - 6 = 4$ | $11 - 10 = 1$ | **$1$** |
| **$11$** | **`'e'`** | **$0$** | **$0$** | **`0`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Target at End ($s = \text{"aaab"}, c = \text{'b'}$):** Forward pass fills $\infty$ until end; backward pass corrects all to $3 - i \implies [3, 2, 1, 0]$.
- **Single Target at Beginning ($s = \text{"baaa"}, c = \text{'b'}$):** Forward pass fills $0, 1, 2, 3$; backward pass leaves unchanged.
- **Consecutive Target Characters ($s = \text{"aabaa"}, c = \text{'b'}$):** Center is 0; distances increase symmetrically on both sides $\implies [2, 1, 0, 1, 2]$.
- **Length 1 String ($s = \text{"a"}, c = \text{'a'}$):** Distance is $[0]$.

---

## 6. Traps & Common Anti-Patterns

- **Searching for All Occurrences of $c$ for Every Index ($O(N^2)$):** Scanning the array for each index $i$ takes quadratic time. Two directional sweeps achieve linear $O(N)$ time.
- **Using 0 as Initial $pre$:** If $pre$ is initialized to 0, indices before the first $c$ will falsely think an occurrence of $c$ existed at index 0. Initialize $pre = -\infty$ and $suf = +\infty$.
- **Recomputing Indices with Binary Search ($O(N \log K)$):** While binary searching a list of occurrences works, two-pass sweep is simpler, cache-friendly, and strictly $O(N)$ without log factors.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Forward sweep: $\mathcal{O}(N)$.
  - Backward sweep: $\mathcal{O}(N)$.
  - Total Time: strictly linear $\mathcal{O}(N)$ where $N \le 10^4$. Completes in $< 0.5$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space beyond the output array.
