## General

The distance between words at indices `a` and `b` is $\lvert a-b\rvert$. A direct solution could collect every occurrence of `word1`, collect every occurrence of `word2`, and compare all pairs. That is unnecessary because the indices arrive in sorted order during a left-to-right scan. At each new occurrence, only the most recently seen occurrence of the other word can be its closest partner on the left.

The solution stores exactly three pieces of state:

- `i`: the latest index where `word1` has appeared;
- `j`: the latest index where `word2` has appeared;
- `ans`: the smallest distance found between a valid pair so far.

Both indices begin at `-1`, a sentinel meaning “not seen yet,” and `ans` begins at positive infinity so that the first real distance automatically replaces it.

**Why the latest opposite occurrence is enough**

Suppose the scan reaches a new occurrence of `word1` at index `k`. Every occurrence of `word2` seen so far has an index no greater than `k`. Among those indices, the largest one—the latest `word2` index—is closest to `k`, because subtracting a larger prior index produces a smaller distance. Any older occurrence lies even farther left and cannot form a better pair with this new `word1`.

The same argument holds symmetrically when the new word is `word2`: the latest prior `word1` is the closest `word1` on its left. Future occurrences do not need to be anticipated. When a future target is eventually encountered, it will be paired with the most recent opposite target then available.

This local rule covers the global optimum. Take any closest pair in the complete array and consider whichever of its two occurrences appears later. When the scan reaches that later occurrence, the earlier member of the pair is an occurrence of the opposite target. The stored latest opposite occurrence is either that member or an even later one, and therefore is at least as close. The algorithm evaluates that distance and cannot miss a globally minimum pair.

**How each loop iteration updates the state**

At index `k`, the current word is `w`.

- If `w == word1`, assign `i = k`.
- If `w == word2`, assign `j = k`.
- If both indices are no longer `-1`, evaluate `abs(i - j)` and minimize `ans` with it.

The source uses two independent `if` statements rather than `if` followed by `elif`. The contract guarantees `word1 != word2`, so one word cannot satisfy both conditions in the same iteration; under the valid input, the two forms behave identically. The separate checks also make the symmetry visible.

The distance check occurs on every iteration after both targets have first appeared, even if the current word matches neither target. In those iterations, neither `i` nor `j` changes, so the code simply compares `ans` with the same latest-pair distance again. This repeated constant-time comparison is harmless. An implementation could place the check only inside target-matching branches, but it would not improve the asymptotic bound.

**Trace through the examples**

Use

```text
["practice", "makes", "perfect", "coding", "makes"]
```

with `word1 = "coding"` and `word2 = "practice"`.

- At index `0`, `practice` sets `j = 0`. Since `coding` has not appeared, there is no valid pair yet.
- Indices `1` and `2` match neither target, so the recorded state remains unchanged.
- At index `3`, `coding` sets `i = 3`. Both targets are now known, so the candidate distance is `abs(3 - 0) = 3`, and `ans` becomes `3`.
- Index `4` does not change either target index. The final answer remains `3`.

For `word1 = "makes"` and `word2 = "coding"`, index `1` first records `makes`, index `3` records `coding` and creates distance `2`, and index `4` replaces the latest `makes` position. The new distance is `abs(4 - 3) = 1`, so the answer becomes `1`.

**The maintained meaning of the variables**

After processing the prefix ending at index `k`, `i` and `j` are the greatest occurrence indices of their respective targets within that prefix, or `-1` if absent. Assigning `k` whenever a target appears preserves this meaning because indices are visited in increasing order.

At the same point, `ans` is no greater than every candidate distance evaluated when a target occurrence arrived. As argued above, the globally shortest pair is evaluated when its later endpoint arrives, possibly with an even closer latest opposite endpoint. Therefore, after the final index, `ans` equals the shortest distance over all valid cross-target pairs.

The input guarantees that both words occur. Consequently, both sentinels are eventually replaced, a finite candidate is computed, and returning `ans` satisfies the declared integer return type. Without that guarantee, the function could return infinity, so production code for a broader contract would need an explicit “not found” result.

## Complexity detail

Let $n$ be the number of strings in `wordsDict`. The algorithm performs one left-to-right pass and stores no occurrence lists. Assuming word equality is treated as constant time under the constraint that each word has length at most `10`, the running time is $O(n)$.

More explicitly, let $L$ bound the number of characters examined by a comparison with either target. Each array element may be compared with both targets, so the character-sensitive bound is $O(nL)$. Here $L\le 10$, which reduces to $O(n)$ under the supplied constraints.

The variables `i`, `j`, `k`, `w`, and `ans` occupy constant auxiliary storage, independent of the number of words and occurrences. The auxiliary space complexity is $O(1)$. The input is not modified, and no output collection is built.

The linear time is optimal in the worst case. A potentially closest occurrence can appear near the end of the array, so an algorithm may need to inspect all $n$ positions before it can know the correct minimum.

## Alternatives and edge cases

- **Compare every cross-target pair:** Record or discover every `word1` position and every `word2` position, then test all combinations. It is correct but can take $O(n^2)$ time when both words occur frequently.
- **Store both position lists and merge them:** Since occurrence indices are sorted, a two-pointer merge can find the minimum in linear time after collection. It is also $O(n)$ overall but uses $O(n)$ extra space that the streaming method avoids.
- **Track only the last relevant word and index:** Another one-pass form stores the most recent occurrence of either target. Whenever the other target appears, update the distance. It is equivalent under `word1 != word2`, while the two-index form mirrors the contract directly.
- **Targets at adjacent positions:** Their distance is `1`, the smallest possible because the words are distinct and therefore cannot occupy the same index. An implementation could return immediately once `ans == 1`, although the exact source simply completes the scan.
- **Many repeated occurrences:** Replacing an old target index with the new one is safe; for every future opposite occurrence, the newer index is closer than any older index on the same side.
- **First valid pair appears late:** Until both sentinels are replaced, the solution correctly avoids computing a meaningless distance involving `-1`.
- **Targets at the two ends:** If no closer occurrences exist, `abs(0 - (n - 1))` correctly gives `n - 1`.
- **`word1 == word2`:** The source is not designed for that variant. Its two `if` statements would assign both indices to the same position and report zero. The problem explicitly guarantees that the target words are different; the related same-word variant requires tracking consecutive distinct occurrences.
- **A missing target:** The documented input excludes this case. Without the presence guarantee, `ans` could remain infinity and the API would need to define an alternate return value or exception.
- **Non-target words:** They do not affect the relevant indices. Recomputing the unchanged distance during such iterations is redundant but correct and constant time.
