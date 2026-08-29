## General

**Translate “elements repeat” into a quantity a window can maintain**

A subarray is semi-repeating when at most `k` distinct values appear more than once inside it. The word “elements” is easy to misread here. We are not counting every occurrence after the first. For example, in `[7, 7, 7, 7]`, only one distinct value repeats: the value `7`. Its frequency is four, but it contributes exactly one to the number of repeating values. Likewise, `[1, 1, 2, 2, 2, 3]` has two repeating values, `1` and `2`.

That definition suggests storing a frequency for every value currently inside a contiguous window. Let the window be `nums[l:r + 1]`. The dictionary `cnt` records how many times each value occurs in this window, while `cur` records how many dictionary entries have frequency at least two. With these two pieces of state, the window is valid precisely when `cur <= k`.

The direct but slow strategy would start a subarray at every index, extend it to the right, and count repeating values for each start. Even if the frequencies are updated incrementally for one fixed start, trying every start can inspect quadratically many subarrays. Since `nums.length` can be `10^5`, an `O(n^2)` method is too expensive. A sliding window avoids restarting because adding a new rightmost element cannot make an already invalid window valid. If an extension creates too many repeating values, the only useful move is to discard values from the left.

**Why only two frequency transitions change `cur`**

When the loop reaches a right endpoint `r` with value `x`, it first executes `cnt[x] += 1`. There are three meaningful cases:

- A frequency changes from zero to one. The value appears only once, so it is not repeating and `cur` must not change.
- A frequency changes from one to two. The value has just become a repeating value, so `cur` must increase by one.
- A frequency changes from two to three, three to four, or any larger transition. The value was already counted among the repeating values, so `cur` must not increase again.

This is exactly why the source uses `cur += cnt[x] == 2`. In Python, a Boolean behaves as the integer `1` when true and `0` when false. Therefore that expression adds one only on the transition to frequency two. It does not count excess copies.

Removing the leftmost value is the mirror image, but the order of operations matters. The code first performs `cnt[nums[l]] -= 1` and then evaluates `cnt[nums[l]] == 1`. If the new frequency is one, the old frequency was two. That value has just stopped repeating, so `cur` must decrease by one. A change from one to zero does not affect `cur` because the value was not repeating before removal, and a change from four to three does not affect it because the value still repeats. Thus `cur -= cnt[nums[l]] == 1` is the exact inverse transition.

**Restore the window after every extension**

After adding `nums[r]`, the window might have `cur > k`. The `while` loop repeatedly removes `nums[l]` and advances `l` until `cur <= k` again. A `while` loop is necessary rather than a single `if`: removing one occurrence does not always stop a repeated value from repeating. If one value occurs many times, several left removals may be required before its frequency falls from two to one; other leftmost values may also be unrelated to the excess repeated value.

At the end of this shrinking phase, three facts hold:

1. `cnt` contains the frequencies in exactly `nums[l:r + 1]`.
2. `cur` is exactly the number of distinct values with frequency at least two in that window.
3. `cur <= k`, so the current window is a legal semi-repeating subarray.

The code can therefore compare its length, `r - l + 1`, with `ans`.

**Why this window contains the best answer ending at `r`**

For a fixed right endpoint, a smaller left endpoint gives a longer subarray. The algorithm advances `l` only while the current window is invalid. Once the window becomes valid, it stops immediately. Consequently, `l` is the earliest left boundary still available after repairing all violations caused by the processed extensions.

Another way to see the argument is to focus on every left boundary that the loop discards. At the moment the algorithm advances past such a boundary, the window ending at the current `r` has more than `k` repeating values. Extending that same left boundary to an even later right endpoint cannot reduce any existing frequency, so it cannot reduce the number of repeating values. That boundary can never begin a valid future answer and is safe to discard permanently.

The current repaired window is therefore the longest valid window ending at `r`. The outer loop tries every possible right endpoint, and `ans` remembers the largest of these endpoint-specific best lengths. This proves that the returned value is the length of the longest semi-repeating subarray anywhere in `nums`.

**Walk through the first example**

For `nums = [1, 2, 3, 1, 2, 3, 4]` and `k = 2`, the first occurrences of `1`, `2`, and `3` leave `cur = 0`. Adding the second `1` changes its frequency from one to two, so `cur` becomes one. Adding the second `2` makes `cur = 2`, and the length-six prefix remains valid.

Adding the second `3` makes `cur = 3`, which is too large. The left side must move. Removing the first `1` changes its frequency from two to one, so `cur` returns to two and shrinking stops. The repaired window is `[2, 3, 1, 2, 3]`. The final `4` can then be appended without changing `cur`, producing `[2, 3, 1, 2, 3, 4]` of length six. No discarded left boundary could form a valid longer window ending later, which is why the one forward scan suffices.

## Complexity detail

Let `n` be the length of `nums`. The right pointer visits each index exactly once. The left pointer also moves only forward and can pass each index at most once across the entire run. Although the `while` loop is nested inside the `for` loop, it does not restart from the beginning for each `r`. There are at most `n` additions and at most `n` removals, so the total expected time is `O(n)` when dictionary access has expected `O(1)` cost.

The dictionary may hold a key for every distinct value encountered. The implementation reduces counts to zero but does not delete zero-count keys, so a value that has left the window can remain stored. Across the full input there can be `n` distinct values, giving `O(n)` auxiliary space in the worst case. The other variables—`ans`, `cur`, `l`, `r`, and `x`—use `O(1)` space.

The constraint `1 <= nums[i] <= 10^5` would also permit a fixed frequency array of size `100001`. That would make frequency access worst-case `O(1)` and use `O(10^5)` space. The dictionary instead allocates entries only for values that actually occur, while retaining the stated `O(n)` worst-case bound relative to the input length.

## Alternatives and edge cases

- **Quadratic enumeration:** Fixing every left endpoint and extending every possible right endpoint can maintain frequencies correctly, but it still examines `O(n^2)` subarrays and is not suitable for `n = 10^5`.
- **Frequency array instead of a dictionary:** Because values are bounded by `10^5`, an indexed array is a valid alternative with the same `O(n)` time. It trades predictable access for space proportional to the entire value domain rather than the number of observed values.
- **Count duplicate occurrences instead of repeated values:** A counter such as “window length minus number of distinct values” answers a different question. Four copies of one value would contribute three duplicates even though this problem counts only one repeating value.
- **Increment `cur` whenever a frequency exceeds one:** Using `cnt[x] >= 2` after insertion would add again for the third and later copies. The only insertion transition that creates a newly repeating distinct value is `1 -> 2`.
- **Decrement `cur` before reducing the left frequency:** Testing the old frequency against one would detect the wrong transition. The source decrements the frequency first and tests whether the new frequency is one, thereby recognizing exactly `2 -> 1`.
- **`k = 0`:** No value may repeat. The method becomes the familiar longest subarray with all distinct values; whenever a frequency reaches two, the left side moves until that frequency returns to one.
- **A single value repeated many times:** The whole array is valid when `k >= 1` because only one distinct value repeats, regardless of how many copies it has. With `k = 0`, the maximum length is one.
- **`k` at least the number of distinct input values:** The entire array is valid. The shrink loop never needs to remove anything, and `ans` eventually becomes `n`.
- **Length-one input:** Its only value has frequency one, so `cur = 0` and the algorithm returns one for every permitted `k`.
- **Missing imports in the stored source:** The exact solution uses `List` and `defaultdict` without importing them in this file. Its algorithm assumes the execution harness supplies `List` and that `defaultdict` is available; standalone Python would need imports from `typing` and `collections` respectively.
