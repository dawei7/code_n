## General

**Identify the only possible maximum AND.** A one-element subarray containing the largest array value $M$ has bitwise AND $M$, so the optimum is at least $M$. Adding elements to an AND can only clear bits, never set new ones; consequently, no multi-element subarray can have an AND larger than each of its members and therefore none can exceed $M$. Thus the maximum possible AND is exactly the maximum element.

**Characterize subarrays that retain it.** For positive integers, a subarray has AND $M$ only if every element in it equals $M$. Any smaller element is numerically below $M$ and cannot contain all bits needed to produce $M$. Conversely, the AND of any run consisting entirely of $M$ remains $M$.

The problem therefore reduces to finding the longest consecutive run of the array maximum. Scan the array, incrementing the current run at each maximum and resetting it at every other value, while retaining the largest run observed.

## Complexity detail

Finding the maximum and scanning the array each take $O(n)$ time. The algorithm stores only the maximum and two run lengths, so it uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate all subarrays:** Incrementally computing every subarray AND is correct but costs $O(n^2)$ time.
- **Distinct-AND dynamic programming:** Tracking all AND values ending at each index is useful for broader AND problems, but it is unnecessary once the singleton maximum observation is established.
- **Single element:** Its singleton subarray is optimal, so the answer is 1.
- **All equal:** The entire array is one maximum-valued run.
- **Separated maxima:** Lower intervening values split the candidates into independent runs.
- **Unique maximum:** Only its singleton occurrence can attain the maximum AND.
