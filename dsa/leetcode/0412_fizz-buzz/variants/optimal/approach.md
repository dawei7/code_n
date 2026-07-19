## General
**Classify each integer independently**

Iterate from one through `n`. Divisibility by 3 and 5 fully determines the required output for that position, so no state from earlier numbers is needed.

**Check the combined case first**

A multiple of 15 satisfies both individual divisibility tests. Test it before the single-factor cases so it receives `"FizzBuzz"` rather than stopping at `"Fizz"` or `"Buzz"`.

**Append exactly one result per number**

After the combined check, test 3, then 5, and otherwise convert the integer to decimal text. Appending once in the same iteration preserves increasing order and guarantees the result length is exactly `n`.

**Why the cases are complete and disjoint**

Every integer is either divisible by both factors, only 3, only 5, or neither. The ordered condition chain selects exactly one of these exhaustive categories, so every output string satisfies the specification without overlap.

## Complexity detail
The loop performs constant work for each of `n` values, giving $O(n)$ time. The required output list stores `n` strings and uses $O(n)$ space; auxiliary state is constant.

## Alternatives and edge cases
- **Build labels by concatenating factor words:** appending `"Fizz"` and `"Buzz"` conditionally avoids an explicit 15 test and has the same bounds.
- **Maintain next multiples as counters:** avoids modulus operations but introduces mutable state for a fixed constant-factor task.
- **Rebuild the entire result list for every append:** is correct but repeatedly copies prior outputs and can take $O(n^2)$ time.
- At $n = 1$, the result contains only `"1"`.
- Multiples of 15 must use the combined label.
- Nonmultiples must use decimal strings, not integers.
- Output order always follows the original numeric sequence.
