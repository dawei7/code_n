## General

**Interpret positions after earlier deletions**

After processing original index $i$, exactly `i + 1 - deletions` values have been retained. Thus `i - deletions` is the position that `nums[i]` occupies in the retained prefix. When that position is even, `nums[i]` starts a new pair and the next retained value must differ from it.

**Reject only a value that cannot complete the pair**

If `nums[i]` starts a pair and equals `nums[i + 1]`, retaining both would violate beauty. Deleting the current value is always safe: the next equal value can serve as the same pair's first element, and keeping an earlier duplicate offers no advantage to any later choice. Count that deletion and reconsider parity through the adjusted retained index.

Otherwise the adjacent values can be retained as a valid pair, so no deletion at this boundary can improve the optimum. Continuing left to right greedily preserves the longest possible valid paired prefix. Every counted duplicate deletion is unavoidable for completing the current pair, while every accepted unequal neighbor completes it at the earliest possible point.

**Repair an unpaired tail**

After all boundaries are processed, the retained length may be odd. Its final value has no partner, and deleting exactly that one value makes the length even. Adding this tail deletion when necessary yields the minimum total.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The algorithm inspects each adjacent boundary once, taking $O(n)$ time.

Only the deletion count and loop index are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Physically delete from a list:** Simulating every shift is straightforward but can cost $O(n^2)$ time.
- **Build a retained stack:** Appending greedily retained values is also linear but uses $O(n)$ additional space.
- **Dynamic programming over subsequences:** It can model keep/delete choices but is unnecessary because the earliest unequal completion dominates later ones.
- **All equal values:** No unequal pair can be retained, so every element must be deleted.
- **Already beautiful:** No deletion is counted when all prescribed pairs differ and the length is even.
- **Odd retained length:** One final deletion is mandatory even when every completed pair is valid.
- **Single value:** The only beautiful result is the empty array, requiring one deletion.
