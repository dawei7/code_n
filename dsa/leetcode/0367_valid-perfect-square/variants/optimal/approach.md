## General
**Search the monotone square function**

For non-negative integers, $r^{2}$ increases strictly as $r$ increases. That monotonicity allows binary search over candidate roots instead of testing them one by one. The value $1$ is handled directly; for larger inputs, any square root lies between $1$ and `floor(num / 2)`.

**Discard half of the candidates each step**

At each iteration, square the midpoint. Equality proves that `num` is a perfect square. If the square is smaller, every candidate at or below the midpoint is too small, so move the left boundary above it. If the square is larger, move the right boundary below it. When the interval becomes empty, every possible integer root has been excluded.

**Why termination proves the Boolean result**

The search interval initially contains every feasible root. Each comparison removes only candidates whose squares are all strictly on the wrong side of `num`, preserving any valid root in the remaining interval. Therefore finding equality is sufficient for `True`, while exhausting the interval proves that no integer root exists.

## Complexity detail
The candidate interval is halved on every iteration, so the search performs $O(\log num)$ comparisons. It stores only interval boundaries, the midpoint, and its square, using $O(1)$ space.

## Alternatives and edge cases
- **Newton iteration:** converges quickly to the integer square root and also uses constant space, but its update and stopping conditions are less direct.
- **Subtract consecutive odd numbers:** uses the identity $1 + 3 + \ldots + (2r - 1) = r ^{2}$ but takes $O(\sqrt{num})$ iterations.
- **Linear candidate scan:** is correct but also requires $O(\sqrt{num})$ time.
- Input `1` is the smallest positive perfect square.
- Values immediately below or above a large square must return false.
- In fixed-width languages, comparing `mid <= num / mid` can avoid multiplication overflow; Python integers grow automatically.
