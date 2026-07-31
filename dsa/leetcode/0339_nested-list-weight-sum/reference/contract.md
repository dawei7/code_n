## Function Contract

**Inputs**

- `nestedList`: A list of `NestedInteger` objects. Each object either stores one integer or a nested list of more `NestedInteger` objects.

JSON cases use ordinary nested arrays and integers. The runner reconstructs the `NestedInteger` interface objects before calling `solve(nestedList)`.

**Return value**

Return the sum of each stored integer multiplied by the number of enclosing lists around it.
