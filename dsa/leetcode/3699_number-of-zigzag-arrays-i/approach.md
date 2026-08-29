## General

Because adjacent values cannot be equal, every adjacent pair has one of two directions:

- **up:** the new value is greater than the previous value;
- **down:** the new value is smaller than the previous value.

Three consecutive values are strictly increasing exactly when their two adjacent directions are both up. They are strictly decreasing exactly when both directions are down. Therefore, a valid ZigZag array is precisely an array whose comparison directions alternate:

$$
\text{up},\text{down},\text{up},\ldots
$$

or:

$$
\text{down},\text{up},\text{down},\ldots
$$

The dynamic program records the final value and the final direction. Prefix and suffix sums make each transition linear over the value range rather than quadratic.

**Shifting the value range**

Let:

$$
m=r-l+1.
$$

The actual values $l,l+1,\ldots,r$ are represented by ranks $0,1,\ldots,m-1$. Subtracting the same $l$ from every value preserves all equality, less-than, and greater-than comparisons, so the count depends only on $m$, not on the absolute location of the interval.

The source calls this quantity `value_count`.

**State meaning**

For arrays of the current processed length:

- `ending_up[v]` counts valid arrays ending at rank `v` whose last adjacent comparison is up;
- `ending_down[v]` counts valid arrays ending at rank `v` whose last adjacent comparison is down.

Every valid array of length at least two has exactly one final direction and exactly one final rank, so it belongs to one state and is not double-counted.

**Initializing all length-two arrays**

The source initializes:

`ending_up = list(range(value_count))`

For final rank `v`, a length-two array ending with an up comparison must choose its previous rank from:

$$
0,1,\ldots,v-1.
$$

There are exactly $v$ choices, so `ending_up[v] = v`.

Similarly:

`ending_down = [value_count - value - 1 for value in range(value_count)]`

A down-ending pair with final rank `v` needs a previous rank greater than `v`. There are $m-v-1$ such ranks.

This initialization counts every valid length-two array once. The constraints have `n >= 3`, so there is no need for a separate length-one return path.

**Transitioning into an up-ending state**

To append new rank `v` with an up comparison, the preceding final rank `u` must satisfy:

$$
u<v.
$$

The previous array's final direction must be down; otherwise, the last three values would contain two consecutive up comparisons and form a strictly increasing triple.

Therefore:

$$
\textit{nextUp}[v]
=
\sum_{u=0}^{v-1}\textit{endingDown}[u].
$$

Computing this sum separately for every `v` would be quadratic in $m$. Instead, the source scans ranks from low to high while maintaining `prefix`.

Before adding `ending_down[v]` to `prefix`, the accumulator contains exactly the states for ranks below `v`. The assignment:

`next_up[value] = prefix`

therefore stores the required strict-less-than sum. Adding the current entry afterward ensures equal adjacent values are excluded.

**Transitioning into a down-ending state**

To append new rank `v` with a down comparison, the previous rank must satisfy:

$$
u>v,
$$

and the previous direction must be up. Thus:

$$
\textit{nextDown}[v]
=
\sum_{u=v+1}^{m-1}\textit{endingUp}[u].
$$

The source scans from high rank to low rank with a running `suffix`. It assigns `next_down[v]` before adding `ending_up[v]`, so the suffix contains only strictly larger ranks and again excludes equality.

**Advancing from length two to length $n$**

The loop:

`for _ in range(2, n):`

runs $n-2$ times. The state begins at length two. Each iteration appends one element, so after the last iteration it describes length $n$ arrays.

After computing both new vectors, the source replaces the old states:

`ending_up = next_up`

`ending_down = next_down`

Only the immediately preceding length is needed, which is why the DP uses rolling arrays.

**A complete count for three values**

Take ranks $0,1,2$, corresponding to any interval of size three.

For length two:

`ending_up = [0, 1, 2]`

`ending_down = [2, 1, 0]`.

For length three, prefix sums of `ending_down` give:

`next_up = [0, 2, 3]`.

Suffix sums of `ending_up` give:

`next_down = [3, 2, 0]`.

The total is:

$$
0+2+3+3+2+0=10,
$$

matching the ten arrays in the example for interval `[1,3]`.

**Why the transitions count exactly the valid arrays**

Take any valid array of the new length and remove its last element. The remaining prefix is a valid array represented by one old state. If the new final comparison is up, the previous final direction must be down and the previous rank is strictly smaller than the new rank, so the array appears in exactly one prefix-sum transition. The down case is symmetric.

Conversely, every transition appends a strictly different rank and reverses the previous comparison direction. It cannot create equal neighbors, an increasing triple, or a decreasing triple.

The last element and the shorter prefix uniquely determine the construction, so no array is counted twice.

**Modulo arithmetic**

The number of arrays grows exponentially with $n$. Each prefix and suffix accumulator is reduced modulo $10^9+7$ after adding one state. Addition respects modular arithmetic, so reducing intermediate totals preserves the requested final remainder.

The final sum of both vectors is reduced once more before returning.

## Complexity detail

Let $m=r-l+1$.

Initialization takes $O(m)$ time. Each of the $n-2$ iterations performs one forward scan and one backward scan over $m$ states, plus allocation of two length-$m$ arrays. Total time is:

$$
O(nm).
$$

At any point, the source stores the two current state vectors and two next vectors, each of length $m$. Prefix and suffix accumulators are scalars. Auxiliary space is $O(m)$.

The modulo keeps each stored count bounded even though the conceptual number of arrays is enormous.

## Alternatives and edge cases

- **Enumerate all arrays:** There are $m^n$ possible value sequences before filtering, which is infeasible.
- **Quadratic transition:** For each final rank, scanning every previous rank costs $O(nm^2)$. Prefix and suffix accumulation reduce this to $O(nm)$.
- **Track the last three values:** Future validity needs only the last rank and last comparison direction. A larger state wastes memory.
- **Start both directions with one at length one:** This can work with carefully designed transitions, but direction is not actually defined for one element. The exact source starts from the unambiguous length-two counts.
- **Two available values:** Adjacent inequality forces complete alternation between them. Exactly two arrays exist for every legal length.
- **Lowest final rank:** An up-ending state at rank zero is impossible because no smaller previous rank exists; `next_up[0]` remains zero.
- **Highest final rank:** A down-ending state at rank $m-1$ is impossible because no larger previous rank exists.
- **Strict inequality:** Prefix and suffix values are assigned before including the current rank, deliberately excluding equal adjacent values.
- **Absolute values `l` and `r`:** Only their interval size matters because translating all values preserves comparisons.
- **Final direction partition:** Summing both vectors is safe because every length-$n$ array has exactly one last comparison direction.
