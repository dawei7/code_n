## General
**Keep only days still waiting for an answer**

Scan temperatures from left to right and store indices whose next warmer day has not yet appeared. Their temperatures are nonincreasing from the bottom to the top of the stack: any smaller top would already have been resolved by the day that introduced a larger value below it.

**Resolve every colder stack top with the current day**

For a current temperature at index `i`, repeatedly pop while it is strictly greater than the temperature at the stack top `j`. The current day is the first warmer day for `j`: every intervening day was processed while `j` remained unresolved, so none was warmer. Store `i-j` and continue because the same current value may resolve several colder days.

**Preserve equal temperatures as unresolved**

The comparison must be strict. An equal current temperature does not answer the older day, so its index is pushed above the older equal index. A future warmer value may then pop both and assign different distances.

**Why every reported distance is the nearest one**

An index enters the stack when its day is processed and leaves only upon the first later temperature strictly above it. If it is popped at `i`, no earlier day between the two could have been warmer, otherwise that earlier scan would have popped it. Indices left after the final day have no later warmer temperature and correctly retain their initialized zero answers.

## Complexity detail
Each of the `n` indices is pushed once and popped at most once, so total time is $O(n)$ despite the nested-looking loop. The answer and unresolved-index stack each use $O(n)$ space.

## Alternatives and edge cases
- **Scan forward from every day:** stop at the first warmer value for each index; it is simple but takes $O(n^2)$ time on constant or decreasing temperatures.
- **Scan right to left with jump distances:** previously computed waits can skip over nonwarmer days in linear time, but the boundary reasoning is less direct.
- **Temperature-bounded lookup:** because values lie in a small fixed range, track the nearest future index for each warmer temperature; this is linear with a constant temperature factor.
- **Equal temperatures:** equality is not warmer and must not resolve a waiting day.
- **Strictly increasing input:** every day except the last waits exactly one day.
- **Nonincreasing input:** no index is popped, so every answer is zero.
- **Single day:** there is no later day, yielding `[0]`.
- **Multiple pops:** one hot day may be the nearest warmer day for several unresolved earlier indices.
