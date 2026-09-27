# Guided Example: Strong Password Checker

We trace the step-by-step three-tier length classification ($N < 6$, $6 \le N \le 20$, $N > 20$), character type deficiency counting, modular triplet reduction, and greedy deletion exchange arguments on representative password strings:

- **Input:** $password = \text{"aaaaaaaaaaaaaaaaaaaaaa"}$ (22 lowercase `'a'`s)
- **Required output:** `8`
  - Total length: $N = 22$ (Exceeds maximum length $20 \implies N > 20$)
  - Mandatory deletions required: $D = N - 20 = 22 - 20 = \mathbf{2}$
  - Character types present: lowercase only $\implies types = 1$
  - Missing types: $M = 3 - 1 = \mathbf{2}$ (Needs uppercase letter and digit)
  - Triplet run analysis:
    - Single run of 22 `'a'`s: length $L = 22$
    - Initial replacement requirement: $\lfloor 22 / 3 \rfloor = 7$
    - Modular class: $22 \equiv 1 \pmod 3$
  - Greedy deletion application:
    - Applying $2$ deletions to a run with $L \equiv 1 \pmod 3$ reduces length from $22 \to 20$.
    - New replacement requirement: $\lfloor 20 / 3 \rfloor = 6$ (Saves 1 replacement!)
    - Remaining replacements: $R' = 7 - 1 = \mathbf{6}$
  - Overlap with missing types:
    - The $6$ replacements can be chosen to supply the $2$ missing types (uppercase and digit): $\max(R', M) = \max(6, 2) = 6$.
  - Total minimum operations:
    $$
    D + \max(R', M) = 2 + 6 = \mathbf{8}
    $$
- **Short Password ($N < 6$):** $password = \text{"aA1"} \implies N = 3, M = 0 \implies \max(6 - 3, 0) = \mathbf{3}$ insertions
- **Valid Length ($6 \le N \le 20$):** $password = \text{"1337C0d3"} \implies N = 8, M = 0, R = 0 \implies \mathbf{0}$

This instance demonstrates case-based optimization under three distinct structural regimes, mathematically proves the greedy deletion exchange hierarchy ($L \equiv 0$, then $1$, then $2$), and derives $O(N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a password string $password$:
A password is **strong** if and only if it satisfies all three conditions:
1. **Length:** At least 6 and at most 20 characters ($6 \le |password| \le 20$).
2. **Character Classes:** Contains at least one lowercase letter, one uppercase letter, and one digit ($types \ge 3$).
3. **No Triplets:** Does not contain three repeating characters in a row ($s[i] == s[i+1] == s[i+2]$ is forbidden).

Find the **minimum number of operations** (insert, delete, or replace a character) needed to make the password strong.

```text
Input: "aaaaaaaaaaaaaaaaaaaaaa" (Length 22)

Deficiencies Identified:
  1. Length: 22 > 20 (Excess of 2 characters -> 2 deletions mandatory)
  2. Classes: Only lowercase (Missing 2 classes: uppercase and digit)
  3. Triplets: A contiguous run of 22 identical characters

Optimal Strategy:
  - Delete 2 characters: length becomes 20 (saves 1 replacement)
  - Perform 6 replacements: breaks all triplets AND inserts missing classes
  Total Operations: 2 + 6 = 8
```

### The Three Operational Regimes
The problem naturally partitions into three disjoint length regimes based on whether insertions, deletions, or pure replacements dominate:
- **Case 1 ($N < 6$):** Insertions dominate.
- **Case 2 ($6 \le N \le 20$):** Replacements dominate.
- **Case 3 ($N > 20$):** Deletions interact greedily with replacements.

---

## 2. Conceptual Foundation & Invariants

### 1. Regime 1: Too Short ($N < 6$)
- We must perform at least $6 - N$ insertions to reach length 6.
- Any character inserted can simultaneously be chosen as a missing character type (uppercase, lowercase, digit).
- Insertions can also be placed between repeated characters to break triplets (e.g. `"aaaaa"` with $N = 5$: inserting 1 character at index 2 produces `"aaXaa"`, breaking all triplets).
- Therefore, insertions completely subsume both missing types and triplet breaking:
  $$
  \text{Operations} = \max(6 - N, \; 3 - types)
  $$

### 2. Regime 2: Valid Length ($6 \le N \le 20$)
- No insertions or deletions are needed. Length is already optimal.
- A contiguous repeating run of length $L \ge 3$ requires $\lfloor L / 3 \rfloor$ replacements to break all triplets (e.g. `"aaa"` $\to$ `"aXa"` requires 1 replacement).
- Each replacement can be chosen to supply a missing character type.
- Total replacements needed for triplets: $R = \sum \lfloor L_k / 3 \rfloor$.
- Missing types needed: $M = 3 - types$.
- Because replacements can simultaneously fulfill missing types:
  $$
  \text{Operations} = \max(R, \; M)
  $$

### 3. Regime 3: Too Long ($N > 20$)
- We must delete at least $D = N - 20$ characters to satisfy the length cap.
- Can deletions help reduce the number of replacements needed to break triplets?
  - In a run of length $L$, if we delete characters, how many deletions does it take to reduce the required replacements by 1?
  - **Class 0 ($L \equiv 0 \pmod 3$, e.g. $L = 3$ `"aaa"`):**
    Deleting **1** character reduces length to $2$ (`"aa"`), reducing replacements from $1 \to 0$. **Efficiency: 1 deletion saves 1 replacement.**
  - **Class 1 ($L \equiv 1 \pmod 3$, e.g. $L = 4$ `"aaaa"`):**
    Deleting **2** characters reduces length to $2$ (`"aa"`), reducing replacements from $1 \to 0$. **Efficiency: 2 deletions save 1 replacement.**
  - **Class 2 ($L \equiv 2 \pmod 3$, e.g. $L = 5$ `"aaaaa"`):**
    Deleting **3** characters reduces length to $2$, reducing replacements from $1 \to 0$. **Efficiency: 3 deletions save 1 replacement.**

> **Greedy Deletion Priority Invariant.** To minimize total operations, mandatory deletions must be spent first on runs with $L \equiv 0 \pmod 3$ (cost 1), then on runs with $L \equiv 1 \pmod 3$ (cost 2), and finally on any runs (cost 3).

---

## 3. Step-by-Step Worked Execution

We trace $password = \text{"aaaaaaaaaaaaaaaaaaaaaa"}$ ($N = 22$):

---

### Step 1: Count Character Types and Deficiencies
- Check character sets:
  - Lowercase: `'a'` present $\implies 1$
  - Uppercase: None $\implies 0$
  - Digit: None $\implies 0$
- Types present: $types = 1$.
- Missing types:
  $$
  M = 3 - 1 = \mathbf{2}
  $$

---

### Step 2: Identify Repeating Runs
- The password has one contiguous run of `'a'` with length $L = 22$.
- Initial replacements required:
  $$
  R = \lfloor 22 / 3 \rfloor = \mathbf{7}
  $$
- Modular category:
  $$
  22 \bmod 3 = \mathbf{1} \quad (\text{Class 1 run})
  $$

---

### Step 3: Apply Mandatory Deletions
- Mandatory deletions needed to reach length 20:
  $$
  D = 22 - 20 = \mathbf{2}
  $$
- Evaluate greedy deletion options:
  - Are there any Class 0 runs ($L \equiv 0$)? None.
  - Are there any Class 1 runs ($L \equiv 1$)? Yes, the single run of length 22!
  - We have $D = 2$ available deletions.
  - Spending $2$ deletions on this run reduces its length:
    $$
    L' = 22 - 2 = 20
    $$
  - New replacements needed for this run:
    $$
    R' = \lfloor 20 / 3 \rfloor = \mathbf{6}
    $$
  - Deletions remaining: $2 - 2 = 0$.
  - Net effect: $2$ deletions saved $1$ replacement ($7 \to 6$).

---

### Step 4: Combine Remaining Replacements and Missing Types
- Remaining replacements to break all triplets: $R' = 6$.
- Missing types: $M = 2$.
- Each replacement can replace an `'a'` with an uppercase letter or digit:
  $$
  \max(R', M) = \max(6, 2) = \mathbf{6}
  $$
- Example modification:
  - Delete 2 `'a'`s $\implies 20$ `'a'`s remain.
  - At index 2, replace `'a'` with `'A'` (supplies uppercase).
  - At index 5, replace `'a'` with `'1'` (supplies digit).
  - At indices 8, 11, 14, 17, replace `'a'` with `'b'` (breaks remaining triplets).
  - Final string: `"aaAaa1aabaabaabaabaa"` (length 20, 3 types, no triplets).

---

### Step 5: Final Operation Sum
$$
\text{Total Operations} = D + \max(R', M) = 2 + 6 = \mathbf{8}
$$

---

## 4. Complete Execution Trace

| Phase | Parameter / State | Value | Rationale |
|:---:|:---|:---:|:---|
| **Length Check** | Initial Length $N$ | $22$ | Exceeds maximum 20; requires $D = 22 - 20 = 2$ deletions |
| **Type Check** | Types Present | $\{ \text{lowercase} \}$ | $types = 1 \implies M = 3 - 1 = 2$ missing types |
| **Run Analysis** | Contiguous Runs | $[22]$ | Single run of 22 `'a'`s ($22 \equiv 1 \pmod 3$, initial $R = 7$) |
| **Greedy Deletion 1** | Class 0 ($L \equiv 0$) | 0 available | No runs with $L \equiv 0 \pmod 3$ |
| **Greedy Deletion 2** | Class 1 ($L \equiv 1$) | Run of 22 | Use $2$ deletions $\implies$ reduces length to 20, saves 1 replacement |
| **Post-Deletion State** | Remaining Deletions | $0$ | Exactly reaches target length 20 |
| **Post-Deletion State** | Remaining Replacements $R'$ | $6$ | $\lfloor 20 / 3 \rfloor = 6$ |
| **Type Substitution** | $\max(R', M)$ | $\max(6, 2) = 6$ | 6 replacements absorb 2 missing character types |
| **Final Answer** | Total Operations | $2 + 6 = \mathbf{8}$ | Minimal operations to achieve strong password |

---

## 5. Boundary Cases & Failure Modes

- **Extremely Short ($N = 1$, e.g. `"a"`):** $N = 1, types = 1 \implies M = 2$. Formula gives $\max(6 - 1, 2) = \mathbf{5}$ insertions (e.g. `"aA1bcd"`).
- **Short with Repeats ($N = 5$, `"aaaaa"`):** $N = 5, types = 1 \implies M = 2$. Required insertions: $6 - 5 = 1$. Inserting 1 character breaks the run into two runs of 2 (e.g. `"aaAaa"`), but still needs a digit $\implies \max(1, 2) = \mathbf{2}$ insertions (e.g. `"aaAaa1"`).
- **Already Strong ($N = 8$, `"1337C0d3"`):** $6 \le N \le 20$, all 3 types present, no triplets $\implies \mathbf{0}$ operations.
- **Many Small Runs ($N = 24$, `"aaa...aaa"` with 8 triplets):** Deletions prioritizing $L \equiv 0$ remove 1 char from each of the first 4 triplets, saving 4 replacements directly.

---

## 6. Traps & Common Anti-Patterns

- **Suboptimal Deletion Allocation:** Deleting characters arbitrarily instead of prioritizing $L \equiv 0 \pmod 3$ wastefully uses deletions without reducing the required replacement count.
- **Double-Counting Replacements and Types:** Treating missing types as additive to replacements ($\text{replacements} + \text{missing}$) rather than taking the maximum $\max(R, M)$ creates unnecessary extra operations.
- **Miscalculating Short Passwords:** Trying to delete characters when $N < 6$ is always suboptimal. Any deletion decreases length, increasing the number of insertions required.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Scanning the password to count character classes and identify contiguous run lengths takes a single pass of $O(N)$ time.
  - The greedy deletion adjustments operate on the identified run counts in $O(1)$ time.
  - Total Time: $\mathcal{O}(N)$. For $N \le 50$, this executes in under a microsecond.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$. Memory is restricted to counters for character types, deletion quotas, and run lengths.
