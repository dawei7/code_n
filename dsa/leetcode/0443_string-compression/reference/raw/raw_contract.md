## Function Contract

**Inputs**

- `chars`: A mutable array of single-character strings.

**Return value**

- The native method returns the compressed length $k$ after writing the compressed sequence into `chars[0:k]`.
- The app-local `solve` adapter returns `{"length": k, "prefix": chars[:k]}` so both the length and the meaningful prefix are observable.

The in-place compression must use $O(1)$ auxiliary space.
