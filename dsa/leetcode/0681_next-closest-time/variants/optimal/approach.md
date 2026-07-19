## General
**Generate displays from the allowed digits**

Remove the colon and take the set of displayed digits. Enumerate every four-position selection with repetition from this set. At most four digits are available, so there are at most $4^{4} = 256$ arrangements.

**Reject arrangements that are not valid times**

Interpret the first two selected digits as an hour and the last two as a minute. Keep only hours below 24 and minutes below 60. Convert each valid display to minutes since midnight.

**Measure forward distance on the daily cycle**

For a candidate minute value, compute its forward difference from the input modulo 1,440. A zero difference represents the same display on the next day, so treat it as 1,440 rather than zero. Choose the valid candidate with the smallest positive cyclic difference. The original display is always constructible, guaranteeing a fallback after one full day.

**Why the chosen candidate is the next time**

Enumeration covers every display using only allowed digits, including repeated uses, and validity filtering removes exactly the impossible clock readings. Modular distance is precisely the number of forward minutes required to reach each remaining display. Minimizing that positive distance therefore returns the first legal display encountered in time order.

## Complexity detail
The clock domain and the number of input digit positions are fixed. At most 256 arrangements are generated, each with constant work, so time and auxiliary space are both $O(1)$ with respect to input size.

## Alternatives and edge cases
- **Advance one minute at a time:** test each new display until its digits are allowed; it is simple and bounded by 1,440 iterations, but runtime depends on the cyclic waiting distance.
- **Scan all 1,440 clock displays:** collect valid candidates and select the minimum cyclic distance; this is also constant for the fixed clock domain but performs more work than digit enumeration.
- **Greedily increment individual positions:** can be fast, but hour and minute validity plus carry and wrap rules make the case analysis error-prone.
- The returned time must be strictly later, so the identical display represents the next day's occurrence.
- Input digits may be reused more times than they originally appeared.
- Leading zeros are display digits and must be preserved in the returned `HH:MM` format.
