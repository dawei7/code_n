## General

**View the increments as choosing a final array**

An operation increases one element by one. Instead of deciding on individual increments one at a time, imagine choosing the final value of every element. If the original value at index `i` is `nums[i]` and its chosen final value is `y_i`, then that position costs exactly

$$
y_i-\texttt{nums}[i],
$$

because decreases are forbidden and each unit increase costs one operation.

The first element cannot be changed, so

$$
y_0=\texttt{nums}[0].
$$

For every later position, the beauty condition requires its finalized value to be divisible by the preceding finalized value:

$$
y_i \bmod y_{i-1}=0.
$$

Thus the task is to choose a chain of nondecreasing multiples, starting at the fixed first value, whose total increase is minimum. The choice at one index affects which values are legal at the next, so a locally cheapest increment is not always enough. Dynamic programming retains the best cost for each possible finalized last value.

**The dynamic-programming state**

After some prefix has been processed, the dictionary `f` maps

`pre -> minimum cost for a valid finalized prefix ending with value pre`.

Only the last finalized value is needed. All earlier divisibility conditions have already been satisfied and their costs are included in the stored total. For the next original number, future legality depends on the prefix only through `pre`, because the next final value merely has to be a multiple of it.

The initialization is `f = {nums[0]: 0}`. This exactly expresses the first-element rule: there is one possible finalized first value, it equals the original first element, and changing nothing costs zero.

**Generate every legal next value**

Suppose the next original value is `x` and the previous finalized value is `pre`. A legal current finalized value `cur` must satisfy two conditions:

1. `cur >= x`, because the operation can only increase `x`.
2. `cur` is a multiple of `pre`, so the adjacent divisibility condition holds.

The smallest such multiple is

`(x + pre - 1) // pre * pre`.

The integer expression `(x + pre - 1) // pre` computes $\lceil x/\texttt{pre}\rceil$ without floating-point arithmetic. Multiplying by `pre` gives the first multiple at least `x`. Every other legal choice is found by repeatedly adding `pre`.

For each state `pre` with accumulated cost `s`, the inner loop considers this smallest multiple and then all later multiples through 100. Choosing `cur` adds `cur - x` operations, so the candidate total is

`s + cur - x`.

Several different previous values may reach the same `cur`. The new dictionary `g` keeps only the smallest candidate for each `cur`. A more expensive prefix ending at the same value can be discarded safely: both prefixes offer exactly the same legal choices to all later positions, and the cheaper one will remain no worse after adding identical future costs.

Once all states in `f` have contributed transitions, `g` becomes the new `f`. Using a separate dictionary matters. Updating `f` in place could accidentally let the current input element participate in several transitions as though multiple array positions had been processed.

After the last input value, every entry of `f` represents a complete beautiful array. The ending value is not prescribed, so `min(f.values())` selects the least cost among all valid endings.

**Why considering values only through 100 is safe**

The input values are at most 50. Let

$$
M=50
\quad\text{and}\quad
V=2M=100.
$$

The code enumerates only finalized values at most `V`. A finite cap must be justified: it would be incorrect merely to assume that large values are unlikely.

First observe that finalized values never decrease. If `y_i` is divisible by the positive integer `y_{i-1}`, then `y_i` is at least `y_{i-1}`. More strongly, every value later in the chain is an integer multiple of every earlier one.

Assume for contradiction that an optimal final array has a value greater than 100. Let `i` be the first index with `y_i > 100`. This cannot be index zero because `y_0 = nums[0] <= 50`. Let `p = y_{i-1}`. By the choice of `i`, `p <= 100`, and because `y_i` is a multiple of `p`, write

$$
y_i=q p
$$

for an integer `q`. Since `y_i > p`, `q >= 2`.

Now reduce the base of the entire suffix by one copy of `p`:

$$
y_i' = y_i-p=(q-1)p.
$$

Because `q >= 2`, `p <= y_i/2`, which gives

$$
y_i' = y_i-p \ge \frac{y_i}{2} > 50.
$$

Therefore `y_i'` is still greater than every possible original input value, so it remains reachable using increments only.

