# Guided Example: Reconstruct Original Digits from English

We trace the step-by-step character frequency histogramming, triangular linear system deduction, three-wave dependency peeling, and sorted digit reconstruction on representative anagram strings:

- **Input:** $s = \text{"owoztneoer"}$
- **Required output:** `"012"`
  - Character histogram of $s$:
    - `'e': 2, 'n': 1, 'o': 3, 'r': 2, 't': 1, 'w': 1, 'z': 1`
  - **Wave 1 (Unique signature letters):**
    - `'z'` appears only in `"zero"` $\implies cnt[0] = \text{count('z')} = \mathbf{1}$
    - `'w'` appears only in `"two"` $\implies cnt[2] = \text{count('w')} = \mathbf{1}$
    - `'u'` appears only in `"four"` $\implies cnt[4] = \text{count('u')} = \mathbf{0}$
    - `'x'` appears only in `"six"` $\implies cnt[6] = \text{count('x')} = \mathbf{0}$
    - `'g'` appears only in `"eight"` $\implies cnt[8] = \text{count('g')} = \mathbf{0}$
  - **Wave 2 (Secondary shared letters):**
    - `'h'` in `"three"` and `"eight"` $\implies cnt[3] = \text{count('h')} - cnt[8] = 0 - 0 = \mathbf{0}$
    - `'f'` in `"four"` and `"five"` $\implies cnt[5] = \text{count('f')} - cnt[4] = 0 - 0 = \mathbf{0}$
    - `'s'` in `"six"` and `"seven"` $\implies cnt[7] = \text{count('s')} - cnt[6] = 0 - 0 = \mathbf{0}$
  - **Wave 3 (Tertiary residual letters):**
    - `'o'` in `"zero"`, `"two"`, `"four"`, `"one"`:
      $$
      cnt[1] = \text{count('o')} - cnt[0] - cnt[2] - cnt[4] = 3 - 1 - 1 - 0 = \mathbf{1}
      $$
    - `'i'` in `"five"`, `"six"`, `"eight"`, `"nine"`:
      $$
      cnt[9] = \text{count('i')} - cnt[5] - cnt[6] - cnt[8] = 0 - 0 - 0 - 0 = \mathbf{0}
      $$
  - Assembled digits: $cnt[0]=1, cnt[1]=1, cnt[2]=1 \implies \mathbf{\text{"012"}}$
- **Residual Pair Instance:** $s = \text{"fviefuro"} \implies cnt[4]=1 (\text{'u'}), cnt[5]=1 (\text{'f'}-cnt[4]) \implies \mathbf{\text{"45"}}$
- **Repeated Zeros Instance:** $s = \text{"zerozero"} \implies cnt[0]=2 \implies \mathbf{\text{"00"}}$

This instance demonstrates modeling multiset anagram decomposition as an upper-triangular system of linear equations, proves why topological back-substitution solves the system without Gaussian elimination in $O(N)$ time, and derives $O(N)$ runtime and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a string $s = \text{"owoztneoer"}$ containing an anagram of English words for digits ($0\dots 9$):
Reconstruct the original digits in **ascending order** as a string:

```text
Input Characters:
  o: 3   w: 1   z: 1   t: 1   n: 1   e: 2   r: 2

Deduction Tree:
  1. 'z' only appears in "zero" -> Exactly 1 "zero" -> Digits: [0]
  2. 'w' only appears in "two"  -> Exactly 1 "two"  -> Digits: [0, 2]
  3. 'o' appears in "zero", "two", "four", and "one".
     count('o') = 3, subtract 1 ('zero') and 1 ('two') -> 1 remaining 'o' belongs to "one" -> Digits: [0, 1, 2]

Result in Ascending Order: "012"
```

### The Linear Algebra of Anagram Decomposition
The English words for digits $0$ through $9$ share characters:
- `"zero"`, `"one"`, `"two"`, `"three"`, `"four"`, `"five"`, `"six"`, `"seven"`, `"eight"`, `"nine"`.
Instead of searching through exponential permutations ($O(10^K)$ backtracking), we express character counts as a system of linear equations over the 10 digit counts $x_0, \dots, x_9$:
$$
\text{count}(c) = \sum_{k=0}^9 \text{multiplicity}(c, \text{word}_k) \cdot x_k
$$
Because the English digit words contain specific unique and cascading letters, this system is **upper-triangular** and can be solved by direct back-substitution in 3 stages.

