## General

**Partition the timer values by the source rules**

Two states occur at single timer values: `0` means `"Green"`, and `30` means `"Orange"`. Test those equality cases directly. The red state occupies the interval $30 < \texttt{timer} \le 90$, so it begins at `31` and includes `90`. If none of these three checks succeeds, the required result is `"Invalid"`.

These categories are mutually exclusive. They also cover every valid outcome named by the contract: the two isolated values are handled first, the complete red interval is handled next, and the final branch contains precisely the remaining legal values. Returning the corresponding string from each branch is therefore correct.

## Complexity detail

The method evaluates at most four integer comparisons for one scalar input, independent of the numeric value of `timer`. Its running time is $O(1)$, and it uses $O(1)$ auxiliary space.

There is no growing input collection or other scalable workload dimension. The bounded-domain certificate therefore replaces runtime tiers with a fixed-work proof and an exhaustive comparison of all $1{,}001$ legal timer values against an independent classification oracle.

## Alternatives and edge cases

- **Lookup table for every legal value:** A 1,001-entry table could answer each call in constant time, but it stores a fixed domain unnecessarily when four comparisons express the rules directly.
- **Special-value dictionary plus a range test:** A dictionary for `0` and `30` is also correct, but two explicit equality checks are simpler and avoid an extra data structure.
- **Strict lower red boundary:** `timer = 30` is orange, not red; the red test must use $30 < \texttt{timer}$.
- **Inclusive upper red boundary:** `timer = 90` is red, while `timer = 91` is invalid.
- **Values between special states:** Every value from `1` through `29` is invalid. Testing only `timer <= 90` for red would classify this region incorrectly.
- **Exact output spelling:** The required strings begin with capital letters and otherwise use lowercase letters; different capitalization is not equivalent.
