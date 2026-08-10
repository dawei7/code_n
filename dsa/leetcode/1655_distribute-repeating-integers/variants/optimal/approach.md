## General

**Reduce individual integers to supplies of equal values**

A customer does not care which integer value they receive; they care that they receive exactly their requested number and that all integers in their own allocation are equal. Consequently, the positions and ordering of `nums` are irrelevant. What matters is how many copies exist of each distinct value.

`Counter(nums)` computes those frequencies. If a value appears seven times, it becomes one supply group with capacity seven. The list `arr = list(cnt.values())` keeps only these capacities because the actual integer labels never affect feasibility. Let `u = len(arr)` be the number of distinct values and `m = len(quantity)` be the number of customers. The constraints make `m <= 10`, which is the key reason a subset dynamic program is practical even though `nums` may contain up to $10^5$ elements.

One supply group may serve several customers: all of those customers can receive the same underlying integer value. What cannot happen is splitting one customer’s order across different values. Representing a group assignment as a subset of whole customers enforces exactly that rule.

**Represent customer subsets with bitmasks**

An `m`-bit mask represents a set of customers. Bit `j` is one precisely when customer `j` belongs to the set. Mask zero is the empty set, and mask `(1 << m) - 1` contains every customer.

Before running the main dynamic program, the source builds `s`, where `s[mask]` is the total quantity requested by the customers in `mask`. For each nonzero mask `i`, the inner loop finds its first set bit `j`. Removing that bit gives `i ^ (1 << j)`, whose subset sum has already been computed because it is numerically smaller. The recurrence

`s[i] = s[i ^ (1 << j)] + quantity[j]`

therefore adds exactly the one newly restored customer. The immediate `break` is important: only one set bit should be removed and added back. By induction from `s[0] = 0`, every subset sum is correct.

These precomputed sums let the main loop test in constant time whether one value frequency `x` can satisfy all customers in a chosen subset `k`. The condition is `s[k] <= x`. Equality is not required because unused copies of values are allowed. Each included customer still receives exactly their own `quantity[j]`; the inequality applies only to the shared supply capacity.

**The two-dimensional feasibility state**

The Boolean table `f` has `u` rows and `2^m` columns. The meaning of `f[i][j]` is:

> Using only value-frequency groups `arr[0]` through `arr[i]`, it is possible to satisfy exactly all customers whose bits are set in mask `j`.

Every `f[i][0]` is set to true because satisfying no customers is possible with any number of available groups: simply distribute nothing. All nonempty states begin false and become true only when the code constructs a valid allocation.

The algorithm considers the groups one row at a time. At row `i`, `x` is the number of copies in the current value group. For each nonempty target mask `j`, it first checks whether `i > 0` and `f[i - 1][j]` is already true. If so, earlier value groups can satisfy all customers in `j`, so the current group may remain unused. The state is copied as true, and `continue` avoids unnecessary subset enumeration.

**Assign a subset to the current value**

If the state cannot simply be inherited, the loop enumerates every nonempty submask `k` of `j` with

`k = (k - 1) & j`.

It begins at `k = j`. Subtracting one changes the low-order bit pattern, and intersecting with `j` removes any bits not present in `j`; repeating the operation visits every nonempty subset of `j` exactly once.

The interpretation is that every customer in `k` receives the current integer value. Their combined demand must fit, which is `ok2 = s[k] <= x`. The other customers, represented by `j ^ k`, must be satisfiable using only earlier groups. For rows after the first, this is checked by `f[i - 1][j ^ k]`.

The first row has no earlier table row. Instead of allocating a separate base row, the exact source uses `ok1 = j == k` when `i == 0`. If all target customers are assigned to the first group, then `j ^ k` is empty and needs no earlier supply. If `k` is only part of `j`, the remaining nonempty customers cannot be served without an earlier group, so that option must fail. This special condition is exactly equivalent to an imaginary base state in which only the empty mask is true.

When both `ok1` and `ok2` hold, the allocation for `j ^ k` and the allocation of `k` to the current value are disjoint in customers and in supply groups. Combining them is valid, so `f[i][j]` becomes true. The loop then breaks because feasibility is all that matters; finding additional allocations cannot improve a Boolean result.

