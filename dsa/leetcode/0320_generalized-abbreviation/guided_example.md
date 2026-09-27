# Guided Example: Generalized Abbreviation

We trace the step-by-step recursive combinatorial partitioning, non-adjacent abbreviation substring constraints, mandatory literal delimiter insertion (`word[j] if j < n else ""`), and exhaustive $2^N$ abbreviation tree generation on representative word instances:

- **Input:** $\text{word} = \text{"word"}$
- **Required output:** List of all $2^4 = 16$ valid abbreviations:
  `["word", "wor1", "wo1d", "wo2", "w1rd", "w1r1", "w2d", "w3", "1ord", "1or1", "1o1d", "1o2", "2rd", "2r1", "3d", "4"]`
- **Single Character Base Case:** $\text{word} = \text{"a"} \implies \text{["a", "1"]}$
- **Two Character Combinations:** $\text{word} = \text{"in"} \implies \text{["in", "i1", "1n", "2"]}$
- **No Adjacent Digits Guarantee:** Substrings like `"11rd"` are invalid; consecutive abbreviated letters must merge into their combined count (`"2rd"`).

This instance demonstrates recursive divide-and-conquer over combinatorial choice sequences, mathematically proves why fixing the next literal character at index $j$ enforces the non-adjacent abbreviation invariant without post-processing cleanup, and analyzes time and space bounds ($O(N \cdot 2^N)$).

---

## 1. Instance & Teaching Goal

Given string $\text{word} = \text{"word"}$ of length $N = 4$:
Generate all generalized abbreviations formed by replacing any number of non-overlapping and non-adjacent substrings with their lengths.

```text
The Non-Adjacent Abbreviation Rule:
- Valid:   "w1rd"  (abbreviated 'o' -> 1; surrounded by literals 'w' and 'r')
- Valid:   "2rd"   (abbreviated "wo" -> 2; followed by literal 'r')
- Valid:   "4"     (abbreviated entire "word" -> 4)
- INVALID: "11rd"  (two adjacent numbers '1' and '1'; MUST be merged to "2rd")

Every character at position i has two binary choices:
Keep as literal OR Abbreviate.
Total possible abbreviations for length N = 2^N = 2^4 = 16.
```

### The Invariant Architecture of `dfs(i)`
To prevent producing adjacent number tokens (such as `"11"`):
- **Choice 1 (Keep $word[i]$):** Append $word[i]$ literally and recurse on suffix $i + 1$:
  $$
  word[i] + s \quad \text{for } s \in dfs(i + 1)
  $$
- **Choice 2 (Abbreviate $[i, j-1]$):**
  Choose the length of the abbreviated run $L = j - i$ for $j \in [i + 1, n]$.
  To ensure the next token is not a number:
  - If $j < n$, **force character $word[j]$ to be kept literally** as the separator!
  - Then recurse strictly on suffix $j + 1$ ($dfs(j + 1)$)!
  - If $j == n$, the entire remaining suffix is abbreviated to length $n - i$.

---

## 2. Conceptual Foundation & Invariants

### Recursive Contract `dfs(i)`:
Returns a list of all valid abbreviations for the suffix $\text{word}[i \dots n-1]$:
1. **Base Case:** If $i \ge n$, the suffix is empty:
   $$
   dfs(n) = [\text{""}]
   $$
   *(Returning `[""]` provides a neutral identity element for string concatenation; returning `[]` would erase recursive branches).*
2. **Branch 1 (Keep Current Character):**
   $$
   ans_1 = \{ word[i] + s \mid s \in dfs(i + 1) \}
   $$
3. **Branch 2 (Abbreviate Run from $i$ to $j-1$ with Forced Separator $word[j]$):**
   For each endpoint $j \in [i + 1, n]$:
   $$
   \text{separator} = word[j] \text{ if } j < n \text{ else } \text{""}
   $$
   $$
   ans_2 = \{ \text{str}(j - i) + \text{separator} + s \mid s \in dfs(j + 1) \}
   $$
4. Return $ans = ans_1 \cup ans_2$.

