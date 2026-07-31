## General

Kadane's algorithm retains the best sum of a nonempty subarray ending at the current index. Here, whether the operation range has begun or ended also affects the current value, so retain four kinds of ending-at-this-index sums:

- `no_operation`: the operation has not affected the current sum range;
- `multiplying`: the current index lies inside a multiplication range;
- `dividing`: the current index lies inside a division range; and
- `finished`: a multiplication or division range affected an earlier part of the current sum range and has already ended.

For an original value `value`, let `multiplied = value * k`. Compute `divided` by truncating `value / k` toward zero; in integer arithmetic this is `value // k` for nonnegative values and `-((-value) // k)` for negative values.

The ordinary Kadane transition either starts a new sum range at `value` or extends `no_operation`. A multiplying range can start with the current value, begin after the best prior `no_operation` sum, or extend the prior `multiplying` state. The division transition has the same three choices with `divided`. Once an operation ends, `finished` extends with the unchanged current value; it can come from the prior `multiplying`, `dividing`, or `finished` state. Every transition uses only states from the preceding index, so the operation-affected portion stays contiguous and uses a single operation type.

By induction over the scanned prefix, each state is the greatest sum among exactly the subarrays described by its phase, because its transition enumerates every legal way that phase can begin or continue at the current index. Taking the maximum over all states and all ending indices therefore covers every final sum range whose intersection with the operation range is nonempty, including partial overlap and a sum range that continues after the operation.

The maximum also includes `no_operation`. This does not violate the requirement to perform exactly one operation. For any nonempty unchanged candidate range, choose one value inside it: multiplying a positive value, dividing a negative value toward zero, or applying either operation to zero cannot decrease the range's sum. Thus every `no_operation` value is attainable by an exact nonempty operation, while the active states capture any strict improvement.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. Each value performs a constant number of state transitions, so the running time is $O(n)$. Only the four previous states, their next values, and the global maximum are retained, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate operation and sum ranges:** Directly trying intervals is straightforward but requires at least quadratic work and can become cubic if each transformed array is rescanned.
- **Run Kadane on only the fully multiplied and fully divided arrays:** This misses cases where only part of the final sum range is transformed or where the sum continues after the operation ends.
- **All values negative:** The answer must still use a nonempty sum range; dividing a negative value can move it toward zero, but no empty sum of zero is allowed unless a transformed element actually becomes zero.
- **Multiplier equal to one:** Both operations leave all values unchanged, and the state machine reduces to ordinary Kadane behavior.
- **Truncation direction:** Python floor division rounds a negative quotient downward, so negative values require `-((-value) // k)` to implement the required ceiling and hence truncation toward zero.
- **Different operation and sum ranges:** The phase states permit partial overlap and unchanged values before or after the transformed portion; equality of the two ranges is never assumed.
- **Wide sums:** A transformed value may have magnitude $10^{10}$ and a sum may reach magnitude $10^{15}$, so fixed-width implementations require 64-bit integers.
