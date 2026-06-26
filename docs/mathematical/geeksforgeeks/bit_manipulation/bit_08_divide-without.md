# Formal Mathematical Specification: Divide Two Integers Without Division

## 1. Definitions and Notation

This section defines the mathematical entities, their domains, and the notation used throughout the specification.

*   **Input Domain:**
    *   Let $D \in \mathbb{Z}$ denote the dividend.
    *   Let $S \in \mathbb{Z}$ denote the divisor.
    *   The domain for both $D$ and $S$ is the set of 32-bit signed integers, denoted by $\mathcal{I} = [-2^{31}, 2^{31}-1]$.
    *   **Constraint:** $S \neq 0$.
*   **Output Domain:**
    *   Let $Q \in \mathbb{Z}$ denote the quotient.
    *   The output $Q$ must also be within $\mathcal{I}$, with a specific overflow handling rule.
*   **Constants:**
    *   $\text{BIT\_WIDTH} = 32$: The number of bits used for integer representation.
    *   $\text{MAX\_SIGNED\_INT} = 2^{31}-1$: The maximum value for a 32-bit signed integer.
    *   $\text{MIN\_SIGNED\_INT} = -2^{31}$: The minimum value for a 32-bit signed integer.
*   **Internal State Variables:**
    *   $N \in \{\text{true}, \text{false}\}$: A boolean flag indicating if the final quotient should be negative.
    *   $a \in \mathbb{N}_0$: The current absolute value of the remaining dividend.
    *   $b \in \mathbb{N}_0$: The absolute value of the divisor.
    *   $q \in \mathbb{N}_0$: The accumulated absolute quotient.
    *   $p \in \mathbb{N}_0$: A bit-shift power counter, representing $2^p$.

## 2. Algebraic Characterization

The algorithm computes the integer division $D/S$ (truncating towards zero) by first determining the sign of the result, then calculating the absolute value of the quotient using bit shifts and subtractions, and finally applying the correct sign and handling potential overflow.

**2.1. Preprocessing and Sign Determination:**
1.  **Sign Determination:** A boolean flag $N$ is set to $\text{true}$ if $D$ and $S$ have different signs, and $\text{false}$ otherwise. This can be formally expressed as:
    $N = (D < 0) \oplus (S < 0)$, where $\oplus$ denotes the exclusive OR operation.
2.  **Absolute Value Initialization:** The algorithm operates on the absolute values of the dividend and divisor to simplify the core division logic.
    $a_0 = |D|$
    $b_0 = |S|$
    *Note: In a strict 32-bit environment (e.g., C/Java), computing $|-2^{31}|$ would result in an overflow. The Python implementation's `abs()` handles this by implicitly using larger integer types. For this specification, we assume $|D|$ is well-defined and fits within a sufficiently large unsigned integer type for intermediate calculations.*
3.  **Quotient Accumulator Initialization:**
    $q_0 = 0$
4.  **Power Counter Initialization:**
    $p_{init} = \text{BIT\_WIDTH}-1 = 31$.

**2.2. Determining Initial Maximum Power ($P_{max}$):**
The algorithm first identifies the largest integer $P_{max}$ such that $b_0 \cdot 2^{P_{max}} \le a_0$. This is achieved by iteratively decrementing $p$ from $p_{init}$:
Let $p_{curr} \leftarrow p_{init}$.
While $b_0 \cdot 2^{p_{curr}} > a_0$:
  $p_{curr} \leftarrow p_{curr} - 1$.
The value of $p_{curr}$ upon termination of this loop is $P_{max}$. If $b_0 > a_0$, then $P_{max}$ will be less than $0$, correctly leading to an absolute quotient of $0$.

**2.3. Iterative Subtraction and Quotient Accumulation:**
The core division logic iteratively subtracts multiples of $b_0$ (specifically, $b_0 \cdot 2^p$) from the remaining dividend $a$ and accumulates the corresponding powers of 2 into $q$.
Let $a^{(p)}$ and $q^{(p)}$ denote the values of $a$ and $q$ at the beginning of an iteration where the power counter is $p$.
The loop proceeds for $p$ from $P_{max}$ down to $0$:
For $p \in \{P_{max}, P_{max}-1, \dots, 0\}$:
  If $b_0 \cdot 2^p \le a^{(p)}$:
    $a^{(p-1)} = a^{(p)} - (b_0 \cdot 2^p)$
    $q^{(p-1)} = q^{(p)} + 2^p$
  Else:
    $a^{(p-1)} = a^{(p)}$
    $q^{(p-1)} = q^{(p)}$
The final absolute quotient is $Q_{abs} = q^{(-1)}$.

**Loop Invariant for Iterative Subtraction Loop:**
At the beginning of each iteration, for a given power $p \in \{P_{max}, \dots, 0\}$, the following conditions hold:
1.  **Decomposition of Dividend:** The initial absolute dividend $a_0$ can be expressed as the sum of the accumulated quotient times the divisor, the current remainder, and the contribution from bits of the quotient yet to be determined:
    $a_0 = (q^{(p)} + \sum_{j=p+1}^{P_{max}} \delta_j \cdot 2^j) \cdot b_0 + a^{(p)}$,
    where $\delta_j \in \{0,1\}$ are the bits of the quotient for powers $j > p$.
