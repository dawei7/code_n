## General

**Focus on zero blocks, not individual zeros.** An operation selects a `"1"` immediately followed by `"0"` and moves that one right across the entire consecutive zero block, stopping before the next one or at the end. Crossing a zero block counts as one operation regardless of how many zeros it contains.

Therefore each maximal block of one or more zeros is one obstacle that earlier ones may cross. The maximum answer can be counted by pairing each zero block with every one that originally appears before it.

**Count earlier ones during a left-to-right scan.** Variable `cnt` is the number of ones seen so far. Whenever the loop sees `"1"`, it increments `cnt`.

A new zero block begins exactly when current character is zero and the previous character is one. The source detects this with:

`elif i and s[i - 1] == "1"`.

At that boundary, all `cnt` ones seen so far can each be made to cross this block once in a maximum-length sequence of operations. The method adds `cnt` to `ans`.

Later zeros in the same block do not add anything because their previous character is zero. This correctly counts the entire block once.

**Why one can cross a given block at most once.** When a selected one moves across a zero block, it ends on the block's right side, either at the string end or just before another one. Operations only move ones to the right. That same one can never return to the left of the same original zero block and cross it again. Thus each pair consisting of an earlier one and a later zero block contributes at most one operation.

This gives an upper bound equal to the sum of prefix-one counts over zero-block starts.

**Why every such pair can be realized.** Process moves so earlier ones are allowed to encounter blocks successively rather than sending all rightmost ones straight to the end immediately. For a zero block, ones on its left can be moved across it one by one. After one crosses, the arrangement of adjacent ones may block others temporarily, but operations around later blocks move those blockers onward and expose the earlier ones. A left-to-right/maximizing schedule realizes one crossing for every earlier-one/block pair.

Another way to see the construction is to label each one while preserving their relative order. Each zero block migrates left across all labeled ones originally before it; each such crossing corresponds to one legal operation moving a one right across that block. No pair needs to cross twice, and no order inversion among ones is required.

Because the upper bound is achievable, the sum is the maximum operation count.

**Trace `"1001101"`.** The first zero block begins after the first one, so it contributes one. By the time the later zero block begins, three ones have appeared, so it contributes three. Total is four, matching a schedule where the first one crosses the early block and all three prefix ones eventually cross the later block.

For `"00111"`, the leading zero block has no preceding one and does not begin after `"1"`. No later zero block exists, so the answer is zero.

**Why individual zero count would be wrong.** In `"1000"`, the one moves across all three consecutive zeros in one operation, not three. Counting only the `"10"` transition recognizes the block-level behavior.

**Original-string scanning is sufficient.** The algorithm does not simulate mutations. Moving ones changes local adjacency, but the pair-count invariant depends only on original relative order between ones and maximal zero blocks. The operations never swap two ones or split the identity of a zero block in a way that changes how many earlier ones can cross it.

## Complexity detail

Let $n$ be string length. The loop visits each character once and performs constant work, so time is $O(n)$. This is optimal because a final zero block can change the answer and the string must be inspected.

Only `ans`, `cnt`, the index, and current character are stored, so auxiliary space is $O(1)$. The immutable input string is not modified. The answer can be quadratic in $n$—many ones before many separate zero blocks—but Python integers represent it exactly.

## Alternatives and edge cases

- **Explicit block loop:** Skip across each maximal zero run and add the number of earlier ones once. It expresses blocks directly but needs a manual index loop.
- **Simulate operations:** Repeated string movement can take quadratic or worse time and is unnecessary for counting.
- **Count every inversion `1...0`:** Individual zero inversions overcount consecutive zeros because one operation crosses an entire block.
- **No ones:** No operation is possible and all block contributions are zero.
- **No zeros:** No `"10"` boundary exists, so the answer is zero.
- **Leading zero block:** It has no preceding ones and contributes nothing.
- **Trailing zero block:** Every earlier one can cross it, so its prefix-one count is added.
- **Consecutive zeros:** Only the first zero in the run triggers an addition.
- **Consecutive ones:** They all increase `cnt` and can contribute at the next zero block.
- **Alternating string:** Every zero after a one begins its own one-length block, producing large cumulative prefix counts.
- **Single character:** No adjacent `"10"` pair exists.
- **Relative order of ones:** Operations do not swap ones with each other, which supports the labeled crossing interpretation.
- **Input preservation:** The source derives the maximum from the original string without constructing intermediate states.
