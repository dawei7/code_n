## General

**Use the average gap to rule out bucket interiors**

Let `lowest` and `highest` be the extrema of $n \ge 2$ values. The $n - 1$ adjacent gaps in sorted order sum to
`highest - lowest`, so the maximum gap is at least

$$
\left\lceil \frac{\texttt{highest} - \texttt{lowest}}{n - 1} \right\rceil.
$$

The candidate computes that positive ceiling as `width` with integer arithmetic and partitions the value range into
buckets of that width. Values assigned to the same bucket differ by less than `width`, so the maximum adjacent gap
cannot lie strictly inside one bucket. Only each nonempty bucket's minimum and maximum are needed.

For every `value`, compute its bucket position `i` and update that bucket's two extrema. Then scan buckets in numeric
order. The maximum of one nonempty bucket and the minimum of the next are consecutive in global sorted order, even
when empty buckets lie between them. Compare each such pair and retain the largest difference.

The average-gap bound proves that some cross-bucket pair attains the answer, and the scan examines every consecutive
nonempty pair. It therefore returns the same maximum gap as full sorting without ordering values inside buckets.

When all values are equal, `width` would be zero; the candidate returns zero before division. Fewer than two values
also have no adjacent sorted pair and return zero.

## Complexity detail

Computing extrema, assigning all $n$ values, and scanning at most $n$ buckets are linear passes, so time is $O(n)$.
The bucket minima and maxima use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Comparison sorting:** is straightforward but takes $O(n \log n)$ time.
- **Radix sort:** can be linear for fixed-width nonnegative integers but fully orders the data and needs digit-pass
  machinery.
- **Presence array over the value range:** can require $O(\texttt{highest} - \texttt{lowest})$ space rather than
  $O(n)$.
- Duplicate values share a bucket and contribute no positive gap.
- A single value or an all-equal array returns zero.
- Fixed-width implementations need a sufficiently wide type for the range difference and ceiling numerator.
