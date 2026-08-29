## General

**Store counts for a growing stream**

The class must support many interleaved `add` and `find` calls. A frequency map
is a natural persistent representation: `self.cnt[x]` is the number of times
value `x` has been added and not otherwise removed. There is no removal method,
so counts only increase.

`defaultdict(int)` supplies zero as the initial count for a missing key.
`add(number)` can therefore increment one entry directly without an explicit
existence branch.

Keeping counts rather than a set is essential. A set can say whether value
three exists, but it cannot distinguish one copy from two copies. That
distinction determines whether three may pair with another three to satisfy
`find(6)`.

**Search complements among distinct values**

For a query `value`, the source iterates over `(x, v)` entries in the map.
For each stored value `x`, its only possible partner is:

`y = value - x`.

If `y` is absent, no pair beginning with `x` reaches the target. If it is
present and differs from `x`, one occurrence of each key is enough and the
method returns true.

If `x == y`, the equation asks to use the same numeric value twice. The problem
allows two equal integers but still requires two stored elements. The condition
`v > 1` verifies that at least two copies were added.

If no key finds a valid complement, the loop finishes and returns false.

**Trace the sample operations**

Construction creates an empty frequency map. Adding one, three, and five gives
counts `{1:1, 3:1, 5:1}`.

For `find(4)`, when the loop examines one, it computes complement three.
Three is present and different from one, so the query returns true.

For `find(7)`, complements six, four, and two are all absent. The full scan
ends and returns false.

Suppose another three is added. `find(6)` may examine `x = 3`, compute the same
value as its complement, and see count two. It returns true. With only one
three, the `v > 1` test would correctly reject using that single occurrence
twice.

**Why checking every key is complete**

Any valid pair has values $a$ and $b$ with $a+b=\texttt{value}$. Since $a$
was added, it appears as some key visited by the loop. At that iteration, the
computed complement is exactly $b$.

If $a\ne b$, membership proves both distinct stored elements exist. If
$a=b$, the frequency test proves there are at least two stored occurrences.
Therefore every valid pair causes a true return.

Conversely, every true return satisfies the sum equation through
`y = value - x`, and the condition ensures two actual stored occurrences are
available. The method cannot produce a false positive.

**Understand the operation tradeoff**

`add` is optimized to one expected constant-time hash update. `find` may scan
every distinct value. This design is attractive when additions are frequent or
the set of distinct values is moderate.

Another design could precompute every possible pair sum during each add. That
would make `find` constant time but make additions and storage potentially
linear per insertion and quadratic overall. The local Reference does not
specify an operation-frequency preference, so the frequency-map tradeoff is
the standard balanced choice.

**Map iteration remains stable**

The expression `y in self.cnt` checks membership without indexing the
`defaultdict`, so it does not create a missing complement entry while the map
is being iterated. Mutating dictionary size during iteration would be unsafe;
this source avoids it.

Calls to `add` occur outside an active `find` loop under ordinary sequential
class semantics.

**Exact-source dependency**

The selected source uses `defaultdict` but does not import it. A standalone
module requires `from collections import defaultdict`. Without that import,
constructing `TwoSum` raises `NameError`.

## Complexity detail

Let $u$ be the number of distinct stored values and $n$ the total number of
added values.

`add` performs one expected-$O(1)$ hash-table update. `find` examines at most
$u$ keys and does expected constant-time membership work for each, so it takes
$O(u)$ expected time, which is $O(n)$ in the worst case.

The map stores one key and count per distinct value, using $O(u)$ space and
therefore $O(n)$ worst-case space. These worst-case bounds match the manifest.

## Alternatives and edge cases

- **Sorted list with lazy sorting:** Append in $O(1)$, sort after changes, then use two pointers for queries. A query after an add can cost $O(n\log n)$.
- **Maintain a sorted list on every add:** Enables linear two-pointer queries but insertion can cost $O(n)$.
- **Precompute pair sums:** Makes `find` expected $O(1)$ but can require $O(n^2)$ update work and storage.
- **Set only:** Insufficient because it cannot validate two equal operands.
- **Empty structure:** The loop is empty and `find` returns false.
- **One stored value:** It cannot pair with itself unless added again.
- **Negative values:** Complement subtraction and hash lookup work unchanged.
- **Large query target:** An absent complement is simply rejected; no overflow occurs in Python.
- **Repeated additions:** They increment one count without increasing distinct-key space.
- **Missing import:** `defaultdict` must be imported before construction.
