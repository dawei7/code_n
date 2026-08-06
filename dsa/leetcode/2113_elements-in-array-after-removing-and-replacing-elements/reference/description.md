## Description

An integer array `nums` changes once per minute. At minute $0$, it contains all
of its original elements. During each of the next $m$ minutes, where
$m = \lvert\texttt{nums}\rvert$, the leftmost element is removed. The array is
therefore empty after minute $m$.

During the following $m$ minutes, the removed elements are appended one at a
time in their original order. This restores `nums` completely after minute
$2m$, and the same removal-and-replacement cycle then repeats indefinitely.

Each query gives a time and an index. Report the element occupying that
zero-based index at the specified time, or $-1$ when the current array is too
short to contain the index. Queries observe the process independently; they do
not advance a shared clock.
