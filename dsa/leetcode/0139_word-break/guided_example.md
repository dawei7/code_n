# Guided Example: Word Break

We trace the step-by-step 1D dynamic programming prefix reachability recurrence and dictionary matching on representative word segmentation instances:

- **Input:** $s = \text{"leetcode"}$, $\text{wordDict} = [\text{"leet"}, \text{"code"}]$
- **Required output:** `true` (Segmented as $\text{"leet"} + \text{"code"}$)
- **Negative Branching Instance:** $s = \text{"catsandog"}$, $\text{wordDict} = [\text{"cats"}, \text{"dog"}, \text{"sand"}, \text{"and"}, \text{"cat"}] \implies \text{false}$

This instance demonstrates formulating the prefix feasibility state ($DP[i] \iff s[0 \dots i-1]$ is segmentable), anchoring with base case $DP[0] = \text{True}$, evaluating subproblem chaining ($DP[j] \land s[j \dots i-1] \in \text{dict}$), and pruning inner loops via word length bounds in $O(N^2)$ time.

---

## 1. Instance & Teaching Goal

Given a string $s = \text{"leetcode"}$ of length $N = 8$ and a dictionary $\text{wordDict} = [\text{"leet"}, \text{"code"}]$:
Determine if $s$ can be segmented into a space-separated sequence of one or more dictionary words. Dictionary words may be reused arbitrarily.

In this instance:
- Prefix $s[0 \dots 3] = \text{"leet"}$ exists in `wordDict`.
- Suffix $s[4 \dots 7] = \text{"code"}$ exists in `wordDict`.
Because the concatenation $\text{"leet"} + \text{"code"}$ equals $s$, the answer is `true`.

A recursive backtracking solution without memoization tries all possible word splits, degrading to $O(2^N)$ time on overlapping words (e.g. `s = "aaaaab"`, `dict = ["a", "aa", "aaa"]`).
1D Dynamic Programming memoizes prefix reachability in a boolean table of size $N + 1$. State $DP[i]$ checks whether any previously reachable prefix $j < i$ can be extended to $i$ with a valid dictionary word, reducing complexity to polynomial time.

---

## 2. Conceptual Foundation & Invariants

### 1D Boolean Dynamic Programming Protocol
Let $N = |s|$.
Convert `wordDict` into a hash set `words` for $O(1)$ lookup.
Define array $DP$ of length $N + 1$ initialized to $\text{False}$:
$$
DP[i] \iff \text{the prefix } s[0 \dots i-1] \text{ can be segmented into dictionary words}
$$

1. **Base Case:**
   The empty prefix of length $0$ is vacuously segmentable:
   $$
   DP[0] = \text{True}
   $$
2. **State Transition for $i \in [1, N]$:**
   Examine every possible split index $j \in [0, i - 1]$:
   $$
   DP[i] = \bigvee_{j=0}^{i-1} \left( DP[j] \land (s[j \dots i - 1] \in \text{words}) \right)
   $$
   - If a valid $j$ is found, set $DP[i] \leftarrow \text{True}$ and immediately `break` the inner loop (early termination for state $i$).
3. **Word Length Pruning:**
   Instead of scanning all $j \in [0, i-1]$, only test lengths $L = i - j$ where $L \le \max(\text{len}(w) \text{ for } w \in \text{words})$.

> **Invariant.** For every computed index $i \in [0, N]$, $DP[i] == \text{True}$ if and only if there exists a valid sequence of dictionary words whose concatenation equals $s[0 \dots i-1]$.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"leetcode"}$ with `words = {"leet", "code"}`:
$N = 8$. Valid word lengths are $\{4\}$.

### Initialization
- $DP = [\text{True}, \text{False}, \text{False}, \text{False}, \text{False}, \text{False}, \text{False}, \text{False}, \text{False}]$

---

### Step 1: Prefixes of Length $i = 1, 2, 3$
- $i = 1$ ($s[0:1] = \text{"l"}$): not in `words` $\implies DP[1] = \text{False}$.
- $i = 2$ ($s[0:2] = \text{"le"}$): not in `words` $\implies DP[2] = \text{False}$.
- $i = 3$ ($s[0:3] = \text{"lee"}$): not in `words` $\implies DP[3] = \text{False}$.

---

### Step 2: Prefix Length $i = 4$ ($s[0 \dots 3] = \text{"leet"}$)
- Evaluate split indices $j \in [0, 3]$:
  - $j = 0$: $DP[0] == \text{True}$.
  - Substring $s[0 \dots 3] = \text{"leet"}$.
  - Check set: $\text{"leet"} \in \text{words}$!
  - Transition succeeds:
    $$
    DP[4] \leftarrow \text{True}
    $$
  - Break inner loop.

State: $DP[0] = \text{True}, \, DP[4] = \text{True}$, all other entries $\text{False}$.

---

