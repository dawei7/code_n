# Formal Mathematical Specification: Multiply Two Integers Without Multiplication (Russian Peasant)

## 1. Definitions and Notation

Let $a, b \in \mathbb{Z}$ be the two integer inputs to the algorithm.
The algorithm computes an integer $P \in \mathbb{Z}$ such that $P = a \cdot b$.

The state of the algorithm at any point is defined by a tuple of variables $(s, x, y, R)$, where:
*   $s \in \{0, 1\}$ is a boolean flag indicating the sign of the final product. $s=1$ if the product should be negative, $s=0$ otherwise.
*   $x \in \mathbb{N}_0$ is the current multiplicand, representing a scaled version of $|a|$.
*   $y \in \mathbb{N}_0$ is the current multiplier, representing a progressively reduced version of $|b|$.
*   $R \in \mathbb{N}_0$ is the accumulated partial product.

**Initial State:**
The algorithm initializes its state variables based on the inputs $a$ and $b$:
*   $s_0 = 1$ if $(a < 0 \land b \ge 0) \lor (a \ge 0 \land b < 0)$, otherwise $s_0 = 0$. This can be expressed as $s_0 = (a < 0) \oplus (b < 0)$.
*   $x_0 = |a|$.
*   $y_0 = |b|$.
*   $R_0 = 0$.

**Operations:**
The algorithm employs the following operations:
*   $|z|$: Absolute value of an integer $z$.
*   $z \pmod 2$: The remainder when $z$ is divided by 2 (equivalent to bitwise AND with 1, $z \text{ & } 1$).
*   $z \leftarrow z + w$: Integer addition.
*   $z \leftarrow 2z$: Left bit shift (equivalent to $z \text{ << } 1$).
*   $z \leftarrow \lfloor z/2 \rfloor$: Integer division by 2 (equivalent to right bit shift, $z \text{ >> } 1$).

## 2. Algebraic Characterization

The algorithm computes the product $P' = |a| \cdot |b|$ by iteratively decomposing the multiplier $y$ into its binary representation. Let $y_0 = \sum_{i=0}^{m-1} c_i 2^i$, where $c_i \in \{0, 1\}$ are the binary digits of $y_0$ and $m = \lfloor \log_2 y_0 \rfloor + 1$ (if $y_0 > 0$). The target product $P'$ can be expressed as:
$$P' = x_0 \cdot y_0 = x_0 \cdot \sum_{i=0}^{m-1} c_i 2^i = \sum_{i=0}^{m-1} (x_0 \cdot c_i \cdot 2^i)$$

The algorithm maintains a loop invariant that ensures correctness. Let $(x_k, y_k, R_k)$ denote the state variables at the beginning of iteration $k$ of the main loop.

**Loop Invariant:**
At the beginning of each iteration $k$ (before the loop condition $y_k > 0$ is evaluated), the following invariant holds:
$$P' = x_k \cdot y_k + R_k$$

**Proof of Invariant:**
*   **Base Case (k=0):**
    From the initial state, $x_0 = |a|$, $y_0 = |b|$, and $R_0 = 0$.
    Substituting these into the invariant: $x_0 \cdot y_0 + R_0 = |a| \cdot |b| + 0 = P'$.
    The invariant holds for $k=0$.

*   **Inductive Step:**
    Assume the invariant holds at the beginning of iteration $k$: $P' = x_k \cdot y_k + R_k$.
    We need to show that it holds at the beginning of iteration $k+1$, i.e., $P' = x_{k+1} \cdot y_{k+1} + R_{k+1}$.

    Inside the loop, the updates to the state variables are as follows:
    1.  If $y_k \pmod 2 = 1$ (i.e., the least significant bit of $y_k$ is 1):
        $R_{k+1}' = R_k + x_k$.
    2.  Else ($y_k \pmod 2 = 0$):
        $R_{k+1}' = R_k$.
    3.  $x_{k+1} = 2x_k$.
    4.  $y_{k+1} = \lfloor y_k/2 \rfloor$.

    Let $y_k = 2q + c_0$, where $c_0 = y_k \pmod 2$. Then $y_{k+1} = q = (y_k - c_0)/2$.
    The update to $R$ can be compactly written as $R_{k+1}' = R_k + c_0 x_k$.

    Now, substitute these updated values into the invariant for $k+1$:
    $$x_{k+1} \cdot y_{k+1} + R_{k+1}' = (2x_k) \cdot \left(\frac{y_k - c_0}{2}\right) + (R_k + c_0 x_k)$$
    $$= x_k (y_k - c_0) + R_k + c_0 x_k$$
    $$= x_k y_k - c_0 x_k + R_k + c_0 x_k$$
    $$= x_k y_k + R_k$$
    By the inductive hypothesis, $x_k y_k + R_k = P'$.
    Therefore, $x_{k+1} \cdot y_{k+1} + R_{k+1}' = P'$. The invariant holds for $k+1$.

**Termination:**
The loop terminates when $y_k = 0$. At this point, the invariant $P' = x_k \cdot y_k + R_k$ becomes $P' = x_k \cdot 0 + R_k = R_k$.
Thus, the variable $R_k$ holds the value of the absolute product $P'$.
The final result $P$ is then determined by applying the initial sign flag $s_0$:
$$P = (-1)^{s_0} \cdot R_k$$
This completes the proof of correctness.

## 3. Complexity Analysis

### Time Complexity

The algorithm's primary computational work is performed within the `while` loop.
Let $y_0 = |b|$ be the initial value of the multiplier (or $\min(|a|, |b|)$ if optimized).
In each iteration of the loop, the value of $y$ is updated by $y \leftarrow \lfloor y/2 \rfloor$. This operation effectively removes the least significant bit of $y$.
The loop continues as long as $y > 0$.
The number of iterations is precisely the number of bits required to represent $y_0$ (excluding leading zeros), or $\lfloor \log_2 y_0 \rfloor + 1$ for $y_0 > 0$. If $y_0 = 0$, the loop executes 0 times.
Thus, the number of iterations is proportional to $\log_2 y_0$.

Within each iteration, the operations performed are:
*   Bitwise AND (`y & 1`): $O(1)$
*   Addition (`result += x`): $O(1)$
*   Left bit shift (`x <<= 1`): $O(1)$
*   Right bit shift (`y >>= 1`): $O(1)$

These operations are considered constant time, $O(1)$, under the standard assumption of fixed-width integer types (e.g., 32-bit or 64-bit integers).
Therefore, the total time complexity is the product of the number of iterations and the time per iteration:
$$T(y_0) = (\lfloor \log_2 y_0 \rfloor + 1) \cdot O(1) = O(\log y_0)$$
If the algorithm is optimized to use the smaller of $|a|$ and $|b|$ as the multiplier, let $N = \min(|a|, |b|)$. The time complexity becomes $O(\log N)$.

### Space Complexity

The algorithm utilizes a fixed number of variables: `negative` ($s$), `x`, `y`, and `result` ($R$).
These variables store integer values. Assuming fixed-width integer types, the memory required for each variable is constant, regardless of the magnitude of the input integers $a$ and $b$.
No auxiliary data structures (like arrays, lists, or recursive call stacks) are used that would grow with the input size.
Therefore, the auxiliary space complexity is $O(1)$.
The total space complexity is also $O(1)$.