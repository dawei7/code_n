# Guided Example: Shortest Word Distance III

We trace the step-by-step distinct-word vs identical-word bifurcation, consecutive identical-instance gap evaluation, and unified streaming state tracking on representative string dictionaries:

- **Input:** $\text{wordsDict} = [\text{"practice"}, \text{"makes"}, \text{"perfect"}, \text{"coding"}, \text{"makes"}], \quad \text{word1} = \text{"makes"}, \quad \text{word2} = \text{"makes"}$
- **Required output:** $3$ (Indices $1$ and $4$ share word $\text{"makes"}$; $|4 - 1| = 3$)
- **Different Targets Instance:** $\text{word1} = \text{"makes"}, \quad \text{word2} = \text{"coding"} \implies 1$ (Index $4$ and index $3$)
- **Minimal Pair Instance:** $\text{wordsDict} = [\text{"a"}, \text{"a"}], \quad \text{word1} = \text{"a"}, \quad \text{word2} = \text{"a"} \implies 1$
- **Multiple Duplicate Run:** $\text{wordsDict} = [\text{"a"}, \text{"b"}, \text{"a"}, \text{"a"}], \quad \text{word1} = \text{"a"}, \quad \text{word2} = \text{"a"} \implies 1$ (Consecutive duplicate pair at indices 2 and 3)

This instance demonstrates handling identical target parameters ($\text{word1} == \text{word2}$) without self-collision ($i == j \implies \text{dist} = 0$), proves why the minimum distance between identical words must occur between consecutive occurrences, unifies both distinct and equal word logic in a single $O(N)$ forward pass, and operates in strictly $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given a string dictionary $\text{wordsDict} = [\text{"practice"}, \text{"makes"}, \text{"perfect"}, \text{"coding"}, \text{"makes"}]$:
Find the shortest index distance $|i - j|$ between an occurrence of `word1` and an occurrence of `word2`, where $i \ne j$.

### The Identical Target Challenge ($\text{word1} == \text{word2}$)
In LeetCode 243, `word1 != word2` was guaranteed.
In this problem, **`word1` and `word2` may be identical strings**:
- If `word1 != word2`: The problem reduces to tracking the latest occurrence of each distinct label.
- If `word1 == word2`: We must find the minimum distance between **two distinct occurrences** of the same word.
If we blindly applied the LeetCode 243 logic when $\text{word1} == \text{word2}$:
Both pointers would update to the same index ($i = j$), yielding a false distance of $|i - i| = 0$!
To prevent self-collision, when $\text{word1} == \text{word2}$, we shift the previous index before recording the new one, measuring the distance strictly between **consecutive occurrences** of the shared word.

### Design Alternatives Compared

| Design | Mechanism | Time | Auxiliary space | Outcome on this instance |
|:---|:---|:---:|:---:|:---|
| Reuse the two-cursor scheme unchanged | Let the same index variable be written by both match tests | $O(N \cdot L)$ | $O(1)$ | Wrong whenever $\text{word1} == \text{word2}$: both branches fire on the same character, so $\text{idx}_1 = \text{idx}_2 = i$ and the recorded distance $0$ is not even a legal pair |
| Enumerate every pair of occurrences | Collect the occurrence list of the target and test all pairs | $O(N \cdot L) + O(K^2)$ | $O(K)$ | Correct but quadratic in the occurrence count $K$; a word occupying a long consecutive run forces nearly $K^2 / 2$ comparisons for an answer of $1$ |
| Posting lists plus adjacent-gap scan | Bucket every word once, then scan neighbouring gaps in one list | $O(N \cdot L)$ | $O(N)$ | Correct for both cases, at the price of materialising the whole index structure even though a single answer is requested |
| Streaming cursors with an explicit same-word branch (chosen) | Shift the previous occurrence into a second cursor before writing the new one | $O(N \cdot L)$ | $O(1)$ | Handles distinct and identical targets in one pass, checks only consecutive occurrences, and the run ends at the minimum possible value $1$ |

