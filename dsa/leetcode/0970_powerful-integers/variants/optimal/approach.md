## General
**Enumerate each distinct power once.** Build the sequence beginning at `1`. When a base is greater than `1`, repeatedly multiply by that base while the next power is no larger than `bound`. When the base equals `1`, stop immediately because every exponent produces the same value.

**Combine the finite power sequences.** Visit every pair from $P_x\times P_y$. If `x_power + y_power <= bound`, insert the sum into a set. The set removes collisions caused by different exponent pairs without affecting the unrestricted result order.

**Why larger powers can be ignored.** Both powers are positive. Once one power already exceeds `bound`, adding any power of the other positive base cannot restore a valid sum. The generated finite sequences therefore contain every power that might participate, and the Cartesian enumeration considers every qualifying exponent pair.

## Complexity detail
Generating the two sequences costs $O(A+B)$, and their Cartesian product contains $AB$ pairs, so total time is $O(AB)$. The two power lists and the set of $R$ answers use $O(A+B+R)$ space.

## Alternatives and edge cases
- **Nested multiplication loops:** Advance powers directly inside two loops and break when each base stops growing. This has the same asymptotic cost but needs explicit `base == 1` guards to avoid infinite loops.
- **Linear result deduplication:** Store answers in a list and scan it before each insertion. It remains correct but can add a factor of $R$ to the running time.
- **Enumerate exponent bounds blindly:** Trying a fixed exponent range works only when that range is proved sufficient for every allowed base and bound.
- **Base equals one:** Its distinct power sequence contains only `1`, regardless of exponent.
- **Bound below two:** No powerful integer qualifies because the smallest possible sum is $1+1=2$.
- **Duplicate sums:** Return a value once even if multiple exponent pairs generate it.
