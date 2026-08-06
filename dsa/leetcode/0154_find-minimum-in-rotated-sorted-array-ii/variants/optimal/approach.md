## General

**Preserve a minimum inside a closed interval**

Maintain `[left, right]` so that it contains at least one occurrence of the global minimum. Compare
`nums[middle]` with `nums[right]`, where `middle = (left + right) // 2`.

If the midpoint value is greater, `middle` is in the high prefix of the rotation and the minimum lies strictly to
its right, so set `left = middle + 1`. If it is smaller, the midpoint is in the low suffix and may itself be the
minimum, so preserve it with `right = middle`.

Equality is the distinction from problem 153. It does not reveal which side contains the rotation boundary, but
discarding the right endpoint is safe: if `nums[right]` is a minimum, the equal value at `middle` leaves another
minimum inside the interval. Therefore `right -= 1` preserves the invariant while making progress.

Each update strictly shortens the interval without removing every occurrence of the minimum. When the boundaries
meet, their sole remaining value must be the global minimum.

## Complexity detail

Informative comparisons halve the interval, but equal values may reduce it by only one position. Thus the worst-case
time is $O(n)$, as demonstrated by an all-equal array, while inputs without sustained ambiguity retain logarithmic
behavior. The three boundary indices use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Linear `min`:** matches the worst-case bound but gives up binary-search behavior on informative inputs.
- **Distinct-value binary search:** can discard the wrong half when the midpoint and right endpoint are equal.
- **Remove duplicates first:** requires a linear pass plus mutation or additional storage without improving the
  worst-case bound.
- All values may be equal, in which case each iteration can remove only one endpoint.
- The minimum may occur once, appear on both sides of the rotation boundary, or be surrounded by duplicates.
- A one-element array terminates immediately and returns its only value.
