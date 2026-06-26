# Formal Mathematical Specification: Minimum Bit Flips to Convert Number

## 1. Definitions and Notation

Let $\mathbb{Z}_{2^W} = \{0, 1, \dots, 2^W - 1\}$ denote the set of non-negative integers representable within a $W$-bit computer word, where $W \in \mathbb{N}$ is the word size (typically $W = 32$ or $W = 64$). 

### Binary Representation
For any integer $x \in \mathbb{Z}_{2^W}$, its unique $W$-bit binary representation is given by the vector $\mathbf{x} = (x_{W-1}, x_{W-2}, \dots, x_0) \in \{0, 1\}^W$ such that:
$$x = \sum_{i=0}^{W-1} x_i 2^i$$
where $x_i \in \{0, 1\}$ represents the $i$-th bit of $x$.

### Bitwise Operators
We define the following binary operators over $\mathbb{Z}_{2^W}$:
1. **Bitwise XOR ($\oplus$):** 
   $$(x \oplus y)_i = x_i \oplus y_i \equiv (x_i + y_i) \pmod 2 \quad \forall i \in \{0, \dots, W-1\}$$
2. **Bitwise AND ($\wedge$):**
   $$(x \wedge y)_i = x_i \cdot y_i \quad \forall i \in \{0, \dots, W-1\}$$

### Hamming Distance and Hamming Weight
* **Hamming Distance:** The Hamming distance $d_H: \mathbb{Z}_{2^W} \times \mathbb{Z}_{2^W} \to \{0, \dots, W\}$ measures the number of positions at which the corresponding bits of two integers differ:
  $$d_H(a, b) = \sum_{i=0}^{W-1} (a_i \oplus b_i)$$
* **Hamming Weight:** The Hamming weight (or population count) $\operatorname{wt}: \mathbb{Z}_{2^W} \to \{0, \dots, W\}$ is the number of non-zero bits in an integer:
  $$\operatorname{wt}(z) = \sum_{i=0}^{W-1} z_i$$

### Problem Formulation
Given two integers $a, b \in \mathbb{Z}_{2^W}$, the objective is to compute the minimum number of bit flips required to convert $a$ to $b$. This is mathematically equivalent to computing the Hamming distance between $a$ and $b$:
$$f(a, b) = d_H(a, b) = \operatorname{wt}(a \oplus b)$$

---

## 2. Algebraic Characterization and Correctness

The algorithm computes $f(a, b)$ in two distinct phases:
1. **Isolating Discrepancies:** Computing the bitwise XOR difference $z = a \oplus b$.
2. **Population Count:** Computing $\operatorname{wt}(z)$ using Brian Kernighan’s algorithm.

### Algebraic Properties of Brian Kernighan's Transition
Let $\operatorname{lsb}(x)$ denote the index of the least significant set bit of a non-zero integer $x \in \mathbb{Z}_{2^W} \setminus \{0\}$:
$$\operatorname{lsb}(x) = \min \{ i \in \{0, \dots, W-1\} \mid x_i = 1 \}$$

We can express $x$ algebraically as:
$$x = y \cdot 2^{\operatorname{lsb}(x) + 1} + 2^{\operatorname{lsb}(x)}$$
where $y \in \mathbb{Z}_{2^{W - \operatorname{lsb}(x) - 1}}$. 

Subtracting $1$ from $x$ yields:
$$x - 1 = y \cdot 2^{\operatorname{lsb}(x) + 1} + 2^{\operatorname{lsb}(x)} - 1 = y \cdot 2^{\operatorname{lsb}(x) + 1} + \sum_{i=0}^{\operatorname{lsb}(x)-1} 2^i$$

Applying the bitwise AND operator to $x$ and $x-1$:
$$x \wedge (x - 1) = \left( y \cdot 2^{\operatorname{lsb}(x) + 1} + 2^{\operatorname{lsb}(x)} \right) \wedge \left( y \cdot 2^{\operatorname{lsb}(x) + 1} + \sum_{i=0}^{\operatorname{lsb}(x)-1} 2^i \right)$$

Because the bitwise AND of $2^{\operatorname{lsb}(x)}$ and $\sum_{i=0}^{\operatorname{lsb}(x)-1} 2^i$ is $0$, the expression simplifies to:
$$x \wedge (x - 1) = y \cdot 2^{\operatorname{lsb}(x) + 1}$$

This proves that the transition $x \leftarrow x \wedge (x - 1)$ clears exactly the least significant set bit of $x$ to $0$, leaving all other more significant bits unchanged. Consequently:
$$\operatorname{wt}(x \wedge (x - 1)) = \operatorname{wt}(x) - 1$$

