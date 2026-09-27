# Guided Example: Shortest Completing Word

We trace the step-by-step alphanumeric character filtering, lowercase normalization, multiset character frequency requirement construction ($cnt[c]$), word-by-word containment verification ($t[c] \ge cnt[c]$), strict length minimization ($|w| < |ans|$), first-occurrence tie-breaking preservation, and candidate selection on representative vocabulary lists:

- **Input:**
  - License plate: $licensePlate = \text{"1s3 PSt"}$
  - Vocabulary: $words = [\text{"step"}, \; \text{"steps"}, \; \text{"stripe"}, \; \text{"stepple"}]$
- **Required output:** `"steps"`
  - Completing word criteria:
    1. **Alphanumeric Filtering & Case Insensitivity:**
       - Ignore all digits, spaces, and punctuation in $licensePlate$.
       - Convert all letters to lowercase.
    2. **Multiplicity Requirement:**
       - If a letter appears $k$ times in $licensePlate$, a completing word must contain that letter **at least $k$ times**.
    3. **Shortest Length & Tie-Breaking:**
       - Find the completing word with the **minimum total character length**.
       - If there is a tie for the minimum length, return the **first one** that occurs in $words$.
    - For the input:
      - Plate letters in `"1s3 PSt"`:
        - Digits `1` and `3`, and space `' '` are discarded.
        - Letters: `'s'`, `'P'`, `'S'`, `'t'`.
        - Normalizing to lowercase: `'s'`, `'p'`, `'s'`, `'t'`.
        - Required multiset: $\{\text{'s'}: 2, \; \text{'p'}: 1, \; \text{'t'}: 1\}$.
      - Testing words:
        - `"step"`: Contains only one `'s'` (needs 2) $\implies$ Incomplete.
        - `"steps"`: Contains two `'s'`, one `'p'`, one `'t'`, one `'e'`. Fulfills all requirements! Length $= 5$.
        - `"stripe"`: Contains only one `'s'` $\implies$ Incomplete.
        - `"stepple"`: Contains only one `'s'` $\implies$ Incomplete.
      - Shortest valid completing word: `"steps"`.
- **Multiset Subbag Inclusion & Greedy Replacement Invariant:**
  - **The Subbag Relation ($cnt \subseteq t$):**
    - Let $cnt$ be the multiset of required character frequencies extracted from $licensePlate$.
    - A candidate word $w$ with character frequency multiset $t$ is a completing word if and only if:
      $$
      \forall (c, k) \in cnt: \quad t[c] \ge k
      $$
  - **Length Minimization & Strict Replacement Rule:**
    - To satisfy the tie-breaking invariant (keep the *first* completing word among ties of minimal length):
      - If we currently hold a valid completing word $ans$:
        - Any future candidate $w$ with $|w| \ge |ans|$ can be skipped immediately!
        - A candidate replaces $ans$ if and only if it is a valid completing word **and** its length is strictly shorter:
          $$
          |w| < |ans| \implies ans \leftarrow w
          $$
- **Step-by-Step Worked Execution Trace on $licensePlate = \text{"1s3 PSt"}$:**
  - **Phase 0: Build Plate Multiset:**
    - Scan characters of `"1s3 PSt"`:
      - `'1'`: digit $\to$ skip.
      - `'s'`: letter $\to cnt[\text{'s'}] \leftarrow 1$.
      - `'3'`: digit $\to$ skip.
      - `' '`: space $\to$ skip.
      - `'P'`: letter $\to cnt[\text{'p'}] \leftarrow 1$.
      - `'S'`: letter $\to cnt[\text{'s'}] \leftarrow 2$.
      - `'t'`: letter $\to cnt[\text{'t'}] \leftarrow 1$.
    - Required frequencies:
      $$
      cnt = \{ \text{'s'}: 2, \; \text{'p'}: 1, \; \text{'t'}: 1 \}
      $$
    - Initialize $ans = \text{null}$.
  - **Phase 1: Test Candidate Words:**
    - **Candidate 1: $w = \text{"step"}$ (Length 4):**
      - Frequencies of `"step"`: $\{\text{'s'}: 1, \; \text{'t'}: 1, \; \text{'e'}: 1, \; \text{'p'}: 1\}$.
      - Check requirements:
        - $t[\text{'s'}] = 1 < cnt[\text{'s'}] = 2 \implies \mathbf{Fails\ 's'\ requirement!}$
      - Discard.
    - **Candidate 2: $w = \text{"steps"}$ (Length 5):**
      - Frequencies of `"steps"`: $\{\text{'s'}: 2, \; \text{'t'}: 1, \; \text{'e'}: 1, \; \text{'p'}: 1\}$.
      - Check requirements:
        - $t[\text{'s'}] = 2 \ge 2$ (Pass).
        - $t[\text{'p'}] = 1 \ge 1$ (Pass).
        - $t[\text{'t'}] = 1 \ge 1$ (Pass).
      - All requirements satisfied!
      - Since $ans$ was null, adopt:
        $$
        ans \leftarrow \mathbf{\text{"steps"}} \quad (|ans| = 5)
        $$
    - **Candidate 3: $w = \text{"stripe"}$ (Length 6):**
      - Pruning check: $|w| = 6 \ge |ans| = 5$.
      - Length is greater than or equal to current best $\implies$ Skip without counting!
    - **Candidate 4: $w = \text{"stepple"}$ (Length 7):**
      - Pruning check: $|w| = 7 \ge |ans| = 5$.
      - Skip immediately!
  - **Phase 2: Final Result:**
    $$
    ans = \mathbf{\text{"steps"}}
    $$