> **Invariant.** `dfs(i)` never produces consecutive numeric tokens. The separator $word[j]$ guarantees that any abbreviated number is strictly flanked by a literal character or string boundary.

---

## 3. Step-by-Step Worked Execution

We trace `dfs(i)` bottom-up from the end of $\text{word} = \text{"word"}$ ($n = 4$):

---

### Step 1: Base Case & Suffix $i = 3$ ($\text{"d"}$)
- Base: $dfs(4) = [\text{""}]$.
- For $i = 3$ ($word[3] = \text{'d'}$):
  - Keep 'd': $\text{'d'} + s \text{ for } s \in dfs(4) \implies \text{["d"]}$.
  - Abbreviate: $j = 4 \implies \text{length } 4 - 3 = 1$. Since $j = n$, separator is `""`.
    $\text{"1"} + \text{""} + s \text{ for } s \in dfs(5) \implies \text{["1"]}$.
- Result:
  $$
  dfs(3) = \mathbf{\text{["d", "1"]}} \quad (2^1 = 2 \text{ items})
  $$

---

### Step 2: Suffix $i = 2$ ($\text{"rd"}$)
- Keep 'r': $\text{'r'} + s \text{ for } s \in dfs(3)$:
  - $\text{'r'} + \text{"d"} = \text{"rd"}$
  - $\text{'r'} + \text{"1"} = \text{"r1"}$
  - Branch 1: `["rd", "r1"]`.
- Abbreviate from index 2:
  - $j = 3$ (len $3 - 2 = 1$): separator is $word[3] = \text{'d'}$.
    $\text{"1"} + \text{"d"} + s \text{ for } s \in dfs(4) \implies \text{"1d"}$.
  - $j = 4$ (len $4 - 2 = 2$): $j = n \implies$ separator is `""`.
    $\text{"2"} + \text{""} + s \text{ for } s \in dfs(5) \implies \text{"2"}$.
- Result:
  $$
  dfs(2) = \mathbf{\text{["rd", "r1", "1d", "2"]}} \quad (2^2 = 4 \text{ items})
  $$

---

### Step 3: Suffix $i = 1$ ($\text{"ord"}$)
- Keep 'o': $\text{'o'} + s \text{ for } s \in dfs(2)$:
  - `["ord", "or1", "o1d", "o2"]`.
- Abbreviate from index 1:
  - $j = 2$ (len 1): separator $word[2] = \text{'r'}$.
    $\text{"1r"} + s \text{ for } s \in dfs(3) \implies \text{["1rd", "1r1"]}$.
  - $j = 3$ (len 2): separator $word[3] = \text{'d'}$.
    $\text{"2d"} + s \text{ for } s \in dfs(4) \implies \text{["2d"]}$.
  - $j = 4$ (len 3): $j = n$, separator `""`.
    $\text{"3"} + \text{""} + s \text{ for } s \in dfs(5) \implies \text{["3"]}$.
- Result:
  $$
  dfs(1) = \mathbf{\text{["ord", "or1", "o1d", "o2", "1rd", "1r1", "2d", "3"]}} \quad (2^3 = 8 \text{ items})
  $$

---

### Step 4: Full String $i = 0$ ($\text{"word"}$)
- Keep 'w': $\text{'w'} + s \text{ for } s \in dfs(1)$:
  - `["word", "wor1", "wo1d", "wo2", "w1rd", "w1r1", "w2d", "w3"]` ($8$ items).
- Abbreviate from index 0:
  - $j = 1$ (len 1): separator $word[1] = \text{'o'}$.
    $\text{"1o"} + s \text{ for } s \in dfs(2) \implies \text{["1ord", "1or1", "1o1d", "1o2"]}$ ($4$ items).
  - $j = 2$ (len 2): separator $word[2] = \text{'r'}$.
    $\text{"2r"} + s \text{ for } s \in dfs(3) \implies \text{["2rd", "2r1"]}$ ($2$ items).
  - $j = 3$ (len 3): separator $word[3] = \text{'d'}$.
    $\text{"3d"} + s \text{ for } s \in dfs(4) \implies \text{["3d"]}$ ($1$ item).
  - $j = 4$ (len 4): $j = n$, separator `""`.
    $\text{"4"} + \text{""} + s \text{ for } s \in dfs(5) \implies \text{["4"]}$ ($1$ item).
