## General

**Use the three-letter alphabet to split the problem into exhaustive cases**

The string contains only `'a'`, `'b'`, and `'c'`. A nonempty substring can therefore contain exactly one, exactly two, or exactly three distinct characters. There is no fourth possibility. The solution deliberately solves these three cases separately:

- `calc1` finds the longest balanced substring with one distinct character.
- Three calls to `calc2` find the longest balanced substring with exactly two distinct characters, one call for each pair `(a, b)`, `(b, c)`, and `(a, c)`.
- `calc3` finds the longest balanced substring with all three distinct characters.

The final answer is `max(x, y, z)`, where `x`, `y`, and `z` are the best lengths from those cases. This division is what makes a linear-time solution possible. Instead of maintaining a general frequency structure for every possible left endpoint, each helper uses the simplest invariant appropriate to its number of distinct letters.

**Case one: a balanced substring containing one character**

If a substring contains only one distinct character, all its present characters automatically have the same frequency because there is only one frequency to compare. Such a substring is simply a consecutive run of identical letters.

The helper `calc1` scans these runs. It places `i` at the first character of a run, advances `j` while `s[j] == s[i]`, records the run length `j - i`, and then moves `i` directly to `j`, the beginning of the next run. Each character belongs to exactly one run and is passed once. The greatest run length is exactly the best answer among one-letter substrings.

**Case two: equal counts of one chosen pair**

Consider `calc2(s, a, b)` for two chosen character names. A valid substring for this case must contain those two characters equally often and must not contain the alphabet's third character. That third character acts as a separator: a candidate substring cannot cross it, because crossing would include a third distinct character.

The outer part of `calc2` skips characters that are neither `a` nor `b`. It then processes one maximal segment containing only the chosen pair. Inside that segment, it maintains a prefix difference

$$
d = \#a - \#b.
$$

Reading `a` adds one to `d`; reading `b` subtracts one. Suppose `d` had the same value immediately before a candidate substring and at its right endpoint. The changes made within that substring must sum to zero, so the substring added equally many `a` and `b` characters. Conversely, any substring with equal counts contributes net difference zero and therefore has matching prefix differences at its two boundaries.

The map `pos` stores the earliest index at which each difference was seen in the current pair-only segment. It starts as `{0: i - 1}`. The index `i - 1` represents the empty prefix immediately before the segment, whose difference is zero. This seed is essential: if a balanced candidate starts at the segment's first character, a later return to difference zero gives length `right - (i - 1)`, which includes that first character.

When the current difference has appeared before at `pos[d]`, the balanced substring ends at the current index and has length `i - pos[d]`. The code compares that length with `res`. When a difference is new, the code stores its index. It intentionally does not replace an existing index: for a fixed right endpoint, subtracting the earliest equal-difference index gives the longest possible substring.

After a separator is encountered, the inner loop ends. The next outer iteration skips the separator or separators and creates a fresh map for the next maximal pair-only segment. Prefix differences cannot be matched across a forbidden third character.

The solution runs this helper for all three unordered pairs. A balanced two-letter substring must use exactly one of those pairs, so one of the calls will examine it inside the correct separator-bounded segment.

**Case three: equal counts of `a`, `b`, and `c`**

For all three letters to have the same frequency, tracking only one difference is insufficient. The helper `calc3` tracks two independent prefix differences:

