## General
Use a difference array indexed by year offset from 1950. For every lifetime, add 1 at its birth index and subtract 1 at its death index. The subtraction at `death` implements the half-open interval `[birth, death)` exactly.

Scan year offsets in increasing order while accumulating the difference values. The running sum after applying a year's change is precisely the population alive during that year: every earlier birth has added one, and every death at or before the year has removed one.

Keep the largest population seen and its year. Update the saved year only when the running population is strictly larger, not when it merely ties. Since scanning is chronological, this preserves the earliest year among all maxima.

## Complexity detail
Recording all lifetimes takes $O(n)$ time, and scanning the $Y$ year positions takes $O(Y)$ time, for $O(n+Y)$ total. The difference array uses $O(Y)$ space. Under the source's fixed 1950–2050 domain, $Y=101$ is a small constant, but it remains explicit in the bound.

## Alternatives and edge cases
- **Test every person for every year:** Straightforward, but costs $O(nY)$ time.
- **Sorted birth and death events:** A sweep over event tuples also works, but simultaneous birth/death ordering must preserve the exclusive death boundary.
- **Death year:** A person is not alive during `death`, so decrement at that exact year.
- **Earliest tie:** Replace the answer only for a strictly greater population.
- **Simultaneous death and birth:** Both changes apply before evaluating that year's population.
- **Single lifetime:** Its birth year is the earliest maximum.
- **Boundary years:** Birth may be 1950 and death may be 2050 without indexing outside the difference array.
- **Consecutive non-overlapping lives:** They create equal populations in adjacent years rather than an overlap.
