# Formal Mathematical Specification: Single Number III

## 1. Definitions and Notation

To establish a rigorous foundation for the Single Number III algorithm, we model the computer's word-level operations using both vector spaces over finite fields and modular arithmetic rings.

### 1.1. Mathematical Domains
Let $w \in \mathbb{N}$ denote the word size of the machine (typically $w = 32$ or $w = 64$). We define two isomorphic representations of a computer word:

1. **The Vector Space Representation**: Let $\mathcal{V} = \mathbb{F}_2^w$ be the $w$-dimensional vector space over the Galois field of two elements $\mathbb{F}_2 = (\{0, 1\}, +, \cdot)$. An element $\mathbf{x} \in \mathcal{V}$ is represented as a column vector:
   $$\mathbf{x} = \begin{pmatrix} x_0 \\ x_1 \\ \vdots \\ x_{w-1} \end{pmatrix}$$
   where $x_i \in \mathbb{F}_2$ represents the $i$-th bit of the word, with $x_0$ being the least significant bit (LSB).

2. **The Ring Representation**: Let $\mathcal{R} = \mathbb{Z} / 2^w\mathbb{Z}$ be the ring of integers modulo $2^w$. 

We define the bijective encoding function $\phi: \mathcal{V} \to \mathcal{R}$ that maps a bit vector to its unsigned integer equivalent:
$$\phi(\mathbf{x}) = \sum_{i=0}^{w-1} x_i 2^i \pmod{2^w}$$

### 1.2. Bitwise Operators
We formally define the bitwise operators over our domains:
* **Bitwise XOR ($\oplus$)**: This corresponds exactly to vector addition in the vector space $\mathcal{V}$:
  $$\mathbf{x} \oplus \mathbf{y} \triangleq \mathbf{x} + \mathbf{y} = \begin{pmatrix} x_0 + y_0 \pmod 2 \\ \vdots \\ x_{w-1} + y_{w-1} \pmod 2 \end{pmatrix}$$
* **Bitwise AND ($\wedge$)**: This corresponds to the component-wise multiplication of vectors:
  $$\mathbf{x} \wedge \mathbf{y} \triangleq \begin{pmatrix} x_0 \cdot y_0 \\ \vdots \\ x_{w-1} \cdot y_{w-1} \end{pmatrix}$$
* **Arithmetic Negation ($-$)**: Defined via the ring representation $\mathcal{R}$ to capture two's complement behavior:
  $$-\mathbf{x} \triangleq \phi^{-1}\left( -\phi(\mathbf{x}) \pmod{2^w} \right)$$

### 1.3. Input and Output Specifications
* **Input**: A finite sequence $A = (a_1, a_2, \dots, a_N)$ of length $N$, where $a_i \in \mathcal{V}$ for all $i \in \{1, \dots, N\}$.
* **Multiplicity Function**: Let $m_A: \mathcal{V} \to \mathbb{N}_0$ denote the multiplicity of an element in $A$:
  $$m_A(\mathbf{x}) = \sum_{i=1}^N \mathbb{I}(a_i = \mathbf{x})$$
  where $\mathbb{I}$ is the indicator function.
* **Constraints**:
  1. There exist exactly two distinct elements $\mathbf{u}, \mathbf{v} \in \mathcal{V}$ such that $\mathbf{u} \neq \mathbf{v}$, $m_A(\mathbf{u}) = 1$, and $m_A(\mathbf{v}) = 1$.
  2. For all other elements $\mathbf{x} \in \mathcal{V} \setminus \{\mathbf{u}, \mathbf{v}\}$, if $m_A(\mathbf{x}) > 0$, then $m_A(\mathbf{x}) = 2$.
  3. The total length of the sequence is $N = 2k + 2$ for some $k \in \mathbb{N}_0$.
* **Output**: The set $Y = \{\mathbf{u}, \mathbf{v}\}$.

---

## 2. Algebraic Characterization

The correctness of the Single Number III algorithm relies on the algebraic properties of the vector space $\mathcal{V}$ and the interaction between ring addition and bitwise operations.

### 2.1. Algebraic Properties of $(\mathcal{V}, \oplus)$
The algebraic structure $(\mathcal{V}, \oplus)$ is an abelian group of exponent 2, satisfying:
1. **Identity**: $\mathbf{x} \oplus \mathbf{0} = \mathbf{x}$
2. **Self-Inverse**: $\mathbf{x} \oplus \mathbf{x} = \mathbf{0}$
3. **Commutativity**: $\mathbf{x} \oplus \mathbf{y} = \mathbf{y} \oplus \mathbf{x}$
4. **Associativity**: $(\mathbf{x} \oplus \mathbf{y}) \oplus \mathbf{z} = \mathbf{x} \oplus (\mathbf{y} \oplus \mathbf{z})$

