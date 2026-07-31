## Function Contract

**Inputs**

- `nums`: The immutable integer array used to construct native `NumArray`.
- `queries`: The app adapter's ordered `[left, right]` inclusive ranges.

**Return value**

Return one range sum per entry in `queries`, in the same order. The native interface returns each value from a separate `sumRange` call.
