## General

Build a frequency table for all array values in one pass. Determine the
largest count stored in that table, then add every stored count equal to that
maximum.

Summing the qualifying counts, rather than merely counting qualifying distinct
values, is essential. If three values each occur four times, all twelve array
elements belong to maximum-frequency groups and contribute to the answer.

## Complexity detail

The frequency table is built and scanned in $O(N)$ time. It stores at most $N$
distinct values, so the auxiliary-space bound is $O(N)$. The source contract's
smaller fixed value range could also support a constant-size counting array.

## Alternatives and edge cases

- **Fixed counting array:** An array indexed from 1 through 100 gives the same $O(N)$ time with $O(1)$ contract-bounded space.
- **Sort and group:** Sorting reveals run lengths but costs $O(N\log N)$ time.
- **Rescan for each distinct value:** Counting occurrences independently for every value is correct but can cost $O(N^2)$ time.
- **All values unique:** Every frequency is one, so the answer is the full array length.
- **One dominant value:** Its frequency alone is returned.
- **Multiple tied groups:** Add their frequencies, not the number of groups.
