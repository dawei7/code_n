## General

**The operation can only remove set bits.** A change chooses a bit of `n` that is currently one and turns it into zero. It can never create a one where `n` has zero. Therefore every set bit required by `k` must already be set in `n`.

Think of the one-bits as sets:

$$
B(k)\subseteq B(n)
$$

is the exact feasibility condition. If `k` contains even one bit outside `n`'s set, no sequence of allowed changes can produce it.

**Test subset inclusion with bitwise AND.** `n & k` keeps precisely the bits that are one in both integers. If every one-bit of `k` is also in `n`, the intersection equals `k`:

$$
n\mathbin{\&}k=k.
$$

The source returns $-1$ when `n & k != k`. This detects every impossible zero-to-one requirement at once.

For example, $n=14$ is `1110` and $k=13$ is `1101`. The lowest bit is one in $k$ but zero in $n$. Their AND is `1100`, not `1101`, so the result is impossible.

**Count exactly the removable extra bits.** Once feasibility is established, all bits fall into three categories:

- one in both `n` and `k`: keep it;
- zero in both: do nothing;
- one in `n` and zero in `k`: flip it once.

The impossible fourth category—zero in `n` and one in `k`—has already been ruled out.

`n ^ k` has a one exactly where the two bit representations differ. Under the subset condition, every such mismatch is an allowed one-to-zero change. Therefore

`(n ^ k).bit_count()`

is both the number of necessary changes and the number sufficient to reach `k`.

**Why the count is minimal.** Each allowed operation affects exactly one bit. Every mismatch between a one in `n` and zero in `k` must be changed at least once, giving a lower bound equal to the mismatch count. Flipping each of those positions once reaches `k` without touching matching positions, achieving the lower bound. No operation can solve two mismatches simultaneously.

**Trace $n=13,k=4$.** Their binary forms are `1101` and `0100`. AND with $k$ is `0100`, so the target's only set bit is available. XOR is `1001`, which has two set bits. Turning off the high extra bit and the low extra bit changes $13$ to $4$ in exactly two operations.

For equal values such as $21$ and $21$, the subset test passes and XOR is zero. Zero has no set bits, so no changes are needed.

**Why numeric ordering is not enough.** A target smaller than `n` can still be impossible. Although $13<14$, obtaining binary `1101` from `1110` requires creating the low one-bit. Conversely, subset inclusion automatically implies $k\le n$ for positive integers, but the reverse implication does not hold.

**Operator precedence in the one-line source.** Python parses

`n & k != k`

as `(n & k) != k` because bitwise AND binds more tightly than comparison. Adding parentheses would make the intent more obvious, but the exact condition behaves correctly.

## Complexity detail

The constraints cap values at $10^6$, so integers use a fixed small number of bits. AND, XOR, comparison, and `bit_count` are constant-time under the problem model. The method therefore runs in $O(1)$ time and uses $O(1)$ auxiliary space.

For arbitrary-precision values outside the contract, bit operations take time proportional to the number of machine words, or $O(\log\max(n,k))$ bit length. The manifest's constant bound follows the fixed numeric domain.

No input objects are mutated; integers are immutable and the method returns one integer.

## Alternatives and edge cases

- **Inspect bits in a loop:** Compare corresponding low bits, reject a required zero-to-one change, and count extra ones. It is correct but more verbose than masks.
- **Use `(n | k) == n`:** Bitwise OR equals `n` exactly when every set bit of `k` is already in `n`. This is an equivalent feasibility test.
- **Subtract powers of two greedily:** Numeric subtraction can borrow across bits and obscures the operation, which flips chosen bits independently.
- **`n == k`:** XOR is zero and the answer is zero.
- **`k` has a missing bit:** The AND test fails immediately and returns $-1$.
- **`k` is a bit subset:** Every XOR one is an extra bit in `n` and can be cleared.
- **One extra bit:** Exactly one operation is necessary.
- **Target power of two:** It is reachable only if that specific bit is set in `n`; all other set bits are then removed.
- **`k=0` outside the positive contract:** It would always be reachable by clearing every set bit, and the formula would return `n.bit_count()`.
- **Leading zeros:** Binary representations conceptually have unlimited leading zeros, but they match in both positive integers and never affect XOR or feasibility.
- **Smaller target not sufficient:** Numeric comparison cannot replace bit-subset testing.
- **No overflow:** Python bit operations and popcount are exact.
- **Mismatch mask after feasibility:** Once `k` is known to be a bit subset of `n`, `n ^ k` contains no required additions. Every one in that mask is precisely an independently removable extra bit, which is why popcount needs no further filtering.
