# Guided Example: Valid Palindrome II

We trace the step-by-step inward two-pointer convergence ($i \to \leftarrow j$), character equality propagation ($s[i] == s[j]$), first mismatch identification ($s[i] \ne s[j]$), dual single-deletion branch testing (skipping left character $i+1 \dots j$ vs skipping right character $i \dots j-1$), strict palindrome verification subroutine, and early feasibility determination on representative strings:

- **Input:** $s = \text{"abca"}$
- **Required output:** `true`
  - Problem objective:
    - Determine if the string can be converted into a palindrome by deleting **at most one** character.
    - A string is a palindrome if it reads the exact same forward and backward.
    - For `"abca"`:
      - Deleting character `'c'` at index 2 yields `"aba"` (a valid palindrome).
      - Alternatively, deleting character `'b'` at index 1 yields `"aca"` (a valid palindrome).
      - Return **`true`**.
- **Inward Two-Pointer & Single-Branch Invariant:**
  - **The First Mismatch Invariant:**
    - As long as the characters at the outer boundaries match ($s[i] == s[j]$), neither character needs to be deleted. Both can be preserved in the final palindrome. We advance both pointers inward:
      $$
      i \leftarrow i + 1, \quad j \leftarrow j - 1
      $$
    - Suppose we encounter the **first mismatch**:
      $$
      s[i] \ne s[j]
      $$
    - Because we are permitted at most **one single deletion** across the entire string, the character causing this asymmetry **must be either $s[i]$ or $s[j]$**!
  - **The Two Competing Hypotheses:**
    - **Hypothesis 1 (Delete Left Character $s[i]$):**
      - Check whether the remaining inner substring $s[i + 1 \dots j]$ is a strict palindrome (with zero further deletions permitted).
    - **Hypothesis 2 (Delete Right Character $s[j]$):**
      - Check whether the remaining inner substring $s[i \dots j - 1]$ is a strict palindrome (with zero further deletions permitted).
    - If **either** hypothesis holds, the string is valid:
      $$
      \text{Result} = \text{is\_palindrome}(s[i + 1 \dots j]) \lor \text{is\_palindrome}(s[i \dots j - 1])
      $$
    - If neither substring is a palindrome, then at least two deletions would be required $\implies \mathbf{False}$.
- **Step-by-Step Worked Execution Trace on $s = \text{"abca"}$ ($n = 4$):**
  - Initialize pointers:
    $$
    i = 0, \quad j = 3 \quad (s[0] = \text{'a'}, \; s[3] = \text{'a'})
    $$
  - **Step 1: Check Outer Pair $(0, 3)$:**
    - Compare:
      $$
      s[0] = \text{'a'}, \quad s[3] = \text{'a'} \implies s[0] == s[3] \quad \mathbf{(Match!)}
      $$
    - Both characters are valid symmetric boundaries.
    - Advance pointers inward:
      $$
      i \leftarrow 0 + 1 = \mathbf{1}, \quad j \leftarrow 3 - 1 = \mathbf{2}
      $$
  - **Step 2: Check Inner Pair $(1, 2)$:**
    - Inspect values:
      $$
      s[1] = \text{'b'}, \quad s[2] = \text{'c'} \implies \mathbf{\text{'b'} \ne \text{'c'}} \quad \mathbf{(First\ Mismatch\ Encountered!)}
      $$
    - We must spend our single deletion budget here.
    - Branch into two sub-checks:
  - **Step 3: Test Hypothesis 1 (Skip Left Character $s[1] = \text{'b'}$):**
    - Substring to verify: $s[i + 1 \dots j] = s[2 \dots 2] = \text{"c"}$.
    - A single-character string is trivially a palindrome!
    - Sub-check returns:
      $$
      \text{check}(2, 2) = \mathbf{True}
      $$
    - Deleting `'b'` yields string `"aca"`, which is a palindrome!
  - **Step 4: Test Hypothesis 2 (Skip Right Character $s[2] = \text{'c'}$):**
    - Substring to verify: $s[i \dots j - 1] = s[1 \dots 1] = \text{"b"}$.
    - A single-character string is trivially a palindrome!
    - Sub-check returns:
      $$
      \text{check}(1, 1) = \mathbf{True}
      $$
    - Deleting `'c'` yields string `"aba"`, which is also a palindrome!
  - **Step 5: Emit Final Outcome:**
    - At least one branch succeeded ($\mathbf{True} \lor \mathbf{True} = \mathbf{True}$).
    - Return **`true`**.
- **Two Deletions Required Failure Trace ($s = \text{"abc"}$):**
  - Compare $s[0] = \text{'a'}$ and $s[2] = \text{'c'}$ $\implies$ Mismatch at step 1!
  - Hypothesis 1 (skip `'a'`): test $s[1 \dots 2] = \text{"bc"}$.
    - In `"bc"`, `'b' \ne 'c'` $\implies$ False.
  - Hypothesis 2 (skip `'c'`): test $s[0 \dots 1] = \text{"ab"}$.
    - In `"ab"`, `'a' \ne 'b'` $\implies$ False.
  - Both hypotheses fail $\implies$ Returns **`false`**.
