## General

**Track a continuous coverage frontier.**

Trying to store every subset sum would be far too expensive because each element can be selected or omitted. The greedy solution instead summarizes all relevant subset sums with one number, `x`.

Its invariant is:

> Before each loop iteration, using the input values already consumed plus the patches already chosen, every integer sum from `1` through `x - 1` can be formed. The value `x` is the smallest sum not yet guaranteed to be formable.

It is also useful to include the empty subset's sum zero mentally. The known interval is then every sum from `0` through `x - 1`. Initially, `x = 1`. No positive value is covered yet, so the interval `1` through `0` is empty and the invariant is true.

The loop continues while `x <= n`, because the first uncovered value is still inside the required range. Once `x > n`, every value from `1` through `n` lies below the frontier and is covered.

**Use the next input value when it can touch the covered interval.**

Let the next unused sorted value be $v=\text{nums}[i]$. If $v\le x$, it can extend coverage without leaving a gap.

Before using $v$, old subset sums cover

$$
[0,x-1].
$$

Selecting $v$ together with any old subset produces the shifted interval

$$
[v,v+x-1].
$$

Because $v\le x$, this shifted interval starts no later than one position after the old interval ends. The two intervals therefore touch or overlap, and their union covers

$$
[0,x+v-1].
$$

The new smallest uncovered sum is $x+v$, exactly the source update `x += nums[i]`. The index advances because each array element is an individual item and may be consumed only once.

For example, if all sums through `6` are covered, then `x = 7`. Consuming a next value `5` creates new sums from `5` through `11` by adding `5` to old sums `0` through `6`. Together, the old and new intervals cover everything through `11`, so the frontier becomes `12`.

**Why a value larger than `x` cannot help yet.**

If the next input value is greater than `x`, it cannot be part of a subset summing to `x`: all values are positive, so including it would already exceed `x`. Excluding it leaves only previously consumed values, which by the invariant do not guarantee `x`. Since `nums` is sorted ascending, every later unused input is at least as large and cannot close the gap either.

At least one patch is therefore unavoidable at this point. This is the key fact that makes a greedy choice possible: the algorithm is not patching merely because it seems helpful; any valid completion must add some value no greater than the current missing sum.

**Why patching exactly `x` is best.**

Suppose a patch value $p$ is meant to cover the missing value `x`. Since all values are positive and previous subset sums reach only through $x-1$, the patch must satisfy $p\le x$. If $p>x$, it cannot participate in a sum equal to `x`.

After adding any $p\le x$, combining it with old sums extends guaranteed coverage at most through

$$
x+p-1.
$$

This upper endpoint is largest when $p=x$. Choosing a smaller patch may fill the immediate gap, but it advances the frontier less and cannot reduce the number of patches needed later. Thus the best forced patch is the missing value itself.

With $p=x$, the old interval `[0, x - 1]` and the shifted interval `[x, 2x - 1]` join perfectly. Coverage doubles to `[0, 2x - 1]`, making `2x` the next missing value. The source records one patch in `ans` and performs `x <<= 1`, which is a bit-shift spelling of multiplying the positive integer by two.

**Walk through `[1,5,10]` with target `20`.**

Start with `x = 1`, `i = 0`, and zero patches.

- The next value `1` is at most `x`. Consume it, extending coverage through `1`; now `x = 2`.
- The next value `5` is greater than `2`, so `2` cannot be formed. Patch `2`, extending coverage through `3`; now `x = 4` and the patch count is one.
- Value `5` is still greater than `4`. Patch `4`, extending coverage through `7`; now `x = 8` and the count is two.
- Value `5` is now usable because `5 <= 8`. Consume it, extending coverage through `12`; now `x = 13`.
- Value `10` is usable because `10 <= 13`. Consume it, extending coverage through `22`; now `x = 23`.

Since `23 > 20`, all required values are covered, and the answer is two. The patches are `[2,4]`.

For `[1,3]` and target `6`, consuming `1` moves `x` to `2`. The value `3` cannot cover the missing `2`, so patching `2` moves `x` to `4`. Then consuming `3` moves the frontier to `7`, covering the full target with one patch.

**Why the number of patches is minimal.**

At every patch step, `x` is genuinely not formable from all usable original values and earlier patches. Any successful strategy must introduce a patch no greater than `x`; otherwise `x` stays missing. So the greedy algorithm's patch consumes one action that no solution can avoid.

Among all patches that can fill this forced gap, choosing `x` gives the farthest possible new coverage frontier. After the same number of patch actions, no alternative choice can guarantee coverage beyond the greedy frontier. This is a dominance argument: replacing an alternative's first gap-closing patch with `x` never reduces what is coverable and does not use an extra patch.

Apply that exchange at every gap encountered. If greedy uses another patch, any competing strategy with no more patches cannot have advanced farther and must also spend an action to cover the same frontier. Therefore no strategy can finish with fewer patches than `ans`.

**Why sorted order matters.**

The algorithm only examines `nums[i]`, the smallest unused original value. If it is too large, sorted order proves all later values are too large as well, so a patch is forced. If the array were unsorted, a smaller usable value could appear later and the greedy decision would need a preliminary sort or another way to retrieve the smallest remaining value.

## Complexity detail

Let $m$ be `len(nums)`. Each loop iteration does one of two things: it consumes one array element and increments `i`, which can happen at most $m$ times, or it patches and doubles `x`. Starting from one, only $O(\log n)$ doublings can occur before `x > n`.

The total time complexity is therefore $O(m+\log n)$. Values beyond the useful frontier may remain unconsumed, so this is an upper bound.

Only `x`, `ans`, and `i` are maintained. The input is already sorted and no subset-sum structure is stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Explicit subset-sum set or Boolean table:** Updating all reachable sums can solve smaller bounded targets, but it needs $O(n)$ or more storage and potentially $O(mn)$ time. Here `n` can approach $2^{31}-1$, making that approach impossible.

- **Patch with a smaller value than `x`:** It may close the immediate gap, but extends the frontier less than patching `x`. It cannot lead to fewer future patches under the coverage invariant.

- **Patch with a value larger than `x`:** Positive numbers already consumed cannot combine with it to make the smaller missing value `x`, so the gap remains. Such a patch is invalid as the next greedy action.

- **Input already covers the target:** Every next value is consumed while it is at most the frontier, and `ans` remains zero. For `[1,2,2]` and target `5`, the frontier advances `1 -> 2 -> 4 -> 6` with no patch.

- **First value greater than one:** Since `x` begins at `1`, patching `1` is forced. No positive value greater than one can form sum one.

- **Unused large values:** If `x` exceeds `n` before all input values are consumed, the loop stops. Values beyond the target are irrelevant because required coverage is already complete.

- **Duplicate values:** Each occurrence is a separate selectable element. If a duplicate is at most `x`, consuming it legitimately extends coverage by its value again.

- **Large target and overflow:** Python integers grow automatically. In fixed-width languages, `x` should use a wider integer type because the final doubling can exceed the signed 32-bit target even though `n` itself fits.
