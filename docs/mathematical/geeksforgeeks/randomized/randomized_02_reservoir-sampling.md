# Formal Mathematical Specification: Reservoir Sampling

## 1. Definitions and Notation

Let $\mathcal{S} = \{x_1, x_2, \dots, x_N\}$ be a sequence of items (a stream) of unknown length $N \in \mathbb{N}$. We define the sampling objective as the selection of a subset $\mathcal{R} \subset \mathcal{S}$ such that $|\mathcal{R}| = K$, where $K \le N$.

*   **Input:** A stream $\mathcal{S}$ and a capacity $K \in \mathbb{Z}^+$.
*   **State Space:** Let $\mathcal{R}_i$ denote the state of the reservoir after processing the $i$-th element of the stream, where $\mathcal{R}_i = \{r_1, r_2, \dots, r_K\}$.
*   **Random Variable:** Let $J_i$ be a discrete uniform random variable such that $J_i \sim \text{Uniform}\{1, 2, \dots, i\}$.
*   **Output:** The final state $\mathcal{R}_N$ such that for any $x \in \mathcal{S}$, the probability of inclusion $P(x \in \mathcal{R}_N) = \frac{K}{N}$.

## 2. Algebraic Characterization

The algorithm is defined by the following state transition for the reservoir $\mathcal{R}_i$ upon the arrival of element $x_{i+1}$:

1.  **Initialization:** For $i \le K$, $\mathcal{R}_i = \{x_1, \dots, x_i\}$.
2.  **Transition:** For $i > K$, the reservoir $\mathcal{R}_i$ is updated to $\mathcal{R}_{i+1}$ as follows:
    $$
    \mathcal{R}_{i+1} = 
    \begin{cases} 
    (\mathcal{R}_i \setminus \{r_{J_{i+1}}\}) \cup \{x_{i+1}\} & \text{if } J_{i+1} \le K \\
    \mathcal{R}_i & \text{if } J_{i+1} > K 
    \end{cases}
    $$
    where $J_{i+1} \sim \text{Uniform}\{1, \dots, i+1\}$.

**Theorem (Correctness):** For any $x_m \in \mathcal{S}$, the probability that $x_m \in \mathcal{R}_N$ is $\frac{K}{N}$.

*Proof by Induction:*
Base case: For $i=K$, $P(x_m \in \mathcal{R}_K) = 1 = \frac{K}{K}$.
Inductive step: Assume $P(x_m \in \mathcal{R}_i) = \frac{K}{i}$. Upon arrival of $x_{i+1}$, $x_m$ remains in the reservoir if it was already present and was not replaced. The probability of replacement is $P(\text{replace}) = P(J_{i+1} \le K) \cdot P(\text{select } x_m | J_{i+1} \le K) = \frac{K}{i+1} \cdot \frac{1}{K} = \frac{1}{i+1}$.
Thus, the probability of survival is:
$$P(x_m \in \mathcal{R}_{i+1}) = P(x_m \in \mathcal{R}_i) \cdot \left(1 - \frac{1}{i+1}\right) = \frac{K}{i} \cdot \frac{i}{i+1} = \frac{K}{i+1}$$
By induction, $P(x_m \in \mathcal{R}_N) = \frac{K}{N}$.

## 3. Complexity Analysis

### Time Complexity
The algorithm processes each element $x_i$ in the stream exactly once. For each $i \in \{1, \dots, N\}$, the operations performed are:
1.  Generation of a random integer $J_i$: $O(1)$.
2.  Conditional comparison and potential array update: $O(1)$.

The total time complexity $T(N)$ is given by the summation:
$$T(N) = \sum_{i=1}^{N} O(1) = O(N)$$
Since the algorithm performs a single pass and constant-time operations per element, the complexity is strictly linear with respect to the stream length $N$.

### Space Complexity
The algorithm maintains a reservoir $\mathcal{R}$ of fixed capacity $K$. 
*   **Auxiliary Space:** The reservoir requires $O(K)$ storage to hold the sampled elements.
*   **Total Space:** Beyond the input stream (which is processed element-by-element and not stored in its entirety), the memory footprint is dominated by the reservoir.
Thus, the space complexity is $O(K)$, independent of $N$.