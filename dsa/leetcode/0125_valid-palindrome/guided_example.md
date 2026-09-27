# Guided Example: Valid Palindrome

We trace the step-by-step two-pointer inward scanning and alphanumeric filtering on representative palindrome and mismatch instances:

- **Valid Palindrome Instance:** $s = \text{"A man, a plan, a canal: Panama"} \implies \text{True}$
- **Mismatch Counterexample:** $s = \text{"race a car"} \implies \text{False}$ (Normalized `"raceacar"`, $'e' \ne 'a'$)
- **Empty / Punctuation-Only Base:** $s = \text{"   , : "} \implies \text{True}$ (Empty normalized string reads symmetrically)

This instance demonstrates in-place two-pointer convergence without allocating an auxiliary normalized string, advancing pointers over non-alphanumeric noise, case-insensitive comparison, and early-exit mismatch detection in $O(N)$ time and $O(1)$ space.

---

## 1. Instance & Teaching Goal

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given the string $s = \text{"A man, a plan, a canal: Panama"}$ (length $30$):
- Filtered normalized string:
  $$
  \text{"a"} \, \text{"m"} \, \text{"a"} \, \text{"n"} \, \text{"a"} \, \text{"p"} \, \text{"l"} \, \text{"a"} \, \text{"n"} \, \text{"a"} \, \text{"c"} \, \text{"a"} \, \text{"n"} \, \text{"a"} \, \text{"l"} \, \text{"p"} \, \text{"a"} \, \text{"n"} \, \text{"a"} \, \text{"m"} \, \text{"a"}
  $$
  which is $\text{"amanaplanacanalpanama"}$ of length $21$.
- Symmetrically reversed, it reads identically: $\text{"amanaplanacanalpanama"}$.
- Return value is $\text{True}$.

A naive approach extracts all alphanumeric characters into a new string or list and checks `filtered == filtered[::-1]`. While correct, this allocates $O(N)$ auxiliary memory.
Using two pointers ($L$ initialized to the start and $R$ to the end) that move inward while skipping punctuation and spaces verifies symmetry in-place with strictly $O(1)$ extra space.

---

## 2. Conceptual Foundation & Invariants

### Inward Two-Pointer Convergence Protocol
Initialize $L = 0$ and $R = |s| - 1$.

While $L < R$:
1. **Advance Left Pointer Past Non-Alphanumerics:**
   $$
   \text{while } L < R \text{ and not } s[L].\text{isalnum}(): \quad L \leftarrow L + 1
   $$
2. **Decrement Right Pointer Past Non-Alphanumerics:**
   $$
   \text{while } L < R \text{ and not } s[R].\text{isalnum}(): \quad R \leftarrow R - 1
   $$
3. **Compare Symmetrical Characters:**
   Convert both characters to lowercase:
   $$
   \text{if } s[L].\text{lower}() \ne s[R].\text{lower}(): \quad \text{return False}
   $$
4. **Step Inward:**
   $$
   L \leftarrow L + 1, \quad R \leftarrow R - 1
   $$

If the loop completes without detecting a mismatch, return $\text{True}$.

> **Invariant.** Before each iteration, all alphanumeric characters strictly outside the interval $[L, R]$ have already been paired and confirmed equal under lowercase normalization.

---

## 3. Step-by-Step Worked Execution

We trace the two pointers on $s = \text{"A man, a plan, a canal: Panama"}$ ($|s| = 30$):

```text
Indices:  012345678901234567890123456789
String:   A man, a plan, a canal: Panama
          ^                            ^
          L=0                         R=29
```

### Iteration 1:
- $L = 0$ ($s[0] = \text{'A'}$): alphanumeric. Lowercase: `'a'`.
- $R = 29$ ($s[29] = \text{'a'}$): alphanumeric. Lowercase: `'a'`.
- Compare: `'a' == 'a'`. Match!
- Inward step: $L = 1$, $R = 28$.

---

### Iteration 2:
- $L = 1$ is space `' '` $\implies L$ advances to $2$ ($s[2] = \text{'m'}$).
- $R = 28$ ($s[28] = \text{'m'}$): alphanumeric.
- Compare: `'m' == 'm'`. Match!
- Inward step: $L = 3$, $R = 27$.

---

### Iteration 3:
- $L = 3$ ($s[3] = \text{'a'}$), $R = 27$ ($s[27] = \text{'a'}$).
- Compare: `'a' == 'a'`. Match!
- Inward step: $L = 4$, $R = 26$.

---

### Iteration 4:
- $L = 4$ ($s[4] = \text{'n'}$), $R = 26$ ($s[26] = \text{'n'}$).
- Compare: `'n' == 'n'`. Match!
- Inward step: $L = 5$, $R = 25$.

---

### Iteration 5:
- $L = 5$ is `','` $\implies L$ advances to $7$ ($s[7] = \text{'a'}$).
- $R = 25$ ($s[25] = \text{'a'}$).
- Compare: `'a' == 'a'`. Match!
- Inward step: $L = 8$, $R = 24$.

