# Formal Mathematical Specification: Power of Two Check

## 1. Definitions and Notation

To establish a rigorous foundation for the algorithm, we define the mathematical domains, representation schemes, and operators used to characterize the input, output, and state space.

### 1.1 Mathematical Domains and Sets
* Let $\mathbb{Z}$ denote the set of all integers.
* Let $\mathbb{Z}^+$ denote the set of strictly positive integers, $\{n \in \mathbb{Z} \mid n > 0\}$.
* Let $\mathbb{N}_0$ denote the set of non-negative integers, $\{0, 1, 2, \dots\}$.
* Let $\mathbb{B} = \{\text{True}, \text{False}\}$ denote the boolean domain.
* Let $\mathcal{P}_2 \subset \mathbb{Z}^+$ be the set of all powers of two, defined formally as:
  $$\mathcal{P}_2 = \{ 2^x \mid x \in \mathbb{N}_0 \}$$

### 1.2 Binary Representation
For any positive integer $n \in \mathbb{Z}^+$, there exists a unique binary representation of the form:
$$n = \sum_{i=0}^{k} b_i 2^i$$
where $k = \lfloor \log_2 n \rfloor$, $b_i \in \{0, 1\}$ for all $0 \le i \le k$, and the most significant bit $b_k = 1$. 

We denote the sequence of binary coefficients of $n$ as a bit-vector $\mathbf{b}(n) = (b_k, b_{k-1}, \dots, b_0)_2$.

### 1.3 Bitwise Operators
Let $\&$ denote the bitwise AND operator. For any two non-negative integers $u, v \in \mathbb{N}_0$ with binary expansions $u = \sum_{i=0}^{\infty} u_i 2^i$ and $v = \sum_{i=0}^{\infty} v_i 2^i$ (where $u_i, v_i \in \{0, 1\}$ and only finitely many coefficients are non-zero), the bitwise AND operation is defined algebraically as:
$$u \ \& \ v = \sum_{i=0}^{\infty} (u_i \cdot v_i) 2^i$$
where $u_i \cdot v_i$ represents standard multiplication in $\{0, 1\}$, equivalent to the logical conjunction $u_i \land v_i$.

---

## 2. Algebraic Characterization

The algorithm evaluates a decision function $f: \mathbb{Z} \to \mathbb{B}$ defined by:
$$f(n) = (n > 0) \land \big( (n \ \& \ (n - 1)) == 0 \big)$$

### Theorem 1 (Correctness of the Power of Two Check)
For any integer $n \in \mathbb{Z}$, 
$$f(n) = \text{True} \iff n \in \mathcal{P}_2$$

### Proof
We prove this equivalence by partitioning the domain $\mathbb{Z}$ into two cases: $n \le 0$ and $n > 0$.

#### Case 1: $n \le 0$
* **Left-to-Right ($\implies$):** If $n \le 0$, the clause $(n > 0)$ evaluates to $\text{False}$. By the definition of logical conjunction, $f(n) = \text{False}$.
* **Right-to-Left ($\impliedby$):** By definition, $\mathcal{P}_2 = \{2^x \mid x \in \mathbb{N}_0\}$. Since $2^x > 0$ for all $x \in \mathbb{R}$, it follows that $\mathcal{P}_2 \subset \mathbb{Z}^+$. Thus, if $n \le 0$, then $n \notin \mathcal{P}_2$.
* Hence, the theorem holds vacuously for all $n \le 0$.

#### Case 2: $n > 0$
For $n \in \mathbb{Z}^+$, the clause $(n > 0)$ evaluates to $\text{True}$. The decision function simplifies to:
$$f(n) = \text{True} \iff (n \ \& \ (n - 1)) = 0$$
We must show that for any $n \in \mathbb{Z}^+$, $(n \ \& \ (n - 1)) = 0 \iff n \in \mathcal{P}_2$.

Let the unique binary representation of $n$ be:
$$n = \sum_{i=0}^{k} b_i 2^i \quad \text{with } b_k = 1$$
Let $j$ be the index of the least significant set bit (the rightmost $1$-bit) of $n$:
$$j = \min \{ i \in \mathbb{N}_0 \mid b_i = 1 \}$$
By definition of $j$, we have $b_j = 1$, and $b_i = 0$ for all $0 \le i < j$. We can decompose $n$ as:
$$n = \sum_{i=j+1}^{k} b_i 2^i + 2^j$$

Now, consider the algebraic representation of $n - 1$:
$$n - 1 = \sum_{i=j+1}^{k} b_i 2^i + 2^j - 1$$
Using the geometric series identity $2^j - 1 = \sum_{i=0}^{j-1} 2^i$, we substitute to obtain:
$$n - 1 = \sum_{i=j+1}^{k} b_i 2^i + \sum_{i=0}^{j-1} 1 \cdot 2^i$$

