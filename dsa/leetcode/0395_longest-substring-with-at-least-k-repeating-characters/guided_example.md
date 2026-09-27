# Guided Example: Longest Substring with At Least K Repeating Characters

We trace the step-by-step divide-and-conquer frequency threshold partitioning ($v < k \implies \text{split}$), delimiter exclusion, recursive sub-segment evaluation, and base-case segment acceptance on representative string instances:

- **Input:** $s = \text{"aaabb"}, \quad k = 3$
- **Required output:** $3$
  - Step 1: Compute frequencies of $s = \text{"aaabb"}$:
    - $cnt = \{\text{'a'}: 3, \; \text{'b'}: 2\}$
  - Step 2: Identify deficit characters ($v < k = 3$):
    - Character `'b'` has count $2 < 3$
    - Any valid substring cannot contain `'b'`!
  - Step 3: Split $s$ around delimiter `'b'`:
    - Sub-segment before `'b'`: $s[0 \dots 2] = \text{"aaa"}$
  - Step 4: Recurse on $s[0 \dots 2] = \text{"aaa"}$:
    - Frequencies: $cnt = \{\text{'a'}: 3\}$
    - All characters satisfy frequency $\ge 3 \implies$ Entire substring valid!
    - Length: $3$
  - Longest valid substring length: $\mathbf{3}$ (Substring `"aaa"`)
- **Multi-Split Instance:** $s = \text{"ababbc"}, k = 2$
  - Frequencies: $cnt = \{\text{'a'}: 2, \text{'b'}: 3, \text{'c'}: 1\}$
  - Deficit character: `'c'` ($1 < 2$)
  - Segment before `'c'`: `"ababb"` $\implies$ counts `a: 2, b: 3` $\ge 2 \implies \mathbf{5}$
- **All Deficit Failure:** $s = \text{"abcdef"}, k = 2 \implies$ all counts $1 < 2 \implies 0$

This instance demonstrates divide-and-conquer partitioning driven by frequency constraints, mathematically proves why characters with global frequency $< k$ cannot appear in any valid substring, and derives $O(N \cdot |\Sigma|)$ runtime and $O(|\Sigma|)$ recursion depth bounds.

---

## 1. Instance & Teaching Goal

Given a string $s = \text{"aaabb"}$ and an integer $k = 3$:
Find the length of the longest substring where every character appears **at least $k$ times**:

```text
Input: "aaabb", k = 3
Counts: 'a': 3,  'b': 2

Observation:
  Character 'b' appears only 2 times in the ENTIRE string.
  Since 2 < 3, 'b' can NEVER appear in ANY valid substring!
  Therefore, 'b' acts as an absolute barrier / delimiter.

Split on 'b':
  Sub-segment 1: "aaa" -> 'a' appears 3 times (3 >= 3) -> VALID! Length = 3
  Sub-segment 2: empty

Max Length = 3
```

### Why Standard Sliding Window Fails Directly
The condition "every unique character in the window has frequency $\ge k$" is **non-monotonic**:
- Adding a character can make an invalid window valid (e.g. adding the 3rd `'a'`).
- Adding a character can also make a valid window invalid (e.g. adding a new character `'c'` with count 1).
Because expanding the window does not monotonically preserve feasibility, a simple two-pointer sliding window cannot decide whether to expand or shrink without extra constraints. Divide-and-conquer provides a clean, optimal solution.

---

## 2. Conceptual Foundation & Invariants

### 1. The Delimiter Elimination Principle:
For any substring $s[l \dots r]$:
1. Compute the histogram:
   $$
   cnt = \text{Counter}(s[l \dots r])
   $$
2. Find any character $c$ with frequency $v < k$:
   - If no such character exists:
     Every character in $s[l \dots r]$ has frequency $\ge k$. The entire substring is valid!
     $$
     \text{return } r - l + 1
     $$
   - If such a character $c$ exists ($v < k$):
     Character $c$ cannot be part of any valid substring anywhere within $s[l \dots r]$.
     Therefore, $c$ divides $[l, r]$ into disjoint candidate intervals.
3. For every contiguous chunk $[i, j - 1]$ not containing $c$:
   $$
   ans \leftarrow \max(ans, \; dfs(i, j - 1))
   $$

> **Invariant.** A character with frequency $< k$ in a segment $S$ cannot be present in any valid subsegment of $S$. Dividing along all occurrences of that character preserves all potentially valid maximal substrings.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"aaabb"}, k = 3$:
Initial call: `dfs(0, 4)`.

---

### Step 1: Root Frame `dfs(0, 4)` on `"aaabb"`
- Segment: $s[0 \dots 4] = \text{"aaabb"}$, length $= 5 \ge 3$.
- Count frequencies:
  $$
  cnt[\text{'a'}] = 3, \quad cnt[\text{'b'}] = 2
  $$
- Threshold check ($k = 3$):
  - `'a'`: $3 \ge 3$ (Satisfied).
  - `'b'`: $2 < 3$ (Deficit detected!).
