# Formal Mathematical Specification: Swap Odd and Even Bits

## 1. Definitions and Notation

Let $W \in 2\mathbb{N}$ denote the word size of the machine representation (typically $W = 32$ or $W = 64$). We define the domain of $W$-bit unsigned integers as the ring of integers modulo $2^W$, denoted by $\mathbb{Z}_{2^W}$. 

Any element $x \in \mathbb{Z}_{2^W}$ can be uniquely decomposed into its binary representation:
$$x = \sum_{i=0}^{W-1} b_i 2^i$$
where $b_i \in \mathbb{B} = \{0, 1\}$ for all $i \in I = \{0, 1, \dots, W-1\}$. We denote the bit-vector representation of $x$ as $\mathbf{b} = (b_{W-1}, b_{W-2}, \dots, b_1, b_0) \in \mathbb{B}^W$, using the standard **LSB-0 indexing convention** where the Least Significant Bit (LSB) is at index $0$.

We partition the index set $I$ into two disjoint subsets representing even and odd bit positions:
- **Even Indices:** $I_e = \{2k \mid 0 \le k < \frac{W}{2}\}$
- **Odd Indices:** $I_o = \{2k + 1 \mid 0 \le k < \frac{W}{2}\}$

Clearly, $I = I_e \cup I_o$ and $I_e \cap I_o = \emptyset$.

### The Swapping Permutation
The objective of the algorithm is to apply a permutation $\pi: I \to I$ to the bit indices of $x$. The permutation $\pi$ is defined as:
$$\pi(i) = \begin{cases} 
i + 1 & \text{if } i \in I_e \\ 
i - 1 & \text{if } i \in I_o 
\end{cases}$$

Equivalently, using the bitwise exclusive-OR (XOR) operator $\oplus$:
$$\pi(i) = i \oplus 1$$

The target function $f: \mathbb{Z}_{2^W} \to \mathbb{Z}_{2^W}$ is defined as:
$$f(x) = \sum_{i=0}^{W-1} b_{\pi(i)} 2^i$$

---

## 2. Algebraic Characterization

To implement $f(x)$ efficiently in $O(1)$ time, we express the bit-permutation using bitwise algebraic operators over the ring $\mathbb{Z}_{2^W}$.

### Bitwise Operators
For any $u, v \in \mathbb{Z}_{2^W}$ with binary representations $u = \sum u_i 2^i$ and $v = \sum v_i 2^i$:
1. **Bitwise AND ($\wedge$):** 
   $$u \wedge v = \sum_{i=0}^{W-1} (u_i \cdot v_i) 2^i$$
2. **Bitwise OR ($\vee$):** 
   $$u \vee v = \sum_{i=0}^{W-1} (u_i + v_i - u_i \cdot v_i) 2^i$$
3. **Logical Left Shift by 1 ($\ll 1$):** 
   $$u \ll 1 = (u \cdot 2) \pmod{2^W} = \sum_{i=1}^{W-1} u_{i-1} 2^i$$
4. **Logical Right Shift by 1 ($\gg 1$):** 
   $$u \gg 1 = \lfloor u / 2 \rfloor = \sum_{i=0}^{W-2} u_{i+1} 2^i$$

### Bitmask Definitions
We define two constant masks, $M_e$ and $M_o$, to isolate the even and odd bits respectively:
- **Even Mask ($M_e$):**
  $$M_e = \sum_{i \in I_e} 2^i = \sum_{k=0}^{\frac{W}{2}-1} 2^{2k}$$
  For $W = 32$, $M_e = \text{0x55555555}_{16}$.
  
- **Odd Mask ($M_o$):**
  $$M_o = \sum_{i \in I_o} 2^i = \sum_{k=0}^{\frac{W}{2}-1} 2^{2k+1}$$
  For $W = 32$, $M_o = \text{0xAAAAAAAA}_{16}$.

Note that $M_e \wedge M_o = 0$ and $M_e \vee M_o = 2^W - 1$.

### Theorem (Correctness of the Algebraic Formulation)
The target function $f(x)$ can be computed via the following algebraic identity:
$$f(x) = ((x \wedge M_e) \ll 1) \vee ((x \wedge M_o) \gg 1)$$

