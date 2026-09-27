# Guided Example: Backspace String Compare

We trace the step-by-step reverse two-pointer scan, backspace debt counter accumulation ($skip \mathrel{+}= 1$), retroactive character absorption ($skip > 0 \implies \text{skip character}$), dual-pointer synchronization on surviving characters, and $O(1)$ auxiliary space string equivalence verification on representative backspace sequences:

- **Input:**
  $$
  s = \text{"ab\#c"}, \quad t = \text{"ad\#c"}
  $$
- **Required output:** `true`
  - Text editor backspace semantics:
    - The character `'#'` denotes a backspace key.
    - Typing a character appends it to the buffer; typing `'#'` deletes the most recent preceding character (if one exists).
    - Backspacing an empty buffer leaves it empty.
    - Objective: Determine if the final rendered strings from $s$ and $t$ are identical, using strictly $\mathcal{O}(1)$ extra memory.
    - For $s = \text{"ab\#c"}$:
      - Type `'a'` $\to$ `"a"`
      - Type `'b'` $\to$ `"ab"`
      - Type `'#'` $\to$ backspaces `'b'` $\to$ `"a"`
      - Type `'c'` $\to$ `"ac"`
    - For $t = \text{"ad\#c"}$:
      - Type `'a'` $\to$ `"a"`
      - Type `'d'` $\to$ `"ad"`
      - Type `'#'` $\to$ backspaces `'d'` $\to$ `"a"`
      - Type `'c'` $\to$ `"ac"`
    - Both strings resolve to `"ac"`.
    - Output: **`true`**.
- **Reverse Pointer & Backspace Debt Invariant:**
  - **The Right-to-Left Traversal Advantage:**
    - A backspace character affects characters that appear **before** it (to its left).
    - Scanning from left to right requires buffering characters on a stack ($\mathcal{O}(N)$ memory).
    - Scanning backwards from right to left allows us to know how many characters must be deleted **before** we even reach them!
  - **The Skip Counter Invariant:**
    - Maintain an integer variable $skip$ tracking the accumulated debt of backspaces.
    - As cursor $i$ steps backwards ($n - 1 \dots 0$):
      - If $s[i] == \text{'\#'}$:
        - Increment debt: $skip \leftarrow skip + 1$.
        - Move cursor: $i \leftarrow i - 1$.
      - Else if $skip > 0$:
        - The current character $s[i]$ is deleted by a pending backspace!
        - Pay off debt: $skip \leftarrow skip - 1$.
        - Move cursor: $i \leftarrow i - 1$.
      - Else ($s[i] \ne \text{'\#'}$ and $skip == 0$):
        - This character $s[i]$ survived all backspaces! Stop skipping; this is the current active character.
  - **Dual Character Comparison:**
    - Locate the next surviving character in $s$ at index $i$, and the next surviving character in $t$ at index $j$.
    - If both survive ($i \ge 0$ and $j \ge 0$):
      - If $s[i] \ne t[j]$, return **`false`** immediately.
      - Decrement both: $i \leftarrow i - 1, j \leftarrow j - 1$.
    - If one string has surviving characters remaining while the other is exhausted, return **`false`**.
    - If both exhaust simultaneously ($i < 0$ and $j < 0$), return **`true`**.
- **Step-by-Step Worked Execution Trace on $s = \text{"ab\#c"}$ and $t = \text{"ad\#c"}$:**
  - Initialize pointers: $i = 3$ (length of $s$ minus 1), $j = 3$ (length of $t$ minus 1).
  - Initialize debts: $skip_1 = 0, skip_2 = 0$.
  - **Round 1 (Locate First Surviving Characters):**
    - **In String $s$ ($i = 3$):**
      - $s[3] = \text{'c'}$. Not `'#'`, $skip_1 = 0 \implies \mathbf{Survives!}$ Active character is `'c'`.
    - **In String $t$ ($j = 3$):**
      - $t[3] = \text{'c'}$. Not `'#'`, $skip_2 = 0 \implies \mathbf{Survives!}$ Active character is `'c'`.
    - **Comparison:**
      - $s[3] == t[3] \iff \text{'c'} == \text{'c'} \implies \mathbf{Match!}$
      - Step backwards: $i \leftarrow 2, j \leftarrow 2$.
  - **Round 2 (Locate Second Surviving Characters):**
    - **In String $s$ ($i = 2$):**
      - $s[2] = \text{'\#'}$: increment debt $skip_1 \leftarrow 1$, advance $i \leftarrow 1$.
      - $s[1] = \text{'b'}$: debt $skip_1 = 1 > 0 \implies \mathbf{Character\ Deleted!}$
        - Pay debt: $skip_1 \leftarrow 0$, advance $i \leftarrow 0$.
      - $s[0] = \text{'a'}$: not `'#'`, $skip_1 = 0 \implies \mathbf{Survives!}$ Active character is `'a'`.
    - **In String $t$ ($j = 2$):**
      - $t[2] = \text{'\#'}$: increment debt $skip_2 \leftarrow 1$, advance $j \leftarrow 1$.
      - $t[1] = \text{'d'}$: debt $skip_2 = 1 > 0 \implies \mathbf{Character\ Deleted!}$
        - Pay debt: $skip_2 \leftarrow 0$, advance $j \leftarrow 0$.
      - $t[0] = \text{'a'}$: not `'#'`, $skip_2 = 0 \implies \mathbf{Survives!}$ Active character is `'a'`.
    - **Comparison:**
      - $s[0] == t[0] \iff \text{'a'} == \text{'a'} \implies \mathbf{Match!}$
      - Step backwards: $i \leftarrow -1, j \leftarrow -1$.
  - **Round 3 (Termination Check):**
    - Both pointers are negative ($i = -1 < 0$ and $j = -1 < 0$).
    - Both strings successfully exhausted with identical characters throughout.
  - **Final Output:**
    $$
    ans = \mathbf{\text{true}}
    $$
