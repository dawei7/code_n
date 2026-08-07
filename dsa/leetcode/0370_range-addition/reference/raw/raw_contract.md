## Function Contract

**Inputs**

- `length`: The positive length of the zero-initialized result array.
- `updates`: A list of inclusive range updates `[startIdx, endIdx, inc]`.

**Return value**

Return the length-`length` array after accumulating all additions, including overlaps and negative increments.
