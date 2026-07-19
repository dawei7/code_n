## General
**Reduce each rectangle to one relevant value**

A square cut from `[l_i, w_i]` must fit within both dimensions, so its side cannot exceed $\min(l_i,w_i)$. That bound is also attainable by cutting along the longer dimension. Therefore, every rectangle is represented completely for this task by `side = min(length, width)`; the larger dimension cannot affect either the global optimum or the count.

**Maintain the best side and its frequency**

Scan the rectangles once while storing `best_side` and `count`. When `side` exceeds `best_side`, the new rectangle establishes a strictly better `maxLen`, so discard the obsolete count and set `count = 1`. When `side` equals `best_side`, increment the count. A smaller side changes neither value.

After any processed prefix, `best_side` is the largest attainable square side in that prefix, and `count` is exactly its frequency. Each update preserves those two facts. Once the entire array has been processed, they describe the required `maxLen` and the number of rectangles that can produce it.

## Complexity detail
Let $n$ be the number of rectangles. The scan computes one minimum and performs constant additional work for each rectangle, taking $O(n)$ time. Only the current best side, its count, and the current pair are retained, so the auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Two passes:** One pass can compute the largest smaller dimension and a second can count its occurrences. This is also $O(n)$ time and $O(1)$ space, but the one-pass update combines both tasks without revisiting the input.
- **Sort all attainable sides:** Sorting makes the maximum and its trailing frequency easy to identify, but costs $O(n\log n)$ time and $O(n)$ storage for a separately constructed side array.
- **Single rectangle:** Its smaller dimension is automatically the global maximum, so the answer is one.
- **Orientation:** `[a,b]` and `[b,a]` have the same attainable square side because only their minimum matters.
- **Tied maxima:** Every rectangle with the maximum smaller dimension counts, regardless of its larger dimension.
- **Maximum dimensions:** Values up to $10^9$ require only comparison; no multiplication or area calculation is needed.
