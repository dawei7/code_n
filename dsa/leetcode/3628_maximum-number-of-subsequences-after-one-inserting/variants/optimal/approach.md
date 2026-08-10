## General

Every `"LCT"` subsequence chooses an L, then a later C, then a later T. The source first counts all such subsequences already present. It then calculates the best number of new subsequences obtainable by inserting one L, C, or T.

Inserting any other uppercase letter cannot participate in `"LCT"` and cannot improve the count.

**Count existing subsequences by their center C**

During the main scan:

- `l` is the number of L characters already passed;
- `r` is the number of T characters still to the right.

`r` starts as `s.count("T")`. Before processing current character `c`, the source subtracts one if `c` is T, so `r` excludes the current position and counts only later T characters.

When `c=="C"`, every earlier L can pair with every later T. This C contributes:

`l*r`

distinct LCT subsequences. Summing this over all C positions counts every existing subsequence exactly once by its unique chosen C.

Afterward, `l` is incremented if the current character is L, so it becomes available to later centers.

**Gain from inserting C**

If a new C is inserted at one position, every L before it can combine with every T after it. Its gain is:

`number_of_left_L * number_of_right_T`.

The loop evaluates `l*r` after processing each character, corresponding to inserting C immediately after that position. It stores the maximum in `mx`.

The beginning and end need no special profitable cases: at the beginning there are zero left Ls, and at the end there are zero right Ts. Their gain is zero, already covered by initial `mx=0`.

**Gain from inserting L**

An inserted L should be placed at the beginning. Moving it earlier cannot remove any C-T pair after it and may add more.

Once placed first, it creates one new LCT subsequence for every existing `"CT"` subsequence in `s`. Thus the best L-insertion gain is the number of CT pairs.

**Gain from inserting T**

Symmetrically, an inserted T should be placed at the end. It then completes every existing `"LC"` subsequence. Its gain is the number of LC pairs.

**The `calc` pair counter**

For two-character target `t`, `a` counts occurrences of `t[0]` seen so far. Whenever current character equals `t[1]`, the helper adds `a` to `cnt`.

Therefore:

- `calc("LC")` counts ordered L-before-C pairs;
- `calc("CT")` counts ordered C-before-T pairs.

Both target characters are distinct, so updating `cnt` before updating `a` has the expected strict-position behavior.

**Choosing the best insertion**

After the scan, the source compares:

- best internal C gain;
- `calc("LC")`, the gain from a final T;
- `calc("CT")`, the gain from an initial L.

Their maximum is added to the existing count `ans`.

All gains are nonnegative. “At most one insertion” therefore permits choosing the best gain even when it is zero; inserting nothing and inserting an irrelevant/no-gain character produce the same count.

**Why no other placement is better**

For an inserted L, its contribution is the number of CT pairs after it. Moving L left only increases that set, so the beginning is optimal.

For inserted T, its contribution is the number of LC pairs before it. Moving T right only increases that set, so the end is optimal.

For inserted C, placement matters through the product of left Ls and right Ts, and the loop explicitly tests every boundary.

These exhaust all useful inserted letters and positions.

**Following `"LCCT"`**

There is one L, two C characters, and one final T. Existing count is 2.

Inserting L at the beginning gains two CT pairs, producing total 4. Inserting T gains two LC pairs and also produces 4. A C insertion can gain at most one because one L and one T surround it. The source chooses gain 2.


Every existing LCT is counted once at its center. Every new LCT must contain the inserted character, because subsequences not using it already existed.

If the inserted character is L, C, or T, the corresponding formulas count exactly all subsequences using it. The source finds the maximum over all three cases, so adding that gain to the existing count yields the global optimum.

## Complexity detail

Let `n=len(s)`. Counting T characters, performing the main scan, and running two `calc` scans each take `O(n)` time. A constant number of linear passes remains `O(n)`.

Only counters `l`, `r`, `ans`, `mx`, `a`, and `cnt` are stored. Auxiliary space is `O(1)`.

Counts can be cubic in `n` in magnitude, but Python integers grow as needed.

## Alternatives and edge cases

- **Prefix/suffix arrays:** Store L prefixes and T suffixes to evaluate each C insertion. It is correct but uses `O(n)` space instead of rolling counters.
- **Dynamic programming over subsequence length:** Track counts of L, LC, and LCT, then separately model insertion choices. It is more general but less direct here.
- **Insert unrelated letter:** It creates no new LCT and never beats a nonnegative useful choice.
- **No L:** Existing count and C/T gains are zero; inserting L may use existing CT pairs.
- **No C:** Only one insertion cannot create both a missing C and another required letter, so gains depend on existing LC or CT pairs and may be zero.
- **No T:** Inserting T can complete existing LC pairs.
- **Single-character string:** One insertion leaves length two, so answer is zero.
- **Insert C at beginning or end:** One side count is zero, giving no gain.
- **Repeated letters:** Each index choice is a distinct subsequence and is counted multiplicatively.
- **Existing subsequences:** They remain after insertion because relative order of original characters does not change.
- **At most one insertion:** Zero gain is acceptable; the formula does not require a positive improvement.
- **Input preservation:** The source scans immutable `s` and constructs no modified string.
