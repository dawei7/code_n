## General
**Invert bloom order into a day per position**

Build `days[position]`, the day that position's bulb turns on. For endpoints `left` and `right = left + k + 1`, the first day both endpoints are lit is `max(days[left], days[right])`. The gap is valid exactly when every interior position has a later bloom day than both endpoints.

**Slide endpoints while invalidating windows early**

Begin with the first possible endpoint pair. Scan interior positions. If an interior bulb blooms before either endpoint pair is complete, the current window is invalid. That interior position can become the next left endpoint: any window starting between the old left and this earlier bulb would still contain that bulb, which blooms too soon, so those starts can be skipped.

**Recognize a window when the scan reaches its right endpoint**

Treat the right endpoint as the scan boundary. If no earlier interior position invalidated the window before the scan reaches `right`, record `max(days[left], days[right])` as a candidate day. Then move the left endpoint to this right endpoint and continue. Taking the minimum recorded candidate gives the earliest qualifying day.

**Why skipped windows cannot contain a better pair**

Suppose interior position `i` has a day smaller than at least one current endpoint. Every candidate window whose left endpoint lies after the current left but before `i`, and whose right endpoint reaches beyond `i`, contains this prematurely lit bulb. It cannot have an entirely dark interior when both endpoints are lit. Advancing to `i` therefore removes only impossible starts, so the single forward scan tests every potentially valid pair.

## Complexity detail
Creating the inverse day array takes $O(N)$ time and space. The window scan only advances indices and never moves backward, so it performs $O(N)$ additional work. Total time is $O(N)$ and auxiliary space is $O(N)$.

## Alternatives and edge cases
- **Monotonic deque over interior bloom days:** obtain each window's minimum interior day in amortized $O(1)$, giving another $O(N)$ solution with explicit window minima.
- **Ordered set of lit positions:** insert each daily position and inspect its immediate neighbors; it takes $O(N \log N)$ time with a balanced search tree.
- **Compare each new bloom with all earlier blooms:** is direct and can verify the gap, but takes $O(N^2)$ time.
- When $k = 0$, the endpoints are adjacent and there is no interior bulb to check.
- The answer is determined by the later endpoint day, not by either position order in `bulbs`.
- If $k + 2 > N$, no endpoint pair fits and the answer is `-1`.
