# Greatest Common Divisor (Euclidean Algorithm)

| | |
|---|---|
| **ID** | `math_01` |
| **Category** | math |
| **Complexity (required)** | $O(log(min(A, B)$)) Time, $O(1)$ Space |
| **Difficulty** | 2/10 |
| **Interview relevance** | 8/10 |
| **Wikipedia** | [Euclidean algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm) |

## Problem statement

Given two positive integers A and B. Find their Greatest Common Divisor (GCD).
The GCD is the largest positive integer that divides both A and B without leaving a remainder.
(Also known as Highest Common Factor or HCF).

**Input:** Two integers `A` and `B`.
**Output:** An integer representing their GCD.

## When to use it

- To simplify fractions (divide both numerator and denominator by their GCD).
- As a prerequisite building block for the Lowest Common Multiple (LCM), Modular Multiplicative Inverse, and RSA Cryptography.
- One of the oldest surviving algorithms in mathematics (described by Euclid around 300 BC).

## Approach

**1. The Basic Subtraction Rule:**
If a number C exactly divides both A and B (where A > B), then C must also exactly divide their difference (A - B)!
Why? If A = X \cdot C and B = Y \cdot C, then A - B = (X - Y) \cdot C.
Therefore, \text{GCD}(A, B) = \text{GCD}(A - B, B).
We could just keep subtracting the smaller number from the larger number until they are equal. That number is the GCD!
*(Example: \text{GCD}(20, 8) -> \text{GCD}(12, 8) -> \text{GCD}(4, 8) -> \text{GCD}(4, 4) = 4).*

**2. The Modulo Optimization:**
Repeated subtraction is very slow if A is massive and B is tiny (e.g., A=1000000, B=2). We would have to subtract 2 half a million times!
Repeated subtraction is mathematically identical to the **Modulo** operation!
Instead of A - B - B - B, we just do A \pmod B, which instantly gives us the remainder after subtracting B as many times as possible!
Therefore, the core theorem is:
$\text{GCD}(A, B) = \text{GCD}(B, A \pmod B)

**3. The Base Case:**
When the remainder becomes `0`, it means the smaller number perfectly divided the larger number! The non-zero number at this point is our final GCD!
\text{GCD}(X, 0) = X.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for math_01: GCD (Euclidean algorithm).

Repeatedly replace (a, b) with (b, a mod b) until b is 0; the
last non-zero a is the gcd. O(log min(a, b)) time.
"""


def solve(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
```

</details>

## Walk-through

`A = 48`, `B = 18`.

1. `b != 0` (18 != 0).
   - `remainder = 48 % 18 = 12`. (18 goes into 48 twice, remainder 12).
   - `a = 18`.
   - `b = 12`.
2. `b != 0` (12 != 0).
   - `remainder = 18 % 12 = 6`.
   - `a = 12`.
   - `b = 6`.
3. `b != 0` (6 != 0).
   - `remainder = 12 % 6 = 0`. (6 goes into 12 exactly twice!).
   - `a = 6`.
   - `b = 0`.
4. `b == 0`. Loop terminates.
Return `a = 6`. ✓

*(Note: What if we pass `A = 18, B = 48` initially? The very first step does `18 % 48 = 18`. So `a=48` and `b=18`. It naturally swaps them into the correct order in exactly one step!)*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(log(\min(A, B)$)) | $O(1)$ |
| **Worst** | $O(log(\min(A, B)$)) | $O(1)$ |

Gabriel Lamé proved in 1844 that the Euclidean algorithm takes at most 5 \times \text{number of digits of } \min(A,B) steps to complete.
The absolute worst-case scenario occurs when A and B are consecutive Fibonacci numbers.
Because the remainder drops by at least half every two steps, the time complexity is strictly $O(\log(\min(A, B)$)).
Space complexity is $O(1)$ for the iterative approach. (If implemented recursively, it takes $O(\log(\min(A,B)$)) call stack space).

## Variants & optimizations

- **Extended Euclidean Algorithm (`math_07`):** Not only finds the GCD, but also finds the integer coefficients x and y such that A \cdot x + B \cdot y = \text{GCD}(A, B) (Bézout's identity). This is absolutely critical for finding the Modular Multiplicative Inverse.
- **Binary GCD Algorithm (Stein's Algorithm):** An optimization that completely avoids the expensive modulo `%` operator, relying entirely on bitwise shifts `>> 1` and subtraction. It is faster on bare-metal hardware but is rarely necessary in high-level coding interviews.

## Real-world applications

- **RSA Public-Key Cryptography:** The GCD is used to ensure the public exponent `e` is coprime to Euler's totient function \phi(N)$, a strictly required mathematical property for the encryption to be reversible.

## Related algorithms in cOde(n)

- **[math_07 - Extended Euclidean Algorithm](math_07_extended-euclidean-algorithm.md)** — The advanced version that computes Bézout coefficients.
- **[greedy_11 - Egyptian Fraction](../greedy/greedy_11_egyptian-fraction.md)** — An algorithm that relies heavily on GCD to simplify fractions and prevent integer overflow.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
