## General
**Distribute the significant bits**

Leading zeros are flexible, but each `1` contributes to the represented value. If the total number of ones is not divisible by three, equal nonzero parts are impossible. If there are no ones, all three values are zero and any legal cuts work, such as `[0,2]`.

Otherwise let each part contain one third of the ones. Locate the first `1` belonging to each part. Call their positions `first`, `second`, and `third`. These anchors are forced in every valid partition because no part may take a different number of ones.

**Use the third part as the required pattern**

The suffix beginning at `third` contains the significant bits of the third value and all of its trailing zeros. Its length and exact bit pattern must also occur beginning at `first` and `second`. Compare the three anchored suffixes in lockstep, advancing indices `i`, `j`, and `k` while `arr[i] == arr[j] == arr[k]`.

If `k` reaches the array end, the complete significant patterns match. Return `[i - 1, j]`: `i - 1` ends the first copy after its required trailing zeros, while `j` begins the third part after the second copy. Zeros before `second` and `third` remain as harmless leading zeros in the following parts.

If a comparison fails before `k` reaches the end, no different cuts can repair the unequal significant patterns because the three first-one anchors and the third part's trailing-zero count are fixed. Therefore `[-1,-1]` is necessary.

## Complexity detail
Counting ones, locating the three anchors, and comparing the anchored patterns each scan at most $n$ positions, giving $O(n)$ time. The algorithm uses a constant number of counters and indices, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Enumerate both cuts:** Testing every pair `[i, j]` and evaluating all three binary parts is correct but can take $O(n^3)$ time.
- **Convert slices to integers:** Arbitrary-precision conversion can compare values, but repeatedly building large integers is unnecessary and obscures the linear structure.
- **Store every one position:** A positions list simplifies anchor lookup but uses $O(n)$ space in the worst case.
- **All zeros:** Every non-empty part represents zero, so many answers are valid.
- **One count not divisible by three:** No partition can give all three parts the same positive value.
- **Trailing zeros:** Each significant pattern must include exactly as many trailing zeros as the third part; insufficient space before a later anchor makes the partition fail.
- **Leading zeros:** They may be assigned to the following part without changing its value.
- **Multiple valid cuts:** Any valid pair is acceptable, so validation must compare the represented values rather than require one fixed pair.
