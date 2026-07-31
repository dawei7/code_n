## General

**Locate the maximal sequential prefix.** Begin its sum with `nums[0]`.
Continue while each next value equals its predecessor plus one, adding every
accepted value. Stop at the first violation; nothing after that point can
extend a prefix, so the accumulated sum is the required lower bound.

**Search by membership.** Insert every array value into a set. Starting at the
prefix sum, increment while the candidate belongs to the set. The first absent
candidate is returned. Every skipped integer is both at least the prefix sum
and present in `nums`, while the returned integer is absent, proving it is the
smallest valid answer.

## Complexity detail

The prefix scan and set construction each take $O(N)$ time. The candidate can
advance past at most the $N$ distinct stored values, so the complete time is
$O(N)$ with expected constant-time hash membership. The set uses $O(N)$ space.

## Alternatives and edge cases

- **Repeated list membership:** This is correct but can take $O(N^2)$ when many consecutive candidates occur late in the array.
- **Boolean presence table:** The bounded value domain supports a fixed array and also gives linear time.
- **Single element:** Its value is the prefix sum; if present, the answer advances by one.
- **Immediate break:** The first element alone defines the prefix when `nums[1]` is not `nums[0] + 1`.
- **Later consecutive values:** Values after the first break cannot rejoin the sequential prefix, though they still affect missing-value membership.
- **Duplicate values:** Duplicates do not change whether a candidate is present.
