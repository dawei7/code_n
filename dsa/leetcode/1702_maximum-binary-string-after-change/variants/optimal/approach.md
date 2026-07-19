## General
**Fix the prefix before the first zero**

Find the first `0`. If none exists, the string is already all ones and cannot be improved. Otherwise, every character before that position is `1`. No operation can introduce a zero to the left of this prefix while improving the result, so those leading ones remain part of the maximum string.

The operation `10` to `01` can move a zero left across a one, allowing zeros in the remaining suffix to meet. Whenever two zeros are adjacent, `00` to `10` removes one of them. Repeating these moves can therefore reduce any suffix containing zeros to exactly one zero. A result with fewer zeros is always larger than one with more zeros, so a maximum must perform all possible eliminations.

**Locate the unavoidable zero**

Let `first_zero` be the first zero's index and let `zero_count` be the total number of zeros. Combining the first zero with each of the other `zero_count - 1` zeros advances the surviving zero's boundary by one position. Its final index is consequently `first_zero + zero_count - 1`.

The leading positions can all be made `1`, but the survivor cannot be pushed farther right without either retaining another earlier zero or reversing an improvement. Thus the maximum string consists of `1` everywhere except at that single forced index. Constructing exactly that pattern proves both reachability and maximality: every earlier bit is as large as possible, and the only unavoidable zero is delayed as far as the operations permit.

## Complexity detail
Finding the first zero, counting all zeros, and constructing the length-$n$ result each take $O(n)$ time. The immutable output string occupies $O(n)$ space; aside from the returned value, only constant-sized counters are needed.

## Alternatives and edge cases
- **Repeated operation simulation:** applying local replacements and restarting a scan can perform quadratic work and obscures the final single-zero structure.
- **Breadth-first search over strings:** exploring reachable states is exponential and unnecessary because the maximum has a direct form.
- **Recompute zero statistics per output position:** this constructs the right answer but repeats full-string scans, taking $O(n^2)$ time.
- **All ones:** no operation applies, so return the original string.
- **Exactly one zero:** no zero can be eliminated; its position is unchanged in the maximum.
- **All zeros:** the result is `1` in every position except the last.
- **Leading ones:** the first-zero index must be included in the survivor formula; counting zeros alone would place it too far left.
- **Equal-length comparison:** maximizing the binary value is equivalent to maximizing lexicographically, so earlier bits have priority.
