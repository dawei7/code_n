## General
**Leave an already monotone prefix unchanged when possible**

Convert `n` to a mutable digit array. If every adjacent pair is nondecreasing, `n` itself is the largest permitted answer. A descent means some earlier digit must become smaller; only then can the suffix be rearranged without exceeding `n`.

**Repair descents from right to left**

Scan indices from the last digit toward the first. Whenever `digits[i - 1] > digits[i]`, decrement `digits[i-1]` and record `i` as the beginning of a suffix that will be replaced. Continuing left is essential because the decrement may create a new descent with its own predecessor, as in `332` becoming a prefix `22` before suffix replacement.

**Maximize everything after the decisive decrement**

Once the leftmost required decrement has been found, set every digit from the recorded boundary onward to `9`. The decreased prefix makes the result strictly smaller than `n`, so choosing the largest possible suffix cannot exceed `n` and maximizes the answer for that prefix.

**Why the greedy result is maximal**

A descent cannot be fixed while keeping all earlier digits equal to `n`: the offending left digit must decrease, possibly propagating left across equal digits. The reverse scan finds exactly the earliest position forced to decrease and lowers it by only one, preserving the longest and largest possible prefix. After that strict decrease, all `9`s form the greatest monotone suffix. Any larger candidate would need either a larger forced prefix, which recreates a descent or exceeds `n`, or a suffix larger than all `9`s, which is impossible.

## Complexity detail
Let `d` be the number of decimal digits. One reverse scan and one suffix fill take $O(d)$ time. The mutable digit array uses $O(d)$ space.

## Alternatives and edge cases
- **Construct digits left to right with bounded dynamic programming:** track whether the prefix is already smaller than `n`; it is general but heavier than the direct greedy repair.
- **Repeatedly repair the first descent:** restarting a left-to-right scan after each decrement is correct but can rescan the digit prefix and take $O(d^2)$ time.
- **Decrement and test candidates:** checking every integer below `n` can require an enormous number of trials.
- **Already monotone input:** return `n` unchanged.
- **Zero:** its one digit is monotone, so the answer is zero.
- **Leading zero after repair:** converting the final digit string to an integer naturally removes it, as `10` becomes `09` and then `9`.
- **Cascading equal digits:** inputs such as `11110` require the decrement to propagate left across several equal digits.
- **Upper boundary:** $10^{9}$ repairs to `999999999`.