### 2.2. Phase 1: The Global XOR Sum
Let $\mathbf{S} \in \mathcal{V}$ be the cumulative XOR sum of all elements in $A$:
$$\mathbf{S} = \bigoplus_{i=1}^N a_i$$

Using the commutativity and associativity of $\oplus$, we partition the sum over the unique elements and the pairs:
$$\mathbf{S} = \mathbf{u} \oplus \mathbf{v} \oplus \left( \bigoplus_{\mathbf{x} \in \mathcal{V} \setminus \{\mathbf{u}, \mathbf{v}\}} \bigoplus_{j=1}^{m_A(\mathbf{x})} \mathbf{x} \right)$$

Since $m_A(\mathbf{x}) = 2$ for all paired elements, we have:
$$\bigoplus_{j=1}^{m_A(\mathbf{x})} \mathbf{x} = \mathbf{x} \oplus \mathbf{x} = \mathbf{0}$$

Thus, the global sum simplifies to:
$$\mathbf{S} = \mathbf{u} \oplus \mathbf{v}$$

Since $\mathbf{u} \neq \mathbf{v}$, it follows that $\mathbf{S} \neq \mathbf{0}$.

### 2.3. Phase 2: Bit Isolation (LSB Extraction)
Because $\mathbf{S} \neq \mathbf{0}$, there exists at least one index $p \in \{0, \dots, w-1\}$ such that $S_p = 1$. This implies $u_p \neq v_p$.

To isolate the lowest set bit of $\mathbf{S}$, we define the mask vector $\boldsymbol{\delta} \in \mathcal{V}$:
$$\boldsymbol{\delta} = \mathbf{S} \wedge (-\mathbf{S})$$

#### Lemma 1 (LSB Isolation)
*For any non-zero vector $\mathbf{x} \in \mathcal{V}$, let $p = \min \{ i \in \{0, \dots, w-1\} \mid x_i = 1 \}$ be the index of its least significant set bit. Then:*
$$\mathbf{x} \wedge (-\mathbf{x}) = \mathbf{e}^{(p)}$$
*where $\mathbf{e}^{(p)}$ is the $p$-th standard basis vector of $\mathbb{F}_2^w$ (i.e., $e^{(p)}_p = 1$ and $e^{(p)}_i = 0$ for all $i \neq p$).*

**Proof**:
Let $X = \phi(\mathbf{x})$. Since $p$ is the LSB index of $\mathbf{x}$, we can write $X$ as:
$$X = 2^p + q \cdot 2^{p+1} = 2^p(1 + 2q)$$
for some $q \in \mathbb{Z}$.

In the ring $\mathcal{R} = \mathbb{Z}/2^w\mathbb{Z}$, the additive inverse of $X$ is:
$$-X \equiv 2^w - X \equiv 2^w - 2^p(1 + 2q) \equiv 2^p(2^{w-p} - 1 - 2q) \pmod{2^w}$$

