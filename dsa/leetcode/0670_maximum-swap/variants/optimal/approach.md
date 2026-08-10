## General

**Maximize the earliest digit that can improve**

Decimal place values make an earlier digit more important than every combination of later digits. If one swap can increase position zero, that improvement dominates any swap whose first change occurs at position one or later.

Therefore, the greedy goals are:

1. find the leftmost position that can receive a larger digit from its suffix;
2. place the largest available suffix digit there;
3. if that largest digit occurs more than once, use its rightmost occurrence.

The exact two-pass solution precomputes the best suffix index for every position and then performs the first beneficial swap.

**Convert digits into a mutable list**

`str(num)` exposes the decimal digits in order, and `list(...)` makes them individually swappable. Character comparison works for single decimal digits because their character ordering is the same as numeric ordering.

Let `n` be the number of digits.

**Meaning of the suffix-index array**

`d[i]` stores the index of the largest digit in suffix `s[i:n]`. When the largest value occurs several times, it stores the rightmost occurrence.

The array begins as `[0, 1, ..., n - 1]`, so every position initially points to itself. The backward loop then propagates better choices from the right.

At position `i`:

- `d[i + 1]` already identifies the rightmost maximum in the suffix strictly after `i`;
- if `s[i] <= s[d[i + 1]]`, assign `d[i] = d[i + 1]`;
- otherwise, leave `d[i] = i`.

The less-than-or-equal comparison is deliberate. When digits tie, it chooses the later index from the suffix rather than the current one.

**Why the rightmost equal maximum is best**

Suppose the left digit `x` will be exchanged with a larger repeated digit `y`. Every choice puts `y` at the same important left position. The difference is where the displaced smaller `x` lands.

Putting `x` at the rightmost possible occurrence of `y` preserves earlier suffix digits as `y`, producing a larger remaining suffix.

For `1993`, swapping one with the first nine gives `9193`, while swapping with the second, rightmost nine gives `9913`. The latter is larger.

**Find the first beneficial position**

The second pass scans `i` from left to right and lets `j = d[i]`.

If `s[i] < s[j]`, a larger suffix digit can improve this position. The algorithm swaps `s[i]` and `s[j]` and stops immediately.

Stopping at the first opportunity is correct because this is the most significant digit position that can be increased. Any swap beginning later would leave this smaller digit unchanged and produce a smaller number, regardless of later details.

If `s[i] == s[j]`, swapping would not improve the current digit. If `d[i] == i`, the current digit is already strictly larger than every later digit. In either case, continue.

**A walkthrough**

For `2736`, the backward pass identifies:

- suffix at index three: digit six;
- suffix at index two: maximum six at index three;
- suffix at index one: maximum seven at index one;
- full suffix at index zero: maximum seven at index one.

The forward pass starts at digit two. Its stored suffix digit is seven, which is larger, so swap indices zero and one. The result is `7236`.

For `9973`, no position has a larger digit to its right. The forward pass makes no swap and returns the original number.

**Why at most one swap is respected**

Only one pair assignment is executed, followed by `break`. If no beneficial pair exists, zero swaps are used, which is allowed by “at most once.”

**Why the greedy choice is correct**

Let `i` be the first position where some later digit is larger. Every position before `i` is already at least as large as every digit available to its right, so no swap can improve an earlier prefix.

Any maximum result using one swap must therefore make its first improvement at `i`. Putting anything smaller than the maximum suffix digit there would lose immediately at the most significant changed position. Among equal maximum suffix digits, using the rightmost occurrence leaves the displaced smaller digit latest and maximizes the remainder.

The exact swap makes all three optimal choices, so no other at-most-one-swap result can be larger.

**Convert back to an integer**

After the optional swap, `"".join(s)` reconstructs the digit string and `int(...)` returns its numeric value.

The operation cannot introduce a leading zero. A swap involving the first position occurs only when a strictly larger suffix digit replaces it; otherwise no first-position swap happens.

## Complexity detail

Let `D` be the number of decimal digits.

String conversion, list creation, the backward pass, the forward pass, joining, and integer conversion each take `O(D)` time. Total time is `O(D)`, which is `O(log N)` for positive numeric input.

The digit list and suffix-index array each contain `D` entries, so auxiliary space is `O(D) = O(log N)`.

For `num = 0`, there is one digit even though the logarithm expression needs the usual special-case interpretation. The direct digit-count bound `O(D)` remains precise.

## Alternatives and edge cases

- **Last-position table for digits zero through nine:** Record each digit's last occurrence, then scan left to right looking for the largest greater digit available later. This uses constant-size metadata because the alphabet has ten digits.

- **Try every pair:** Swap every pair, convert, and retain the maximum. With `D` digits this takes roughly `O(D^3)` if each conversion copies `D` characters, though the small numeric constraint may hide the cost.

- **Swap with the first maximum occurrence:** This can be suboptimal when the maximum repeats; the displaced smaller digit should be moved as far right as possible.

- **Choose the globally largest digit without considering position:** If it is already in an optimal leading location, moving it may hurt. The algorithm searches for the earliest improvable position.

- **Already non-increasing digits:** No digit has a larger suffix digit, so the original number is maximal.

- **One digit:** No pair exists and the input is returned.

- **Zero:** Its one-character representation remains zero.

- **Repeated equal digits:** Equal digits may propagate the rightmost index, but a swap occurs only under strict improvement.

- **Repeated maximum suffix digit:** The `<=` condition in the backward pass preserves the rightmost occurrence.

- **Zeros inside the number:** A larger digit can move ahead of zero normally. The displaced zero moves right and cannot create an invalid representation.

- **At most one swap:** Leaving the number unchanged is correct when every possible swap is non-improving.

- **Character comparison:** It is safe only because every compared string element is one decimal digit, not a multi-character number.

- **Breaking after the swap:** A second beneficial-looking position must not be processed because only one swap is allowed.
