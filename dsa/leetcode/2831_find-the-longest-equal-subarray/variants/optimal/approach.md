## General

**View a future equal subarray through an original window.** Choose a target value and some of its occurrences that will become adjacent after deletions. In the original array, consider the window from the first chosen occurrence through the last. Every non-target value inside that window must be deleted, while target occurrences are kept.

If a window has length $w$ and its most frequent value occurs $f$ times, deleting the other $w-f$ elements makes those $f$ copies consecutive. The window is feasible when

$$
w-f\le k.
$$

The answer contributed by that window is $f$, not $w$, because deleted elements are absent from the final equal subarray.

**Maintain one window over the original array.** The exact solution uses `l` and `r` as inclusive window endpoints. `cnt` records the frequency of each value in the current window. When right endpoint `r` adds value `x`, `cnt[x]` is incremented.

Variable `mx` is the largest frequency ever observed during the sliding process. It is updated with `max(mx, cnt[x])`. It is deliberately not recomputed or decreased when the left endpoint moves.

**Use the deletion budget to decide when to shrink.** The current length is `r - l + 1`. The expression

`r - l + 1 - mx`

is the number of non-majority positions under the stored frequency bound. If it exceeds `k`, the source removes exactly one leftmost value from `cnt` and increments `l`.

A `while` loop is unnecessary here. Before adding the new right element, the maintained expression is at most `k`. Adding one element can increase it by at most one: window length rises by one, while `mx` either stays fixed or also rises by one. Therefore, at most one left move is required to restore the inequality measured with stored `mx`.

**Why a stale maximum is safe.** After the left endpoint moves, the actual maximum frequency inside the window might fall, but `mx` remains historical. The resulting window may not literally be convertible using at most `k` deletions when judged by its current true frequency. That would be dangerous if the code returned window length. It returns `mx` instead.

Every time `mx` increases from $q$ to $q+1$, the just-added value actually occurs $q+1$ times in the current window. At that moment, the new window length minus the new `mx` equals the prior window length minus the old `mx`, which was at most `k`. Thus, the newly established frequency is backed by a genuinely feasible window. Later stale reuse cannot increase the answer; it merely avoids unnecessary shrinking.

Therefore, every value ever assigned to `mx` is achievable by deleting at most `k` elements from some window.

**Why the scan does not miss a larger achievable frequency.** A window is forced to move left only when its length exceeds the stored achievable frequency plus `k`. Keeping a longer window without increasing frequency cannot help establish a better answer: it contains too many expendable positions relative to the best count seen. Whenever an added occurrence raises a value's count beyond `mx`, the previous paragraph shows the window is feasible and `mx` records it. Scanning all right endpoints therefore captures every possible improvement.

This is the same stale-maximum principle used in the longest-repeating-character-replacement pattern, with one important output difference: here the retained equal-subarray length is the repeated-value frequency, so the code returns `mx`.

**A deletion trace.** For `nums = [1, 1, 2, 2, 1, 1]` and `k = 2`, the full window eventually contains four ones and two twos. Its length minus frequency is two, so deleting the twos makes four ones consecutive and `mx` reaches four.

**Why elements outside the window do not matter.** Deletions are global, but an equal subarray only needs to exist somewhere in the resulting array. Values before the first kept occurrence and after the last kept occurrence may remain; they sit outside the chosen equal block. Only non-target values between the endpoints must be deleted, exactly as the window formula counts.

**The exact algorithm differs from the manifest.** The manifest describes grouping occurrence indices by value and sliding over deletion gaps within each group. This source instead runs one frequency window over the raw array with a historical maximum. Both achieve $O(n)$ time and $O(n)$ space, but their state and proof are different.

## Complexity detail

The right endpoint visits each of $n$ positions once. The left endpoint only moves forward and advances at most $n$ times. Counter increments and decrements are expected $O(1)$ hash operations. Total expected time is $O(n)$.

`cnt` can store one key for every distinct value, up to $n$, so auxiliary space is $O(n)$. The pointer and maximum variables use constant space. The source does not mutate `nums`.

The grouped-indices alternative also stores $O(n)$ total positions. Neither approach requires sorting because input order or occurrence order is already available.

The algorithm is asymptotically optimal in time: the last element can extend the best equal subarray, so all positions may need inspection.

## Alternatives and edge cases

- **Group occurrence indices:** For each value, store its sorted positions and maintain a window where `positions[r] - positions[l] - (r-l) <= k`. The expression counts non-target gaps directly and matches the manifest.
- **Recompute current maximum after every shrink:** This preserves a literally valid window but can be expensive without another data structure. The historical maximum avoids that work safely because only `mx` is returned.
- **Binary search answer length:** Test whether some value has enough closely spaced occurrences. It adds logarithmic work and is unnecessary.
- **`k = 0`:** A window may contain no non-target gaps, so the answer becomes the longest already-consecutive run of one value.
- **All values equal:** `mx` rises to $n$, the window never shrinks, and the full array is returned as the length.
- **All values distinct:** No frequency exceeds one; deletions cannot create multiple equal copies, so the answer is one.
- **Budget at least array length:** Every occurrence of the most frequent value can be joined, and `mx` becomes its total frequency.
- **Stale `mx`:** It may make the current window appear feasible when it is not, but it never creates a new unsupported answer value.
- **Single shrink:** The violation can grow by at most one per added element, so one left move restores the stored inequality.
- **Outside values:** They need not be deleted because the requested equal sequence is a subarray, not necessarily the entire final array.
- **Counter entries reaching zero:** They may remain as zero-valued keys, which does not affect frequency updates or asymptotic space.
