## Function Contract

**Inputs**

- `num`: The exact number of digits required in the positive result.
- `sum`: The exact total required across those digits.

The first digit cannot be zero because the result represents a positive integer with exactly `num` digits.

**Return value**

Return the maximum good integer among those attaining the maximum digit-square score, encoded as a string. Return the empty string when `sum` cannot be distributed among `num` decimal digits.