- Total generated: $8 + 4 + 2 + 1 + 1 = \mathbf{16}$ valid abbreviations!

---

## 4. Complete Execution Trace

```text
word = "word" (n = 4)

dfs(4) = [""]
dfs(3) = ['d'+""= "d", '1'+""= "1"]                                (2 items)
dfs(2) = ['r' + dfs(3), "1d" + dfs(4), "2" + dfs(5)]               (4 items)
       = ["rd", "r1", "1d", "2"]
dfs(1) = ['o' + dfs(2), "1r" + dfs(3), "2d" + dfs(4), "3"]        (8 items)
       = ["ord", "or1", "o1d", "o2", "1rd", "1r1", "2d", "3"]
dfs(0) = ['w' + dfs(1), "1o" + dfs(2), "2r" + dfs(3), "3d", "4"] (16 items)

Total Count: 16
```

| Recursion Level | Suffix Length | Branch Type | Formulation | Generated Subsequence Items | Count |
|:---:|:---:|:---:|:---|:---|:---:|
| $dfs(3)$ | 1 ("d") | Keep 'd' / Abbreviate 1 | `'d'`, `'1'` | `["d", "1"]` | 2 |
| $dfs(2)$ | 2 ("rd") | Keep 'r' | `'r'` + $dfs(3)$ | `["rd", "r1"]` | 2 |
| | | Abbreviate $L=1, 2$ | `"1d"`, `"2"` | `["1d", "2"]` | 2 |
| $dfs(1)$ | 3 ("ord") | Keep 'o' | `'o'` + $dfs(2)$ | `["ord", "or1", "o1d", "o2"]` | 4 |
| | | Abbreviate $L=1, 2, 3$ | `"1r"`+$dfs(3)$, `"2d"`, `"3"` | `["1rd", "1r1", "2d", "3"]` | 4 |
| **$dfs(0)$** | **4 ("word")** | **Keep 'w'** | `'w'` + $dfs(1)$ | `["word", ..., "w3"]` | **8** |
| | | **Abbreviate $L=1,2,3,4$** | `"1o"`+$dfs(2)$, ..., `"4"` | `["1ord", ..., "4"]` | **8** |
| **Total** | - | - | - | **All 16 Distinct Abbreviations** | **16** |

---

## 5. Algorithmic Correctness

**Soundness.** Every abbreviation generated represents a partition of the original string where consecutive runs of abbreviated characters are strictly delimited by kept literal characters. Forcing literal character $word[j]$ after run $[i, j-1]$ guarantees that two numeric tokens can never appear adjacently. Every character from index $0$ to $n-1$ is accounted for.

**Completeness.** At each step, all possibilities for the prefix starting at $i$ are partitioned into mutually exclusive cases: either $word[i]$ is kept, or an abbreviation of length $L \in [1, n - i]$ begins at $i$. Because this partition is exhaustive, every valid abbreviation is uniquely generated without duplicates.

---

## 6. Traps This Instance Exposes

- **Adjacent Numbers Trap:** Generating independent runs of deletions without enforcing literal delimiters risks producing strings like `"11rd"`, which is malformed. The separator $word[j]$ structurally prevents adjacent numbers.
- **Empty Base Case Return:** Returning an empty list `[]` for $dfs(n)$ causes all loops over $dfs(n)$ to terminate immediately, discarding all recursive branches. The base case must return `[""]`.
- **Exponential Complexity Reality:** Because there are $2^N$ abbreviations, algorithms that perform string replacements or regex cleanup on $2^N$ items suffer heavy overhead. Constructing valid strings directly during recursion is optimal.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot 2^N)$, where $N$ is the length of `word`. There are exactly $2^N$ abbreviations. Constructing each abbreviation of length $O(N)$ takes $O(N)$ string concatenation time.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary stack frames (excluding the $O(N \cdot 2^N)$ space required to hold the returned list of strings).