Using the identity $2^{w-p} - 1 = \sum_{j=0}^{w-p-1} 2^j$, we observe that:
$$-X = 2^p \left( 1 + 2k' \right)$$
for some $k' \in \mathbb{Z}$. This implies that the binary representation of $-X$, denoted by $\mathbf{y} = \phi^{-1}(-X)$, also has its first set bit at index $p$. Thus:
* For $i < p$: $x_i = 0$ and $y_i = 0 \implies x_i \cdot y_i = 0$.
* For $i = p$: $x_p = 1$ and $y_p = 1 \implies x_p \cdot y_p = 1$.
* For $i > p$: The two's complement negation guarantees that for any bit position $i > p$, $y_i = 1 - x_i$ (the bits are inverted). Thus, $x_i \cdot y_i = x_i \cdot (1 - x_i) = 0$.

Therefore, the bitwise AND yields:
$$\mathbf{x} \wedge (-\mathbf{x}) = \mathbf{e}^{(p)}$$
$\blacksquare$

Applying Lemma 1 to our global sum $\mathbf{S}$, we obtain:
$$\boldsymbol{\delta} = \mathbf{e}^{(p)}$$
where $p$ is the lowest index where $\mathbf{u}$ and $\mathbf{v}$ differ.

### 2.4. Phase 3: Partitioning and Projection
We define a projection operator $\pi_p: \mathcal{V} \to \mathbb{F}_2$ that extracts the $p$-th coordinate of a vector:
$$\pi_p(\mathbf{x}) = \mathbf{x} \wedge \boldsymbol{\delta} = \begin{pmatrix} 0 \\ \vdots \\ x_p \\ \vdots \\ 0 \end{pmatrix}$$

We partition the input sequence $A$ into two disjoint sub-sequences $A_0$ and $A_1$ based on this projection:
$$A_0 = (a_i \in A \mid \pi_p(a_i) = \mathbf{0})$$
$$A_1 = (a_i \in A \mid \pi_p(a_i) = \boldsymbol{\delta})$$

#### Theorem 1 (Partition Correctness)
*The partition of $A$ into $A_0$ and $A_1$ separates $\mathbf{u}$ and $\mathbf{v}$ into different sub-sequences, while keeping all identical pairs within the same sub-sequence.*

**Proof**:
1. **Separation of $\mathbf{u}$ and $\mathbf{v}$**: By definition of $p$, we have $u_p \neq v_p$. Without loss of generality, assume $u_p = 1$ and $v_p = 0$. Then:
   $$\pi_p(\mathbf{u}) = \boldsymbol{\delta} \implies \mathbf{u} \in A_1$$
   $$\pi_p(\mathbf{v}) = \mathbf{0} \implies \mathbf{v} \in A_0$$
2. **Coherence of Pairs**: Let $\mathbf{x}, \mathbf{x}$ be a pair of identical elements in $A$. Since they are identical, their $p$-th bits are identical:
   $$\pi_p(\mathbf{x}) = \pi_p(\mathbf{x})$$
   Thus, both instances of $\mathbf{x}$ map to the same sub-sequence (either both to $A_0$ or both to $A_1$).
$\blacksquare$

### 2.5. Phase 4: Final Reduction
We compute the independent XOR sums of the partitions $A_0$ and $A_1$:
$$\mathbf{a} = \bigoplus_{\mathbf{x} \in A_1} \mathbf{x}, \quad \mathbf{b} = \bigoplus_{\mathbf{y} \in A_0} \mathbf{y}$$

By applying the self-inverse property of $(\mathcal{V}, \oplus)$ to the paired elements in each partition:
$$\mathbf{a} = \mathbf{u} \oplus \left( \bigoplus_{\mathbf{x} \in A_1 \setminus \{\mathbf{u}\}} \mathbf{x} \right) = \mathbf{u} \oplus \mathbf{0} = \mathbf{u}$$
$$\mathbf{b} = \mathbf{v} \oplus \left( \bigoplus_{\mathbf{y} \in A_0 \setminus \{\mathbf{v}\}} \mathbf{y} \right) = \mathbf{v} \oplus \mathbf{0} = \mathbf{v}$$

Thus, the final state variables $\mathbf{a}$ and $\mathbf{b}$ converge exactly to the unique elements $\mathbf{u}$ and $\mathbf{v}$.

---

## 3. Complexity Analysis

### 3.1. Time Complexity
Let $N$ be the number of elements in the input sequence $A$. The execution of the algorithm can be decomposed into three sequential loops:

1. **Global XOR Summation**:
   $$T_1(N) = \sum_{i=1}^N c_{\oplus}$$
   where $c_{\oplus}$ is the constant time required to perform a word-level bitwise XOR operation. Thus, $T_1(N) = \Theta(N)$.

2. **Bit Isolation**:
   $$T_2 = c_{\text{neg}} + c_{\wedge}$$
   where $c_{\text{neg}}$ and $c_{\wedge}$ are the constant times for word-level negation and bitwise AND. Under the word-RAM model, this is $T_2 = \Theta(1)$.

3. **Partitioned XOR Summation**:
   $$T_3(N) = \sum_{i=1}^N \left( c_{\text{cond}} + c_{\oplus} \right)$$
   where $c_{\text{cond}}$ is the constant time to evaluate the projection condition $\pi_p(a_i)$. Thus, $T_3(N) = \Theta(N)$.

The total time complexity $T(N)$ is the sum of these components:
$$T(N) = T_1(N) + T_2 + T_3(N) = \Theta(N) + \Theta(1) + \Theta(N) = \Theta(N)$$

This linear time complexity is optimal, as any algorithm solving this problem must read all $N$ elements at least once, establishing a lower bound of $\Omega(N)$.

### 3.2. Space Complexity
The algorithm operates by updating a fixed set of state variables in-place:
$$\mathcal{S} = \{ \mathbf{S}, \boldsymbol{\delta}, \mathbf{a}, \mathbf{b} \} \subset \mathcal{V}^4$$

* **Auxiliary Space**: The size of the state space $|\mathcal{S}|$ is independent of the input size $N$. The partitioning of $A$ into $A_0$ and $A_1$ is performed implicitly and on-the-fly without allocating physical memory for the sub-sequences. Thus, the auxiliary space complexity is:
  $$S_{\text{aux}}(N) = \Theta(1)$$
* **Total Space**: Including the read-only input sequence $A$, the total space complexity is:
  $$S_{\text{total}}(N) = \Theta(N)$$