# K Empty Slots

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 683 |
| Difficulty | Hard |
| Topics | Array, Binary Indexed Tree, Segment Tree, Queue, Sliding Window, Heap (Priority Queue), Ordered Set, Monotonic Queue |
| Official Link | [LeetCode](https://leetcode.com/problems/k-empty-slots/) |

## Problem Description
### Goal
There are `n` bulbs arranged at positions `1` through `n`, initially all off. On day `i`, the bulb at position `bulbs[i]` turns on, and the array is a permutation so exactly one previously unlit bulb is activated each day.

Return the earliest one-based day on which two turned-on bulbs have exactly `k` bulbs between them and all `k` intermediate bulbs are still off. The endpoint positions therefore differ by $k + 1$. Return `-1` if no day ever satisfies this condition.

### Function Contract
**Inputs**

- `bulbs`: a permutation where `bulbs[day - 1]` is the position switched on that day
- `k`: the required number of unlit positions strictly between the two lit endpoints

**Return value**

- The earliest 1-based day satisfying the condition, or `-1` when no such day exists

### Examples
**Example 1**

- Input: `bulbs = [1,3,2], k = 1`
- Output: `2`

**Example 2**

- Input: `bulbs = [1,2,3], k = 1`
- Output: `-1`

**Example 3**

- Input: `bulbs = [2,1,3], k = 0`
- Output: `2`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Invert bloom order into a day per position**

Build `days[position]`, the day that position's bulb turns on. For endpoints `left` and `right = left + k + 1`, the first day both endpoints are lit is `max(days[left], days[right])`. The gap is valid exactly when every interior position has a later bloom day than both endpoints.

**Slide endpoints while invalidating windows early**

Begin with the first possible endpoint pair. Scan interior positions. If an interior bulb blooms before either endpoint pair is complete, the current window is invalid. That interior position can become the next left endpoint: any window starting between the old left and this earlier bulb would still contain that bulb, which blooms too soon, so those starts can be skipped.

**Recognize a window when the scan reaches its right endpoint**

Treat the right endpoint as the scan boundary. If no earlier interior position invalidated the window before the scan reaches `right`, record `max(days[left], days[right])` as a candidate day. Then move the left endpoint to this right endpoint and continue. Taking the minimum recorded candidate gives the earliest qualifying day.

**Why skipped windows cannot contain a better pair**

Suppose interior position `i` has a day smaller than at least one current endpoint. Every candidate window whose left endpoint lies after the current left but before `i`, and whose right endpoint reaches beyond `i`, contains this prematurely lit bulb. It cannot have an entirely dark interior when both endpoints are lit. Advancing to `i` therefore removes only impossible starts, so the single forward scan tests every potentially valid pair.

#### Complexity detail

Creating the inverse day array takes $O(N)$ time and space. The window scan only advances indices and never moves backward, so it performs $O(N)$ additional work. Total time is $O(N)$ and auxiliary space is $O(N)$.

#### Alternatives and edge cases

- **Monotonic deque over interior bloom days:** obtain each window's minimum interior day in amortized $O(1)$, giving another $O(N)$ solution with explicit window minima.
- **Ordered set of lit positions:** insert each daily position and inspect its immediate neighbors; it takes $O(N \log N)$ time with a balanced search tree.
- **Compare each new bloom with all earlier blooms:** is direct and can verify the gap, but takes $O(N^2)$ time.
- When $k = 0$, the endpoints are adjacent and there is no interior bulb to check.
- The answer is determined by the later endpoint day, not by either position order in `bulbs`.
- If $k + 2 > N$, no endpoint pair fits and the answer is `-1`.

</details>
