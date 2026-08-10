## General

**Align bits by distance from the right end**

The loop index `i` is not a direct string index. It counts how many positions have been processed from the right. Character `a[-(i+1)]` is the bit at that distance from `a`'s end, and the analogous expression reads `b`.

The loop runs `max(len(a),len(b))` times. Before accessing a string, it checks whether `i` is smaller than that string's length. Missing higher bits in the shorter input contribute nothing, exactly like leading zero padding.

**Calculate one column total**

At each iteration, `val` begins as the incoming `carry`. Available input bits are converted individually and added. `carry, val = divmod(val, 2)` then separates the total into the next carry and current output bit.

The four possible totals map as follows: 0 becomes carry 0/bit 0; 1 becomes 0/1; 2 becomes 1/0; and 3 becomes 1/1. This is complete because no larger total can occur from two binary digits plus one carry.

**Accumulate in reverse positional order**

The units bit is computed first, so `result += str(val)` builds a least-significant-first string. After all aligned input positions, a remaining carry is appended at this reverse string's end. `result[::-1]` then reverses the complete sequence into normal display order.

For `"11" + "1"`, the loop appends 0 for the first position and 0 for the second, then appends carry 1. The reverse of `"001"` is `"100"`.

It helps to read that trace by columns rather than as whole numbers. At distance zero from the right, the two bits are 1 and 1, so their total 2 writes 0 and carries 1. At distance one, the available bit from `a` is 1, `b` has no bit and therefore contributes 0, and the incoming carry contributes 1; again the total 2 writes 0 and carries 1. The fixed loop is now finished, and that final carry supplies the most significant 1. Every written character therefore has a local explanation; the algorithm never needs to convert the complete inputs to numeric values.

The same alignment rule also explains an unequal example such as `"1010" + "11"`. The shorter input participates in the two rightmost columns only. For the remaining two columns, its guarded access is skipped, which has precisely the same mathematical effect as imagining `"0011"` without actually allocating that padded string.

**Why the carry is appended after the fixed loop**

The `for` loop processes exactly the positions supplied by the longer input. Carry is not an input position, so it is handled afterward. It is either zero, requiring nothing, or one, representing one new most significant bit.

This is equivalent to an extra while-loop iteration but separates input processing from final overflow.

**Correctness invariant**

Before iteration `i`, `result` contains correct bits for positions 0 through `i-1` measured from the right, in that same low-to-high order, and `carry` is the exact transfer into position `i`.

The conditional character accesses supply the two bits at position `i`, treating absent ones as zero. Quotient and remainder produce the correct current bit and next carry, preserving the invariant. After the fixed positions and possible carry are appended, reversing yields the unique binary representation of the sum.

**A source-accurate string-construction caveat**

Python strings are immutable at the language level. Each `result += str(val)` may allocate a new string and copy all previously accumulated bits. Some CPython versions optimize repeated concatenation when the string has one reference, so observed behavior is often near linear. That optimization is not a portable semantic guarantee.

Under a conservative cross-implementation analysis, constructing an $L$-character result this way can take $O(L^2)$ total copying time. The manifest's $O(L)$ time describes the arithmetic and assumes efficient incremental concatenation. A list of bit pieces followed by one join would guarantee the linear bound.

**Selected class and unused alternative**

`Solution2` uses `itertools.izip_longest`, a Python 2 name, and is not the selected class. The canonical `Solution` uses explicit negative indices and works without that dependency.

## Complexity detail

The arithmetic loop has $L=\max(m,n)$ iterations, and final reversal costs $O(L)$. With an amortized/in-place concatenation optimization, total observed time is $O(L)$, matching the manifest. Without that non-guaranteed optimization, immutable prefix copying gives a conservative $O(L^2)$ bound for the exact source.

The growing reverse string and final reversed string each have $O(L)$ characters, so peak space is $O(L)$, matching the manifest's output-scale bound. Scalar arithmetic state is constant. The source comment's $O(1)$ excludes the returned and under-construction strings.

## Alternatives and edge cases

- **List append plus join:** Collect output bits in a list, reverse, and join. This guarantees $O(L)$ construction time in Python.
- **Two descending pointers:** Track explicit indices into `a` and `b` and continue while either pointer or carry remains. It avoids negative-index arithmetic.
- **Preallocated character buffer:** Fill from the end and slice away an unused leading slot. It provides predictable linear construction.
- **Unequal lengths:** Bounds checks make missing high bits contribute zero.
- **Final overflow:** A nonzero carry is appended before reversal and becomes the leading 1.
- **`"0" + "0"`:** The one loop iteration appends zero, no carry follows, and reversal returns `"0"`.
- **Long carry chain:** Inputs such as many ones still use one constant-time arithmetic update per bit.
- **Immutable concatenation:** Correctness is unaffected, but portable time complexity may be quadratic.
- **No integer overflow:** Only individual digit values and a carry at most one are stored.
- **Input strings unchanged:** Negative indexing only reads characters.