$$
(\#a - \#b,\ \#b - \#c).
$$

The counter `cnt` holds prefix counts through the current index, and the tuple `k` is this pair of differences. The map `pos` is initialized with `(0, 0): -1`, representing the empty prefix before the entire string.

Suppose the same tuple appears at prefix endpoints `p` and `i`. Let the numbers of letters contributed by the intervening substring be `A`, `B`, and `C`. Equality of the first tuple component before and after gives

$$
A - B = 0,
$$

and equality of the second component gives

$$
B - C = 0.
$$

Thus `A = B = C`, so the substring is balanced. The reverse is also true: if a substring adds the same positive number of each letter, neither prefix difference changes, and its two boundary tuples match.

Because every character in the input is one of these three letters, a nonempty zero-change interval cannot add zero copies of all three. If its changes are equal, each is positive. Therefore a matched tuple really does describe a substring containing all three letters, except that even if one viewed `calc3` as allowing other cases, taking the maximum with the other helpers would remain safe.

As in `calc2`, `pos` keeps only the first occurrence of every tuple. When the tuple returns, the earliest occurrence produces the longest interval ending here. For example, if prefix counts move from `(2, 1, 0)` to `(4, 3, 2)`, both prefixes have difference tuple `(1, 1)`. The intervening substring contributed two copies of each letter and has length six.

**Why the maximum of the helpers is the complete answer**

Take any balanced substring. It has one, two, or three distinct characters. If it has one, it is part of a homogeneous run examined by `calc1`. If it has two, its pair is one of the three passed to `calc2`, and it lies wholly within one pair-only segment where equal prefix differences detect it. If it has three, equal frequencies force both prefix differences to return to the same tuple, so `calc3` detects it.

Every length reported by a helper is also valid for that helper's case. Thus the helpers neither miss a balanced substring nor create an invalid candidate. Their maximum is exactly the longest balanced substring.

## Complexity detail

Let `n` be the string length. `calc1` advances its indices only forward and takes $O(n)$ time. A single `calc2` call also takes $O(n)$ time: the skip loop and segment loop together consume every character at most once. It is called exactly three times, which is a constant factor, so all pair processing remains $O(n)$. `calc3` performs one pass and takes expected $O(n)$ time using hash-table lookups.

The total expected time is

$$
O(n) + 3O(n) + O(n) = O(n).
$$

In `calc2`, a maximal segment of length `m` can produce at most `m + 1` distinct difference values. Its map is discarded before the next segment, so its peak auxiliary space is $O(n)$. In `calc3`, at most `n + 1` different difference tuples are stored, also requiring $O(n)$ space. The counter contains only three keys. Since the helpers run sequentially rather than retaining all maps together, the overall auxiliary space complexity is $O(n)$.

The expected-time qualification comes from Python dictionary operations. The algorithmic number of scans is deterministic and linear; ordinary hash-table lookup and insertion are expected $O(1)$.

## Alternatives and edge cases

- **Quadratic substring expansion:** Fixing every left endpoint, extending every right endpoint, and maintaining three counts gives an easy $O(n^2)$ solution. That is suitable for the smaller version of the problem but not for a length up to $10^5$.
- **One general prefix-frequency map:** One can derive separate normalized signatures depending on which letters are present, but mixing absent-letter semantics into one state is easy to get wrong. The three-case split makes the completeness argument explicit and keeps each state minimal.
- **Binary balance without separator resets:** Running the `a` versus `b` difference across a `c` would incorrectly allow a reported interval that contains `c`. Every unchosen letter must end the current pair-only segment and reset `pos`.
- **Keeping the latest prefix position:** Replacing `pos[d]` or `pos[k]` on every occurrence would still find some balanced substrings, but it could lose the longest one. The earliest matching boundary always maximizes the length for a fixed right endpoint.
- **Missing the empty-prefix seed:** Without `{0: i - 1}` in `calc2` or `{(0, 0): -1}` in `calc3`, a balanced substring beginning at the start of a segment or at index zero would not be measured correctly.
- **All characters identical:** `calc1` returns the entire string. The pair and three-letter helpers may return smaller values, but the final maximum preserves the correct full length.
- **Only two letters occur in the entire string:** The matching `calc2` call can return the whole string when their totals are equal. `calc3` does not need to manufacture a three-letter answer; the exhaustive maximum includes the two-letter case independently.
- **A single character:** `calc1` records its run length as one. All loops terminate safely, and the answer is one.
- **Several forbidden characters in a row:** The initial loop in `calc2` keeps advancing until it reaches a chosen letter or the end. It cannot become stuck, and a fresh `pos` is created only for a real next segment.
- **Difference values becoming negative:** Negative values are expected when the second chosen letter is more frequent. Dictionary keys can be negative, and equality of prefix differences—not their sign—is what matters.
- **Why two differences suffice for three counts:** Requiring `A - B = 0` and `B - C = 0` already implies `A = B = C`. A third difference `A - C` would be redundant because it is the sum of the first two.
