# Guided Example: Encode String with Shortest Length

We trace the step-by-step interval dynamic programming ($f[i][j]$), string doubling periodicity detection ($(t + t).\text{index}(t, 1)$), encoding overhead threshold ($L < 5$), split-point partitioning ($f[i][k] + f[k+1][j]$), and nested bracket compression on representative string instances:

- **Input:** $s = \text{"aaaaa"}$
- **Required output:** `"5[a]"`
  - Substring length: $L = 5$
  - Literal representation: `"aaaaa"` (Length 5)
  - Period detection on $t = \text{"aaaaa"}$:
    - Doubled string: $t + t = \text{"aaaaaaaaaa"}$
    - First internal match of $t$ in $(t + t)[1:]$: occurs at index $pos = 1$
    - Since $pos = 1 < L$: String is periodic with period length $1$ (repeating unit `"a"`)
    - Repetition count: $cnt = 5 / 1 = 5$
    - Encoded representation:
      $$
      5[\text{encode}(s[0 \dots 0])] = \text{"5[a]"}
      $$
    - Length of encoded form: $4$ characters (`'5'`, `'['`, `'a'`, `']'`)
    - Comparison: $4 < 5 \implies$ Encoded form is strictly shorter!
  - Optimal result: **`"5[a]"`**
- **Below Overhead Threshold Instance:** $s = \text{"aaa"}$ ($L = 3$)
  - Encoded candidate: `"3[a]"` has length $4$.
  - Literal `"aaa"` has length $3$.
  - Since $4 > 3$, compression increases string length $\implies$ Return literal **`"aaa"`**
- **Multi-Character Unit Instance:** $s = \text{"abcabcabc"}$ ($L = 9$)
  - Period $pos = 3$, repeating unit `"abc"`, count $9 / 3 = 3$
  - Encoded: `"3[abc]"` (Length 6 vs 9) $\implies \mathbf{\text{"3[abc]"}}$
- **Nested Compression Instance:** $s = \text{"a"}\times 10 \implies \mathbf{\text{"10[a]"}}$ (Length 5 vs 10)

This instance demonstrates interval dynamic programming with periodic compression grammars, mathematically proves why lengths $< 5$ never benefit from repetition syntax, and derives $O(N^3)$ runtime and $O(N^2)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string $s$:
Encode the string such that its encoded length is the **shortest possible**.
The encoding rule is:
$$
k[\text{encoded\_string}]
$$
Where the `encoded_string` inside square brackets is repeated exactly $k$ times ($k > 0$).
If encoding does not make the string strictly shorter, leave it unencoded.

```text
Evaluating "aaaaa" (Length 5):
  Option 1 (Literal): "aaaaa"      (Length 5)
  Option 2 (Encoded): "5[a]"       (Length 4)
  Optimal: "5[a]"

Evaluating "aaa" (Length 3):
  Option 1 (Literal): "aaa"        (Length 3)
  Option 2 (Encoded): "3[a]"       (Length 4)
  Optimal: "aaa" (Encoding adds 1 extra character)
```

### The 4-Character Overhead Rule
Why is length 5 the minimal threshold for compression?
- Repetition syntax requires at least:
  - 1 digit for the count $k \ge 2$
  - 1 opening bracket `'['`
  - 1 character for the unit pattern
  - 1 closing bracket `']'`
- Total minimum syntax overhead: $1 + 1 + 1 + 1 = 4$ characters.
- For a string of length $L \le 4$:
  - $L = 1$: `"a"` $\to$ `"1[a]"` (4 chars, longer).
  - $L = 2$: `"aa"` $\to$ `"2[a]"` (4 chars, longer).
  - $L = 3$: `"aaa"` $\to$ `"3[a]"` (4 chars, longer).
  - $L = 4$: `"aaaa"` $\to$ `"4[a]"` (4 chars, equal, no gain).
- Therefore, for any substring of length $< 5$, the shortest encoding is **unconditionally the literal substring itself**.

---

## 2. Conceptual Foundation & Invariants

### 1. The Periodicity Extraction Operator:
For any substring $t = s[i \dots j]$ of length $L \ge 5$:
- Search for the first non-zero shift in $(t + t)$ matching $t$:
  $$
  pos = (t + t).\text{index}(t, 1)
  $$
- If $pos < L$:
  - The minimal period length is $pos$, with repeating unit $s[i \dots i + pos - 1]$.
  - The repetition count is $cnt = L / pos$.
  - Candidate periodic encoding:
    $$
    \text{candidate} = \text{str}(cnt) + \text{"["} + f[i][i + pos - 1] + \text{"]"}
    $$

### 2. Interval Dynamic Programming (Split Transitions):
Let $f[i][j]$ be the shortest encoded string for $s[i \dots j]$:
1. Initialize $f[i][j]$ using the best self-periodic encoding (or literal string $t$ if not periodic or if $L < 5$).
2. If $L \ge 5$, test all internal partition boundaries $k \in [i, j - 1]$:
   $$
   \text{split} = f[i][k] + f[k + 1][j]
   $$
   If $|\text{split}| < |f[i][j]|$:
   $$
   f[i][j] \leftarrow \text{split}
   $$
3. By iterating interval lengths from $1$ to $N$, smaller subproblems are fully solved before larger intervals query them.

> **Optimal Substructure Invariant.** The shortest encoding of substring $s[i \dots j]$ is either its fully folded periodic compression $cnt[f[i \dots i+pos-1]]$ or the concatenation of two independently optimal sub-encodings $f[i][k] + f[k+1][j]$.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"aaaaa"}$ ($N = 5$):

