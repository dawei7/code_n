## Function Contract

**Inputs**

- `n`: The positive upper endpoint of the initial integer sequence.

The initial sequence is `[1, 2, ..., n]`. A sweep keeps the first number visited from its starting side, deletes the next one, and continues alternating keep/delete decisions across the entire current sequence. The sweep direction changes after every operation, beginning from the left.

**Return value**

Return the sole integer left after all alternating deletion operations finish.
