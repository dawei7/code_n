## Function Contract

The app exposes the native iterator through an equivalent batch adapter.

**Inputs**

- `vec`: A two-dimensional integer vector whose rows may be empty.

**Return value**

Return all values in the order produced by repeatedly calling `next`. The native interface instead constructs `Vector2D(vec)` and preserves the incremental `next` and `hasNext` operations.
