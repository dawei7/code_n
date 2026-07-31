## Function Contract

**Inputs**

- `iterator_data`: The offline app's values for the underlying iterator.
- `operations`: The sequence of `peek`, `next`, and `hasNext` calls executed by the app adapter.

**Return value**

The offline adapter returns one result for each requested operation. The native `PeekingIterator` exposes the constructor and three methods described above.
