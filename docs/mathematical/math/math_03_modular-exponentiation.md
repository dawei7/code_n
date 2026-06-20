# Formal Mathematical Specification: Modular Exponentiation (Binary Exponentiation)

## 1. Definitions and Notation

Let the base $b \in \mathbb{Z}$, the exponent $e \in \mathbb{N}_0$ (where $\mathbb{N}_0 = \{0, 1, 2, \dots\}$), and the modulus $m \in \mathbb{Z}^+$. We define the modular exponentiation function $f: \mathbb{Z} \times \mathbb{N}_0 \times \mathbb{Z}^+ \to \mathbb{Z}_{m}$ as:
$$f(b, e, m) \equiv b^e \pmod m$$

The state space $\mathcal{S}$ of the algorithm is defined by the triplet $(r_i, b_i, e_i)$, where:
- $r_i \in \mathbb{Z}_m$ is the accumulated result at iteration $i$.
- $b_i \in \mathbb{Z}_m$ is the current base raised to the power of $2^i$.
- $e_i \in \mathbb{N}_0$ is the remaining exponent to be processed.

The binary representation of the exponent $e$ is given by the sequence of bits $(a_k, a_{k-1}, \dots, a_0)$ such that:
$$e = \sum_{i=0}^{k} a_i 2^i, \quad a_i \in \{0, 1\}$$
where $k = \lfloor \log_2 e \rfloor$.

## 2. Algebraic Characterization

The algorithm relies on the property of exponentiation by squaring, derived from the binary representation of $e$. We define the state transition $(r_{i+1}, b_{i+1}, e_{i+1})$ from $(r_i, b_i, e_i)$ as follows:

1. **Base Update:** $b_{i+1} \equiv b_i^2 \pmod m$
2. **Exponent Update:** $e_{i+1} = \lfloor e_i / 2 \rfloor$
3. **Result Update:** 
   $$r_{i+1} \equiv \begin{cases} r_i \cdot b_i \pmod m & \text{if } e_i \equiv 1 \pmod 2 \\ r_i \pmod m & \text{if } e_i \equiv 0 \pmod 2 \end{cases}$$

**Loop Invariant:**
At the start of each iteration $i$ (where $i$ denotes the number of bits processed), the following invariant holds:
$$r_i \cdot b_i^{e_i} \equiv b^e \pmod m$$
Base case: For $i=0$, $r_0 = 1$, $b_0 = b \pmod m$, and $e_0 = e$. Thus, $1 \cdot b^e \equiv b^e \pmod m$.
Termination: When $e_k = 0$, the invariant yields $r_k \cdot b_k^0 \equiv r_k \equiv b^e \pmod m$, confirming the correctness of the result.

The modular property utilized is the homomorphism of the multiplication operation over the ring $\mathbb{Z}_m$:
$$(x \cdot y) \pmod m = ((x \pmod m) \cdot (y \pmod m)) \pmod m$$
This ensures that all intermediate products $r_i \cdot b_i$ and $b_i^2$ remain within the range $[0, m-1]$, preventing arithmetic overflow.

## 3. Complexity Analysis

### Time Complexity
The algorithm terminates when the exponent $e$ reaches 0. In each iteration, the exponent is transformed via the right-shift operation $e \leftarrow \lfloor e/2 \rfloor$. 

Let $T(e)$ be the number of iterations required for an exponent $e$. The recurrence relation is:
$$T(e) = 1 + T(\lfloor e/2 \rfloor), \quad T(0) = 0$$
By the Master Theorem (or simple expansion), the number of iterations is exactly $\lfloor \log_2 e \rfloor + 1$. Since each iteration involves a constant number of arithmetic operations (multiplication, modulo, bitwise shift, and comparison), the total time complexity is:
$$T(e) = O(\log e)$$

### Space Complexity
The algorithm maintains a fixed number of variables $(r, b, e, m)$ regardless of the magnitude of the input. No auxiliary data structures (such as arrays or recursion stacks) are utilized. 

Let $S(m)$ be the space required to store the variables. Assuming the word size of the machine is sufficient to hold the intermediate products (typically $O(\log m)$ bits), the auxiliary space complexity is:
$$S = O(1)$$
This is strictly constant space, as the memory footprint does not scale with the magnitude of $e$ or $b$.