## General

**Represent each lifetime by two population changes.** A person contributes one to every year from `birth` through `death - 1`. Instead of incrementing every year in that range, the solution records:

- plus one at the birth year, when the person starts being counted;
- minus one at the death year, when the person stops being counted.

A prefix sum of these changes then reconstructs the population for every year.

**Use the small fixed year domain.** All relevant years lie from 1950 through 2050. `d = [0] * 101` gives one change bucket for each year in that inclusive domain. `offset = 1950` maps a calendar year `y` to array index `y - 1950`.

For each log `[a, b]`, the code first converts both years to indices. `d[a] += 1` records the birth event, and `d[b] -= 1` records the death event.

**Why subtraction occurs at death, not after death.** The person is not alive during the death year. When the prefix scan reaches index `b`, applying minus one before considering that year removes the person immediately. Thus the represented interval is exactly half-open `[birth, death)`, equivalent to the stated inclusive years through `death - 1`.

**Recover yearly population with a prefix sum.** `s` is the current population. At each index `i`, `s += d[i]` applies all births and deaths occurring in that calendar year. After this addition, `s` equals the number of people whose birth is no later than the year and whose death is later than it.

The scan includes the 2050 bucket so deaths at the upper bound are applied consistently, although no person can be born in 2050 under `birth < death <= 2050`. The population there will not create a new positive maximum.

**Keep the earliest maximum by updating only on strict improvement.** `mx` is the largest population seen so far, and `j` is the index of its earliest year. The condition `if mx < s` updates both only when the current population is strictly greater.

If a later year ties `mx`, the condition is false, so `j` remains the earlier index. Because years are scanned from earliest to latest, this implements the required tie rule without a separate comparison.

**Trace overlapping logs.** For `[1950, 1961]`, changes are plus one at 1950 and minus one at 1961. For `[1960, 1971]`, another plus one occurs at 1960. The prefix population becomes one in 1950 and rises to two in 1960, so the maximum record changes to 1960. If population two occurs again in 1970 after other events, strict comparison preserves 1960 as the answer.

**Why simultaneous births and deaths work.** Suppose one person dies in a year when another is born. The difference bucket contains minus one plus one, with net zero. Applying their sum at that year correctly excludes the deceased person and includes the newborn person. Only the net population matters for the result.

**Difference-array invariant.** After processing change index `i`, `s` equals the sum of all birth events at or before year `1950 + i` minus all death events at or before that year. This counts exactly those people satisfying `birth <= year < death`.

The strict record update ensures `mx` is the largest of all populations through `i` and `j` is its smallest index. Induction over the scan proves that, at the end, `j + offset` is the earliest year with the global maximum population.

**Why not sort event tuples.** Sorting births and deaths is another valid sweep, but the 101-year domain is tiny and fixed. Direct indexing makes chronological order implicit and avoids comparison sorting.

## Complexity detail

Let `n = logs.length` and let `Y = 101` be the size of the supported year domain. Recording two changes per log takes `O(n)` time, and scanning all year buckets takes `O(Y)`. Total time is `O(n + Y)`.

The difference array uses `O(Y)` space. Under the fixed constraints, `Y` is a constant, but naming it makes the data structure explicit. All other variables are scalars.

## Alternatives and edge cases

- **Increment every lifetime year:** With this tiny domain it can pass, but it repeats work for long lifetimes and obscures the half-open interval idea.
- **Sort birth and death events:** A chronological event sweep works in `O(n log n)` time and generalizes to large year ranges.
- **Separate birth and death counters:** Two arrays can be prefix-scanned, but one signed difference array contains the same information more compactly.
- **Death-year exclusion:** Subtracting at `death` ensures the person is absent in that year.
- **Several births in one year:** Their increments accumulate in the same bucket.
- **Births and deaths in one year:** Net change is applied before evaluating that year’s population.
- **Tied maximum years:** Strict `mx < s` preserves the first occurrence.
- **One person:** Their birth year is the earliest year with population one.
- **Disjoint lifetimes:** The maximum may be one in several ranges; the earliest birth year wins.
- **Death at 2050:** Bucket index 100 safely stores the removal event.
- **No overflow concern:** At most 100 people contribute, and Python integers are unbounded anyway.
- **Offset mapping:** Returning `j + 1950` converts the internal index back to the calendar year.
