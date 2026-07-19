## General
**Unfold reflections into a straight ray**

Instead of changing the ray's direction at a mirror, reflect the entire room across that wall. Repeating this construction tiles the plane with mirrored copies of the room, and the physical reflected path becomes one straight line. After crossing `h` room widths, the unfolded ray has risen through `v` room heights precisely when

$$
h p = \operatorname{lcm}(p,q)
\quad\text{and}\quad
v p = h q.
$$

Reducing the ratio gives $h=p/g$ and $v=q/g$, where $g=\gcd(p,q)$. This is the first lattice corner on the ray because the two reduced integers are coprime.

**Use parity to fold the corner back**

Each horizontal room crossing alternates east and west in the original square. Thus odd $h$ ends on the east wall and even $h$ ends on the west wall. Likewise, odd $v$ ends on the north wall and even $v$ ends on the south wall.

The reduced values $h$ and $v$ cannot both be even. Their three possible parity combinations correspond exactly to the three receptors: odd/even reaches southeast receptor `0`, odd/odd reaches northeast receptor `1`, and even/odd reaches northwest receptor `2`. Testing these parities therefore returns the first receptor, not merely some later receptor on the same line, because $h$ and $v$ describe the first unfolded corner.

## Complexity detail
Euclid's algorithm computes $g=\gcd(p,q)$ in $O(\log \min(p,q))$ time. The remaining divisions and parity checks take constant time. Only a fixed number of integers is stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Simulate every reflected segment:** Advancing wall by wall is correct, but it can require $p/\gcd(p,q)$ iterations instead of logarithmic time.
- **Compute the least common multiple explicitly:** It finds the same unfolded corner, but multiplying before dividing is unnecessary and can overflow in fixed-width languages.
- **Remove factors of two:** Repeatedly divide both values while they are even, then inspect parity; this is equivalent, but a greatest-common-divisor reduction states the geometry more directly.
- **The ray hits the northeast corner immediately:** When `q == p`, both reduced counts are odd and receptor `1` is reached.
- **Shared factors:** Values such as `p = 6, q = 4` must be reduced before parity is interpreted.
- **No southwest outcome:** Coprimality prevents both reduced counts from being even, so the starting corner is never selected as a later first receptor.
