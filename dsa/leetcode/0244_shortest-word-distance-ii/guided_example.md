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

| Query Call | Step | Pointer $p_1$ ($A$) | Pointer $p_2$ ($B$) | Absolute Difference $|A[p_1] - B[p_2]|$ | Running $\text{min\_dist}$ | Pointer Advanced |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| `shortest("coding", "practice")` | 1 | $p_1 = 0$ ($3$) | $p_2 = 0$ ($0$) | $|3 - 0| = 3$ | **3** | $p_2 \leftarrow 1$ (End) |
| `shortest("makes", "coding")` | 1 | $p_1 = 0$ ($1$) | $p_2 = 0$ ($3$) | $|1 - 3| = 2$ | 2 | $p_1 \leftarrow 1$ |
| `shortest("makes", "coding")` | 2 | $p_1 = 1$ ($4$) | $p_2 = 0$ ($3$) | $|4 - 3| = 1$ | **1** | $p_2 \leftarrow 1$ (End) |

---

## 5. Algorithmic Correctness

**Soundness.** Every difference $|A[p_1] - B[p_2]|$ is formed by indices where `wordsDict` contains `word1` and `word2` respectively.

**Completeness.** Let $(a^*, b^*)$ be a globally optimal pair with $a^* \in A, b^* \in B$. Without loss of generality, assume $a^* < b^*$. In the two-pointer traversal, $p_1$ can only advance past $a^*$ when $A[p_1] \ge B[p_2]$. If $p_2$ had not reached $b^*$ yet, $B[p_2] \le a^* < b^*$, meaning $p_1$ does not advance past $a^*$ until $p_2$ catches up. The pair $(a^*, b^*)$ is guaranteed to be evaluated during the walk, ensuring the true minimum is found.

---

## 6. Traps This Instance Exposes

- **Nested $O(L_1 \cdot L_2)$ Loops:** If a word appears $10,000$ times, a nested loop checking all pairs evaluates $10^8$ operations per query. The two-pointer merge checks at most $L_1 + L_2$ steps.
- **Short-Circuit on Minimum Possible Distance:** The smallest possible distance between two distinct words is $1$. If $\text{min\_dist} == 1$, returning $1$ immediately provides an early exit optimization.
- **Binary Search Alternative:** If one list has size $1$ and the other has size $10,000$, binary searching for the single element inside the large list takes $O(\log L_2)$ time instead of $O(L_2)$. The two-pointer method is $O(L_1 + L_2)$ and universally optimal across general queries.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - **Constructor:** $O(N \cdot L)$, where $N$ is the number of words in `wordsDict` and $L$ is word length. Single pass to populate the hash map.
  - **`shortest(word1, word2)`:** $O(L_1 + L_2)$, where $L_1$ and $L_2$ are the occurrence counts of `word1` and `word2` ($L_1 + L_2 \le N$). In each iteration, either $p_1$ or $p_2$ increments by 1.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory to store all $N$ indices partitioned across lists in the hash map.
