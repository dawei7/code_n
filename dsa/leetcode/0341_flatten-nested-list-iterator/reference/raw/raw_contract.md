## Function Contract

**Inputs**

- `nestedList`: A list of `NestedInteger` objects. Each object either stores one integer or a nested list of more `NestedInteger` objects.

JSON cases use ordinary nested arrays and integers. The runner reconstructs the `NestedInteger` interface objects before constructing `NestedIterator(nestedList)`.

**Return value**

`NestedIterator.next()` returns the next integer, while `hasNext()` reports whether one remains. The app's `solve` dispatcher exhausts that same iterator so validated cases can display the complete sequence.
