# Guided Example: Detect Capital

We trace the step-by-step capital letter frequency counting ($cnt = \sum \mathbf{1}[c \in \text{Upper}]$), tri-modal rule taxonomy evaluation (all uppercase $cnt = n$, all lowercase $cnt = 0$, or titlecase $cnt = 1 \land word[0] \in \text{Upper}$), and invalid mixture detection on representative word strings:

- **Input:** $word = \text{"FlaG"}$
- **Required output:** `false`
  - Word length: $n = 4$
  - The 3 legal capital usage conditions:
    1. **All Capitals:** Every character in $word$ is uppercase (e.g. `"USA"`).
    2. **All Lowercase:** No character in $word$ is uppercase (e.g. `"leetcode"`).
    3. **Titlecase:** Exactly the first character is uppercase, and all remaining characters are lowercase (e.g. `"Google"`).
- **Execution trace on `"FlaG"`:**
  - Character casing inspection:
    - Character 0: `'F'` $\to$ **Uppercase**
    - Character 1: `'l'` $\to$ Lowercase
    - Character 2: `'a'` $\to$ Lowercase
    - Character 3: `'G'` $\to$ **Uppercase**
  - Total uppercase characters:
    $$
    cnt = 1 + 0 + 0 + 1 = \mathbf{2}
    $$
  - Evaluate the 3 legal predicates:
    - Condition 1 ($cnt == n$): $2 == 4$ (**False**)
    - Condition 2 ($cnt == 0$): $2 == 0$ (**False**)
    - Condition 3 ($cnt == 1 \land word[0] \in \text{Upper}$): $2 == 1$ (**False**)
  - Capital count $2$ does not match any legal pattern $\implies$ Returns **`false`**.
- **All-Uppercase Instance ($word = \text{"USA"}$):**
  - $n = 3$, characters `['U', 'S', 'A']` are all uppercase.
  - $cnt = 3 == n \implies$ Matches Condition 1 $\implies \mathbf{true}$.
- **Titlecase Instance ($word = \text{"Google"}$):**
  - $n = 6$, uppercase count $cnt = 1$.
  - First character $word[0] = \text{'G'}$ is uppercase.
  - $cnt == 1 \land word[0] \in \text{Upper} \implies$ Matches Condition 3 $\implies \mathbf{true}$.
- **All-Lowercase Instance ($word = \text{"leetcode"}$):**
  - $n = 8$, uppercase count $cnt = 0$.
  - Matches Condition 2 $\implies \mathbf{true}$.
- **Single Character Words (`"A"`, `"z"`):**
  - For `"A"`: $cnt = 1 == n \implies \mathbf{true}$.
  - For `"z"`: $cnt = 0 \implies \mathbf{true}$.

