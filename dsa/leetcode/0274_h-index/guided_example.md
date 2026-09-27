# Guided Example: H-Index

We trace the step-by-step descending rank comparison, citation threshold monotonicity, and bucket counting aggregation on representative publication citation arrays:

- **Input:** $\text{citations} = [3, 0, 6, 1, 5]$
- **Required output:** $3$ (Researcher has 3 papers with at least 3 citations: papers cited 6, 5, and 3 times; the 4th paper has only 1 citation)
- **Low Citation Instance:** $\text{citations} = [1, 3, 1] \implies 1$ (Only 1 paper has $\ge 2$ citations; maximum $h = 1$)
- **Zero Citations Instance:** $\text{citations} = [0, 0, 0] \implies 0$ (No papers meet threshold 1)
- **Single Highly-Cited Paper:** $\text{citations} = [100] \implies 1$ ($h \le N$; bounded by total number of papers)
- **All Papers Uniformly Cited:** $\text{citations} = [4, 4, 4, 4] \implies 4$ ($4$ papers cited at least $4$ times)

This instance demonstrates metric ranking invariants, explains why a researcher with $N$ papers can never have an $h$-index greater than $N$, proves the equivalence between sorted rank index tests ($\text{citations}[i] \ge i + 1$) and cumulative bucket counting, and compares the $O(N \log N)$ sorting approach with the $O(N)$ bucket sort alternative.

---

## 1. Instance & Teaching Goal

Given citation counts $\text{citations} = [3, 0, 6, 1, 5]$ for $N = 5$ papers:
Find the **$h$-index**, defined as the maximum value $h$ such that at least $h$ papers have each received at least $h$ citations.

```text
Sorted in descending order:
Rank 1: 6 citations >= 1 (Qualifies)
Rank 2: 5 citations >= 2 (Qualifies)
Rank 3: 3 citations >= 3 (Qualifies)
Rank 4: 1 citation  >= 4 (Fails: 1 < 4)
Rank 5: 0 citations >= 5 (Fails: 0 < 5)

Maximum qualifying h = 3
```

### The Dual Role of Parameter $h$
In the condition "at least $h$ papers have at least $h$ citations":
- The first $h$ is a **paper count** (cardinality).
- The second $h$ is a **citation threshold** (intensity).
Since the total number of authored papers is $N$, the researcher has at most $N$ papers, so:
$$
0 \le h \le N
$$
Even if a author has 1 paper with 1,000,000 citations, their $h$-index is strictly $1$.

---

## 2. Conceptual Foundation & Invariants

### Method 1: Descending Sort Rank Comparison
Sort $\text{citations}$ in non-increasing order:
$$
c_0 \ge c_1 \ge c_2 \ge \dots \ge c_{N-1}
$$
At zero-based index $i$, the paper at rank $i + 1$ has citation count $c_i$.
Because earlier papers have even more citations ($c_0 \ge \dots \ge c_i$):
- If $c_i \ge i + 1$:
  At least $i + 1$ papers have at least $i + 1$ citations. The rank $i + 1$ is achievable!
- If $c_i < i + 1$:
  Paper $i$ (and all subsequent papers) have fewer than $i + 1$ citations. Rank $i + 1$ is impossible!
The maximum valid $h$ is the number of indices where $c_i \ge i + 1$.

### Method 2: $O(N)$ Bucket Counting Sort
Since $h \le N$, citations $> N$ are equivalent to $N$ for the purpose of reaching threshold $N$:
1. Create bucket array `count` of size $N + 1$.
2. For each citation $c \in \text{citations}$:
   $$
   \text{bucket}[\min(c, N)] \leftarrow \text{bucket}[\min(c, N)] + 1
   $$
3. Accumulate qualifying papers backwards from $h = N$ down to $0$:
   $$
   \text{total\_papers} \leftarrow \text{total\_papers} + \text{bucket}[h]
   $$
   If $\text{total\_papers} \ge h$:
   $$
   \text{return } h
   $$

> **Invariant.** If rank $h$ satisfies the condition (at least $h$ papers cited $\ge h$ times), all smaller thresholds $h' < h$ are also satisfied. The transition from feasible to infeasible is strictly monotonic.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{citations} = [3, 0, 6, 1, 5]$ ($N = 5$):

### Execution via Descending Sort
Sort descending:
$$
\text{citations} = [6, 5, 3, 1, 0]
$$

- **Rank 1 ($i = 0$, Threshold $h = 1$):**
  - Paper citation: $c_0 = 6$.
  - Comparison: $6 \ge 1$ (**True**).
  - Feasible $h \ge 1$.