#### Proof:
Let $T_1 = (x \wedge M_e) \ll 1$ and $T_2 = (x \wedge M_o) \gg 1$. We analyze the bitwise components of $T_1$ and $T_2$.

1. **Analysis of $T_1$:**
   The term $x \wedge M_e$ isolates the even bits of $x$:
   $$x \wedge M_e = \sum_{k=0}^{\frac{W}{2}-1} b_{2k} 2^{2k}$$
   Applying the logical left shift:
   $$T_1 = (x \wedge M_e) \ll 1 = \sum_{k=0}^{\frac{W}{2}-1} b_{2k} 2^{2k+1}$$
   Thus, the $i$-th bit of $T_1$, denoted $(T_1)_i$, is:
   $$(T_1)_i = \begin{cases} 
   b_{i-1} & \text{if } i \in I_o \\ 
   0 & \text{if } i \in I_e 
   \end{cases}$$

2. **Analysis of $T_2$:**
   The term $x \wedge M_o$ isolates the odd bits of $x$:
   $$x \wedge M_o = \sum_{k=0}^{\frac{W}{2}-1} b_{2k+1} 2^{2k+1}$$
   Applying the logical right shift:
   $$T_2 = (x \wedge M_o) \gg 1 = \sum_{k=0}^{\frac{W}{2}-1} b_{2k+1} 2^{2k}$$
   Thus, the $i$-th bit of $T_2$, denoted $(T_2)_i$, is:
   $$(T_2)_i = \begin{cases} 
   b_{i+1} & \text{if } i \in I_e \\ 
   0 & \text{if } i \in I_o 
   \end{cases}$$

3. **Synthesis via Bitwise OR:**
   Let $y = T_1 \vee T_2$. Since $(T_1)_i \cdot (T_2)_i = 0$ for all $i \in I$, the bitwise OR simplifies to direct addition of the bit values:
   $$y_i = (T_1)_i + (T_2)_i$$
   
   We evaluate $y_i$ for both index partitions:
   - If $i \in I_e$:
     $$y_i = 0 + b_{i+1} = b_{i+1} = b_{\pi(i)}$$
   - If $i \in I_o$:
     $$y_i = b_{i-1} + 0 = b_{i-1} = b_{\pi(i)}$$

   Therefore, for all $i \in I$, $y_i = b_{\pi(i)}$, which implies:
   $$y = \sum_{i=0}^{W-1} b_{\pi(i)} 2^i = f(x)$$
   $\blacksquare$

### Pedagogical Note on Indexing Conventions
If an architecture or programming language utilizes the **MSB-0 indexing convention** (where index $0$ is the Most Significant Bit), the direction of the shifts is inverted relative to the index arithmetic. Under MSB-0:
- Even bits must be shifted *right* to reach odd positions: $(x \wedge M_e) \gg 1$.
- Odd bits must be shifted *left* to reach even positions: $(x \wedge M_o) \ll 1$.

This explains why some implementations swap the shift directions depending on the underlying bit-ordering model.

---

## 3. Complexity Analysis

### Time Complexity
Let $W$ be the word size of the processor. Under the **Word-RAM model of computation**, any primitive bitwise operation (AND, OR, logical shifts) on a $W$-bit register is executed in $O(1)$ time.

The algorithm executes a strictly bounded sequence of operations:
1. Two bitwise AND operations: $a = x \wedge M_e$ and $b = x \wedge M_o$.
2. One logical left shift: $c = a \ll 1$.
3. One logical right shift: $d = b \gg 1$.
4. One bitwise OR operation: $y = c \vee d$.

The total number of operations is exactly $5$. Thus, the time complexity is:
$$T(W) = \Theta(1)$$

In the bit-complexity model (where operations are analyzed at the individual bit level), the complexity is $\Theta(W)$ since each bitwise operation requires processing $W$ bits.

### Space Complexity
The algorithm operates entirely in-place within the processor registers. 
- **Auxiliary Space:** The algorithm requires storage for a constant number of intermediate variables ($T_1, T_2$) and the masks ($M_e, M_o$). This requires $O(1)$ auxiliary registers.
- **Total Space:** The total space complexity, including the input $x$, is:
$$S(W) = \Theta(1) \text{ auxiliary registers (or } \Theta(W) \text{ bits)}$$