# Formal Mathematical Specification: 0-1 Knapsack (FPTAS Approximation)

## 1. Definitions and Notation

Let $I = \{1, 2, \dots, n\}$ denote a set of $n \in \mathbb{N}_{>0}$ items. Each item $i \in I$ is characterized by a tuple $(w_i, v_i)$, where:
*   $w_i \in \mathbb{R}_{>0}$ represents the **weight** of item $i$.
*   $v_i \in \mathbb{R}_{>0}$ represents the **value** of item $i$.

Let $W \in \mathbb{R}_{>0}$ denote the maximum weight capacity of the knapsack. Without loss of generality, we assume that $w_i \le W$ for all $i \in I$, as any item exceeding the capacity can be discarded in a preprocessing step.

Let $x = (x_1, x_2, \dots, x_n) \in \{0, 1\}^n$ be a decision vector, where $x_i = 1$ if item $i$ is selected, and $x_i = 0$ otherwise. The feasible region $\mathcal{X}$ is defined as:
$$\mathcal{X} = \left\{ x \in \{0, 1\}^n \;\middle|\; \sum_{i=1}^n w_i x_i \le W \right\}$$

The objective is to maximize the total value of the selected items. The optimal solution value $OPT$ is defined as:
$$OPT = \max_{x \in \mathcal{X}} \sum_{i=1}^n v_i x_i$$

Let $\epsilon \in (0, 1)$ be the user-defined approximation tolerance parameter. A **Fully Polynomial-Time Approximation Scheme (FPTAS)** is an algorithm that outputs a feasible solution $x^{approx} \in \mathcal{X}$ satisfying:
$$\sum_{i=1}^n v_i x^{approx}_i \ge (1 - \epsilon) OPT$$
with a running time bounded by a polynomial in $n$ and $1/\epsilon$.

---

## 2. Algebraic Characterization

To decouple the computational complexity from the magnitude of the values $v_i$ and the capacity $W$, the FPTAS scales and rounds the item values.

### 2.1 Value Scaling and Quantization
Let $v_{\max} = \max_{i \in I} v_i$. Since $w_i \le W$ for all $i$, the optimal solution must contain at least one item, implying:
$$v_{\max} \le OPT \le n \cdot v_{\max}$$

We define the scaling factor $K \in \mathbb{R}_{>0}$ as:
$$K = \frac{\epsilon \cdot v_{\max}}{n}$$

For each item $i \in I$, we define its scaled integer value $v'_i \in \mathbb{Z}_{\ge 0}$ via the floor function:
$$v'_i = \left\lfloor \frac{v_i}{K} \right\rfloor$$

### 2.2 Dual Dynamic Programming Formulation (Value-Based DP)
Because the scaled values $v'_i$ are integers, we can compute the minimum weight required to achieve a specific scaled value. Let $V'_{max}$ be the upper bound on the sum of scaled values:
$$V'_{max} = \sum_{i=1}^n v'_i \le \sum_{i=1}^n \frac{v_i}{K} \le \frac{n \cdot v_{\max}}{K} = \frac{n^2}{\epsilon}$$

