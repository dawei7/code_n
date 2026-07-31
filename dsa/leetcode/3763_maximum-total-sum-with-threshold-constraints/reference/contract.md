## Function Contract

**Inputs**

- `nums`: The positive contribution earned when the corresponding index is chosen.
- `threshold`: The earliest step at which each corresponding index becomes eligible.

The arrays have the same length $n$. Each index can be chosen at most once, and the process cannot stop voluntarily while an unused eligible index exists.

**Return value**

Return the greatest running total achievable when the required process terminates.
