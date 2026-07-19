## General
**Classify digits by their effect**

Digits `3`, `4`, and `7` are forbidden. The remaining digits are valid, but a number is good only if at least one position uses `2`, `5`, `6`, or `9`; a number made solely from `0`, `1`, and `8` would rotate to itself.

**Count valid prefixes up to the bound**

Process the decimal digits of `n` from left to right with digit dynamic programming. A state records the current position, whether the prefix still equals `n`'s prefix, and whether a changing digit has appeared. Try every valid digit up to the tight limit and update those two flags. Leading zeros behave like unchanged zero digits, so fixed-width representations count shorter positive numbers naturally.

At the end, contribute one exactly when the changing flag is set. Every integer from zero through `n` has one fixed-width digit sequence considered by the tight transitions. Invalid sequences are excluded at their first forbidden digit, valid unchanged sequences contribute zero, and valid changed sequences contribute one. Zero also contributes zero, so the resulting total is precisely the good positive integers.

## Complexity detail
For each of $O(\log n)$ decimal positions, there are only four combinations of the tight and changed flags and at most ten transitions. Time is therefore $O(\log n)$. The memoized recursion stores $O(\log n)$ states and uses the same maximum stack depth.

## Alternatives and edge cases
- **Iterative digit DP:** Carry counts for the tight and changed states across positions; this keeps the same $O(\log n)$ time and can use $O(1)$ state space.
- **Combinatorial prefix counting:** Count valid and unchanged suffix choices when a prefix becomes smaller than `n`; this is equally efficient but more delicate.
- **Check every integer:** Validate each number digit by digit in $O(n \log n)$ total time.
- **Only unchanged digits:** Numbers composed entirely of `0`, `1`, and `8` are valid rotations but are not good.
- **Any forbidden digit:** One `3`, `4`, or `7` invalidates the whole number.
- **Leading zeros in the DP:** They do not create a changed digit and allow shorter numbers to share the bound's width.
- **Small bounds:** No special table is needed; the same states handle one-digit ranges.
