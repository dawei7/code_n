## General

The pairwise condition initially looks expensive because every chosen number must be comparable by divisibility with every other chosen number. Sorting reveals a much simpler chain structure. Once the distinct positive values are ascending, an earlier value can precede a later value exactly when the later value is divisible by the earlier one.

The exact solution computes the length of the longest divisible chain ending at every sorted position. It then reconstructs one maximum chain by scanning backward through those lengths. It does not store an explicit predecessor index for every position.

**Why sorting is the essential first step.**

For two distinct positive integers in ascending order, `small < large`. The smaller cannot be divisible by the larger, so the pair is compatible exactly when

$$
\texttt{large}\bmod\texttt{small}=0.
$$

Sorting gives every valid subset a consistent direction from smaller to larger. More importantly, divisibility is transitive: if $a$ divides $b$ and $b$ divides $c$, then $a$ divides $c$. Therefore it is enough to build a chain in which every new number is divisible by the chain's current largest number. All earlier chain elements then divide the new number automatically.

The call `nums.sort()` modifies the input list in place. This supplies the order needed by both dynamic programming and reconstruction.

**Meaning of `f[i]`.**

`f[i]` is the maximum length of a divisible subset whose largest and final value is `nums[i]`. Every single value is a valid subset by itself, so all entries begin at one.

For a fixed ending index `i`, the inner loop considers every earlier index `j`. When `nums[i] % nums[j] == 0`, any valid chain ending at `nums[j]` can be extended with `nums[i]`. Its new length is `f[j] + 1`, so the update is

```text
f[i] = max(f[i], f[j] + 1).
```

If divisibility fails, `nums[j]` cannot be the immediate previous largest element of a chain ending at `nums[i]`, so that state is ignored.

**Why extending only the previous largest value is sufficient.**

Suppose the chain ending at `nums[j]` is

$$
a_1\mid a_2\mid\cdots\mid a_t=\texttt{nums}[j],
$$

where the vertical bar means “divides.” If `nums[j]` divides `nums[i]`, transitivity implies every $a_p$ also divides `nums[i]`. The extended values remain pairwise compatible.

Conversely, take any valid subset ending at `nums[i]` and remove that largest value. If elements remain, their largest member occurs at some earlier index `j`, divides `nums[i]`, and the remaining subset has length at most `f[j]`. The recurrence considers this `j`. Thus it cannot miss a better chain.

**Tracking where a global optimum ends.**

Variable `k` stores an index whose `f` value is the greatest seen so far. After finishing each `i`, the source updates `k` only when `f[i]` is strictly greater than `f[k]`.

When multiple maximum subsets exist, keeping the earlier one is fine because the contract accepts any optimum. At the end, `f[k]` is the largest DP length and `nums[k]` can serve as the largest value of one maximum divisible subset.

**A DP trace for `[1, 2, 4, 8]`.**

After sorting, the order is unchanged.

- `1` starts a length-one chain, so `f[0] = 1`.
- `2` is divisible by `1`, giving `f[1] = 2`.
- `4` can extend the chain ending at `2`, giving `f[2] = 3`.
- `8` can extend the chain ending at `4`, giving `f[3] = 4`.

The maximum endpoint is `8`, and reconstruction recovers `8`, `4`, `2`, and `1` in descending order.

**Reconstruction without predecessor pointers.**

The source sets `m = f[k]`, initializes scan index `i = k`, and starts with an empty answer. Here `m` is the DP length that the next reconstructed element must have, while `nums[k]` is the most recently chosen chain value.

The first scan position is the maximum endpoint itself. It satisfies `nums[k] % nums[i] == 0` because every positive integer divides itself, and `f[i] == m`, so it is appended.

After choosing a value, the assignment `k, m = i, m - 1` makes that value the new divisibility ceiling and asks for a predecessor whose chain length is exactly one smaller. The scan continues backward with `i -= 1`.

An index is chosen only when both conditions hold:

- `nums[k] % nums[i] == 0`, so the candidate divides the already chosen next-larger value.
- `f[i] == m`, so it occupies the preceding DP level of an optimal chain.

The DP recurrence guarantees such a predecessor exists whenever `m` is positive. If the current chosen value has DP length $m+1$, that value obtained its length by extending at least one divisible earlier state of length $m$. The backward scan eventually reaches one.

**Why one backward scan is enough.**

The reconstruction never resets `i`; it moves from the maximum endpoint toward zero once. Positions rejected for one predecessor level are earlier than the chosen endpoint but may still be examined as the scan continues. Once a predecessor is chosen at index `i`, all remaining predecessors must occur before it because values were sorted and DP transitions only move forward.

Therefore reconstruction is linear, not another quadratic pass. The returned list is in descending numerical order because it begins at the largest chain value and walks backward. The problem asks for a subset, not ascending order, so this is valid.

**Why the reconstructed values satisfy every pair.**

Each newly appended smaller value divides the previously appended larger value. By transitivity, it also divides every still larger value already in `ans`. The `f` levels decrease from the global maximum to one, so exactly the optimal number of values is chosen. The result is therefore pairwise divisible and maximum in size.

For `[1,2,3]`, both `[1,2]` and `[1,3]` have length two. The strict endpoint update and scan order select one of them; either meets the contract.

## Complexity detail

Let $n$ be the number of input values. Sorting takes $O(n\log n)$ time. The nested DP loops examine every pair with $j<i$, performing $n(n-1)/2=O(n^2)$ divisibility checks. This dominates sorting. Reconstruction decrements `i` at most $n$ times, so it costs $O(n)$. Total time is $O(n^2)$.

The `f` array uses $O(n)$ auxiliary space. Reconstruction stores up to $n$ values in the returned `ans` list; including output, storage is also $O(n)$. Only constant additional scalar variables are used. This matches the manifest.

The input is sorted in place. Python's sorting implementation may use $O(n)$ temporary memory internally, which remains within the stated overall linear-space bound.

## Alternatives and edge cases

- **Explicit predecessor array:** Whenever `f[i]` improves through `j`, store `parent[i] = j`. Reconstruction then follows direct links. It remains $O(n^2)$ time and $O(n)$ space and can be easier to understand, while the source saves that extra array through backward scanning.

- **Store the whole best subset at every index:** This simplifies reconstruction but copying chains can require $O(n^2)$ space in the worst case.

- **Recursive memoization:** Compute the best chain ending at each index on demand. With memoization it has similar quadratic transition work but adds recursion overhead.

- **Single input value:** Its DP length remains one, it is selected immediately, and the result contains that value.

- **All values form a chain:** Every later value extends the preceding best length, and the answer contains all $n$ values.

- **No pair divides another:** Every `f[i]` stays one. Any single value is a maximum valid subset.

- **Value one:** One divides every positive integer, so it can begin every divisible chain when present.

- **Distinctness matters:** The contract excludes duplicates. If duplicates were allowed, equal values divide one another and would need an explicit decision about treating occurrences as separate subset elements.

- **Large values:** Modulo uses exact integer arithmetic. Values up to $2\cdot10^9$ do not affect the pair-count complexity.

- **Multiple optima:** Strict `f[k] < f[i]` keeps the first endpoint reaching a maximum length. The contract permits this arbitrary tie choice.

- **Output order:** The source returns largest to smallest. Divisibility-subset validity is order-independent, so no reversal is required.
