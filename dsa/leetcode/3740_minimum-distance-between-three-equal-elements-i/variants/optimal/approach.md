## General

**Simplify the three-index distance**

Sort the three selected indices conceptually as `i<j<k`. Their distance becomes

$$
(j-i)+(k-j)+(k-i)=2(k-i).
$$

The middle index cancels. For three equal values, minimizing the stated distance is therefore equivalent to minimizing the span from the first selected occurrence to the third.

Tuple order does not matter because absolute pairwise distances are symmetric. Every set of three distinct indices can be analyzed in increasing order.

**Group occurrence positions by value**

The dictionary `g` maps each array value to its list of indices. Because indices are appended during a left-to-right enumeration, every list is already strictly increasing.

For example, if a value occurs at indices `[0,2,3,8]`, all good triples using it come from choosing three entries of this list. The distance depends only on the first and last chosen entries.

**Only consecutive occurrence triples can be optimal**

Consider a chosen triple at occurrence-list positions `p<q<r`. If these are not three consecutive occurrences, then either an occurrence exists between the first and middle or between the middle and last. Replacing an outer selected occurrence with a closer intervening occurrence can only shrink, never enlarge, the outer span.

More directly, for any fixed first occurrence position `h` in the list, the smallest possible third occurrence is `h+2`; choosing a later one makes `k-i` larger. Every globally minimum triple therefore appears as

`ls[h], ls[h+1], ls[h+2]`

for some `h`.

One can also start from an arbitrary nonconsecutive triple `p_a,p_b,p_c`. Because `b>=a+1` and `c>=b+1`, `p_{a+2}` exists and is at most `p_c`. Replacing the chosen middle and third occurrences by `p_{a+1}` and `p_{a+2}` keeps the value equal and distinct while shrinking or preserving the outer endpoint. This constructs the required consecutive witness explicitly.

The source does not need the middle index numerically. It loops `h` through `0` to `len(ls)-3`, reads `i=ls[h]` and `k=ls[h+2]`, and evaluates `2*(k-i)`.

Overlapping consecutive triples are all considered. In `[0,2,3,8]`, windows `[0,2,3]` and `[2,3,8]` are separate candidates.

**Why the minimum is exact**

Every evaluated window contains three distinct indices holding the same dictionary key, so it is a valid tuple and its simplified distance is exact.

For any valid triple, replacing skipped occurrence positions until its three list positions are consecutive produces a valid triple with no larger span. Therefore some evaluated consecutive window is at least as good as every arbitrary triple. Taking the minimum over all values and windows gives the global answer.

`ans` starts at infinity. If no value has three occurrences, every inner range is empty and infinity remains, so the source returns `-1`. Otherwise it returns the finite minimum.

For `[1,2,1,1,3]`, value one has positions `[0,2,3]`. Their span is three and distance six. For `[1,1,2,3,2,1,2]`, value two has positions `[2,4,6]`, giving distance eight.

Although this is the smaller “I” version, the exact Optimal source already uses the linear occurrence-list method rather than the editorial's cubic enumeration.

The list scan counts windows rather than tuples because only a minimum is requested. If two different windows have the same distance, retaining either numerical value is sufficient; the indices themselves do not need to be returned.

## Complexity detail

Let `n` be the array length. Building all lists takes expected $O(n)$ time. Across all values, the total list lengths are `n`, and the total number of consecutive triple windows is at most `n`. The scan therefore takes $O(n)$ time, for $O(n)$ expected total.

The dictionary and occurrence lists collectively store every index once, requiring $O(n)$ auxiliary space. Hash-table operations supply the expected-time qualification.

## Alternatives and edge cases

- **Three nested loops:** The small constraints permit $O(n^3)$ enumeration, but occurrence grouping is both clearer and asymptotically better.
- **Check all triples within each list:** A value appearing many times still creates cubic combinations. Consecutive windows are sufficient.
- **Track only frequencies:** A count tells whether a triple exists but not its index span, so positions are required.
- **Use the middle index in the formula:** Its two adjacent gaps telescope; only the outer span matters.
- **Exactly three occurrences:** The list contributes one window.
- **More than three occurrences:** Overlapping windows must all be checked because the tightest cluster can occur anywhere.
- **No value appears three times:** Infinity remains and maps to `-1`.
- **Adjacent equal occurrences:** Indices `i,i+1,i+2` produce the minimum possible distance four.
- **Several values qualify:** Their best windows compete in the same global minimum.
- **Tuple ordering:** Permuting the same three indices does not change pairwise absolute distances.
- **Input values bounded by `n`:** The dictionary works without relying on that bound and uses space proportional to actual occurrences.