- **First-Occurrence Tie-Breaking Trace ($licensePlate = \text{"1s3 456"}, words = [\text{"looks"}, \text{"pest"}, \text{"stew"}, \text{"show"}]$):**
  - Required: $\{\text{'s'}: 1\}$.
  - `"pest"` (length 4) is valid $\implies ans \leftarrow \text{"pest"}$.
  - `"stew"` (length 4) is valid, but $|w| == |ans|$ (not strictly shorter) $\implies$ rejected to preserve first occurrence!
  - `"show"` (length 4) is valid $\implies$ rejected.
  - Returns `"pest"`.

This instance demonstrates multiset subbag containment checking and order-preserving argmin search, mathematically proves why strict length inequality preserves stable first-occurrence tie breaking, and derives $O(N \cdot L + P)$ runtime and $O(1)$ alphabet space bounds.

---

## 1. Instance & Teaching Goal

Given a string $licensePlate$ and an array of $words$:
Find the **shortest completing word** containing all letters from $licensePlate$ (case-insensitive, matching multiplicity).
Ignore numbers and spaces. Return the **first** occurring word in case of a length tie.

```text
licensePlate = "1s3 PSt"
letters required: 's' (twice), 'p' (once), 't' (once)

words:
  "step":    has 1 's' -> fails
  "steps":   has 2 's', 1 'p', 1 't' -> VALID! (length 5)
  "stripe":  length 6 >= 5 -> skip
  "stepple": length 7 >= 5 -> skip

Result: "steps"
```

### The Invariant of Multiset Subbag Containment
- A word $w$ is a completing word if for all required characters $c$, $count_w(c) \ge count_{plate}(c)$.
- Keeping $ans$ updated only when $|w| < |ans|$ naturally guarantees that length ties preserve the first occurring word.

---

## 2. Conceptual Foundation & Invariants

### 1. Plate Multiset Construction:
$$
cnt = \text{Multiset}(\{ c.\text{lower}() \mid c \in licensePlate, \; c \in [a-z, A-Z] \})
$$

### 2. Candidate Invariance:
$$
w \text{ completes plate} \iff \forall c \in cnt: \quad \text{count}_w(c) \ge cnt[c]
$$
$$
ans \leftarrow w \iff w \text{ completes plate} \ \land \ (|w| < |ans|)
$$

> **Multiset Projection Invariant.** The letter extraction operator $\pi: \Sigma^* \to \mathbb{N}^{26}$ projects strings into a commutative monoid, whose natural partial order $a \le b \iff \forall i: a_i \le b_i$ uniquely defines completing word validity.

---

## 3. Step-by-Step Worked Execution

We trace $licensePlate = \text{"1s3 PSt"}$:

---

### Step 1: Parse Plate
- Plate letters: `'s'` (2), `'p'` (1), `'t'` (1).

---

### Step 2: Check Words
- `"step"`: only 1 `'s'` $\implies$ Invalid.
- `"steps"`: has 2 `'s'`, 1 `'p'`, 1 `'t'` $\implies$ Valid, length 5 $\implies ans = \text{"steps"}$.
- `"stripe"`: length $6 \ge 5 \implies$ Skip.
- `"stepple"`: length $7 \ge 5 \implies$ Skip.

---

### Step 3: Output
$$
\mathbf{\text{"steps"}}
$$

---

## 4. Complete Execution Trace

| Word $w$ | Length $|w|$ | Pruned by Length? | 's' Count | 'p' Count | 't' Count | Valid? | Best Word $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `"step"` | $4$ | No | $1 < 2$ (Fail) | $1$ | $1$ | No | None |
| **`"steps"`** | **$5$** | **No** | **$2 \ge 2$** | **$1 \ge 1$** | **$1 \ge 1$** | **Yes** | **`"steps"`** |
| `"stripe"` | $6$ | Yes ($6 \ge 5$) | — | — | — | — | `"steps"` |
| `"stepple"`| $7$ | Yes ($7 \ge 5$) | — | — | — | — | `"steps"` |
| **Final** | — | — | — | — | — | — | **`"steps"`** |

---

## 5. Boundary Cases & Failure Modes

- **Tied Lengths:** If two valid words have the same shortest length, the first one seen is retained because replacement requires $|w| < |ans|$.
- **Plate Has Single Letter ($"a"$):** Any word with at least one `'a'` qualifies.
- **Words with Uppercase Characters:** Problem states words contain only lowercase letters.
- **Extra Characters in Words:** Completing words may contain other letters (e.g. `'e'`, `'r'`) not in the plate.

---

## 6. Traps & Common Anti-Patterns

- **Replacing on Equal Length ($|w| \le |ans|$):** Using $\le$ instead of $<$ would replace the first shortest completing word with subsequent ties, violating the specification to return the first one.
- **Ignoring Multiplicity:** Checking `set(plate).issubset(set(w))` ignores repeated letters. A multiset frequency count ($Counter$) is required.
- **Case Sensitivity:** Failing to convert plate letters to lowercase (e.g. `'P'` vs `'p'`) causes false mismatches.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Parsing plate: $\mathcal{O}(P)$ where $P = |licensePlate| \le 7$.
  - Testing $N$ words of max length $L$: $\mathcal{O}(N \cdot L)$ where $N \le 1000, L \le 15$.
  - Total Time: strictly linear $\mathcal{O}(P + N \cdot L)$. Completes in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space (frequency tables of size $\le 26$ for the English alphabet).