---

## 2. Conceptual Foundation & Invariants

### The Consecutive Occurrence Distance Lemma
Suppose a target word appears at sorted indices $p_1 < p_2 < \dots < p_m$.
Any non-consecutive gap can be decomposed as a sum of positive consecutive gaps:
$$
p_k - p_j = (p_{j+1} - p_j) + (p_{j+2} - p_{j+1}) + \dots + (p_k - p_{k-1}) \ge \min_{r}(p_{r+1} - p_r)
$$
Because all gaps are positive integers, the minimum distance between any two distinct occurrences of the same word is **strictly achieved between two consecutive occurrences**!
Therefore, we only need to compare each occurrence with its immediate predecessor.

### Unified Algorithm Protocol
Initialize $\text{idx}_1 = -1, \quad \text{idx}_2 = -1, \quad \text{min\_dist} = \infty$.
Let $\text{is\_same} = (\text{word1} == \text{word2})$.

For each index $i$ and word $w \in \text{wordsDict}$:
1. **Match Target 1 ($w == \text{word1}$):**
   - If $\text{is\_same}$:
     Shift history to preserve distinct occurrences:
     $$
     \text{idx}_1 \leftarrow \text{idx}_2, \quad \text{idx}_2 \leftarrow i
     $$
   - Else:
     $$
     \text{idx}_1 \leftarrow i
     $$
2. **Match Target 2 ($w == \text{word2}$ and $\text{not is\_same}$):**
   $$
   \text{idx}_2 \leftarrow i
   $$
3. **Distance Evaluation:**
   If $\text{idx}_1 \ne -1$ and $\text{idx}_2 \ne -1$:
   $$
   \text{min\_dist} \leftarrow \min(\text{min\_dist}, \; |\text{idx}_1 - \text{idx}_2|)
   $$

Return $\text{min\_dist}$.

> **Invariant.** Whenever neither sentinel is still in place, $\text{idx}_1$ and $\text{idx}_2$ are two *distinct* indices of $\text{wordsDict}$ with $\text{wordsDict}[\text{idx}_1] == \text{word1}$ and $\text{wordsDict}[\text{idx}_2] == \text{word2}$; while a sentinel remains, the pair is simply not complete yet and no distance is formed. In the $\text{is\_same}$ branch the shift leaves $\text{idx}_1 < \text{idx}_2$, so a self-distance of $0$ can never be produced.

---

## 3. Step-by-Step Worked Execution

We trace two queries on $\text{wordsDict} = [\text{"practice"}, \text{"makes"}, \text{"perfect"}, \text{"coding"}, \text{"makes"}]$:

### Query 1: Identical Targets ($\text{word1} = \text{"makes"}, \quad \text{word2} = \text{"makes"}$)
Here $\text{is\_same} = \text{True}$.
Initial state: $\text{idx}_1 = -1, \, \text{idx}_2 = -1, \, \text{min\_dist} = \infty$.

- **Index $i = 0$ ($w = \text{"practice"}$):**
  - No match. State unchanged.
- **Index $i = 1$ ($w = \text{"makes"}$):**
  - Target match! Since $\text{is\_same}$ is True:
    $$
    \text{idx}_1 \leftarrow \text{idx}_2 = -1
    $$
    $$
    \text{idx}_2 \leftarrow i = 1
    $$
  - Since $\text{idx}_1 == -1$, no pair yet.
  - State: $\text{idx}_1 = -1, \, \text{idx}_2 = 1, \, \text{min\_dist} = \infty$.
- **Index $i = 2$ ($w = \text{"perfect"}$):** No match.
- **Index $i = 3$ ($w = \text{"coding"}$):** No match.
- **Index $i = 4$ ($w = \text{"makes"}$):**
  - Target match! Since $\text{is\_same}$ is True:
    $$
    \text{idx}_1 \leftarrow \text{idx}_2 = 1
    $$
    $$
    \text{idx}_2 \leftarrow i = 4
    $$
  - Both indices valid! Candidate distance:
    $$
    |\text{idx}_1 - \text{idx}_2| = |1 - 4| = 3
    $$
  - $\text{min\_dist} \leftarrow \min(\infty, 3) = \mathbf{3}$.
  - State: $\text{idx}_1 = 1, \, \text{idx}_2 = 4, \, \text{min\_dist} = 3$.

