## General
**Start from the mandatory index**

Every good subarray contains `k`, so begin with the one-element window `[k, k]`. Track its left and right endpoints, its current minimum, and the best score seen. Each expansion preserves the good-subarray condition automatically and adds exactly one new value.

**Cross the less damaging boundary first**

When both sides remain available, compare `nums[left - 1]` with `nums[right + 1]` and expand toward the larger value. If the smaller boundary were taken first, the window minimum could fall earlier. Taking the larger boundary cannot lower the minimum more, and any later interval that crosses the smaller boundary can still include this larger value at no additional loss of minimum. Thus the two expansions can be exchanged so the larger boundary comes first without reducing any attainable score.

If only one side remains, expansion must continue there. After each step, update the minimum with the newly included endpoint and test `minimum * (right - left + 1)`.

**Reach the widest window at every threshold**

Consider a value $x$ encountered as the current minimum. The greedy rule consumes every adjacent value at least $x$ before it crosses a boundary below $x$: whenever one boundary is below $x$ and the other is not, the other is larger and is selected.

The resulting window is therefore the widest contiguous interval containing `k` that can be reached without lowering the minimum below $x$. No good subarray whose minimum is at least $x$ can extend past either blocking boundary, so none can combine threshold $x$ with a greater length. The algorithm evaluates this maximal product for every threshold it crosses, including the threshold belonging to an optimal subarray, which proves that the largest recorded score is optimal.

## Complexity detail
Each iteration moves `left` or `right` outward once. Across the entire run, the two pointers cross the other $n-1$ indices exactly once, so the time is $O(n)$. The endpoints, current minimum, and best score are scalar values, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate every good interval:** Trying all $i \le k \le j$ and maintaining minima is correct but takes $O(n^2)$ time.
- **Monotonic-stack boundaries:** Previous- and next-smaller indices identify the widest interval for which each value is a minimum; filtering intervals that contain `k` also takes $O(n)$ time but requires $O(n)$ space.
- **Binary search by threshold:** Testing the reachable interval for selected minimum values can work with additional preprocessing, but is more complex and generally costs an extra logarithmic factor.
- **Single element:** When $n=1$, the singleton value is the score and no expansion occurs.
- **`k` at an endpoint:** One expansion direction is unavailable from the start, so the window grows only toward the other side.
- **Equal neighbors:** Either direction is safe because both choices preserve the same next minimum.
- **Minimum located at `k`:** Every good subarray has minimum at most `nums[k]`; increasing length may still make the entire array optimal.
- **Positive values:** All scores are positive, so initializing the best score with the singleton at `k` is valid.
