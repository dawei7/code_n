## Function Contract

**Inputs**

- `nums`: An integer array containing at least two elements.

A valid split includes index `i` in the prefix and starts the suffix at `i + 1`. The suffix minimum is a value, not a sum. Scores and the maximum score may be negative.

**Return value**

Return the maximum of `sum(nums[0:i+1]) - min(nums[i+1:n])` over every `0 <= i < n - 1`.
