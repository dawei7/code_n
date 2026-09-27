# Guided Example: Shortest Word Distance

We trace the step-by-step single-pass index tracking, closest-neighbor distance minimization, and streaming state updates on representative string dictionaries:

- **Input:** $\text{wordsDict} = [\text{"practice"}, \text{"makes"}, \text{"perfect"}, \text{"coding"}, \text{"makes"}], \quad \text{word1} = \text{"coding"}, \quad \text{word2} = \text{"practice"}$
- **Required output:** $3$ (Indices: $\text{"coding"}$ at $3$, $\text{"practice"}$ at $0 \implies |3 - 0| = 3$)
- **Adjacent Duplicates Instance:** $\text{word1} = \text{"makes"}, \quad \text{word2} = \text{"coding"} \implies 1$ (Closest pair is index $3$ and index $4$: $|3 - 4| = 1$)
- **Minimal Array Instance:** $\text{wordsDict} = [\text{"a"}, \text{"b"}], \quad \text{word1} = \text{"a"}, \quad \text{word2} = \text{"b"} \implies 1$
- **Opposite Boundary Instance:** $\text{wordsDict} = [\text{"a"}, \text{"c"}, \text{"d"}, \text{"b"}], \quad \text{word1} = \text{"a"}, \quad \text{word2} = \text{"b"} \implies 3$

This instance demonstrates linear streaming proximity tracking on list indices, mathematically proves why updating distance only against the most recently seen opposite target guarantees capturing the global minimum, details $O(1)$ auxiliary space without collecting full index lists, and runs in $O(N)$ time.

---

## 1. Instance & Teaching Goal

Given a list of words:
$$
\text{wordsDict} = [\text{"practice"}, \text{"makes"}, \text{"perfect"}, \text{"coding"}, \text{"makes"}]
$$
Find the shortest index distance $|i - j|$ between an occurrence of $\text{word1} = \text{"coding"}$ and an occurrence of $\text{word2} = \text{"practice"}$.

- Index of `"practice"`: $[0]$
- Indices of `"coding"`: $[3]$
- Indices of `"makes"`: $[1, 4]$
For `"coding"` and `"practice"`, the distance is $|3 - 0| = \mathbf{3}$.
For `"makes"` and `"coding"`, possible pairs are $(1, 3)$ with distance $2$, and $(4, 3)$ with distance $1$. The minimum distance is $\mathbf{1}$.

A brute-force comparison collects all indices of `word1` ($K_1$ indices) and `word2` ($K_2$ indices) and checks all pairs in $O(K_1 \cdot K_2) = O(N^2)$ time.
A streaming single-pass approach updates the most recently observed index for both targets. It computes the distance only against the latest opposite target, finding the global optimum in a single $O(N)$ pass with $O(1)$ extra space.

---

## 2. Conceptual Foundation & Invariants

### The Latest-Occurrence Optimality Lemma
Suppose we scan from left to right and encounter $\text{word1}$ at index $k$.
Consider all occurrences of $\text{word2}$ seen so far at indices $j_1 < j_2 < \dots < j_m < k$.
Because distance is $|k - j| = k - j$ (for $j < k$):
$$
k - j_m < k - j_{m-1} < \dots < k - j_1
$$
The **most recent** occurrence $j_m$ is strictly closer to $k$ than all previous occurrences of $\text{word2}$!
Therefore, we never need to compare $k$ against earlier occurrences $j_1, \dots, j_{m-1}$.
Tracking only the latest index of each target is necessary and sufficient.

### Streaming Protocol:
Initialize $\text{idx}_1 = -1, \quad \text{idx}_2 = -1, \quad \text{min\_dist} = \infty$:
For each index $i$ and word $w \in \text{wordsDict}$:
1. If $w == \text{word1}$:
   $\text{idx}_1 \leftarrow i$
2. Else if $w == \text{word2}$:
   $\text{idx}_2 \leftarrow i$
3. If $\text{idx}_1 \ne -1$ and $\text{idx}_2 \ne -1$:
   $$
   \text{min\_dist} \leftarrow \min(\text{min\_dist}, \; |\text{idx}_1 - \text{idx}_2|)
   $$
Return $\text{min\_dist}$.

> **Invariant.** At any index $i$, $\text{min\_dist}$ is strictly equal to the minimum distance between any occurrence of `word1` and `word2` in the prefix $\text{wordsDict}[0 \dots i]$.

---

## 3. Step-by-Step Worked Execution

We trace $\text{wordsDict} = [\text{"practice"}, \text{"makes"}, \text{"perfect"}, \text{"coding"}, \text{"makes"}]$ with $\text{word1} = \text{"makes"}$ and $\text{word2} = \text{"coding"}$:
Initial state: $\text{idx}_1 = -1, \quad \text{idx}_2 = -1, \quad \text{min\_dist} = \infty$.

---

