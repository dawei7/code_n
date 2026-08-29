## General

**Start from the cheapest possible length-`n` string**

Every position must contain a lowercase letter, and the smallest letter `a` has numeric value one. Therefore any valid string of length `n` spends at least `n` total value. The source begins with exactly that baseline:

`ans = ['a'] * n`.

At this point, the string has numeric value `n`. The variable `d = k - n` is the additional value that still must be distributed. The constraints `n <= k <= 26n` guarantee

$$
0 \le d \le 25n.
$$

Each position currently holds `a` and can be increased by at most `25` before reaching `z`. Thus there is always exactly enough total capacity to place the remaining `d`.

**Why extra value belongs as far right as possible**

Lexicographic order is determined by the first position at which two strings differ. Keeping an earlier character smaller is more important than making any later character smaller. Therefore the additional numeric value should be pushed toward the right end, allowing the longest possible prefix to remain `a`.

Suppose a candidate has some extra value at an earlier position while a later position is not yet `z`. Moving one unit of value from the earlier character to that later character keeps the total numeric value unchanged. At the first affected position, the new string has a smaller character, so it is lexicographically smaller. Repeating this exchange shows that in an optimal string, later positions must be filled to `z` before an earlier position receives extra value.

This yields a simple shape: zero or more leading `a` characters, possibly one partially increased character, and then zero or more trailing `z` characters.

**Fill complete `z` characters from the end**

`i` starts at `n - 1`, the last index. While `d > 25`, more extra value remains than one position can hold. The method sets `ans[i] = 'z'`, which adds exactly `25` beyond that position’s baseline `a`. It subtracts `25` from `d` and moves `i` one step left.

The loop condition is strictly greater than `25`, not greater than or equal to it. Once `d` is at most `25`, the current one position can absorb all remaining value. Stopping there leaves every earlier position untouched at `a`, which is lexicographically best.

At the maximum input `k = 26n`, the initial extra value is `25n`. The loop fills the last `n - 1` positions with `z`, leaving `d = 25` and `i = 0`. The final step turns the first position into `z` as well. Thus the index never needs to move below zero for a valid input.

**Place the residual increment**

After the loop, `d` lies between zero and `25`. The current character `ans[i]` is still `a`. The expression

`chr(ord(ans[i]) + d)`

converts `a` to its integer character code, adds the residual offset, and converts back to a character. An offset zero keeps `a`; offset one produces `b`; offset `25` produces `z`. Since the residual stays within that range, the result is always a lowercase English letter.

For `n = 3` and `k = 27`, the baseline `"aaa"` costs three, leaving `d = 24`. The loop does not run because one position can hold all of it. Increasing the final `a` by `24` produces `y`, giving `"aay"`.

For `n = 5` and `k = 73`, the baseline costs five and leaves `68`. The loop spends `25` on the last position and another `25` on the previous one, leaving `18` at index two. Adding `18` to `a` produces `s`, so the result is `"aaszz"`.

**Why the numeric value is exact**

Initially the array contributes `n`. Every loop iteration changes one `a` of value one into `z` of value 26, increasing the total by `25`, and reduces `d` by the same amount. The final character change increases the total by the remaining `d`. All of the original `k - n` extra units are therefore used exactly once, making the final numeric value `k`.

**Why the result is lexicographically smallest**

The construction places extra value in the latest available position until that position reaches its maximum, then moves left only when necessary. Consequently no positive increment can be moved from an earlier position to a later non-`z` position. If another valid string differed first at some index and were smaller there, it would have to move the missing value to later positions. But the constructed suffix is already using the maximum capacity forced by the remaining total, so those later positions cannot absorb enough value. Such a smaller first differing character is impossible.

Equivalently, at every prefix boundary the method leaves the smallest value in the prefix that still allows the suffix, whose capacity is `26` per position, to achieve the required total. This greedy choice is feasible and lexicographically optimal at every step.

Finally, `''.join(ans)` converts the character list into the required string without changing order or values.

## Complexity detail

Allocating `ans` with `n` copies of `'a'` takes $O(n)$ time. The loop moves `i` left at most `n - 1` times, and the residual assignment is constant time. Joining the `n` characters into the return string takes another $O(n)$ time. Total running time is $O(n)$.

The character list uses $O(n)$ space, and the returned immutable string also contains `n` characters. Peak memory remains $O(n)$. If output storage is excluded from auxiliary-space conventions, the mutable list itself still makes this exact Python implementation $O(n)$ auxiliary space.

Only `i` and `d` are scalar working variables. The algorithm does not use recursion, sorting, or a search over possible strings.

## Alternatives and edge cases

- **Greedy construction from the left:** At each position, choose the smallest character that leaves at most `26` value for every remaining position and at least one for each. This is also $O(n)$ and correct, but its feasibility formula is slightly less intuitive than filling extra value from the right.
- **Fill all `a` characters and scan every position backward:** Add `min(d, 25)` at each index until `d` becomes zero. This is nearly identical; the exact source accelerates full increments with a loop and performs one residual assignment afterward.
- **Enumerate strings or use dynamic programming:** Both are unnecessary because lexicographic order and uniform per-position bounds give a direct greedy exchange argument. Enumeration is exponential.
- **Minimum value `k == n`:** Then `d == 0`, the loop is skipped, the last `a` remains unchanged, and the answer is all `a` characters.
- **Maximum value `k == 26n`:** Every position becomes `z`, including the first position in the residual step.
- **Residual exactly `25`:** The strict loop condition stops and the final assignment turns the current position into `z`. This avoids an extra iteration but produces the same correct suffix.
- **Residual zero after baseline:** `chr(ord('a') + 0)` safely writes `a` again.
- **Single-character string:** `d` is between zero and `25`, so the loop never moves left and the final assignment directly selects the letter of value `k`.
- **Large `n`:** Work and storage grow linearly up to the $10^5$ constraint; there is no recursion-depth or combinatorial issue.
- **Why not fill from the left:** Spending extra value early makes the first differing character larger even when later positions still have capacity, so it cannot produce the lexicographically smallest result.
- **Input feasibility:** The bounds on `k` are necessary. Below `n` no length-`n` lowercase string has small enough value, and above `26n` the positions lack sufficient capacity; the source relies on the guarantee rather than checking these cases.