### Formal Loop Invariant
Let $z^{(0)} = a \oplus b$ be the initial state, and let $c^{(0)} = 0$ be the initial counter. The state sequence $(z^{(j)}, c^{(j)})$ at the end of the $j$-th iteration of the loop is defined recursively by:
$$z^{(j+1)} = z^{(j)} \wedge (z^{(j)} - 1)$$
$$c^{(j+1)} = c^{(j)} + 1$$

**Invariant:** For any iteration step $j \ge 0$ where $z^{(j)}$ is defined:
$$\operatorname{wt}(z^{(j)}) = \operatorname{wt}(z^{(0)}) - j \quad \text{and} \quad c^{(j)} = j$$

#### Proof by Induction:
* **Base Case ($j=0$):** 
  $$\operatorname{wt}(z^{(0)}) = \operatorname{wt}(z^{(0)}) - 0 \quad \text{and} \quad c^{(0)} = 0$$
  The invariant holds trivially.
* **Inductive Step:** Assume the invariant holds for $j = k$, meaning $\operatorname{wt}(z^{(k)}) = \operatorname{wt}(z^{(0)}) - k$ and $c^{(k)} = k$. If $z^{(k)} \neq 0$, the loop executes for step $k+1$:
  $$\operatorname{wt}(z^{(k+1)}) = \operatorname{wt}(z^{(k)} \wedge (z^{(k)} - 1)) = \operatorname{wt}(z^{(k)}) - 1$$
  Substituting the inductive hypothesis:
  $$\operatorname{wt}(z^{(k+1)}) = \left( \operatorname{wt}(z^{(0)}) - k \right) - 1 = \operatorname{wt}(z^{(0)}) - (k+1)$$
  Similarly, for the counter:
  $$c^{(k+1)} = c^{(k)} + 1 = k + 1$$
  The invariant holds for $j = k+1$. $\square$

### Termination and Correctness
Since $\operatorname{wt}(z^{(j)}) \in \{0, \dots, W\}$ is a strictly decreasing sequence of non-negative integers, there exists a unique finite integer $K = \operatorname{wt}(z^{(0)})$ such that $z^{(K)} = 0$. 

At step $j = K$, the loop termination condition $z^{(j)} = 0$ is met. The final counter value is:
$$c^{(K)} = K = \operatorname{wt}(z^{(0)}) = \operatorname{wt}(a \oplus b) = d_H(a, b)$$

This guarantees both the termination of the algorithm and the correctness of the output.

---

## 3. Complexity Analysis

### Time Complexity
Let $K = d_H(a, b)$ be the Hamming distance between $a$ and $b$.

1. **XOR Operation:** The initial computation $z = a \oplus b$ is a primitive bitwise operation requiring $\Theta(1)$ time under the Word RAM model.
2. **Loop Iterations:** The loop executes exactly $K$ times. In each iteration $j \in \{0, \dots, K-1\}$, the algorithm performs:
   * One subtraction: $z^{(j)} - 1$
   * One bitwise AND: $z^{(j)} \wedge (z^{(j)} - 1)$
   * One increment: $c^{(j)} + 1$
   * One comparison: $z^{(j+1)} \neq 0$
   
   Each of these operations takes $\Theta(1)$ time on standard hardware architectures.

Thus, the total time complexity is:
$$T(W, K) = \Theta(1) + \sum_{j=0}^{K-1} \Theta(1) = \Theta(K)$$

#### Asymptotic Bounds:
* **Best-Case Complexity:** $\Theta(1)$ when $a = b$ (hence $K = 0$). The loop condition is false initially, and the algorithm terminates immediately.
* **Worst-Case Complexity:** $\Theta(W)$ when $a = \sim b$ (bitwise complement, hence $K = W$).
* **Average-Case Complexity:** Assuming $a$ and $b$ are chosen uniformly at random from $\mathbb{Z}_{2^W}$, each bit of $z = a \oplus b$ is an independent Bernoulli trial with parameter $p = 0.5$. The expected Hamming distance is:
  $$\mathbb{E}[K] = \sum_{i=0}^{W-1} \mathbb{E}[z_i] = \frac{W}{2}$$
  Thus, the average-case time complexity is $\Theta(W)$.

*Note on Hardware Optimization:* If the target architecture supports a dedicated hardware instruction for population count (e.g., `POPCNT` in x86 or `VCNT` in ARM), the Hamming weight can be computed in parallel using bit-permutation networks, reducing the time complexity to $\Theta(1)$ regardless of $K$.

### Space Complexity
The algorithm operates in-place and requires storage for only a fixed number of variables: the input values $a, b$, the intermediate difference $z$, and the counter $c$.

* **Auxiliary Space Complexity:** $\Theta(1)$ words of memory, which corresponds to $\Theta(W)$ bits.
* **Total Space Complexity:** $\Theta(1)$ words of memory to store the inputs and execution state.