---

## 2. Conceptual Foundation & Invariants

### 1. The Three-Wave Topological Deduction Hierarchy:

| Stage | Distinct Feature Letter | Words Containing Letter | Direct Closed-Form Formula |
|:---:|:---:|:---|:---|
| **Wave 1** | `'z'` | `"zero"` | $cnt[0] = count(\text{'z'})$ |
| **Wave 1** | `'w'` | `"two"` | $cnt[2] = count(\text{'w'})$ |
| **Wave 1** | `'u'` | `"four"` | $cnt[4] = count(\text{'u'})$ |
| **Wave 1** | `'x'` | `"six"` | $cnt[6] = count(\text{'x'})$ |
| **Wave 1** | `'g'` | `"eight"` | $cnt[8] = count(\text{'g'})$ |
| **Wave 2** | `'h'` | `"three"`, `"eight"` | $cnt[3] = count(\text{'h'}) - cnt[8]$ |
| **Wave 2** | `'f'` | `"four"`, `"five"` | $cnt[5] = count(\text{'f'}) - cnt[4]$ |
| **Wave 2** | `'s'` | `"six"`, `"seven"` | $cnt[7] = count(\text{'s'}) - cnt[6]$ |
| **Wave 3** | `'o'` | `"zero"`, `"two"`, `"four"`, `"one"` | $cnt[1] = count(\text{'o'}) - cnt[0] - cnt[2] - cnt[4]$ |
| **Wave 3** | `'i'` | `"five"`, `"six"`, `"eight"`, `"nine"` | $cnt[9] = count(\text{'i'}) - cnt[5] - cnt[6] - cnt[8]$ |

### 2. Dependency Graph:
```text
  Wave 1:  [0: 'z']   [2: 'w']   [4: 'u']   [6: 'x']   [8: 'g']
                                   |          |          |
  Wave 2:                     [5: 'f'-4] [7: 's'-6] [3: 'h'-8]
                                   |          |          |
  Wave 3:  [1: 'o' - 0 - 2 - 4]    +----------+----------+---> [9: 'i' - 5 - 6 - 8]
```

> **Invariant.** At the start of Wave $k$, all digit counts required on the right-hand side of Wave $k$'s formulas have already been uniquely and accurately determined.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"owoztneoer"}$:

---

### Step 1: Character Histogram
Count character occurrences in $s$:
$$
\text{counts} = \{\text{'e'}: 2, \; \text{'n'}: 1, \; \text{'o'}: 3, \; \text{'r'}: 2, \; \text{'t'}: 1, \; \text{'w'}: 1, \; \text{'z'}: 1\}
$$
All other lowercase letters have count $0$.

---

### Step 2: Wave 1 Evaluation (Unique Signature Letters)
- $cnt[0] = \text{counts}[\text{'z'}] = \mathbf{1}$  (`"zero"`)
- $cnt[2] = \text{counts}[\text{'w'}] = \mathbf{1}$  (`"two"`)
- $cnt[4] = \text{counts}[\text{'u'}] = \mathbf{0}$
- $cnt[6] = \text{counts}[\text{'x'}] = \mathbf{0}$
- $cnt[8] = \text{counts}[\text{'g'}] = \mathbf{0}$

---

### Step 3: Wave 2 Evaluation (Secondary Shared Letters)
- **Digit 3 (`"three"`):**
  $$
  cnt[3] = \text{counts}[\text{'h'}] - cnt[8] = 0 - 0 = \mathbf{0}
  $$
- **Digit 5 (`"five"`):**
  $$
  cnt[5] = \text{counts}[\text{'f'}] - cnt[4] = 0 - 0 = \mathbf{0}
  $$
- **Digit 7 (`"seven"`):**
  $$
  cnt[7] = \text{counts}[\text{'s'}] - cnt[6] = 0 - 0 = \mathbf{0}
  $$

---

### Step 4: Wave 3 Evaluation (Tertiary Residual Letters)
- **Digit 1 (`"one"`):**
  Letter `'o'` is present in `"zero"` (1), `"two"` (1), `"four"` (0), and `"one"`:
  $$
  cnt[1] = \text{counts}[\text{'o'}] - cnt[0] - cnt[2] - cnt[4] = 3 - 1 - 1 - 0 = \mathbf{1}
  $$