Loop terminates. Output: $\mathbf{3}$.

---

### Query 2: Distinct Targets ($\text{word1} = \text{"makes"}, \quad \text{word2} = \text{"coding"}$)
Here $\text{is\_same} = \text{False}$.
- $i = 1$ (`"makes"`): $\text{idx}_1 \leftarrow 1$.
- $i = 3$ (`"coding"`): $\text{idx}_2 \leftarrow 3 \implies |\text{idx}_1 - \text{idx}_2| = |1 - 3| = 2$.
  $\text{min\_dist} \leftarrow 2$.
- $i = 4$ (`"makes"`): $\text{idx}_1 \leftarrow 4 \implies |\text{idx}_1 - \text{idx}_2| = |4 - 3| = 1$.
  $\text{min\_dist} \leftarrow 1$.
Output: $\mathbf{1}$.

---

## 4. Complete Execution Trace

```text
Query: word1 = "makes", word2 = "makes" (is_same = True)

i = 0 ("practice"): no match
i = 1 ("makes"):    idx1 = -1, idx2 = 1 -> no pair
i = 2 ("perfect"):  no match
i = 3 ("coding"):   no match
i = 4 ("makes"):    idx1 = 1,  idx2 = 4 -> dist = |1 - 4| = 3 -> min_dist = 3

Result: 3
```

| Index $i$ | Word $w$ | Match Branch | $\text{idx}_1$ | $\text{idx}_2$ | Pair Distance Evaluated | Running $\text{min\_dist}$ |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 0 | `"practice"` | None | -1 | -1 | - | $\infty$ |
| 1 | `"makes"` | $\text{is\_same}$ shift | -1 | 1 | - | $\infty$ |
| 2 | `"perfect"` | None | -1 | 1 | - | $\infty$ |
| 3 | `"coding"` | None | -1 | 1 | - | $\infty$ |
| **4** | **`"makes"`** | **$\text{is\_same}$ shift** | **1** | **4** | **$\lvert 1 - 4 \rvert = 3$** | **$\mathbf{3}$ (Final Answer)** |

---

## 5. Algorithmic Correctness

**Soundness.** For $\text{word1} \ne \text{word2}$, the algorithm matches the proven logic of LeetCode 243. For $\text{word1} == \text{word2}$, setting $\text{idx}_1 = \text{idx}_2$ and $\text{idx}_2 = i$ guarantees that $\text{idx}_1$ holds the index of the immediately preceding occurrence, so $\text{idx}_1 \ne \text{idx}_2$ always holds and the evaluated gap is between two distinct occurrences.

**Completeness.** By the Consecutive Occurrence Lemma, the minimum distance between identical words is achieved between two adjacent occurrences. Since every adjacent pair is evaluated when the right word is reached, the global minimum is guaranteed to be recorded.

### Every Identical-Target Pair, and the Six That Collapse to Three

Take $\text{wordsDict} = [\text{"x"}, \text{"a"}, \text{"x"}, \text{"a"}, \text{"b"}, \text{"a"}, \text{"a"}]$ with $\text{word1} = \text{word2} = \text{"a"}$. The shared word occupies indices $p = [1, 3, 5, 6]$, so six distinct pairs of occurrences exist, yet the scan examines only the three consecutive ones:

