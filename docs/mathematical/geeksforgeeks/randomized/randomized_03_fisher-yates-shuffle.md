# Formal Mathematical Specification: Fisher-Yates Shuffle

## 1. Definitions and Notation

Let $A = (a_0, a_1, \dots, a_{n-1})$ be a sequence of $n$ distinct elements belonging to a set $\mathcal{X}$. The set of all possible permutations of $A$ is denoted by $\mathcal{S}_n$, where $|\mathcal{S}_n| = n!$.

*   **Input:** A sequence $A^{(0)} \in \mathcal{S}_n$.
*   **State Space:** The algorithm proceeds through a sequence of states $A^{(k)}$ for $k = 0, 1, \dots, n-1$, where $A^{(k)}$ represents the configuration of the array after $k$ iterations.
*   **Random Variable:** Let $J_i$ be a discrete uniform random variable representing the index chosen at iteration $i$, such that $J_i \sim \text{Uniform}\{0, 1, \dots, i\}$.
*   **Output:** A permutation $A^{(n-1)}$ such that for any $\sigma \in \mathcal{S}_n$, the probability $P(A^{(n-1)} = \sigma) = \frac{1}{n!}$.

## 2. Algebraic Characterization

The Fisher-Yates shuffle (Durstenfeld's variant) defines a sequence of transpositions. Let $\tau_{i, j}$ be the transposition operator that swaps elements at indices $i$ and $j$. The algorithm generates a sequence of permutations:

$$A^{(n-k)} = A^{(n-k+1)} \circ \tau_{n-k, J_{n-k}}$$

where $k$ ranges from $1$ to $n-1$. 

### Correctness via Induction
To prove that the algorithm produces a uniform distribution, we define the loop invariant: at the start of iteration $i$ (where $i$ goes from $n-1$ down to $1$), the suffix $A[i+1 \dots n-1]$ is a uniformly random permutation of the $n-1-i$ elements originally at those positions, and the prefix $A[0 \dots i]$ contains the remaining elements.

**Base Case:** For $i = n-1$, the suffix is empty, and the prefix is the original array. The probability of any element being at index $n-1$ is $P(J_{n-1} = j) = \frac{1}{n}$ for all $j \in \{0, \dots, n-1\}$.

**Inductive Step:** Assume that after $k$ steps, any sequence of $k$ elements has been placed in the suffix with probability $\frac{(n-k)!}{n!}$. In the next step, we choose an index $j \in \{0, \dots, n-k-1\}$ with probability $\frac{1}{n-k}$. The probability that a specific element $x$ is moved to position $n-k-1$ is:
$$P(\text{element } x \text{ is chosen}) = P(\text{chosen at step } k) \times P(\text{not chosen in steps } 0 \dots k-1)$$
$$= \frac{1}{n-k} \times \prod_{m=0}^{k-1} \left(1 - \frac{1}{n-m}\right) = \frac{1}{n-k} \times \frac{n-k}{n} = \frac{1}{n}$$
Thus, by induction, every element has a $1/n$ probability of occupying any position, satisfying the condition for a uniform distribution over $\mathcal{S}_n$.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of a single loop iterating from $i = n-1$ down to $1$. 
Let $T(n)$ be the total time complexity. The work performed in each iteration $i$ consists of:
1. Generating a random integer $J_i$: $O(1)$ assuming a constant-time PRNG.
2. Swapping two elements in memory: $O(1)$.

The total time complexity is given by the summation:
$$T(n) = \sum_{i=1}^{n-1} (O(1) + O(1)) = O(n)$$
Since the number of operations scales linearly with the input size $n$, the algorithm is $\Theta(n)$.

### Space Complexity
The algorithm operates in-place. We define the auxiliary space $S(n)$ as the additional memory required beyond the input array.
*   The algorithm utilizes a constant number of scalar variables (the loop index $i$, the random index $j$, and a temporary variable for the swap operation).
*   No additional data structures proportional to $n$ are allocated.

Thus, the auxiliary space complexity is:
$$S(n) = O(1)$$
The total space complexity, including the input array, is $O(n)$.