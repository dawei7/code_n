## General

**Reuse almost all work when the fixed window moves.** A size-`k` window beginning at index `i` and the next window beginning at `i + 1` share `k - 1` elements. Only two events occur: `nums[i]` leaves and `nums[i + k]` enters. Rebuilding a set or counter from scratch for every window would repeatedly process the shared portion.

The solution maintains a `Counter` named `cnt` whose keys and frequencies describe exactly the current window. The number of keys, `len(cnt)`, is then exactly the number of distinct values in that window.

**Build the first window.** `Counter(nums[:k])` counts the first `k` elements. If a value occurs several times, it has one key with a larger frequency; if it occurs once, it has one key with frequency one. `ans = [len(cnt)]` records the distinct count for the window `nums[0:k]`.

The exact Python slice `nums[:k]` creates a temporary list of `k` references before the counter consumes it. This does not change the algorithm, but it contributes `O(k)` temporary space.

**Slide one index at a time.** The loop variable `i` runs from `k` through `len(nums) - 1`. At that moment, `nums[i]` is the new rightmost value, while `nums[i - k]` is the old leftmost value.

The code increments the incoming value first:

`cnt[nums[i]] += 1`.

Then it decrements the outgoing value:

`cnt[nums[i - k]] -= 1`.

If the outgoing frequency becomes zero, `cnt.pop(nums[i - k])` removes its key entirely. Removing zero-count keys is essential because `len(cnt)` must count values currently present, not values that appeared in an earlier window.

**Why adding before removing is safe.** The entering and leaving values may be equal. In that case, incrementing and then decrementing restores the same positive frequency, so the key remains. That is correct because one occurrence left while another identical occurrence entered; the window’s multiset did not change for that value.

If the values differ, their two frequency changes are independent. The outgoing key is guaranteed to exist before its decrement because it belongs to the current old window.

**Record every completed window.** After both updates, `cnt` represents the new window ending at `i` and beginning at `i - k + 1`. Appending `len(cnt)` produces one answer for it. The first answer plus one appended answer for each of the remaining `n - k` endpoints yields `n - k + 1` results, the actual number of length-`k` subarrays.

**Trace the first transition.** For `nums = [1, 2, 3, 2, 2, 1, 3]` and `k = 3`, the initial counter contains one, two, and three once each, so the first answer is three.

When `i = 3`, another two enters, raising its count to two. The outgoing one drops to zero and its key is removed. The counter keys are now two and three, matching window `[2, 3, 2]`, so two is appended.

At the next step, a two enters and the outgoing two leaves. Its net frequency is unchanged, and keys remain two and three. This correctly reports two for `[3, 2, 2]`.

**Window invariant.** Before each loop iteration at endpoint `i`, `cnt[v]` equals the frequency of value `v` in `nums[i - k:i]` and contains no zero-frequency keys. Adding `nums[i]` and removing `nums[i - k]` transforms those frequencies exactly into `nums[i - k + 1:i + 1]`. Popping a zero key restores the no-zero-key condition.

Initialization establishes the invariant for the first window. Induction proves that every appended `len(cnt)` is the exact distinct count for its corresponding window.

**Why a set alone is insufficient.** A set tells whether a value is present but not how many copies remain. When one occurrence leaves, the value should stay present if another copy remains in the window. Frequencies provide the information needed to decide whether removal should delete the key.

## Complexity detail

Let `n = nums.length`. Building the initial counter processes `k` elements. The loop processes the remaining `n - k` elements, with expected constant-time counter updates and key removal per step. Total expected time is `O(n)`.

The counter contains at most `k` keys, and the initial slice also has length `k`, so auxiliary space is `O(k)`. The required answer contains `n - k + 1` integers and uses `O(n - k + 1)` output space.

## Alternatives and edge cases

- **Rebuild a set for every window:** It is simple but costs `O(k)` per window and `O(nk)` total in the worst case.
- **Frequency array:** Since values are bounded by 100,000, an indexed count array gives deterministic constant-time updates but allocates space by the value domain rather than the window.
- **Set plus separate duplicate handling:** This recreates frequency information indirectly and is more complicated than a counter.
- **`k = 1`:** Every window contains one value, so every answer is one; the update logic still works.
- **`k = n`:** Only the initialized window exists, the loop is empty, and one distinct count is returned.
- **All values equal:** The counter always has one key even as individual copies enter and leave.
- **All window values distinct:** The counter holds exactly `k` keys until values overlap across later windows.
- **Incoming equals outgoing:** Increment then decrement leaves the frequency and distinct count unchanged.
- **Outgoing last copy:** Its frequency reaches zero and the key must be popped.
- **Repeated values outside the window:** They have no effect until their positions enter; the counter tracks positions only through frequency updates.
- **Output length:** There are `n - k + 1` size-`k` windows, including the one beginning at `n - k`.
- **Python slice:** `nums[:k]` allocates a temporary length-`k` list, consistent with the `O(k)` auxiliary bound.
