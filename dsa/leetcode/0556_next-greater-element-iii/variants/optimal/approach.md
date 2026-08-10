## General

The task is the standard next lexicographic permutation of the decimal digits. Among all rearrangements greater than the current digit string, the next permutation changes the rightmost possible position by the smallest possible amount, then makes the remaining suffix minimal.

The code converts the integer to mutable character list `cs`. Digit characters compare in the same order as their numeric values.

**Find the rightmost pivot that can increase.** Starting at the second-last index, the loop moves left while:

`cs[i] >= cs[i + 1]`.

This identifies the longest suffix that is nonincreasing from left to right. Such a suffix is already the greatest permutation of its digits, so rearranging only that suffix cannot produce a larger number.

The first position `i` with `cs[i] < cs[i + 1]` is the rightmost pivot where an increase is possible.

If no pivot exists, all digits are nonincreasing, such as `"21"` or `"987"`. The number is already the largest permutation of its digits, so the method returns `-1`.

**Choose the smallest suffix digit larger than the pivot.** Pointer `j` starts at the final digit and moves left while `cs[i] >= cs[j]`.

Because the suffix is nonincreasing, scanning from its right end encounters candidate digits from smallest upward. The first digit greater than the pivot is therefore the smallest value that can increase the pivot.

Swapping `cs[i]` and `cs[j]` makes the whole number larger at the latest possible position and by the smallest possible digit increase.

**Make the suffix as small as possible.** Before the swap, the suffix was nonincreasing. After exchanging with the selected rightmost-greater digit, it remains arranged so reversing it produces nondecreasing order.

The assignment:

`cs[i + 1 :] = cs[i + 1 :][::-1]`

therefore creates the smallest suffix possible with the remaining digits.

For `12`, pivot one is smaller than two, they swap, and the one-element suffix stays unchanged, yielding `21`.

For `21`, no increasing pivot exists and the answer is `-1`.

For `12443322`, the pivot is the rightmost digit that is below some suffix digit. Swapping it with the smallest greater suffix digit and reversing the suffix avoids skipping any valid permutation.

**Why the result is the smallest greater number.** Any greater permutation must differ from the original at some position. Choosing the rightmost possible pivot preserves the longest prefix. At that pivot, selecting the smallest greater digit minimizes the first changed value. Finally, sorting the remaining suffix ascending minimizes everything after it. Lexicographic digit order and numeric order coincide for equal-length positive decimal strings.

The digits are joined and parsed as integer `ans`.

**Enforce the 32-bit result limit.** Even if the next permutation exists mathematically, the contract rejects it when it exceeds `2**31 - 1`. The final conditional returns `-1` in that case.

Rearranging digits preserves length except that leading zero could theoretically matter, but the pivot increase process cannot place zero at the leading position of a positive number when producing a greater same-length permutation.

For a concrete repeated-digit trace, take `115`. The suffix scan finds pivot index one because digit one is less than five. The successor is five; swapping gives `151`, and the one-character suffix is already minimal. For `151`, the longest nonincreasing suffix is `51`, so the pivot is the first one. The smallest suffix digit greater than it is five; after swapping and reversing the remaining `11`, the result is `511`. No permutation strictly between 151 and 511 exists with those digits.

The rightmost-pivot rule is what preserves the longest possible leading prefix. Changing an earlier digit causes a larger numeric jump than any valid change at a later position, regardless of how cleverly the suffix is arranged.

## Complexity detail

Let $d$ be the number of decimal digits. Pivot search, successor search, suffix reversal, join, and parsing each take $O(d)$ time, so total time is $O(d)$.

The mutable digit list and temporary suffix/joined string use $O(d)$ space, matching the manifest. Scalar indices use constant space.

Under 32-bit input, $d$ is at most ten, but the asymptotic digit analysis remains informative.

Parsing the joined result before the overflow check is safe in Python because its integer type is unbounded. In a fixed-width language, overflow should be detected during construction or by using a wider temporary type.

## Alternatives and edge cases

- **Generate all digit permutations:** It is factorial and produces many duplicates when digits repeat.
- **Sort all digits and search:** It discards the useful near-sorted suffix structure and still needs permutation logic.
- **Choose any greater suffix digit:** Picking one larger than necessary skips closer valid numbers.
- **Leave the suffix descending:** The result would be greater but not the smallest greater permutation.
- **Already descending digits:** No greater permutation exists.
- **Repeated digits:** The strict pivot and successor comparisons handle duplicates correctly.
- **One digit:** No pivot exists, so return `-1`.
- **Zeroes in the suffix:** Reversal places them as early as possible after the pivot, minimizing the result.
- **Overflow:** A valid permutation above the signed 32-bit maximum returns `-1`.
- **Input unchanged:** Only the character list is mutated.
