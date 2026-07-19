## General
**Maintain the only possible interval**

Start with inclusive boundaries around the complete array. At every iteration, any possible target index lies between `left` and `right`.

**Use the middle value to discard half**

If the middle value equals `target`, return its index. If it is smaller, strict ordering proves the middle and every earlier value are too small, so move `left` past the middle. If it is larger, move `right` before the middle for the symmetric reason.

**Interpret an exhausted interval**

Each nonmatching step removes the checked middle and one impossible half while preserving every possible target position. When `left > right`, no candidate index remains, so returning `-1` is correct.

## Complexity detail
Each comparison reduces the candidate interval to at most half its previous length, producing $O(\log n)$ iterations. The algorithm stores only two boundaries and a middle index, using $O(1)$ extra space.

## Alternatives and edge cases
- **Half-open lower-bound search:** maintain `[left, right)` and locate the first value not smaller than `target`; verify equality before returning.
- **Linear scan:** stop at `target` or the first larger value; it is correct but takes $O(n)$ time in the worst case.
- The target may appear at either endpoint or in a one-element array.
- A target below the minimum or above the maximum returns `-1`.
- Strictly increasing input means a successful result is unique.
- Updating past the middle, rather than to the middle, is necessary to guarantee progress.
