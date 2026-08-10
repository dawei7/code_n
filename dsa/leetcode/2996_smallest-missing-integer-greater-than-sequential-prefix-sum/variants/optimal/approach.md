## General

**The task has two independent phases**

First find the sum of the longest sequential prefix. Then, starting from that sum, find the first integer absent from the entire array. Mixing these ideas can cause a common mistake: the sequential condition applies only while discovering the prefix, whereas the missing-value condition checks all positions in `nums`.

The prefix always contains `nums[0]`, even when the second value fails immediately. The code therefore initializes `s = nums[0]` and `j = 1`.

**Extend the prefix only while the exact rule holds**

The loop condition is:

`nums[j] == nums[j - 1] + 1`.

This requires consecutive values increasing by exactly one. Merely being increasing is not enough, and a repeated or smaller value also ends the prefix.

Whenever the condition holds, `nums[j]` is added to `s` and `j` advances. The first failure ends the longest sequential prefix permanently. Even if a later part of the array becomes sequential again, it cannot belong to a prefix because a prefix must start at index zero and contain every preceding position.

For `[3,4,5,1,12,14,13]`, the loop includes three, four, and five, making `s = 12`. It stops at one because one is not six. Values after that point do not affect the prefix sum.

**Build a membership set for the whole array**

The code creates `vis = set(nums)`. Duplicates are irrelevant to the next question: an integer is either present at least once or missing. A set gives expected constant-time membership tests.

Notice that `vis` includes elements after the sequential prefix. In the example, 12, 13, and 14 all appear outside the prefix and must be skipped even though the prefix sum is 12.

**Search upward from the required lower bound**

`count(s)` is an infinite iterator producing `s, s + 1, s + 2, ...`. The loop returns the first `x` not in `vis`.

This directly implements both parts of the output condition:

- every generated value is at least the prefix sum;
- processing in ascending order makes the first missing value the smallest possible one.

The loop is guaranteed to return. A finite array contains only finitely many distinct integers. Even if several consecutive values starting at `s` are present, eventually the search reaches a value outside the finite set.

**Why the result is minimal**

Let the returned value be $x$. It is absent because the code returns only after `x not in vis`. It is at least the prefix sum because the iterator starts there and only increases.

For every integer $q$ with $s\le q<x$, the loop examined $q$ earlier and did not return, so $q$ belongs to `vis`. Therefore no smaller eligible missing integer exists. This proves both validity and minimality.

**A complete trace**

For `nums = [1,2,3,2,5]`:

- start with `s = 1`;
- two equals one plus one, so `s = 3`;
- three equals two plus one, so `s = 6`;
- the next two is not four, so prefix extension stops;
- the set is `{1,2,3,5}`;
- the first candidate is six, which is absent, so the result is six.

For the second sample, the computed lower bound 12 is present, as are 13 and 14. The iterator tests them in order and returns 15.

**Why no sorting is useful**

Sorting would destroy the original prefix order, so it cannot help with the first phase. It would also cost $O(N\log N)$ merely to answer membership queries that a set handles in expected linear total time.

The input remains unchanged: the algorithm reads it in order and builds a separate set.

## Complexity detail

Let $N$ be the array length and $U$ the number of distinct values. The prefix scan visits at most $N$ positions. Building `vis` visits all $N$ elements.

The upward search can encounter at most $U$ present candidates before finding an absent one, because every successful membership hit corresponds to a distinct integer in the set. It therefore performs at most $U+1\le N+1$ expected constant-time lookups. Total expected time is $O(N)$.

The set stores $U$ values, so auxiliary space is $O(U)$, or $O(N)$ in the worst case. `count` is lazy and does not allocate an infinite sequence; it stores only its current integer.

## Alternatives and edge cases

- **Linear membership scans:** Testing each candidate with `x in nums` can repeat an $O(N)$ scan and become quadratic when many consecutive candidates are present.
- **Sort a copy:** It can find the missing value after prefix computation but costs $O(N\log N)$ time and $O(N)$ copy space.
- **Continue after a prefix break:** This would form a subsequence or later run, not the longest prefix required by the definition.
- **One-element array:** Its sole value is the sequential-prefix sum; return it if absent is impossible because it is present, so the search advances to the next missing integer.
- **Duplicate values:** They occupy one set entry and do not change presence.
- **Prefix sum already missing:** It is returned immediately.
- **Values after the prefix:** They still matter to missingness and are included in `vis`.
- **Infinite iterator safety:** Finiteness of `vis` guarantees termination even though `count` itself has no endpoint.
- **Input preservation:** Neither the scan nor set construction modifies `nums`.