---

### Step 1: Subproblems of Lengths 1 to 4
For all intervals of length $L < 5$:
- Length 1: $f[0][0] = \text{"a"}, \; f[1][1] = \text{"a"}, \dots$
- Length 2: $f[0][1] = \text{"aa"}, \dots$
- Length 3: $f[0][2] = \text{"aaa"}, \dots$
- Length 4: $f[0][3] = \text{"aaaa"}, \dots$
None can be compressed shorter than their literal lengths.

---

### Step 2: Interval of Length 5 ($s[0 \dots 4] = \text{"aaaaa"}$)
- Evaluate periodic compression on $t = \text{"aaaaa"}$ ($L = 5$):
  - Find internal match in $t + t = \text{"aaaaaaaaaa"}$:
    $$
    (t + t)[1:].\text{find}(\text{"aaaaa"}) \implies pos = 1
    $$
  - Period length $pos = 1 < 5$ (**Periodic!**).
  - Repetition count:
    $$
    cnt = 5 / 1 = \mathbf{5}
    $$
  - Sub-unit optimal encoding:
    $$
    f[0][0 + 1 - 1] = f[0][0] = \text{"a"}
    $$
  - Construct periodic string:
    $$
    f[0][4] \leftarrow \text{str}(5) + \text{"["} + f[0][0] + \text{"]"} = \mathbf{\text{"5[a]"}} \quad (\text{Length } 4)
    $$

---

### Step 3: Test Split Points for $s[0 \dots 4]$
Examine all partition splits $k \in [0, 3]$:
- $k = 0: f[0][0] + f[1][4] = \text{"a"} + \text{"aaaa"} = \text{"aaaaa"}$ (Length 5)
- $k = 1: f[0][1] + f[2][4] = \text{"aa"} + \text{"aaa"} = \text{"aaaaa"}$ (Length 5)
- $k = 2: f[0][2] + f[3][4] = \text{"aaa"} + \text{"aa"} = \text{"aaaaa"}$ (Length 5)
- $k = 3: f[0][3] + f[4][4] = \text{"aaaa"} + \text{"a"} = \text{"aaaaa"}$ (Length 5)
None are shorter than $\text{"5[a]"}$ (length 4).
Thus, $f[0][4]$ remains $\mathbf{\text{"5[a]"}}$.

---

## 4. Complete Execution Trace

| Substring Span $[i, j]$ | Substring Text | Length $L$ | Periodic Unit | Repetition Count | Periodic Encoded Form | Best Split Candidate | Optimal $f[i][j]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $[0, 0]$ | `"a"` | $1$ | — | — | `"a"` | — | `"a"` |
| $[0, 1]$ | `"aa"` | $2$ | `"a"` | $2$ | `"2[a]"` (len 4) | — | `"aa"` |
| $[0, 2]$ | `"aaa"` | $3$ | `"a"` | $3$ | `"3[a]"` (len 4) | — | `"aaa"` |
| $[0, 3]$ | `"aaaa"` | $4$ | `"a"` | $4$ | `"4[a]"` (len 4) | `"aa"+"aa"` (len 4) | `"aaaa"` |
| **$[0, 4]$** | **`"aaaaa"`** | **$5$** | **`"a"`** | **$5$** | **`"5[a]"` (len 4)** | `"aaaaa"` (len 5) | **`"5[a]"`** |

---

## 5. Boundary Cases & Failure Modes

- **String Length $< 5$ ($s = \text{"abcd"}):$** Loop skips compression checks $\implies$ returns literal $s$.
- **Non-Compressible Random String ($s = \text{"abcdef"}$):** Period detection yields $pos = L$. Split partitions combine literals $\implies$ returns `"abcdef"`.
- **Nested Repetitions ($s = \text{"a"}\times 20$):** Can form `"20[a]"` (length 5) or `"2[10[a]]"` (length 7). $f$ dynamically selects the representation with minimal string length.
- **Multiple Disjoint Repeating Blocks ($s = \text{"aaaaabbbbb"}$):** Split at $k = 4$ combines $f[0][4] = \text{"5[a]"}$ and $f[5][9] = \text{"5[b]"}$ to produce $\mathbf{\text{"5[a]5[b]"}}$ (length 8 vs 10).

---

## 6. Traps & Common Anti-Patterns

- **Compressing Small Substrings ($L \le 4$):** Allowing `"aaa"` to encode as `"3[a]"` expands the string length from 3 to 4. Restricting periodic encoding to strictly shorten strings prevents regressions.
- **Omitting Recursion on Sub-Units:** Encoding `"abcabc"` as `2[abc]` is fine, but if the inner unit itself can be compressed, using $f[i][i + pos - 1]$ ensures sub-patterns are recursively optimized.
- **Iterating in Wrong Order:** Iterating $i$ ascending before outer loops finish larger intervals leads to uninitialized subproblems. Iterating $i$ descending ($n-1 \dots 0$) and $j$ ascending ($i \dots n-1$) ensures all sub-intervals $f[i][k]$ and $f[k+1][j]$ are computed before $f[i][j]$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Number of subproblems (intervals $[i, j]$) is $\frac{N(N+1)}{2} = O(N^2)$.
  - For each interval, period detection via string doubling takes $O(L) = O(N)$ time.
  - Testing all split points $k \in [i, j-1]$ takes $O(L) = O(N)$ time.
  - Total Time: $\mathcal{O}(N^3)$. For $N \le 150$, $N^3 \approx 3.3 \times 10^6$ operations, executing in $< 80$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N^3)$ memory to store strings in the $N \times N$ DP table $f$.
