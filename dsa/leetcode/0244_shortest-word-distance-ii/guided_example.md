# Guided Example: Shortest Word Distance II

We trace the step-by-step posting list hash table preprocessing, ascending index extraction, and dual-pointer sorted list merge search on representative recurring word distance queries:

- **Input:**
  - Initialization: $\text{wordsDict} = [\text{"practice"}, \text{"makes"}, \text{"perfect"}, \text{"coding"}, \text{"makes"}]$
  - Query 1: `shortest("coding", "practice")` $\implies 3$ (Index $3$ vs index $0$)
  - Query 2: `shortest("makes", "coding")` $\implies 1$ (Index $4$ vs index $3$)
- **Multi-Occurrence Instance:** $\text{wordsDict} = [\text{"a"}, \text{"b"}, \text{"a"}, \text{"c"}], \quad \text{shortest("a", "c")} \implies 1$ (Index $2$ vs index $3$)

This instance demonstrates amortized precomputation for multi-query word proximity, explains indexing word occurrences into naturally sorted posting lists in $O(N)$ construction time, details the two-pointer bisection merge on sorted index arrays in $O(L_1 + L_2)$ query time, and proves why smaller pointer advancement monotonically narrows the search frontier.

---

## 1. Instance & Teaching Goal

We design the `WordDistance` data structure for repeatedly querying the minimum index distance between two words:
```text
wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
WordDistance wd = new WordDistance(wordsDict);
wd.shortest("coding", "practice"); // returns 3
wd.shortest("makes", "coding");    // returns 1
```

In LeetCode 243 (Shortest Word Distance I), a single query was answered by scanning the entire array in $O(N)$ time.
In this problem, `shortest` will be called repeatedly (up to $5,000$ times). Running an $O(N)$ scan per query would cost $O(Q \cdot N) \approx 5000 \times 30000 = 1.5 \times 10^8$ operations, causing Time Limit Exceeded (TLE).
- **Constructor ($O(N)$ Time & Space):** Map each distinct word to the sorted list of indices where it appears (a posting list).
- **Query ($O(L_1 + L_2)$ Time):** With two sorted index lists $A$ and $B$, find the minimum absolute difference $|a - b|$ in linear time using two pointers.

### Design Alternatives Compared

| Design | One-time preprocessing | Cost per `shortest` call | Auxiliary space | When it wins, and how it fails |
|:---|:---|:---|:---|:---|
| Rescan the dictionary on every call (the single-query design) | none | $O(N \cdot L)$ word comparisons | $O(1)$ | Optimal when exactly one query is ever asked; with $5000$ queries over $30000$ words it performs about $1.5 \times 10^8$ comparisons and times out |
| Posting lists plus two-pointer merge (chosen) | $O(N \cdot L)$ to bucket every word | $O(L_1 + L_2)$ pointer steps | $O(N)$ for all posting lists | Every call is linear in the two occurrence counts rather than in $N$; the only price is that the whole index is held in memory |
| Posting lists plus binary search of the shorter list | $O(N \cdot L)$ | $O(\min(L_1, L_2) \cdot \log \max(L_1, L_2))$ | $O(N)$ | Wins when one target occurs once and the other occurs very often; loses to the merge when both lists are long, because each probe pays a logarithm |
| Precomputed distance for every word pair | $O(N^2)$ pairs, both time and space | $O(1)$ lookup | $O(N^2)$ | Would make each call constant time, but at $N = 30000$ it needs on the order of $9 \times 10^8$ table entries before any deduplication |

---

## 2. Conceptual Foundation & Invariants

### 1. Posting List Construction
Store a hash map `indices`:
For index $i$ and word $w \in \text{wordsDict}$:
$$
\text{indices}[w].\text{append}(i)
$$
Because the loop iterates $i = 0 \dots N - 1$ in ascending order, each list $\text{indices}[w]$ is **automatically sorted in strictly increasing order** without requiring explicit sorting!