Let $c_i(x)$ denote the $i$-th binary coefficient of an integer $x$. From our expressions for $n$ and $n-1$, we extract their respective coefficients:
$$c_i(n) = \begin{cases} 
b_i & \text{if } i > j \\ 
1 & \text{if } i = j \\ 
0 & \text{if } i < j 
\end{cases}$$

$$c_i(n - 1) = \begin{cases} 
b_i & \text{if } i > j \\ 
0 & \text{if } i = j \\ 
1 & \text{if } i < j 
\end{cases}$$

Applying the definition of the bitwise AND operator, the coefficients of $n \ \& \ (n - 1)$ are given by:
$$c_i(n \ \& \ (n - 1)) = c_i(n) \cdot c_i(n - 1)$$

Evaluating this product for each interval of $i$:
1. For $i > j$: $c_i(n \ \& \ (n - 1)) = b_i \cdot b_i = b_i$ (since $b_i \in \{0, 1\}$).
2. For $i = j$: $c_i(n \ \& \ (n - 1)) = 1 \cdot 0 = 0$.
3. For $i < j$: $c_i(n \ \& \ (n - 1)) = 0 \cdot 1 = 0$.

Reconstructing the integer value of the bitwise AND operation yields:
$$n \ \& \ (n - 1) = \sum_{i=j+1}^{k} b_i 2^i$$

We now evaluate the condition under which this value equals $0$:
$$n \ \& \ (n - 1) = 0 \iff \sum_{i=j+1}^{k} b_i 2^i = 0$$
Because $2^i > 0$ and $b_i \ge 0$ for all $i$, the sum is zero if and only if:
$$b_i = 0 \quad \forall i \in \{j+1, \dots, k\}$$

This condition implies that $j$ is the only index for which $b_i = 1$. Thus, $k = j$, and the binary expansion of $n$ collapses to:
$$n = 2^j$$
Since $j \in \mathbb{N}_0$, this is equivalent to stating that $n \in \mathcal{P}_2$. 

Conversely, if $n \notin \mathcal{P}_2$, there must exist at least one index $m > j$ such that $b_m = 1$. This guarantees that:
$$\sum_{i=j+1}^{k} b_i 2^i \ge 2^m > 0$$
which implies $n \ \& \ (n - 1) \neq 0$.

This completes the proof. $\blacksquare$

---

## 3. Complexity Analysis

### 3.1 Time Complexity
To analyze the time complexity formally, we define our execution model under the **Word RAM Model of Computation**. In this model, the CPU operates on words of size $w$ bits, where $w \ge \log_2 n$. Basic arithmetic operations (addition, subtraction) and bitwise operations (AND, comparisons) on $w$-bit words are executed in $O(1)$ time.

Let $T(n)$ be the primitive operation count for input $n$:
1. **Relational Comparison ($n > 0$):** Requires 1 comparison operation.
2. **Arithmetic Subtraction ($n - 1$):** Requires 1 subtraction operation.
3. **Bitwise Conjunction ($n \ \& \ (n - 1)$):** Requires 1 bitwise AND operation.
4. **Equality Comparison ($== 0$):** Requires 1 comparison operation.
5. **Logical Conjunction ($\land$):** Requires at most 1 logical operation (with short-circuit evaluation).

Thus, the total number of operations is bounded by a constant $C \le 5$.
$$T(n) \le C \cdot \tau = \Theta(1)$$
where $\tau$ is the clock cycle cost of a word-level instruction.

#### Arbitrary-Precision Generalization
If $n$ is an arbitrary-precision integer represented using $L = \Theta(\log n)$ bits:
* Subtraction $n - 1$ requires $\Theta(L)$ bit operations in the worst case.
* Bitwise AND $n \ \& \ (n - 1)$ requires $\Theta(L)$ bit operations.
* Under this bit-complexity model, the time complexity is $\Theta(L) = \Theta(\log n)$. However, for standard hardware-supported fixed-width integers (e.g., 32-bit or 64-bit), the complexity remains strictly $\Theta(1)$.

### 3.2 Space Complexity
Let $S(n)$ denote the total space complexity of the algorithm, partitioned into input space, auxiliary space, and stack space.

* **Input Space:** The algorithm takes a single integer $n$ represented in a single machine word of size $w$ bits. Thus, input space is $O(1)$ words.
* **Auxiliary Space ($A(n)$):** The algorithm does not allocate dynamic memory, nor does it scale its variables with the input size. It requires only a constant number of registers to store intermediate states:
  $$\mathcal{S}_{\text{intermediate}} = \{ n - 1, \ n \ \& \ (n-1), \ \text{boolean flags} \}$$
  This requires $O(1)$ auxiliary memory.
* **Call Stack Space:** The execution is non-recursive, yielding a call stack depth of $O(1)$.

Therefore, the auxiliary space complexity is:
$$A(n) = \Theta(1)$$