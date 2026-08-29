## General

**Focus on adjacent differences instead of the final common value.** The array is equal exactly when every neighboring pair is equal. Define the boundary difference at position $i$ as

$$
d_i=\texttt{nums}[i]-\texttt{nums}[i+1].
$$

The target condition is simply $d_i=0$ for all $0\le i<n-1$. It does not matter what shared value the array finally has.

**Understand what one prefix operation changes.** Suppose an operation selects the prefix ending at index $p$, then adds an arbitrary integer `k` to positions 0 through $p$.

For every adjacent pair entirely inside that prefix, both values receive the same addition, so their difference does not change. Pairs entirely outside the prefix also remain unchanged. Only the boundary pair $(p,p+1)$ has its left value changed while its right value stays fixed. Thus an operation on that prefix changes exactly one adjacent difference: $d_p$.

If the selected prefix is the whole array, both members of every adjacent pair change together, so no boundary difference changes at all. Such an operation can alter the eventual common value but can never help make unequal neighbors equal, so it is unnecessary in a minimum solution.

**Every unequal boundary forces an operation.** If `nums[i] != nums[i + 1]` initially, then $d_i\ne0$. No operation ending before or after index $i$ can change this difference: either neither endpoint changes or both endpoints change equally. At least one operation whose prefix ends exactly at $i$ is therefore mandatory.

Different unequal boundaries require different prefix lengths. One operation has only one ending boundary, so it cannot simultaneously correct two nonzero adjacent differences. This establishes a lower bound equal to the number of unequal neighboring pairs.

**One operation is also sufficient for each unequal boundary.** Process boundaries from right to left. At boundary $i$, choose the prefix through index $i$ and add whatever integer makes its current left endpoint equal its right endpoint. Because the added amount is unrestricted and may be negative, one operation always suffices.

This adjustment does not disturb any boundary to the right: both endpoints of earlier corrected boundaries lie outside the shorter prefix. It may shift boundaries to the left, but those have not yet been finalized and will receive their own operations later. After handling every initially unequal boundary, all adjacent pairs are equal.

There is an even more algebraic view. Each prefix ending at $i$ controls only $d_i$, so choose the addition `k = -d_i` in the difference representation. Operations at other boundaries leave $d_i$ unchanged. The adjacent-difference coordinates are independent, and each nonzero coordinate needs exactly one arbitrary adjustment.

**Why initially equal boundaries never need their own operation.** An operation ending elsewhere affects either both elements or neither element of an equal pair, preserving equality. The right-to-left construction therefore never turns a zero $d_i$ into a nonzero one through operations for other boundaries. Spending an operation ending at an initially equal boundary would be unnecessary.

**The implementation is the mathematical result directly.** `pairwise(nums)` yields

`(nums[0], nums[1]), (nums[1], nums[2]), ...`.

For each pair, expression `x != y` produces Boolean `True` for a nonzero adjacent difference and `False` otherwise. In Python, these behave as integers one and zero in `sum`. The returned value is exactly the count proved necessary and sufficient above.

**Trace `[1,4,2]`.** Both boundaries differ, so the source returns two. One construction first changes prefix `[1,4]` by $-2$, producing `[-1,2,2]` and fixing the right boundary. Then it changes prefix `[-1]` by $3$, producing `[2,2,2]`. The order illustrates why correcting from right to left avoids disturbing finished work.

For `[5,5,2,2]`, only the middle boundary differs, so a single operation on the first two elements can make all four equal. The equal boundaries on either side remain equal because both of their endpoints are shifted together or not shifted at all.

**Why the count is the exact minimum.** Each unequal adjacent boundary supplies an independent one-operation lower bound, while the right-to-left construction meets all those bounds with exactly one operation per boundary. Since the lower and upper bounds coincide, counting unequal adjacent pairs gives the minimum rather than merely some feasible number of operations.

## Complexity detail

Let $n$ be the array length. `pairwise` lazily produces $n-1$ adjacent pairs, and each comparison takes constant time. Total time is $O(n)$.

The iterator and running sum use $O(1)$ auxiliary space. No list of differences or pairs is created, and `nums` is not modified. The source assumes `pairwise` is imported from `itertools` and `List` is supplied for the annotation.

## Alternatives and edge cases

- **Explicit difference array:** Building every $d_i$ makes the proof visible but uses $O(n)$ storage merely to count nonzero entries.
- **Simulate prefix operations:** It can find a construction but may repeatedly rewrite long prefixes, leading to $O(n^2)$ time.
- **Process left to right:** A valid construction is possible with careful bookkeeping, but later longer-prefix changes can disturb already fixed left boundaries; right-to-left is the clearer witness.
- **Single element:** There are no adjacent pairs, `pairwise` is empty, and zero operations are necessary.
- **Already equal array:** Every comparison is false, so the sum is zero.
- **All adjacent pairs different:** The answer reaches its maximum $n-1$.
- **Repeated blocks:** Only transitions between different block values contribute.
- **Negative values:** The permitted addition can also be negative, so sign imposes no restriction.
- **Large magnitude differences:** One operation can use any integer `k`, so magnitude does not increase the operation count.
- **Whole-array prefix:** It changes the final common value but no adjacent difference and is never required.
- **Boolean summation:** Python's `True == 1` and `False == 0` make the one-line count exact.
- **Import requirement:** On Python versions before 3.10, `itertools.pairwise` is unavailable and an equivalent adjacent zip would be needed.
- **Input name inconsistency:** The description mentions both `nums` and `arr`, but the executable contract and source consistently use `nums`.
