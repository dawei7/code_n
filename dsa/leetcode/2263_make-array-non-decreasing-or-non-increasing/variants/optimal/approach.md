## General

**Express operation count as distance**

Changing a value `x` into a target value `y` requires exactly `|x - y|` operations: increment `x` when it is too small or decrement it when it is too large. Once a complete target array `y` is chosen, its total conversion cost is therefore

$$
\sum_{i=0}^{n-1} \lvert \texttt{nums}[i] - y_i \rvert.
$$

The target is legal if it is non-decreasing or non-increasing. The solution first finds the cheapest non-decreasing target through dynamic programming. It then reverses the input and performs the same computation to cover non-increasing targets.

**Why target values zero through 1000 are sufficient**

Every input value lies between zero and 1000. There is always an optimal target whose values remain in that interval. If a proposed target contains values below zero, replacing each such value by zero cannot increase its distance from any nonnegative input value. Similarly, replacing values above 1000 by 1000 cannot increase distance from inputs no greater than 1000.

Clamping every target value through the same non-decreasing clamp function also preserves its order. Therefore, no optimum is lost by considering only the 1,001 integer target values zero through 1000. This finite value domain makes the table-based dynamic program possible.

**Define the dynamic-programming state**

Inside `solve(nums)`, `f[i][j]` is the minimum cost to transform the first `i` input elements into a non-decreasing sequence whose `i`th, or latest, target value is exactly `j`. Here `i` ranges from one through `n` and `j` ranges from zero through 1000.

The extra row `f[0]` represents an empty prefix. It is initialized to zero for every `j`. One can interpret this as allowing the imaginary value before the sequence to be any permissible value at no cost. For the first real element, taking a minimum over this all-zero row correctly leaves only the cost of choosing its target.

**Derive the transition**

Suppose the current input value is `x = nums[i - 1]` and the chosen current target is `j`. For the transformed prefix to be non-decreasing, the previous target value `v` must satisfy `v \le j`. The best earlier prefix compatible with `j` therefore costs

$$
\min_{0 \le v \le j} f[i-1][v].
$$

Changing the current `x` to `j` adds `|x-j|` operations. The full transition is

$$
f[i][j]
=
\min_{0 \le v \le j} f[i-1][v]
+
\lvert x-j\rvert.
$$

This considers every legal final step into state `(i,j)`. It excludes every decreasing step because values `v > j` are absent from the minimum.

**Compute every prefix minimum in one sweep**

Calculating the minimum over `f[i - 1][0:j + 1]` separately for every `j` would add another factor of the value-domain size. The variable `mi` avoids that repetition.

At the start of each input row, `mi` is infinity. The loop visits target values `j` in increasing order. Before setting `f[i][j]`, it compares `mi` with `f[i - 1][j]`. At that moment,

$$
\texttt{mi} = \min_{0 \le v \le j} f[i-1][v].
$$

The assignment `f[i][j] = mi + abs(x - j)` is therefore exactly the recurrence above. As `j` advances, the eligible previous-target range expands by one value, so one comparison is enough to maintain its minimum.

The strict condition `if mi > f[i - 1][j]` and an unconditional `min` would produce the same numeric state. When the values tie, leaving `mi` unchanged is harmless because only the cost is needed, not which predecessor achieved it.

**Finish the non-decreasing computation**

The last value of the transformed array may be any integer from zero through 1000. Therefore, the answer for one orientation is `min(f[n])` rather than one particular table entry.

Every table state is attainable by some transformed prefix and stores the least cost among all such prefixes. This follows by induction: the empty row has cost zero, and the transition combines the optimal compatible previous state with the exact current conversion cost. Conversely, every non-decreasing transformed prefix ending at `j` has some previous value `v \le j`, so its cost is among the options minimized by the recurrence. Thus, `solve` returns precisely the minimum cost for a non-decreasing target.

**Turn non-increasing into non-decreasing by reversal**

If a target sequence satisfies

$$
y_0 \ge y_1 \ge \cdots \ge y_{n-1},
$$

then reading it backward produces

$$
y_{n-1} \le y_{n-2} \le \cdots \le y_0,
$$

which is non-decreasing. Reversing `nums` at the same time preserves the element-to-target pairings and therefore preserves the total absolute-difference cost.

Consequently, `solve(nums[::-1])` is the minimum cost of making the original array non-increasing. It is not merely another estimate: reversal gives a cost-preserving one-to-one correspondence between original non-increasing targets and reversed non-decreasing targets.

