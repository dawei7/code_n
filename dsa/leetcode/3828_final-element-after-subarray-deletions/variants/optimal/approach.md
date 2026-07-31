## General

Alice can finish the game on her first turn. Deleting the suffix `nums[1..N-1]` preserves only `nums[0]`, while deleting the prefix `nums[0..N-2]` preserves only `nums[N - 1]`. She can therefore guarantee at least the larger of the two original endpoints.

It remains to show that no interior value can give Alice a better guaranteed result. After any first move that leaves at least two elements, at least one original endpoint must still be present: a single proper contiguous deletion cannot remove both ends of the array. Any surviving original endpoint is still an endpoint of the shortened array. Bob can then delete every other element in one legal prefix or suffix move, ending the game with that endpoint. Its value is no greater than `max(nums[0], nums[-1])`.

Thus Alice can force the endpoint maximum and Bob can prevent every larger outcome. The minimax value is exactly `max(nums[0], nums[-1])`. When $N=1$, the two endpoint expressions refer to the same element and no move is needed.

## Complexity detail

The algorithm reads only the first and last array entries, so it takes $O(1)$ time and $O(1)$ auxiliary space, independent of $N$.

The benchmark defines size as the array length $N$. The accepted implementation and the independent same-class control both inspect only the endpoints, whereas the slower control traverses all $N$ entries before returning the same endpoint maximum.

## Alternatives and edge cases

- **Full minimax search:** Enumerating every legal deletion and alternating maximum and minimum choices models the game directly, but the branching search is exponential and cannot handle $N$ up to $10^5$.
- **Scan for the global maximum:** Alice cannot isolate a middle element in one move because that would require deleting both a prefix and a suffix. Bob can remove such an interior candidate, so `max(nums)` is generally wrong.
- **Interval dynamic programming:** Tracking all possible surviving intervals still performs unnecessary work; the immediate endpoint strategies already prove both matching bounds on the result.
- **Singleton array:** No deletion is possible or necessary, and the only element is both endpoints.
- **Two elements:** Alice removes one single-element prefix or suffix and directly keeps the larger value.
- **Equal endpoints:** Both optimal first moves yield the same guaranteed final value.
- **Large interior values:** Even an interior value larger than both endpoints does not change the answer, because Bob can prevent it from being the survivor.