### Step 3: Prefixes of Length $i = 5, 6, 7$
- $i = 5$: $j \in \{0, 4\}$:
  - $j = 4: s[4:5] = \text{"c"} \notin \text{words} \implies DP[5] = \text{False}$.
- $i = 6$: $j = 4: s[4:6] = \text{"co"} \notin \text{words} \implies DP[6] = \text{False}$.
- $i = 7$: $j = 4: s[4:7] = \text{"cod"} \notin \text{words} \implies DP[7] = \text{False}$.

---

### Step 4: Full String Length $i = 8$ ($s[0 \dots 7] = \text{"leetcode"}$)
- Evaluate split indices $j$ where $DP[j] == \text{True}$:
  - Candidate $j = 0$: $s[0:8] = \text{"leetcode"} \notin \text{words}$.
  - Candidate $j = 4$: $DP[4] == \text{True}$.
    - Suffix substring: $s[4 \dots 7] = \text{"code"}$.
    - Check set: $\text{"code"} \in \text{words}$!
    - Transition succeeds:
      $$
      DP[8] \leftarrow \text{True}
      $$
    - Break inner loop.

Target reached: $DP[8] = \mathbf{True}$.
String `"leetcode"` can be segmented.

---

## 4. Complete Execution Trace

```text
Indices:     0   1   2   3   4   5   6   7   8
Characters:    l   e   e   t   c   o   d   e
DP Table:   [T,  F,  F,  F,  T,  F,  F,  F,  T]
             ^               ^               ^
            Base           "leet"          "code"
                           (j=0)           (j=4)
```

| Prefix Length $i$ | Substring $s[0 \dots i-1]$ | Candidate Split $j$ | Prior $DP[j]$ | Candidate Word $s[j \dots i-1]$ | In `words`? | Resulting $DP[i]$ | Action Taken |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | $\emptyset$ | - | - | - | - | **True** | Base case anchor |
| 1 | `"l"` | 0 | True | `"l"` | No | False | - |
| 2 | `"le"` | 0 | True | `"le"` | No | False | - |
| 3 | `"lee"` | 0 | True | `"lee"` | No | False | - |
| **4** | **`"leet"`** | **0** | **True** | **`"leet"`** | **Yes** | **True** | **Break ($DP[4]=\text{True}$)** |
| 5 | `"leetc"` | 4 | True | `"c"` | No | False | - |
| 6 | `"leetco"` | 4 | True | `"co"` | No | False | - |
| 7 | `"leetcod"` | 4 | True | `"cod"` | No | False | - |
| **8** | **`"leetcode"`** | **4** | **True** | **`"code"`** | **Yes** | **True** | **Break ($DP[8]=\text{True}$)** |

The header also names a negative instance, and it deserves a full trace because it reaches a long prefix and still cannot finish. Only reachable split indices are listed, since an unreachable $j$ cannot extend any decomposition:

| Prefix length $i$ | Prefix $s[0 \dots i-1]$ | Reachable splits tested | Suffixes tried | Why the state is decided that way | $DP[i]$ |
|:---:|:---|:---|:---|:---|:---:|
| 1 | `"c"` | $j = 0$ | `"c"` | No dictionary word ends here | False |
| 2 | `"ca"` | $j = 0$ | `"ca"` | Index 1 is unreachable, so $j = 0$ is the only candidate | False |
| 3 | `"cat"` | $j = 0$ | `"cat"` | `"cat"` is a dictionary word, so this prefix becomes reachable | **True** |
| 4 | `"cats"` | $j = 0$ | `"cats"` | `"cats"` is a dictionary word as well | **True** |
| 5 | `"catsa"` | $j = 0, 3, 4$ | `"catsa"`, `"sa"`, `"a"` | None of the three suffixes is a word | False |
| 6 | `"catsan"` | $j = 0, 3, 4$ | `"catsan"`, `"san"`, `"an"` | `"sand"` needs one more character, and no shorter suffix matches | False |
| 7 | `"catsand"` | $j = 0, 3, 4$ | `"catsand"`, `"sand"`, `"and"` | Two different splits succeed: `"cat"` plus `"sand"`, and `"cats"` plus `"and"` | **True** |
| 8 | `"catsando"` | $j = 0, 3, 4, 7$ | `"catsando"`, `"sando"`, `"ando"`, `"o"` | The reachable prefix would have to be extended by the single character `"o"`, which is absent | False |
| 9 | `"catsandog"` | $j = 0, 3, 4, 7$ | `"catsandog"`, `"sandog"`, `"andog"`, `"og"` | `"dog"` begins at index 6, but index 6 was never reachable | **False** |

The last row is the whole point of this instance. Prefix length 7 is reachable, so a greedy scan that stops as soon as it has consumed seven characters would look successful; the recurrence survives that temptation because `"dog"` can only be appended at the boundary 6, and `DP[6]` is `False`. Reachability is a property of exact boundaries, not of how much of the string has been matched.

