# Guided Example: Valid Parenthesis String

We trace the step-by-step interval dynamic programming formulation ($dp[i][j]$ on substring $s[i \dots j]$), tri-state wildcard branch semantics (`*` as `'('`, `')'`, or empty string `""`), single-character base states ($dp[i][i] \iff s[i] == \text{'*'}$), enclosing pair reduction ($s[i] \in \text{"(*"} \land s[j] \in \text{"*)"} \land dp[i+1][j-1]$), interval concatenation decomposition ($dp[i][k] \land dp[k+1][j]$), and complete bracket validity determination on representative wildcard strings:

- **Input:** $s = \text{"(*)"}$
- **Required output:** `true`
  - Valid parenthesis rules:
    - Every left parenthesis `'('` must have a matching right parenthesis `')'`.
    - Every right parenthesis `')'` must have a matching left parenthesis `'('`.
    - Openers must precede their corresponding closers.
    - Special wildcard rule: `'*'` may represent:
      1. An open parenthesis `'('`
      2. A closed parenthesis `')'`
      3. An empty string `""`
    - In `"(*)"`, treating `'*'` as an empty string yields `"()"`, which is balanced $\implies$ **True**.
- **Interval Parsing & Wildcard Reduction Invariant:**
  - **The Tri-State Wildcard:**
    - Unlike standard parenthesis matching where characters have fixed roles, each `'*'` can morph into three distinct syntactic entities.
  - **Interval Dynamic Programming State ($dp[i][j]$):**
    - Let $dp[i][j]$ be a boolean value indicating whether the substring $s[i \dots j]$ can form a valid balanced parenthesis string.
  - **Base Cases (Length 1 Substrings):**
    - A single character can never be balanced if it is `'('` or `')'`.
    - A single `'*'` can act as the empty string `""`, which is trivially balanced:
      $$
      dp[i][i] = (s[i] == \text{'*'})
      $$
  - **Recursive Interval Transitions for Substring $s[i \dots j]$ ($j > i$):**
    1. **Outer Enclosure Match:**
       - If $s[i]$ can act as an open bracket ($s[i] \in \{\text{'('}, \; \text{'*'}\}$) AND $s[j]$ can act as a close bracket ($s[j] \in \{\text{')'}, \; \text{'*'}\}$):
         - If $i + 1 == j$ (adjacent pair like `()` or `**`), they match directly.
         - If $i + 1 < j$, the inner substring $s[i+1 \dots j-1]$ must also be valid ($dp[i+1][j-1] == \mathbf{True}$).
         $$
         dp[i][j] = (s[i] \in \text{"(*"} \land s[j] \in \text{"*)"} \land (i + 1 == j \lor dp[i + 1][j - 1]))
         $$
    2. **Concatenation of Two Valid Substrings:**
       - If the interval can be split at some intermediate point $k \in [i, j-1]$ such that both halves are valid:
         $$
         dp[i][j] = dp[i][j] \lor \bigvee_{k=i}^{j-1} \left( dp[i][k] \land dp[k + 1][j] \right)
         $$
