## Function Contract

### Inputs

- `num`: A non-negative integer whose encoding must be determined from the supplied mapping pattern.

For the complexity discussion, let $q = \texttt{num} + 1$.

### Return value

Return the binary-character string assigned to `num` by the deduced function. Leading zeros are part of an encoding, and the encoding of `0` is the empty string.
