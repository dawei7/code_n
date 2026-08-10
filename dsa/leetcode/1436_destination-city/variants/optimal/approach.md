## General

**The destination is characterized by having no outgoing edge**

Each path `[a,b]` says that travel leaves city `a` and arrives at city `b`. The destination city is not merely a city that appears on the right; intermediate cities also appear there. It is the right-side city that never appears as a left-side departure.

Because the paths form one loop-free line, exactly one such city exists.

**Collect every city with an outgoing path**

The set comprehension:

```python
s = {a for a, _ in paths}
```

unpacks every pair, keeps the departure `a`, and ignores the arrival with underscore. The resulting set contains exactly the cities that have an outgoing path.

A set is appropriate because only presence matters. If a more general input repeated a departure city, storing it once would still answer whether it has any outgoing edge.

Expected set membership is constant time, replacing a repeated scan through all paths.

**Search among arrival cities**

The return expression is:

```python
next(b for _, b in paths if b not in s)
```

Every destination candidate must appear as `b` in some path because it is reached from the previous city on the line. The generator visits arrivals in input order and yields only those absent from the outgoing-city set.

`next` returns the first yielded city. The problem guarantee ensures exactly one destination exists, so the generator cannot be exhausted without a result.

The city does not have to appear in the final input row. Paths may be listed in arbitrary order. Membership in `s`, not row position, determines whether an arrival is terminal.

**Trace an out-of-order input**

For:

```text
[["B","C"],["D","B"],["C","A"]]
```

the outgoing set is `{"B","D","C"}`.

- Arrival `"C"` is in the set because another path leaves C.
- Arrival `"B"` is in the set because another path leaves B.
- Arrival `"A"` is absent, so `next` returns A.

The actual chain is D to B to C to A even though the input begins with its middle edge.

**Why only arrivals need to be tested**

The first city in the line has outgoing travel but no incoming travel, so it cannot be the destination. Every intermediate city has both incoming and outgoing travel. The final city has incoming travel and no outgoing travel.

Therefore, searching right-side cities for the one absent from the left-side set covers the final city and excludes both starting and intermediate cities.

**Why the line guarantee matters**

In an arbitrary directed graph, several sink cities could have no outgoing edges, or an isolated city might never appear in a path. The problem guarantees a single loop-free line, so:

- There is exactly one sink.
- It appears as an arrival.
- Returning the first qualifying arrival is unambiguous.

The implementation intentionally relies on this contract rather than adding error handling for malformed graphs.

**Why the algorithm is correct**

Every city in `s` has at least one outgoing path, so none can be the required destination. The returned city `b` appears as an arrival and is not in `s`, so it has no outgoing path and satisfies the destination definition.

Conversely, the guaranteed destination is reached by the line's final edge, so it appears among the tested `b` values. It has no outgoing edge, so it is absent from `s` and will satisfy the generator condition. Thus the returned value is exactly the destination.

**Why generator evaluation is efficient**

The generator is lazy. It does not build a list of every arrival without outgoing travel. As soon as the unique destination is found, `next` stops iteration.

The worst case still examines all paths when the destination's incoming edge occurs last, but no extra result collection is allocated.

## Complexity detail

Let $n$ be the number of paths. Building the outgoing set scans $n$ pairs in expected $O(n)$ time. Searching arrivals scans at most $n$ pairs with expected $O(1)$ membership tests, so total expected time is $O(n)$.

The set contains at most $n$ departure cities and uses $O(n)$ space. The generator and local variables use constant additional state. These bounds match the manifest.

## Alternatives and edge cases

- **Nested scan:** For each arrival, scan all departures to see whether it leaves again. It uses constant space but takes $O(n^2)$ time.
- **Set difference:** Build both arrival and departure sets, then return the sole member of `arrivals - departures`. It is concise but stores a second set that the generator avoids.
- **Degree counting:** Record incoming and outgoing degrees for every city, then select outdegree zero. This generalizes to richer graphs but stores more information than needed.
- **Follow the chain:** Build a map from departure to arrival, find the start, and walk until no next city exists. It works but requires identifying and traversing the entire line.
- **One path:** Its right city is absent from the one-element departure set and is returned.
- **Input edges out of order:** Set membership makes order irrelevant.
- **City names with spaces:** Strings are used as opaque hash keys; their contents require no parsing.
- **Intermediate arrival:** It is rejected because it also occurs as a departure.
- **Uniqueness guarantee:** `next` safely returns the first match because exactly one destination exists.
- **No fallback return:** Malformed input without a destination would raise generator exhaustion, but the contract rules that case out.
