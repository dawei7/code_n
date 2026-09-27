# Guided Example: Top K Frequent Elements

We trace the step-by-step frequency map generation (`Counter(nums)`), heap-based top-$k$ selection (`cnt.most_common(k)` / `heapq.nlargest`), bucket-sort frequency aggregation, and result extraction on representative integer arrays:

- **Input:** $\text{nums} = [1, 1, 1, 2, 2, 3], \quad k = 2$
- **Required output:** $[1, 2]$
  - Frequency distribution:
    - Element $1$: occurs $3$ times
    - Element $2$: occurs $2$ times
    - Element $3$: occurs $1$ time
  - Top $k = 2$ most frequent elements: $1$ (count 3) and $2$ (count 2)
  - Output: $[1, 2]$ (or $[2, 1]$ in any order)
- **Single Element Array:** $\text{nums} = [1], k = 1 \implies [1]$
- **Negative Integer Elements:** $\text{nums} = [-1, -1, 2], k = 1 \implies [-1]$
- **All Elements Distinct:** $\text{nums} = [4, 5, 6], k = 2 \implies$ any two elements

This instance demonstrates frequency ranking algorithms, contrasts full sorting ($O(U \log U)$), heap selection ($O(U \log K)$), and bucket sort ($O(N)$), proves why hash-based frequency aggregation avoids quadratic element scans, and analyzes time and space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums} = [1, 1, 1, 2, 2, 3]$ ($N = 6$) and an integer $k = 2$:
Return the $k$ most frequent elements in $\text{nums}$ in any order:

```text
Array: [1, 1, 1, 2, 2, 3]

Frequencies Counted:
1 -> 3 times  (Rank 1)
2 -> 2 times  (Rank 2)
3 -> 1 time   (Rank 3)

Top k = 2 Elements: [1, 2]
```

### The $O(N \log N)$ Full-Sort vs $O(N)$ Linear Goal
- Sorting the distinct elements by frequency costs $O(U \log U)$ time, where $U$ is the number of unique elements ($U \le N$).
- Standard library `Counter.most_common(k)` uses `heapq.nlargest`, maintaining a min-heap of size $k$ in $O(N + U \log k)$ time.
- Alternatively, **Bucket Sort** groups numbers by frequency into $N + 1$ buckets, allowing a linear scan from frequency $N$ down to 1 in strictly $O(N)$ time.

---

## 2. Conceptual Foundation & Invariants

### 1. Hash Map Frequency Counting
Count occurrences of each unique element $x \in \text{nums}$:
$$
cnt = \text{Counter}(\text{nums})
$$
Mapping for our instance:
$$
cnt = \{1: 3, \; 2: 2, \; 3: 1\}
$$

### 2. Selection via `cnt.most_common(k)`
- Evaluates the top $k$ items with the highest frequency values.
- Returns list of pairs `[(val_1, freq_1), ..., (val_k, freq_k)]` sorted in descending frequency order:
  $$
  \text{most\_common}(2) = [(1, 3), \; (2, 2)]
  $$
- Unpack values discarding frequencies:
  $$
  [x \text{ for } x, \_ \text{ in } cnt.\text{most\_common}(k)]
  $$

### 3. Linear-Time Bucket Sort Alternative
- Create $N + 1$ empty bucket lists $\text{buckets}[0 \dots N]$.
- For each $(val, freq) \in cnt.\text{items}()$: append $val$ to $\text{buckets}[freq]$.
- Iterate $f$ backwards from $N$ down to $1$, collecting elements until $k$ elements are gathered.

> **Invariant.** The returned list contains precisely the $k$ distinct keys from `nums` with the greatest associated frequency counts.

---

## 3. Step-by-Step Worked Execution

We trace $\text{nums} = [1, 1, 1, 2, 2, 3]$ with $k = 2$:

---

### Step 1: Count Frequencies
Scan `nums` from left to right:
1. $x = 1 \implies cnt[1] = 1$
2. $x = 1 \implies cnt[1] = 2$
3. $x = 1 \implies cnt[1] = 3$
4. $x = 2 \implies cnt[2] = 1$
5. $x = 2 \implies cnt[2] = 2$
6. $x = 3 \implies cnt[3] = 1$
Resulting dictionary:
$$
cnt = \{1: 3, \; 2: 2, \; 3: 1\}
$$
Number of unique elements: $U = 3$.

---

### Step 2: Rank Frequencies (Top $k = 2$)
Using a min-heap of capacity $k = 2$ over the $(count, element)$ pairs:
- Insert $(3, 1)$: heap has $[(3, 1)]$.
- Insert $(2, 2)$: heap has $[(2, 2), (3, 1)]$.
- Compare $(1, 3)$ with heap minimum $(2, 2)$: $1 < 2$, rejected!
Extracted pairs with largest frequencies:
$$
[(1, 3), \; (2, 2)]
$$

---

### Step 3: Extract Element Values
List comprehension extracts the element keys:
$$
[x \text{ for } x, \_ \text{ in } [(1, 3), (2, 2)]] = \mathbf{[1, 2]}
$$

---

## 4. Complete Execution Trace

```text
nums = [1, 1, 1, 2, 2, 3], k = 2

1. Frequency Map:
   cnt = {1: 3, 2: 2, 3: 1}

2. Selection (k = 2):
   Rank 1: Element 1 (count 3)
   Rank 2: Element 2 (count 2)
   Rank 3: Element 3 (count 1) [Excluded]

3. Output Extraction:
   [1, 2]
```

| Element $x$ | Frequency Count | Rank in Descending Frequency | In Top $k = 2$? | Included in Output? |
|:---:|:---:|:---:|:---:|:---:|
| **1** | **3** | **1** | **Yes** | **Yes (`1`)** |
| **2** | **2** | **2** | **Yes** | **Yes (`2`)** |
| 3 | 1 | 3 | No | No |

---

## 5. Algorithmic Correctness

**Soundness.** Frequency mapping accurately tallies the exact multiplicity of every distinct integer in `nums`. The extraction `most_common(k)` selects the $k$ elements corresponding to the highest frequencies. Since no two elements with lower frequencies can surpass those selected, the resulting set is strictly the $k$ most frequent elements.

**Completeness.** The input problem guarantees that a unique top-$k$ set exists (or any valid order is accepted if tied). Because every distinct element is tallied in $cnt$ and considered during heap selection, no high-frequency element is missed.

---

## 6. Traps This Instance Exposes

- **Full Array Sorting:** Sorting the entire input array `nums` of length $N$ takes $O(N \log N)$ time, which violates the requirement for better than $O(N \log N)$ when $N$ is large.
- **Negative Integer Keys:** In arrays with negative values (e.g. $[-1, -1, 2]$), direct array indexing fails. Hash map counting seamlessly handles negative keys without offset shifts.
- **Tied Frequencies:** When multiple elements share the same frequency, any choice among the tied elements that fulfills size $k$ is acceptable per problem specifications.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N + U \log k)$, where $N$ is the number of elements in `nums`, and $U$ is the number of unique elements ($U \le N$).
  - Counting elements in `Counter(nums)` takes $O(N)$ time.
  - `most_common(k)` executes `heapq.nlargest`, processing $U$ elements with a heap of size $k$ in $O(U \log k)$ time.
  - When implemented with bucket sort, runtime is strictly $O(N)$ linear time.
- **Auxiliary Space Complexity:** $O(U)$ auxiliary memory to store unique elements and their counts in the frequency hash map.
