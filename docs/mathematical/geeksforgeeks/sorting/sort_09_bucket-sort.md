# Formal Mathematical Specification: Bucket Sort

## 1. Definitions and Notation

Let $A = \{a_1, a_2, \dots, a_n\}$ be a multiset of $n$ real numbers such that each $a_i \in [x_{\min}, x_{\max}] \subset \mathbb{R}$. We define the range of the input as $R = x_{\max} - x_{\min}$.

We define a partition of the interval $[x_{\min}, x_{\max}]$ into $k$ disjoint sub-intervals (buckets), denoted by $B_0, B_1, \dots, B_{k-1}$. For a given $k \in \mathbb{N}$, the width of each bucket is defined as:
$$w = \frac{R}{k}$$
The $j$-th bucket $B_j$ is defined as the set of elements $a_i$ such that:
$$B_j = \{a_i \in A \mid \lfloor \frac{a_i - x_{\min}}{w} \rfloor = j\}$$
For the boundary case where $a_i = x_{\max}$, we define the mapping to the index $k-1$ to ensure inclusion in the final bucket.

The output is a sequence $S = (s_1, s_2, \dots, s_n)$ which is a permutation of $A$ such that $s_1 \leq s_2 \leq \dots \leq s_n$.

## 2. Algebraic Characterization

The correctness of Bucket Sort relies on the property that the concatenation of sorted buckets yields a sorted sequence. Let $f: A \to \{0, 1, \dots, k-1\}$ be the bucket assignment function:
$$f(a_i) = \min\left( \left\lfloor \frac{a_i - x_{\min}}{w} \right\rfloor, k-1 \right)$$

**Correctness Invariant:**
For any two buckets $B_u$ and $B_v$ where $u < v$, and for any elements $x \in B_u$ and $y \in B_v$, it holds that $x \leq y$. 

Proof sketch:
By the definition of $f(a_i)$, if $f(x) = u$ and $f(y) = v$ with $u < v$, then:
$$\frac{x - x_{\min}}{w} < u+1 \leq v \leq \frac{y - x_{\min}}{w}$$
Multiplying by $w$ and adding $x_{\min}$ yields $x < y$. Thus, if each bucket $B_j$ is sorted internally to produce a sequence $S_j$, the concatenation $S = S_0 \oplus S_1 \oplus \dots \oplus S_{k-1}$ is monotonically non-decreasing.

## 3. Complexity Analysis

### Time Complexity
The total time complexity $T(n)$ is the sum of the distribution time, the sorting time for each bucket, and the concatenation time.

1. **Distribution:** Mapping $n$ elements to buckets takes $\Theta(n)$ time.
2. **Sorting:** Let $n_j = |B_j|$ be the number of elements in bucket $j$. The time to sort the buckets is $\sum_{j=0}^{k-1} O(n_j^2)$ if using Insertion Sort.
3. **Concatenation:** Merging $k$ buckets takes $\Theta(n + k)$ time.

**Average Case:** Assuming the input $A$ is drawn from a uniform distribution, the expected number of elements in each bucket is $E[n_j] = \frac{n}{k}$. Setting $k = \Theta(n)$, we have $E[n_j] = 1$. The expected time complexity is:
$$E[T(n)] = \Theta(n) + \sum_{j=0}^{n-1} O(E[n_j^2]) = \Theta(n) + n \cdot O(1^2) = \Theta(n)$$

**Worst Case:** If the distribution is non-uniform such that all elements map to a single bucket ($n_j = n$ for some $j$), the complexity becomes:
$$T(n) = \Theta(n) + O(n^2) = O(n^2)$$

### Space Complexity
The algorithm requires auxiliary space to store the $k$ buckets and the $n$ elements distributed within them. 

1. **Bucket Storage:** We maintain an array of $k$ pointers/lists, requiring $\Theta(k)$ space.
2. **Element Storage:** Each element $a_i$ is stored exactly once across all buckets, requiring $\Theta(n)$ space.

The total space complexity is $\Theta(n + k)$. Given the standard implementation where $k \approx n$, the space complexity is $\Theta(n)$.