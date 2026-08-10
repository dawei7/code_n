## General

**Encode values relative to the current minimum**

The competitive class maintains one list, `stack`, plus a scalar `self.min`.
It does not store most pushed values directly. Instead, after the first entry,
it stores the difference between the new value and the minimum that existed
immediately before the push.

Suppose the old minimum is $m$ and the new value is $x$. The stored number is:

$$
d = x - m.
$$

The sign of $d$ records the relationship that matters:

- $d>0$ means $x$ is above the old minimum, so the minimum does not change;
- $d=0$ means $x$ equals the old minimum;
- $d<0$ means $x$ is a new minimum, so `self.min` must become $x$.

This representation allows both the current top and an earlier minimum to be
reconstructed in constant time.

**Handle the first element as the base state**

When `stack` is empty, `push(x)` appends zero and assigns `self.min = x`.
There is no previous minimum from which to form a meaningful difference, so
zero acts as the base marker.

The same marker is also what would be stored for a later value equal to the
current minimum. In either situation, while that marker is on top, the actual
top value equals `self.min`.

The code checks emptiness rather than checking whether `self.min` is `None`.
This matters after the final element is popped: `self.min` may retain an old
numeric value, but the next push sees an empty list and correctly establishes a
new base minimum.

**Update the minimum only for a negative difference**

For a nonempty stack, `push(x)` first calculates and appends
`x - self.min`. If $x$ is smaller than the old minimum, the difference is
negative and the source changes `self.min` to $x$. Otherwise, the prior minimum
remains valid.

Consider pushing `-2`, then `0`, then `-3`.

- Pushing `-2` stores zero and sets the minimum to `-2`.
- Pushing `0` stores `0 - (-2) = 2`; the positive marker says the minimum
  remains `-2`.
- Pushing `-3` stores `-3 - (-2) = -1`; the negative marker says `-3` became
  the new minimum.

The internal list is `[0, 2, -1]`, while `self.min` is `-3`.

**Decode the top from the marker**

Let the top stored difference be $d$.

If $d>0$, the value did not change the minimum when it was pushed. The old
minimum is still the current minimum, so rearranging $d=x-m$ gives
$x=d+m$. The source returns `x + self.min`, where its local variable `x`
actually holds the stored difference.

If $d\le 0$, the top value equals the current minimum. A zero marker represents
the base value or an equal duplicate. A negative marker represents the value
that became the new minimum. In both cases, returning `self.min` is correct.

This explains the source's seemingly unusual `if x > 0` rather than
`if x >= 0`: zero must take the minimum branch.

**Restore an older minimum during pop**

`pop()` removes the top difference. A nonnegative difference never changed the
minimum, so no restoration is needed.

A negative difference is different. At the time of its push:

$$
d = x - m_{\text{old}}
\quad\text{and}\quad
m_{\text{current}} = x.
$$

Solving for the previous minimum gives:

$$
m_{\text{old}} = x-d = m_{\text{current}}-d.
$$

The source performs exactly `self.min = self.min - x`, again using local `x`
for the stored difference. Because that difference is negative, subtracting it
raises the minimum back to its previous value.

In the trace above, popping marker `-1` restores
`-3 - (-1) = -2`. The next top marker is two, so `top()` reconstructs
`2 + (-2) = 0`. `getMin()` returns `-2`, matching the expected state.

**Why duplicate minima remain safe**

If a value equals the current minimum, its stored difference is zero. Popping
that zero does not alter `self.min`, which is correct because an earlier equal
minimum remains below it. If the zero is the final base marker, the stack
becomes empty; valid calls will not query the stale scalar, and the next push
will overwrite it.

The invariant is that `self.min` is the minimum of the nonempty logical stack,
and every stored marker contains enough information either to reconstruct its
top value or to restore the minimum that preceded it. Push establishes this
information, and pop uses it in reverse, so all valid operation sequences are
handled.

## Complexity detail

Let $n$ be the current number of elements.

Every operation performs a constant number of list-end accesses and arithmetic
operations. `push`, `pop`, `top`, and `getMin` are each $O(1)$ amortized time
in Python. The source comment saying `Time: O(n)` is therefore inaccurate if it
means one operation; a sequence of $n$ operations takes $O(n)$ total time.

The list contains one encoded number per logical element, and the scalar
minimum uses constant additional storage. Total auxiliary space is $O(n)$, not
the `O(1)` claimed by the first source comment. Encoding changes what is stored
per element but cannot eliminate the need to represent the stack itself. The
manifest's $O(1)$ per-call time and $O(n)$ space are accurate.

Python integers grow as necessary. In a fixed-width language, computing
`x - min` or restoring `min - difference` can overflow even when all input
values fit the declared integer type; that implementation would need a wider
numeric type.

## Alternatives and edge cases

- **Parallel prefix-minimum stacks:** Store each actual value and the minimum at that depth. This is easier to reason about but uses two list entries per pushed value.
- **Pairs in one stack:** Store `(value, minimum_so_far)` together. It keeps the same simple invariant and avoids encoded arithmetic.
- **Sparse minimum tracker:** Store only new minima and their duplicate counts alongside an ordinary value stack. It may save repeated tracker entries but uses two containers.
- **Linear scan for minimum:** Straightforward, but `getMin()` becomes $O(n)$ and fails the required interface guarantee.
- **First value:** The zero base marker and assigned scalar establish the representation without needing a prior minimum.
- **Equal minima:** They produce zero differences; popping one correctly leaves the current minimum unchanged.
- **New minimum:** It produces a negative marker, which is exactly the signal needed to restore the old minimum later.
- **Positive, zero, and negative input values:** The sign of the input itself is irrelevant; only the difference from the prior minimum is interpreted.
- **Pop to empty:** `self.min` is stale afterward, but the contract forbids queries on an empty stack and the next push overwrites it.
- **Fixed-width overflow:** A translation should calculate differences in a wider type; Python's arbitrary-precision integers avoid this issue.
- **Misleading source comments:** The implemented representation uses linear storage and constant time per operation, in agreement with the manifest rather than the nearby comments.
