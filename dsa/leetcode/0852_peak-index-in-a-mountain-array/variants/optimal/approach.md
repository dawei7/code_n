## General

**Use the slope to decide which half contains the peak**

A valid mountain array strictly rises to one peak and then strictly falls. At any internal index `mid`, comparing `arr[mid]` with `arr[mid+1]` reveals the side:

- if `arr[mid] < arr[mid+1]`, we are on the rising slope, so the peak lies strictly to the right;
- if `arr[mid] > arr[mid+1]`, we are at the peak or on the falling slope, so the peak lies at `mid` or to the left.

This monotone change from rising edges to falling edges enables binary search.

**Restrict the initial search to valid peak positions**

The mountain definition guarantees the peak is neither the first nor last element. The code initializes:

`left = 1` and `right = len(arr) - 2`.

This also guarantees `mid+1` is always in bounds.

**Search invariant**

At the start of every loop, the true peak index lies in the inclusive interval `[left,right]`.

The midpoint is:

`(left + right) >> 1`,

which is integer floor division by two for these nonnegative indices.

**Descending edge keeps `mid`**

If `arr[mid] > arr[mid+1]`, the edge immediately after `mid` descends. The peak cannot lie to the right of `mid`, because everything after the peak is descending and a rising-to-peak path would require the next edge to rise if the peak were farther right.

`mid` itself may be the peak, so the update is `right = mid` rather than `mid-1`.

**Rising edge discards `mid`**

Otherwise, the valid mountain guarantee means `arr[mid] < arr[mid+1]`; there are no equal adjacent values on the mountain slopes.

The peak must lie strictly to the right, so `left = mid + 1`. Index `mid` cannot be the peak because its next value is larger.

Both updates preserve the invariant and strictly shrink the interval.

**Termination**

The loop stops when `left == right`. The invariant says the peak lies in this one-index interval, so that index is returned.

There is no need for a final neighbor check: the binary-search proof has already isolated the unique peak.

**Trace `[0,2,5,3,1]`**

Search begins at indices 1 through 3.

- `mid=2`, and `arr[2]=5 > arr[3]=3`, so the peak is at or left of 2; set `right=2`.
- Now `left=1,right=2`, so `mid=1`. `arr[1]=2 < arr[2]=5`, so set `left=2`.

Both boundaries meet at index 2, the peak.

**Why the method is correct**

Before the peak, every edge points upward; starting at the peak and afterward, the edge to the next element points downward. The predicate “`arr[i] > arr[i+1]`” is therefore false on indices before the peak and true from the peak onward.

The algorithm is binary searching for the first true index of that monotone predicate. Its updates are exactly the standard first-true search, so it returns the unique peak.

To see why no candidate is accidentally discarded, suppose the peak is `p`. On a rising comparison at `mid`, strict mountain order implies `mid < p`, so every index through `mid` is safely removed. On a descending comparison, `mid >= p`, so every index after `mid` is safely removed while `mid` remains available in case `mid=p`. Hence, every update removes only indices proven not to be `p`. Because the interval length decreases on every iteration, it must eventually shrink to the still-preserved peak.

The chosen midpoint also cannot equal the current right boundary while `left < right`, because floor averaging makes `mid < right`. Consequently, reading `arr[mid+1]` stays within the search interval and within the array throughout the loop.

## Complexity detail

Each iteration reduces the inclusive search interval to at most about half its previous size. Starting from `O(n)` indices, this requires `O(\log n)` iterations.

Every iteration performs constant work, so time is `O(\log n)`.

Only `left`, `right`, and `mid` are stored, giving `O(1)` auxiliary space.

The array is accessed but never copied or modified.

## Alternatives and edge cases

- **Linear scan for the maximum:** The peak is the unique maximum, so scanning works in `O(n)` time but misses the requested logarithmic target.

- **Compare with both neighbors:** It can identify a peak at one midpoint but still needs slope logic to choose a half. Comparing only `mid` and `mid+1` is sufficient.

- **Peak at index 1:** It is included in the initial range and can become the first true descending-edge index.

- **Peak at index `n-2`:** It is also included, and rising comparisons move `left` toward it.

- **Three-element mountain:** Initial left and right both equal one, so the loop skips and returns the center.

- **No equal adjacent values:** Guaranteed by the mountain shape; the `else` branch safely represents a rising edge.

- **Why not search endpoints:** A valid mountain's endpoints cannot be the peak, and excluding them keeps `mid+1` safe.

- **Use `right=mid`:** Necessary because `mid` may be the peak on a descending comparison.

- **Use `left=mid+1`:** Safe because a rising edge proves `mid` is not the peak.

- **Large values:** Only comparisons matter; magnitude does not affect complexity.

- **Input validity:** The code relies on the guaranteed mountain shape and does not handle arbitrary multiple-peak arrays.
