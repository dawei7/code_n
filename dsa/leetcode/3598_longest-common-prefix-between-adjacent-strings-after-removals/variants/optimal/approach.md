## General
Let `adjacent[j]` be the longest-common-prefix length of `words[j]` and `words[j + 1]`. Removing `words[i]` destroys only the original edges at indices `i - 1` and `i`. Every edge with index at most `i - 2` or at least `i + 1` remains unchanged.

**Summarize unaffected edges:** Build prefix maxima and suffix maxima over `adjacent`. For removal `i`, `prefix_max[i - 2]` gives the best surviving edge strictly to the left when it exists, and `suffix_max[i + 1]` gives the best surviving edge strictly to the right. These two lookups cover every adjacency whose endpoints were already neighbors.

**Evaluate the only new edge:** If `i` is internal, removing it makes `words[i - 1]` and `words[i + 1]` adjacent. Compute their longest common prefix directly and include it in the maximum. Endpoint removals create no bridge.

No other pair can change adjacency: pairs away from `i` retain their positions relative to each other, while the predecessor and successor of `i` are the only formerly separated words that meet. Therefore the maximum of the surviving-left score, surviving-right score, and optional bridge score is exactly the requested answer for every removal.

## Complexity detail
Let $n$ be the number of words and $S$ their total character count. Each word participates in at most two original adjacent comparisons and at most two bridge comparisons. Longest-common-prefix scans therefore examine $O(S)$ characters in total. Building both maximum arrays and producing all answers costs another $O(n)$, which is $O(S)$ because every word is nonempty. Total time is $O(S)$.

The adjacent scores, prefix maxima, suffix maxima, and result each contain $O(n)$ integers. Apart from those arrays, the algorithm uses constant scalar state, so auxiliary space is $O(n)$.

## Alternatives and edge cases
- **Remove and rescan for every index:** It directly follows the definition but repeats nearly all adjacent comparisons, taking $O(nS)$ time and $O(n)$ temporary space if each reduced array is copied.
- **Copy surviving edge scores:** Precomputing original LCP values helps, but slicing out the two invalid edges and scanning the copied scores for every removal still takes $O(n^2)$ time.
- **Segment tree over adjacent scores:** Range maxima can answer the unaffected left and right parts in $O(\log n)$ per removal, but static prefix and suffix maxima make those queries $O(1)$ and are simpler.
- **Multiset of edge scores:** Temporarily deleting two scores and adding a bridge can work, but maintaining ordered counts adds logarithmic overhead and mutation complexity.
- **Single word:** Removing it leaves no pair, so the only answer is `0`.
- **Two words:** Either removal leaves one word; both answers are `0` even if the original strings are identical.
- **Endpoint removal:** Only one incident edge disappears and no bridge is created.
- **Internal removal:** The bridge can exceed every original adjacent score and must be checked explicitly.
- **Tied maxima:** If one maximum edge is destroyed but another equal edge survives elsewhere, the maximum remains unchanged.
- **Prefix equals a whole word:** The LCP may be the full length of the shorter word; comparisons stop at that boundary.
