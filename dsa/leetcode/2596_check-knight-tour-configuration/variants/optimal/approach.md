## General

**Invert the visit-order matrix.** The board stores the move number at each coordinate, but validation needs the coordinate of each move number. Create `positions` so that `positions[k]` is the cell containing `k`. The uniqueness and range guarantees make this a complete inverse mapping after one matrix scan.

**Validate the recorded sequence.** First require `positions[0]` to be `(0, 0)`. Then inspect every consecutive pair `positions[k - 1]` and `positions[k]`. A knight move is legal exactly when the absolute row and column changes are one and two in either order.

The inverse mapping contains every visit exactly once, so the loop checks every transition in the claimed tour and no unrelated pair. If all transitions pass and move zero has the required location, the matrix describes the required complete tour. Conversely, a wrong start or any illegal transition is directly detected and makes the configuration invalid.

## Complexity detail

The board has $n^2$ cells. Constructing the inverse mapping visits each cell once, and validating the $n^2-1$ transitions takes another linear pass over the moves. The total time is $O(n^2)$ and the coordinate mapping uses $O(n^2)$ auxiliary space.

## Alternatives and edge cases

- **Repeated matrix search:** Locate each next move by scanning the whole board. This avoids the inverse array but costs $O(n^4)$ time in the worst case.
- **Direction-set lookup:** The eight signed knight offsets can be stored in a set and queried for each transition; checking the sorted absolute differences is equivalent and needs no direction table.
- **Wrong starting cell:** Legal transitions alone are insufficient because the specification separately requires move zero at the top-left cell.
- **Late invalid transition:** Every consecutive pair must be checked; a path can remain legal until its final move and still be invalid.
- **Distinct labels:** Because the input guarantees every value in the required range occurs exactly once, duplicate and missing labels do not require separate validation.