- **Rank 2 ($i = 1$, Threshold $h = 2$):**
  - Paper citation: $c_1 = 5$.
  - Comparison: $5 \ge 2$ (**True**).
  - Feasible $h \ge 2$.

- **Rank 3 ($i = 2$, Threshold $h = 3$):**
  - Paper citation: $c_2 = 3$.
  - Comparison: $3 \ge 3$ (**True**).
  - Feasible $h \ge 3$.

- **Rank 4 ($i = 3$, Threshold $h = 4$):**
  - Paper citation: $c_3 = 1$.
  - Comparison: $1 \ge 4$ (**False**; $1 < 4$).
  - Infeasible! Monotonicity guarantees no higher rank can succeed.

Maximum valid $h = \mathbf{3}$.

---

### Execution via $O(N)$ Bucket Sort
Array length $N = 5$. Buckets $[0, 1, 2, 3, 4, 5]$:
- $3 \implies \text{bucket}[3] \mathrel{+}= 1$
- $0 \implies \text{bucket}[0] \mathrel{+}= 1$
- $6 \implies \min(6, 5) = 5 \implies \text{bucket}[5] \mathrel{+}= 1$
- $1 \implies \text{bucket}[1] \mathrel{+}= 1$
- $5 \implies \min(5, 5) = 5 \implies \text{bucket}[5] \mathrel{+}= 1$

Bucket array:
$$
\text{bucket} = [1, 1, 0, 1, 0, 2]
$$

Scan from $h = 5$ down to $0$:
- $h = 5$: $\text{total} = 0 + \text{bucket}[5] = 2$. Check $2 \ge 5$ (False).
- $h = 4$: $\text{total} = 2 + \text{bucket}[4] = 2 + 0 = 2$. Check $2 \ge 4$ (False).
- $h = 3$: $\text{total} = 2 + \text{bucket}[3] = 2 + 1 = 3$. Check $3 \ge 3$ (**True!**).

Found maximum $h = \mathbf{3}$.

---

## 4. Complete Execution Trace

```text
citations = [3, 0, 6, 1, 5] -> sorted: [6, 5, 3, 1, 0]

i = 0: c[0] = 6 >= 1 -> Valid
i = 1: c[1] = 5 >= 2 -> Valid
i = 2: c[2] = 3 >= 3 -> Valid
i = 3: c[3] = 1 < 4  -> Violated! Stop

Result: 3
```

| Rank ($i + 1$) | Sorted Citations ($c_i$) | Required Threshold ($h$) | Comparison ($c_i \ge h$) | Feasible? | Current Candidate $h$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 6 | 1 | $6 \ge 1$ | Yes | 1 |
| 2 | 5 | 2 | $5 \ge 2$ | Yes | 2 |
| **3** | **3** | **3** | **$3 \ge 3$** | **Yes** | **3** |
| 4 | 1 | 4 | $1 \ge 4$ | **No ($1 < 4$)** | Fails |
| 5 | 0 | 5 | $0 \ge 5$ | No | Fails |
| **End** | - | - | - | - | **$\mathbf{3}$ (Final H-Index)** |

---

## 5. Algorithmic Correctness

**Soundness.** If $c_{h-1} \ge h$, then because the array is sorted descending, all previous entries $c_0, c_1, \dots, c_{h-1}$ are $\ge c_{h-1} \ge h$. Thus, there are at least $h$ papers with at least $h$ citations.

**Completeness.** If $c_h < h + 1$, then paper $h$ and all subsequent papers have $< h + 1$ citations. The total number of papers with $\ge h + 1$ citations is at most $h$, which is strictly less than $h + 1$. Thus, no threshold larger than $h$ can be satisfied, guaranteeing that $h$ is maximal.

---

## 6. Traps This Instance Exposes

- **Exceeding $N$ Citations:** Having paper citations of $1,000$ does not mean $h$ can be $1,000$. The $h$-index is bounded by the total number of papers ($h \le N$).
- **All Zeros:** When `citations = [0, 0, 0]`, paper 0 has $0 < 1$. The loop terminates immediately, returning $0$.
- **Off-by-One in 0-Indexed Arrays:** At index $i$, the number of papers evaluated is $i + 1$. The comparison must test `citations[i] >= i + 1`, not `citations[i] >= i`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - **Sorting Approach:** $O(N \log N)$ to sort the array, followed by an $O(N)$ linear scan. Total time is $O(N \log N)$.
  - **Bucket Counting Approach:** $O(N)$ to populate buckets of size $N + 1$, followed by an $O(N)$ reverse linear scan. Total time is strictly $O(N)$.
- **Auxiliary Space Complexity:**
  - $O(1)$ auxiliary space for in-place sorting.
  - $O(N)$ auxiliary space for the bucket count array.
