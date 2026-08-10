## General

**Separate activation value from active lifetime**

An element contributes `value[i]` as soon as it is activated. That contribution remains in the total even if the element immediately or later becomes permanently inactive. Therefore, the objective is to choose which activation operations can be completed, not to maximize the sum of values that remain active at the end.

The `limit` controls two related events:

1. An element with limit `L` may be activated only while the current active count is strictly below `L`.
2. Whenever an activation temporarily raises the active count to `x`, every element with limit at most `x` becomes permanently inactive, whether it was active or had never been activated.

At first this looks like an order-dependent scheduling problem over all `n` elements. The key simplification is that elements sharing the same limit have a clean independent bound: among all elements whose limit is `L`, at most `L` can ever be activated.

**Why a limit-`L` group contributes at most `L` elements**

Assume, for contradiction, that more than `L` elements with limit `L` could be activated. Focus on the attempted `(L + 1)`-st activation from that group.

There are only two possibilities for the first `L` activated group members:

- If none of them has become inactive, all `L` are still currently active. The next group member cannot be activated because its rule requires the current count to be strictly less than `L`.
- If at least one has become inactive, that could only have happened after an activation made the count `x >= L`. At that event, the rule permanently deactivated all elements with limit at most `x`, including every still-inactive element of the limit-`L` group. There is then no group member left that may be activated later.

Both cases make an `(L + 1)`-st activation impossible. Thus a group containing `m` elements can contribute no more than `min(m, L)` activation values.

This upper bound depends only on the group’s limit and size. It does not say which group members should be chosen. Since every `value[i]` is positive, activating an additional permitted element always increases the total. We should therefore use the full allowance `min(m, L)` and choose the largest values in that group.

**Why all per-group allowances can be achieved together**

A collection of independent upper bounds would not be useful if reaching one group’s bound prevented reaching another’s. Here they are simultaneously achievable.

Conceptually process distinct limits in increasing order. Before processing a limit `L`, any active leftovers come only from previously processed smaller-limit groups. After every activation-and-deactivation step, each surviving active element has a limit greater than the count that triggered cleanup and therefore greater than or equal to what the reduced active count can challenge. As new elements are activated, any smaller-limit leftovers are removed when the temporary count reaches their limit.

This means old groups cannot permanently block the count below `L`. Activate the chosen members of the limit-`L` group one after another. If fewer than `L` are chosen, they can all be activated without exhausting this group’s limit. If exactly `L` are chosen, the `L`-th activation may raise the count to `L` and permanently deactivate the group, but that happens only after all `L` desired values have already been added to the total.

Then continue to the next larger limit. Deactivation never subtracts an earned value, and processing a larger limit gives enough room to activate its own selected members. Hence one valid global ordering realizes `min(m, L)` chosen activations from every limit group.

The source does not construct this order because the method only has to return the maximum total. The increasing-limit schedule is a proof that the independently computed group contributions can coexist. Consequently, the dictionary’s actual iteration order does not matter for the numerical sum.

**Group equal limits and keep their largest values**

The dictionary `g` maps each limit to the list of values having that limit. The loop

`for v, lim in zip(value, limit)`

visits corresponding entries of the two equal-length arrays and appends `v` to `g[lim]`. After this pass, every input element belongs to exactly one group.

For one dictionary entry `lim, vs`, the source sorts `vs` in non-decreasing order. Its best permitted contribution is the suffix

`vs[-lim:]`.

If the group has at least `lim` values, this slice contains exactly the largest `lim`. If it has fewer, Python’s slice simply begins before index zero conceptually and returns the entire list, which represents all `min(len(vs), lim)` permitted elements. Because constraints guarantee `lim >= 1`, there is no special zero-slice behavior to handle.

Adding the sum of each chosen suffix produces

`sum over each limit L of the largest min(group_size[L], L) values`.

The per-group upper bound proves no activation order can exceed this expression, and the increasing-limit schedule proves an order exists that attains it. The computed sum is therefore the global maximum.

**Trace the examples by groups**

For `value = [3, 5, 8]` and `limit = [2, 1, 3]`, the groups are:

- Limit one: values `[5]`, so take its largest one.
- Limit two: values `[3]`, so take all one available value.
- Limit three: values `[8]`, so take all one available value.