| Pair of occurrences $(p_r, p_s)$ | Gap $p_s - p_r$ | Examined by the consecutive-only scan? | Why it can never be the reported minimum |
|:---:|:---:|:---|:---|
| $(1, 3)$ | 2 | Yes, when index $3$ is reached | The pair is consecutive, so nothing stands between the two occurrences and the gap is directly recorded |
| $(1, 5)$ | 4 | No | Index $3$ lies inside the interval, so $4 = 2 + 2$; the interior consecutive gap $2$ is strictly smaller |
| $(1, 6)$ | 5 | No | Two interior occurrences split the gap as $2 + 2 + 1$, and the final part $1$ is strictly smaller |
| $(3, 5)$ | 2 | Yes, when index $5$ is reached | Consecutive pair, recorded as a tie with the earlier candidate $2$ |
| $(3, 6)$ | 3 | No | Index $5$ splits the gap as $2 + 1$, so the interior part $1$ is strictly smaller |
| $(5, 6)$ | 1 | Yes, when index $6$ is reached | Consecutive pair, and it lowers the running minimum to $1$, which is the smallest distance two distinct indices can have |

Every skipped pair contains at least one interior occurrence, and its gap is a sum of positive parts, each strictly smaller than the whole. So a skipped pair can only be as good as a pair already examined, never better, and the reported answer is $\mathbf{1}$.

---

## 6. Traps This Instance Exposes

- **Self-Distance Zero Trap:** If the distinction between $\text{word1} == \text{word2}$ and $\text{word1} \ne \text{word2}$ is ignored, encountering `"makes"` updates both $\text{idx}_1$ and $\text{idx}_2$ to $i$, resulting in $|i - i| = 0$.
- **Non-Adjacent Pair Redundancy:** Checking all pairs of identical occurrences takes $O(K^2)$ time. Comparing only consecutive occurrences reduces this to $O(K)$ without missing the minimum.
- **Short-Circuiting on 1:** If $\text{min\_dist} == 1$ is ever reached, it can immediately be returned since no two elements can have distance $< 1$.

### Boundary Behaviour of the Two Branches

| Boundary scenario | Concrete input | Required result | Why the scan returns it |
|:---|:---|:---|:---|
| Smallest dictionary with identical targets | $\text{wordsDict} = [\text{"a"}, \text{"a"}]$, $\text{word1} = \text{word2} = \text{"a"}$ | $1$ | Index $0$ only seeds the history ($\text{idx}_2 = 0$, $\text{idx}_1$ still $-1$); index $1$ shifts and scores $1 - 0 = 1$, the smallest value two distinct indices can have |
| Distinct targets with one occurrence each | $\text{wordsDict} = [\text{"a"}, \text{"x"}, \text{"x"}, \text{"b"}]$, $\text{word1} = \text{"a"}$, $\text{word2} = \text{"b"}$ | $3$ | Exactly one candidate pair exists, $\lvert 0 - 3 \rvert$; the sentinels stop any distance from being formed before both characters have appeared |
| Best identical pair appears late | $\text{wordsDict} = [\text{"x"}, \text{"a"}, \text{"x"}, \text{"a"}, \text{"b"}, \text{"a"}, \text{"a"}]$ | $1$ | The shared word sits at indices $1, 3, 5, 6$; consecutive gaps of $2$, then $2$, then $1$ are scored in order, so the early candidate $2$ must not be treated as final |
| Distinct targets whose best pair is found after the first live pair | $\text{wordsDict} = [\text{"practice"}, \text{"makes"}, \text{"perfect"}, \text{"coding"}, \text{"makes"}]$, $\text{word1} = \text{"makes"}$, $\text{word2} = \text{"coding"}$ | $1$ | The first live pair scores $\lvert 1 - 3 \rvert = 2$; the later occurrence of `"makes"` at index $4$ overwrites the cursor and scores $\lvert 4 - 3 \rvert = 1$ |
| Two occurrences at the two ends of a maximum dictionary | $100000$ words with `"aaaaaaaaaa"` at index $0$ and again at index $99999$ | $99999$ | Only matches update the cursors, so the $99998$ unmatched words in between leave the history intact and the single consecutive gap equals the full span |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot L)$, where $N$ is the number of words in `wordsDict` and $L$ is the maximum word length ($\le 10$). A single forward pass is performed with $O(1)$ scalar updates per word.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory.
