# Guided Example: Split Concatenated Strings

We trace the step-by-step greedy intact-string orientation ($\max(s, s[::-1])$), circular string loop concatenation, single-string internal cut position iteration ($j$), dual forward/reverse split reconstruction ($a + t + b$ vs $b[::-1] + t + a[::-1]$), and global lexicographical maximum selection on representative string arrays:

- **Input:** $strs = [\text{"abc"}, \text{"xyz"}]$
- **Required output:** `"zyxcba"`
  - Transformation rules:
    1. Each string $s_i \in strs$ can independently be kept as-is or reversed.
    2. Strings are joined in original order into a **continuous loop** (circular string).
    3. Exactly one cut is made at any character, and the loop is unfolded clockwise to form a linear string.
    4. Goal: Maximize the resulting string **lexicographically**.
- **Greedy Orientation & Circular Cut Trace:**
  - **Phase 1: Maximize All Intact Strings:**
    - Any string that is not cut through by the split point simply appears as a complete intact block in the circular traversal.
    - To maximize the final string lexicographically, every intact string should be oriented in its lexicographically larger direction:
      $$
      s_i \leftarrow \max(s_i, \; \text{reversed}(s_i))
      $$
      - For `"abc"`: $\max(\text{"abc"}, \text{"cba"}) = \mathbf{\text{"cba"}}$
      - For `"xyz"`: $\max(\text{"xyz"}, \text{"zyx"}) = \mathbf{\text{"zyx"}}$
    - Updated greedy array:
      $$
      strs = [\text{"cba"}, \; \text{"zyx"}]
      $$
  - **Phase 2: Iterate Through All Possible Cut Locations:**
    - The single cut must fall inside some string $s_i$ at some index $j$.
    - The remaining intact strings appear in circular order:
      $$
      t = \text{join}(strs[i+1:]) + \text{join}(strs[:i])
      $$
    - **Cut in $s_0 = \text{"cba"}$ ($i = 0$):**
      - Intact circular tail: $t = \text{"zyx"}$.
      - Check cuts across original or reversed $s_0$:
        - At index $j = 0$ in `"cba"`: $a = \text{"cba"}, \; b = \text{""} \implies a + t + b = \mathbf{\text{"cbazyx"}}$.
    - **Cut in $s_1 = \text{"zyx"}$ ($i = 1$):**
      - Intact circular tail: $t = strs[:1] = \mathbf{\text{"cba"}}$.
      - String $s_1$ has characters `['z', 'y', 'x']`.
      - **Cut at $j = 0$ in `"zyx"`:**
        - Suffix: $a = \text{"zyx"}$
        - Prefix: $b = \text{""}$
        - Assembled candidate:
          $$
          \text{Candidate} = a + t + b = \text{"zyx"} + \text{"cba"} + \text{""} = \mathbf{\text{"zyxcba"}}
          $$
        - Compare: $\text{"zyxcba"} > \text{"cbazyx"} \implies ans \leftarrow \mathbf{\text{"zyxcba"}}$.
      - **Cut at $j = 1$ in `"zyx"`:**
        - $a = \text{"yx"}, \; b = \text{"z"}$.
        - Candidate: $\text{"yx"} + \text{"cba"} + \text{"z"} = \text{"yxcbaz"} < \text{"zyxcba"}$.
      - **Cut at $j = 2$ in `"zyx"`:**
        - $a = \text{"x"}, \; b = \text{"zy"}$.
        - Candidate: $\text{"x"} + \text{"cba"} + \text{"zy"} = \text{"xcbazy"} < \text{"zyxcba"}$.
  - All possible cuts evaluated.
  - Global lexicographical maximum: **`"zyxcba"`**.
- **Single String Instance ($strs = [\text{"abc"}]$):**
  - Reversal: $\max(\text{"abc"}, \text{"cba"}) = \mathbf{\text{"cba"}}$.
  - Cut at index 0 $\implies \mathbf{\text{"cba"}}$.
- **Internal Cut in Forward vs Reversed:**
  - In a string like `"lc"`, reversing gives `"cl"`, but cut at index 1 of `"lc"` gives `"c" + t + "l"`, starting with `'c'`. The dual evaluation $a + t + b$ and $b[::-1] + t + a[::-1]$ guarantees neither orientation is missed.

This instance demonstrates greedy local component maximization coupled with exhaustive cycle cut bisection, mathematically proves why non-cut strings remain in their dominant canonical orientation, and derives $O(N \cdot L^2)$ runtime and $O(N \cdot L)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an array of strings $strs = [\text{"abc"}, \text{"xyz"}]$:
1. You can reverse each string or leave it as is.
2. Concatenate them in order into a circular ring.
3. Make one cut at any position and read the ring clockwise.
Return the **lexicographically largest** string that can be formed.

```text
Strings: ["abc", "xyz"]

Step 1: Orient intact strings to be as large as possible:
  "abc" -> "cba"
  "xyz" -> "zyx"
  Loop: [ "cba" ] -> [ "zyx" ] -> (back to "cba")

Step 2: Best starting cut is at 'z' in "zyx":
  Read clockwise: "z", "y", "x" -> "c", "b", "a"
  Result: "zyxcba"
```

### The Invariant of Intact Block Dominance
- When a cut is made inside string $s_i$, only $s_i$ is broken into two pieces (a prefix and a suffix).
- All other $N - 1$ strings remain **completely intact**.
- Because larger letters earlier in a string dominate lexicographical order, any intact string $s_k$ ($k \ne i$) should always be in its lexicographically larger orientation:
  $$
  s_k \leftarrow \max(s_k, \; \text{reversed}(s_k))
  $$
- This leaves only the single cut-through string $s_i$ to be explored across all its internal split positions.

---

## 2. Conceptual Foundation & Invariants

