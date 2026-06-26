# Formal Mathematical Specification: Count Inversions (using BIT)

## 1. Definitions and Notation

Let $A = [a_1, a_2, \dots, a_n]$ be a sequence of $n$ integers. 

**Definition 1 (Inversion):** An inversion in $A$ is a pair of indices $(i, j)$ such that $1 \le i < j \le n$ and $a_i > a_j$. The set of all inversions is denoted by $\mathcal{I} = \{ (i, j) \in \mathbb{Z}^2 \mid 1 \le i < j \le n, a_i > a_j \}$. The objective is to compute the cardinality $|\mathcal{I}|$.

**Definition 2 (Coordinate Compression):** Let $U = \{u_1, u_2, \dots, u_m\}$ be the set of unique elements in $A$, sorted such that $u_1 < u_2 < \dots < u_m$, where $m \le n$. We define a rank function $\rho: A \to \{1, 2, \dots, m\}$ such that $\rho(a_i) = k$ if $a_i = u_k$. The transformed sequence is $A' = [\rho(a_1), \rho(a_2), \dots, \rho(a_n)]$.

**Definition 3 (Fenwick Tree):** A Fenwick Tree (Binary Indexed Tree) is a data structure represented by an array $B$ of size $m+1$, supporting two operations:
1. $\text{Update}(k, \delta)$: $B[j] \leftarrow B[j] + \delta$ for all $j$ such that $j$ is an ancestor of $k$ in the BIT structure.
2. $\text{Query}(k)$: $\sum_{j=1}^k B[j]$, which returns the prefix sum of frequencies.

## 2. Algebraic Characterization

The total number of inversions can be expressed as the sum of inversions contributed by each element $a_j$ as we traverse the array:
$$|\mathcal{I}| = \sum_{j=1}^n |\{ i < j \mid a_i > a_j \}|$$

By iterating from $j = n$ down to $1$, we maintain a frequency distribution of elements already processed. Let $S_j$ be the set of elements $\{a_{j+1}, \dots, a_n\}$. For a fixed $j$, the number of inversions involving $a_j$ is the count of elements in $S_j$ strictly smaller than $a_j$:
$$|\mathcal{I}_j| = \sum_{x \in S_j} \mathbb{I}(x < a_j)$$
where $\mathbb{I}(\cdot)$ is the indicator function. Using the rank function $\rho$, this becomes:
$$|\mathcal{I}_j| = \text{Query}(\rho(a_j) - 1)$$

**Loop Invariant:** At the start of iteration $j$ (where $j$ goes from $n$ down to $1$), the Fenwick Tree $B$ stores the frequency distribution of the set $\{ \rho(a_{j+1}), \dots, \rho(a_n) \}$. Specifically, for any $k \in \{1, \dots, m\}$, the prefix sum $\text{Query}(k)$ returns $|\{ i > j \mid \rho(a_i) \le k \}|$.

The total inversion count is the accumulation of these queries:
$$|\mathcal{I}| = \sum_{j=1}^n \text{Query}(\rho(a_j) - 1)$$
followed by the update $\text{Update}(\rho(a_j), 1)$ at each step.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of two primary phases:
1. **Coordinate Compression:** Sorting the unique elements of $A$ takes $O(n \log n)$. Mapping elements to ranks via a hash map or binary search takes $O(n \log n)$.
2. **BIT Operations:** The algorithm performs $n$ iterations. In each iteration, one `Query` and one `Update` operation are performed. Both operations traverse the height of the BIT, which is $\lceil \log_2 m \rceil$. Since $m \le n$, each operation is $O(\log n)$.

The total time complexity is:
$$T(n) = O(n \log n) + \sum_{j=1}^n O(\log n) = O(n \log n)$$

### Space Complexity
1. **Coordinate Compression:** Storing the unique elements and the rank mapping requires $O(n)$ space.
2. **Fenwick Tree:** The BIT array $B$ requires $O(m)$ space, where $m \le n$.
3. **Input Storage:** The compressed array $A'$ requires $O(n)$ space.

The total space complexity is:
$$S(n) = O(n) + O(m) + O(n) = O(n)$$