## General
**The leftmost effective zero forces a decision:** Scan from left to right. Once position `i` is reached, no future flip starting to its right can change it. If its effective bit is zero, an optimal solution is therefore forced to start a length-`k` flip at `i`; if fewer than `k` positions remain, the task is impossible.

**Track only the parity of active flips:** A bit is inverted when an odd number of previously started windows still covers it. Maintain this parity instead of physically changing all `k` bits. When a forced flip starts, toggle the parity and mark its start position with a sentinel value. At index `i`, a marked start at `i - k` has just expired, so toggle the parity again before inspecting the current bit.

For an original binary bit, `nums[i] == parity` means that applying the active inversions produces zero, so a new flip is required. Every chosen flip is forced by the earliest unresolved zero; induction over the scan positions therefore proves both feasibility and minimality.

## Complexity detail
The scan performs constant work at each of the $N$ positions, giving $O(N)$ time. Reusing processed entries of `nums` as flip-start markers requires $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Physically toggle every chosen window:** The same greedy starts are correct, but changing all `k` entries per operation can take $O(Nk)$ time.
- **Difference or expiration array:** Recording where each flip ends also gives $O(N)$ time, but consumes $O(N)$ additional space.
- **Insufficient suffix:** If an effective zero occurs after the final legal start index, return `-1`.
- **Window length one:** Each zero must be flipped independently, so the answer is the number of zeros.
- **Already all ones:** No flip is needed regardless of `k`.
