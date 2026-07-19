## General
**Track the current odd suffix**

Scan the array while maintaining the length of the consecutive odd run ending at the current position. An odd value extends that suffix by one; an even value makes the suffix length zero because no qualifying block can cross it.

**Stop when the threshold is reached**

When the suffix length reaches three, the last three processed positions are adjacent and odd, so return `true`. If the scan finishes without reaching three, every odd run in the array has length at most two and the answer is `false`.

The state exactly describes the current suffix after each element: resetting on an even value and extending on an odd one preserves that meaning. Consequently, reaching three is both sufficient and necessary for a qualifying block.

## Complexity detail
Each of the $n$ values is inspected once, so the time is $O(n)$. The algorithm stores only one integer streak counter, using $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Check every length-three window:** directly testing `arr[i:i + 3]` is also $O(n)$ because the window size is constant, but it performs repeated parity checks.
- **Repeatedly rescan every prefix:** this remains correct but performs $O(n^2)$ unnecessary work.
- Arrays shorter than three elements always return `false`.
- Exactly three odd values return `true`.
- An even value between odd values breaks the run completely.
- A qualifying run may begin at index zero or end at the final index.
- Longer odd runs still require only one successful length-three block.
- Parity, not positivity or magnitude, determines whether a value is odd.