This instance demonstrates predicate classification via aggregate frequency invariants, mathematically proves why partition rules reduce casing validation to three scalar comparisons, and derives $O(N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string $word$:
Determine whether the usage of capital letters is correct according to the three standard English orthographic rules:
1. All letters are capitals (e.g., `"USA"`).
2. All letters are not capitals (e.g., `"leetcode"`).
3. Only the first letter is capital (e.g., `"Google"`).
Return `true` if the usage is valid, and `false` otherwise.

```text
Evaluating "FlaG":
  'F' -> Upper (1)
  'l' -> Lower
  'a' -> Lower
  'G' -> Upper (2)

Total uppercase letters = 2 (Length = 4)
  All upper?   2 == 4 -> False
  All lower?   2 == 0 -> False
  Titlecase?   2 == 1 -> False

Result: false
```

### The Reduction to Uppercase Counting
Rather than managing stateful flag machines or regular expressions:
- Let $n = |word|$ and $cnt$ be the total count of uppercase letters in $word$.
- A word is valid **if and only if**:
  $$
  cnt == 0 \quad \lor \quad cnt == n \quad \lor \quad (cnt == 1 \land word[0] \in \text{Upper})
  $$
- Any word that does not satisfy one of these three exact conditions has invalid capitalization.

---

## 2. Conceptual Foundation & Invariants

### 1. The Tri-Modal Classification Theorem:
Let $cnt = \sum_{c \in word} \mathbf{1}[c \text{ is uppercase}]$:
- If $cnt == 0$: All characters are lowercase $\implies$ **Valid**.
- If $cnt == n$: All characters are uppercase $\implies$ **Valid**.
- If $cnt == 1$: Exactly one capital exists. It is valid if and only if that capital is located at index $0$ ($word[0]$) $\implies$ **Valid**.
- For all other values of $cnt \in [2, n - 1]$: There are mixed capitals that do not cover the whole word $\implies$ **Invalid**.

> **Orthographic Invariant.** The set of valid strings is the disjoint union of $\{\text{all lower}\}$, $\{\text{all upper}\}$, and $\{\text{titlecase}\}$, each uniquely determined by $cnt$ and the position of the single capital.

---

## 3. Step-by-Step Worked Execution

We trace $word = \text{"FlaG"}$ ($n = 4$):

---

### Step 1: Count Uppercase Characters
Iterate through characters:
- Index 0: `'F'` is uppercase $\implies cnt = 1$.
- Index 1: `'l'` is lowercase $\implies cnt = 1$.
- Index 2: `'a'` is lowercase $\implies cnt = 1$.
- Index 3: `'G'` is uppercase $\implies cnt = 2$.
Total uppercase count:
$$
cnt = \mathbf{2}
$$

---

### Step 2: Test Validation Predicates
1. Test All-Lowercase:
   $$
   cnt == 0 \iff 2 == 0 \implies \mathbf{False}
   $$
2. Test All-Uppercase:
   $$
   cnt == n \iff 2 == 4 \implies \mathbf{False}
   $$
3. Test Titlecase:
   $$
   cnt == 1 \land word[0] \in \text{Upper} \iff 2 == 1 \land \text{True} \implies \mathbf{False}
   $$

---

### Step 3: Emit Output
All three predicates failed.
Output:
$$
\mathbf{false}
$$

---

## 4. Complete Execution Trace

| Word Tested | Length $n$ | Uppercase Count $cnt$ | $cnt == 0$? | $cnt == n$? | $cnt == 1 \land word[0] \in \text{Upper}$? | Valid? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `"USA"` | $3$ | $3$ | False | **True** | False | **`true`** |
| `"leetcode"` | $8$ | $0$ | **True** | False | False | **`true`** |
| `"Google"` | $6$ | $1$ | False | False | **True** | **`true`** |
| **`"FlaG"`** | $4$ | $2$ | False | False | False | **`false`** |
| `"gOOGLE"` | $6$ | $5$ | False | False | False | **`false`** |
| `"leetcodE"` | $8$ | $1$ | False | False | False ($word[0]$ is `'l'`) | **`false`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Uppercase Letter (`"A"`):** $n = 1, cnt = 1 == n \implies \mathbf{true}$.
- **Single Lowercase Letter (`"a"`):** $n = 1, cnt = 0 \implies \mathbf{true}$.
- **Capital at End Only (`"leetcodE"`):** $cnt = 1$, but $word[0] = \text{'l'}$ is not uppercase $\implies$ titlecase check correctly returns $\mathbf{false}$.
- **Inverted Titlecase (`"gOOGLE"`):** $cnt = 5 \notin \{0, 6\}$ and $word[0]$ is lowercase $\implies \mathbf{false}$.

---

## 6. Traps & Common Anti-Patterns

- **Checking Only $cnt == 1$ for Titlecase:** If a word is `"mL"`, $cnt = 1$, but the capital is at index 1, not index 0. You must explicitly verify `word[0].isupper()`.
- **Using Slow String Allocations (`word == word.upper()`):** Generating new upper/lowercase string copies creates unnecessary heap allocations. Character-level counting runs with zero heap allocations.
- **Overcomplicating with Regex:** Regex expressions like `^[A-Z]+$|^[a-z]+$|^[A-Z][a-z]+$` incur regex engine compilation and parsing overhead for a problem that evaluates with 3 integer comparisons.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Counting uppercase characters takes a single pass over the string of length $N$.
  - Evaluating the boolean expressions takes $O(1)$ scalar comparisons.
  - Total Time: $\mathcal{O}(N)$. For $N \le 100$, completes in $< 1$ microsecond.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ extra space using a single integer counter.
