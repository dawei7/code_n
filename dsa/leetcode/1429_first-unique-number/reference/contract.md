## Function Contract

The source-native object exposes these operations:

- `FirstUnique(nums)`: initialize the queue with the integers in `nums`, preserving their order;
- `showFirstUnique()`: return the earliest value whose current frequency is exactly one, or `-1` when no such value exists;
- `add(value)`: append `value` to the queue and return nothing.

The app represents one object lifecycle with two aligned arrays:

- `operations`: begins with `"FirstUnique"`; each later entry is `"showFirstUnique"` or `"add"`;
- `arguments`: supplies `[nums]` to the constructor, no arguments to `showFirstUnique`, and `[value]` to `add`.

Let $n = \lvert\texttt{nums}\rvert$ and let $q$ be the number of calls after construction.

**Return value**

Return one result per operation. Construction and `add` produce `null`; each `showFirstUnique` entry produces the requested integer or `-1`.
