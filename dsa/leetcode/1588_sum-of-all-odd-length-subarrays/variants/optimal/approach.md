## General

**Group subarrays by their ending index**

Every odd-length subarray has exactly one right endpoint. The solution processes endpoints from left to right and keeps two dynamic-programming sums:

- `f[i]` is the sum of the sums of all odd-length subarrays ending at index `i`;
- `g[i]` is the sum of the sums of all even-length subarrays ending at index `i`.

Once `f[i]` is known, it can be added to the final answer because it contains the complete contribution from all odd-length subarrays whose final index is `i`. Summing `f[i]` over every endpoint counts every required subarray once.

This is different from storing one ordinary prefix sum. A prefix sum quickly computes the sum of one chosen subarray, while `f` and `g` aggregate the sums of many subarrays at once and exploit how their length parity changes when a new element is appended.

**Why parity alternates when extending a subarray**

Take any subarray ending at `i - 1` and append `arr[i]`:

- an even-length subarray becomes odd;
- an odd-length subarray becomes even.

Therefore, all non-singleton odd subarrays ending at `i` come from even subarrays ending at `i - 1`. All even subarrays ending at `i` come from odd subarrays ending at `i - 1`.

The sum of an extended subarray is its previous sum plus `arr[i]`. If several subarrays are extended, their old sums are already aggregated in `g[i - 1]` or `f[i - 1]`, and `arr[i]` must be added once for every extended subarray. The only remaining task is to know how many previous subarrays have the relevant parity.

**Deriving the odd-ending recurrence**

There are `i` non-empty subarrays ending at `i - 1`, with lengths one through `i`. Among those lengths, exactly `i // 2` are even. Extending each of those even subarrays contributes:

- its old sum, whose aggregate is `g[i - 1]`;
- one new copy of `arr[i]` for each of the `i // 2` subarrays.

There is also the one-element subarray `[arr[i]]`. It has odd length and contributes another copy of `arr[i]`.

Consequently:

`f[i] = g[i - 1] + arr[i] * (i // 2 + 1)`.

The factor `i // 2 + 1` combines the extended even subarrays with the new singleton. It is not an arbitrary rounding formula.

For example, at `i = 4`, subarrays ending at index three have lengths one, two, three, and four. The even ones have lengths two and four, so two are extended into odd lengths three and five. The singleton creates length one. Thus `arr[4]` appears three times, and `4 // 2 + 1` is three.

**Deriving the even-ending recurrence**

Among the `i` subarrays ending at `i - 1`, the number with odd length is the number of odd integers from one through `i`, namely `(i + 1) // 2`.

Every even-length subarray ending at `i` is formed by extending one of these odd subarrays. There is no even singleton. Therefore:

`g[i] = f[i - 1] + arr[i] * ((i + 1) // 2)`.

The old sums of all extended odd subarrays contribute `f[i - 1]`, and the new endpoint value contributes once per extension.

**Initialization**

At index zero, the only non-empty subarray ending there is `[arr[0]]`. It has odd length, so:

- `f[0] = arr[0]`;
- `g[0] = 0`.

The code creates zero-filled arrays, then performs the chained assignment `ans = f[0] = arr[0]`. `g[0]` remains its initialized zero. This also places the only odd subarray ending at zero into the answer before the loop starts.

The input is guaranteed non-empty, so reading `arr[0]` is safe.

**Building the final answer**

For each index from one through `n - 1`, the source computes `f[i]` and `g[i]` from the immediately previous entries. It then performs `ans += f[i]`.

To see why this gives the full requested sum, partition all odd-length subarrays according to their right endpoint. The group ending at zero sums to `f[0]`, the group ending at one sums to `f[1]`, and so forth. These groups are disjoint and collectively contain every odd-length subarray. Their aggregate is exactly `ans`.

**A short trace**

For `arr = [1, 4, 2]`:

- At index zero, `f[0] = 1` and `g[0] = 0`. The answer is one.
- At index one, `f[1] = g[0] + 4 * 1 = 4`, representing only `[4]`. `g[1] = f[0] + 4 * 1 = 5`, representing `[1,4]`. The answer becomes five.
- At index two, `f[2] = g[1] + 2 * 2 = 9`. This is the sum of `[2]` and `[1,4,2]`, namely two plus seven. `g[2] = f[1] + 2 * 1 = 6`, representing `[4,2]`. Adding `f[2]` produces fourteen, the sum of all odd-length subarray sums.

**Why the recurrence is correct**

Every subarray ending at `i` is either the singleton at `i` or uniquely obtained by extending a subarray ending at `i - 1`. Extension flips parity, and the formulas include precisely the correct previous parity class plus one copy of the new value per extension. Therefore, by induction, `f[i]` and `g[i]` maintain their definitions at every index.

Since only `f` groups represent odd-length subarrays and each is added once, the returned value is exact.

## Complexity detail

Let $N$ be the length of `arr`.

The initialization is constant time, and the loop processes each remaining index once. Every iteration performs a constant number of arithmetic operations and array accesses, so the total time complexity is $O(N)$.

The exact checked-in source allocates both `f` and `g` with $N$ entries. Its actual auxiliary space complexity is therefore $O(N)$. The package manifest’s $O(1)$ space bound corresponds to a straightforward optimization that retains only the previous odd and even aggregate values, because the recurrence never reads entries older than `i - 1`. That scalar optimization is not present in this source, so the exact implementation uses linear memory.

The integer answer can grow beyond a narrow machine integer, but Python integers expand automatically.

## Alternatives and edge cases

- **Contribution counting per element:** Count how many odd-length subarrays contain each index and multiply that occurrence count by `arr[i]`. It also runs in $O(N)$ time and can use $O(1)$ space, but derives the result through combinatorial endpoint choices rather than parity DP.
- **Scalar parity DP:** Replace arrays `f` and `g` with two previous-state variables. It preserves the exact recurrence and $O(N)$ time while achieving the manifest’s $O(1)$ auxiliary space.
- **Enumerate all subarrays with rolling sums:** Maintaining a sum for every start avoids a third loop but still takes $O(N^2)$ time.
- **Recompute every subarray sum:** Three nested loops are conceptually direct but take $O(N^3)$ time.
- **One element:** Initialization returns that value. The loop is empty, and the sole subarray has odd length.
- **Two elements:** Only the two singleton subarrays are odd. The recurrence’s `f[1]` contains only the second singleton, so the answer is their sum.
- **Odd full-array length:** The recurrence includes the full array in `f[n - 1]` because its parity is odd.
- **Even full-array length:** The full array contributes to `g[n - 1]` and is intentionally not added to `ans`.
- **Positive input values:** Positivity is part of the contract but not required by the recurrence; parity grouping would also work for zero or negative values.
- **Large totals:** A fixed-width implementation may need a wider integer type. Python avoids overflow.
- **Array allocation mismatch:** Although only the previous state is mathematically needed, this source stores every `f[i]` and `g[i]`. Documentation and memory analysis must reflect that exact choice.
- **No empty subarray:** The initialization and recurrences include only non-empty subarrays. The empty subarray contributes nothing and is not part of the problem definition.
