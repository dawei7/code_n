## General
**Add from least significant positions:** Start at the right ends of both arrays and maintain an integer carry. At each position, add the available input bits to that carry.

**Normalize for a negative base:** Let the position total be $s$. The output bit must have the same parity, so choose `bit = s & 1`. The remaining even value belongs at the next position, whose place value is multiplied by $-2$, giving

$$
\text{next carry}=\frac{s-\text{bit}}{-2}.
$$

This carry may be negative or positive; the same parity rule handles either sign. Append bits in least-significant-first order until both inputs and the carry are exhausted.

**Canonicalize the representation:** Remove redundant zeros from the most-significant side of the reversed result while retaining one digit for zero, then reverse the digits into the required order.

At every step, the chosen bit plus $-2$ times the next carry equals the current total, so the transformation preserves the unprocessed numeric value. Induction across positions proves the accumulated digits represent the input sum. Removing only leading zero coefficients does not change that value.

## Complexity detail
The loop consumes at least one input position per iteration, with only a constant number of final carry positions, so it runs in $O(A+B)$ time. The result contains $O(A+B)$ digits and is built in an array of that size, giving $O(A+B)$ space including the required output.

## Alternatives and edge cases
- **Convert to an ordinary integer:** Evaluate both inputs and convert the sum back to base $-2$. It is conceptually simple but relies on arbitrary-precision values rather than operating within the digit representation.
- **Prepend every produced bit:** Maintaining most-significant-first order during addition repeatedly shifts or copies the current result and can take quadratic time.
- **Ordinary binary carry:** Dividing the leftover by positive two is incorrect because the next place has weight $-2$ times the current place.
- **Zero plus zero:** Trimming must preserve the canonical result `[0]`.
- **Negative represented value:** Base $-2$ naturally represents negative numbers without a sign bit, and the carry formula handles them directly.
- **Final nonzero carry:** Continue emitting normalized bits until it becomes zero.
- **Cancellation:** Opposite represented values may produce zero even when neither input is `[0]`.
