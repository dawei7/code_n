# Formal Mathematical Specification: Modular Exponentiation

## 1. Definitions and Notation

Let the domain of the algorithm be defined by the triple $(x, y, p) \in \mathbb{Z}_{\ge 0} \times \mathbb{Z}_{\ge 0} \times \mathbb{Z}_{> 1}$. 
The objective is to compute the function $f: \mathbb{Z}_{\ge 0}^2 \times \mathbb{Z}_{> 1} \to \mathbb{Z}_p$, where $\mathbb{Z}_p = \{0, 1, \dots, p-1\}$, defined as:
$$f(x, y, p) \equiv x^y \pmod{p}$$

We define the state of the algorithm at iteration $i$ (where $i=0$ is the initialization) as a tuple $\mathcal{S}_i = (r_i, b_i, e_i)$, where:
*   $r_i \in \mathbb{Z}_p$ is the accumulated result.
*   $b_i \in \mathbb{Z}_p$ is the current base, representing $x^{2^i} \pmod{p}$.
*   $e_i \in \mathbb{Z}_{\ge 0}$ is the remaining exponent, where $e_i = \lfloor y / 2^i \rfloor$.

## 2. Algebraic Characterization

The correctness of the algorithm relies on the property of modular multiplication: for any $a, b, m \in \mathbb{Z}$, $(a \cdot b) \pmod{m} = [(a \pmod{m}) \cdot (b \pmod{m})] \pmod{m}$. 

We represent the exponent $y$ in its binary expansion: $y = \sum_{j=0}^{\lfloor \log_2 y \rfloor} d_j 2^j$, where $d_j \in \{0, 1\}$. By the laws of exponents:
$$x^y = x^{\sum d_j 2^j} = \prod_{j=0}^{\lfloor \log_2 y \rfloor} (x^{2^j})^{d_j}$$

Applying the modulo operator to the product:
$$x^y \pmod{p} = \left( \prod_{j=0}^{\lfloor \log_2 y \rfloor} (x^{2^j})^{d_j} \right) \pmod{p}$$

**Loop Invariant:**
At the start of each iteration $i$, the following invariant holds:
$$x^y \equiv r_i \cdot b_i^{e_i} \pmod{p}$$

**Transition Rules:**
Given $\mathcal{S}_i = (r_i, b_i, e_i)$, the state $\mathcal{S}_{i+1}$ is derived as follows:
1.  **Update Result:** If $e_i \equiv 1 \pmod{2}$, then $r_{i+1} = (r_i \cdot b_i) \pmod{p}$; otherwise $r_{i+1} = r_i$.
2.  **Update Base:** $b_{i+1} = (b_i^2) \pmod{p}$.
3.  **Update Exponent:** $e_{i+1} = \lfloor e_i / 2 \rfloor$.

The algorithm terminates at iteration $k = \lfloor \log_2 y \rfloor + 1$ when $e_k = 0$, yielding $r_k \equiv x^y \pmod{p}$.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs a sequence of operations governed by the binary representation of $y$. Let $L = \lfloor \log_2 y \rfloor + 1$ be the number of bits required to represent $y$. 
In each iteration $i \in \{0, 1, \dots, L-1\}$, the algorithm performs a constant number of arithmetic operations (multiplication, modulo, bitwise shift, and comparison). 

The total time complexity $T(y)$ is given by the summation:
$$T(y) = \sum_{i=0}^{L-1} \Theta(1) = \Theta(L) = \Theta(\log y)$$
Since each multiplication involves numbers bounded by $p$, assuming $p$ fits within a machine word, each multiplication is $O(1)$. Thus, the time complexity is $O(\log y)$.

### Space Complexity
The algorithm maintains a fixed set of variables $(r, b, e)$. Regardless of the magnitude of $y$ or $p$, the memory footprint is restricted to the storage of these three variables.
*   $r, b \in [0, p-1]$
*   $e \in [0, y]$

The auxiliary space required is $S = \Theta(1)$, as the memory usage does not scale with the input size $y$ or $p$ (assuming fixed-width integer representation). Thus, the space complexity is $O(1)$.