### 1. Pre-Orientation Phase:
For each string in $strs$:
$$
strs[k] \leftarrow \max(strs[k], \; \text{reversed}(strs[k]))
$$

### 2. Cut Exploration Phase:
For each string index $i \in [0, N - 1]$:
1. Concatenate all other intact strings in circular order:
   $$
   t = \text{"".join}(strs[i+1:]) + \text{"".join}(strs[:i])
   $$
2. For each split position $j \in [0, |s_i|)$:
   - **Forward Orientation of $s_i$:**
     Suffix $a = s_i[j:]$, Prefix $b = s_i[:j]$.
     Candidate: $a + t + b$.
   - **Reversed Orientation of $s_i$:**
     Candidate: $\text{reversed}(b) + t + \text{reversed}(a)$.
   - Update $ans \leftarrow \max(ans, \text{candidates})$.

> **Cyclic Transposition Invariant.** Fixing all $N - 1$ non-cut strings to their greedy maxima restricts the search to $2 \sum |s_i|$ total linear cut evaluations.

---

## 3. Step-by-Step Worked Execution

We trace $strs = [\text{"abc"}, \text{"xyz"}]$:

---

### Step 1: Greedy Pre-Orientation
- `"abc"`: $\max(\text{"abc"}, \text{"cba"}) = \text{"cba"}$.
- `"xyz"`: $\max(\text{"xyz"}, \text{"zyx"}) = \text{"zyx"}$.
- $strs = [\text{"cba"}, \text{"zyx"}]$.
- Initial baseline: $ans = \text{"cbazyx"}$.

---

### Step 2: Cut in String 0 ($s_0 = \text{"cba"}$)
- Intact tail: $t = \text{"zyx"}$.
- $j = 0$: $a = \text{"cba"}, b = \text{""} \implies \text{"cbazyx"}$.
- No other cut exceeds `"cbazyx"`.

---

### Step 3: Cut in String 1 ($s_1 = \text{"zyx"}$)
- Intact tail: $t = \text{"cba"}$.
- **Test $j = 0$:**
  - $a = \text{"zyx"}, b = \text{""}$.
  - Forward: $a + t + b = \text{"zyx"} + \text{"cba"} + \text{""} = \mathbf{\text{"zyxcba"}}$.
  - Update: $ans \leftarrow \max(\text{"cbazyx"}, \text{"zyxcba"}) = \mathbf{\text{"zyxcba"}}$.
- **Test $j = 1$:**
  - $a = \text{"yx"}, b = \text{"z"}$.
  - Forward: $\text{"yxcbaz"} < ans$.
- **Test $j = 2$:**
  - $a = \text{"x"}, b = \text{"zy"}$.
  - Forward: $\text{"xcbazy"} < ans$.

---

### Step 4: Final Output
$$
ans = \mathbf{\text{"zyxcba"}}
$$

---

## 4. Complete Execution Trace

| String Cut $i$ | Split Index $j$ | Suffix $a$ | Intact Ring $t$ | Prefix $b$ | Resulting String $a + t + b$ | Running $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ (`"cba"`) | $0$ | `"cba"` | `"zyx"` | `""` | `"cbazyx"` | `"cbazyx"` |
| $0$ (`"cba"`) | $1$ | `"ba"` | `"zyx"` | `"c"` | `"bazyxc"` | `"cbazyx"` |
| $1$ (`"zyx"`) | **$0$** | **`"zyx"`** | **`"cba"`** | **`""`** | **`"zyxcba"`** | **`"zyxcba"`** |
| $1$ (`"zyx"`) | $1$ | `"yx"` | `"cba"` | `"z"` | `"yxcbaz"` | `"zyxcba"` |
| $1$ (`"zyx"`) | $2$ | `"x"` | `"cba"` | `"zy"` | `"xcbazy"` | `"zyxcba"` |
| **Result** | — | — | — | — | — | **`"zyxcba"`** |

---

## 5. Boundary Cases & Failure Modes

- **Single String ($[\text{"abc"}]$):** $t = \text{""}$. Reverses to `"cba"`, cuts at $0 \implies \mathbf{\text{"cba"}}$.
- **Palindromic Strings ($[\text{"aba"}, \text{"cdc"}]$):** Reversals equal originals; loop evaluates cut positions normally.
- **Identical Repeated Strings ($[\text{"a"}, \text{"a"}, \text{"a"}]$):** Produces `"aaa"`.
- **Large Total String Length ($1000$ characters):** Evaluates at most $1000$ candidate strings, each comparison taking $O(L)$ time.

---

## 6. Traps & Common Anti-Patterns

- **Testing All $2^N$ Reversals:** Brute-force orientation requires testing $2^N$ configurations, which causes TLE for $N = 1000$. All non-cut strings are provably optimal in their greedy maximum orientation.
- **Forgetting the Reversed Orientation of the Cut String:** The cut string $s_i$ might achieve its best start when flipped. Testing both $a + t + b$ and $b[::-1] + t + a[::-1]$ guarantees full coverage.
- **Splitting Outside Word Boundaries:** Cuts can occur *between* words or *inside* words. Setting $j = 0$ cleanly covers the boundary between word $i$ and word $i-1$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $M = \sum |s_i|$ be the total number of characters across all strings.
  - Phase 1 (Greedy orientation): $O(M)$ time.
  - Phase 2 (Cut exploration):
    - There are $N$ strings, and string $i$ has $|s_i|$ possible cut positions.
    - Total cut configurations tested: $2 \sum |s_i| = 2M$.
    - Each string concatenation and comparison takes $O(M)$ time.
    - Total Time: $\mathcal{O}(M^2)$. For $M \le 1000$, $1000^2 = 10^6$ operations, completing in $< 25$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M)$ space to construct candidate strings.
