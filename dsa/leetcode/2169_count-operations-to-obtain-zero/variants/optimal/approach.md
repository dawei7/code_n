## General

**Notice when the same subtraction is forced repeatedly**

Assume the current larger value is $a$ and the smaller positive value is $b$.
The rule must subtract $b$ from $a$ until the larger value falls below $b$ or
becomes zero. No choice or comparison outcome can interrupt that run.

Euclidean division writes

$$
a=qb+r,\qquad 0\le r<b.
$$

Those $q$ forced subtractions replace $a$ by $r$. Therefore one `divmod`
operation can advance to exactly the same state that the literal simulation
would reach after $q$ operations, while adding $q$ to the answer.

**Repeat the Euclidean reduction**

While both values are positive, divide the larger by the smaller, retain the
remainder in the larger value's slot, and accumulate the quotient. If the
remainder is positive, the roles of larger and smaller swap on the next
iteration. If it is zero, the required stopping condition has been reached.

Each batched step is equivalent to a consecutive segment of the prescribed
simulation, and the quotient records that segment's exact length. The segments
join without skipping or reordering an operation. When one value reaches zero,
their accumulated lengths therefore equal the number of operations in the
original process.

## Complexity detail

The remainder sequence is the Euclidean algorithm. Its number of iterations is
$O(\log M)$ for $M=\max\{2,\texttt{num1},\texttt{num2}\}$, and each iteration
uses constant auxiliary state. The time complexity is $O(\log M)$ and the
space complexity is $O(1)$.

The benchmark defines `size` as $M$ and pairs increasing powers with a unit
second value. Quotient batching finishes each tier in one reduction, whereas a
correct literal simulation performs $M$ individual subtractions and takes
$O(M)$ time.

## Alternatives and edge cases

- **Literal subtraction simulation:** Following one operation per loop mirrors
  the statement directly and returns the same count, but inputs such as
  `(M, 1)` require $M$ iterations.
- **Recursive Euclidean batching:** Returning the current quotient plus the
  answer for the divisor and remainder is equivalent, but the iterative form
  avoids recursion state.
- If either input starts at zero, the answer is zero and division must not be
  attempted.
- Equal positive values produce quotient one and remainder zero, so exactly
  one operation is counted.
- The accumulated operation count can be much larger than the number of
  Euclidean iterations; every quotient must be added rather than merely
  counting divisions.
- Swapping the two inputs does not change the eventual operation count.