### Step 1: Index $i = 0$ ($w = \text{"practice"}$)
- Matches neither target.
- State: $\text{idx}_1 = -1, \, \text{idx}_2 = -1, \, \text{min\_dist} = \infty$.

---

### Step 2: Index $i = 1$ ($w = \text{"makes"}$)
- Matches $\text{word1}$!
- Update: $\text{idx}_1 \leftarrow 1$.
- Since $\text{idx}_2 == -1$, no complete pair exists yet.
- State: $\text{idx}_1 = 1, \, \text{idx}_2 = -1, \, \text{min\_dist} = \infty$.

---

### Step 3: Index $i = 2$ ($w = \text{"perfect"}$)
- Matches neither target.
- State unchanged.

---

### Step 4: Index $i = 3$ ($w = \text{"coding"}$)
- Matches $\text{word2}$!
- Update: $\text{idx}_2 \leftarrow 3$.
- Both targets now seen! Compute candidate distance:
  $$
  \text{dist} = |\text{idx}_1 - \text{idx}_2| = |1 - 3| = 2
  $$
- Update minimum: $\text{min\_dist} \leftarrow \min(\infty, 2) = \mathbf{2}$.
- State: $\text{idx}_1 = 1, \, \text{idx}_2 = 3, \, \text{min\_dist} = 2$.

---

### Step 5: Index $i = 4$ ($w = \text{"makes"}$)
- Matches $\text{word1}$!
- Update: $\text{idx}_1 \leftarrow 4$ (overwrites old index $1$).
- Both targets active! Compute candidate distance:
  $$
  \text{dist} = |\text{idx}_1 - \text{idx}_2| = |4 - 3| = 1
  $$
- Update minimum: $\text{min\_dist} \leftarrow \min(2, 1) = \mathbf{1}$.
- State: $\text{idx}_1 = 4, \, \text{idx}_2 = 3, \, \text{min\_dist} = 1$.

Loop terminates.
Final answer: $\mathbf{1}$.

---

## 4. Complete Execution Trace

```text
wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes", word2 = "coding"

i = 0 ("practice"): no match
i = 1 ("makes"):    idx1 = 1, idx2 = -1 -> no pair
i = 2 ("perfect"):  no match
i = 3 ("coding"):   idx1 = 1, idx2 = 3  -> dist = |1 - 3| = 2 -> min_dist = 2
i = 4 ("makes"):    idx1 = 4, idx2 = 3  -> dist = |4 - 3| = 1 -> min_dist = 1

Result: 1
```

| Index $i$ | Word $w$ | Target Match | Latest $\text{idx}_1$ (`"makes"`) | Latest $\text{idx}_2$ (`"coding"`) | Candidate $\lvert \text{idx}_1 - \text{idx}_2 \rvert$ | Best $\text{min\_dist}$ |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 0 | `"practice"` | None | -1 | -1 | - | $\infty$ |
| 1 | `"makes"` | $\text{word1}$ | **1** | -1 | - | $\infty$ |
| 2 | `"perfect"` | None | 1 | -1 | - | $\infty$ |
| **3** | **`"coding"`** | **$\text{word2}$** | **1** | **3** | **$\lvert 1 - 3 \rvert = 2$** | **2** |
| **4** | **`"makes"`** | **$\text{word1}$** | **4** | **3** | **$\lvert 4 - 3 \rvert = 1$** | **$\mathbf{1}$ (Global Min)** |

---

## 5. Algorithmic Correctness

**Soundness.** Every evaluated distance $|\text{idx}_1 - \text{idx}_2|$ corresponds to real indices where $\text{wordsDict}[\text{idx}_1] == \text{word1}$ and $\text{wordsDict}[\text{idx}_2] == \text{word2}$.

**Completeness.** Let $(i^*, j^*)$ be any global minimum pair with $j^* > i^*$. When the scan reaches $j^*$, the opposite target has already been observed at index $i^*$. The recorded index for the opposite target is either $i^*$ or an even later occurrence $i' \in (i^*, j^*)$. In either case, the recorded distance is $\le j^* - i^*$, guaranteeing that the global minimum is evaluated and preserved.

---

## 6. Traps This Instance Exposes

- **Guarantee of `word1 != word2`:** This problem guarantees `word1 != word2`. (LeetCode 245 relaxes this condition, requiring special handling when `word1 == word2`).
- **Sentinel Initialization:** Initializing $\text{idx}_1 = -1$ and $\text{idx}_2 = -1$ ensures that meaningless differences like $|-1 - 3|$ are never evaluated before both words have appeared.
- **Short-Circuit on Distance 1:** Because words are distinct and cannot share an index, the minimum possible distance is $1$. If $\text{min\_dist} == 1$, an implementation can return $1$ immediately.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot L)$, where $N$ is the number of words in `wordsDict` and $L$ is the maximum word length (up to 10 characters). Each string comparison takes $O(L)$ time, and the array is scanned exactly once. Total time is strictly $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory, using only three scalar integer variables.
