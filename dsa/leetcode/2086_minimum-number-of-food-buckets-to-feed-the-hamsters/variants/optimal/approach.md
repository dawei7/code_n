## General

**Process hamsters from left to right and resolve each one immediately**

A bucket can feed a hamster only from an adjacent empty position. When the scan reaches a hamster that has not already been handled, there are at most two possible bucket positions: the empty cell immediately left or the empty cell immediately right.

The greedy rule is to prefer the right cell whenever it is empty. A bucket on the right feeds the current hamster and may also feed a hamster two positions later. A bucket on the left can feed the current hamster and something earlier, but earlier hamsters have already been resolved by the left-to-right scan. Therefore, the right placement preserves at least as much usefulness for the unprocessed suffix.

The exact source avoids modifying the string or storing placed-bucket positions. It uses careful index jumps to remember when a right-side bucket also handles a future hamster.

**Place a right bucket when possible**

At hamster index `i`, the first condition checks:

`i + 1 < n and street[i + 1] == '.'`.

The bounds test ensures the right position exists, and the character test ensures a bucket may legally be placed there.

When both are true, the code increments the answer and executes `i += 2` inside the branch. The unconditional `i += 1` at the bottom of the loop then makes the total jump three positions, from the current index `i` to the original `i + 3`.

Why is it safe to skip the next two positions?

- Original position `i + 1` is the bucket location, so it is not a hamster needing inspection.
- If original position `i + 2` is a hamster, it is adjacent to that new bucket and is already fed.
- If original position `i + 2` is empty, there is nothing to feed there.

The jump is how the immutable-string implementation records the coverage. It never writes a bucket marker into `street`, but it also never revisits a hamster whose need was satisfied by the selected right bucket.

For `".H.H."`, the scan reaches the hamster at index 1, places a bucket at index 2, and jumps beyond the hamster at index 3 because that same bucket feeds both. The answer is one.

**Use the left cell only when right placement is unavailable**

If the right cell is out of bounds or not empty, the code tests `i and street[i - 1] == '.'`. The `i` condition is a concise truth test for `i > 0`, preventing access to a nonexistent left position at index $-1$.

When the left cell is empty, placing a bucket there is the only remaining way to feed the current hamster. The answer increases by one. No special jump is needed because the bucket points into the already processed side and cannot newly cover a later hamster two positions to the right.

For `"H..H"`, the hamster at index 0 receives a right bucket at index 1. The jump continues at index 3. Its right side is outside the string, but index 2 is empty, so a left bucket is placed there. Two buckets are necessary and sufficient.

**Return impossible when neither adjacent cell can hold food**

If a reached hamster has neither an empty right neighbor nor an empty left neighbor, there is no legal position that can feed it. The source immediately returns `-1`.

This is a proof of impossibility, not merely a greedy failure. The rules permit buckets only at `i - 1` or `i + 1` for this hamster, and the branch conditions have ruled both out.

In `".HHH."`, the first hamster can use the empty cell at index 0. The middle hamster has hamsters on both sides, so neither adjacent position can contain a bucket. Returning `-1` is unavoidable.

**Why preferring the right side is optimal**

Consider the first unresolved hamster encountered by the scan. If its right cell is empty, the greedy algorithm places a bucket there.

Suppose some optimal arrangement instead feeds this hamster with a bucket on its left. Replacing that left bucket with a right bucket still feeds the current hamster. The left bucket cannot be needed by an earlier unresolved hamster because every earlier hamster has already been fed. The right bucket can additionally help a later hamster at `i + 2`, so the replacement cannot make the remaining problem harder or increase the number of buckets.

Therefore, an optimal arrangement exists that makes the greedy right placement. If the right position is unavailable, an empty left position is forced. If neither exists, no arrangement is possible.

Applying this argument at each reached hamster shows that every counted placement is compatible with a globally minimum solution.

**Why the skipping scheme does not double-count buckets**

When a bucket is placed to the right of a hamster, the scan skips a possible hamster that this bucket feeds. It will not later add a second bucket for that already satisfied hamster.

When the code reaches a hamster normally, it has not been skipped by an earlier right placement. Thus it still needs a bucket. A left empty cell observed in the fallback branch is a new legal location required for this hamster, not an already recorded right bucket that the source forgot to mark. The jump logic ensures the only pattern where an earlier bucket at `i - 1` feeds the current hamster never reaches this iteration.

The algorithm counts placements without constructing the final placement layout, which is why it achieves constant extra space.

## Complexity detail

Let $n$ be the length of `street`.

The index `i` moves only forward. Most iterations advance by one; a right-bucket placement advances by three in total. No position is processed more than once, so time complexity is $O(n)$.

The source stores only `ans`, `i`, and `n`. It does not copy the string, create a placement array, or use recursion. Auxiliary space complexity is $O(1)$.

The early `-1` return may stop before scanning the whole string, but the worst case remains linear.

## Alternatives and edge cases

- **Place left whenever possible:** This can waste a bucket that could have been shared with a later hamster. Right preference is the forward-looking greedy choice.
- **Mutate a character array with bucket markers:** Marking chosen positions can make coverage explicit and still run in $O(n)$ time, but converting the immutable string uses $O(n)$ extra space. The index jump encodes the same state in $O(1)$.
- **Dynamic programming:** A small-state DP over positions can represent bucket and feeding states, but the local exchange argument yields a simpler greedy solution.
- **Count each hamster independently:** Adding one bucket per hamster ignores sharing. A bucket between two hamsters can feed both.
- **Single hamster:** It is possible if at least one neighboring in-bounds position is empty; at a one-character string `"H"`, neither position exists, so the answer is `-1`.
- **No hamsters:** The scan never enters a placement branch and returns zero.
- **Hamster at the left boundary:** Only the right cell can hold a bucket. If it is not empty or does not exist, feeding is impossible.
- **Hamster at the right boundary:** If it was not already skipped as fed, only an empty left cell can save it.
- **Pattern `"H.H"`:** The first hamster chooses the middle right cell, and the jump recognizes that the same bucket feeds the last hamster, producing one.
- **Adjacent hamsters:** They cannot place a bucket between them. Each must rely on its outer side, and a middle hamster in three consecutive `H` cells is impossible to feed.
- **Right-placement jump:** The internal increment by two plus the loop's final increment is intentional. Removing either part can revisit a fed hamster or skip the wrong position.
- **Input preservation:** `street` remains unchanged; the algorithm returns only the minimum count, not the placement itself.
