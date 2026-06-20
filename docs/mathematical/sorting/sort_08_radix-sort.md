# Formal Mathematical Specification: Radix Sort

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be an input sequence of $n$ non-negative integers, where each $a_i \in \mathbb{N}_0$. Let $b \in \mathbb{N}, b \ge 2$ denote the radix (base) of the number system. 

Any integer $a_i$ can be represented in base $b$ as a sequence of digits:
$$a_i = \sum_{j=0}^{D-1} d_{i,j} \cdot b^j$$
where $d_{i,j} = \lfloor \frac{a_i}{b^j} \rfloor \pmod b$ is the digit at position $j$, and $D = \lfloor \log_b(\max(A)) \rfloor + 1$ is the maximum number of digits required to represent the largest element in $A$.

We define a stable sorting function $f(A, j)$, which returns a permutation of $A$ such that for any two elements $a_x, a_y$ where $a_x$ appears before $a_y$ in the input, if $d_{x,j} < d_{y,j}$, then $a_x$ precedes $a_y$ in the output. If $d_{x,j} = d_{y,j}$, the relative order of $a_x$ and $a_y$ is preserved.

## 2. Algebraic Characterization

The correctness of Radix Sort relies on the principle of induction over the digit positions $j \in \{0, 1, \dots, D-1\}$.

**Loop Invariant:**
Let $A^{(k)}$ be the state of the array after $k$ passes of the algorithm (sorting by digits $0$ through $k-1$). After the $k$-th pass, the sequence $A^{(k)}$ is sorted according to the values of the $k$-length suffixes of the base-$b$ representation of the integers. Specifically, for any $a_x, a_y \in A^{(k)}$, if:
$$\sum_{j=0}^{k-1} d_{x,j} \cdot b^j < \sum_{j=0}^{k-1} d_{y,j} \cdot b^j$$
then $a_x$ precedes $a_y$ in $A^{(k)}$.

**Stability Requirement:**
The algorithm utilizes a stable counting sort as the subroutine $f(A, j)$. Stability is defined as:
$$\forall x, y \in \{0, \dots, n-1\}, x < y \land d_{x,j} = d_{y,j} \implies \text{pos}(a_x) < \text{pos}(a_y)$$
where $\text{pos}(\cdot)$ denotes the index in the output array. This ensures that the sorted order established by digits $0$ through $j-1$ is not disrupted when sorting by digit $j$.

**Termination:**
The algorithm terminates when $k = D$. At this state, the condition becomes:
$$\sum_{j=0}^{D-1} d_{x,j} \cdot b^j < \sum_{j=0}^{D-1} d_{y,j} \cdot b^j \iff a_x < a_y$$
Thus, $A^{(D)}$ is sorted in non-decreasing order.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs $D$ passes. In each pass, we perform a Counting Sort. The Counting Sort subroutine consists of:
1. Frequency counting: $\sum_{i=0}^{n-1} 1 = O(n)$.
2. Prefix sum calculation: $\sum_{i=0}^{b-1} 1 = O(b)$.
3. Output array construction: $\sum_{i=0}^{n-1} 1 = O(n)$.

The total time complexity $T(n, D, b)$ is the sum of the work across all $D$ passes:
$$T(n, D, b) = \sum_{j=0}^{D-1} O(n + b) = O(D \cdot (n + b))$$
Given $K = b$, we obtain the standard form $O(D(n + K))$. In the case where $b$ is chosen such that $b \approx n$, the complexity is $O(D \cdot n)$.

### Space Complexity
The algorithm requires auxiliary space for:
1. The `counts` array of size $b$ (or $K$).
2. The `output` array of size $n$.

The total auxiliary space complexity $S(n, K)$ is:
$$S(n, K) = O(n + K)$$
This space is reused in each of the $D$ iterations, thus the total space complexity remains $O(n + K)$.