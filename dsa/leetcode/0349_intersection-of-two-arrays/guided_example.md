# Guided Example: Intersection of Two Arrays

We trace the step-by-step hash set construction (`set(nums1)`, `set(nums2)`), duplicate element deduplication, mathematical set intersection ($S_1 \cap S_2$), and unique common element collection on representative integer array instances:

- **Input:** $\text{nums1} = [1, 2, 2, 1], \quad \text{nums2} = [2, 2]$
- **Required output:** $[2]$
  - Unique elements in $\text{nums1}$: $\{1, 2\}$
  - Unique elements in $\text{nums2}$: $\{2\}$
  - Set intersection: $\{1, 2\} \cap \{2\} = \{2\}$
  - Converted output list: $[2]$
- **Multi-Element Disjoint Instance:** $\text{nums1} = [4, 9, 5], \text{nums2} = [9, 4, 9, 8, 4]$
  - Set 1: $\{4, 5, 9\}$, Set 2: $\{4, 8, 9\}$
  - Intersection: $\{4, 9\}$ (Any order: `[4, 9]` or `[9, 4]`)
- **Completely Disjoint Arrays:** $\text{nums1} = [1, 2, 3], \text{nums2} = [4, 5, 6] \implies []$
- **Subset Relationship:** $\text{nums1} = [1, 2], \text{nums2} = [1, 2, 3] \implies [1, 2]$

This instance demonstrates set-theoretic intersections on finite multisets, proves why hash set deduplication eliminates duplicate checking overhead, contrasts $O(N + M)$ linear hashing with $O(N \cdot M)$ pairwise nested comparisons, and analyzes $O(N + M)$ memory bounds.

---

## 1. Instance & Teaching Goal

Given two integer arrays:
$$
\text{nums1} = [1, 2, 2, 1], \quad \text{nums2} = [2, 2]
$$
Return an array of their intersection such that:
1. Each element in the result is **unique** (no duplicates).
2. Elements may be returned in **any order**.

```text
nums1: [1, 2, 2, 1] -> Distinct Elements: {1, 2}
nums2: [2, 2]       -> Distinct Elements: {2}

Mathematical Intersection:
{1, 2} ∩ {2} = {2}

Output: [2]
```

### Why Naive Pairwise Comparison ($O(N \times M)$) Fails
- Comparing each element of `nums1` against all elements of `nums2` takes $O(N \times M)$ time.
- Collecting matches directly creates duplicate entries (e.g. four pairings of `2` with `2`), requiring an extra deduplication step.
- Hashing both inputs into hash sets reduces conversion and intersection to strictly **$O(N + M)$ linear time**.

---

## 2. Conceptual Foundation & Invariants

### 1. Hash Set Conversion
Convert both arrays to hash sets to deduplicate and enable $O(1)$ average-time membership testing:
$$
S_1 = \text{set}(\text{nums1}) = \{1, 2\}
$$
$$
S_2 = \text{set}(\text{nums2}) = \{2\}
$$

### 2. Set Bitwise Intersection (`&`)
In Python, `S_1 & S_2` evaluates the mathematical intersection:
$$
S_{\cap} = S_1 \cap S_2 = \{x \mid x \in S_1 \land x \in S_2\}
$$
Iterates over the smaller set and queries membership in the larger set in $O(\min(|S_1|, |S_2|))$ operations.

### 3. List Conversion
Transform the resulting set into a list:
$$
\text{list}(S_{\cap})
$$

> **Invariant.** An integer $x$ belongs to the result list if and only if $x \in \text{nums1}$ and $x \in \text{nums2}$. By definition of a set, every element appears at most once.

---

## 3. Step-by-Step Worked Execution

We trace the evaluation on $\text{nums1} = [1, 2, 2, 1]$ and $\text{nums2} = [2, 2]$:

---

### Step 1: Deduplicate `nums1` into $S_1$
Scan `nums1 = [1, 2, 2, 1]`:
- Element $1 \implies \text{add } 1$ to $S_1$.
- Element $2 \implies \text{add } 2$ to $S_1$.
- Element $2 \implies$ duplicate, already present.
- Element $1 \implies$ duplicate, already present.
$$
S_1 = \{1, 2\}
$$

---

### Step 2: Deduplicate `nums2` into $S_2$
Scan `nums2 = [2, 2]`:
- Element $2 \implies \text{add } 2$ to $S_2$.
- Element $2 \implies$ duplicate, already present.
$$
S_2 = \{2\}
$$

---

### Step 3: Compute Set Intersection $S_1 \ \& \ S_2$
Evaluate membership across sets:
- Test element $2 \in S_2$: Is $2 \in S_1$? **Yes!** Include $2$.
Intersection set:
$$
S_1 \cap S_2 = \{\mathbf{2}\}
$$

---

### Step 4: Convert to Output List
$$
\text{list}(\{2\}) = \mathbf{[2]}
$$

---

## 4. Complete Execution Trace

```text
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

1. set(nums1) = {1, 2}
2. set(nums2) = {2}
3. set(nums1) & set(nums2) = {2}
4. list({2}) = [2]

Result: [2]
```

| Distinct Candidate | Present in `nums1` ($S_1$)? | Present in `nums2` ($S_2$)? | In Intersection ($S_1 \cap S_2$)? | Emitted to Output? |
|:---:|:---:|:---:|:---:|:---:|
| 1 | Yes | No | No | No |
| **2** | **Yes** | **Yes** | **Yes** | **Yes (`2`)** |

---

## 5. Algorithmic Correctness

**Soundness.** Every element in $S_1 \ \& \ S_2$ is confirmed to be present in both $S_1$ and $S_2$. Because $S_1$ and $S_2$ were constructed directly from the inputs, any emitted number exists in both `nums1` and `nums2`. Since sets cannot store duplicate elements, every value in the returned list is unique.

**Completeness.** If an integer $x$ exists in both `nums1` and `nums2`, it is inserted into both $S_1$ and $S_2$. The set intersection operator `&` evaluates all shared members without omitting any common values. Thus, all intersecting numbers are included.

---

## 6. Traps This Instance Exposes

- **Preserving Duplicates (LeetCode 350 Contrast):** Problem 349 requires strictly unique values in the output (`[2]`). Problem 350 (Intersection of Two Arrays II) requires preserving element multiplicities (`[2, 2]`). Using sets naturally enforces uniqueness for Problem 349.
- **Unordered Output Freedom:** The problem allows returning the answer in any order. Relying on array insertion order or sorting is unnecessary and adds overhead.
- **Empty Output Case:** When the two arrays share no common elements, $S_1 \cap S_2 = \emptyset$, correctly yielding `[]`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N + M)$, where $N = \text{len}(nums1)$ and $M = \text{len}(nums2)$.
  - Constructing $S_1$ takes $O(N)$ time.
  - Constructing $S_2$ takes $O(M)$ time.
  - Computing $S_1 \ \& \ S_2$ takes $O(\min(|S_1|, |S_2|))$ average time.
  - Total runtime is strictly linear $O(N + M)$.
- **Auxiliary Space Complexity:** $O(N + M)$ auxiliary memory to store hash sets $S_1$ and $S_2$.