- **Step-by-Step Worked Execution Trace on $s = \text{"(*)"}$ ($n = 3$):**
  - Indices: $0 = \text{'('}, \; 1 = \text{'*'}, \; 2 = \text{')'}$.
  - **Phase 1: Length 1 Substrings ($j - i = 0$):**
    - Substring $s[0 \dots 0] = \text{"("}$:
      $$
      dp[0][0] = (\text{'('} == \text{'*'}) = \mathbf{False}
      $$
    - Substring $s[1 \dots 1] = \text{"*"}$:
      $$
      dp[1][1] = (\text{'*'} == \text{'*'}) = \mathbf{True}
      $$
      *(Because `*` can disappear as empty string `""`)*
    - Substring $s[2 \dots 2] = \text{")"}$:
      $$
      dp[2][2] = (\text{')'} == \text{'*'}) = \mathbf{False}
      $$
  - **Phase 2: Length 2 Substrings ($j - i = 1$):**
    - **Substring $s[0 \dots 1] = \text{"(*"}$:**
      - Enclosure test: $s[0] = \text{'('} \in \text{"(*"}$, but $s[1] = \text{'*'} \in \text{"*)"}$.
      - Adjacent pair ($i + 1 == j$): matches directly!
      - Can form `"()"` by treating `'*'` as `')'`.
      - $dp[0][1] = \mathbf{True}$.
    - **Substring $s[1 \dots 2] = \text{"*)"}$:**
      - Enclosure test: $s[1] = \text{'*'} \in \text{"(*"}$, and $s[2] = \text{')'} \in \text{"*)"}$.
      - Adjacent pair: matches directly!
      - Can form `"()"` by treating `'*'` as `'('`.
      - $dp[1][2] = \mathbf{True}$.
  - **Phase 3: Length 3 Substrings ($j - i = 2$, Full String $s[0 \dots 2] = \text{"(*)"}$):**
    - **Test 1: Enclosure Transition:**
      - Left character: $s[0] = \text{'('} \in \text{"(*"}$ $\implies$ Valid opener.
      - Right character: $s[2] = \text{')'} \in \text{"*)"}$ $\implies$ Valid closer.
      - Inner core substring: $s[i+1 \dots j-1] = s[1 \dots 1] = \text{"*"}$.
      - Query inner state:
        $$
        dp[1][1] = \mathbf{True}
        $$
      - Enclosure condition evaluates to:
        $$
        \mathbf{True} \land \mathbf{True} \land dp[1][1] = \mathbf{True}!
        $$
      - Outer pair `'('` and `')'` match each other, while the inner `'*'` dissolves into the empty string `""`!
      - Set:
        $$
        dp[0][2] = \mathbf{True}
        $$
  - **Step 4: Output Evaluation:**
    - Full string query:
      $$
      ans = dp[0][n - 1] = dp[0][2] = \mathbf{True}
      $$
    - Return **`true`**.
- **Alternative Interpretations on $s = \text{"(*))"}$:**
  - Prefix `"(*"` treats `'*'` as `'('` $\implies$ `"(()"`.
  - Suffix `")"` closes it $\implies$ `"(())"` which is balanced $\implies$ **True**.
- **Unmatchable Imbalance ($s = \text{")("}$):**
  - Closer precedes opener.
  - $s[0] = \text{')'} \notin \text{"(*"}$.
  - No split yields valid components $\implies$ Returns **`false`**.

This instance demonstrates interval dynamic programming on context-free languages with wildcard expansion, mathematically proves why single-character empty reductions anchor inductive bracket matching, and derives $O(N^3)$ interval DP (or $O(N)$ linear open-bracket range tracking) runtime bounds.

---

## 1. Instance & Teaching Goal

Given a string containing `'('`, `')'`, and `'*'`:
Each `'*'` can be `'('`, `')'`, or empty `""`.
Determine if the string can be a **valid balanced parenthesis string**.

```text
s = "(*)"

Interpretations of '*':
  1. As '(': "(()" -> Not balanced.
  2. As ')': "())" -> Not balanced.
  3. As "":  "()"  -> BALANCED!

Result: true
```

### The Invariant of Bracket Decomposition
A balanced substring $s[i \dots j]$ must either:
1. Be enclosed by matching outer brackets: $s[i]$ matches $s[j]$ and inner core $s[i+1 \dots j-1]$ is valid.
2. Be a concatenation of two valid parts: $s[i \dots k]$ and $s[k+1 \dots j]$ are both valid.
3. A single character is valid only if it is `'*'` (acting as empty string `""`).

---

## 2. Conceptual Foundation & Invariants

### 1. The Dynamic Programming Recurrence:
Base case:
$$
dp[i][i] = (s[i] == \text{'*'})
$$
For interval $[i, j]$:
$$
\text{Enclosure: } s[i] \in \text{"(*"} \land s[j] \in \text{"*)"} \land (i + 1 == j \lor dp[i + 1][j - 1])
$$
$$
\text{Concatenation: } \exists k \in [i, j-1]: dp[i][k] \land dp[k + 1][j]
$$
$$
dp[i][j] = \text{Enclosure} \lor \text{Concatenation}
$$

