## General
**Count the bounded values.** Allocate one slot beyond each possible value and, for every input `value`, increment `counts[value + 1]`. The one-position shift is deliberate: after prefix accumulation, `counts[value]` will exclude occurrences equal to `value`.

**Convert frequencies into strict-prefix counts.** Traverse the counter array from low to high, adding each preceding total. At the end, position `value` stores the number of input elements drawn from values $0$ through `value - 1`, exactly the number strictly smaller than `value`.

Look up that total for each original element without reordering `nums`. The shifted counter proves duplicates are excluded, while the prefix sum includes every and only smaller value, so every returned position is correct.

## Complexity detail
Building answers touches all $n$ input and output positions, while prefix accumulation touches the $U$ possible values. Time is $O(n+U)$. The frequency-prefix array occupies $O(U)$ auxiliary space; the required result occupies $O(n)$ output space.

## Alternatives and edge cases
- **Sort with first ranks:** Sort a copy and map each distinct value to its first index. This takes $O(n\log n)$ time and $O(n)$ space.
- **Repeated sorted lookup:** Sort once but call a linear first-index search for every original element. This is correct but can cost $O(n^2)$ time.
- **Compare every pair:** Directly count smaller elements for each position in $O(n^2)$ time without exploiting the bounded values.
- **Duplicate values:** Equal values share one strict-prefix count and never count one another.
- **All equal:** No index has a strictly smaller element, so every answer is zero.
- **Domain boundaries:** Values `0` and `100` fit the shifted 102-slot implementation without special cases.
- **Input order:** Build the output from the original array, not the sorted copy.
