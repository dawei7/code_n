# Guided Example: Subsets

We trace the step-by-step generation of the power set on a representative distinct-integer instance using both iterative cascading and binary bitmask generation:

- **Input:** $\text{nums} = [1, 2, 3]$
- **Required output:** $[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]$

This instance demonstrates generating all $2^N$ subsets (the power set), iterative doubling / cascading accumulation, mapping subset generation to binary bitmasks ($0 \dots 2^N - 1$), and recursive include/exclude decision trees.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums} = [1, 2, 3]$ of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets.

For an array of $N = 3$ elements, every element can independently be either included or excluded.
The cardinality of the power set is strictly:
$$
|\mathcal{P}(\text{nums})| = 2^N = 2^3 = 8
$$

A naive recursive approach risks complex bookkeeping.
We explore two elegant, deterministic paradigms:
1. **Iterative Cascading:** Start with the empty subset `[[]]`. For each number $x$, duplicate all existing subsets and append $x$ to each duplicate.
2. **Binary Bitmask Enumeration:** Map each integer $m \in [0, 2^N - 1]$ to a subset by inspecting its binary representation.

---

## 2. Conceptual Foundation & Invariants

### Method 1: Iterative Cascading
Start with `subsets = [[]]`.
For each element $x \in \text{nums}$:
$$
\text{new\_subsets} = [s + [x] \text{ for } s \text{ in subsets}]
$$
$$
\text{subsets} \leftarrow \text{subsets} + \text{new\_subsets}
$$
The size of `subsets` doubles with each element: $1 \to 2 \to 4 \to 8$.

### Method 2: Binary Bitmask Enumeration
Since there are $N$ elements, there are $2^N$ possible combinations of presence/absence.
Each integer $m \in [0, 2^N - 1]$ written in binary has $N$ bits:
- If bit $j$ of $m$ is $1$ (`(m >> j) & 1 == 1`), include $\text{nums}[j]$.
- If bit $j$ is $0$, exclude $\text{nums}[j]$.

> **Invariant.** Every integer mask $m \in [0, 2^N - 1]$ corresponds to a unique, non-overlapping subset of $\text{nums}$, guaranteeing zero duplicates and complete coverage.

---

## 3. Step-by-Step Worked Execution

### Method 1: Iterative Cascading Trace on $[1, 2, 3]$

- **Base State:**
  - $\text{subsets} = [[]]$ (Size 1).
- **Process Element $x = 1$:**
  - Existing subsets: `[[]]`.
  - Append $1$ to each: `[[1]]`.
  - Combined: $[[], [1]]$ (Size 2).
- **Process Element $x = 2$:**
  - Existing subsets: `[[], [1]]`.
  - Append $2$ to each: `[[2], [1, 2]]`.
  - Combined: $[[], [1], [2], [1, 2]]$ (Size 4).
- **Process Element $x = 3$:**
  - Existing subsets: `[[], [1], [2], [1, 2]]`.
  - Append $3$ to each: `[[3], [1, 3], [2, 3], [1, 2, 3]]`.
  - Combined: $[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]$ (Size 8).

All 8 subsets generated.

---

### Method 2: Bitmask Enumeration Trace ($0 \dots 7$)

| Integer Mask $m$ | 3-Bit Binary $(b_2 b_1 b_0)_2$ | Bit 0 ($1$) | Bit 1 ($2$) | Bit 2 ($3$) | Synthesized Subset |
|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | `000` | 0 | 0 | 0 | `[]` |
| 1 | `001` | 1 | 0 | 0 | `[1]` |
| 2 | `010` | 0 | 1 | 0 | `[2]` |
| 3 | `011` | 1 | 1 | 0 | `[1, 2]` |
| 4 | `100` | 0 | 0 | 1 | `[3]` |
| 5 | `101` | 1 | 0 | 1 | `[1, 3]` |
| 6 | `110` | 0 | 1 | 1 | `[2, 3]` |
| 7 | `111` | 1 | 1 | 1 | `[1, 2, 3]` |

---

## 4. Complete Execution Trace

### Cascading Evolution Table

| Iteration Step | Number Incorporated | Pre-existing Subsets Count | Newly Created Subsets | Total Subsets Accumulated |
|:---:|:---:|:---:|:---|:---:|
| 0 | Base | 0 | `[[]]` | 1 |
| 1 | $1$ | 1 | `[[1]]` | 2 |
| 2 | $2$ | 2 | `[[2], [1, 2]]` | 4 |
| 3 | $3$ | 4 | `[[3], [1, 3], [2, 3], [1, 2, 3]]` | **8 (Full Power Set)** |

---

## 5. Algorithmic Correctness

**Soundness.** Let $\text{nums}$ have distinct elements. By induction on $k$, the subsets of $\text{nums}[0 \dots k-1]$ are formed by the subsets of $\text{nums}[0 \dots k-2]$ without $\text{nums}[k-1]$, plus the subsets of $\text{nums}[0 \dots k-2]$ with $\text{nums}[k-1]$ appended. Since the two groups are disjoint, no subset can appear twice.

**Completeness.** There are $2^N$ distinct subsets of an $N$-element set. The iterative process doubles the list size at each of the $N$ steps, terminating with exactly $2^N$ unique subsets.

---

## 6. Traps This Instance Exposes

- **Modifying the List While Iterating Over It:** In Python, doing `for s in subsets: subsets.append(...)` causes an infinite loop because `subsets` grows during iteration. Iterating over a snapshot `for s in subsets[:]` or using list comprehension `[s + [x] for s in subsets]` avoids this.
- **Empty Array Handling:** If $\text{nums} = []$, $2^0 = 1$, and the algorithm correctly returns $[[]]$ (the power set of the empty set contains the empty set).
- **Subsets with Duplicates (Subsets II):** If $\text{nums}$ contains duplicate numbers (e.g. $[1, 2, 2]$), ordinary cascading generates duplicate subsets. Sorting and only branching duplicate elements on subsets created in the immediately preceding iteration resolves duplicates (LeetCode 90).

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot 2^N)$. There are $2^N$ total subsets, and each subset has an average length of $N / 2$. Copying them into memory takes $O(N \cdot 2^N)$ operations.
- **Auxiliary Space Complexity:** $O(N \cdot 2^N)$ to store the output subsets list.
