# Formal Mathematical Specification: Freivalds' Algorithm (Matrix Product Check)

## 1. Definitions and Notation

Let $n \in \mathbb{N}$ denote the dimension of the square matrices. We are given three matrices $A, B, C \in \mathbb{F}^{n \times n}$, where $\mathbb{F}$ is a field (typically $\mathbb{R}$ or a finite field $\mathbb{Z}_p$). 

The objective is to decide the predicate $P: A \cdot B = C$. 

We define the following:
*   **Random Vector Space:** Let $\mathcal{R} = \{0, 1\}^n$ be the set of all possible column vectors of length $n$ with entries in $\{0, 1\}$.
*   **Sampling:** Let $\mathbf{r} \in \mathcal{R}$ be a random vector chosen uniformly at random from $\mathcal{R}$, such that $\mathbb{P}(\mathbf{r} = \mathbf{v}) = 2^{-n}$ for any $\mathbf{v} \in \mathcal{R}$.
*   **State Space:** The algorithm operates on the state space $\mathcal{S} = \mathbb{F}^n$, representing the intermediate vectors resulting from matrix-vector products.
*   **Trial Parameter:** Let $k \in \mathbb{N}$ be the number of independent iterations performed to amplify the confidence of the result.

## 2. Algebraic Characterization

The correctness of the algorithm relies on the associativity of matrix multiplication and the properties of the difference matrix $D = A \cdot B - C$.

**Theorem (Correctness):**
1. If $A \cdot B = C$, then for any $\mathbf{r} \in \mathcal{R}$, $A(B\mathbf{r}) = C\mathbf{r}$. This follows from the distributive property: $A(B\mathbf{r}) - C\mathbf{r} = (AB - C)\mathbf{r} = \mathbf{0}\mathbf{r} = \mathbf{0}$.
2. If $A \cdot B \neq C$, let $D = AB - C$. Since $D \neq \mathbf{0}$, there exists at least one non-zero row in $D$. Freivalds' Lemma states that for a vector $\mathbf{r}$ chosen uniformly at random from $\{0, 1\}^n$:
   $$\mathbb{P}(D\mathbf{r} = \mathbf{0} \mid D \neq \mathbf{0}) \leq \frac{1}{2}$$

**Proof Sketch:**
Let $d_i$ be a non-zero row of $D$. The condition $D\mathbf{r} = \mathbf{0}$ implies $d_i \cdot \mathbf{r} = 0$. Let $d_{ij} \neq 0$ be a non-zero entry in $d_i$. We can isolate $r_j$ in the dot product:
$$r_j = -\frac{1}{d_{ij}} \left( \sum_{k \neq j} d_{ik} r_k \right)$$
For any fixed assignment of the other $n-1$ variables, there is at most one value for $r_j$ that satisfies the equation. Since $r_j$ is chosen from $\{0, 1\}$, the probability that the chosen $r_j$ satisfies this equality is at most $1/2$.

**Error Probability:**
By repeating the test $k$ times with independent vectors $\mathbf{r}_1, \dots, \mathbf{r}_k$, the probability of a false positive (outputting `True` when $A \cdot B \neq C$) is bounded by:
$$\mathbb{P}(\text{False Positive}) \leq \left( \frac{1}{2} \right)^k = 2^{-k}$$

## 3. Complexity Analysis

### Time Complexity
The algorithm performs $k$ iterations. In each iteration, we compute:
1. $\mathbf{v}_1 = B\mathbf{r}$
2. $\mathbf{v}_2 = A\mathbf{v}_1$
3. $\mathbf{v}_3 = C\mathbf{r}$

Each matrix-vector multiplication involves $n^2$ scalar multiplications and $n(n-1)$ additions. The complexity of one matrix-vector product is $\Theta(n^2)$. 
The total time complexity $T(n, k)$ is given by:
$$T(n, k) = \sum_{i=1}^{k} \Theta(n^2) = \Theta(k \cdot n^2)$$
Given $k$ is a constant relative to $n$, the algorithm achieves $O(n^2)$ time complexity, which is strictly superior to the $O(n^3)$ required for explicit matrix multiplication.

### Space Complexity
The algorithm requires storage for the input matrices ($O(n^2)$) and auxiliary space for the vectors $\mathbf{r}, \mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$. Each vector requires $O(n)$ space.
The auxiliary space complexity is:
$$S(n) = O(n)$$
Thus, the algorithm is highly space-efficient, requiring only linear auxiliary space beyond the input storage.