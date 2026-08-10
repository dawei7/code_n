## General

**Keep the number unchanged if its digits already qualify**

Digits are monotone increasing when every adjacent pair satisfies left digit less than or equal to right digit. The exact solution converts `n` to a mutable list of digit characters and scans from left to right while this condition holds.

The index `i` begins at one. After the first loop, either:

- `i == len(s)`, meaning no descent exists and `n` itself is the largest valid number no greater than `n`.
- `s[i - 1] > s[i]`, meaning `i` is the first position where monotonicity fails.

If the number already qualifies, the method performs no edits and returns it after joining the digits.

**Why the first descent forces a decrease somewhere to its left**

At a descent such as the `3, 2` boundary in `332`, leaving the prefix unchanged cannot produce a monotone number no greater than the input. Raising the later digit enough to reach 3 would make the candidate larger than `n` at the first differing position.

Therefore some digit at or before the left side of the descent must be decreased. To maximize the result, the solution starts by decreasing the digit immediately before the descent by exactly one.

After lowering that digit, every later position should eventually be made as large as possible, namely nine, because the prefix has already made the candidate strictly smaller than `n`.

**Why a decrement may propagate left**

Lowering `s[i - 1]` can create a new descent with its own left neighbor. In `332`, lowering the second 3 to 2 gives the prefix `32`, which is still decreasing. The first 3 must also be lowered.

The loop

`while i and s[i - 1] > s[i]`

decrements `s[i - 1]` and moves `i` one position left. It repeats until the digit before the changed boundary is no greater than the digit after it, or until it has moved past the leading position.

Every decremented digit was at least one: it was strictly greater than a decimal digit to its right. Subtracting one therefore never creates a negative digit.

**Why the suffix becomes all nines**

When leftward repair stops, the prefix through the relevant decreased digit is monotone. More importantly, that prefix is now strictly smaller than the corresponding prefix of the original `n`.

Once a more significant prefix is smaller, choosing any suffix digits from zero through nine cannot make the complete number exceed `n`. The largest monotone-compatible suffix is all nines. Nine is at least every preceding decimal digit, and no other digit is larger.

The code increments `i` once after the repair loop and writes `'9'` from that position to the end. The increment positions the fill immediately after the leftmost digit that had to be decreased.

**Trace `332`**

The initial scan stops at index 2 because the second 3 is greater than 2.

1. Decrement the digit at index 1 from 3 to 2 and move `i` from 2 to 1.
2. Now the digit at index 0 is 3 and the digit at index 1 is 2, so the new boundary also descends.
3. Decrement index 0 from 3 to 2 and move `i` to 0.
4. The repair stops. Increment `i` to 1 and fill indices 1 and 2 with nine.

The result is `299`. It is monotone, no greater than 332, and any number beginning with 3 would be forced above the input or retain a descent.

**Trace `120`**

The first descent is `2 > 0`. Decrease 2 to 1, producing prefix `11`. The preceding boundary `1 <= 1` is already valid, so propagation stops. Filling the remaining position with nine gives `119`.

This example shows why only the suffix after the repaired position becomes nines; the valid prefix should be preserved as much as possible.

**Leading zero behavior**

For `n = 10`, the first digit is decreased from 1 to 0 and the suffix becomes 9, forming the character string `"09"`. Converting it with `int` returns 9, which is the correct ordinary integer representation.

For `n = 0`, the digit list has length one. No adjacent pair exists, no repair occurs, and zero is returned.

**Why the answer is the largest valid candidate**

If there is no descent, returning `n` is obviously optimal. Otherwise, any valid candidate no greater than `n` must first differ at or before the descent’s left digit and must be smaller there. The repair loop finds the rightmost possible stable place to make the smallest necessary decrement, propagating left only when monotonicity forces it.

The preserved prefix is therefore lexicographically greatest among feasible prefixes. After it becomes smaller than `n`, filling every remaining digit with nine maximizes the suffix while maintaining monotonicity. The resulting number is valid, does not exceed `n`, and no larger valid candidate can exist.

## Complexity detail

Let `d` be the number of decimal digits. The first scan advances at most `d` positions. The repair loop moves only left, at most `d` positions, and the suffix-fill loop moves only right across at most `d` positions.

The total time is `O(d)`.

The mutable character list and joined string contain `d` characters, so auxiliary space is `O(d)`. The number of scalar indices is constant. Strings are used to make individual digits mutable through the list representation.

## Alternatives and edge cases

- **Try every smaller number:** Decrement `n` until finding a monotone candidate. This can inspect an enormous number of integers and is far slower than repairing digits directly.

- **Construct the answer with digit dynamic programming:** A tight-prefix DP can maximize a monotone sequence under the upper bound. It is general but significantly more complex for a property solved by one greedy repair.

- **Decrement only the first offending digit once:** This fails when the decrement creates a new descent to its left, as in `332`. The repair must propagate.

- **Fill the suffix with zeroes:** That would produce a valid but unnecessarily small result. Once the prefix is smaller, nines maximize the answer.

- **Already monotone input:** The scan reaches the end, so the original number is returned unchanged.

- **Repeated equal digits:** Equality is allowed. The initial scan continues across equal adjacent digits.

- **A chain of descents:** The backward loop can propagate all the way to the leading digit.

- **Input ten:** The internal `"09"` converts to integer 9, removing the leading zero automatically.

- **Input zero:** A single digit is vacuously monotone and is returned.

- **Upper bound `10^9`:** The digit-based reasoning is independent of the numeric magnitude and uses only the short decimal representation.
