## General

**Reduce the grid to independent one-dimensional sight lines**

Rightward visibility depends only on a person's row, and downward visibility
depends only on that person's column. Process every row from right to left and
every column from bottom to top, adding both directional counts into the same
answer matrix.

**Keep only candidates not hidden by a nearer person**

For one backward scan, maintain a monotonic stack of relevant heights ahead.
For the current height $h$, repeatedly pop and count every smaller stack top.
Each popped person is visible: all candidates that survived between it and the
current position are even shorter. After those pops, the remaining top, if
any, is the nearest height at least $h$ and is also visible. It blocks every
person behind it, so no later stack entry is counted.

Equal heights need careful handling. After counting an equal top as the
current person's blocker, remove that older equal entry before pushing the
current one. The nearer equal person blocks the older one for every future
observer, because an intervening equal height is not strictly shorter than
both endpoints.

Every visible person falls into exactly one of the two counted groups: a
smaller candidate popped before any blocker, or the first candidate at least
as tall. Conversely, any later candidate is blocked by a surviving person
whose height is at least the smaller endpoint. This proves the scan counts
exactly the visible people.

## Complexity detail

Let the grid have $m$ rows and $n$ columns. Each cell is pushed and popped at
most once in its row scan and once in its column scan, so total time is
$O(mn)$. The returned matrix uses $O(mn)$ space. A working stack uses at most
$O(\max(m,n))$ additional space.

## Alternatives and edge cases

- **All-pairs directional scans:** Testing every later cell with a running intervening maximum is correct but takes $O(mn(m+n))$ time.
- **Distinct-height queue logic without deduplication:** Leaving multiple equal heights in the stack lets a taller observer incorrectly see through the nearer equal person.
- **One cell:** With nobody rightward or below, its count is zero.
- **One row or one column:** Only one directional scan contributes, and the other adds zero.
- **Equal adjacent people:** The nearer equal person is visible but blocks the equal person behind it.
- **Strictly increasing heights:** Each person sees the adjacent taller blocker only.
- **Mixed directions:** A person may independently see people in both its row and column, and both counts are added.
