# Guided Example: License Key Formatting

We trace the step-by-step alphanumeric character isolation, case normalization ($c \to \text{upper}(c)$), modular first-group sizing ($M \pmod k \text{ or } k$), right-aligned $k$-character block grouping, and hyphen insertion on representative license strings:

- **Input:** $s = \text{"2-5g-3-J"}, \quad k = 2$
- **Required output:** `"2-5G-3J"`
  - Step 1: Filter dashes and convert to uppercase:
    $$
    t = [\text{'2'}, \text{'5'}, \text{'G'}, \text{'3'}, \text{'J'}] \quad (M = 5 \text{ characters})
    $$
  - Step 2: Determine first group size:
    - Every group after the first must have exactly $k = 2$ characters.
    - Total pure characters: $M = 5$.
    - First group size:
      $$
      first = M \pmod k = 5 \pmod 2 = \mathbf{1}
      $$
  - Step 3: Segment into hyphen-separated blocks:
    - Group 1: $1$ character $\implies \text{"2"}$
    - Insert hyphen: `"-"`
    - Group 2: $k = 2$ characters $\implies \text{"5G"}$
    - Insert hyphen: `"-"`
    - Group 3: $k = 2$ characters $\implies \text{"3J"}$
  - Assembled license key: **`"2-5G-3J"`**
- **Evenly Divisible Instance ($s = \text{"5F3Z-2e-9-w"}, k = 4$):**
  - Pure uppercase characters: `"5F3Z2E9W"` ($M = 8$)
  - Modulo: $8 \pmod 4 = 0 \implies first = k = 4$
  - Group 1: `"5F3Z"`, Group 2: `"2E9W"` $\implies \mathbf{\text{"5F3Z-2E9W"}}$
- **All Dashes Input ($s = \text{"---"}, k = 3$):**
  - Zero alphanumeric characters $\implies M = 0 \implies \mathbf{\text{""}}$
- **Single Character Input ($s = \text{"a-a-a-a"}, k = 1$):**
  - Pure chars: `"AAAA"` ($M = 4, k = 1$) $\implies \mathbf{\text{"A-A-A-A"}}$

This instance demonstrates modular string partitioning with variable-length prefix rules, mathematically proves why right-aligned grouping is equivalent to prefix remainder modular arithmetic, and derives $O(N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a license string $s$ consisting of alphanumeric characters and dashes, and an integer $k$:
Reformat $s$ such that:
1. Each group contains exactly $k$ characters, **except the first group**, which may have fewer (between $1$ and $k$).
2. All lowercase letters are converted to uppercase.
3. Groups are separated by a single dash `'-'`.

```text
Original String: "2 - 5 g - 3 - J"   (k = 2)

Step 1: Clean and Capitalize:
        "2", "5", "G", "3", "J"     (Total M = 5 characters)

Step 2: Grouping (Right-to-Left in pairs of 2):
        [2]  -  [5 G]  -  [3 J]
      (1 char) (2 chars) (2 chars)

Output: "2-5G-3J"
```

### The Prefix Sizing Formula
Since grouping is strictly enforced from right to left in blocks of $k$:
- Let $M$ be the count of non-dash characters.
- If $M == 0$, the formatted string is empty.
- The number of characters remaining for the leftmost group is:
  $$
  first = M \pmod k
  $$
- If $M$ is an exact multiple of $k$ ($first == 0$):
  The first group takes a full block of $k$ characters ($first = k$).
- All subsequent groups take exactly $k$ characters.

---

## 2. Conceptual Foundation & Invariants

### 1. Sequential Scanning with Counter:
We can reformat the string in a single forward pass:
- Initialize counter $cnt = (M \pmod k) \text{ or } k$.
- As we iterate through each non-dash character:
  - Append its uppercase form `c.upper()`.
  - Decrement $cnt \leftarrow cnt - 1$.
  - When $cnt == 0$:
    A group boundary has been completed!
    Reset $cnt \leftarrow k$.
    Append a dash `'-'` (unless we are at the very end of the string).
- Finally, strip any trailing dash.

> **Grouping Invariant.** At every stage, exactly $(M - first) \pmod k == 0$ characters remain after the first group, guaranteeing every subsequent segment has length exactly $k$.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"2-5g-3-J"}$ with $k = 2$:

---

### Step 1: Pre-Count Alphanumeric Characters
- Total length: $|s| = 8$.
- Dashes: 3 dashes.
- Pure character count:
  $$
  M = 8 - 3 = \mathbf{5}
  $$