- **Already Palindromic ($s = \text{"aba"}$):**
  - $s[0] == s[2] == \text{'a'}$.
  - $i$ reaches $j$ ($1 == 1$) without any mismatch.
  - 0 deletions used $\implies$ Returns **`true`**.

This instance demonstrates two-pointer boundary contraction with single-level branch bifurcation, mathematically proves why mismatch resolution restricts candidate deletions to boundary endpoints, and derives $O(N)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a string $s$:
Determine if it can become a palindrome by deleting **at most 1 character**.

```text
s = "abca"

Step 1: Check s[0] and s[3] -> 'a' == 'a' (Match! Advance inward)
Step 2: Check s[1] and s[2] -> 'b' != 'c' (Mismatch!)

Decision:
  Option A (Delete 'b'): Remaining is "c" -> Palindrome! Valid!
  Option B (Delete 'c'): Remaining is "b" -> Palindrome! Valid!

Result: true
```

### The Invariant of the Single Mismatch Fork
- Matching characters from both ends never need to be deleted.
- At the very first mismatch $s[i] \ne s[j]$, the single allowable deletion must delete either $s[i]$ or $s[j]$.
- Checking if $s[i+1 \dots j]$ or $s[i \dots j-1]$ is a palindrome resolves the problem in strictly linear time.

---

## 2. Conceptual Foundation & Invariants

### 1. Inward Two-Pointer Traversal:
While $i < j$:
- If $s[i] == s[j]$: $i \leftarrow i + 1, \; j \leftarrow j - 1$.
- If $s[i] \ne s[j]$:
  $$
  \text{return } \text{is\_palindrome}(s[i + 1 \dots j]) \lor \text{is\_palindrome}(s[i \dots j - 1])
  $$

### 2. Strict Palindrome Checker:
Runs a standard two-pointer check on the remaining interval without any further deletions allowed.

> **Palindromic Boundary Reduction Invariant.** If $s[0 \dots k] = \text{reverse}(s[n-1-k \dots n-1])$, any single deletion producing a palindrome within $s$ must be an admissible deletion for the core subproblem $s[k+1 \dots n-2-k]$.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"abca"}$:

---

### Step 1: Boundary Pair $(0, 3)$
- $s[0] = \text{'a'}, s[3] = \text{'a'}$.
- Match! $i \leftarrow 1, j \leftarrow 2$.

---

### Step 2: Interior Pair $(1, 2)$
- $s[1] = \text{'b'}, s[2] = \text{'c'}$.
- Mismatch!

---

### Step 3: Branch A (Skip $i = 1$)
- Check $s[2 \dots 2] = \text{"c"}$.
- Valid palindrome $\implies \mathbf{true}$.

---

### Step 4: Output
$$
\mathbf{true}
$$

---

## 4. Complete Execution Trace

| Step | Pointer $i$ | Pointer $j$ | Characters $(s[i], s[j])$ | Equal? | Action Taken | Result |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $0$ | $3$ | $(\text{'a'}, \text{'a'})$ | Yes | Advance both | Continue |
| **$2$** | **$1$** | **$2$** | **$(\text{'b'}, \text{'c'})$** | **No** | **Fork into two checks** | **Evaluate** |
| Branch A | $2$ | $2$ | $(\text{'c'}, \text{'c'})$ | Yes | Single char | **`True`** |
| Branch B | $1$ | $1$ | $(\text{'b'}, \text{'b'})$ | Yes | Single char | `True` |
| **Final** | — | — | — | — | **Branch A succeeded** | **`true`** |

---

## 5. Boundary Cases & Failure Modes

- **Already a Palindrome ($s = \text{"aba"}$):** Returns `true` with 0 deletions.
- **Two Characters ($s = \text{"ab"}$):** Deleting either `'a'` or `'b'` leaves a 1-character palindrome $\implies$ returns `true`.
- **Requires 2 Deletions ($s = \text{"abcde"}$):** Fails on both branches $\implies$ returns `false`.
- **Mismatch in Middle vs Ends:** Handled uniformly regardless of where the mismatch occurs.

---

## 6. Traps & Common Anti-Patterns

- **Deleting More Than One Character:** Permitting recursion beyond depth 1 violates the constraint of deleting *at most one* character.
- **Greedy One-Sided Deletion:** Assuming you should always delete $s[i]$ fails on strings like `"abca"` (if only $s[i+1 \dots j]$ is tested) or `"cbbcc"` where only skipping $s[j]$ works. Both branches must be tested with `or`.
- **String Slicing Copy Overhead ($O(N^2)$):** Slicing strings `s[i+1:j+1]` creates new string copies in Python. Using integer indices in `check(i, j)` runs with zero allocations in $O(1)$ auxiliary space.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Initial scan: at most $N/2$ comparisons before finding the first mismatch.
  - Sub-checks: two linear scans over substrings of length $\le N$.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 1$ ms for $N = 10^5$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space using pointer indices (no string copying).
