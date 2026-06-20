# Formal Mathematical Specification: Single Number (XOR)

## 1. Definitions and Notation

To establish a rigorous foundation for the algorithm, we define the mathematical domains, algebraic structures, and input-output spaces.

### 1.1 Mathematical Domains
* Let $W \in \mathbb{N}^+$ denote the word size of the machine architecture (typically $W = 32$ or $W = 64$).
* Let $\mathbb{B} = \{0, 1\}$ be the boolean domain.
* Let $\mathbb{F}_2^W$ denote the $W$-dimensional vector space over the Galois field of two elements, $\mathbb{F}_2$. An element $x \in \mathbb{F}_2^W$ is represented as a bit-vector:
  $$x = (x_{W-1}, x_{W-2}, \dots, x_0), \quad \text{where } x_k \in \mathbb{B} \text{ for } 0 \le k < W$$
* There exists a bijective mapping $\phi: \mathbb{F}_2^W \to \mathbb{Z}_{2^W}$ that maps each bit-vector to its unsigned integer representation:
  $$\phi(x) = \sum_{k=0}^{W-1} x_k 2^k$$

### 1.2 Input Specification
The input is a finite sequence (array) $A = (a_1, a_2, \dots, a_N)$ of length $N \in \mathbb{N}^+$, where $a_i \in \mathbb{F}_2^W$ for all $i \in \{1, \dots, N\}$. 

The sequence $A$ is guaranteed to satisfy the **Single Number Partition Property**:
There exists an odd integer $N = 2M + 1$ (for $M \in \mathbb{N}$) and a partition of the index set $I = \{1, 2, \dots, N\}$ into a singleton $\{i^*\}$ and $M$ disjoint pairs $P_j = \{u_j, v_j\}$ for $j \in \{1, \dots, M\}$:
$$I = \{i^*\} \cup \left( \bigcup_{j=1}^M \{u_j, v_j\} \right)$$
such that:
1. $a_{i^*} = x^*$ (the unique single element).
2. $\forall j \in \{1, \dots, M\}, \quad a_{u_j} = a_{v_j} = y_j$.
3. $x^* \neq y_j$ for all $j \in \{1, \dots, M\}$, and $y_j \neq y_k$ for all $j \neq k$.

### 1.3 Output Specification
The output of the algorithm is the unique element $x^* \in \mathbb{F}_2^W$ satisfying the input partition property.

### 1.4 State Space
The state of the algorithm at step $i$ is represented by an accumulator variable $s_i \in \mathbb{F}_2^W$. The state space of the algorithm is:
$$\mathcal{S} = \mathbb{F}_2^W$$

---

## 2. Algebraic Characterization

The correctness of the algorithm relies on the algebraic properties of the bitwise Exclusive-OR ($\text{XOR}$) operator, denoted by $\oplus$.

### 2.1 The Algebraic Structure $(\mathbb{F}_2^W, \oplus, \mathbf{0})$
The operator $\oplus: \mathbb{F}_2^W \times \mathbb{F}_2^W \to \mathbb{F}_2^W$ is defined bitwise. For $x, y \in \mathbb{F}_2^W$, the $k$-th bit of $x \oplus y$ is:
$$(x \oplus y)_k = x_k \oplus y_k = (x_k + y_k) \pmod 2$$

The algebraic structure $(\mathbb{F}_2^W, \oplus, \mathbf{0})$ forms an **elementary abelian 2-group** (isomorphic to the additive group of the vector space $\mathbb{F}_2^W$), which guarantees the following axioms:

1. **Closure:** $\forall x, y \in \mathbb{F}_2^W, \quad x \oplus y \in \mathbb{F}_2^W$.
2. **Associativity:** $\forall x, y, z \in \mathbb{F}_2^W, \quad (x \oplus y) \oplus z = x \oplus (y \oplus z)$.
3. **Identity Element:** The zero vector $\mathbf{0} = (0, 0, \dots, 0)$ acts as the identity:
   $$\forall x \in \mathbb{F}_2^W, \quad x \oplus \mathbf{0} = \mathbf{0} \oplus x = x$$
4. **Self-Inverse (Involution):** Every element is its own inverse:
   $$\forall x \in \mathbb{F}_2^W, \quad x \oplus x = \mathbf{0}$$
5. **Commutativity:** $\forall x, y \in \mathbb{F}_2^W, \quad x \oplus y = y \oplus x$.

### 2.2 State Transition and Recurrence Relation
The execution of the algorithm can be modeled as a discrete dynamical system over the state space $\mathcal{S}$. Let $s_i$ denote the state after processing the $i$-th element of the sequence $A$:

$$\begin{aligned}
s_0 &= \mathbf{0} \\
s_i &= s_{i-1} \oplus a_i, \quad \text{for } 1 \le i \le N
\end{aligned}$$

