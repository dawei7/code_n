## General

**Partition the stream into earliest complete face blocks**

The set `s` collects distinct die faces seen since the most recent reset. Whenever its size reaches `k`, the current segment contains every possible face from 1 through `k`.

At that moment, the method increments `ans` and clears `s`, beginning a new block after the earliest prefix that completed the alphabet.

If the scan forms `g` complete blocks, `ans` ends as `g + 1` because it starts at one and increments once per block.

**Why every sequence of length g exists**

Take any desired roll sequence `[a_1,a_2,...,a_g]` of length `g`. The first complete block contains every face, so choose an occurrence of `a_1` from it. The second block lies entirely later and contains `a_2`, so choose that. Continue one choice per block.

The selected positions increase from block to block, making them a subsequence of `rolls`. Since the desired values were arbitrary, every possible length-`g` sequence occurs.

Any shorter sequence also occurs by using only the first required number of complete blocks. Therefore the shortest impossible length is greater than `g`.

**Construct a missing sequence of length g plus one**

The trailing incomplete segment after the last reset omits at least one face; call it `z`. If no complete block exists, `[z]` is already a missing sequence of length one.

For each complete block, consider the face whose first appearance in that block caused the set to reach size `k`. Call these completion faces `c_1,c_2,...,c_g`. By construction, `c_t` does not appear earlier inside block `t`; its first block occurrence is the block's final character.

Now consider sequence

`[c_1,c_2,...,c_g,z]`.

To match `c_1`, a subsequence cannot finish that choice before the end of block one. After that, matching `c_2` cannot occur before the end of block two, and so on. Inductively, after matching `c_g` the subsequence is in the trailing incomplete segment. That segment contains no `z`, so the final symbol cannot be matched.

Thus at least one sequence of length `g + 1` is impossible. Combined with the previous lower bound, the shortest impossible length is exactly `g + 1 = ans`.

**Why clearing at the earliest completion is optimal**

Resetting immediately maximizes the number of disjoint complete blocks obtainable from the stream. Delaying a boundary would consume rolls that could help complete the next block without adding any new face to the already complete current block.

The greedy earliest boundaries therefore provide the largest universality length `g` for which every sequence is guaranteed.

**Trace the set**

For `k = 2` and rolls `[1,1,2,2]`, the set becomes complete after the first 2, forming one block `[1,1,2]`. It clears, and the trailing `[2]` lacks face 1. Thus `g = 1` and the answer is 2. Indeed sequence `[2,1]` is absent.

If some face never appears anywhere, no complete block forms and `ans` remains one, correctly identifying that missing single-face sequence.

Only distinct faces matter while forming a block. Seeing the same face many times cannot complete a missing choice, so the set intentionally ignores those repetitions until another previously unseen face arrives.

## Complexity detail

Let `n` be the roll count. Each roll is inserted into a hash set once, and each clear operation discards at most `k` distinct entries. Across the scan, expected running time is `O(n)`.

The set contains at most `k` faces, so auxiliary space is `O(k)`. It is cleared between complete blocks rather than allocating new sets.

The input list is not modified. `ans` is at most `floor(n/k) + 1`.

## Alternatives and edge cases

- **Dynamic programming over all sequences:** There are `k^\ell` sequences of length `\ell`, making explicit enumeration infeasible.
- **Count total frequency of every face:** Frequency alone ignores order. Complete blocks capture the sequential ability to choose arbitrary symbols.
- **Do not clear after completion:** One global set can prove only that all length-one sequences occur; it cannot measure repeated universality.
- **Delay clearing:** It cannot increase the number of complete blocks and may waste useful rolls for the next block.
- **Missing face globally:** No complete block forms, so answer one.
- **Exactly one complete block:** Every one-symbol sequence exists, while the construction finds a missing sequence of length two.
- **Incomplete tail empty:** After the last block, every face is absent from the empty tail, so any `z` can finish the missing construction.
- **`k = 1`:** Every roll is face one and completes a block individually; the answer is `n + 1` because all shorter all-one sequences occur.
- **Repeated faces within a block:** Set insertion ignores duplicates until all distinct faces arrive.
- **Block-completion face:** Its first occurrence in that block is necessarily the final character that made the set complete.
- **Subsequence rather than subarray:** Choices may skip rolls inside each block, which is why one complete block can supply any requested single face.
- **Input preservation:** Only the temporary set changes.
- **Hash-set assumptions:** Complexity uses expected constant-time insertion for bounded integer faces.
