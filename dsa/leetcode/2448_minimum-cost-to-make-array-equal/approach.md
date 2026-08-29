## General

**Express the cost of choosing one common value**

If every element is changed to a target value $x$, element `i` moves by `abs(nums[i]-x)` unit steps. Each step costs `cost[i]`, so the total objective is

$$
F(x)=\sum_i \texttt{cost}[i]\,
\lvert\texttt{nums}[i]-x\rvert.
$$

This is a weighted absolute-distance function. The exact solution sorts value-weight pairs and evaluates this function efficiently at every input value.

**Why an input value is enough**

Between two consecutive sorted values, every absolute-value term is linear, so their weighted sum is also linear. A linear function on such an interval reaches its minimum at an endpoint unless it is flat, in which case every point, including both endpoints, is optimal. Therefore at least one optimal target equals some value already present in `nums`.

This is closely related to the weighted median: an optimum occurs where neither the total weight strictly to the left nor the total weight strictly to the right exceeds half the overall weight. The source does not explicitly select one weighted median. Instead, it computes the cost for every sorted input value and takes the minimum, which necessarily finds an optimum.

**Keep values attached to their weights**

`arr = sorted(zip(nums, cost))` creates pairs `(value, weight)` and sorts primarily by value. Keeping the pair together is essential because `cost[i]` belongs to the corresponding `nums[i]`.

The arrays `f` and `g` have length `n+1` and use a leading zero:

- `g[i]` is the total weight of the first `i` sorted pairs.
- `f[i]` is the sum of `value * weight` for those pairs.

For pair `a,b = arr[i-1]`, the updates are

`f[i] = f[i-1] + a*b`

and

`g[i] = g[i-1] + b`.

The leading zero lets formulas for an empty left side work without special cases.

**Cost of moving values on the left upward**

When candidate target `a` is the value at sorted position `i-1`, every earlier value is at most `a`. Its contribution is `(a-value)*weight`. Summing gives

$$
\begin{aligned}
L
&=
\sum_{j<i-1}(a-\texttt{value}_j)\texttt{weight}_j \\
&=
a\sum_{j<i-1}\texttt{weight}_j
-\sum_{j<i-1}\texttt{value}_j\texttt{weight}_j \\
&=
a\cdot g[i-1]-f[i-1].
\end{aligned}
$$

This is the source's `l` formula.

**Cost of moving values on the right downward**

Every later value is at least `a` and contributes `(value-a)*weight`. Prefix totals let the code obtain suffix totals by subtraction:

$$
R =
(f[n]-f[i])
-a\cdot(g[n]-g[i]).
$$

The current pair itself is excluded from both sides and has zero movement cost. Equal-valued pairs placed on either side also contribute zero through the formulas.

The method minimizes `l+r` across all sorted positions. It initializes `ans=inf` so the first finite candidate always replaces it.

**Trace the sample**

For `nums=[1,3,5,2]` and `cost=[2,3,1,14]`, sorting yields pairs `(1,2),(2,14),(3,3),(5,1)`. Choosing target 2 costs:

- $1$ upward step for value 1 with weight 2, costing 2;
- $1$ downward step for value 3 with weight 3, costing 3;
- $3$ downward steps for value 5 with weight 1, costing 3;
- zero for value 2.

The total is 8. The prefix formulas compute these group totals without looping over all elements again for each target.

**Why the minimum returned is globally correct**

For every candidate input value, the left and right formulas algebraically equal its full operation cost. At least one global minimizer is an input value because the objective is piecewise linear with breakpoints at those values. The loop checks every breakpoint, so the smallest computed total equals the global minimum.

## Complexity detail

Let $n$ be the array length. Creating and sorting the pairs takes $O(n\log n)$ time. Building prefix arrays takes $O(n)$, and evaluating all candidates takes another $O(n)$. Total time is $O(n\log n)$.

The sorted pair list, `f`, and `g` each use $O(n)$ space. Scalar totals use $O(1)$ additional storage, so auxiliary space is $O(n)$.

Products such as `nums[i]*cost[i]` and total costs can be large. Python integers are unbounded. Other languages should use a sufficiently wide integer type; the contract notes that the final result is at most $2^{53}-1$, but intermediate weighted sums should still be treated carefully.

## Alternatives and edge cases

- **Select a weighted median directly:** Sort pairs, find the first value where cumulative weight reaches at least half the total, and evaluate its cost in one pass. It has the same $O(n\log n)$ time with potentially less prefix storage.
- **Convex binary search:** Compare costs or slopes at neighboring integer targets to locate the minimum. It can work because the objective is convex, but sorting and weighted-median reasoning are more direct.
- **Try every integer target:** The value range reaches $10^6$, and recomputing cost for each target would be unnecessarily expensive.
- **All values already equal:** Every candidate equal to that value has zero cost, so the result is zero.
- **One element:** Its own value is an optimal target with zero operations.
- **Duplicate values:** Sorting keeps all weights, and their movement contributions remain zero when that shared value is chosen.
- **Very large weight:** It can pull the weighted median toward its value; treating the problem as an unweighted median would be wrong.
- **Target outside the input range:** Moving it inward toward the nearest input value cannot increase any weighted absolute distance, so it is never uniquely better.
- **Flat optimum interval:** If left and right total weights balance, several integer targets can tie. Evaluating the interval's input endpoints still finds the minimum.
- **Input preservation:** `sorted(zip(...))` creates a new list and does not reorder `nums` or `cost`.