- Split delimiter chosen:
  $$
  split = \mathbf{\text{'b'}}
  $$
- Scan for subsegments between occurrences of `'b'`:
  - From $i = 0$: $s[0] = \text{'a'}, s[1] = \text{'a'}, s[2] = \text{'a'}$.
  - At index $3$: $s[3] = \text{'b'}$ (delimiter hit).
  - First chunk: interval $[0, 2]$ representing `"aaa"`.
  - Recurse: `dfs(0, 2)`.

---

### Step 2: Child Frame `dfs(0, 2)` on `"aaa"`
- Segment: $s[0 \dots 2] = \text{"aaa"}$, length $= 3$.
- Count frequencies:
  $$
  cnt[\text{'a'}] = 3
  $$
- Threshold check ($k = 3$):
  - Every character has frequency $\ge 3$.
  - No split character found (`split == ''`).
- Valid base case reached!
- Return length:
  $$
  r - l + 1 = 2 - 0 + 1 = \mathbf{3}
  $$

---

### Step 3: Root Frame Continuation
- Chunk $[0, 2]$ returned $3 \implies ans = \max(0, 3) = \mathbf{3}$.
- Advance past delimiters: indices $3$ and $4$ are both `'b'`.
- No further chunks remain in $[0, 4]$.
- Return:
  $$
  ans = \mathbf{3}
  $$

---

## 4. Complete Execution Trace

```text
dfs(0, 4) on "aaabb", k = 3
  cnt = {'a': 3, 'b': 2}
  split = 'b' (cnt['b'] = 2 < 3)
  chunk [0, 2] ("aaa"):
    dfs(0, 2) on "aaa"
      cnt = {'a': 3}
      no split -> returns 3
    ans = max(0, 3) = 3
  chunk [3, 4] ("bb"): delimiters skipped
  returns 3

Final Output: 3
```

| Recursion Depth | Segment Bounds $[l, r]$ | Substring Text | Frequency Map $cnt$ | Deficit Split Character | Action Taken | Subproblem Result |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| 0 (Root) | $[0, 4]$ | `"aaabb"` | `{'a': 3, 'b': 2}` | `'b'` ($2 < 3$) | Split on `'b'`, recurse $[0, 2]$ | **3** |
| **1 (Child)** | **$[0, 2]$** | **`"aaa"`** | **`{'a': 3}`** | **None** | **All $\ge 3 \implies$ Valid** | **3** |

---

### Comparison: Multi-Split Trace ($s = \text{"ababbc"}, k = 2$)

```text
dfs(0, 5) on "ababbc", k = 2
  cnt = {'a': 2, 'b': 3, 'c': 1}
  split = 'c' (cnt['c'] = 1 < 2)
  chunk [0, 4] ("ababb"):
    dfs(0, 4) on "ababb"
      cnt = {'a': 2, 'b': 3}
      all counts >= 2 -> returns 5
  ans = 5
```

---

## 5. Algorithmic Correctness

**Soundness.** If a character $c$ appears fewer than $k$ times in $s[l \dots r]$, it appears fewer than $k$ times in *every* subsegment of $s[l \dots r]$. Therefore, no valid substring can contain $c$. Removing all occurrences of $c$ partitions the segment into maximal intervals where a valid substring could possibly reside without losing any potential solution.

**Completeness.** At each level of recursion, either the segment contains zero deficit characters (in which case the entire segment is valid and returned), or at least one deficit character is eliminated. Since there are at most 26 lowercase English letters, the recursion tree depth is bounded by $|\Sigma| \le 26$, guaranteeing termination and complete coverage.

---

## 6. Traps This Instance Exposes

- **All Characters Below Threshold:** If $s = \text{"abcdef"}$ and $k = 2$, every character has count 1. The algorithm splits on `'a'`, recursing on `"bcdef"`, then `'b'`, etc., gracefully terminating and returning 0.
- **Short Substring Optimization:** If $r - l + 1 < k$, the segment is strictly shorter than $k$ and cannot satisfy the condition. Returning 0 immediately prunes empty recursive calls.
- **Alternative Fixed-Unique Sliding Window:** An alternative approach runs a sliding window 26 times (fixing the number of unique characters $u \in [1, 26]$ in the window). For a fixed $u$, the window becomes monotonic, also achieving $O(26 \cdot N)$ runtime.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot |\Sigma|)$, where $N = \text{len}(s)$ and $|\Sigma| \le 26$ is the lowercase alphabet size.
  - At each recursion level, counting characters takes $O(N)$ time.
  - Each level eliminates at least one distinct character from the alphabet.
  - Maximum recursion depth is $|\Sigma| \le 26$.
  - Total operations: at most $26 \times N$, running well under 10 ms for $N \le 10^4$.
- **Auxiliary Space Complexity:** $O(|\Sigma|) = O(1)$ recursion stack depth and frequency table memory, bounded by 26 English letters.
