## General

**Identify each first session.** Partition rows by user and order by
`session_start`; `session_id` gives a deterministic secondary order. Assign
`ROW_NUMBER`, so row one is the user's first session regardless of fixture or
storage order.

**Combine eligibility and count.** Group the numbered rows by user. A
conditional maximum records whether row one is a Viewer, while a conditional
sum counts every Streamer row. Keep users satisfying the first condition and
having a positive count, then sort by count and user ID descending. The row
number proves the eligibility test refers to the chronological first session,
and the sum examines the complete history, so the two conditions exactly
characterize viewers who later or otherwise streamed.

## Complexity detail

Let $R$ be the number of sessions. Partition ordering and final ordering take
$O(R\log R)$ time in the general model. Window and grouping state can use
$O(R)$ space.

## Alternatives and edge cases

- **First-value window:** Carrying `FIRST_VALUE(session_type)` across each partition and deduplicating users is equivalent.
- **Correlated first-session search:** Rechecking earlier rows and recounting streams for every candidate viewer is correct but can be quadratic.
- **Viewer only:** Starting as Viewer is insufficient without a Streamer session.
- **Streamer first:** A later Viewer session does not qualify the user.
- **Multiple streams:** Count every Streamer session, not merely those immediately after the first row.
- **Ordering ties:** Equal counts are resolved by `user_id` descending.
