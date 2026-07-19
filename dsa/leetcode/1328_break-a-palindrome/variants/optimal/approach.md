## General
**Prefer the earliest possible decrease**

Only positions before the midpoint need to be considered for a lexicographic decrease. If a character there is not `a`, replace the first such character with `a`. The mirrored character remains unchanged, so the result is not a palindrome, and changing the earliest reducible position dominates every change at a later position.

**Fall back to the smallest final increase**

If the entire left half is already `a`, no character before or at the decisive prefix can be decreased. Change the last character to `b`. This breaks symmetry while postponing the first difference as far right as possible and using the smallest increase from `a`.

For length 1, every replacement still produces a one-character palindrome, so return empty. Excluding the middle position from the first-half scan is essential for odd lengths: changing only the center would preserve the palindrome.

## Complexity detail
The scan examines at most half of the $n$ characters, and constructing the modified string copies $n$ characters. Time is $O(n)$ and the mutable character list uses $O(n)$ space.

## Alternatives and edge cases
- **Enumerate every replacement:** Testing candidates and checking each for symmetry is correct but takes $O(n^2)$ time even when only the first useful position matters.
- **Single-character input:** No valid result exists, so return the empty string.
- **Odd-length center:** Never choose it as the only change because the string remains palindromic.
- **All `a` characters:** Change the last character to `b`.
- **First character reducible:** Replacing it with `a` gives the greatest possible lexicographic improvement.
- **Exactly one replacement:** Even when the input is all `a`, returning it unchanged is not permitted.
