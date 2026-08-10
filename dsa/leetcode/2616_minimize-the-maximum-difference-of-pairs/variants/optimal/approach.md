## General

**Turn an optimization problem into a yes-or-no question**

The answer is not the sum of pair differences. It is the largest difference among the chosen $p$ pairs, and that largest value must be as small as possible.

Instead of trying to construct the optimal pairs immediately, choose a candidate threshold $D$ and ask:

> Can we form at least $p$ disjoint pairs whose individual differences are all at most $D$?

This feasibility question is easier than the original minimization. More importantly, it is monotone:

- if threshold $D$ works, every larger threshold also works because the same pairs remain valid;
- if threshold $D$ fails, every smaller threshold also fails because it allows no additional pair.

Therefore, feasibility changes only once, from false to true. The first true threshold is exactly the minimum possible maximum difference.

**Why sorting reveals the useful pairs**

The solution sorts `nums` in nondecreasing order. After sorting, values that are close numerically become close in position.

For a fixed threshold, suppose the smallest still-unused value at index $i$ can participate in a valid pair at all. If some later value `nums[j]` with $j>i$ is close enough, then its immediate neighbor `nums[i + 1]` is no farther away:

$$
\texttt{nums[i+1]}-\texttt{nums[i]}
\le
\texttt{nums[j]}-\texttt{nums[i]}.
$$

So whenever the leftmost value can be paired, pairing it with the next value is safe. There is no reason to skip the nearer neighbor in favor of a farther one.

Sorting changes the array in place. Original indices are irrelevant because the output is only the optimal difference, and the constraint merely says that each occurrence may be used once. Equal values at different original indices remain distinct sortable elements.

**Greedily count the maximum number of threshold-valid pairs**

The helper `check(diff)` scans the sorted array from left to right with pointer `i` and counter `cnt`.

- If `nums[i + 1] - nums[i] <= diff`, it pairs these adjacent values, increments `cnt`, and advances by two so neither occurrence can be reused.
- Otherwise it advances by one, permanently leaving `nums[i]` unused.

At the end, feasibility is `cnt >= p`.

The scan does not need to remember the actual pairs. Only their count matters for deciding whether the current threshold is sufficient.

**Why taking the first possible adjacent pair is optimal**

Consider the leftmost still-unprocessed value $a=\texttt{nums[i]}$.

If $a$ and the next value $b=\texttt{nums[i+1]}$ differ by more than the threshold, then $a$ cannot pair with any later value: all later values are at least $b$, so their differences from $a$ are no smaller. Discarding $a$ is forced.

If $a$ and $b$ do form a valid pair, take any solution that obtains the maximum possible number of pairs from the remaining suffix.

- If that solution already pairs $a$ with $b$, it agrees with the greedy choice.
- If it pairs $a$ with a later value $x$, replace $(a,x)$ with $(a,b)$. The replacement remains valid and frees $x$.
- If it pairs $b$ with a later value $x$ while leaving $a$ unused, replace $(b,x)$ with $(a,b)$.
- If it uses both $a$ and $b$ in two different pairs, say $(a,x)$ and $(b,y)$ with the later endpoints ordered appropriately, using $(a,b)$ leaves the later values available to preserve at least as many choices in the suffix; the standard exchange can align the greedy first pair without reducing the achievable count.

Thus some maximum-cardinality pairing begins with the greedy pair whenever it is available. Removing those two elements reduces the problem to the same question on the remaining suffix. Repeating this argument proves that `check` returns the maximum number of valid disjoint pairs for the threshold.

**Binary-search the first feasible threshold**

After sorting, no pair difference can be negative, so zero is the smallest candidate. The largest necessary candidate is

$$
R=\texttt{nums[-1]}-\texttt{nums[0]}.
$$

At threshold $R$, every adjacent pair is valid, and the constraint $p\le\lfloor n/2\rfloor$ guarantees enough disjoint pairs. Hence the search range always contains a feasible answer.

The code uses

`bisect_left(range(R + 1), True, key=check)`.

Conceptually, applying `check` to thresholds $0,1,\ldots,R$ produces a sorted Boolean sequence:

$$
\text{false},\ldots,\text{false},\text{true},\ldots,\text{true}.
$$

`bisect_left` returns the index of the first `True`. Because the virtual range value equals its index, that returned index is also the smallest feasible threshold.

The range is lazy in Python; it does not allocate all values through $R$, which may be as large as $10^9$.

**Why the returned threshold is the desired optimum**

Let $D^\star$ be the returned first feasible threshold. `check(D^\star)` constructs at least $p$ valid disjoint pairs, so an assignment with maximum difference at most $D^\star$ exists.

Every smaller threshold is infeasible by the definition of the first true position. Therefore no collection of $p$ pairs can have maximum difference below $D^\star$. Together these statements prove that $D^\star$ is exactly the minimum possible maximum difference.

When $p=0$, every threshold is feasible because zero pairs are already enough. The first feasible value is zero, matching the definition that the maximum of the empty set is zero.

**Trace a representative input**

For `nums = [10,1,2,7,1,3]`, sorting gives `[1,1,2,3,7,10]`.

At threshold zero, only the first two ones pair, so the count is one and $p=2$ is not reached. At threshold one, the scan pairs the two ones, then pairs two and three, reaching two pairs. Therefore one is the first feasible threshold.

## Complexity detail

Let $n$ be the array length and

$$
D=\max(\texttt{nums})-\min(\texttt{nums}).
$$

Sorting costs $O(n\log n)$. Binary search examines $O(\log(D+1))$ thresholds, and every call to `check` performs one linear scan in $O(n)$ time. Total time is

$$
O(n\log n+n\log(D+1)).
$$

Python's list sort may use $O(n)$ temporary memory, which matches the manifest. Outside sorting, the feasibility scan and binary search use $O(1)$ auxiliary state. The input list is mutated by sorting.

## Alternatives and edge cases

- **Dynamic programming for each threshold:** A prefix DP can count pairs, but the greedy exchange proof makes a table unnecessary.
- **Enumerate every threshold:** Testing $0,1,2,\ldots$ is correct but may require up to $10^9$ scans.
- **Pair original neighbors:** Numerical closeness, not original adjacency, determines difference; sorting is essential.
- **`p = 0`:** No pair is required, so the first feasible threshold is zero.
- **Duplicate values:** They create difference-zero pairs and are handled as separate occurrences.
- **Odd array length:** At most one occurrence remains unused; the greedy scan naturally allows this.
- **Threshold too small for the first value:** If its adjacent gap is too large, no later partner can work, so skipping it is safe.
- **Maximum allowed `p`:** When $p=\lfloor n/2\rfloor$, the feasibility scan must pair almost or all values without reuse.
- **Large value range:** The lazy `range` and logarithmic search avoid memory or time proportional to the numeric range.
- **Input mutation:** `nums.sort()` changes caller-visible order; copy before sorting if preservation were required.
