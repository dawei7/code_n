## General

This problem asks many distance queries about one unchanging word array. Scanning the entire array separately for every call would repeat the same search for word occurrences. The constructor therefore performs the reusable work once: it builds an inverted index, mapping each distinct word to the ordered list of positions where that word occurs.

For example, if the input is

```text
["practice", "makes", "perfect", "coding", "makes"]
```

then the relevant entries are

```text
"practice" -> [0]
"makes"    -> [1, 4]
"perfect"  -> [2]
"coding"   -> [3]
```

The lists are automatically sorted because the constructor enumerates `wordsDict` from left to right and appends increasing indices. No separate sorting step is needed.

Once `shortest(word1, word2)` retrieves the two occurrence lists, the problem becomes: given two sorted arrays of positions, find the minimum absolute difference between one value from the first and one value from the second. The exact solution solves that smaller problem with two pointers.

**Why comparing every pair is wasteful**

If `word1` occurs $a$ times and `word2` occurs $b$ times, a nested-loop comparison examines $ab$ pairs. Sorting changes what is necessary. Suppose the current positions are `a[i] = 4` and `b[j] = 10`. Keeping `4` while moving `j` forward cannot help, because every later `b` position is at least `10` and therefore at least as far from `4`. The only possible improvement involving these frontiers comes from advancing the smaller position `4` toward `10`.

This gives the merge rule:

- compute the current distance `abs(a[i] - b[j])`;
- if `a[i] <= b[j]`, increment `i`;
- otherwise, increment `j`.

At least one pointer advances on every iteration, so the scan always progresses.

**Why discarding the smaller position is safe**

Assume `a[i] <= b[j]`. All unexamined values in `b` are at indices `j` or later and satisfy `b[j'] >= b[j]`. Therefore,

$$
b[j']-a[i] \ge b[j]-a[i].
$$

The pair `(a[i], b[j])` is already the best possible pair involving `a[i]` and any not-yet-considered `b` value. Earlier `b` values were handled before pointer `j` reached its current position. Consequently, no future pair using `a[i]` can improve the answer, and advancing `i` loses nothing.

When `a[i] > b[j]`, the symmetric argument shows that every later `a` value is at least as far from this fixed `b[j]` as the current `a[i]`. Advancing `j` is safe.

By repeatedly finalizing the smaller frontier in this way, the loop considers enough neighboring cross-list positions to include a globally closest pair. It does not need to enumerate pairs whose ordering proves they are already worse.

**A complete query trace**

For the example mapping, call `shortest("makes", "coding")`. The lists are `a = [1, 4]` and `b = [3]`.

1. Start with `i = 0`, `j = 0`, comparing positions `1` and `3`. Their distance is `2`, so `ans` becomes `2`. Since `1 <= 3`, advance `i`.
2. Compare positions `4` and `3`. Their distance is `1`, so `ans` becomes `1`. Since `4 > 3`, advance `j`.
3. Pointer `j` has reached the end of `b`, so no further cross-list pair can be formed and the loop stops.

The method returns `1`, matching the adjacent occurrences at indices `3` and `4`.

For `shortest("coding", "practice")`, each list contains one position: `[3]` and `[0]`. The only distance is `3`, and advancing the pointer at `0` ends the loop.

**Why stopping when either list ends is correct**

The loop condition requires both pointers to reference real positions. When one list is exhausted, every position removed from that list was advanced only after its best possible pairing with the current and future frontier of the other list had been considered. No unused position remains on the exhausted side, so no new cross-list pair exists. Positions remaining only in the other list cannot be paired with each other, and the recorded minimum is final.

**The constructor-query tradeoff**

Preprocessing is valuable because the contract permits up to `5000` calls to `shortest`. The constructor spends one pass and $O(n)$ storage to make a query depend only on the occurrences of its two requested words. Rare words can then be queried much faster than rescanning all $n$ input positions.

The stored structure is a `defaultdict(list)`. Accessing a missing word would silently create an empty list, but the contract guarantees both query words exist, so valid calls always retrieve nonempty position lists. It also guarantees `word1 != word2`; positions from the two lists cannot be identical, and the true distance is at least `1`.

**Why the reported minimum is correct**

Initially, `ans = inf`, so the first real pair establishes a finite upper bound. Every iteration records the current pair before discarding either frontier. The inequality argument proves that the discarded smaller position cannot participate in a better unexamined pair. Thus each discard removes only a position whose relevant opportunity has already been accounted for. When one list is exhausted, all possible candidates from that side have been safely settled, and `ans` is the minimum distance over every pair that could be globally optimal.

## Complexity detail

Let $n$ be the number of words in `wordsDict`. The constructor visits each position once and performs an expected constant-time dictionary lookup plus list append, so preprocessing takes expected $O(n)$ time. Across the entire mapping, exactly $n$ indices are stored. Dictionary keys and lists add overhead proportional to the number of distinct words, which is at most $n$, so total retained space is $O(n)$.

For one query, let $a$ and $b$ be the occurrence counts of `word1` and `word2`. Each loop iteration advances exactly one pointer. Pointer `i` advances at most $a$ times and `j` at most $b$ times, giving $O(a+b)$ query time and $O(1)$ temporary space.

For $q$ queries, the precise total is

$$
O\left(n+\sum_{r=1}^{q}(a_r+b_r)\right).
$$

Because every occurrence count is bounded by $n$, a coarse worst-case bound is $O(n+qn)$, matching the manifest. The persistent index remains $O(n)$; each query adds only constant temporary state.

String hashing and equality have a character cost in the most detailed model, but each word has length at most `10`, so those operations are constant under the stated constraints.

## Alternatives and edge cases

- **Rescan `wordsDict` for every query:** The one-pass method from Shortest Word Distance uses $O(1)$ extra space and $O(n)$ time per call. It may be reasonable for one query, but repeated calls waste the opportunity to preprocess the fixed array.
- **Compare all occurrence pairs:** After indexing, testing every pair costs $O(ab)$ per query. The sorted two-pointer merge reduces this to $O(a+b)$.
- **Binary search the larger occurrence list:** For every position in the smaller list, find neighboring insertion positions in the larger list. This costs $O(\min(a,b)\log\max(a,b))$ and can be attractive when one word is extremely rare, though the implemented merge has a clean linear bound.
- **Cache query results:** If identical word pairs are requested repeatedly, an additional cache could return later answers in $O(1)$ expected time. It would require canonicalizing pair order and using extra space; the exact solution does not assume repeated queries.
- **Adjacent occurrences:** Distance `1` is the smallest legal answer because the query words are distinct. The loop could return immediately when it finds `1`, but continuing remains correct.
- **One occurrence per word:** Each list has length one, so the loop performs one comparison and returns their absolute index difference.
- **Highly frequent words:** The two lists may together contain much of the original array, making a query $O(n)$ in the worst case, but never quadratic.
- **Missing query word:** Valid input excludes this case. With `defaultdict`, an invalid lookup would create an empty list and leave `ans` as infinity, so a broader API should validate keys or define missing-word behavior.
- **Equal query words:** The contract forbids this. Supporting it would require the minimum gap between consecutive distinct entries within one occurrence list; comparing a list with itself would otherwise permit distance zero at the same occurrence.
- **Sortedness dependency:** The merge proof relies on each posting list being sorted. Appending indices during a left-to-right constructor pass guarantees that property without explicit sorting.
- **Input mutation after construction:** The class stores indices derived from the original snapshot. The interface provides no mutation operation; if the external array later changed, the index would not automatically update.