2.  **Remainder Bound:** The current remainder $a^{(p)}$ is non-negative and strictly less than the next potential subtraction term $b_0 \cdot 2^{p+1}$:
    $0 \le a^{(p)} < b_0 \cdot 2^{p+1}$.
3.  **Quotient Accumulation:** The accumulated quotient $q^{(p)}$ represents the sum of powers of 2 corresponding to bits of the quotient already determined for powers greater than $p$:
    $q^{(p)} = \sum_{j=p+1}^{P_{max}} \delta_j \cdot 2^j$.

**Termination:**
The loop terminates when $p < 0$. At this point, $p=-1$.
From Invariant 1: $a_0 = Q_{abs}^{(-1)} \cdot b_0 + a^{(-1)}$, where $Q_{abs}^{(-1)}$ is the final accumulated quotient.
From Invariant 3: $Q_{abs}^{(-1)} = \sum_{j=0}^{P_{max}} \delta_j \cdot 2^j$. This is the final absolute quotient, $Q_{abs}$.
From Invariant 2: $0 \le a^{(-1)} < b_0 \cdot 2^0 = b_0$. This confirms that $a^{(-1)}$ is the remainder $R_{abs}$ such that $0 \le R_{abs} < b_0$.
Therefore, $Q_{abs} = \lfloor a_0 / b_0 \rfloor$ and $R_{abs} = a_0 \pmod{b_0}$.

**2.4. Final Result Construction and Overflow Handling:**
Let $Q_{abs}$ be the final value of $q$ obtained from the iterative subtraction.
The raw quotient $Q_{raw}$ is determined by applying the sign:
$Q_{raw} = \begin{cases} -Q_{abs} & \text{if } N = \text{true} \\ Q_{abs} & \text{if } N = \text{false} \end{cases}$
Finally, the algorithm must adhere to the 32-bit signed integer range constraint. The final output $Q_{final}$ is defined as:
$Q_{final} = \begin{cases} \text{MAX\_SIGNED\_INT} & \text{if } Q_{raw} > \text{MAX\_SIGNED\_INT} \\ Q_{raw} & \text{otherwise} \end{cases}$
This handles the specific case where $D = \text{MIN\_SIGNED\_INT}$ and $S = -1$, which would yield $Q_{raw} = 2^{31}$, exceeding $\text{MAX\_SIGNED\_INT}$.

## 3. Complexity Analysis

**3.1. Time Complexity:**
Let $\text{BIT\_WIDTH}$ be the number of bits representing the integers (e.g., 32).
Let $Q_{abs} = \lfloor |D|/|S| \rfloor$ be the absolute value of the quotient.

1.  **Preprocessing:** Operations for sign determination and absolute value initialization are constant time, $O(1)$.
2.  **Determining Initial Maximum Power:** The first `while` loop iterates, decrementing $p$ from $\text{BIT\_WIDTH}-1$ until $b_0 \cdot 2^p \le a_0$. In the worst case, $p$ decreases from $\text{BIT\_WIDTH}-1$ down to approximately $\lfloor \log_2(a_0/b_0) \rfloor$. The number of iterations is bounded by $\text{BIT\_WIDTH}$. Thus, this phase takes $O(\text{BIT\_WIDTH})$ time.
3.  **Iterative Subtraction and Quotient Accumulation:** The second `while` loop iterates $p$ from $P_{max}$ down to $0$. The value of $P_{max}$ is at most $\text{BIT\_WIDTH}-1$. Therefore, this loop performs at most $\text{BIT\_WIDTH}$ iterations. Each iteration involves a bit shift, a comparison, a subtraction, and a bitwise OR operation. For fixed-width integers, these are all $O(1)$ operations. Thus, this phase also takes $O(\text{BIT\_WIDTH})$ time.
4.  **Final Result Construction:** Applying the sign and checking for overflow are $O(1)$ operations.

Combining these, the total time complexity is $O(1) + O(\text{BIT\_WIDTH}) + O(\text{BIT\_WIDTH}) + O(1) = O(\text{BIT\_WIDTH})$.
Since $\text{BIT\_WIDTH}$ is a constant (e.g., 32 for 32-bit integers), the time complexity can be considered $O(1)$ in terms of the machine's word size.
More precisely, the number of iterations in the main loop is directly related to the number of bits in the absolute quotient $Q_{abs}$. The number of bits in $Q_{abs}$ is $\lfloor \log_2 Q_{abs} \rfloor + 1$.
Therefore, the time complexity is $O(\log Q_{abs})$. Given that $Q_{abs} \le 2^{31}$, this is bounded by $O(\log 2^{31}) = O(31)$, which is constant.

**3.2. Space Complexity:**
The algorithm utilizes a fixed number of variables: $D, S, N, a, b, q, p$. Each of these variables stores a single integer value, whose size is bounded by the machine's word size (e.g., 32 bits). No auxiliary data structures (such as arrays, lists, or a recursion stack) are allocated whose memory footprint grows with the magnitude of the input integers.
Therefore, the auxiliary space complexity is $O(1)$. The total space complexity, including the space for inputs, is also $O(1)$.