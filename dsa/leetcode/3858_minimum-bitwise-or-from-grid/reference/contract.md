## Function Contract

**Inputs**

- `grid`: A nonempty rectangular matrix of positive integers, with at least one value in every row.

If row $i$ contributes the selected value $x_i$, a valid selection contains exactly $m$ values and produces

$$
x_0\mathbin{\vert}x_1\mathbin{\vert}\cdots\mathbin{\vert}x_{m-1}.
$$

No column consistency is required: each row may contribute a value from any of its columns.

**Return value**

Return the minimum numerical value of the combined bitwise OR among all selections.