By unfolding the recurrence, the final state $s_N$ is the n-ary bitwise sum of the entire sequence:
$$s_N = \bigoplus_{i=1}^N a_i = a_1 \oplus a_2 \oplus \dots \oplus a_N$$

### 2.3 Loop Invariant
To formally prove correctness, we define the loop invariant $\mathcal{L}(i)$ for the loop variable $i \in \{0, \dots, N\}$:
$$\mathcal{L}(i): \left( s_i = \bigoplus_{k=1}^i a_k \right)$$

#### Proof of Loop Invariant by Induction:
* **Base Case ($i = 0$):** Before entering the loop, $s_0 = \mathbf{0}$. The empty XOR sum is defined as the identity element $\mathbf{0}$. Thus, $\mathcal{L}(0)$ holds.
* **Inductive Step:** Assume $\mathcal{L}(i-1)$ holds for some $1 \le i \le N$, meaning $s_{i-1} = \bigoplus_{k=1}^{i-1} a_k$. In the $i$-th iteration, the state transition updates the accumulator:
  $$s_i = s_{i-1} \oplus a_i$$
  Substituting the inductive hypothesis:
  $$s_i = \left( \bigoplus_{k=1}^{i-1} a_k \right) \oplus a_i = \bigoplus_{k=1}^i a_k$$
  Thus, $\mathcal{L}(i)$ holds. By mathematical induction, the loop invariant holds for all $i \in \{0, \dots, N\}$.

### 2.4 Proof of Correctness
Upon termination of the loop, $i = N$. By the loop invariant $\mathcal{L}(N)$, the final state is:
$$s_N = \bigoplus_{i=1}^N a_i$$

Using the **Single Number Partition Property** defined in Section 1.2, we partition the index set of the summation:
$$s_N = a_{i^*} \oplus \left( \bigoplus_{j=1}^M (a_{u_j} \oplus a_{v_j}) \right)$$

Applying the property that $a_{i^*} = x^*$ and $a_{u_j} = a_{v_j} = y_j$:
$$s_N = x^* \oplus \left( \bigoplus_{j=1}^M (y_j \oplus y_j) \right)$$

By the **Self-Inverse** property of $(\mathbb{F}_2^W, \oplus, \mathbf{0})$, we have $y_j \oplus y_j = \mathbf{0}$ for all $j$:
$$s_N = x^* \oplus \left( \bigoplus_{j=1}^M \mathbf{0} \right)$$

By the **Identity** property, the n-ary sum of $\mathbf{0}$ is $\mathbf{0}$:
$$s_N = x^* \oplus \mathbf{0}$$

Applying the identity property once more yields:
$$s_N = x^*$$

This completes the proof that the final state of the accumulator is precisely the unique unpaired element. $\blacksquare$

---

## 3. Complexity Analysis

### 3.1 Time Complexity
Let $T(N)$ represent the computational step complexity of the algorithm on an input sequence of size $N$. Under the standard **Word RAM model**, bitwise operations ($\oplus$) on $W$-bit words take $O(1)$ constant time.

The total work $T(N)$ can be expressed as the sum of the initialization cost and the cost of the loop iterations:
$$T(N) = T_{\text{init}} + \sum_{i=1}^N T_{\text{iter}}(i)$$

Where:
* $T_{\text{init}}$ is the cost of initializing $result = 0$, which is $O(1)$.
* $T_{\text{iter}}(i)$ is the cost of the $i$-th iteration, consisting of:
  1. Array lookup $a_i$: $O(1)$ time.
  2. Bitwise XOR operation $s_{i-1} \oplus a_i$: $O(1)$ time.
  3. State assignment $s_i \leftarrow s_{i-1} \oplus a_i$: $O(1)$ time.

Thus, $T_{\text{iter}}(i) = c$ for some constant $c > 0$. The summation yields:
$$T(N) = c_0 + \sum_{i=1}^N c = c_0 + c \cdot N$$

Using asymptotic notation:
$$T(N) \in \Theta(N)$$

The algorithm runs in strictly linear time, matching both the worst-case and best-case bounds:
$$\Omega(N) \le T(N) \le O(N)$$

### 3.2 Space Complexity
Let $S_{\text{aux}}(N)$ denote the auxiliary space complexity of the algorithm, representing the additional memory allocated beyond the input array.

The algorithm allocates memory for exactly one state variable:
$$\text{Var} = \{s\} \subset \mathbb{F}_2^W$$

The memory footprint of $s$ is constant and independent of the input size $N$:
$$\text{Size}(s) = W \text{ bits} = O(1) \text{ words}$$

Since no dynamic memory allocation, auxiliary data structures, or recursive call stacks are utilized:
$$S_{\text{aux}}(N) \in \Theta(1)$$

The total space complexity (including the read-only input sequence of size $N$) is:
$$S_{\text{total}}(N) = S_{\text{input}}(N) + S_{\text{aux}}(N) \in \Theta(N)$$