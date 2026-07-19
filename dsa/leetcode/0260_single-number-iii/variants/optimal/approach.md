## General
**Pair cancellation reveals how the singletons differ**

XOR every value. Paired values cancel, leaving `first ^ second`. Its lowest set bit identifies a position on which the two singleton values differ.

**One set bit separates the two unknown values**

XOR values into two groups according to the distinguishing bit. Equal pairs enter the same group and cancel; the two singletons enter different groups.

**Each partition cancels independently**

After any prefix, each group accumulator equals the XOR of values assigned to that group. At completion all pairs contribute zero, leaving exactly one singleton in each accumulator. The selected bit guarantees they cannot land together.

## Complexity detail
Two linear passes take $O(n)$ time. The total XOR, mask, and two accumulators use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Frequency map:** takes linear time but $O(n)$ extra space.
- **Count every candidate:** can take $O(n^2)$.
- XOR and the lowest-set-bit operation work for zero and negative Python integers as well.