- **Empty String Reduction Trace ($s = \text{"ab\#\#"}, t = \text{"c\#d\#"}$):**
  - $s$: `'#'` deletes `'b'`, then `'#'` deletes `'a'`. Pointer $i$ reaches $-1$ with no surviving characters.
  - $t$: `'#'` deletes `'d'`, then `'#'` deletes `'c'`. Pointer $j$ reaches $-1$.
  - Both strings reduce to the empty string $\implies \mathbf{\text{true}}.$
- **Unbalanced Length Trace ($s = \text{"a\#c"}, t = \text{"b"}$):**
  - First round: compares `'c'` with `'b'` $\implies \text{'c'} \ne \text{'b'} \implies \mathbf{\text{false}}.$

This instance demonstrates retroactive stream editing and monoid free group word reduction, mathematically proves why suffix-first stream parsing enables memoryless inverse-operator evaluation, and derives $O(N + M)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given strings $s$ and $t$:
`'#'` means backspace.
Return `true` if both strings are equal after applying all backspaces, using **$O(1)$ extra space**.

```text
s = "ab#c"  -> type a, b, backspace b, type c -> "ac"
t = "ad#c"  -> type a, d, backspace d, type c -> "ac"

Result: true
```

### The Invariant of the Reverse Skip Counter
- Scanning **backwards** from the end lets us count backspaces ahead of time.
- Accumulate $skip$ count for each `'#'`.
- Skip non-`#` characters while $skip > 0$.
- The first unskipped character is the next surviving character.
- Compare surviving characters one by one in $O(1)$ memory.

---

## 2. Conceptual Foundation & Invariants

### 1. Free Monoid Backspace Reduction:
$$
\text{reduce}(\epsilon) = \epsilon, \quad \text{reduce}(w \cdot c) = \text{reduce}(w) \cdot c, \quad \text{reduce}(w \cdot \text{'\#'}) = \text{init}(\text{reduce}(w))
$$

### 2. Backward Fiber Skip State:
$$
(i, skip) \leftarrow \begin{cases}
(i - 1, \; skip + 1) & s[i] = \text{'\#'} \\
(i - 1, \; skip - 1) & s[i] \ne \text{'\#'} \;\land\; skip > 0 \\
(i, \; 0) & \text{Stop: } s[i] \text{ survives}
\end{cases}
$$

> **Inverse Generator Invariant.** The rewrite rule $x \# \to \epsilon$ defines a confluent reduction on strings. Reversing the time arrow converts retroactive deletions into prospective skipping tokens, enabling online streaming equivalence verification with zero lookahead buffer.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"ab\#c"}, t = \text{"ad\#c"}$:

---

### Step 1: Compare from Right
- $s[3] = \text{'c'}, t[3] = \text{'c'}$. Match!
- Decrement to $i = 2, j = 2$.

---

### Step 2: Resolve in $s$
- $s[2] = \text{'\#'} \implies skip = 1$.
- $s[1] = \text{'b'} \implies$ consumed by skip ($skip = 0$).
- $s[0] = \text{'a'} \implies$ survives.

---

### Step 3: Resolve in $t$
- $t[2] = \text{'\#'} \implies skip = 1$.
- $t[1] = \text{'d'} \implies$ consumed by skip ($skip = 0$).
- $t[0] = \text{'a'} \implies$ survives.

---

### Step 4: Compare Surviving Characters
- $s[0] == t[0] \iff \text{'a'} == \text{'a'}$. Match!

---

### Step 5: Output
- Both exhausted $\implies \mathbf{\text{true}}.$

---

## 4. Complete Execution Trace

| Step | Pointer $i$ | Action in $s$ | Pointer $j$ | Action in $t$ | Surviving Pair Compared | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $3$ | Character `'c'` survives | $3$ | Character `'c'` survives | `'c'` vs `'c'` | **Match** |
| $2$ | $2 \to 1 \to 0$ | `'#'` deletes `'b'`; `'a'` survives | $2 \to 1 \to 0$ | `'#'` deletes `'d'`; `'a'` survives | `'a'` vs `'a'` | **Match** |
| **End** | **$-1$** | **String $s$ exhausted** | **$-1$** | **String $t$ exhausted** | **None (Both empty)** | **`true`** |

---

## 5. Boundary Cases & Failure Modes

- **Multiple Consecutive Backspaces ($"a\#\#\#"$):** $skip$ accumulates to 3; skips up to string start without negative indexing errors.
- **Both Empty After Reduction ($"ab\#\#" \to ""`$):** Both pointers exit at $-1 \implies \text{true}$.
- **Different Final Lengths ($"a" \text{ vs } "a\#"$):** One pointer finds a character while the other exhausts $\implies \text{false}$.
- **Mismatch on First Character:** Discovered immediately on the first comparison round.

---

## 6. Traps & Common Anti-Patterns

- **Building Full Reduced Strings in Memory ($O(N)$ Space):** Using a stack or string builder violates the $O(1)$ space constraint of the problem. Two pointers achieve constant space.
- **Forgetting That $skip$ Can Exceed 1:** Multiple backspaces like `##` require a counter, not a boolean flag.
- **Stopping at $i < 0$ While $j \ge 0$:** If one string still has unexamined characters, ensure they are skipped if they are backspaced, rather than immediately declaring a mismatch.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Pointers $i$ and $j$ strictly decrease from $N - 1$ and $M - 1$ down to $-1$.
  - Each character is inspected at most twice.
  - Total Time: strictly linear $\mathcal{O}(N + M)$ where $N, M \le 200$. Completes in $< 0.1$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (only scalar integer pointers and counters).