**Why the dynamic program is correct**

Consider any state `f[i][j]`. A valid distribution using groups through `i` has exactly two possibilities regarding the current group. It either serves no customer in `j`, in which case the same mask must be feasible using earlier groups, or it serves some nonempty subset `k` of `j`. In the second case, those customers’ total demand cannot exceed `arr[i]`, and the complementary customers must be feasible with earlier groups. The transition checks every such subset, so it cannot miss a valid distribution.

In the other direction, every transition marked true corresponds to a real distribution. An inherited state simply leaves the current copies unused. A subset transition combines a previously feasible complementary set with enough equal copies of one new value for all customers in `k`. No customer appears on both sides because `k` and `j ^ k` are disjoint, and no value group is reused because the complement comes only from row `i - 1`.

Thus, by induction over the frequency groups, every table entry has exactly its stated meaning. The returned entry `f[-1][-1]` uses the last group row and the all-customers mask. It is true exactly when every customer can be satisfied.

## Complexity detail

Let `N = len(nums)`, `u` be the number of distinct values, and `m = len(quantity)`. Counting `nums` costs $O(N)$ expected time and $O(u)$ space.

There are $2^m$ subset masks. The source’s subset-sum construction searches for one set bit in each mask, taking $O(m2^m)$ time in the straightforward upper bound and $O(2^m)$ storage.

For one frequency group, the submask work across all target masks is $O(3^m)$. One way to see the factor three is to classify each customer as outside target mask `j`, inside `j` but outside assigned submask `k`, or inside `k`. Across all pairs `(j, k)` with `k` a submask of `j`, those three choices produce $3^m$ combinations. Over `u` groups, the main DP therefore costs $O(u3^m)$ time. Including preprocessing, the total is $O(N + m2^m + u3^m)$, commonly shortened to $O(N + u3^m)$ because the DP term dominates for relevant `m`.

The exact table contains `u2^m` Boolean entries, so this implementation uses $O(u2^m + u)$ auxiliary space, dominated by $O(u2^m)$. The package manifest’s $O(2^m + u)$ space is attainable with rolling rows, but the exact source retains every row and therefore has the larger bound.

## Alternatives and edge cases

- **Rolling one-dimensional DP:** Only row `i - 1` is needed to build row `i`, so two arrays of length $2^m$, or a carefully separated previous/current pair, reduce DP storage to $O(2^m)$ while preserving the $O(u3^m)$ transition time.
- **Backtracking by customer:** Sort demands from largest to smallest and try placing each customer into a frequency bucket. This can be effective with symmetry pruning, but its worst-case search is harder to bound and duplicate capacities can create many equivalent branches.
- **Sort both demands and capacities:** Greedy matching is not sufficient because one capacity can serve several customers, and choosing a small request for a particular group can prevent a necessary later combination. Subset DP keeps all meaningful groupings.
- **One customer:** The all-customer mask has one bit. The answer is true exactly when at least one frequency is at least that customer’s quantity.
- **Unused integers:** The capacity test uses `<=`, so a value group may have leftover copies. The contract does not require every element of `nums` to be distributed.
- **Unused distinct values:** The inheritance transition allows an entire frequency group to be skipped.
- **Several customers sharing a value:** A submask can contain multiple customer bits, and `s[k]` checks their combined demand against one frequency.
- **A customer cannot mix values:** Each customer bit is assigned as a whole to exactly one chosen submask transition. The state never divides `quantity[j]` across groups.
- **Demand larger than every frequency:** No submask containing that customer can fit any group, so the all-customers state correctly remains false.
- **Duplicate quantity values:** Customers remain distinct bit positions even when they request the same amount. This may create symmetric masks, but it does not affect correctness.
- **All customers fit one frequency:** On any row whose capacity covers `s[all]`, choosing `k` equal to the full mask immediately establishes the final state.
- **First frequency row:** The special `j == k` condition prevents the code from pretending that a nonempty complement was handled by nonexistent earlier groups.
- **Nonempty input guarantee:** `nums` contains at least one item, so `arr` and the table have at least one row; consequently `f[-1][-1]` is well-defined.
