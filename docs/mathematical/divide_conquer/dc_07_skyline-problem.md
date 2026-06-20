# Formal Mathematical Specification: The Skyline Problem

## 1. Definitions and Notation

Let $\mathcal{B} = \{b_1, b_2, \dots, b_n\}$ be a set of $n$ buildings, where each building $b_i$ is defined as a triplet $(L_i, R_i, H_i) \in \mathbb{Z}^3$ such that $L_i < R_i$ and $H_i > 0$. 

The **skyline** of $\mathcal{B}$ is defined as a sequence of key points $S = \{(x_1, y_1), (x_2, y_2), \dots, (x_m, y_m)\}$ such that:
1. The points are strictly ordered by their x-coordinates: $x_1 < x_2 < \dots < x_m$.
2. The sequence represents the upper envelope of the buildings: $f(x) = \max(\{H_i \mid L_i \le x < R_i\} \cup \{0\})$.
3. For any $x \in [x_j, x_{j+1})$, $f(x) = y_j$.
4. The sequence is minimal, meaning $y_j \neq y_{j+1}$ for all $1 \le j < m$.

The domain of the input is $\mathcal{B} \subset \mathbb{Z}^3$, and the output is a sequence $S \subset \mathbb{Z}^2$.

## 2. Algebraic Characterization

The algorithm utilizes a divide-and-conquer strategy based on the principle of superposition of functions. Let $f_L(x)$ and $f_R(x)$ be the skyline functions for two disjoint subsets of buildings $\mathcal{B}_L$ and $\mathcal{B}_R$. The skyline of the union $\mathcal{B}_L \cup \mathcal{B}_R$ is given by:
$$f_{merged}(x) = \max(f_L(x), f_R(x))$$

### Recurrence Relation
The algorithm decomposes the problem into subproblems of size $n/2$. Let $T(n)$ be the time complexity for a set of $n$ buildings. The recurrence is:
$$T(n) = 2T\left(\frac{n}{2}\right) + M(n)$$
where $M(n)$ is the cost of the merge operation. Given two skylines $S_L$ and $S_R$ with lengths $|S_L| = k_1$ and $|S_R| = k_2$, the merge operation performs a linear scan of both sequences. Since the number of key points is at most $2n$, $M(n) = O(k_1 + k_2) = O(n)$.

### Loop Invariant
During the execution of the `_merge` function, let $i$ and $j$ be the indices of the current key points being processed in $S_L$ and $S_R$. Let $h_1$ and $h_2$ be the heights of the most recently processed key points from $S_L$ and $S_R$ respectively. At any iteration, the invariant holds that the height of the merged skyline at the current $x$ is:
$$H_{curr} = \max(h_1, h_2)$$
The algorithm appends $(x, H_{curr})$ to the result if and only if $H_{curr} \neq y_{last}$, where $y_{last}$ is the height of the previously added key point. This ensures the minimality of the skyline representation.

## 3. Complexity Analysis

### Time Complexity
The recurrence relation $T(n) = 2T(n/2) + O(n)$ falls under the **Master Theorem** (Case 2).
- Here, $a = 2$, $b = 2$, and $f(n) = O(n^1)$.
- Since $n^{\log_b a} = n^{\log_2 2} = n^1$, the complexity is:
$$T(n) = \Theta(n^{\log_b a} \log n) = \Theta(n \log n)$$
The work at each level of the recursion tree is $O(n)$, and there are $\log_2 n$ levels, confirming the $O(n \log n)$ upper bound.

### Space Complexity
- **Recursion Stack:** The depth of the recursion tree is $\lceil \log_2 n \rceil$, contributing $O(\log n)$ to the auxiliary space.
- **Output Storage:** Each merge step creates a new list of key points. In the worst case, the number of key points in a skyline is $2n$. Since the algorithm stores the results of subproblems, the total space complexity is dominated by the storage of the key points:
$$S(n) = 2S(n/2) + O(n) \implies S(n) = O(n)$$
Thus, the total space complexity is $O(n)$, which is optimal for storing the resulting skyline.