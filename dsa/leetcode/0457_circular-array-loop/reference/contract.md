## Function Contract

**Inputs**

- `nums`: A nonempty circular array of nonzero signed jump lengths.

**Return value**

- Return `True` if some repeated route contains more than one position and uses jumps of one consistent sign; otherwise, return `False`.

The destination of position `i` is `(i + nums[i]) % len(nums)`. A one-position self-loop is not a valid cycle.