The final expression takes the minimum of `solve(nums)` and `solve(nums[::-1])` because the problem accepts either orientation.

**A compact example of the two orientations**

For `nums = [3, 2]`, forcing non-decreasing order requires at least one operation, such as changing it to `[2, 2]` or `[3, 3]`. However, the original array is already non-increasing.

The first `solve` call obtains cost one. The reversed input is `[2, 3]`, which is already non-decreasing, so the second call obtains zero. Taking their minimum returns zero, exactly matching the “non-decreasing or non-increasing” requirement.

For an already non-decreasing array such as `[2, 2, 3, 4]`, the states that choose each original value form a legal path through the table with total cost zero. Since costs cannot be negative, the first call returns zero immediately as the global optimum.

**What the exact implementation differs from**

The branch summary mentions max-heap isotonic regression and `O(n \log n)` time. The executable Optimal source shown here does not use a heap or sign reversal. It allocates a full `(n + 1)` by 1,001 DP table and uses array reversal for the opposite orientation. Its correctness comes from the bounded-value recurrence, and its resource costs must be stated for that actual code.

## Complexity detail

Let `n` be the array length and let `V = 1001` be the number of allowed target values. One call to `solve` fills `nV` states. Each state uses one comparison, one absolute difference, and one addition, so one call takes `O(nV)` time. The function is called twice, which changes only the constant factor. Total time is

$$
O(nV) = O(1001n).
$$

Because 1,001 is fixed by the source constraints, this is linear in `n` under this particular bounded domain. It is not the `O(n \log n)` heap algorithm described by the manifest summary; if the numeric range were a variable, the accurate parameterized bound would remain `O(nV)`.

The table stores `(n + 1)V` integers, so one `solve` call uses `O(nV)` auxiliary space. The first table becomes unreachable before the second call is evaluated to completion under Python's evaluation of the two arguments to `min`, although memory reclamation timing is implementation-dependent; asymptotically, peak DP storage remains `O(nV)`. The reversed slice `nums[::-1]` additionally uses `O(n)` space, which is dominated by the table.

The existing table keeps all rows even though each row depends only on the preceding row. Thus, `O(nV)` is the exact source's space bound, not `O(V)`.

## Alternatives and edge cases

- **Max-heap L1 isotonic regression:** A heap-based method can compute a monotone absolute-error adjustment in `O(n \log n)` time and `O(n)` space. It satisfies the follow-up more directly, but it is not what this exact solution executes.
- **Rolling two DP rows:** Since row `i` depends only on row `i - 1`, the same recurrence can reduce auxiliary space from `O(nV)` to `O(V)` without changing `O(nV)` time.
- **Recompute each prefix minimum:** Taking `min(f[i - 1][:j + 1])` independently for every state is correct but raises time to `O(nV^2)`.
- **Enumerate all target arrays:** There are exponentially many length-`n` monotone choices if generated naively; the DP merges prefixes sharing the same final target.
- **Negate values for the opposite direction:** With a suitable transformed value domain, negation can turn non-increasing into non-decreasing. The exact code uses reversal, which preserves the zero-to-1000 domain unchanged.
- **Already non-decreasing:** Choosing every original value yields a zero-cost path, so the first `solve` call returns zero.
- **Already non-increasing:** Reversing the input makes it non-decreasing, so the second `solve` call returns zero.
- **All values equal:** Both orientations have cost zero.
- **Single element:** Any one-element sequence is both non-decreasing and non-increasing; the DP can choose the original value and returns zero.
- **Values at zero or 1000:** Both boundaries are included in `range(1001)`, so no legal input value is omitted.
- **Targets outside the input range:** Clamping to zero through 1000 preserves monotonicity and cannot increase cost, proving the bounded table is sufficient.
- **Ties in the transformed sequence:** Non-decreasing and non-increasing both permit equality. The transition uses `v \le j`, not the strict relation `v < j`.
- **Unit-operation interpretation:** The absolute difference is exact because each operation changes one selected value by exactly one.
- **Choice between orientations:** Costs must be computed independently and minimized; deciding from the first or last input values alone is not sufficient.
- **Full last-row minimum:** Requiring a particular ending value would exclude valid optima, so `min(f[n])` is essential.
- **Input preservation:** The first call reads `nums`, and slicing creates a separate reversed list for the second; the original list is not changed.
- **Large table:** With the stated maxima, the table has roughly one million entries. This is why the fixed domain matters and why rolling-row optimization would materially reduce memory.
