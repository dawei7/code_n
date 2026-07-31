## General

**Pair seats from left to right**

Every valid first section must end after the second seat, every valid second
section after the fourth seat, and so on. The seat pairing is therefore fixed;
only the divider gap between consecutive pairs can vary.

**Count gaps between seat pairs**

Suppose the second seat of one pair is at index $a$ and the first seat of the
next pair is at index $b$. A divider may occupy any gap after index $a$ through
the gap before index $b$, giving $b-a$ choices. These choices are independent
for different pair boundaries, so multiply all such distances modulo
$10^9+7$.

During one scan, count encountered seats and remember the position of every
second seat. When the first seat of the next pair appears, multiply by its
distance from the remembered position. If the final seat count is zero or odd,
return zero; otherwise the product describes every valid division exactly
once.

## Complexity detail

Let $n$ be the corridor length. One scan takes $O(n)$ time. The seat count,
previous pair endpoint, and product use $O(1)$ space.

## Alternatives and edge cases

- **Store every seat index:** Multiplying gaps from an index list is also
  $O(n)$ time but requires $O(n)$ space.
- **Dynamic programming by seat count:** Tracking partial section states works
  but obscures the independent gap-product structure.
- **Recount every prefix:** Deriving each seat number from a fresh prefix scan
  is correct but takes $O(n^2)$ time.
- Zero seats and every odd positive seat count produce zero ways.
- Exactly two seats produce one way, regardless of surrounding plants.
- Adjacent seat pairs contribute a factor of one.
- Apply the modulus after each multiplication.
