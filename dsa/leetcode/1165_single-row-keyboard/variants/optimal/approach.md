## General
**Index the fixed layout once.** Build a mapping from each letter to its index in `keyboard`. Since every lowercase English letter occurs exactly once, every character in `word` has one well-defined destination.

**Accumulate consecutive movements.** Set `current = 0` and `total = 0`. For each character in `word`, obtain its mapped destination, add `abs(destination - current)` to `total`, and then assign `current = destination`. This follows the typing process in order: after a character is typed, its key is precisely the starting position for the next movement.

The running sum contains the cost of every required move exactly once, including the initial move from index `0`. Therefore, after the final character, `total` is the requested typing time.

## Complexity detail
Building the position map scans the fixed $26$-character keyboard. The word scan performs constant work per character, so the total time is $O(26+m)=O(m)$. The map has exactly $26$ entries, which is $O(1)$ space because the alphabet is fixed.

## Alternatives and edge cases
- **Call `keyboard.index` for each character:** This is correct, but each lookup scans up to $26$ fixed positions; it remains $O(m)$ under this problem's fixed alphabet and differs only by a constant factor.
- **Simulate one-index steps:** Moving a cursor one position at a time also stays $O(m)$ because every movement is at most $25$, but directly adding the absolute difference is simpler.
- **Repeated letter:** Typing the same character consecutively adds zero after the first occurrence because the finger is already on its key.
- **First key:** A word beginning with `keyboard[0]` incurs zero initial movement.
- **Reversed layout:** Indices come from `keyboard`, not alphabetical order.
