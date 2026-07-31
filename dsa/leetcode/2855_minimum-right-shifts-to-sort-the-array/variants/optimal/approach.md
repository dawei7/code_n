## General

**A sorted rotation has at most one internal break**

Scan adjacent pairs from left to right. Within a sorted array rotated at one boundary, both pieces remain strictly increasing because all values are distinct. The only possible descent `nums[i] > nums[i + 1]` is where the larger prefix is followed by the smaller suffix. If a second descent appears, no cyclic shift can repair both breaks, so return `-1` immediately.

If the scan finds no descent, the array is already increasing and the minimum answer is `0`.

**Validate the cyclic boundary**

One internal descent is necessary but not sufficient. After moving the suffix to the front, the last value of that suffix is followed by the first value of the original prefix. Therefore `nums[-1]` must be smaller than `nums[0]`; otherwise the rotated order would still contain a descent at that join.

When this boundary comparison succeeds, the suffix `nums[i + 1:]` is the smaller increasing run and the prefix `nums[:i + 1]` is the larger increasing run. Moving the suffix to the front makes every adjacent pair increasing, so the rotation is valid. A right shift moves one suffix element to the front, hence moving the entire suffix requires exactly $n - i - 1$ shifts. No smaller number reaches the unique valid boundary.

## Complexity detail

Let $n$ be the length of `nums`. The algorithm examines each adjacent pair once, so it takes $O(n)$ time. It stores only the break index and loop variables, using $O(1)$ auxiliary space.

The benchmark uses legal lengths $n$ as `size`, spanning from 6 to 96. Each input is a valid rotation whose break occurs away from both ends, forcing a full scan. A correct brute-force method that tries every right shift and checks whether the entire array is sorted performs $O(n^2)$ work and fails the scaling verdict while still finishing all tiers.

## Alternatives and edge cases

- **Try every right shift:** Repeatedly rotate and test whether the array is sorted. This directly models the operation but requires $O(n^2)$ time and may allocate $O(n)$ space per rotation.
- **Sort and compare rotations:** Sort a copy, locate the possible boundary, and compare the implied rotation. This is correct but costs $O(n \log n)$ time and $O(n)$ additional space.
- **Locate the minimum:** The minimum value must begin the sorted rotation. Checking both increasing runs and their boundary from that index also works, but the descent scan expresses invalidity more directly.
- **Single element:** It has no descent and needs zero shifts.
- **Already sorted:** Return `0`, not $n$.
- **One internal descent with a bad wraparound:** An array such as `[2, 1, 4]` is still impossible because the suffix cannot precede the prefix in increasing order.
- **Two or more descents:** No single cyclic boundary can eliminate all of them.
