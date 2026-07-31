## General

**Separate users before making decisions**

A retained request for one user cannot help or harm another user, so the global optimum is the sum of independent per-user optima. Group the request times by user and sort each group in ascending order.

**Keep the earliest feasible requests**

For one sorted group, scan times from earliest to latest. Maintain a deque containing exactly the retained times that lie within `window` of the current time. Before deciding on the current request, remove deque entries whose difference from the current time is strictly greater than `window`; those older records cannot share any inclusive interval of the prohibited span with the current or any later request.

If fewer than `k` retained times remain in the deque, keep the current request and append its time. Otherwise, adding it would place `k + 1` retained requests between the deque's first time and the current time, a span no greater than `window`, so discard the current record.

**Why discarding the latest conflicting request is optimal**

Whenever the current request would create a violation, every feasible selection can retain at most `k` requests from that conflicting interval. The greedy selection already holds `k` earlier requests. Replacing any of them with the current, later request cannot increase the number retained so far, and the later replacement expires from future windows no sooner than the earlier request it displaced. Keeping the earlier requests therefore leaves at least as much room for every future timestamp. Inductively, after each processed prefix, an optimal solution exists with exactly the greedy retained set size and with retained times no later than an alternative of the same size. Discarding the current request never reduces the maximum attainable final count.

## Complexity detail

Let $N$ be the number of request records. If one user owns $m$ records, sorting that group costs $O(m\log m)$. Summed over all groups, this is at most $O(N\log N)$. Each retained time enters and leaves its deque at most once, so all scans take $O(N)$ additional time. The grouped time arrays and deques use $O(N)$ space.

The benchmark defines size as $N$, uses one user's times in descending input order, and forces recurring inclusive-window conflicts. The accepted grouping, sorting, and deque scan is $O(N\log N)$, whereas the correct slower control repeatedly selects the next minimum timestamp in $O(N^2)$ time before applying the same greedy rule.

## Alternatives and edge cases

- **Global `(user, time)` sort:** Sorting all records by both fields and resetting one deque when the user changes also achieves $O(N\log N)$ time; grouping makes the independence argument more explicit.
- **Repeated minimum selection:** Finding and removing the smallest remaining time by a full scan avoids a sort call but takes $O(N^2)$ time in the worst case.
- **Enumerate discarded subsets:** Testing every retained subset gives a direct correctness oracle only for tiny inputs and requires exponential time.
- **Inclusive endpoint:** Times whose difference equals `window` still belong to one inclusive interval and must remain together only when their count is at most `k`.
- **Duplicate timestamps:** Equal-time requests are separate records. No more than `k` of one user's duplicates can remain.
- **Arbitrary input order:** Sorting within every user group is required before the chronological greedy scan.
- **Dropped requests:** A discarded record is never inserted into the deque and cannot contribute to a later violation.
- **Large `k`:** If a user's request count does not exceed `k`, every request for that user is retained.
