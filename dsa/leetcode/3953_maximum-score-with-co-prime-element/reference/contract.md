## Function Contract

**Inputs**

- `nums`: The original positive integer values.
- `maxVal`: The inclusive upper bound for every replacement value.

Let $n=\texttt{nums.length}$ and define

$$
U=\max(\texttt{maxVal},\max(\texttt{nums})).
$$

**Return value**

Return the maximum possible final selected value minus the number of changed array elements, subject to the selected value being co-prime with every other final element.
