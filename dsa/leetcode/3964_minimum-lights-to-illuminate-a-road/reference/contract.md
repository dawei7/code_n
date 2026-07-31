## Function Contract

**Inputs**

- `lights`: A nonempty list of nonnegative integers; index `i` is a road position, and a positive value is the illumination radius of the existing bulb at that position.

Let $n$ be the number of road positions.

**Return value**

Return the smallest number of additional radius-one bulbs whose combined coverage, together with the existing working bulbs, makes all `n` positions visible.
