## Function Contract

**Inputs**

- `points`: Distinct coordinate pairs representing the existing points.

Two existing points are directly connected when their x-coordinates are equal or their y-coordinates are equal. Activation reaches an entire connected component under the transitive closure of this relation. The added coordinate must contain integers and must differ from every existing coordinate pair; either individual coordinate may still equal an existing x- or y-coordinate.

Let $n=\lvert\texttt{points}\rvert$.

**Return value**

Return the largest number of activated points achievable after adding and initially activating one valid point. Include the newly added point in the count.
