## General

The answer after each arrival depends only on the length of the stream's current trailing run of `value`. Keep that length in `streak`. When `num == value`, extend the run by one. Otherwise the new last element is not the target, so no positive suffix ending there can consist entirely of the target; reset `streak` to zero.

After either update, return whether `streak >= k`. The maintained number is exact by induction over the calls: it is zero after a mismatch, and a matching arrival extends precisely the previous target-only suffix. Therefore reaching `k` is equivalent to the last `k` stream elements all being `value`. A longer run continues to return `true`, as every suffix of its last `k` elements also consists entirely of the target.

The app-local adapter constructs the same stateful object and processes `commands` in order, preserving the native interface's state across calls.

## Complexity detail

Let $q$ be the number of `consec` calls. Each call performs one comparison, one counter update, and one threshold comparison, so it takes $O(1)$ time. The complete sequence takes $O(q)$ time. The object stores only `value`, `k`, and `streak`, giving $O(1)$ auxiliary space; the adapter's returned list is output storage and is excluded.

## Alternatives and edge cases

- **Queue of the last `k` values:** Retaining a bounded queue models the statement directly, but checking all `k` entries after every arrival can cost $O(qk)$ total time and uses $O(k)$ state.
- **Queue plus mismatch count:** A queue with a count of non-target entries supports $O(1)$ updates, but it still spends $O(k)$ memory when only a trailing-run counter is needed.
- **Fewer than `k` arrivals:** The streak cannot yet reach `k`, so the result is `false`.
- **Threshold `k = 1`:** Every target arrival returns `true`, while every non-target arrival returns `false`.
- **Runs longer than `k`:** The counter may exceed `k`; keeping the exact run length makes every later target arrival correctly remain `true`.
- **Mismatch reset:** A single non-target value invalidates every suffix containing earlier target values, so the next run must start from zero.
