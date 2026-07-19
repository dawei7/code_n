## General
**Solve the construction backward.** Forward stamping can overwrite useful characters, making local choices difficult. Instead, imagine erasing `target` back to question marks. A window can be erased once every character that still matters in it agrees with `stamp`; already erased positions impose no restriction. Reversing the successful erase indices gives a valid forward order.

**Represent each window's blockers.** For every start, separate covered target positions into `made`, where the target matches the corresponding stamp character, and `todo`, where it differs. A window with empty `todo` can be erased immediately. Mark each newly erased position once and place it in a queue.

**Propagate newly erased positions.** When position `p` leaves the queue, inspect only windows covering `p` and remove it from their `todo` sets. When a set becomes empty, record that window and enqueue its not-yet-erased `made` positions. Each window-position dependency is processed once. If all $n$ positions become erased, reverse the recorded windows; otherwise return `[]`. Every reverse erase was compatible when chosen, so the reversed forward sequence reconstructs the target.

## Complexity detail
There are $n-m+1$ windows with $m$ covered positions each. Building and processing dependencies takes $O(nm)$ time and stores $O(nm)$ total memberships. The queue and erased markers add $O(n)$ space.

## Alternatives and edge cases
- **Repeated full-window scans:** Repeatedly search every window for one that can be erased. This is correct but can take $O(n^2m)$ time when only one window becomes available per pass.
- **Forward backtracking:** Try and undo placements from the question-mark string; the branching factor is exponential.
- **Stamp equals target:** One move at index `0` suffices.
- **Overlapping stamps:** Overlap is permitted and often necessary.
- **Move limit:** Each window is recorded at most once, so the result has at most $n-m+1 \le 10n$ moves.
