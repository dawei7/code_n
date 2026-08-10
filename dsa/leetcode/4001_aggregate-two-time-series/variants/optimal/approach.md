## General

**“Next available” points naturally to the first unprocessed entry.**  Each series is sorted by strictly increasing timestamp. At a queried time `t`, a series contributes the value from its first entry whose timestamp is at least `t`. If no such entry remains, its contribution is zero.

The output needs only timestamps that appear in at least one input. This is the same ordered-union structure as merging two sorted arrays, but with one extra detail: when the next timestamps differ, the later entry's value is already the “next available” value for the earlier timestamp.

The exact source keeps two indices:

- `i` points to the first unprocessed entry of `series1`;
- `j` points to the first unprocessed entry of `series2`.

All union timestamps smaller than both current entries have already been emitted. Therefore, when the next output timestamp is chosen, the values at the two pointers are precisely the contributions required by the contract.

**Case one: the timestamps are equal.**  If `t1 == t2`, both series have an explicit entry at the same next union timestamp. The output receives

`[t1, v1 + v2]`.

Both entries have now been consumed for their own timestamp, so both `i` and `j` advance.

**Case two: the first timestamp is earlier.**  If `t1 < t2`, the next union timestamp is `t1`.

- `series1` contributes `v1` from its entry exactly at `t1`.
- `series2` has no entry at `t1`. Its first available timestamp is the current `t2`, so it contributes `v2`.

The source appends `[t1, v1 + v2]` and advances only `i`. It deliberately leaves `j` unchanged. The same `series2[j]` value may remain the next available value for several `series1` timestamps that occur before `t2`.

**Case three: the second timestamp is earlier.**  If `t2 < t1`, the reasoning is symmetric. The output timestamp is `t2`, `series2` contributes its exact `v2`, and the future `series1` entry contributes `v1`. Only `j` advances.

These three branches always emit the smaller current timestamp, or the common timestamp when equal. Since each input is strictly increasing, the output is also strictly increasing and contains no duplicate timestamp.

**Why advancing only the owner of the emitted earlier timestamp is essential.**  Consider `series1` timestamps `1` and `4` while the next `series2` timestamp is `5`. At both timestamps `1` and `4`, the next available `series2` entry is still the entry at `5`. If the algorithm advanced `j` after producing timestamp `1`, it would discard the value needed at timestamp `4`. Keeping the later pointer fixed models the forward-looking rule exactly.

**What happens when one series is exhausted.**  The main loop stops when either pointer reaches the end. Every remaining timestamp belongs only to the nonempty series. The exhausted series has no current or future timestamp, so its contribution at all of those remaining times is zero.

The source can therefore append the remaining rows from the nonempty series unchanged. Adding zero would not alter their values.

**A loop invariant explains the full merge.**  At the start of each main-loop iteration:

- `ans` contains the correct aggregate for every union timestamp smaller than both current pointer timestamps;
- those output timestamps are in strictly increasing order;
- `series1[i]` and `series2[j]` are the first entries from their series not yet passed;
- each current value is the correct “next available” contribution for the smaller of the two current timestamps.

Every branch emits exactly that next union timestamp with both correct contributions and advances precisely the entries that occur at the emitted time. The invariant is preserved. When the loop ends, the tail logic adds all remaining union timestamps with zero from the exhausted side, so no timestamp is omitted.

**Walk through the first example.**  Start with `[1, 3]` and `[2, 2]` at the two pointers.

- `1 < 2`, so timestamp `1` receives `3 + 2 = 5`. Advance only the first pointer.
- The pointers now show `[4, 1]` and `[2, 2]`. Since `2 < 4`, timestamp `2` receives `1 + 2 = 3`. Advance only the second pointer.
- The pointers show `[4, 1]` and `[5, 2]`. Timestamp `4` receives `1 + 2 = 3`.
- `series1` is exhausted. Its contribution at the remaining timestamp `5` is zero, so append `[5, 2]`.

The result is `[[1, 5], [2, 3], [4, 3], [5, 2]]`.

Notice that the algorithm never iterates across every integer time between two timestamps. A gap from `1` to `1_000_000_000` costs no additional work because only timestamps present in an input belong in the output.

**Manifest wording versus the exact source.**  The Optimal manifest summary says the method “merges timestamps from right to left.” The exact implementation does the opposite: `i` and `j` begin at zero, increase after entries are consumed, and emit timestamps in ascending order. It is a left-to-right merge whose pointers retain future values. The complexity fields remain accurate, but that directional summary does not describe the stored code.

## Complexity detail

Let `m = len(series1)` and `n = len(series2)`. Each main-loop iteration advances `i`, `j`, or both. The tail loops advance through whatever entries remain. No input row is processed more than once.

- Time complexity is `O(m + n)`.
- Auxiliary space complexity is `O(1)` when the required output is excluded.

The output has one row per distinct timestamp in the union, so it can contain up to `m + n` rows and necessarily uses `O(m + n)` output space. The algorithm itself maintains only two indices and a constant number of current timestamp/value variables.

In the tail loops, `ans.append(series1[i])` or `ans.append(series2[j])` appends the existing two-element row object rather than making a new row. This does not change the returned values and the method does not mutate either input, but it means those tail rows are shared references in Python. Rows produced in the main loop are newly allocated.

## Alternatives and edge cases

- **Binary-search each union timestamp:** One could build the union and use lower-bound searches in both series, taking `O((m+n)(\log m+\log n))` time. The monotone pointers reuse search progress and give a linear merge.
- **Hash maps by exact timestamp:** A map does not directly answer “first timestamp at least `t`.” Extra sorting or successor queries would still be required.
- **Scan every integer timestamp:** Timestamp values can be as large as `10^9`, and only input timestamps belong in the result. Iterating through gaps is both unnecessary and potentially enormous.
- **Merge from right to left:** A reverse traversal could maintain different state, but it is not what the exact source does. The current implementation moves from smallest to largest timestamp.
- **Equal timestamps:** Emit one row containing the sum and advance both pointers, preventing a duplicate output timestamp.
- **Several timestamps before the other series' next entry:** Keep the later pointer fixed so its value can contribute repeatedly as the next available value.
- **One series ends early:** It contributes zero at every later timestamp, so remaining rows from the other series can be appended unchanged.
- **Identical timestamp lists:** Every iteration uses the equality branch, and the output is the elementwise value sum.
- **Widely separated timestamps:** Runtime depends on the number of rows, not on numeric gaps.
- **Strictly increasing input:** This guarantee ensures each series has at most one value at a timestamp and lets the merge produce a strictly increasing union without deduplication inside one series.
- **Large values:** A sum can reach `2 \times 10^9` under the stated bounds. Python handles it directly; fixed-width implementations should choose a type that safely covers the required sum.
- **Input mutation:** Pointer movement changes only local indices. The source never edits the input arrays or their rows.
- **Tail-row aliasing:** Because remaining rows are appended by reference, mutating a returned tail row later could also mutate the corresponding input row. This is an exact Python object-sharing detail, not a numerical error in the produced aggregate.