---

## 5. Algorithmic Correctness

**Soundness.** If $DP[i] == \text{True}$, then by induction there exists some $j < i$ such that $DP[j] == \text{True}$ and $s[j \dots i-1] \in \text{words}$. The substring from $0$ to $i-1$ is therefore the concatenation of the valid sequence for $s[0 \dots j-1]$ and the valid word $s[j \dots i-1]$.

**Completeness.** Any valid segmentation of $s[0 \dots i-1]$ must have a last word starting at some index $j$. Because the algorithm tests all possible prefix split points $j$, any reachable configuration will be discovered and set to `True`.

---

## 6. Traps This Instance Exposes

- **Greedy Segmentation Failure:** Greedily matching the first or longest word fails. For example, on $s = \text{"cars"}$, $\text{words} = [\text{"car"}, \text{"ca"}, \text{"rs"}]$, greedily choosing `"car"` leaves `"s"` which cannot be matched, whereas `"ca" + "rs"` succeeds. Dynamic programming explores all valid segmentations.
- **Substring Creation Overhead:** Slicing `s[j:i]` creates a temporary string. Scanning only up to $\max(\text{len}(w))$ limits the maximum slice length, preventing $O(N^3)$ operations.
- **Base Case $DP[0]$:** If $DP[0]$ is set to `False`, no transition can ever start, causing every entry to remain `False`.

The authored cases separate the reachable boundaries from the unreachable ones, which is the only state that matters:

| Authored case | `s` | `wordDict` | Reachable prefix lengths | Returned |
|:---|:---|:---|:---|:---:|
| `sample-1` | `"leetcode"` | `["leet", "code"]` | $\{0, 4, 8\}$ | true |
| `sample-2` | `"applepenapple"` | `["apple", "pen"]` | $\{0, 5, 8, 13\}$ | true |
| `sample-3` | `"catsandog"` | `["cats", "dog", "sand", "and", "cat"]` | $\{0, 3, 4, 7\}$ | false |
| `trial-single-miss` | `"a"` | `["b"]` | $\{0\}$ | false |
| `trial-reused-words` | `"aaaaaaa"` | `["aaaa", "aaa"]` | $\{0, 3, 4, 6, 7\}$ | true |

Two rows carry most of the teaching value. In `sample-2` the word `"apple"` is consumed twice, once from boundary 0 and again from boundary 8, which is what makes arbitrary reuse of dictionary words essential rather than convenient. In `trial-reused-words` the reachable set contains four interior boundaries, so the final prefix can be completed in two different orders, `"aaa"` followed by `"aaaa"` from boundary 3, or `"aaaa"` followed by `"aaa"` from boundary 4; a solver that commits to the longest word at boundary 0 still succeeds, but one that commits to a single fixed word length does not.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2 \cdot K)$, where $N = |s|$ and $K$ is the maximum length of a word in `wordDict` ($K \le N$). With max length pruning, the inner loop runs at most $K$ times, each taking $O(K)$ to slice and hash, yielding $O(N \cdot K^2)$ total operations.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory for the boolean $DP$ array of length $N + 1$, plus $O(M)$ for the hash set of dictionary words.

The recurrence is the same in every row below; what changes is how many candidate suffixes are tested and whether a substring is ever materialized:

| Strategy | Decision procedure | Time | Auxiliary space | Behavior on these cases |
|:---|:---|:---:|:---:|:---|
| Unmemoized recursion | Try every dictionary word that prefixes the remaining suffix | $O(2^N)$ | $O(N)$ recursion stack | Exponential on `trial-reused-words`, because `"aaa"` and `"aaaa"` re-enter the same suffix boundaries |
| Prefix DP testing every split | Test all $j < i$ and slice $s[j \dots i-1]$ | $O(N^3)$ worst case | $O(N)$ | Correct, but on `"applepenapple"` it slices substrings of length up to 13 for each of the 91 candidate pairs |
| Prefix DP with maximum-word-length pruning | Test only the $K$ most recent boundaries | $O(N \cdot K^2)$ | $O(N)$ | This lesson's method; for `sample-1` only length 4 is ever tested |
| Prefix DP plus a trie walk | From each reachable boundary, descend the trie along `s` instead of slicing | $O(N \cdot K)$ | $O(N)$ plus $O\left(\sum_{w} \lvert w \rvert\right)$ for the trie | Removes the slicing factor and abandons a walk as soon as no dictionary word continues |
| BFS over reachable boundaries | Treat each reachable index as a graph node and each dictionary word as an edge | $O(N \cdot K^2)$ | $O(N)$ | Visits only reachable indices, so on `sample-3` it never examines boundary 6 |

Every row returns the same values on the authored cases; they differ in how much work the failing suffix `"og"` costs before the search gives up. The DP rows pay for it in one pass, while the recursion row pays for it by re-deriving the same unreachable boundaries repeatedly.

---
