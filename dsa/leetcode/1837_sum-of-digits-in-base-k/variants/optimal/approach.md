## General
**Extract the least significant base-\(k\) digit**

For a positive current value $x$, Euclidean division gives

$$
x = kq + r,
\qquad 0 \le r < k.
$$

The remainder $r$ is the least significant digit of $x$ in base $k$, and the quotient $q$ contains every more significant digit. Add `x % k` to the answer, replace `x` with `x // k`, and repeat until the quotient is zero.

**Why the accumulated remainders are exactly the digits**

The first division separates the units digit from a multiple of $k$. Dividing the quotient repeats the same decomposition for the next power of $k$. After $t$ iterations,

$$
n = d_0 + d_1k + \cdots + d_{t-1}k^{t-1},
$$

where every extracted remainder $d_i$ lies between 0 and $k-1$. This is precisely the unique base-$k$ representation, so summing the remainders returns the required digit sum.

The digits emerge from least significant to most significant, but addition is order-independent. No string conversion or reversal is needed.

## Complexity detail
Each iteration divides the remaining value by $k$, so there are $\lfloor\log_k n\rfloor+1$ iterations and time is $O(\log_k n)$. The current quotient, remainder, and sum use $O(1)$ space.

## Alternatives and edge cases
- **Build a representation string:** It is correct but stores $O(\log_k n)$ characters that are unnecessary when only the sum is requested.
- **Repeated subtraction for division:** It can recover each quotient and remainder without division, but may perform $O(n)$ total subtractions.
- **Recursive digit extraction:** It mirrors the positional definition but uses $O(\log_k n)$ call-stack space.
- **`n < k`:** The representation has one digit and the answer is `n`.
- **Base 10:** Repeated quotient and remainder operations sum the familiar decimal digits.
- **Base 2:** Every digit is 0 or 1, so the result equals the number of set bits.
- **Power of `k`:** Its representation is 1 followed by zeros and the answer is 1.
- **Maximum input:** `n = 100` still follows the same loop for every allowed base.
- **Zero remainders:** Interior or trailing zero digits contribute nothing but division must continue while the quotient is positive.
