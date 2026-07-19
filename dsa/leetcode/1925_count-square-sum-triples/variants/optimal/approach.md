## General
**Precompute the legal right-hand sides**

Create a set containing $c^2$ for every integer $c$ from $1$ through $n$. Membership in this set answers in expected constant time whether a sum of two squares is the square of an allowed integer.

**Enumerate the ordered legs**

Visit every ordered pair `(a, b)` in $[1,n]^2`. Compute `a * a + b * b` and increment the answer exactly when that value belongs to the precomputed square set.

Each qualifying ordered pair has at most one positive `c`, because squaring is strictly increasing on positive integers. Set membership therefore identifies exactly one legal triple without explicitly searching `c`. Conversely, every square triple contributes when its ordered pair `(a, b)` is visited, so none are missed. Iterating both full ranges naturally counts the reversed orientation separately.

## Complexity detail
Building the $n$ squares takes $O(n)$ time and space. The nested loops examine $n^2$ ordered pairs with expected $O(1)$ set membership each, giving $O(n^2)$ time and $O(n)$ space.

## Alternatives and edge cases
- **Enumerate `a`, `b`, and `c`:** Checking every possible triple is direct but costs $O(n^3)$ time.
- **Square root per pair:** Testing `isqrt(a * a + b * b)` avoids the set and uses $O(1)$ space, while retaining $O(n^2)$ time.
- **Count only `a < b` and double:** This is valid because no positive solution has $a=b$, but the ordered-loop form follows the contract more directly.
- **Values below five:** No positive Pythagorean triple fits, so the answer is zero.
- **Scaled triples:** Multiples such as `(6,8,10)` count independently from their primitive form.
- **Inclusive bound:** A triple with `c == n` is allowed.
