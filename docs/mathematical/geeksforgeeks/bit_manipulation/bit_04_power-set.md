# Formal Mathematical Specification: Power Set (Bitwise Optimization)

## 1. Definitions and Notation

Let $A = (a_0, a_1, \dots, a_{n-1})$ be an ordered $n$-tuple of unique elements drawn from a universe $\mathcal{U}$, where $n = |A| \in \mathbb{N}_0$. We denote the underlying set of elements in $A$ as:
$$S_A = \{a_i \mid 0 \le i < n\}$$

The goal of the algorithm is to construct the power set of $S_A$, denoted by $\mathcal{P}(S_A)$, which is the set of all subsets of $S_A$:
$$\mathcal{P}(S_A) = \{ X \mid X \subseteq S_A \}$$

By elementary combinatorics, the cardinality of the power set is $|\mathcal{P}(S_A)| = 2^n$.

### The Bitmask Domain
Let $\mathbb{B} = \{0, 1\}$ represent the boolean domain. We define the set of $n$-bit integers (or bitmasks) as:
$$\mathcal{M}_n = \{0, 1, \dots, 2^n - 1\}$$

For any integer $m \in \mathcal{M}_n$, there exists a unique binary representation of length $n$, denoted by the sequence of bits $(b_{n-1}, \dots, b_1, b_0)_2$, such that:
$$m = \sum_{i=0}^{n-1} b_i 2^i \quad \text{where} \quad b_i \in \mathbb{B}$$

We define the projection function $\beta: \mathcal{M}_n \times \{0, \dots, n-1\} \to \mathbb{B}$ which extracts the $i$-th bit of $m$:
$$\beta(m, i) = \left\lfloor \frac{m}{2^i} \right\rfloor \bmod 2$$

In computer systems using two's complement representation, this projection is implemented via the bitwise shift and bitwise AND operations:
$$\beta(m, i) = (m \gg i) \ \& \ 1 = \operatorname{sgn}(m \ \& \ (1 \ll i))$$
where $\gg$ is the right-shift operator, $\ll$ is the left-shift operator, $\&$ is the bitwise conjunction, and $\operatorname{sgn}(x)$ is the signum function.

---

## 2. Algebraic Characterization

The correctness of the bitwise power set generation algorithm relies on establishing an isomorphism between the boolean hypercube $\mathbb{B}^n$ (represented by the bitmasks $\mathcal{M}_n$) and the power set $\mathcal{P}(S_A)$.

### The Characteristic Mapping
We define the mapping $\phi: \mathcal{M}_n \to \mathcal{P}(S_A)$ as:
$$\phi(m) = \{ a_i \in S_A \mid \beta(m, i) = 1 \}$$

#### Theorem 1 (Bijectivity of $\phi$)
*The mapping $\phi: \mathcal{M}_n \to \mathcal{P}(S_A)$ is a bijection.*

**Proof:**
1. **Injectivity:** Let $m_1, m_2 \in \mathcal{M}_n$ such that $m_1 \neq m_2$. By the uniqueness of binary representations, there exists at least one index $j \in \{0, \dots, n-1\}$ such that $\beta(m_1, j) \neq \beta(m_2, j)$. Without loss of generality, assume $\beta(m_1, j) = 1$ and $\beta(m_2, j) = 0$. By definition of $\phi$:
   $$a_j \in \phi(m_1) \quad \text{and} \quad a_j \notin \phi(m_2)$$
   Thus, $\phi(m_1) \neq \phi(m_2)$, proving injectivity.

2. **Surjectivity:** Let $Y \in \mathcal{P}(S_A)$ be an arbitrary subset. Construct an integer $m_Y$ such that:
   $$m_Y = \sum_{i=0}^{n-1} \mathbb{I}(a_i \in Y) \cdot 2^i$$
   where $\mathbb{I}$ is the indicator function. Since $Y \subseteq S_A$, we have $0 \le m_Y \le 2^n - 1$, meaning $m_Y \in \mathcal{M}_n$. By construction, $\beta(m_Y, i) = 1 \iff a_i \in Y$. Thus, $\phi(m_Y) = Y$, proving surjectivity.

Since $\phi$ is both injective and surjective, it is a bijection. Consequently, iterating through all $m \in \mathcal{M}_n$ and computing $\phi(m)$ guarantees the generation of every subset of $S_A$ exactly once.

### Loop Invariants
Let $\mathcal{R}^{(k)}$ denote the state of the accumulated list of subsets after processing $k$ iterations of the outer loop, where $k \in \{0, \dots, 2^n\}$.

* **Initialization ($k = 0$):**
  $$\mathcal{R}^{(0)} = \emptyset$$
  The relation holds trivially as no masks have been processed.

