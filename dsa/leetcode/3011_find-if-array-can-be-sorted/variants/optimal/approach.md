## General

**The sequence of set-bit counts cannot change**

Assign each element a label equal to `element.bit_count()`. A legal adjacent swap exchanges two elements only when their labels are equal. Swapping equal labels leaves the label sequence unchanged.

Therefore, an element can move only inside its original maximal contiguous block of one label. It can never cross a neighboring block with a different set-bit count. The block boundaries are permanent.

Within one block, however, any permutation is possible: arbitrary permutations can be produced through adjacent swaps, and every adjacent pair in the block has the same label. Thus each block may be sorted internally.

**Reduce global sorting to block ranges**

After sorting every block internally, the smallest value of a block appears first and its largest appears last. The concatenation is globally nondecreasing exactly when every block’s minimum is at least the maximum value of all earlier blocks.

Because earlier blocks have already passed this condition, the immediately previous block’s maximum is also the largest value seen in the sortable prefix. The code stores it as `pre_mx`.

For the current block, it computes `mi` and `mx`. If `pre_mx > mi`, some earlier value is larger than the smallest current value. Those two values lie in different immutable label blocks and cannot cross, so global sorting is impossible.

If `pre_mx <= mi`, every value in the earlier sorted prefix is at most every value at the beginning of this block. Sorting the current block internally preserves global order across the boundary. `pre_mx` becomes this block’s maximum.

**How the exact scan identifies blocks**

Pointer `i` begins a block. `cnt = nums[i].bit_count()` stores its label. Pointer `j` advances while later values have the same bit count.

During that inner scan, `mi` and `mx` track the block’s extremes. The algorithm does not actually sort or swap values because only these two boundary facts are needed to decide feasibility.

After checking the block, `i = j` jumps directly to the next label block.

**Trace a sortable example**

For `[8,4,2,30,15]`, bit counts form labels `[1,1,1,4,4]`. The first block has values 8, 4, 2 and range $[2,8]$. It can be rearranged to 2, 4, 8.

The second block has values 30 and 15 with range $[15,30]$. Since previous maximum eight is at most current minimum 15, the blocks can concatenate as `[2,4,8,15,30]`.

**Trace an impossible boundary**

If an earlier block contains value 16 and a later different-label block contains value eight, sorting requires eight to cross 16. Their set-bit counts differ, and the label boundary cannot move. The range test detects that the earlier maximum exceeds the later minimum and returns false.

**Why the condition is necessary and sufficient**

Necessity follows from immovable blocks: if an earlier block has any value greater than a later block’s minimum, the final array retains that earlier-before-later relationship and cannot be sorted.

For sufficiency, sort each block internally using legal adjacent swaps. The code’s successful range checks prove the maximum of every earlier block is at most the next block’s minimum. Hence the concatenation of internally sorted blocks is nondecreasing. This gives a concrete legal sorting strategy.

**Why zero initialization is safe**

`pre_mx` begins at zero. All input values are positive, so the first block’s minimum is at least one and cannot fail the comparison. After the first block, `pre_mx` contains a real maximum.

No input mutation occurs; the method answers possibility without constructing the final sorted array.

**Why one previous maximum summarizes every earlier block**

After a boundary passes, successful checks guarantee all values in older blocks are no greater than the next block’s minimum. Consequently, the most recently completed block’s maximum is also at least every earlier value. Carrying `pre_mx` forward therefore summarizes the entire sortable prefix, not merely one neighboring element.

## Complexity detail

Let $N$ be the array length. Every element is visited once by the advancing block pointers. `bit_count` is constant time for the bounded integers, so running time is $O(N)$.

The method stores only block pointers, one label, two extrema, and `pre_mx`. Auxiliary space is $O(1)$. It neither copies nor sorts `nums`.

## Alternatives and edge cases

- **Bubble-sort with legality checks:** It can simulate valid swaps but takes $O(N^2)$ time and may mutate or copy the input.
- **Sort each block explicitly:** This is constructive but costs $O(N\log N)$ total; minima and maxima suffice for feasibility.
- **Group all equal-popcount values globally:** Noncontiguous blocks cannot cross intervening labels, so they must not be merged.
- **Already sorted array:** Every boundary range is compatible, and the method returns true without swaps.
- **One element:** It forms one block and is trivially sortable.
- **All labels equal:** The whole array is one block and any permutation, including sorted order, is reachable.
- **Equal values across a boundary:** Nondecreasing order permits equality; failure uses strict `pre_mx > mi`.
- **Positive input guarantee:** It makes zero a valid initial previous maximum.
- **Input preservation:** Only range summaries are computed.