### 2. Two-Pointer Merging Protocol for `shortest(word1, word2)`
Let $A = \text{indices}[\text{word1}]$ and $B = \text{indices}[\text{word2}]$.
Initialize $p_1 = 0, \quad p_2 = 0, \quad \text{min\_dist} = \infty$:
While $p_1 < \text{len}(A)$ and $p_2 < \text{len}(B)$:
1. Update candidate minimum distance:
   $$
   \text{min\_dist} \leftarrow \min(\text{min\_dist}, \; |A[p_1] - B[p_2]|)
   $$
2. **Monotonic Frontier Advancement:**
   - If $A[p_1] < B[p_2]$:
     Advance $p_1 \leftarrow p_1 + 1$.
     *(Why? Because $B$ is sorted, all future elements $B[j]$ ($j > p_2$) are even larger than $B[p_2]$, so $|A[p_1] - B[j]| = B[j] - A[p_1] > B[p_2] - A[p_1]$. Pair $(A[p_1], B[p_2])$ is already the best possible pair involving $A[p_1]$; incrementing $p_1$ is safe)*.
   - Else:
     Advance $p_2 \leftarrow p_2 + 1$.
     *(Symmetrically, $A[p_1] - B[p_2] > 0$, so later $A[i]$ would only increase the distance)*.

Return $\text{min\_dist}$.

> **Invariant.** At each step, advancing the pointer with the smaller index discards an index that is provably farther from all remaining candidate indices in the other list.

---

## 3. Step-by-Step Worked Execution

### Preprocessing Phase: `WordDistance(wordsDict)`
Given $\text{wordsDict} = [\text{"practice"}, \text{"makes"}, \text{"perfect"}, \text{"coding"}, \text{"makes"}]$:
- $i = 0$: `"practice"` $\to [0]$
- $i = 1$: `"makes"` $\to [1]$
- $i = 2$: `"perfect"` $\to [2]$
- $i = 3$: `"coding"` $\to [3]$
- $i = 4$: `"makes"` $\to [1, 4]$

Precomputed index dictionary:
```text
{
  "practice": [0],
  "makes":    [1, 4],
  "perfect":  [2],
  "coding":   [3]
}
```

---

### Query 1: `shortest("coding", "practice")`
- Target lists: $A = [3]$, $B = [0]$.
- Start: $p_1 = 0 \, (A[0] = 3), \quad p_2 = 0 \, (B[0] = 0)$.
- Distance: $|3 - 0| = 3$.
  $\text{min\_dist} = \min(\infty, 3) = \mathbf{3}$.
- Compare: $A[0] = 3 > B[0] = 0 \implies$ Advance $p_2 \leftarrow 1$.
- $p_2 = 1 == \text{len}(B) \implies$ Loop terminates.
- **Return $3$.**

---

### Query 2: `shortest("makes", "coding")`
- Target lists: $A = [1, 4]$ (`"makes"`), $B = [3]$ (`"coding"`).
- Initial state: $p_1 = 0, \, p_2 = 0, \, \text{min\_dist} = \infty$.

**Iteration 1:**
- Current elements: $A[p_1] = 1, \quad B[p_2] = 3$.
- Distance: $|1 - 3| = 2$.
  $\text{min\_dist} \leftarrow \min(\infty, 2) = \mathbf{2}$.
- Compare: $A[0] = 1 < B[0] = 3 \implies$ Advance $p_1 \leftarrow 1$.

**Iteration 2:**
- Current elements: $A[p_1] = 4, \quad B[p_2] = 3$.
- Distance: $|4 - 3| = 1$.
  $\text{min\_dist} \leftarrow \min(2, 1) = \mathbf{1}$.
- Compare: $A[1] = 4 > B[0] = 3 \implies$ Advance $p_2 \leftarrow 1$.

**Termination:**
- $p_2 = 1 == \text{len}(B) \implies$ Loop terminates.
- **Return $1$.**

---

