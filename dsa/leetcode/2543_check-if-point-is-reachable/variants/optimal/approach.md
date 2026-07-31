## General

Track the greatest common divisor of the two coordinates. Replacing one coordinate by its difference with the other does not change the gcd:

$$
\gcd(x,y-x)=\gcd(x,y)=\gcd(x-y,y).
$$

Doubling one coordinate can either preserve the gcd or multiply it by two; it cannot introduce an odd prime factor that was not already shared. Since the starting gcd is 1, every reachable point must therefore have a gcd that is a power of two.

**Why the condition is sufficient**

The same operations generate all integer coordinate pairs whose shared divisor has no odd prime factor. Euclidean difference transformations handle the coprime part of a pair, while coordinate doublings supply every required factor of two. Equivalently, after removing all factors of two from the target gcd, the target is reachable exactly when the remaining gcd is 1. Thus the power-of-two condition is both necessary and sufficient.

Compute `gcd(targetX, targetY)`. A positive integer `g` is a power of two exactly when its binary representation has one set bit, which is tested by `g & (g - 1) == 0`.

## Complexity detail

Euclid's gcd algorithm takes $O(\log(\min(\texttt{targetX},\texttt{targetY})))$ time. The bit test is constant time, and the algorithm uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Search the grid:** Breadth-first or depth-first search explores an unbounded state space and cannot scale to coordinates up to $10^9$.
- **Subtraction-based gcd:** Repeatedly subtracting the smaller coordinate is correct but can take linear time for pairs such as `(x, 1)`; modulo-based Euclid is logarithmic.
- **Check that each coordinate is a power of two:** Individual coordinates may contain arbitrary odd factors; only their common divisor matters, as `(4, 7)` demonstrates.
- **Coprime targets:** A gcd of 1 is $2^0$, so every positive coprime target pair is reachable.
- **Equal coordinates:** The point `(v, v)` is reachable exactly when `v` is a power of two.
- **Bit-test parentheses:** Write the comparison around the complete bitwise expression to avoid precedence ambiguity across languages.
