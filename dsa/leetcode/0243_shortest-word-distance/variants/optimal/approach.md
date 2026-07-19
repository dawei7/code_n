## General
**A new occurrence needs only the latest opposite occurrence**

Scan once, updating the most recent index of each target. Whenever both are known, their distance is the best distance ending at the newly seen target occurrence.

After index `i`, the two stored positions are the latest occurrences at or before `i`, and the answer is the minimum distance among every target pair whose later endpoint is at most `i`.

**Every optimal pair is considered at its later endpoint**

Fix a target occurrence as the later endpoint of a pair. Among all earlier occurrences of the other word, the most recent one has the greatest index and therefore the smallest distance. The scan checks precisely that occurrence. Repeating this for every possible later endpoint considers the best pair ending there, and the smallest of those candidates is the global optimum.

## Complexity detail
One scan takes $O(n)$ time, while two indices and the current minimum use constant space.

## Alternatives and edge cases
- **Store all occurrence indices:** works but uses $O(n)$ space.
- **Compare every pair:** can take $O(n^2)$.
- Adjacent targets yield one; repeated target occurrences continually tighten the candidate distance.
