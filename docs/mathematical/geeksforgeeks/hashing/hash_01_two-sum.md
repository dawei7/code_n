# Formal Mathematical Specification: Two Sum

## 1. Definitions and Notation

Let $A = (a_0, a_1, \dots, a_{n-1})$ be a sequence of integers of length $n \in \mathbb{N}$, where $a_i \in \mathbb{Z}$ for all $i \in \{0, 1, \dots, n-1\}$. Let $T \in \mathbb{Z}$ denote the target sum.

We define the solution set $\mathcal{S}$ as the set of index pairs $(i, j)$ such that:
$$\mathcal{S} = \{ (i, j) \in \mathbb{N}^2 \mid 0 \le i < j < n \land a_i + a_j = T \}$$

The problem guarantees the existence of a unique solution, such that $|\mathcal{S}| = 1$. Let $(i^*, j^*)$ be the unique element of $\mathcal{S}$.

We define a partial mapping $M_k: \mathbb{Z} \to \{0, 1, \dots, k-1\}$ representing the state of the hash map after $k$ iterations of the algorithm, where $M_k(v) = i$ if $a_i = v$ and $i < k$. If no such $i$ exists, $M_k(v)$ is undefined.

## 2. Algebraic Characterization

The algorithm proceeds by iterating through the index $k \in \{0, \dots, n-1\}$. At each step $k$, we define the complement $c_k = T - a_k$. The algorithm maintains the following loop invariant:

**Invariant:** At the start of iteration $k$, the map $M_k$ contains all elements $\{a_0, a_1, \dots, a_{k-1}\}$ such that for any $v \in \{a_0, \dots, a_{k-1}\}$, $M_k(v) = \max \{i \mid a_i = v, i < k\}$.

The transition function for the state $M$ is defined as:
$$M_{k+1}(v) = 
\begin{cases} 
k & \text{if } v = a_k \\
M_k(v) & \text{otherwise}
\end{cases}$$

The algorithm terminates at the smallest index $j^*$ such that there exists an $i^* < j^*$ satisfying $a_{i^*} + a_{j^*} = T$. Formally, the algorithm returns $(i^*, j^*)$ where:
$$j^* = \min \{ k \in \{0, \dots, n-1\} \mid (T - a_k) \in \text{dom}(M_k) \}$$
$$i^* = M_{j^*}(T - a_{j^*})$$

Since the problem guarantees a unique solution, the existence of $j^*$ is guaranteed by the existence of $(i^*, j^*) \in \mathcal{S}$.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs a single pass over the input array $A$. For each index $k \in \{0, \dots, n-1\}$, the algorithm performs:
1. A subtraction: $T - a_k$ (constant time, $O(1)$).
2. A hash map lookup: $M_k(c_k)$ (expected $O(1)$).
3. A conditional insertion: $M_{k+1}(a_k) \leftarrow k$ (expected $O(1)$).

The total time complexity $T(n)$ is given by the summation:
$$T(n) = \sum_{k=0}^{j^*} O(1) = O(j^*) \subseteq O(n)$$
In the worst case, where the solution pair is at the end of the array, $j^* = n-1$, yielding a tight bound of $\Theta(n)$.

### Space Complexity
The space complexity $S(n)$ is determined by the auxiliary storage required for the hash map $M$. In the worst case, the algorithm may store $n-1$ elements before finding the complement.

The space complexity is:
$$S(n) = \text{space}(\text{map}) + O(1) = O(n)$$
where the map stores at most $n-1$ key-value pairs $(a_i, i)$. Thus, the auxiliary space complexity is $\Theta(n)$.