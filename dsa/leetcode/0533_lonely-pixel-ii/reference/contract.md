## Function Contract

**Inputs**

- `picture`: a nonempty rectangular matrix containing only `"B"` and `"W"`
- `target`: the required number of black pixels in both the qualifying row and column

**Return value**

- Return the number of black coordinates whose row and column counts equal `target` and whose column's black pixels
  all occur in rows identical to that coordinate's row.
