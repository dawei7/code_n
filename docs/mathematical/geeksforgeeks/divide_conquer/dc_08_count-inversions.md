# Formal Mathematical Specification: Count Inversions

## 1. Definitions and Notation

Let $A = \langle a_1, a_2, \dots, a_n \rangle$ be a sequence of $n$ elements drawn from a totally ordered set $(\mathcal{X}, \leq)$. 

*   **Inversion:** An inversion in $A$ is defined as an ordered pair of indices $(i, j)$ such that $1 \leq i < j \leq n$ and $a_i > a_j$.
*   **Inversion Set:** Let $\mathcal{I}(A) = \{ (i, j) \in \mathbb{Z}^2 \mid 1 \leq i < j \leq n \land a_i > a_j \}$.
*   **Inversion Count:** The objective is to compute the cardinality of the inversion set, denoted by $I(A) = |\mathcal{I}(A)|$.
*   **State Space:** The algorithm operates on the space of permutations of the input sequence, transforming $A$ into its sorted counterpart $A'$ while accumulating the count of inversions encountered during the transformation.

## 2. Algebraic Characterization

The algorithm utilizes the divide-and-conquer paradigm, relying on the property that the total number of inversions in a sequence $A$ can be decomposed based on a partition of $A$ into two subsequences $L = \langle a_1, \dots, a_m \rangle$ and $R = \langle a_{m+1}, \dots, a_n \rangle$, where $m = \lfloor n/2 \rfloor$.

The total inversion count $I(A)$ satisfies the following recurrence:
$$I(A) = I(L) + I(R) + I_{split}(L, R)$$

Where $I_{split}(L, R)$ represents the number of pairs $(i, j)$ such that $a_i \in L$ and $a_j \in R$ with $a_i > a_j$. Given that $L$ and $R$ are sorted (as a post-condition of the recursive calls), we define the counting function during the merge step. Let $L$ be indexed $1 \dots |L|$ and $R$ be indexed $1 \dots |R|$. If $L[i] > R[j]$, then because $L$ is sorted, all elements $L[k]$ for $k \geq i$ satisfy $L[k] \geq L[i] > R[j]$.

Thus, the split inversion count is:
$$I_{split}(L, R) = \sum_{j=1}^{|R|} |\{ i \in \{1, \dots, |L|\} : L[i] > R[j] \}|$$

**Loop Invariant:** At the start of each iteration of the merge process, the auxiliary array contains the sorted elements of $L[1 \dots i-1]$ and $R[1 \dots j-1]$, and the variable `count` holds the number of inversions found within the subarrays processed thus far.

## 3. Complexity Analysis

### Time Complexity
The algorithm follows the Master Theorem for divide-and-conquer recurrences. The work performed at each level of the recursion tree consists of a linear scan (the merge step) to count inversions and reorder elements.

The recurrence relation for the time complexity $T(n)$ is:
$$T(n) = 2T\left(\frac{n}{2}\right) + \Theta(n)$$

Applying the Master Theorem, where $a=2, b=2, f(n) = n^1$:
Since $n^{\log_b a} = n^{\log_2 2} = n^1$, we fall into Case 2 of the Master Theorem.
Therefore, $T(n) = \Theta(n \log n)$.

### Space Complexity
The algorithm requires auxiliary space for the merge process. At any depth $d$ of the recursion tree, the algorithm allocates temporary arrays to hold the elements of the current subarrays. 

*   **Auxiliary Space:** The merge step requires $O(n)$ space to store the merged elements before copying them back to the original array.
*   **Stack Space:** The recursion depth is $\lceil \log_2 n \rceil$. 
*   **Total Space:** Since the merge arrays are deallocated upon the return of the recursive call, the peak auxiliary space complexity is $O(n)$, dominated by the storage required for the largest merge operation at the top level of the recursion. Thus, the total space complexity is $O(n)$.