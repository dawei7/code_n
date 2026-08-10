## General

**Use the upper endpoint as a shrinking candidate**

The competitive `Solution` starts with `n`, its name for the upper endpoint.
While lower endpoint `m` is smaller, it repeatedly executes `n &= n - 1`, which
removes the least significant set bit from `n`. The returned transformed `n` is
the common binary prefix of the endpoints with zeros in every varying suffix
position.

This avoids touching the individual numbers between `m` and `n`. Range size can
be enormous while the integer has at most 31 relevant bits under the Reference.

**Derive the bit-clearing identity**

For positive `n`, locate its rightmost 1-bit. Subtracting one clears that bit
and turns every zero to its right into one. Higher bits stay unchanged. ANDing
the original with `n - 1` clears the selected bit; original trailing zeros clear
all the new lower ones.

Thus each update strictly reduces `n` and removes exactly one of its 1-bits.
The method skips over zero positions instead of shifting through them one by
one.

**Connect bit clearing to the range AND**

The range AND equals the stable high-order prefix shared by `m` and the original
`n`, with zeros below that prefix. At the highest bit where the endpoints differ,
the interval spans both a zero and a one. Lower bits cycle as numbers advance,
so each is also zero somewhere in the interval.

While transformed `n` remains above `m`, it contains a set bit within that
unstable suffix. Clearing that bit cannot remove anything that the full range
AND would retain.

Once transformed `n` is no greater than `m`, all unstable set bits are gone.
The shared prefix remains, and every lower position is zero. Continuing would
risk clearing stable information, so the condition stops at exactly the right
boundary.

**Trace a case that stops below the lower endpoint**

For `m = 5` (`101`) and `n = 6` (`110`), one update changes `110` to `100`.
Now 4 is below 5, so the loop stops and returns 4. This illustrates why the
condition is not “until the endpoints are equal.”

The complete interval contains 5 and 6, and `101 & 110 = 100`, confirming the
returned value.

**Why soundness and completeness follow**

Every removed bit is in a suffix position that changes somewhere between the
endpoints, so at least one range member has zero there. The full AND must remove
it, making every clearing step sound.

At termination, a shared high prefix is the only part left. Every number from
`m` through original `n` has that same prefix, so its 1-bits survive all AND
operations. All lower positions have already been cleared. No required 1-bit is
missing and no unstable 1-bit remains.

**Selected and inactive classes differ**

The ordinary platform entry is the first class named `Solution`. `Solution2`
is an unused alternative. It computes `diff = n - m`, counts the bit length of
that difference in `i`, and returns `n & m >> i << i`.

Python precedence parses the shifted part before bitwise AND, effectively
clearing the low `i` bits of `m` and ANDing with `n`. The idea is to clear a
suffix wide enough to contain all endpoint variation. It is denser and easier
to misread than the selected Kernighan loop, especially because it lacks
parentheses around the shifts.

The second method's `i` is derived from numeric difference, and clearing that
many low positions yields the common stable portion for the endpoint range. It
is not invoked unless a caller explicitly constructs `Solution2`.

**Fixed-width and variable-width complexity language**

The source comment calls the selected method $O(1)$. That is conventional for
a problem restricted to 31 nonnegative bits: at most 31 set bits can be removed.
The manifest writes $O(\log r)$, where $r$ is the upper endpoint, which exposes
the dependence on numeric bit length. Both descriptions are compatible once
the computational model is stated.

**Boundary cases require no branches**

For `m == n`, no bit is cleared and the single range value is returned. For
`m == 0`, the loop continues until `n` reaches zero. For a range that crosses a
major power-of-two boundary, the common prefix may be empty and the result zero.

Nonnegative input ensures the value decreases and cannot enter Python's
negative arbitrary-precision bit semantics.

## Complexity detail

Let $b$ be the bit length of upper endpoint `n`. Each loop removes one 1-bit,
so there are at most $b = O(\log(n+1))$ iterations. This matches the manifest's
$O(\log r)$ form. The actual count can be smaller because zero bits require no
iteration.

For the fixed 31-bit domain this is $O(1)$. The method stores a constant number
of integers, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Endpoint right shifting:** Shift `m` and `n` until equal, then restore the number of removed positions; direct common-prefix construction.
- **Inactive difference mask:** `Solution2` clears a suffix based on the endpoint difference but should use parentheses for readability.
- **Direct iteration:** Becomes prohibitively slow when the interval contains many values.
- **Single-value interval:** Returns that value immediately.
- **Lower endpoint zero:** Final answer is necessarily zero.
- **Crossing bit-length boundary:** Common prefix can vanish completely.
- **Sparse upper endpoint:** Kernighan clearing may use very few iterations.
- **Stopping below `m`:** Expected and correct; equality is not required.
- **Fixed 31-bit contract:** Justifies the source's constant-time comment.
- **Arbitrary-width integers:** Use the logarithmic bit-length bound instead.