Every later finalized value can be written as `y_j=t_j y_i` for some positive integer `t_j`, because the divisibility chain makes it a multiple of `y_i`. Replace it with

$$
y_j'=t_j y_i'.
$$

All adjacent divisibility ratios are preserved: if `y_{j+1}=r y_j`, then `y_{j+1}'=r y_j'`. Every replacement is at least `y_i' > 50 >= nums[j]`, so no position is decreased below its original value. Yet every value in this suffix becomes strictly smaller, which strictly lowers the total number of increments. That contradicts the assumption that the original array was optimal.

Hence at least one optimal solution has every finalized value at most 100. The cap used by the code cannot exclude the true minimum.

**Why transitions never get stuck under the cap**

For any reachable `pre <= 100` and next input `x <= 50`, there is a legal multiple at most 100. If `pre >= x`, choosing `cur = pre` works. If `pre < x`, the smallest multiple at least `x` is less than `x + pre`, which is at most 99 because both are at most 50 and `pre < x`. Thus `g` remains nonempty throughout every valid input.

Combining the state meaning, exhaustive multiple enumeration, minimum-cost merging, and proven cap shows that the returned minimum is the global optimum.

## Complexity detail

Let `n` be the array length and let `V = 100` be the final-value cap. There are at most `V` dictionary states because a key is an integer from one through `V`.

For a previous value `pre`, the transition loop visits at most $\lfloor V/\texttt{pre}\rfloor$ multiples. Summing this over every possible previous key gives

$$
\sum_{p=1}^{V}\left\lfloor\frac{V}{p}\right\rfloor
= O(V\log V),
$$

the harmonic-series bound. Each candidate performs expected constant-time dictionary work. Across the `n - 1` later elements, the expected time complexity is $O(nV\log V)$.

The dictionaries `f` and `g` each contain at most `V` entries. They coexist during one layer transition but only by a constant factor, so the auxiliary space complexity is $O(V)$. For this problem `V=100` is numerically constant, but retaining `V` in the bound explains how the implementation's state space and transition enumeration behave.

## Alternatives and edge cases

- **Greedily choose the smallest legal multiple:** This minimizes the current position's immediate increase, but a slightly larger current value can change which later values are reachable and alter future cost. Dynamic programming compares all relevant endings instead of committing before those consequences are known.
- **Unbounded dynamic programming:** Enumerating arbitrary larger multiples would never terminate without an imposed range. The $2M$ argument proves that values above 100 cannot be necessary for an optimum, turning the idea into a finite exact algorithm.
- **Search every sequence recursively:** Branching over all multiples at every index repeats the same suffix problem whenever branches reach the same finalized last value. The map merges precisely those equivalent subproblems by retaining their cheapest prefix.
- **Shortest-path interpretation:** Each layer is an index, each node is a possible finalized value, and a transition edge has weight `cur - x`. A layered shortest-path computation is equivalent to this DP, but the two dictionaries express it more directly.
- **Modify `f` in place:** Newly created states would then be available while processing the same `x` and could represent applying multiple transitions to one element. Building `g` keeps each DP layer tied to exactly one array position.
- **First element greater than later inputs:** The later element may be raised directly to `pre`, which is divisible by itself. The ceiling-multiple formula returns `pre` and charges the correct increase.
- **An element already divisible by `pre`:** The ceiling formula returns `x` itself, so that transition adds zero operations.
- **Array of length one:** No adjacency condition exists. The loop over `nums[1:]` is empty, and the minimum stored cost is zero.
- **Repeated predecessor routes to one `cur`:** Only the least total cost is retained. Discarded routes cannot become better later because future transitions depend on `cur`, not on the earlier route.
- **Large finalized values propagating through the suffix:** The cap proof reduces the entire suffix together, not only the first oversized value. This simultaneous scaling is necessary to preserve every later divisibility relation.
- **Positive-value assumption:** The ceiling calculation and divisibility chain rely on `pre > 0`. The problem guarantees positive input values, so division by zero and zero-multiple ambiguity cannot occur.
- **Dictionary operation cost:** The stated running time uses expected $O(1)$ Python hash-table operations. The number of mathematical states and transitions is bounded independently of hash-table ordering.
