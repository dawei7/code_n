## Function Contract

`solve(nums, k, mul) -> int`

**Inputs**

- `nums`: A nonempty array of positive integers. Equal values at different indices are separate selectable elements.
- `k`: The exact number of array elements that must be selected and processed.
- `mul`: The multiplier available before the first selected element is processed; it decreases by one after every step.

**Output**

Return the maximum possible integer total after exactly `k` selected elements have been processed in a freely chosen order.

At each step, adding the original value and adding its product with the current multiplier are both permitted. No modulus is applied to the result.
