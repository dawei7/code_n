## General

**Count each element's contribution instead of constructing subsequences.** A non-singleton consecutive subsequence is either increasing by exactly one at every step or decreasing by exactly one at every step. There can be exponentially many such subsequences, so listing them is impossible. The source asks, for every array position, how many qualifying subsequences contain that element. Multiplying that count by the element's value and summing over positions gives the sum of all subsequence values.

The nested helper `calc(nums)` handles increasing-by-one subsequences of length at least two. The outer method runs it once in original order and once after reversing the array to account for decreasing subsequences.

**Count possible increasing left arms.** In the forward loop, the counter has a precise meaning after processing positions before $i$: `cnt[v]` is the number of nonempty increasing-by-one subsequences entirely in that processed prefix whose final value is $v$.

When position `i - 1` with value $v$ is incorporated, it creates one singleton subsequence ending at $v$. It can also extend every previously known subsequence ending at $v-1$. Therefore the update

`cnt[v] += 1 + cnt[v - 1]`

is exact. The `+=` matters because different occurrences of value $v$ create distinct index subsequences even when their values look identical.

After that update, `left[i] = cnt[nums[i] - 1]` counts all nonempty increasing subsequences from earlier indices whose final value is exactly one smaller than the current value. Any one of them can be placed immediately before position $i$ in an increasing-by-one subsequence. Call these possibilities the current element's left arms.

**Count possible increasing right arms.** The backward loop is symmetric. Scanning positions after $i$ from right to left, `cnt[v]` counts nonempty subsequences that start at a processed later position with value $v$ and then increase by one while indices move forward.

When a later position has value $v$, it creates a singleton right arm and can be followed by every stored arm starting with $v+1$. The update is `cnt[v] += 1 + cnt[v + 1]`. Therefore `right[i] = cnt[nums[i] + 1]` counts the nonempty increasing right arms that can immediately follow `nums[i]`.

**Combine arms around each position.** Let $l=\texttt{left}[i]$ and $r=\texttt{right}[i]$. An increasing subsequence of length at least two containing position $i$ has exactly one of three forms:

- a nonempty left arm and no right arm: $l$ choices;
- no left arm and a nonempty right arm: $r$ choices;
- a nonempty arm on both sides: $lr$ choices.

Thus position $i$ occurs in $l+r+lr$ increasing consecutive subsequences of length at least two, contributing

$$
(l+r+lr)\cdot\texttt{nums}[i]
$$

to their combined values. Summing this expression over all positions counts every element of every increasing subsequence once. A whole subsequence is intentionally represented at each of its positions, because its value is the sum of all its elements.

**Reuse increasing logic for decreasing subsequences.** The source first computes `x = calc(nums)`. It then calls `nums.reverse()` and computes `y = calc(nums)`. An increasing-by-one subsequence in the reversed array corresponds, when its selected positions are put back into original index order, to a decreasing-by-one subsequence in the original array. Reversal changes index direction and therefore reverses the value sequence; its element sum remains unchanged. Hence `y` is the total contribution of all original decreasing subsequences of length at least two.

Singleton subsequences satisfy both definitions vacuously, but they must appear only once in the final answer. `calc` deliberately excludes them because its coefficient is zero when both arms are empty. The outer method adds `sum(nums)` once, covering exactly all singleton values. Reversing does not change that sum.

**Why modulo can be applied to the total.** `calc` takes its final sum modulo $10^9+7$, and the outer return reduces `x + y + sum(nums)` again. Modular addition and multiplication preserve the requested residue, so the final number is mathematically correct despite the intermediate counts being exact Python integers.

**Exact-source engineering caveats.** `nums.reverse()` mutates the caller-provided list and leaves it reversed when the method returns. The problem does not inspect the input afterward, but this side effect is important for reusable code.

More seriously, counter values are never reduced modulo `mod`. The number of index subsequences can be exponentially large, so Python's arbitrary-precision integers can acquire many bits. The source performs $O(n)$ counter updates, but those updates are not constant-time in a bit-complexity model, and intermediate memory can greatly exceed the manifest's simple $O(V)$ claim. Applying modulo during every counter update would preserve the final residue and restore bounded-size arithmetic.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$ and let $V$ denote the number or range of relevant values. Each `calc` performs one forward pass, one backward pass, and one zipped sum, so it makes $O(n)$ dictionary operations. Reversal and the singleton sum are also $O(n)$. Under the usual word-RAM assumption that counter arithmetic and hashing are constant-time, total time is expected $O(n)$, which is at least as tight as the manifest's `O(n + V)` because the source never loops across the value domain.

Each call allocates `left` and `right` arrays of length $n$, plus counters with at most $O(\min(n,V))$ keys. Peak structural storage is therefore $O(n+V)$, and in the given bounded domain it is $O(n+V)$. The manifest's `O(V)` omits the two explicit length-$n$ arrays unless $V$ is being used as a combined bound. Without per-update modular reduction, the bit storage of counter values can be much larger than this entry-count analysis.

## Alternatives and edge cases

- **Modulo every counter update:** Replace stored counts with their residues modulo $10^9+7$. Because only additions and multiplications affect the final result, this preserves correctness while preventing enormous arbitrary-precision intermediates.
- **Compute decreasing counts directly:** Mirror the value-neighbor directions instead of reversing `nums`. This avoids mutating the input and can make the two orientations explicit, at the cost of some duplicated logic.
- **Copy before reversing:** Calling `calc(nums[::-1])` preserves caller state but allocates another $O(n)$ list. The existing helper already allocates linear arrays, so asymptotic space is unchanged.
- **Enumerate subsequences:** The number of valid index subsequences can be exponential when values repeat, so enumeration cannot meet the constraints.
- **Count subsequences but not element sums:** Merely knowing how many sequences exist is insufficient. The contribution formula counts each position's value once for every sequence containing it.
- **Single-element input:** Both `left` and `right` remain zero, both `calc` calls contribute zero, and `sum(nums)` returns the only singleton's value.
- **Repeated equal values:** Equal adjacent subsequence values are not consecutive because the required difference is exactly $1$ or $-1$. Repeated occurrences still represent distinct choices for arms at other values.
- **Increasing subsequence of length two:** Its first position is counted through a right arm and its second through a left arm, so both values enter the subsequence total.
- **A sequence valid in both directions:** Only length-one sequences belong to both orientations. A length-two or longer sequence cannot have every difference simultaneously $1$ and $-1$.
- **Modulo and negative values:** The constraints make values positive. The method would still produce Python's nonnegative modulo residue for signed totals, but that extension is outside the contract.
- **Input mutation:** After execution, `nums` is reversed. A production-quality method should restore it or avoid in-place reversal if callers expect inputs to remain unchanged.
- **Counter key range:** Queries for `v-1` or `v+1` can create zero-default entries just outside the input range, but only a linear number of neighboring keys can appear.
- **Manifest discrepancy:** The exact source uses $O(n)$ left/right arrays and unbounded integer counts. Its practical space behavior is not captured by a bare $O(V)$ statement.
