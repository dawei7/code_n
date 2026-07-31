## General

A binary integer has a trailing zero exactly when its least-significant bit is
zero, which is equivalent to the integer being even. A bitwise OR has a zero in
that bit only when every selected operand also has zero there: including even
one odd value sets the result's least-significant bit to one.

Therefore, a valid selection exists exactly when the array contains at least
two even elements. Those two elements alone form a qualifying selection; any
selection with fewer than two even values either has insufficient elements or
must include an odd value.

Scan the array and count even values. Return immediately upon finding the
second one. If the scan ends first, no qualifying pair—and thus no larger
qualifying selection—exists.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. The scan takes $O(N)$ time in the worst case
and uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every pair:** Testing `(nums[i] | nums[j]) & 1` is correct but takes $O(N^2)$ time.
- **Enumerate subsets:** Larger subsets add no useful possibility beyond choosing two even elements and lead to exponential work.
- **Exactly one even value:** A second selected element must be odd, making the OR odd.
- **All values even:** Any pair works, so the answer is immediately true.
- **All values odd:** Every possible OR has its least-significant bit set.
- **More than one trailing zero:** The contract asks for at least one; checking only the least-significant bit is sufficient.
