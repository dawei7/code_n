## General

**Turn each suffix question into a prefix-count query over values**

Process `nums` from right to left. Before handling index $i$, the maintained data structures contain exactly the values at indices $j>i$. The desired score can therefore be obtained by counting stored values that both belong to the opposite parity and are strictly below `nums[i]`.

The values may be as large as $10^9$, so first coordinate-compress the distinct values into ranks `1` through $U$, where $U$ is the number of distinct values. Because compression preserves order, values strictly smaller than `nums[i]` have ranks below its rank. Maintain two Fenwick trees over this rank domain: tree `0` stores frequencies of even suffix values, and tree `1` stores frequencies of odd suffix values.

For the current value, query the prefix ending one rank before its own in the tree for the opposite parity. This excludes equal values and returns exactly the score for the current index. Then add the current rank to the tree matching its own parity so it becomes available to every earlier index.

**Why the counts stay exact**

At the start of an iteration, reverse traversal ensures that neither the current value nor any value to its left has been inserted. Every stored frequency therefore corresponds to one and only one valid right-hand index. Selecting the opposite-parity tree enforces the parity condition, and querying through `rank(value) - 1` enforces strict inequality. Their intersection is precisely the set counted by the score definition.

After recording that count, inserting the current value preserves the same statement for the next earlier index. The invariant holds initially because the suffix after the last index is empty, so induction proves every output entry is correct.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$ and let $U$ be the number of distinct values, with $U\le N$. Sorting for coordinate compression takes $O(N\log N)$ time. Each of the $N$ values performs one Fenwick prefix query and one update in $O(\log U)$ time, so the total time is $O(N\log N)$.

The sorted ranks, rank map, two Fenwick trees, and returned array each require at most $O(N)$ storage, giving $O(N)$ auxiliary space beyond the returned answer as well.

## Alternatives and edge cases

- **Compare every pair:** Checking each later index directly is simple and correct, but requires $O(N^2)$ time and cannot handle the maximum length.
- **Merge-sort counting with parity:** A divide-and-conquer count can also achieve $O(N\log N)$ time, but tracking cross-half contributions separately by parity is more intricate than two Fenwick trees.
- **Balanced search trees:** Two ordered multisets augmented with subtree sizes support the same suffix queries, but they need custom order-statistics support and larger constants.
- **One tree without parity separation:** A total count of smaller suffix values cannot recover how many have the opposite parity; the frequency state must retain parity information.
- **Equal values:** Querying only ranks strictly below the current rank is essential because equal values are not smaller.
- **All values of one parity:** Every query targets an empty opposite-parity tree, so the answer is all zeros.
- **Increasing input:** No value to the right is smaller, regardless of parity, and every score is zero.
- **Single element:** Both Fenwick trees start empty, yielding `[0]` before the lone value is inserted.
