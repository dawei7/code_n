## General
**Decode only from known character boundaries**

Start at index zero, which must be a character boundary. A `0` is a complete one-bit character, so advance one position. A `1` must begin either `10` or `11`, so advance two positions regardless of its second bit. Each jump therefore lands on the next character boundary.

**Stop before deciding the final zero**

Continue decoding only while the current boundary lies before the last array index. There are then two possibilities: a jump lands exactly on the final index, or the preceding two-bit character jumps over it to the end of the array.

**Why the landing position answers the question**

The scan never enters the middle of a character because every jump uses the length dictated by that character's leading bit. Consequently, landing on the final index proves its `0` starts its own one-bit character. Reaching the array length instead proves the final zero was already consumed as the second bit of a two-bit character.

## Complexity detail
Every iteration advances by at least one position, so at most $n - 1$ bits are inspected. The scan takes $O(n)$ time and stores only its current index, using $O(1)$ extra space.

## Alternatives and edge cases
- **Trailing-one parity:** count consecutive `1` bits immediately before the final zero; the last zero stands alone exactly when that count is even.
- **Dynamic programming over prefix boundaries:** it can mark reachable decode positions, but deterministic character lengths make the extra $O(n)$ storage unnecessary.
- **Repeated suffix rebuilding:** decoding the first character and copying the remaining suffix into a new list is correct but may take $O(n^2)$ total time.
- A one-element input `[0]` already consists of one one-bit character.
- If the scan reaches the second-to-last index and sees `1`, its two-bit character necessarily consumes the final zero.
- Zeros earlier in the array each form independent one-bit characters and do not affect later boundaries.
- Runs of `1` bits before the last zero are resolved by their parity, not merely by the immediately preceding bit.
