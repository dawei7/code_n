## General

**Maintain frequencies for one sliding window**

There are `n - k + 1` contiguous windows of length `k`. Recounting every window from scratch costs `O(nk)`.

Adjacent windows differ by only two occurrences: one value enters from the right and one leaves from the left. Dictionary `cnt` stores the current frequency of every value, so the source updates those two counts in constant expected time.

The remaining challenge is retrieving:

1. The largest frequency.
2. Among values with that frequency, the smallest value.

A heap can maintain exactly this priority if each entry is

`(-frequency, value)`.

Python’s min-heap chooses the smallest tuple. A larger frequency produces a more negative first component and wins. When frequencies tie, the smaller value wins through the second component.

**Build the first window**

For every value in `nums[:k]`, the source increments its count and pushes its new state:

`(-cnt[x], x)`.

The same value may be pushed several times while its frequency rises. For example, three occurrences produce entries for frequencies one, two, and three.

Only the newest frequency is valid. Older entries remain in the heap and are removed lazily when they reach the top.

**Validate the heap top before using it**

The helper `get_mode` checks:

`-pq[0][0] == cnt[pq[0][1]]`.

The heap entry says its value has a stored frequency. The dictionary says its current actual frequency. If they differ, the entry is stale and is popped.

This repeats until the top agrees with current state. At that point, no valid entry can have a better priority:

- The heap ordering already places the greatest stored frequency and smallest tied value first.
- Stale entries above it have been discarded.
- Every count change pushes a fresh entry for the new frequency.

Thus the valid top represents the current window’s mode under the required tie rule.

The helper returns

`frequency * value`,

which is the window’s weight.

**Slide the window by one position**

For a new right endpoint `i`:

- `x = nums[i]` enters.
- `y = nums[i - k]` leaves.

The source increments `cnt[x]` and decrements `cnt[y]`, then pushes fresh heap entries for both updated values.

It is important to push the departing value as well. Its old high-frequency heap entry may otherwise continue to look authoritative until compared against the dictionary, and no new entry would represent its lower current priority.

If `x == y`, incrementing and decrementing cancel, leaving the same count. The source pushes two identical current entries. They are harmless duplicates: either can serve as the valid top, and lazy cleanup still preserves correctness.

After both changes, `get_mode` yields the new window’s weight, which is added to `ans`.

**Why lazy deletion is preferable to arbitrary heap updates**

Python’s standard heap supports efficient insertion and removal of the minimum element, but it does not provide a direct decrease-key operation or efficient deletion of an arbitrary tuple.

Trying to locate and edit the old entry for every frequency change could take linear time.

Lazy deletion turns each update into an ordinary `heappush`. Stale records are ignored when they matter—only when they rise to the top. Every pushed entry can be popped at most once, so cleanup remains efficient over the whole scan.

**Tie-breaking is encoded in the tuple**

Suppose values three and five both occur four times. Their heap entries are `(-4, 3)` and `(-4, 5)`. The first components tie, so Python compares the second and selects three.

If value five later reaches frequency five, its entry `(-5, 5)` becomes smaller than every frequency-four tuple and correctly becomes the mode despite its larger numeric value.

No separate tie-handling branch is needed.

**Trace the first example**

For window `[1, 2, 2]`, counts are `1 -> 1` and `2 -> 2`. The valid top is `(-2, 2)`, so weight is four.

Sliding to `[2, 2, 3]` decrements one and increments three. Value two remains at frequency two and still wins, producing another weight four. Their sum is eight.

**Trace a tied window**

For `[1, 2]`, both values have frequency one. Heap keys are `(-1, 1)` and `(-1, 2)`, so value one is selected and weight is one.

Every length-two window in `[1, 2, 1, 2]` has the same tie, giving total three.

**Why every heap answer is current**

After initialization and after every slide, the dictionary exactly matches the current window because it adds the entering occurrence and removes the leaving one.

Whenever a value’s count changes, a tuple for the new count is pushed. Therefore each current dictionary state has at least one matching heap record.

`get_mode` removes only records that disagree with the dictionary. Once it stops, the top is both current and lexicographically optimal under `(-frequency, value)`. This establishes the correct weight for every window.

## Complexity detail

Let `n` be the array length. Initialization pushes `k` entries. Each of the `n - k` slides pushes two more, so the heap receives `O(n)` entries total.

Every entry is pushed once and popped at most once. Each heap operation costs `O(log n)` in the worst case. Total time is `O(n log n)`.

The frequency dictionary contains at most `O(n)` distinct keys, including keys whose current count falls to zero because the source does not delete them. The lazy heap can also hold `O(n)` entries. Auxiliary space is `O(n)`.

Expected constant-time dictionary updates are dominated by heap operations.

## Alternatives and edge cases

- **Recount every window:** It costs `O(nk)` and repeats almost all work.
- **Ordered set of `(frequency, value)` pairs:** Remove the old pair and insert the new pair on every count change. It avoids stale entries but needs a balanced-tree structure with duplicate-safe updates.
- **Frequency buckets:** Track values by frequency and the minimum value in the highest nonempty bucket. This can improve constants or bounds but needs ordered membership within buckets.
- **Max-heap without negating frequency:** Python provides a min-heap, so failing to negate would select the least frequent value.
- **Negate the value too:** That would choose the largest value on a frequency tie, opposite the requirement.
- **Do not validate stale entries:** An old frequency record can report a mode no longer present in the window.
- **Do not push the departing value:** Its lower current frequency would lack a fresh heap representation.
- **Entering and leaving values equal:** Net frequency is unchanged; duplicate heap records are safe.
- **Frequency drops to zero:** A `(0, value)` entry may be pushed, but some positive-frequency value always exists because `k >= 1` and outranks it.
- **`k = 1`:** Each window’s mode is its only value with frequency one, so the answer is the sum of `nums`.
- **`k = n`:** Only the initial window exists, and the helper is called once.
- **All values distinct:** Every frequency is one, so the smallest value in each window is the mode and its weight equals itself.
- **All values equal:** The mode frequency is `k` and every window weight is `value * k`.
- **Large accumulated sum:** Python integers avoid overflow; fixed-width languages should use 64-bit arithmetic.
- **Input preservation:** The method updates only counts and heap records, not `nums`.
- **Missing imports:** The stored source uses `List`, `defaultdict`, `heappush`, and `heappop` without imports. Standalone Python needs the corresponding `typing`, `collections`, and `heapq` imports.