We define the state space $\mathcal{S} = \{0, \dots, n\} \times \{0, \dots, V'_{max}\}$. Let $DP(i, v)$ represent the minimum weight required to achieve a total scaled value of exactly $v$ using a subset of the first $i$ items.

#### Base Cases
$$\forall v \in \{1, \dots, V'_{max}\}, \quad DP(0, v) = \infty$$
$$DP(0, 0) = 0$$

#### Recurrence Relation
For $i \in \{1, \dots, n\}$ and $v \in \{0, \dots, V'_{max}\}$:
$$DP(i, v) = \begin{cases} 
DP(i-1, v) & \text{if } v < v'_i \\
\min\left( DP(i-1, v), \, DP(i-1, v - v'_i) + w_i \right) & \text{if } v \ge v'_i 
\end{cases}$$

### 2.3 Optimization and Reconstruction
The maximum scaled value achievable within capacity $W$ is:
$$V'_{approx} = \max \left\{ v \in \{0, \dots, V'_{max}\} \;\middle|\; DP(n, v) \le W \right\}$$

The approximate decision vector $x^{approx} \in \mathcal{X}$ is reconstructed by backtracking from the state $(n, V'_{approx})$. The final returned value is:
$$ALG = \sum_{i=1}^n v_i x^{approx}_i$$

### 2.4 Mathematical Proof of the Approximation Guarantee
We prove that $ALG \ge (1 - \epsilon) OPT$.

By the definition of the floor function, for any item $i \in I$:
$$\frac{v_i}{K} - 1 < \left\lfloor \frac{v_i}{K} \right\rfloor \le \frac{v_i}{K} \implies v_i - K < K v'_i \le v_i$$

Let $x^* \in \mathcal{X}$ be the optimal decision vector for the original instance, and let $x^{approx} \in \mathcal{X}$ be the optimal decision vector for the scaled instance. By definition of optimality under the scaled values:
$$\sum_{i=1}^n v'_i x^{approx}_i \ge \sum_{i=1}^n v'_i x^*_i$$

Multiplying both sides by $K$:
$$\sum_{i=1}^n K v'_i x^{approx}_i \ge \sum_{i=1}^n K v'_i x^*_i$$

Applying the lower and upper bounds of $K v'_i$:
$$ALG = \sum_{i=1}^n v_i x^{approx}_i \ge \sum_{i=1}^n K v'_i x^{approx}_i \ge \sum_{i=1}^n K v'_i x^*_i \ge \sum_{i=1}^n (v_i - K) x^*_i$$

Expanding the rightmost term:
$$ALG \ge \sum_{i=1}^n v_i x^*_i - K \sum_{i=1}^n x^*_i = OPT - K \sum_{i=1}^n x^*_i$$

Since $x^*_i \in \{0, 1\}$, we have $\sum_{i=1}^n x^*_i \le n$. Substituting this and the definition of $K$:
$$ALG \ge OPT - n K = OPT - n \left( \frac{\epsilon \cdot v_{\max}}{n} \right) = OPT - \epsilon \cdot v_{\max}$$

Since $v_{\max} \le OPT$:
$$ALG \ge OPT - \epsilon \cdot OPT = (1 - \epsilon) OPT$$

This completes the proof.

---

## 3. Complexity Analysis

### 3.1 Time Complexity
The time complexity of the algorithm is dominated by the construction of the dynamic programming table.

1.  **Scaling Step:** Computing $v_{\max}$ and scaling all $n$ values to $v'_i$ takes $\Theta(n)$ operations.
2.  **DP Table Size:** The table has dimensions $n \times (V'_{max} + 1)$. The upper bound on $V'_{max}$ is:
    $$V'_{max} \le \frac{n^2}{\epsilon}$$
    Thus, the total number of states is bounded by:
    $$| \mathcal{S} | \le n \cdot \left( \frac{n^2}{\epsilon} + 1 \right) = O\left( \frac{n^3}{\epsilon} \right)$$
3.  **State Transitions:** Each state transition $DP(i, v)$ requires $O(1)$ operations (a single lookup and minimization).
4.  **Reconstruction:** Finding $V'_{approx}$ requires scanning the last row of the DP table, taking $O(V'_{max}) = O(n^2/\epsilon)$ steps. Backtracking to find the selected items takes $O(n)$ steps.

Summing these components, the total time complexity is:
$$\mathcal{T}(n, \epsilon) = \Theta\left( \frac{n^3}{\epsilon} \right)$$

### 3.2 Space Complexity

#### Naive Implementation
Storing the entire 2D DP table to allow straightforward backtracking requires:
$$\mathcal{S}_{naive}(n, \epsilon) = \Theta\left( n \cdot V'_{max} \right) = \Theta\left( \frac{n^3}{\epsilon} \right) \text{ auxiliary space.}$$

#### Space-Optimized Implementation
Since the recurrence relation for row $i$ only depends on row $i-1$, we can compute the optimal value using only two rows (or a single row updated in reverse order from $V'_{max}$ down to $v'_i$). This reduces the auxiliary space complexity to:
$$\mathcal{S}_{optimized}(n, \epsilon) = \Theta\left( V'_{max} \right) = \Theta\left( \frac{n^2}{\epsilon} \right)$$

If item reconstruction is required within this reduced space bound, divide-and-conquer space-reduction techniques (such as Hirschberg's algorithm) can be applied to maintain $O(n^2/\epsilon)$ space while keeping the time complexity within $O(n^3/\epsilon)$.