- Compute first group capacity:
  $$
  cnt = (5 \pmod 2) \text{ or } 2 = 1 \text{ or } 2 = \mathbf{1}
  $$

---

### Step 2: Forward Pass & Hyphen Placement
- **Char 1 (`'2'`):**
  - Append `'2'`.
  - Decrement $cnt \leftarrow 1 - 1 = 0$.
  - Boundary reached! Reset $cnt \leftarrow k = 2$. Append `'-'`.
  - Result so far: `["2", "-"]`.
- **Char 2 (`'-'`):** Skip.
- **Char 3 (`'5'`):**
  - Append `'5'`.
  - Decrement $cnt \leftarrow 2 - 1 = 1$.
  - Result: `["2", "-", "5"]`.
- **Char 4 (`'g'`):**
  - Append uppercase `'G'`.
  - Decrement $cnt \leftarrow 1 - 1 = 0$.
  - Boundary reached! Reset $cnt \leftarrow 2$. Append `'-'`.
  - Result: `["2", "-", "5", "G", "-"]`.
- **Char 5 (`'-'`):** Skip.
- **Char 6 (`'3'`):**
  - Append `'3'`.
  - Decrement $cnt \leftarrow 2 - 1 = 1$.
  - Result: `["2", "-", "5", "G", "-", "3"]`.
- **Char 7 (`'-'`):** Skip.
- **Char 8 (`'J'`):**
  - Append `'J'`.
  - Decrement $cnt \leftarrow 1 - 1 = 0$.
  - End of string reached.
  - Result: `["2", "-", "5", "G", "-", "3", "J"]`.

---

### Step 3: Assemble String
Join array:
$$
\mathbf{\text{"2-5G-3J"}}
$$

---

## 4. Complete Execution Trace

| Input Character $c$ | Action | Uppercase Appended | Counter $cnt$ | Group Boundary Triggered? | Hyphen Inserted? | Current Output Buffer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| `'2'` | Process | `'2'` | $0$ | **Yes** (first group done) | Yes | `2-` |
| `'-'` | Skip | — | $2$ | No | No | `2-` |
| `'5'` | Process | `'5'` | $1$ | No | No | `2-5` |
| `'g'` | Process | `'G'` | $0$ | **Yes** (group of 2 done) | Yes | `2-5G-` |
| `'-'` | Skip | — | $2$ | No | No | `2-5G-` |
| `'3'` | Process | `'3'` | $1$ | No | No | `2-5G-3` |
| `'-'` | Skip | — | $1$ | No | No | `2-5G-3` |
| `'J'` | Process | `'J'` | $0$ | **Yes** (group of 2 done) | No (at end) | `2-5G-3J` |

---

## 5. Boundary Cases & Failure Modes

- **String of Only Dashes (`"----"`):** $M = 0 \implies$ loop finishes with empty list $\implies \mathbf{\text{""}}$.
- **$M < k$ ($s = \text{"abc"}, k = 5$):** $first = 3 \pmod 5 = 3$. Entire string forms a single group without hyphens $\implies \mathbf{\text{"ABC"}}$.
- **Exact Multiple ($s = \text{"a-b-c-d"}, k = 2$):** $M = 4, first = 4 \pmod 2 = 0 \implies first = 2$. Output is $\mathbf{\text{"AB-CD"}}$.
- **No Dashes in Input ($s = \text{"abcdef"}, k = 2$):** Formatted into equal blocks $\mathbf{\text{"AB-CD-EF"}}$.

---

## 6. Traps & Common Anti-Patterns

- **Inserting Dashes from Left First Without Modulo:** Chunking from the left in sizes of $k$ leaves the remainder at the *end* of the string instead of the *beginning*, violating the requirement that only the *first* group may be shorter than $k$.
- **Repeated String Concatenation (`ans += c`):** In languages with immutable strings, string concatenation in a loop takes $O(N^2)$ time. Using an array buffer with `join` runs in $O(N)$ time.
- **Dangling Trailing Hyphens:** Placing a hyphen after the final character produces invalid strings like `"2-5G-3J-"`. Guarding with `i != n - 1` or calling `rstrip('-')` guarantees clean endings.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Counting dashes takes $O(N)$ time.
  - The forward loop iterates over $N$ characters once, performing $O(1)$ operations per character.
  - Joining the character buffer takes $O(N)$ time.
  - Total Time: $\mathcal{O}(N)$. For $N = 10^5$, executes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ to store the output character array.