The total is `5 + 3 + 8 = 16`. The example’s activation order shows how the limit-one element can disappear immediately, freeing active-count room without losing its value.

For `value = [4, 2, 6]` with every limit equal to one, all values belong to a single limit-one group. At most one can be activated before the entire group becomes permanently inactive, so sorting and taking the largest one gives six.

For `value = [4, 1, 5, 2]` and `limit = [3, 3, 2, 3]`, the limit-two group contains only `[5]` and contributes five. The limit-three group contains `[4, 1, 2]` and may contribute all three values, totaling seven. The global answer is twelve.

**Why values from different limits should not compete in one heap**

The restriction is not “activate at most `L` elements whose limit is at most `L`.” An activation that causes deactivation can reset the currently active population while already-earned values remain counted. As a result, a low-limit choice does not consume a permanent shared slot that must be traded against a high-limit choice.

The correct cap applies separately to the number activated from each exact-limit group. Grouping by equality preserves that structure. Treating the problem as one conventional deadline heap without accounting for these resets would impose a different scheduling model and could discard values that are all attainable.

## Complexity detail

Let `n` be the number of elements, and let group sizes be `m_1, m_2, ..., m_g` with `m_1 + ... + m_g = n`. Building the dictionary takes expected `O(n)` time because each append uses expected constant-time hash-table access.

Sorting one group costs `O(m_i log m_i)`. Across all groups, the total sorting cost is

`O(sum of m_i log m_i)`,

which is at most `O(n log n)`. Taking and summing all suffixes visits at most `n` selected values in total. Thus the overall expected time complexity is `O(n log n)`, matching the manifest. If every element shares a limit, this worst case is reached; many small groups can make the actual sorting work lower.

The group lists collectively store every value once, requiring `O(n)` space. Python sorting is performed in place on each list, though the `vs[-lim:]` slice creates a temporary copy of the selected suffix. The total retained dictionary storage and the largest possible slice are both `O(n)`, so peak auxiliary space remains `O(n)`.

The source does not store or simulate the eventual activation sequence. Doing so could add `O(n)` output or bookkeeping, but it is unnecessary for the requested maximum.

## Alternatives and edge cases

- **Min-heap of size `lim` per group:** Instead of sorting a whole group, maintain its largest `lim` values in a min-heap. This can reduce work when `lim` is much smaller than the group size, at the cost of more involved grouping logic; the worst-case bound remains `O(n log n)`.
- **Selection algorithm:** A linear-time order statistic could partition each group around its largest `min(m, L)` values, giving expected linear total selection time, but sorting is simpler and the constraints permit `O(n log n)`.
- **Simulate a concrete activation order:** Processing selected groups in increasing limit can construct a valid schedule, but simulation is unnecessary because only the maximum total is returned.
- **Globally take the largest values:** A value’s eligibility depends on how many values share its exact limit. Ignoring group caps may select too many from a small-limit group and produce an unattainable total.
- **Take the largest `lim` with no length check:** Python’s negative-start suffix conveniently returns the entire list when `lim` exceeds its size. In languages without this slicing behavior, use `min(len(vs), lim)` explicitly.
- **All values have limit one:** Only the single largest value can be activated; the first activation makes the active count one and permanently disables the whole group.
- **A group smaller than its limit:** Every value in that group can contribute. Positive values mean there is no reason to omit a permitted activation.
- **A group larger than its limit:** Exactly the largest `lim` values are useful; every smaller unchosen value can be exchanged out for a larger chosen value without affecting feasibility because their limits are identical.
- **Immediate deactivation:** An element still contributes even when its own activation causes it to become permanently inactive. Confusing “active at the end” with “was activated” would undercount the answer.
- **Previously inactive elements also disappear:** When a threshold is reached, unactivated elements with small enough limits become permanently unavailable. This is the mechanism behind the per-group upper bound.
- **Positive-value guarantee:** The source always takes the maximum permitted number from a group because all values are at least one. If negative values were allowed, it could be better to activate fewer, and the suffix sum would need to exclude non-positive choices.
- **Dictionary order:** The source may sum groups in any hash-table order because it computes a closed-form maximum, not the witness schedule used in the attainability argument.
- **Missing imports:** The stored source uses `List` and `defaultdict` without imports. A standalone file would need `from typing import List` and `from collections import defaultdict` unless the execution harness supplies them.
