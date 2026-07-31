## General

Every valid operation removes the same number of `a` and `b` characters. Therefore, the difference between their counts never changes. If the initial counts are $A$ and $B$, any final string must contain at least $\lvert A-B\rvert$ characters; removals cannot eliminate the excess copies of the more frequent character.

That lower bound is always attainable. Whenever the current string contains both characters, some neighboring pair must be a transition, either `"ab"` or `"ba"`. Such a two-character substring is balanced, so it may be removed. Repeating this step eventually leaves only one kind of character, and its count is exactly $\lvert A-B\rvert$.

It is consequently unnecessary to simulate any choices. Scan `s`, add one to a balance for each `a`, subtract one for each `b`, and return the absolute value of the final balance.

## Complexity detail

Let $n = \texttt{s.length}$. The scan examines each character once, taking $O(n)$ time, and the balance uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Count with two totals:** Counting `a` and `b` separately is equally optimal; the final answer is the absolute difference between the totals.
- **Stack cancellation:** Pushing equal neighbors and canceling unlike neighbors also leaves the correct unmatched count, but uses $O(n)$ auxiliary space unnecessarily.
- **Repeated substring deletion:** Searching for and physically deleting balanced substrings is correct with suitable choices but can take $O(n^2)$ time because the string is repeatedly scanned or shifted.
- **Already balanced:** Equal total counts allow the entire string to be removed, so the answer is `0` regardless of character order.
- **Only one character:** No valid nonempty substring exists, and the original length is returned.
- **New adjacency after removal:** Joining the surviving prefix and suffix can create another removable transition; the proof uses this fact when repeatedly attaining the lower bound.