## 4. Complete Execution Trace

```text
Target A ("makes"):  [1, 4]
Target B ("coding"): [3]

Step 1: p1=0 (val 1), p2=0 (val 3) -> |1 - 3| = 2 -> min_dist = 2
        1 < 3 -> advance p1 to 1

Step 2: p1=1 (val 4), p2=0 (val 3) -> |4 - 3| = 1 -> min_dist = 1
        4 > 3 -> advance p2 to 1

p2 reaches end -> Stop -> Return 1
```

| Query Call | Step | Pointer $p_1$ ($A$) | Pointer $p_2$ ($B$) | Absolute Difference $\lvert A[p_1] - B[p_2] \rvert$ | Running $\text{min\_dist}$ | Pointer Advanced |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| `shortest("coding", "practice")` | 1 | $p_1 = 0$ ($3$) | $p_2 = 0$ ($0$) | $\lvert 3 - 0 \rvert = 3$ | **3** | $p_2 \leftarrow 1$ (End) |
| `shortest("makes", "coding")` | 1 | $p_1 = 0$ ($1$) | $p_2 = 0$ ($3$) | $\lvert 1 - 3 \rvert = 2$ | 2 | $p_1 \leftarrow 1$ |
| `shortest("makes", "coding")` | 2 | $p_1 = 1$ ($4$) | $p_2 = 0$ ($3$) | $\lvert 4 - 3 \rvert = 1$ | **1** | $p_2 \leftarrow 1$ (End) |

---

## 5. Algorithmic Correctness

**Soundness.** Every difference $|A[p_1] - B[p_2]|$ is formed by indices where `wordsDict` contains `word1` and `word2` respectively.

**Completeness.** Let $(a^*, b^*)$ be a globally optimal pair with $a^* \in A$, $b^* \in B$, and assume without loss of generality that $a^* < b^*$. No index of either list lies strictly between $a^*$ and $b^*$: an $A$-index $c$ with $a^* < c < b^*$ would pair with $b^*$ at distance $b^* - c < b^* - a^*$, and a $B$-index $c$ in that same range would pair with $a^*$ at distance $c - a^* < b^* - a^*$. Either case contradicts optimality, so the smallest $B$-index strictly greater than $a^*$ must be $b^*$ itself.

Now watch the walk at the step where $p_1$ first holds $a^*$. A cursor only leaves an element when the *other* cursor is strictly larger, so $p_2$ cannot have moved beyond $b^*$ while $p_1$ was still left of $a^*$; at this step $p_2$ therefore sits either below $a^*$ or exactly on $b^*$. If it sits below $a^*$, the merge holds $p_1$ fixed (because $A[p_1] > B[p_2]$) and advances $p_2$ until it reaches the first $B$-index above $a^*$, which is $b^*$. That step scores the pair $(a^*, b^*)$ before $p_1$ is allowed to move past $a^*$, so the true minimum is always among the evaluated pairs.

### Which Candidate Pairs the Merge Actually Scores

Take the lists produced by $\text{wordsDict} = [\text{"a"}, \text{"x"}, \text{"b"}, \text{"x"}, \text{"a"}, \text{"b"}, \text{"x"}, \text{"b"}]$: for the query `shortest("a", "b")` we have $A = [0, 4]$ and $B = [2, 5]$. There are $L_1 \cdot L_2 = 4$ pairs in principle, but the merge can only ever score $L_1 + L_2 - 1 = 3$ of them:

| Candidate pair | Distance | Scored by the walk? | What the frontier rule decides |
|:---:|:---:|:---|:---|
| $(0, 2)$ | 2 | At step 1 | Both cursors begin here; $0 < 2$, so the pair is scored and $A$-index $0$ is consumed |
| $(0, 5)$ | 5 | Never | Once $p_1$ leaves index $0$ it never returns, and the walk only ever pairs the current cursor values, so this combination becomes unreachable |
| $(4, 2)$ | 2 | At step 2 | $p_1$ now holds $4$ and $4 > 2$, so the merge holds $p_1$ and advances $p_2$ instead of consuming the larger $A$-index |
| $(4, 5)$ | 1 | At step 3 | The last reachable pair; it lowers the incumbent to $1$, after which $p_1$ runs off the end of $A$ |

