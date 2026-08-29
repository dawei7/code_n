## General

**Represent iteration with one cursor per vector**

The exact source stores references to the two input vectors in `self.vectors` and stores their next unread indices in `self.indexes`. Initially both indices are zero. It also keeps `self.cur`, the vector that should be considered next, and `self.size = 2`.

The iterator does not merge or copy the vector contents. Its complete logical position is described by three small pieces of state:

- `indexes[0]`: the next unread position in `v1`;
- `indexes[1]`: the next unread position in `v2`; and
- `cur`: which vector currently has the turn.

This differs from the manifest's deque-of-active-vectors summary. The protected implementation uses cyclic indices and lets `hasNext()` skip exhausted vectors.

**Let `next()` consume exactly one current element**

When called in the intended protocol, `next()` assumes `cur` points to a vector with an unread element. It retrieves that vector and its saved index, reads the element, increments only that vector's index, and advances `cur` cyclically:

$$
\texttt{cur}=(\texttt{cur}+1)\bmod 2.
$$

Advancing after every returned element creates alternation while both vectors still contain values. Consuming from `v1` gives `v2` the next turn; consuming from `v2` wraps back to `v1`.

The saved indices advance independently. Returning an element from one vector does not change the unread position of the other, so every original vector preserves its internal order.

**Make `hasNext()` both a query and a positioning step**

After one vector is exhausted, blindly alternating to it would make `next()` index past its end. The exact design handles this in `hasNext()`.

Starting from the current turn, `hasNext()` checks whether `indexes[cur] == len(vectors[cur])`. Equality means every element of that vector has been returned. If so, it rotates `cur` to the next vector and checks again.

When it encounters a vector whose saved index is smaller than its length, the loop ends and `hasNext()` returns true. At that moment it has also positioned `cur` so the following `next()` call is safe and returns the correct next available vector's element.

This state-changing behavior is intentional. `hasNext()` is not a purely observational method in this implementation; it normalizes `cur` past exhausted vectors.

**Detect that all vectors are exhausted without looping forever**

The variable `start` remembers the vector index where the search began. Each time an exhausted vector is skipped, `cur` advances modulo two. If `cur` returns to `start`, the search has completed a full cycle without finding any unread element. Both vectors are exhausted, so `hasNext()` returns false.

Without this full-cycle check, a loop over two empty or exhausted vectors would rotate forever. The check works whether exhaustion occurs initially for one vector or after iteration has consumed all values.

**Why the returned order is correct**

While both vectors are nonempty, each `next()` advances to the other vector, so elements alternate. If one vector becomes exhausted, `hasNext()` skips it and leaves `cur` on the other. After the remaining vector returns an element, `cur` points back to the exhausted vector, and the next `hasNext()` skips it again. The surviving vector's remaining elements are therefore returned consecutively in their original order.

At every successful call pair `hasNext(); next()`, exactly one unread element is returned and exactly one saved index increases. No element can be returned twice because its vector index only moves forward. No element can be skipped because a vector is bypassed only when its index equals its length. Iteration ends only after a full cycle finds every vector exhausted. Together, these facts prove that every input element appears exactly once in cyclic order.

**Trace the first example**

For `v1 = [1,2]` and `v2 = [3,4,5,6]`:

| Current vector | Returned value | Saved indices afterward | Next nominal turn |
|---:|---:|---|---:|
| 0 | 1 | `[1,0]` | 1 |
| 1 | 3 | `[1,1]` | 0 |
| 0 | 2 | `[2,1]` | 1 |
| 1 | 4 | `[2,2]` | 0 |

Now vector 0 is exhausted. `hasNext()` moves `cur` from 0 to 1. The iterator returns 5, nominally rotates to 0, skips exhausted vector 0 again, and returns 6 from vector 1. A final full scan finds both exhausted and returns false. The output is `[1,3,2,4,5,6]`.

For `v1 = [1]` and `v2 = []`, the first call returns 1. Subsequent `hasNext()` checks vector 1, skips it, then finds vector 0 exhausted too and returns false. For `v1 = []` and `v2 = [1]`, the initial `hasNext()` moves `cur` from 0 to 1 before the first `next()` call, which then safely returns 1.

**The calling protocol matters**

`next()` itself does not search for a nonempty vector. It relies on a preceding successful `hasNext()` call to ensure `cur` is valid. The provided usage follows exactly that protocol:

```text
while iterator.hasNext():
    consume(iterator.next())
```

Calling `next()` directly when `cur` names an empty vector, or after `hasNext()` has returned false, can cause an out-of-range access. That is acceptable under this iterator contract but is important when reasoning about the division of responsibility between the two methods.

Repeated calls to `hasNext()` before `next()` are safe. Once it finds an available vector, the loop condition is false and it leaves `cur` unchanged, so repeated successful queries do not consume or skip an element.

## Complexity detail

For exactly two vectors, `next()` performs a constant number of reads, writes, and arithmetic operations, so it takes $O(1)$ time. `hasNext()` examines at most two vectors before either finding an element or completing a cycle, so it also takes $O(1)$ time.

The iterator stores two input references, two indices, one current-vector index, and the constant size. It does not copy input elements. With the problem's fixed two-vector interface, auxiliary space is $O(1)$, excluding the input vectors and the caller's collected output.

Construction also takes $O(1)$ time for the fixed interface because it creates two-element state arrays and stores references. Returning all $N=\lvert v1\rvert+\lvert v2\rvert$ elements through the client loop naturally takes $O(N)$ total time.

For a generalized $K$-vector version using the same cyclic arrays, storage becomes $O(K)$, `next()` remains $O(1)$ once positioned, and `hasNext()` can take $O(K)$ in the worst case to skip exhausted vectors. A deque containing only active vector positions would achieve $O(1)$ work per call while using $O(K)$ space, which is the alternative described by the manifest.

## Alternatives and edge cases

- **Deque of active positions:** Enqueue each nonempty vector's `(vector index, element index)`, pop one for `next()`, and re-enqueue its advanced position only if elements remain. This avoids repeatedly scanning exhausted vectors and extends cleanly to $K$ vectors, but it is not the exact source.
- **Precompute the merged result:** Building the complete zigzag list makes later calls simple but costs $O(N)$ additional storage and performs work even if the caller stops early.
- **One vector empty initially:** `hasNext()` rotates to the nonempty vector before `next()`, so all of its values are returned in order.
- **One vector exhausts early:** The exhausted vector is skipped on later turns, and the longer vector supplies its remaining suffix without loss.
- **Equal-length vectors:** Turns alternate until both become exhausted together, after which the full-cycle check returns false.
- **Both empty outside the total-length constraint:** The constructor still works; the first `hasNext()` completes a cycle and returns false.
- **Repeated `hasNext()` calls:** They do not advance past an available vector and therefore do not consume data.
- **Calling `next()` without a successful check:** The exact implementation offers no guard and may index an empty vector. Clients must follow the documented iterator loop.
- **Values and duplicates:** Element magnitude, sign, and equality do not affect scheduling. The iterator preserves all values and each vector's internal order.
- **Generalized cyclic order:** With $K$ vectors, advancing modulo $K$ yields round-robin order, while exhausted vectors must be skipped. The same structure works functionally, though a deque improves worst-case per-call efficiency.
- **Input mutation by callers:** The iterator keeps references rather than snapshots. Changing vector lengths or contents during iteration can invalidate saved indices or alter returned values; such concurrent mutation is outside the intended contract.
