## General

**Describe a trade through three neighboring runs.** In the augmented string, a valid first step chooses a one-run surrounded by zero-runs. Locally, the pattern is

$$
0^a1^b0^c,
$$

where $a,b,c$ are positive run lengths.

Turning the middle $1^b$ into zeros merges all three runs into one zero-run of length $a+b+c$. The second step turns that merged run into ones. The original $b$ ones are removed and then restored, so their net contribution is zero. The two neighboring zero-runs become active, giving net gain

$$
(a+b+c)-b=a+c.
$$

Therefore, the middle one-run's length does not affect the score. A trade is completely valued by the sum of the two zero-runs on its sides.

**Augmentation makes boundary zero-runs usable.** Conceptual ones added before and after `s` ensure a zero-run at the original beginning or end is surrounded by ones when it becomes part of the merged second-step block. Those artificial ones are not counted, but they make the boundary trade legality uniform.

The source does not physically build `"1" + s + "1"`. The lengths of zero-runs inside `s` are unchanged by augmentation, so scanning the original string is enough.

**Scan maximal runs once.** Outer pointer `i` begins a run. Pointer `j` advances while characters equal `s[i]`, making `cur = j - i` the maximal run length.

If the run is a one-run, its length contributes to `ans`, the original number of active sections.

If it is a zero-run, `pre` stores the preceding zero-run's length in the sequence of zero-runs, and the code updates

`mx = max(mx, pre + cur)`.

Consecutive zero-runs in this sequence are necessarily separated by exactly one maximal one-run. Thus every computed sum represents one valid candidate trade and every removable surrounded one-run corresponds to one such adjacent zero-run pair.

After the comparison, `pre = cur` makes the current zero-run available to pair with the next one.

**The negative-infinity sentinel handles the first zero-run.** Before any zero-run is seen, `pre = -inf`. Adding its length cannot improve initial `mx = 0`. This prevents a single zero-run from being mistaken for a valid pair.

If the string has fewer than two zero-runs, no one-run is surrounded by two zero-runs, so no valid trade can increase the answer. `mx` remains zero and the original one count is returned.

For `s = "0100"`, zero-run lengths are one and two, separated by the one-run of length one. Their sum is three. The original active count is one, so the result is four.

For `s = "1000100"`, zero-run lengths are three and two. Trading the one-run between them gains five. The original two ones plus gain five produce seven.

For `"01010"`, the zero-run sequence is $1,1,1$. Adjacent sums are two and two, so the best result is the original two active positions plus two, equal to four.

**Why choosing a different second zero block cannot do better.** After removing a surrounded one-run, the merged zero block contains both its neighboring zero-runs and the removed ones. Turning this newly merged block on restores the sacrificed ones and activates both neighbors. Choosing some unrelated zero-run instead would lose the removed $b$ ones while gaining only that unrelated run, and it can always be matched or beaten by trading around one of its own adjacent one-runs. The local merged block is therefore the relevant optimal second step.
Run decomposition uniquely partitions the string. Every valid first-step one-run lies between two consecutive zero-runs in the zero-run list, and its trade gain is their sum. The source considers every consecutive pair exactly when the later zero-run is scanned and records their maximum. Adding that maximum to the exact original one count returns the best attainable active count. Keeping gain zero also represents performing no trade, as allowed by “at most one.”

## Complexity detail

Pointers `i` and `j` only move from left to right, and each character is visited a constant number of times. Total time is $O(n)$.

The source stores only pointers, current and previous run lengths, active count, and best gain. Auxiliary space is $O(1)$, matching the manifest.

The answer cannot exceed $n$ because only original positions count. Although the formula adds a gain to the original one count, the gained zero-runs were previously inactive and are disjoint from the counted ones.

## Alternatives and edge cases

- **Store all zero-run lengths:** This is correct but uses $O(z)$ space; only the previous length is needed for adjacent sums.
- **Try every substring trade:** Enumerating blocks can be quadratic or worse and ignores the simple run effect.
- **Include the middle one-run in net gain:** It is restored in the second step, so only neighboring zeros increase the count.
- **Only one zero-run:** No one-run has zero-runs on both sides, and no beneficial valid trade exists.
- **No zero-runs:** The string is already all active and the answer is $n$.
- **No one-runs:** There is no first-step block to convert, so the answer remains zero.
- **Boundary zero-run:** Conceptual augmented ones make it valid as a neighbor without contributing to the count.
- **Several equal best pairs:** Any of their middle one-runs yields the same maximum.
- **Long middle one-run:** Its length does not affect net gain.
- **At most one trade:** `mx=0` safely preserves the unchanged string when no trade helps or exists.
- **Run maximality:** Only maximal surrounded blocks matter; choosing a proper sub-block would not be surrounded by zeros on both sides.
- **Sentinel `-inf`:** It prevents the first zero-run from forming a nonexistent pair while leaving later arithmetic unchanged.