- **Digit 9 (`"nine"`):**
  Letter `'i'` is present in `"five"` (0), `"six"` (0), `"eight"` (0), and `"nine"`:
  $$
  cnt[9] = \text{counts}[\text{'i'}] - cnt[5] - cnt[6] - cnt[8] = 0 - 0 - 0 - 0 = \mathbf{0}
  $$

---

### Step 5: Assembly in Ascending Order
Iterate over digits $0 \dots 9$:
- $i = 0: cnt[0] = 1 \implies \text{"0"}$
- $i = 1: cnt[1] = 1 \implies \text{"1"}$
- $i = 2: cnt[2] = 1 \implies \text{"2"}$
- $i = 3\dots 9: cnt[i] = 0$
Concatenated result: **`"012"`**.

---

## 4. Complete Execution Trace

| Digit | Word Name | Primary Letter | Deduction Formula | Raw Count in $s$ | Subtractions Applied | Final Count $cnt[d]$ | String Contribution |
|:---:|:---|:---:|:---|:---:|:---:|:---:|:---:|
| **0** | `zero` | `'z'` | $count(\text{'z'})$ | $1$ | None | **$1$** | `"0"` |
| **1** | `one` | `'o'` | $count(\text{'o'}) - cnt[0] - cnt[2] - cnt[4]$ | $3$ | $1 + 1 + 0 = 2$ | **$1$** | `"1"` |
| **2** | `two` | `'w'` | $count(\text{'w'})$ | $1$ | None | **$1$** | `"2"` |
| **3** | `three` | `'h'` | $count(\text{'h'}) - cnt[8]$ | $0$ | $0$ | **$0$** | — |
| **4** | `four` | `'u'` | $count(\text{'u'})$ | $0$ | None | **$0$** | — |
| **5** | `five` | `'f'` | $count(\text{'f'}) - cnt[4]$ | $0$ | $0$ | **$0$** | — |
| **6** | `six` | `'x'` | $count(\text{'x'})$ | $0$ | None | **$0$** | — |
| **7** | `seven` | `'s'` | $count(\text{'s'}) - cnt[6]$ | $0$ | $0$ | **$0$** | — |
| **8** | `eight` | `'g'` | $count(\text{'g'})$ | $0$ | None | **$0$** | — |
| **9** | `nine` | `'i'` | $count(\text{'i'}) - cnt[5] - cnt[6] - cnt[8]$ | $0$ | $0$ | **$0$** | — |

---

## 5. Boundary Cases & Failure Modes

- **Single Digit Repeated ($s = \text{"zerozerozero"}$):** Count of `'z'` is $3 \implies cnt[0] = 3 \implies \text{"000"}$.
- **All Digits Present ($0\dots 9$ once):** Wave 1 finds $\{0, 2, 4, 6, 8\}$, Wave 2 finds $\{3, 5, 7\}$, Wave 3 finds $\{1, 9\}$. Emits `"0123456789"`.
- **Large Input ($|s| \le 10^5$):** Because character counting is $O(|s|)$ and back-substitution takes exactly 10 constant-time arithmetic steps, execution time is dominated by a single fast string pass ($< 5$ ms).

---

## 6. Traps & Common Anti-Patterns

- **Premature Wave 3 Evaluation:** Attempting to evaluate $cnt[1]$ before $cnt[4]$ is known causes incorrect subtraction, because `"four"` also contains letter `'o'`. The topological ordering Wave 1 $\to$ Wave 2 $\to$ Wave 3 must be strictly respected.
- **Backtracking / DFS Search:** Trying to remove words recursively risks combinatorial explosion on strings with repeated letters (e.g. thousands of `'e'`s and `'o'`s). The mathematical system of equations has a unique solution and requires zero backtracking.
- **Sorting Output Array:** Sorting the final list of digits takes $O(K \log K)$ time. Iterating in index order $0 \dots 9$ naturally emits digits in sorted order in $O(1)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Counting character frequencies in $s$ takes $O(|s|)$ time.
  - The 10 arithmetic subtraction formulas take $O(1)$ time.
  - Assembling the output string takes $O(|output|) \le O(|s|)$ time.
  - Total Time: $\mathcal{O}(|s|)$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ beyond the output string, as the frequency map and digit count array require at most 26 letter keys and 10 digit counters.
