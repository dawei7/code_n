## General

**Separate physical storage from logical meaning**

Store one physical bit per index and a global `flipped` flag. The logical value
at index `idx` is `bits[idx] ^ flipped`. Toggling the flag therefore complements
every logical bit without visiting the array.

For `fix`, change storage only when that logical value is zero, writing the
physical value that represents logical one under the current flag. `unfix`
symmetrically changes only a logical one. This preserves idempotence even after
any number of global flips.

**Maintain the logical one count**

Keep `ones`, the number of logical one bits. A successful `fix` increments it,
and a successful `unfix` decrements it. Flipping turns every current one into a
zero and every zero into a one, so replace the count with `size - ones`.

Now `all`, `one`, and `count` are direct constant-time comparisons or reads.
Only `toString` must inspect every index, XORing each physical bit with the
flag. The physical-value invariant and exact count update establish every
method's result after each operation.

## Complexity detail

Let $n$ be the bitset size and $Q$ the number of method calls. Construction and
`toString` take $O(n)$ time; `fix`, `unfix`, `flip`, `all`, `one`, and `count`
take $O(1)$ time. Since the contract permits at most five string conversions,
the complete trace takes $O(Q+n)$ time and $O(n)$ space.

The benchmark uses $Q=n$ lazy flips followed by a count. Its `size` is the
number of method calls after construction. A physical-flip implementation
performs $O(n)$ work per flip and therefore takes $O(Qn)=O(Q^2)$ when $Q=n$.

## Alternatives and edge cases

- **Physically complement every bit:** This is simple and correct, but each
  `flip` takes $O(n)$ time and repeated flips make a trace quadratic.
- **Two complementary strings:** Swapping active and inactive buffers makes
  `flip` constant-time, but every point update must keep both buffers
  synchronized and string rebuilding remains necessary.
- Repeating `fix` on a logical one or `unfix` on a logical zero must not change
  `ones`.
- A point update after `flip` must compare the logical value, not the stored
  physical bit alone.
- For size one, `one()` and `all()` always agree.
- Two consecutive flips restore both every logical value and the original one
  count.
- `toString` reports index order and must not expose the physical encoding.
