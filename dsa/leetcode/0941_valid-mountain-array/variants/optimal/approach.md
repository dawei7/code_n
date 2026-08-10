## General

**Turn the definition into two monotone walks**

A valid mountain must have one internal peak. Every step before that peak is strictly upward, and every step after it is strictly downward. There can be no flat step, no second rise after descending begins, and neither endpoint may be the peak.

The solution approaches the unknown peak from both ends:

- pointer `i` walks right across the strictly increasing prefix;
- pointer `j` walks left across the strictly decreasing suffix.

If these two maximal walks meet at the same internal index, that index is the single valid peak and the whole array has the required shape.

**Reject arrays that are too short**

An array needs at least three elements to have a first slope, an internal peak, and a second slope. The explicit `n < 3` check returns false immediately.

This guard also makes the later boundary expressions easier to reason about. Once the two pointer loops run, there is at least one possible internal index.

**Walking up from the left**

The first loop advances while `i + 1 < n - 1` and `arr[i] < arr[i + 1]`. The first condition keeps the pointer from walking onto the final element, and the second requires a strictly increasing step.

When it stops, `i` is the last index reachable from the left through strict increases, subject to remaining before the last position.

The boundary `i + 1 < n - 1` is slightly unusual. A more common version walks as far as possible and then explicitly rejects a peak at the last index. This implementation instead prevents `i` from moving beyond `n - 2`. Consequently, an entirely increasing array ends with `i = n - 2` rather than `n - 1`. The right pointer remains at `n - 1`, so they do not meet and the array is rejected.

Any equality stops the walk because a mountain is strictly increasing, not non-decreasing.

**Walking down from the right**

The second loop moves `j` left while `j - 1 > 0` and `arr[j - 1] > arr[j]`. The first condition keeps it from walking onto the first element. The comparison means the pair is a strict descent when read from left to right.

When this loop stops, `j` is the earliest index from which the suffix descends strictly to the final element, while remaining after index zero.

For an entirely decreasing array, the loop stops at `j = 1` rather than moving to zero. The left pointer stays at zero, so the final equality fails. This is the symmetric protection against using the first element as a peak.

**Why meeting means the entire array is covered**

Suppose `i == j == p`.

The left walk proves every adjacent pair from index zero through `p` is strictly increasing. The right walk proves every adjacent pair from `p` through the last index is strictly decreasing. Because `i` can never be the last index and `j` can never be the first, `p` is internal. These statements are exactly the definition of a mountain array.

Now suppose the array is a valid mountain with peak `p`. Every step before `p` is increasing, so the left pointer reaches `p`. It cannot pass `p` because the next step is decreasing. Every step after `p` is decreasing, so the right pointer reaches `p` and cannot pass it. Thus the pointers meet.

The equality test is therefore both sufficient and necessary.

**Examples of invalid shapes**

For `[0, 3, 2, 1]`, the left walk stops at index one and the right walk also reaches index one, so the method returns true.

For `[3, 5, 5]`, the left walk reaches index one, but the right walk cannot cross the equal pair and remains at index two. They do not meet.

For `[0, 2, 1, 3]`, the left walk stops at the first local peak while the right walk stops at the start of the final increasing portion. A valley or second ascent remains between the pointers, so equality fails.

For a strictly increasing or strictly decreasing array, the artificial endpoint limits leave the pointers one position apart rather than accepting an endpoint as a peak.

## Complexity detail

Let `n` be the array length.

Pointer `i` moves only right and at most `n - 2` times. Pointer `j` moves only left and at most `n - 2` times. No pointer reverses direction and every comparison is constant time, so total time is `O(n)`.

The algorithm stores the length and two integer pointers. It does not allocate an auxiliary array, stack, or set, so auxiliary space is `O(1)`.

Although the two scans are written separately, their combined work is still linear rather than two-dimensional. `O(n) + O(n)` simplifies to `O(n)`.

## Alternatives and edge cases

- **One pointer in two phases:** Walk upward, reject if the peak is an endpoint, then walk downward and require reaching the last index. This is the most common formulation and has the same `O(n)` time and `O(1)` space.
- **Track a phase flag:** Scan adjacent differences once, changing from rising to falling at most once. This can work, but it needs careful checks that both phases occurred and that equality is never allowed.
- **Count sign changes:** Compute differences and verify a positive block followed by a negative block. Materializing the difference array adds `O(n)` space unnecessarily.
- **Length below three:** Always false because no internal peak with two sides can exist.
- **Exactly three elements:** The only valid form satisfies `arr[0] < arr[1] > arr[2]`. The two pointers meet at index one precisely in that case.
- **Plateau on either side or at the top:** Equality makes both strict loops stop. The remaining gap prevents acceptance.
- **Strictly increasing input:** The last element would be the only peak candidate, which is forbidden. The loop boundary keeps `i` at `n - 2` and the pointers differ.
- **Strictly decreasing input:** The first element would be the only peak candidate. The right boundary keeps `j` at one and the pointers differ.
- **Multiple peaks:** The left pointer stops at the first failed increase, while the right pointer stops at the last failed descent. They cannot cover the entire middle with one shared index.
- **Valley shape:** Neither monotone walk can cross the central change from decreasing to increasing, so the pointers do not meet.
- **Repeated numeric values far apart:** Repeating a value is not itself forbidden; only adjacent steps must remain strict in the required directions. The pointer comparison enforces the actual local slopes.