* **Maintenance ($k \to k+1$):**
  During the $k$-th iteration, the algorithm computes the subset corresponding to the mask $m = k$:
  $$\text{subset}^{(k)} = \{ a_i \in S_A \mid (k \ \& \ (1 \ll i)) \neq 0 \}$$
  By definition of the bitwise operations, $\text{subset}^{(k)} = \phi(k)$. The state transition is defined by:
  $$\mathcal{R}^{(k+1)} = \mathcal{R}^{(k)} \cup \{ \phi(k) \}$$
  Assuming the invariant holds for $k$, we have:
  $$\mathcal{R}^{(k+1)} = \{ \phi(m) \mid 0 \le m < k \} \cup \{ \phi(k) \} = \{ \phi(m) \mid 0 \le m \le k \}$$

* **Termination ($k = 2^n$):**
  The loop terminates when $k = 2^n$. The final state is:
  $$\mathcal{R}^{(2^n)} = \{ \phi(m) \mid 0 \le m < 2^n \} = \phi(\mathcal{M}_n)$$
  Since $\phi$ is a bijection, $\phi(\mathcal{M}_n) = \mathcal{P}(S_A)$. This proves the algebraic correctness of the algorithm.

---

## 3. Complexity Analysis

### Time Complexity

To derive the time complexity, we analyze the total number of elementary operations performed by the nested loop structure. Let $T(n)$ represent the running time of the algorithm on an input of size $n$.

The outer loop executes exactly $2^n$ times, corresponding to the range of the bitmask $m \in [0, 2^n - 1]$. For each mask $m$, the inner loop executes exactly $n$ times, corresponding to the index $i \in [0, n - 1]$.

Within the inner loop, the algorithm performs:
1. A bitwise left-shift: $1 \ll i$
2. A bitwise AND: $m \ \& \ (1 \ll i)$
3. A comparison with zero: $\neq 0$
4. An conditional array append operation: $\text{subset.append}(a_i)$

On a standard Word-RAM model of computation where the word size $w \ge n$, basic bitwise operations ($1 \ll i$ and $\&$) run in $O(1)$ constant time. The conditional append operation takes $O(1)$ amortized time.

Let $c_1$ be the constant cost of the loop control and bitwise evaluation, and let $c_2$ be the constant cost of appending an element to the current subset. The total time complexity can be modeled as:
$$T(n) = \sum_{m=0}^{2^n-1} \left( \sum_{i=0}^{n-1} c_1 + c_2 \cdot \mathbb{I}(a_i \in \phi(m)) \right)$$

We split this double summation into two parts:
$$T(n) = \sum_{m=0}^{2^n-1} n \cdot c_1 + c_2 \sum_{m=0}^{2^n-1} |\phi(m)|$$

The first term simplifies to:
$$\sum_{m=0}^{2^n-1} n \cdot c_1 = c_1 \cdot n 2^n$$

The second term represents the sum of the cardinalities of all subsets in $\mathcal{P}(S_A)$. Using the binomial theorem, we compute this sum as:
$$\sum_{m=0}^{2^n-1} |\phi(m)| = \sum_{k=0}^{n} \binom{n}{k} k$$

Using the identity $k \binom{n}{k} = n \binom{n-1}{k-1}$, we obtain:
$$\sum_{k=1}^{n} n \binom{n-1}{k-1} = n \sum_{j=0}^{n-1} \binom{n-1}{j} = n 2^{n-1}$$

Substituting these back into the expression for $T(n)$:
$$T(n) = c_1 \cdot n 2^n + c_2 \cdot n 2^{n-1} = \left( c_1 + \frac{c_2}{2} \right) n 2^n$$

Thus, the asymptotic time complexity is tightly bounded:
$$T(n) = \Theta(n 2^n)$$

### Space Complexity

We analyze the space complexity by distinguishing between auxiliary space and total space.

#### Auxiliary Space
Auxiliary space refers to the temporary memory allocated by the algorithm, excluding the memory required to store the final output.
* The loop variables $m$ and $i$ require $O(1)$ space.
* The temporary list `subset` stores at most $n$ elements at any given time before being appended to the result list.
* No recursive call stack is utilized, meaning the call stack depth is $O(1)$.

Thus, the auxiliary space complexity is:
$$S_{\text{aux}}(n) = O(n)$$

If the algorithm writes the generated subsets directly to an output stream or buffer without maintaining the intermediate `subset` array in memory (e.g., via a generator pattern), the auxiliary space complexity reduces to:
$$S_{\text{aux}}(n) = O(1)$$

#### Total Space
The total space complexity includes the memory required to represent the output $\mathcal{P}(S_A)$. The output consists of $2^n$ lists. The total number of elements stored across all lists is:
$$\sum_{k=0}^{n} \binom{n}{k} k = n 2^{n-1}$$

Therefore, the total space complexity is:
$$S_{\text{total}}(n) = \Theta(n 2^n)$$