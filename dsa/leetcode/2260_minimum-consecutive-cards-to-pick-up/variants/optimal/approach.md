## General

**Reduce a picked interval to two equal cards**

A valid answer is a consecutive interval containing at least two cards with the same value. Suppose matching cards of value `x` occur at indices `a < b`. The shortest consecutive pickup containing that particular pair must begin at `a` and end at `b`. Its number of cards is not `b - a`, because both endpoints are included; it is

$$
b - a + 1.
$$

Any interval extending farther left or right contains the same pair but is longer. Therefore, the entire problem reduces to finding two equal values whose indices have the smallest inclusive distance.

**Why only the most recent equal card matters**

While scanning from left to right, suppose the current card `cards[i]` has value `x`. If `x` appeared at several earlier indices, the best partner for the current index is always its latest occurrence. Let two earlier occurrences be at `a < b < i`. Then

$$
i - b + 1 < i - a + 1.
$$

The occurrence at `a` can never form a shorter interval with `i` than the occurrence at `b`. This means the algorithm does not need a list of every index for each value. It needs only one mapping from a value to the greatest index at which that value has been seen.

The dictionary `last` stores exactly this information. Before index `i` is processed, `last[x]`, when present, is the closest earlier occurrence of `x`.

**Process one card**

For every pair `(i, x)` produced by `enumerate(cards)`, the code performs two conceptual steps:

- If `x in last`, it forms a matching pair with the latest earlier `x` and computes `i - last[x] + 1`.
- It assigns `last[x] = i` so that index `i` becomes the latest occurrence for all future cards.

The check must come before the assignment. Updating `last[x]` first would make the dictionary point to `i` itself. The computed length would then be one, falsely treating a single card as a matching pair.

The current interval length is combined with `ans` through `min`. Thus, `ans` never increases and always retains the shortest valid pickup found so far.

**A trace of the dictionary state**

For `cards = [3, 4, 2, 3, 4, 7]`, the first three values have not appeared before, so their indices are merely recorded:

- after index zero, `last[3] = 0`;
- after index one, `last[4] = 1`;
- after index two, `last[2] = 2`.

At index three, value three was last seen at index zero. The inclusive length is `3 - 0 + 1 = 4`, so `ans` becomes four, and `last[3]` moves to three. At index four, value four was last seen at one, producing another length-four interval. The minimum stays four. Value seven has no earlier occurrence. The returned answer is therefore four.

Notice that the method does not store the interval itself. The problem requests only its length, and the two indices already contain all information needed to calculate that length.

**Why consecutive occurrences are sufficient globally**

For any fixed card value, arrange all of its occurrence indices in increasing order. A pair that skips another occurrence has a larger gap than at least one adjacent pair inside it. Consequently, the minimum interval for that value is formed by consecutive occurrences in its occurrence list.

The `last` dictionary makes the scan evaluate exactly those consecutive-occurrence pairs: when a new copy arrives, it is compared with the immediately previous copy, then becomes the previous copy for the next occurrence. Since the scan does this independently for every value, every pair capable of being globally optimal is considered.

**Why the final answer is correct**

Before an iteration, `last` holds the latest processed index for each seen value, and `ans` is the minimum length among all matching consecutive-occurrence pairs found in the processed prefix. If the current value is new, there is no new matching pair, so only `last` changes. If it has appeared, the latest prior occurrence produces the shortest pair ending at this index, and taking `min` extends `ans` to cover that new candidate. Recording the current index restores the dictionary property.

After the final card, all potentially optimal adjacent pairs for every value have been evaluated. If at least one exists, `ans` is their minimum and therefore the shortest valid consecutive pickup.

**Represent the absence of a pair**

The variable `ans` starts at positive infinity. Every real interval length is finite and smaller, so the first duplicate replaces the sentinel. If no value occurs twice, the update branch is never entered and `ans` remains infinity. The final conditional converts that internal state to the required return value `-1`.

Using a sentinel avoids needing a special case for the first duplicate. All duplicate occurrences use the same minimum update.

## Complexity detail

Let `n` be the number of cards and `u` the number of distinct card values. The loop processes each card exactly once. Dictionary membership, lookup, and assignment take expected `O(1)` time in Python, so the total expected running time is `O(n)`.

The dictionary stores one index for each distinct value, using `O(u)` auxiliary space. Since `u \le n`, this is `O(n)` in the worst case. The numeric sentinel and loop variables use constant additional space. The input array is never modified.

The bound of up to `10^5` cards rules out repeated interval scans but is well suited to one pass. Card values can be as large as `10^6`, so a dictionary is more space-conscious than allocating an array covering every possible value when few values appear.

## Alternatives and edge cases

- **Check every pair of indices:** Comparing all card pairs directly takes `O(n^2)` time and ignores the fact that only the nearest previous equal value can help the current index.
- **Store every occurrence list:** Appending all indices by value is correct, but retaining only the latest index is sufficient and uses no more than one entry per distinct value.
- **Sort value-index pairs:** Equal values could be grouped after sorting, but sorting costs `O(n \log n)` and loses the simplicity of the original order scan.
- **Sliding window with frequencies:** A window can locate a duplicate, but finding the minimum over all possibilities requires more moving-state logic than directly measuring adjacent equal occurrences.
- **Array of latest indices:** Because values are bounded, an initialized array can replace the dictionary. It uses space proportional to the entire value domain rather than the number of values actually present.
- **No repeated value:** `ans` stays at infinity and the final expression returns `-1`.
- **Exactly two equal adjacent cards:** Their indices differ by one, so the formula returns two, the smallest possible valid answer.
- **Many copies of one value:** Each copy is compared only with the immediately preceding copy; this is sufficient because any skipped-copy interval is longer.
- **Duplicate intervals with the same length:** Only the length is requested, so keeping either source pair through `min` is enough.
- **Single card:** No matching pair can exist, and the sentinel is converted to `-1`.
- **Card value zero:** Zero is an ordinary dictionary key and requires no special handling.
- **Inclusive length:** The `+ 1` is essential. Omitting it would return the number of gaps between the pair rather than the number of cards picked up.
- **Update order:** The old index must be read before `last[x]` is overwritten with the current index.
- **Large value range:** Hash-map storage depends on distinct observed values, not on the maximum possible card value.
- **Input preservation:** The scan reads `cards` without sorting or changing it, so caller-visible data remains intact.
