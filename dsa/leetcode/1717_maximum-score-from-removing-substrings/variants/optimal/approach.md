## General

**Always give priority to the more valuable pair**

The two removable patterns use the same characters in opposite orders. If one pays more, removing it whenever possible is safe. A local conflict can involve a pattern such as `"aba"` or `"bab"`, where choosing one direction prevents the other. Taking the higher-valued direction yields at least as much as taking the lower one, and all nonconflicting pairs can still be removed.

The source normalizes the problem so the high-value pattern is always called `a+b`. Initially `a="a"` and `b="b"`, with score `x` for `"ab"`. If `x < y`, it swaps both scores and both character labels:

`x, y = y, x` and `a, b = b, a`.

Afterward, `x >= y` and removing the ordered pair `a` followed by `b` earns `x`. If the original `"ba"` was more valuable, the labels make that original pattern the normalized `a+b` without reversing or copying the string.

**Other letters divide the string into independent segments**

Only adjacent `'a'` and `'b'` can ever form a removable pattern. A different character cannot be deleted, so characters on opposite sides of it can never become adjacent. Each maximal segment containing only the two relevant characters can be optimized independently.

The source processes one segment with two counters and flushes it whenever another character appears.

**Count unmatched high-pattern first characters**

`cnt1` counts currently unmatched occurrences of normalized character `a`. When the scan sees `c == a`, it increments `cnt1`. That character might combine with a future `b` into the high-scoring pair, so it should not be committed to a lower pair yet.

When `c == b` and `cnt1 > 0`, an earlier unmatched `a` exists. Removing that `a+b` pair immediately adds `x` and decrements `cnt1`. The current `b` is consumed rather than stored.

This counter behavior is equivalent to a stack removal of every possible high-value pattern, but it stores only counts.

**Track leading unmatched second characters**

If a `b` appears when `cnt1 == 0`, no preceding unmatched `a` can form the high pattern. The source increments `cnt2`.

After all possible high pairs have been greedily removed from one segment, its unmatched characters have the shape

$$
b\,b\,\ldots\,b\,a\,a\,\ldots\,a.
$$

If an unmatched `a` occurred before a later unmatched `b`, the scan would have paired them. Therefore all stored `b` characters conceptually precede all remaining `a` characters.

That residual order forms the lower-scoring pattern `b+a`. At most `min(cnt1,cnt2)` such pairs can be removed, and exactly that many are achievable.

**Flush at barriers and at the end**

When `c` is neither normalized `a` nor `b`, the source adds

`min(cnt1, cnt2) * y`

for all residual low-value pairs, then resets both counters. No useful pair can cross the barrier.

After the loop, the final segment has no following barrier to trigger this logic, so the same addition is performed once more.

**Why high-value removals first are optimal**

Within a two-character segment, the only choices that compete share characters. Consider changing an order that uses a lower `b+a` pair while a high `a+b` opportunity can be taken. At worst, the high removal can replace one lower removal in a local alternating arrangement; the remaining characters allow the other compatible removal. Since `x >= y`, this exchange never lowers the score.

Repeated exchanges transform an optimal sequence into one that removes every high pair greedily first. Once no high pair remains, the residual `b^p a^q` string has only low pairs, and exactly `min(p,q)` can be removed. The counter algorithm computes this canonical optimal score.

**Trace the normalization**

If original `y > x`, normalized `a` is original `'b'` and normalized `b` is original `'a'`. A normalized high pair is therefore original `"ba"` and earns the swapped `x`, which equals the original `y`.

No actual input characters are changed. Comparisons through the variables reinterpret which symbol plays each role.

## Complexity detail

Let $n$ be the length of `s`. The loop examines every character once and performs constant work. Barrier flushing and the final flush are constant per occurrence, so total time is $O(n)$.

The exact source stores only five scalar values—two character labels, two counters, and the score—besides loop temporaries. Auxiliary space is $O(1)$.

The manifest's $O(n)$ space is a valid loose upper bound but is not tight for this implementation. Unlike reversal- or stack-based versions, this file does not allocate a character array or reversed string.

## Alternatives and edge cases

- **Two stack passes:** Remove the higher pair with a stack, then the lower pair from the remainder. It is $O(n)$ time but uses $O(n)$ space.
- **Reverse when `y>x`:** Reversing converts `"ba"` to `"ab"`, but Python allocates an $O(n)$ copy; swapping character roles avoids it.
- **Repeated string replacement:** Searching and rebuilding after each deletion can become quadratic.
- **Equal scores:** Either pair may be prioritized because every removal is worth the same; the source keeps original `"ab"` priority.
- **No `a` or `b` characters:** Every character is a barrier and the result remains zero.
- **Single-character segment:** No pair forms, and the flush contributes zero.
- **Barrier characters:** They are never removed and correctly prevent cross-segment pairing.
- **All one relevant character:** One counter grows, but `min` is zero.
- **Alternating segment:** High pairs are consumed immediately; remaining opposite-order pairs are counted at the flush.
- **Final segment:** The explicit post-loop flush is necessary when the string ends with relevant characters.
- **Score normalization:** After swapping, `x` always means the high score and `y` the low score, regardless of original pattern names.
- **Constant memory:** Counter magnitudes may grow with $n$, but the number of stored integers does not.
