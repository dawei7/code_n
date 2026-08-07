## Function Contract

`solve(reader: list[int], target: int) -> int`

The source-native method is `Solution.search(reader: ArrayReader, target: int) -> int`. The standalone app receives the hidden values as the list `reader` and wraps them in a local equivalent of LeetCode's `ArrayReader`; callers of the search logic still access values only through `get`.

**Inputs**

- `reader`: the strictly increasing secret values used by the app-local reader adapter.
- `target`: the integer to locate.

**Return value**

Return the target's unique zero-based index, or `-1` if it does not occur. An out-of-bound reader access yields $2^{31} - 1$, which is greater than every legal value and target.
