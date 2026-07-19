## General
**Interpret altitude as a prefix sum**

After processing the first $i$ gains, the current altitude is the sum of those $i$ values. There is no need to materialize every prefix sum: keep one running altitude and add each gain as its segment is traversed.

**Include the starting point in the maximum**

Initialize the best altitude to $0$, not to the first gain. After every update, compare the new running altitude with the best value. This ensures the answer remains $0$ when the entire route stays below its starting height, while still capturing a peak at any later point.

## Complexity detail
The scan performs one addition and one maximum comparison for each of the $n$ gains, taking $O(n)$ time. The running altitude and best altitude are the only additional values, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Build every prefix sum:** Storing all $n + 1$ altitudes and taking their maximum is correct but uses $O(n)$ extra space unnecessarily.
- **Recompute each prefix:** Summing `gain[:i]` separately for every point is correct but takes $O(n^2)$ time.
- **All negative gains:** The starting altitude $0$ is the answer because every later point is lower.
- **Zero gains:** Repeated equal altitudes remain valid candidates for the maximum.
- **Peak before the endpoint:** Tracking only the final altitude misses routes that climb and then descend.
- **Single segment:** Compare that one resulting altitude with the starting altitude.
