## General

**Measure the longest run of one chosen character.** The helper `f(x)` computes the maximum length of a contiguous segment containing only character `x`. The main method calls it once for one and once for zero, then compares the two results strictly.

Inside the helper, `cnt` is the length of the current run ending at the most recently scanned character, while `mx` is the longest completed or current run seen anywhere so far.

**Extend a matching run.** When `c == x`, `cnt += 1` extends the current contiguous segment. `mx = max(mx, cnt)` immediately records it if this is a new longest run.

Updating `mx` during every matching character means no special action is required when a run reaches the end of the string.

**Reset on the opposite character.** When `c != x`, the current `x` segment has ended, and `cnt = 0` prepares for a possible new segment later. The stored maximum remains unchanged.

**Why contiguity is captured.** `cnt` accumulates only across uninterrupted matching characters. Encountering the other bit erases the current length, so matching characters separated by a different bit can never be combined into one run.

**Trace `"1101"` for ones.** The first two characters raise `cnt` to one and then two, so `mx` becomes two. The zero resets `cnt`. The last one begins a new run of length one, which does not exceed two. Thus `f("1")` returns two.

For zeros, only one zero occurs, so `f("0")` returns one. The strict comparison two greater than one returns true.

**Tie behavior is deliberate.** For `"111000"`, both helper calls return three. The condition uses `>` rather than `>=`, so equality returns false, exactly matching “strictly longer.”

**Absent-character behavior.** If `x` never appears, `cnt` and `mx` remain zero. This directly implements the statement’s convention that the longest missing-character segment has length zero.

For an all-one string, the one maximum is the full string length and the zero maximum is zero, so the result is true. For an all-zero string, the result is false.
After processing each character, `cnt` equals the length of the maximal suffix of the processed prefix consisting entirely of `x`. This is extended on a match and reset on a mismatch. `mx` is updated with every such suffix length, so it equals the longest `x` run found in the processed prefix. Induction proves the returned value is the global longest run.

Calling the helper for both possible binary characters produces exactly the two quantities in the problem definition. Their strict comparison therefore returns the correct Boolean.

**Why two scans are still linear.** The string is traversed twice, but a constant factor of two does not change `O(n)`. A one-pass version could maintain current and maximum runs for both bits, but the helper keeps the logic small and symmetric.

**Current run versus historical maximum.** These variables must remain separate. `cnt` is allowed to decrease abruptly to zero when the other character appears, while `mx` must never decrease because an earlier run remains a valid candidate even after it ends. Using only one counter would forget the best completed segment whenever a later separator appeared.

For `"110111"` while measuring ones, `cnt` reaches two, resets at zero, then grows to three. `mx` preserves two through the reset and finally becomes three. This example shows why resetting the current run does not erase useful history.

## Complexity detail

Each call to `f` visits all `n` characters and performs constant work. Two calls take `2n` operations, which is `O(n)` time.

Each helper stores two integers and one target character. No substring, run list, or counter collection is allocated, so auxiliary space is `O(1)`.

## Alternatives and edge cases

- **One-pass dual tracking:** Maintain the current character, current run length, and maxima for zero and one in one traversal.
- **Split on the opposite bit:** Maximum token length after splitting can work, but creates substring lists and uses `O(n)` space.
- **Regular expressions:** They can find runs but add unnecessary machinery and allocation.
- **All ones:** Longest one run is `n` and longest zero run is zero.
- **All zeros:** Longest one run is zero, so the strict condition is false.
- **Equal maxima:** The answer is false because one must be strictly longer.
- **Alternating input:** Both maximum runs are one when both symbols occur, so the answer is false.
- **Single character one:** The maxima are one and zero, returning true.
- **Single character zero:** The maxima are zero and one, returning false.
- **Run at the end:** Updating `mx` on every match records it without a post-loop branch.
- **Several separate runs:** Resetting `cnt` prevents their lengths from being combined.
- **Input preservation:** The immutable string is scanned twice and never modified.
- **Run of length one between separators:** It raises `mx` only if no longer run has appeared; surrounding opposite bits keep it separate.
- **Historical maximum after reset:** Resetting `cnt` never resets `mx`, so a strong early segment remains recorded.
- **Strict comparison direction:** The method asks whether the one-run is longer than the zero-run, so reversing operands would solve the opposite question.
- **No integer conversion:** Direct character comparison avoids parsing and exactly matches the binary symbols supplied.
