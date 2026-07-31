## Function Contract

**Inputs**

- `heights`: The positive heights of all blocks that must each be visited exactly once.

The order in the input does not restrict the visiting order. The ground at height `0` supplies only the starting position and is not one of the blocks.

**Return value**

Return the greatest possible sum of squared height differences over the initial ground-to-block jump and the subsequent `n - 1` block-to-block jumps.