### 2. Equivalent Linear Greedy Invariant ($O(N)$):
Track range of possible open brackets $[low, high]$:
- Open bracket `'('`: increment both $[low+1, high+1]$.
- Close bracket `')'`: decrement both $[\max(0, low-1), high-1]$.
- Wildcard `'*'`: can be `(`, `)`, or `""` $\implies [\max(0, low-1), high+1]$.
- Valid if and only if $high \ge 0$ throughout and $low == 0$ at the end.

> **Context-Free Wildcard Parsing Invariant.** The language of balanced parentheses with empty-transition wildcards admits an unambiguous Cocke-Younger-Kasami (CYK) dynamic programming decomposition over the Chomsky normal form interval basis.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"(*)"}$:

---

### Step 1: Base Table
- $dp[0][0] = \text{False}$ (`'('`)
- $dp[1][1] = \text{True}$ (`'*'`)
- $dp[2][2] = \text{False}$ (`')'`)

---

### Step 2: Length 2
- $s[0 \dots 1] = \text{"(*"} \implies \text{True}$.
- $s[1 \dots 2] = \text{"*)"} \implies \text{True}$.

---

### Step 3: Length 3 ($s[0 \dots 2] = \text{"(*)"}$)
- Enclosure: $s[0] = \text{'('} \in \text{"(*"}$, $s[2] = \text{')'} \in \text{"*)"}$.
- Inner: $dp[1][1] = \text{True}$.
- $dp[0][2] = \mathbf{True}$.

---

### Step 4: Output
$$
\mathbf{true}
$$

---

## 4. Complete Execution Trace

| Interval $[i, j]$ | Substring | Enclosure Condition | Inner Substring State | Concatenation Split Found? | Computed $dp[i][j]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $[0, 0]$ | `"("` | Base ($s[0] == \text{'*'}$) | — | — | $\mathbf{False}$ |
| $[1, 1]$ | `"*"` | Base ($s[1] == \text{'*'}$) | — | — | $\mathbf{True}$ |
| $[2, 2]$ | `")"` | Base ($s[2] == \text{'*'}$) | — | — | $\mathbf{False}$ |
| $[0, 1]$ | `"(*"` | $s[0] \in \text{"(*"}, s[1] \in \text{"*)"}$ | Adjacent | — | $\mathbf{True}$ |
| $[1, 2]$ | `"*)"` | $s[1] \in \text{"(*"}, s[2] \in \text{"*)"}$ | Adjacent | — | $\mathbf{True}$ |
| **$[0, 2]$** | **`"(*)"`** | **$s[0]=\text{'('}, s[2]=\text{')'}$** | **$dp[1][1] = \mathbf{True}$** | — | **`True`** |

---

## 5. Boundary Cases & Failure Modes

- **Empty String:** Trivially valid ($true$).
- **All Wildcards ($s = \text{"***"}$):** All dissolve into empty strings $\implies true$.
- **Closing Bracket First ($s = \text{")*("}$):** $high$ drops below 0 immediately $\implies false$.
- **More Openers Than Wildcards ($s = \text{"((("}$):** Unclosed at termination $\implies false$.

---

## 6. Traps & Common Anti-Patterns

- **Treating `*` Only as `(` or `)`:** Forgetting that `'*'` can also represent the **empty string `""`** causes false negatives on strings like `"(*)"`.
- **Greedy Stack Without Range Boundaries:** Using a naive single integer stack count cannot handle the 3-way branching of `'*'`. You must track either the $[low, high]$ interval or use interval DP.
- **Wrong Loop Direction in DP:** Outer loop must iterate backwards ($i = n - 2 \dots 0$) and inner loop forwards ($j = i + 1 \dots n - 1$) so that shorter intervals are solved before longer ones.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Interval DP: $N$ values for $i$, $N$ values for $j$, and up to $N$ split points $k$.
  - Total Time: $\mathcal{O}(N^3)$ operations. For $N \le 100$, takes $\approx 1.6 \times 10^5$ operations, running in $< 5$ ms.
  - *(The linear greedy $[low, high]$ range approach runs in $\mathcal{O}(N)$ time).*
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N^2)$ space for the dynamic programming table $dp$.