---

### Iterations 6 through 11 (Remaining Center Pairs):
- Matches continue: `('p', 'p')`, `('l', 'l')`, `('a', 'a')`, `('n', 'n')`, `('a', 'a')`.
- At the exact center: $L$ reaches index $17$ ($s[17] = \text{'c'}$), and $R$ reaches index $17$.
- Pointers meet ($L = R = 17$).
- Loop terminates with $L \not< R$.

Result: All alphanumeric characters matched symmetrically. Returns $\mathbf{True}$.

---

## 4. Complete Execution Trace

### Pointer Position & Character Matching Table

| Iteration | Left Index $L$ | Raw Char $s[L]$ | Normalized $s[L]$ | Right Index $R$ | Raw Char $s[R]$ | Normalized $s[R]$ | Equal? | Action Taken |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 0 | `'A'` | `'a'` | 29 | `'a'` | `'a'` | Yes | $L \leftarrow 1, R \leftarrow 28$ |
| 2 | 2 | `'m'` | `'m'` | 28 | `'m'` | `'m'` | Yes | Skip space at $1$; $L \leftarrow 3, R \leftarrow 27$ |
| 3 | 3 | `'a'` | `'a'` | 27 | `'a'` | `'a'` | Yes | $L \leftarrow 4, R \leftarrow 26$ |
| 4 | 4 | `'n'` | `'n'` | 26 | `'n'` | `'n'` | Yes | $L \leftarrow 5, R \leftarrow 25$ |
| 5 | 7 | `'a'` | `'a'` | 25 | `'a'` | `'a'` | Yes | Skip `", "` at $5, 6$; $L \leftarrow 8, R \leftarrow 24$ |
| 6 | 9 | `'p'` | `'p'` | 23 | `'P'` | `'p'` | Yes | Skip spaces; match `'p'`; $L \leftarrow 10, R \leftarrow 22$ |
| 7 | 10 | `'l'` | `'l'` | 21 | `'l'` | `'l'` | Yes | Skip punctuation; $L \leftarrow 11, R \leftarrow 20$ |
| 8 | 11 | `'a'` | `'a'` | 19 | `'a'` | `'a'` | Yes | $L \leftarrow 12, R \leftarrow 18$ |
| 9 | 12 | `'n'` | `'n'` | 18 | `'n'` | `'n'` | Yes | $L \leftarrow 13, R \leftarrow 17$ |
| 10 | 15 | `'a'` | `'a'` | 16 | `'a'` | `'a'` | Yes | Skip spaces; $L \leftarrow 16, R \leftarrow 15$ |
| Term | 17 | `'c'` | `'c'` | 17 | `'c'` | `'c'` | - | $L = R \implies$ Loop Ends. **True** |

### Counterexample: `"race a car"`
- Normalized sequence: `"raceacar"`.
- $L = 0$ (`'r'`) vs $R = 7$ (`'r'`): Match.
- $L = 1$ (`'a'`) vs $R = 6$ (`'a'`): Match.
- $L = 2$ (`'c'`) vs $R = 5$ (`'c'`): Match.
- $L = 3$ (`'e'`) vs $R = 4$ (`'a'`):
  - **Mismatch:** `'e' != 'a'`!
  - Early-exit returns **`False`**.

---

## 5. Algorithmic Correctness

**Soundness.** A string is a palindrome if and only if the $k$-th alphanumeric character from the beginning equals the $k$-th alphanumeric character from the end for all $k$. The inner while-loops skip non-alphanumeric characters, ensuring that $s[L]$ and $s[R]$ correspond to the exact $k$-th characters from each boundary. If any pair differs, the string cannot be a palindrome, justifying early `False`.

**Completeness.** Since $L$ increases and $R$ decreases, the pointers strictly converge toward the center, inspecting every alphanumeric character at most once. If no mismatch is detected before $L \ge R$, every required pair has matched, proving `True`.

---

## 6. Traps This Instance Exposes

- **Inner Loop Pointer Guard ($L < R$):** In a string containing only spaces or punctuation (e.g. `"   , :  "`), advancing $L$ without checking $L < R$ will cause $L$ to step past $R$ or out of array bounds. Always include $L < R$ in the inner skip loops.
- **Digits in Alphanumeric Strings:** `isalnum()` includes numeric digits `'0' \dots '9'`. Digits are case-insensitive (`'0'.lower() == '0'`) and must match identical digit characters (`'0'` does not match `'a'`).
- **Creating Filtered String Copies:** Allocating a new string with `[c.lower() for c in s if c.isalnum()]` takes $O(N)$ extra heap memory. In-place two-pointer comparison maintains $O(1)$ space.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = |s|$. Pointer $L$ only advances and pointer $R$ only decreases. Each character is visited at most twice (once during skipping and once during comparison), guaranteeing strictly linear runtime.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, requiring only two index variables ($L$ and $R$) without string allocations.