The skipped pair carries distance $5$, comfortably worse than the $2$ already banked, and the dominance rule explains why this is not luck: when $A[p_1] < B[p_2]$, every later $B$-index is at least as far from $A[p_1]$ as $B[p_2]$ already is, so that pair is the best one involving $A[p_1]$ and the index can be discarded. The walk replaces $L_1 \cdot L_2$ pair tests with at most $L_1 + L_2 - 1$ pointer steps.

---

## 6. Traps This Instance Exposes

- **Nested $O(L_1 \cdot L_2)$ Loops:** If a word appears $10,000$ times, a nested loop checking all pairs evaluates $10^8$ operations per query. The two-pointer merge checks at most $L_1 + L_2$ steps.
- **Short-Circuit on Minimum Possible Distance:** The smallest possible distance between two distinct words is $1$. If $\text{min\_dist} == 1$, returning $1$ immediately provides an early exit optimization.
- **Binary Search Alternative:** If one list has size $1$ and the other has size $10,000$, binary searching for the single element inside the large list takes $O(\log L_2)$ time instead of $O(L_2)$. The two-pointer method is $O(L_1 + L_2)$ and universally optimal across general queries.

### Boundary Behaviour of the Structure

| Boundary scenario | Concrete input | Required result | Why the structure returns it |
|:---|:---|:---|:---|
| Constructed but never queried | $\text{wordsDict} = [\text{"a"}]$ with an empty query sequence | an empty result sequence | The constructor only buckets indices, so it must tolerate a dictionary of length $1$ and must not assume that any `shortest` call follows |
| Smallest queryable dictionary | $\text{wordsDict} = [\text{"x"}, \text{"y"}]$, one query `shortest("x", "y")` | $1$ | Each posting list holds a single index, so the merge scores exactly one pair and terminates immediately |
| Symmetric query order with a repeated word | $\text{wordsDict} = [\text{"a"}, \text{"b"}, \text{"a"}, \text{"c"}]$, posting list `"a"` $= [0, 2]$ | `shortest("a", "c")` $= 1$ and `shortest("c", "a")` $= 1$ | The walk is symmetric in its two lists and the difference is an absolute value, so swapping the arguments cannot change the answer; the two-element list is reused from the constructor rather than rebuilt |
| Optimum found mid-merge, not at the first scored pair | $\text{wordsDict} = [\text{"a"}, \text{"x"}, \text{"b"}, \text{"x"}, \text{"a"}, \text{"b"}, \text{"x"}, \text{"b"}]$ | `shortest("a", "b")` $= 1$ and `shortest("x", "b")` $= 1$ | For `"x"` versus `"b"` the walk needs all $4$ of its steps and the minimum appears only on the last of them, so an early exit that trusts the first scored pair would be wrong |
| Maximum scale with a repeated query | $30000$ words with one distinct query pair requested $5000$ times | $29999$ on every one of the $5000$ calls | The index is built once; each call merges two single-element lists in one step, whereas rescanning per call would cost $5000 \times 30000 = 1.5 \times 10^8$ comparisons |

---

## 7. Complexity Derivation

- **Time Complexity:**
  - **Constructor:** $O(N \cdot L)$, where $N$ is the number of words in `wordsDict` and $L$ is word length. Single pass to populate the hash map.
  - **`shortest(word1, word2)`:** $O(L_1 + L_2)$, where $L_1$ and $L_2$ are the occurrence counts of `word1` and `word2` ($L_1 + L_2 \le N$). In each iteration, either $p_1$ or $p_2$ increments by 1.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory to store all $N$ indices partitioned across lists in the hash map.
