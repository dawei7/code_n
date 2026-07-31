## Description

Design a counter that reports how many hits occurred during the preceding five minutes, which is a window of `300` seconds.

Each operation receives an integer timestamp measured in seconds. Calls arrive in chronological order, and multiple hits may occur at the same timestamp.

Implement the `HitCounter` class with these operations:

- `HitCounter()` initializes an empty counter.
- `hit(timestamp)` records one hit at `timestamp`; repeated calls at the same timestamp record separate hits.
- `getHits(timestamp)` returns the number of recorded hits within the past `300` seconds relative to `timestamp`.
