# Formal Mathematical Specification: Merge Sort

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be a sequence of elements drawn from a totally ordered set $(\mathcal{X}, \le)$. The objective of the Merge Sort algorithm is to produce a permutation $A' = [a'_0, a'_1, \dots, a'_{n-1}]$ of $A$ such that $a'_i \le a'_{i+1}$ for all $0 \le i < n-1$.

We define the following domains and operators:
*   **Sequence Space:** Let $\mathcal{S}$ be the set of all finite sequences over $\mathcal{X}$.
*   **Concatenation:** For $S_1, S_2 \in \mathcal{S}$, $S_1 \oplus S_2$ denotes the concatenation of sequences.
*   **Sub-sequence:** For $0 \le i \le j < |S|$, $S[i:j]$ denotes the subsequence of $S$ from index $i$ to $j-1$.
*   **Merge Operator:** Define a function $\text{merge}: \mathcal{S} \times \mathcal{S} \to \mathcal{S}$ such that for two sorted sequences $L$ and $R$, $\text{merge}(L, R)$ returns a sorted sequence $M$ containing all elements of $L \cup R$ (multiset union).

## 2. Algebraic Characterization

The algorithm is defined by the recursive function $f: \mathcal{S} \to \mathcal{S}$:

$$
f(A) = 
\begin{cases} 
A & \text{if } |A| \le 1 \\
\text{merge}(f(A[0 : \lfloor n/2 \rfloor]), f(A[\lfloor n/2 \rfloor : n])) & \text{if } |A| > 1 
\end{cases}
$$

### The Merge Invariant
The correctness of the $\text{merge}(L, R)$ operation relies on the following invariant. Let $L = [l_1, \dots, l_p]$ and $R = [r_1, \dots, r_q]$ be sorted. At any step $k$ of the merge process, let $M_k$ be the sequence constructed so far, and $L_i, R_j$ be the remaining suffixes of $L$ and $R$. The invariant holds:
1. $M_k$ is sorted.
2. $\forall x \in M_k, \forall y \in (L_i \cup R_j), x \le y$.
3. $M_k \cup L_i \cup R_j = L \cup R$.

Upon termination, $L_i = \emptyset$ and $R_j = \emptyset$, implying $M_k$ is a sorted permutation of the original input.

## 3. Complexity Analysis

### Time Complexity
The time complexity $T(n)$ is governed by the Master Theorem for divide-and-conquer recurrences. Given an array of size $n$:
1. The division step takes $O(1)$ time.
2. The recursive calls consist of two sub-problems of size $n/2$.
3. The merge operation performs at most $n-1$ comparisons, yielding $O(n)$ work.

The recurrence relation is:
$$T(n) = 2T\left(\frac{n}{2}\right) + \Theta(n)$$

Applying the Master Theorem where $a=2, b=2, f(n)=n$:
Since $n^{\log_b a} = n^{\log_2 2} = n^1$, and $f(n) = \Theta(n^1)$, we fall into Case 2 of the Master Theorem. Thus:
$$T(n) = \Theta(n \log n)$$

### Space Complexity
The space complexity is determined by the auxiliary storage required during the merge phase and the recursion stack.

1. **Auxiliary Array:** At each level of the recursion, we allocate temporary space to store the merged results. While the total space across all recursive calls could be $O(n \log n)$ if not managed carefully, the standard implementation reuses memory or releases it such that the maximum auxiliary space required at any point in time is $O(n)$.
2. **Recursion Stack:** The depth of the recursion tree is $\lceil \log_2 n \rceil$. Each stack frame consumes $O(1)$ space, leading to $O(\log n)$ stack space.

Total space complexity is dominated by the auxiliary array:
$$S(n) = O(n) + O(\log n) = O(n)$$