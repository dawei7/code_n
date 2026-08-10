## General

The inverse weight of an integer cannot be known from its own depth alone. It also depends on the deepest integer anywhere in the structure:

$$
\operatorname{weight}(x)=\operatorname{maxDepth}-\operatorname{depth}(x)+1.
$$

A straightforward method would first traverse the nested structure to discover `maxDepth`, then traverse it again to compute the weighted sum. The exact solution performs only one depth-first traversal. It collects three global quantities and combines them algebraically after the deepest level is known.

**Separate the formula into reusable totals.**

Suppose the nested structure contains integer values $v_1,v_2,\ldots,v_r$ at depths $d_1,d_2,\ldots,d_r$, and let $D$ be the maximum integer depth. The requested answer is

$$
\sum_{p=1}^{r}v_p(D-d_p+1).
$$

Distribute each value and separate the sums:

$$
\begin{aligned}
\sum_{p=1}^{r}v_p(D-d_p+1)
&=\sum_{p=1}^{r}\left((D+1)v_p-v_pd_p\right)\\
&=(D+1)\sum_{p=1}^{r}v_p-\sum_{p=1}^{r}v_pd_p.
\end{aligned}
$$

The source names the first ordinary value sum `s` and the depth-weighted sum `ws`. Once traversal has also found `maxDepth`, it returns `(maxDepth + 1) * s - ws`.

This rearrangement is the key. `maxDepth` is needed only in the final formula, so it can be discovered during the same traversal that accumulates the other two totals.

**Meaning of depth in the recursive calls.**

The outer `nestedList` is the container supplied to the method. Each `NestedInteger` directly inside it has depth one, so the method calls `dfs(x, 1)` for every top-level element.

When `x` stores another list, each child is inside one additional list layer. The recursive call therefore uses `d + 1`. The code does not inspect the platform-provided representation directly; it uses `isInteger()`, `getInteger()`, and `getList()` according to the `NestedInteger` contract.

For `[1,[4,[6]]]`, integer `1` is visited at depth one, `4` at depth two, and `6` at depth three. Thus `s = 11`, `ws = 1*1 + 4*2 + 6*3 = 27`, and `maxDepth = 3`. The final expression gives `4*11 - 27 = 17`.

**What happens at an integer.**

When `x.isInteger()` is true, `x.getInteger()` supplies the stored value. The source performs two accumulations:

- `s += value` adds the integer to the unweighted total.
- `ws += value * d` adds its ordinary depth-weighted contribution.

No inverse weight is computed yet. That weight would require the final global maximum depth, which may be discovered in a different branch later.

Negative values require no special treatment. Both sums and the final algebra use ordinary signed arithmetic. For example, a negative shallow value receives a larger inverse weight and therefore contributes a more negative amount, exactly as the formula specifies.

**What happens at a nested list.**

When the object stores a list, it contributes no integer value by itself. The loop recursively visits each child at `d + 1`. The current path's call stack remembers how deeply nested those children are.

The function updates `maxDepth` before checking whether `x` is an integer, so list objects also temporarily participate in the maximum calculation. This remains correct under the explicit guarantee that there are no empty lists. Every visited list contains some descendant, and following nested lists eventually reaches an integer at a strictly greater depth. Therefore no list-only depth can exceed the deepest integer depth left after the complete traversal.

If empty lists were allowed, that ordering could overstate the maximum by counting a deep empty container that has no integer. The local Reference rules out exactly that case.

**Why `nonlocal` is used.**

`maxDepth`, `s`, and `ws` are created in the enclosing method. The nested `dfs` function updates the same three accumulators while exploring all branches. Declaring them `nonlocal` tells Python that assignments refer to those enclosing variables instead of creating new local variables inside each recursive call.

All top-level elements share these accumulators, so values from separate branches are combined into one global result. The visited structure itself is not modified.

**A trace of the first example.**

For `[[1,1],2,[1,1]]`, the four inner `1` values occur at depth two and the top-level `2` occurs at depth one. The traversal produces

$$
s=1+1+2+1+1=6
$$

and

$$
ws=1\cdot2+1\cdot2+2\cdot1+1\cdot2+1\cdot2=10.
$$

The deepest integer level is two, so the answer is `3 * 6 - 10 = 8`. Equivalently, the depth-two ones receive inverse weight one and the depth-one value `2` receives inverse weight two.

**Why the traversal and formula are correct.**

Every `NestedInteger` is visited through exactly one parent path. The depth begins at one and increases once per containing list, so every integer is recorded with its contract-defined depth. Consequently, `s` becomes the sum of all integer values, `ws` becomes the sum of each value times its ordinary depth, and `maxDepth` becomes the deepest integer level.

The algebraic identity then transforms those complete quantities into the sum of each value times $D-d+1$. Nothing is approximated and no contribution is omitted, so the returned integer is exactly the inverse-depth weighted sum.

**The exact source is not a per-depth bucket method.**

The manifest summary says integer totals are accumulated by depth and later weighted. That is a valid one-pass family of solutions, but the source does not create an array or map of depth totals. It stores only the two scalar sums plus the maximum depth and uses the expanded formula. The asymptotic bounds remain compatible, but the data flow should be described accurately.

## Complexity detail

Let $N$ be the total number of `NestedInteger` objects visited, including integer objects and list-valued objects, and let $D$ be the maximum nesting depth.

Each object is visited once. Integer work is constant, and iterating a list distributes visits to its children without revisiting them. Total running time is $O(N)$.

The scalar accumulators use $O(1)$ space. Recursive stack depth is at most $D$, so auxiliary space is $O(D)$. No list proportional to the number of depths is allocated, despite the manifest's bucket-oriented summary. Under the stated depth limit of 50, recursion is safely bounded for this problem.

The result and intermediate products fit easily in Python's arbitrary-precision integers. A fixed-width implementation should still select a type that covers the maximum value count, magnitude, and weight product.

## Alternatives and edge cases

- **Two-pass DFS:** First find the deepest integer, then traverse again and apply each explicit inverse weight. This is conceptually direct and still $O(N)$ time, but it visits the structure twice.

- **Totals grouped by depth:** Accumulate one sum per depth, find the deepest occupied level, then multiply each bucket by its inverse weight. This matches the manifest summary and uses $O(D)$ explicit bucket storage.

- **Breadth-first cumulative sum:** Traverse level by level, maintaining an unweighted running sum and adding it to the answer at each level. Values encountered earlier are added more times and therefore receive greater inverse weights. This avoids knowing the final depth in advance but may require a wide queue.

- **Top-level integers:** Their depth is one, so they receive the largest inverse weight, equal to `maxDepth`.

- **Deepest integers:** Their weight is exactly one because `maxDepth - maxDepth + 1 = 1`.

- **Several branches with different depths:** A shallow branch's weights still depend on the deepest integer in any other branch. Shared global `maxDepth` and the final formula handle that cross-branch dependency.

- **Negative and zero integers:** Zero changes neither sum; negative values participate normally and can reduce the final answer.

- **One top-level integer:** Then `maxDepth = 1`, and the formula returns that value with weight one.

- **No empty lists:** This guarantee is material because the source updates maximum depth for list objects before descending. Every list must lead to a deeper integer.

- **Platform interface objects:** The user should not recreate `NestedInteger`. The solution only consumes the methods supplied by the execution environment.
