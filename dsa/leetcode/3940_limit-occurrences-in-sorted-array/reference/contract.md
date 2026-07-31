## Function Contract

**Inputs**

- `nums`: A nonempty list of integers sorted in non-decreasing order.
- `k`: The positive maximum number of copies to retain for each distinct value.

**Return value**

Return a list containing the elements of `nums` in their original relative order, with each distinct value occurring `min(frequency, k)` times.

The app-local function may resize and return `nums` itself. The returned list is judged by its values; internal capacity and discarded elements beyond its new logical length are irrelevant.
