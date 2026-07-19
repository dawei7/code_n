## General
**Stop at the first duplicate.** Scan `nums` from left to right while storing every previously visited value in a set. If the current value is already present, return it immediately.

**Why that duplicate is the answer.** The contract says that every value except one occurs exactly once. Consequently, the first value encountered twice cannot be one of the singleton values; it must be the value that appears $N$ times. The promised repeated value necessarily produces such an encounter, so the scan always returns before it finishes.

## Complexity detail
At most $2N$ values are processed, and average-case set lookup and insertion take constant time, giving $O(N)$ time. The set may hold $N+1$ distinct values, so it uses $O(N)$ auxiliary space.

## Alternatives and edge cases
- **Constant-distance comparison:** The frequency guarantee implies that two copies of the answer occur within distance three. Comparing each value with the previous three positions yields $O(N)$ time and $O(1)$ space, but its pigeonhole argument is less direct.
- **Frequency table:** Count every value and return the one with count $N$. This is also linear but performs a full scan even after the answer has repeated.
- **Repeated full-array counting:** For each candidate, scan the entire array to count it. This is correct but takes $O(N^2)$ time.
- **Minimum size:** When $N=2$, the four-element array still contains one value twice and two singleton values.
- **Zero as the answer:** A repeated value of `0` is valid and must not be confused with a sentinel.
- **Adjacent copies:** The repeated value may appear consecutively, so the second copy should be returned immediately.
