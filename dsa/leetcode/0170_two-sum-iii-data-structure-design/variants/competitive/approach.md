## General

**Index the stream by value and multiplicity**

The competitive class stores a `defaultdict(int)` named `lookup`. Each call to
`add(number)` increments `lookup[number]`, so the table represents both which
values exist and how many copies of each have arrived.

Hashing makes this update expected constant time. Values are not sorted, and
the full insertion history is not stored as separate list entries when values
repeat.

Multiplicity is required because a pair consists of two elements, not merely
two numeric expressions. One stored five cannot satisfy `find(10)`, but two
stored fives can.

**Convert a target into one complement per key**

During `find(value)`, the method loops through every distinct stored `key` and
computes:

`num = value - key`.

This is the only value that can pair with `key` to produce the query target.
The first half of the condition, `num in self.lookup`, tests whether that
complement has been added.

The second half distinguishes two cases:

- if `num != key`, membership of both keys proves two different stored values
  are available;
- if `num == key`, the method requires `self.lookup[key] > 1`, proving two
  occurrences of that same value exist.

When both requirements hold, it returns true immediately. Exhausting every key
without success returns false.

**Trace distinct and duplicate pairs**

After adding one, three, and five, `find(4)` examines one and computes three.
Both exist as different keys, so it returns true.

`find(7)` checks complements six, four, and two. None exists, so the result is
false.

If five has been added only once, `find(10)` sees that the complement of five
is also five but rejects it because its count is not above one. After adding
five again, the same query succeeds.

For negative numbers, adding negative three and one makes `find(-2)` true:
the complement of negative three is one. The algorithm depends on equality
and arithmetic, not on nonnegative values.

**Prove both directions**

Suppose a valid stored pair exists with values $a$ and $b$. The loop eventually
visits key $a$ and computes:

$$
\texttt{value}-a=b.
$$

If the values differ, both membership checks are satisfied. If they are equal,
the existence of two pair elements means their stored count is at least two.
Thus a real pair cannot be missed.

For any true return, the computed complement guarantees the numeric sum, while
the different-value or duplicate-count condition guarantees two stored
occurrences. Therefore the method cannot claim a pair by reusing one element.

**Why membership does not alter the map**

A `defaultdict` creates a missing entry when accessed through
`self.lookup[missing_key]`, but the `in` operator only checks membership. The
condition tests `num in self.lookup` before any count access for that
complement.

When `num == key`, the count lookup refers to the existing iterated key.
Consequently `find` does not change dictionary size during iteration, avoiding
a Python runtime error and keeping the query read-only.

**Choose where to spend work**

This representation makes each add inexpensive and charges a scan to each
find. The number of iterations depends on distinct values, not total additions.
Many duplicate additions can therefore increase counts without slowing the
key scan.

A successful query may return after its first inspected key, but that is only
best-case behavior. Complexity uses the unsuccessful or late-match case,
because then every distinct key must be checked before the class can know the
answer. Dictionary iteration order is not part of the correctness argument and
should not be relied upon to place a useful key early.

A pair-sum cache would reverse the tradeoff: expensive additions could make
queries constant time. A sorted structure would offer another balance. The
chosen hash-frequency design is simple and meets the overall linear bounds.

**Source imports and class state**

The file correctly imports `defaultdict` from `collections`. All persistent
data belongs to the instance, so constructing a new `TwoSum` creates an empty
stream. No state leaks across objects.

## Complexity detail

Let $u$ be the number of distinct keys and $n$ the number of calls that added a
value. `add` takes expected $O(1)$ time. A worst-case unsuccessful `find`
visits all $u$ keys, taking expected $O(u)$ time and at most $O(n)$.

The frequency map occupies $O(u)$ space, bounded by $O(n)$. Query-local state
is constant. The manifest's $O(n)$ time and space are correct worst-case
summary bounds, though per-operation detail is more informative.

## Alternatives and edge cases

- **Ordinary dictionary:** Use `get(number, 0) + 1` instead of `defaultdict`; behavior and bounds are identical.
- **Sorted values and two pointers:** Requires sorting or maintaining order, shifting cost between `add` and `find`.
- **Cache all sums:** Fast queries but potentially quadratic storage as the stream grows.
- **Only a set:** Fails the equal-operands case because it loses multiplicity.
- **No values:** Every query returns false.
- **One value:** It cannot be used twice.
- **Two identical additions:** They correctly enable a doubled-value query.
- **Many duplicates:** Only one map key is stored, with a larger count.
- **Negative and zero values:** Complement logic treats them normally.
- **Sequential object use:** State persists across calls on one instance and resets in a new instance.
