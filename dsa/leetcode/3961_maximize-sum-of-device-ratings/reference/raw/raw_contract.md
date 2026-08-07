## Function Contract

**Inputs**

- `units`: A nonempty rectangular matrix of positive capacities; every row represents one device and has the same length.

Let $m$ be the number of devices, $n$ the units per device, and $U=mn$ the total number of initially supplied units.

**Return value**

Return the maximum possible sum of final device ratings after zero or more legal transfers. The total may exceed the range of a signed 32-bit integer.
