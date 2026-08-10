## General

**Every valid pair has a later endpoint**

A valid pair uses one index containing one and one index containing two. Its absolute distance is the later index minus the earlier index.

During a left-to-right scan, when the later endpoint is reached, the algorithm only needs the closest earlier occurrence of the opposite value. Among all earlier opposite indices, the largest index is closest to the current position.

This turns an apparent all-pairs problem into maintaining two latest positions.

**Use value arithmetic to select the opposite**

The only relevant nonzero values are one and two. For either one,

`3 - x`

is the other:

- when `x=1`, `3-x=2`;
- when `x=2`, `3-x=1`.

The list `last` has three entries so it can be indexed directly by value. `last[1]` stores the most recent index containing one, and `last[2]` stores the most recent index containing two. Entry zero is unused.

The loop skips `x=0` because zero cannot be part of a valid pair and should update neither latest position.

**Candidate distance at one index**

At current index `i` containing `x`, the closest earlier valid partner is `last[3-x]`. If it exists, the distance is

`i - last[3 - x]`.

The source takes the minimum of this candidate and the best answer seen so far, then records `last[x]=i` for future positions.

Keeping only the latest opposite occurrence is sufficient. If earlier opposite indices are `j_1<j_2<\cdots<j_t<i`, then

$$
i-j_t<i-j_{t-1}<\cdots<i-j_1.
$$

No older index can improve the candidate for this fixed `i`.

**Why all valid pairs are covered**

Take any valid pair `(a,b)` and let `i=\max(a,b)` be its later endpoint. When the scan reaches `i`, the earlier endpoint is an occurrence of the opposite value and has already been recorded or superseded by an even later opposite occurrence.

The candidate considered at `i` is therefore no larger than this pair's distance. In particular, when the globally closest pair's later endpoint is processed, no replacement partner can make the candidate worse; the algorithm records the global minimum.

Every computed finite candidate is itself a valid pair because it joins the current one or two with a previously stored occurrence of the other value. Thus the algorithm neither misses a better distance nor invents an invalid one.

**Sentinel handling**

The answer starts at `n+1`. Any real index distance lies between one and `n-1` because one index cannot simultaneously contain both one and two. Therefore `n+1` is safely larger than every valid answer.

Latest positions start at negative infinity. Before the opposite value has appeared,

`i - (-inf)`

is positive infinity, so taking the minimum leaves the finite answer sentinel unchanged. This avoids an explicit “has the other value appeared?” branch.

At the end, if `ans>n`, no finite valid distance was ever found and the source returns minus one. A genuine distance can never exceed `n-1`, so this test cannot reject a real answer.

**Trace the first example**

For `nums=[1,0,0,2,0,1]`:

- index zero records the latest one but has no earlier two;
- zeros do nothing;
- index three contains two and pairs with the one at index zero for distance three, then records latest two as three;
- index five contains one and pairs with latest two at index three for distance two.

The minimum becomes two.

For `[1,0,1,0]`, no two is ever recorded. Every candidate involving a one remains infinite, and the method returns minus one.

For adjacent values `[2,1]`, index one immediately finds distance one, the smallest possible positive answer. The source still finishes the scan, though an optional early return could stop there because no distance can beat one.

**Loop invariant**

Before processing index `i`:

- `last[1]` and `last[2]` are the greatest processed indices containing those values, or negative infinity if absent;
- `ans` is the minimum distance among every valid pair whose two endpoints are both before `i`, or the sentinel if none exists.

The current comparison adds exactly the best pair whose later endpoint is `i`. Updating `last[x]` then restores the latest-index property. Induction through the array proves the final result.

The exact source requires `inf` to be available.

## Complexity detail

The loop visits every one of `N` elements once and performs constant-time arithmetic, indexing, and comparisons. Total time is `O(N)`.

The three-entry `last` list and scalar variables occupy `O(1)` auxiliary space. These bounds match the manifest.

The official values are only zero, one, and two, so direct indexing and `3-x` are safe. A generalized two-target problem would store two explicit variables or a mapping.

## Alternatives and edge cases

- **Enumerate every one-two index pair:** If both values occur many times, this takes `O(N^2)`. The latest-opposite observation reduces it to one pass.
- **Store all positions of one and two:** Two sorted position lists can be merged with two pointers in `O(N)` time but require `O(N)` space.
- **Two explicit variables:** `last_one` and `last_two` are equivalent and may be clearer than the `3-x` trick in a generalized language.
- **Check only one ordering:** A one may appear before a two or after it. Processing whichever endpoint is later handles both.
- **Zeros:** They are neither target value and must not reset a latest position.
- **Missing one:** No valid pair exists and the sentinel produces minus one.
- **Missing two:** Symmetrically, the result is minus one.
- **Adjacent one and two:** Distance one is globally minimal.
- **Repeated same value:** Each new occurrence updates its latest position, improving potential proximity to a future opposite value.
- **Singleton array:** It cannot contain both required values and returns minus one.
- **Sentinel comparison:** Testing `ans>n` is safe because real distances are at most `n-1`.
- **Negative infinity arithmetic:** Python produces positive infinity for `i-(-inf)`. A language without infinities can use minus one latest indices plus an explicit presence check.
- **Return distance, not indices:** The algorithm discards endpoint identities after updating the minimum because only the numeric distance is requested.
