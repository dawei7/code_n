## General

Every valid subarray is either strictly increasing by one at each step, strictly decreasing by one, or a singleton. The source aggregates values of all valid subarrays ending at each index without enumerating their starts.

`f` is the length of the current plus-one run. `s` is the sum of the values of all increasing-consecutive subarrays ending at the current element. Symmetrically, `g` and `t` describe the minus-one run.

Initially the first singleton is both an increasing and decreasing run of length one, but it must be counted only once. The state variables start at one and `nums[0]`, while `ans` begins with `nums[0]`.

Suppose adjacent values are `x,y` and `y-x == 1`. Every prior increasing subarray ending at `x` can extend with `y`, and singleton `[y]` is new. If the old run length is `f-1`, adding `y` to all extensions plus the singleton adds `f * y` after incrementing `f`. Therefore `s += f * y`. This new `s` is the total value of all increasing subarrays ending at `y` and is added to the answer.

If the pair is not plus one, increasing state resets to singleton: `f=1,s=y`, but it is not immediately added because the decreasing branch or explicit singleton branch will handle `y` exactly once.

The minus-one recurrence is identical with `g,t`. When `y-x == -1`, `t += g*y` and the total decreasing-ending contribution is added.

If the absolute difference is neither one, neither directional branch adds anything, so `ans += y` counts the singleton. When the difference is plus one or minus one, the corresponding `s` or `t` already includes that singleton, preventing double counting.

For `[1,2,3]`, increasing ending totals are one, five, and fourteen. Added across endpoints they produce twenty, which equals the values of all six valid subarrays.

For `[7,6,1,2]`, the decreasing state counts `[7,6]`, the break counts singleton one, and the increasing state counts `[1,2]`, producing thirty-two.

**Why longer direction-changing arrays are excluded.** A subarray such as `[3,4,3]` belongs to neither uninterrupted run at its final endpoint. Run state resets when direction changes, so it is never aggregated.

Modulo is applied to `ans` after contributions. `s` and `t` remain exact integers; Python safely stores them under constraints.

## Complexity detail

`pairwise(nums)` visits each adjacent pair once, and each iteration performs constant arithmetic. Time complexity is $O(n)$.

Only six scalar state values are maintained, giving $O(1)$ auxiliary space. The `pairwise` iterator is lazy. The output is one integer.

## Alternatives and edge cases

- **Enumerate all subarrays:** Checking every candidate takes at least $O(n^2)$ time.
- **Store run arrays:** Prefix lengths for both directions work but use $O(n)$ space; rolling state is sufficient.
- **Count only run lengths:** The task sums subarray values, not counts, so ending-value aggregates `s,t` are needed.
- **Single element:** The loop is empty and the initialized value is returned.
- **Difference plus one:** Only increasing aggregation runs; the singleton is included there.
- **Difference minus one:** Only decreasing aggregation runs.
- **Difference zero:** Neither direction qualifies, and only the singleton is added.
- **Direction reversal:** Both run states reset appropriately on the branch they do not extend.
- **Overlapping valid subarrays:** Ending aggregates intentionally count each distinct start separately.
- **Modulo:** Reducing contributions during accumulation is algebraically safe; the source reduces the running answer.
- **Missing `pairwise` import:** A standalone module needs `from itertools import pairwise` if the harness does not provide it.
- **Positive values:** State initialization uses actual first value and needs no empty-array case because length is at least one.
- **Meaning of `s` after extension:** It includes the singleton ending at `y` and every longer plus-one suffix. Adding it to `ans` counts all valid increasing subarrays by their unique right endpoint.
- **Why `f*y` is added:** There are `f-1` old suffixes to extend plus one new singleton. Each receives one new copy of `y` in its value, totaling exactly `f` copies.
- **Reset does not lose future information:** Once an adjacent difference fails, no earlier increasing suffix can cross it. The only possible increasing suffix ending at `y` starts with `y` itself.
- **Singleton ownership:** Exactly one of three paths counts `[y]`: the increasing aggregate, the decreasing aggregate, or the explicit nonconsecutive branch. The plus-one and minus-one tests cannot both be true.
- **Modulo and ending totals:** `s` and `t` need not be reduced for correctness because only their residues affect `ans`. Reducing them too would also be valid and could ease fixed-width ports.
- **Maximum intermediate scale:** Long runs can make ending aggregates much larger than individual values. Python integer arithmetic avoids overflow before the answer's modulo reduction.
- **Several separate runs:** Reset states ensure subarrays never cross a break, while `ans` retains contributions from earlier completed runs.
- **Pairwise availability:** The exact file assumes Python 3.10's `itertools.pairwise` or an equivalent harness import; older runtimes require a manual adjacent-index loop.
