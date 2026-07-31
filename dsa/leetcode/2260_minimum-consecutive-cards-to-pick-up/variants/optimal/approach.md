## General

**Reduce each valid pickup to its matching endpoints**

Any consecutive pickup containing a matching pair can be shortened until one
chosen pair lies at its two endpoints. Its length is then `right - left + 1`.
The task is therefore to find the smallest inclusive distance between equal
values.

**Only the latest equal card can help**

Scan indices from left to right. When value `cards[index]` has appeared before,
the closest previous occurrence is its latest stored index. Every older
occurrence produces a longer interval ending at the same current index, so it
cannot improve on the latest one. Compare that inclusive distance with the
best answer, then replace the stored index with the current position.

For every value, consecutive occurrences in its ordered occurrence list are
the only pairs that can minimize distance: any nonconsecutive pair contains a
closer pair of the same value between its endpoints. The scan evaluates every
such consecutive pair exactly when its later endpoint arrives. Thus the
smallest recorded distance is globally optimal. If no value repeats, no valid
interval was observed and the result is `-1`.

## Complexity detail

Let $n=\lvert\texttt{cards}\rvert$. The scan performs expected $O(1)$ hash
operations per card, for $O(n)$ expected time. At most one latest index is
stored per distinct value, using $O(n)$ auxiliary space in the worst case.

## Alternatives and edge cases

- **Check every pair:** Comparing all index pairs is correct but takes $O(n^2)$ time.
- **Store every occurrence list:** Consecutive indices can be compared afterward in $O(n)$ time, but retaining only the latest index uses less state.
- **Sliding window with frequencies:** Shrinking a window until it loses its duplicate also works, but the direct distance formulation is simpler.
- **Adjacent equal cards:** The minimum possible result is `2`.
- **No duplicate:** Return `-1`.
- **Several repeated values:** The answer may come from any value, so keep a global minimum.
- **More than two copies:** Update the latest index after every occurrence to test each adjacent occurrence pair.
- **Zero-valued cards:** Zero is an ordinary card value and remains a valid hash key.
- **Single card:** No pair exists.
