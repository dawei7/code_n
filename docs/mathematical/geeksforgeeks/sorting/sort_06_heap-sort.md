# Formal Mathematical Specification: Heap Sort

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be an array of $n$ elements drawn from a totally ordered set $(\mathcal{X}, \le)$. The goal of the algorithm is to produce a permutation $A'$ of $A$ such that $a'_0 \le a'_1 \le \dots \le a'_{n-1}$.

We define a **Binary Max-Heap** as a complete binary tree mapped to an array $A$ of length $n$, where for every node at index $i$ (where $0 \le i < n$), the following **Heap Property** holds:
- If $2i + 1 < n$, then $a_i \ge a_{2i+1}$ (Left child constraint).
- If $2i + 2 < n$, then $a_i \ge a_{2i+2}$ (Right child constraint).

Let $\text{sift\_down}(A, i, k)$ be a function that restores the heap property for a subtree rooted at $i$ within an array segment of length $k$, assuming the subtrees rooted at $2i+1$ and $2i+2$ already satisfy the heap property.

## 2. Algebraic Characterization

The algorithm proceeds in two distinct phases characterized by the following invariants:

### Phase 1: Build Max-Heap
We transform the arbitrary array $A$ into a Max-Heap. We define the state after the $j$-th iteration of the build process (for $j$ from $\lfloor n/2 \rfloor - 1$ down to $0$) as:
- **Invariant:** For all $k > j$, the subtree rooted at $k$ satisfies the Max-Heap property.
- **Transition:** $\text{sift\_down}(A, j, n)$ ensures the subtree rooted at $j$ satisfies the property, extending the invariant to $k \ge j$.

### Phase 2: Extract and Sort
Let $A^{(m)}$ denote the state of the array after $m$ extractions, where $0 \le m < n$. The array is partitioned into two segments: a heap $H_m = A[0 \dots n-m-1]$ and a sorted suffix $S_m = A[n-m \dots n-1]$.
- **Invariant:** 
  1. $H_m$ is a valid Max-Heap.
  2. $\forall x \in H_m, \forall y \in S_m : x \le y$.
  3. $S_m$ is sorted in non-decreasing order.
- **Transition:**
  1. Swap: $A[0] \leftrightarrow A[n-m-1]$.
  2. Restore: $\text{sift\_down}(A, 0, n-m-1)$.

## 3. Complexity Analysis

### Time Complexity
The total time complexity $T(n)$ is the sum of the time for the build phase $T_B(n)$ and the extraction phase $T_E(n)$.

**1. Build Phase:**
The cost of $\text{sift\_down}$ at height $h$ is $O(h)$. In a complete binary tree of $n$ nodes, there are at most $\lceil n/2^{h+1} \rceil$ nodes at height $h$. The total work is:
$$T_B(n) = \sum_{h=0}^{\lfloor \log n \rfloor} \left\lceil \frac{n}{2^{h+1}} \right\rceil O(h) = O\left( n \sum_{h=0}^{\infty} \frac{h}{2^h} \right)$$
Since the geometric series $\sum_{h=0}^{\infty} h x^h$ converges to $\frac{x}{(1-x)^2}$ for $|x|<1$, the summation converges to a constant. Thus, $T_B(n) = O(n)$.

**2. Extraction Phase:**
We perform $n-1$ extractions. Each extraction involves one swap ($O(1)$) and one $\text{sift\_down}$ operation on a heap of size at most $n$. The height of the heap is $\lfloor \log k \rfloor$ for a heap of size $k$.
$$T_E(n) = \sum_{k=1}^{n-1} O(\log k) = O(\log((n-1)!)) = O(n \log n)$$
Combining these, $T(n) = O(n) + O(n \log n) = O(n \log n)$.

### Space Complexity
The algorithm operates strictly in-place. It requires a constant number of auxiliary variables (pointers/indices such as `root`, `child`, `start`, `end`) regardless of the input size $n$.
$$S(n) = O(1)$$
Thus, Heap Sort is an optimal space-complexity sorting algorithm.