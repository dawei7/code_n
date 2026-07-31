## General

Define `prefix(bound)` as the total waviness of every integer from `1` through `bound`. The requested answer is `prefix(num2) - prefix(num1 - 1)`, so it is enough to aggregate all numbers no greater than one decimal bound without enumerating them.

A digit DP processes the bound from left to right. Its state records whether the constructed number has begun, its last two significant digits, and whether its prefix is still equal to the bound's prefix. Leading zeros do not belong to the number and therefore must not enter the neighbor history.

When a new significant digit is appended and two earlier significant digits exist, the formerly last digit now has both neighbors known. At that moment, test whether it is strictly greater than both or strictly less than both and add that contribution for every suffix represented by the transition.

Each state returns two quantities: the number of suffix completions and their total waviness. A transition adds the suffix total plus `added * suffix_count`, ensuring that a newly identified peak or valley is credited once to every completed number below that prefix. The last digit is never evaluated because no later digit arrives, exactly matching the rule that endpoints cannot contribute.

## Complexity detail

Let $D$ be the decimal digit count of the bound. There are only a constant number of states per position: two tightness choices and at most 11 possibilities for each remembered digit when the sentinel is included. Each transition tries ten digits. Treating the decimal alphabet as constant, the time and memoization space are both $O(D)$. Here $D\le16$.

## Alternatives and edge cases

- **Enumerate the range:** The direct Range I method is correct but cannot process an interval that may contain up to $10^{15}$ integers.
- **Iterative digit DP:** Carrying the same state counts in dictionaries avoids recursion and has the same $O(D)$ bound.
- **Leading zeros:** Padding shorter numbers to the bound's width must not create artificial neighbors or valleys before the first nonzero digit.
- **Fewer than three significant digits:** No transition ever has two prior digits, so the contribution remains `0`.
- **Equal neighbor:** The strict comparison fails when the candidate middle digit equals either neighbor.
- **Final digit:** It never becomes a middle digit and is deliberately not evaluated at the end of the DP.
- **Inclusive range:** Subtracting `prefix(num1 - 1)`, rather than `prefix(num1)`, retains the lower endpoint.
