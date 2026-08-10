## General

**Turn equations into connected components with ratios**

Each equation connects two variables. If `a / b = 2` and `b / c = 3`, then `a`, `b`, and `c` belong to one connected component, and `a / c = 6`. Variables in different components have no determined ratio.

Ordinary union–find can answer whether two variables are connected. This solution augments it with multiplicative weights so it can also recover their quotient.

It maintains two mappings:

- `p[x]` is the current parent of variable `x`;
- `w[x]` is the ratio $x / p[x]$.

For a root, `p[x] == x` and its weight is one, because $x/x=1$.

**Initialize every known variable before merging**

The first loop over `equations` assigns each encountered variable as its own parent. All of this initialization happens before any equation is processed by union, so repeated assignments cannot destroy an already-built component.

The weight dictionary is a `defaultdict` whose missing value is one. Thus every newly initialized root begins with the correct self-ratio.

Variables that appear only in queries are deliberately not inserted. The problem defines them as unknown, even for a query such as `x / x`; the correct result for an undefined variable is `-1.0`, not one.

**What `find(x)` returns and repairs**

`find(x)` returns the root of `x`’s component. It also compresses the path and updates `w[x]` so that after the call:

$$
\texttt{p}[x]=\text{root}
\quad\text{and}\quad
\texttt{w}[x]=\frac{x}{\text{root}}.
$$

Suppose `x` currently points to `origin`, and `origin` eventually points to a root. Before compression, the weight invariant gives

$$
\texttt{w}[x]=\frac{x}{\text{origin}}.
$$

The recursive call `find(origin)` compresses `origin` and makes

$$
\texttt{w}[\text{origin}]=\frac{\text{origin}}{\text{root}}.
$$

Multiplying the weights yields

$$
\frac{x}{\text{origin}}
\cdot
\frac{\text{origin}}{\text{root}}
=
\frac{x}{\text{root}}.
$$

That is exactly why the code saves `origin`, recursively updates the parent, and then performs `w[x] *= w[origin]`. Saving the old parent is essential: after `p[x] = find(p[x])`, `p[x]` is already the root, but the multiplication needs the updated weight of the old intermediate parent.

**Derive the union weight from the equation**

For an equation `a / b = v`, calls to `find` produce roots `pa` and `pb`. After those calls:

$$
\texttt{w}[a]=\frac{a}{pa}
\quad\text{and}\quad
\texttt{w}[b]=\frac{b}{pb}.
$$

If the roots are different, the exact solution attaches `pa` under `pb` by setting `p[pa] = pb`. It must choose a weight for that new parent edge:

$$
\texttt{w}[pa]=\frac{pa}{pb}.
$$

Starting from the known equation,

$$
\frac{a}{b}
=
\frac{\texttt{w}[a]\,pa}{\texttt{w}[b]\,pb}
=v.
$$

Solving for the required root ratio gives

$$
\frac{pa}{pb}
=
\frac{\texttt{w}[b]\,v}{\texttt{w}[a]}.
$$

The assignment `w[pa] = w[b] * v / w[a]` is this formula directly. Once the root edge has that weight, every existing ratio in both components and the new equation are simultaneously preserved.

**Why an equation inside one component needs no update**

If `pa == pb`, the two variables are already connected. The input promises no contradictory equations, so the existing implied ratio agrees with `v`. The code safely continues without changing parents or weights.

In a version where contradictions were possible, this branch would need to compare `w[a] / w[b]` with `v` using floating-point tolerance. That validation is unnecessary under this contract.

**Evaluating a query**

For query `c / d`, the list comprehension handles three cases using short-circuit `or`:

1. If `c` or `d` is absent from `p`, at least one variable is undefined, so the result is `-1`.
2. Otherwise, `find(c)` and `find(d)` compress their paths and reveal their roots. Different roots mean no equation chain connects them, so the result is `-1`.
3. If roots match, the updated weights are $c/root$ and $d/root$. Their quotient is

$$
\frac{\texttt{w}[c]}{\texttt{w}[d]}
=
\frac{c/root}{d/root}
=
\frac{c}{d}.
$$

The integer literal `-1` is numerically equivalent to the required `-1.0` in Python’s returned list comparisons.

Short-circuiting is important: `find` indexes `p[x]`, so it must not be called for an undefined variable. The membership checks appear first and prevent that access.

**Tracing `a / b = 2`, then `b / c = 3`**

Initially all three variables are separate roots with weight one.

For `a / b = 2`, roots are `a` and `b`. The solution attaches `a` to `b` and sets

$$
w[a]=w[b]\cdot2/w[a]=2.
$$

This represents $a/b=2$.

For `b / c = 3`, it attaches root `b` to root `c` with weight three. The parent chain is now `a -> b -> c`, with `w[a] = 2` and `w[b] = 3`.

Calling `find(a)` recursively finds `c`, changes `p[a]` directly to `c`, and multiplies its weight to `2 * 3 = 6`. Calling `find(c)` leaves weight one. Query `a / c` returns `6 / 1 = 6`.

Query `b / a` compresses both and returns `3 / 6 = 0.5`. Query `a / a` returns `6 / 6 = 1`. Query `x / x` returns `-1` because `x` never appeared in an equation.

**The representation invariant proves correctness**

Initially every known node is its own root with ratio one. `find` preserves the represented ratios while replacing a path by an equivalent direct root edge. The union formula attaches one root with exactly the ratio required by the new equation, without changing relationships inside either component.

By induction over equations, two variables share a root exactly when an equation chain relates them, and each compressed weight is the variable-to-root ratio. Dividing two same-root weights therefore gives the uniquely determined query quotient. Unknown or separate variables correctly return the failure value.

## Complexity detail

Let $e$ be the number of equations, $q$ the number of queries, and $v$ the number of distinct variables.

Initialization takes $O(e)$. Each equation and query performs a constant number of `find` operations. Path compression makes repeated operations fast, but the exact solution does not perform union by rank or union by size; it always attaches the first root under the second.

The classic $O((e+q)\alpha(v))$ bound requires path compression together with a balancing rule. Because that balancing rule is absent here, the manifest’s inverse-Ackermann bound is not rigorously justified for the exact source. A standard conservative amortized bound for path compression with arbitrary linking is $O((e+q)\log v)$, with an individual first `find` potentially traversing a chain of length $O(v)$. The problem’s small constraints make either bound easily fast enough.

The parent and weight mappings store one entry per known variable, using $O(v)$ space. Recursive `find` can use $O(v)$ call-stack space before a long chain is compressed. The returned answer list adds $O(q)$ output space, normally excluded from auxiliary-space reporting.

Floating-point multiplication and division are treated as constant-time arithmetic. The no-contradiction guarantee avoids needing numerical consistency checks around cycles.

## Alternatives and edge cases

- **Weighted graph plus DFS:** Add edges `a -> b` with weight `v` and `b -> a` with weight `1/v`. For each query, search a path and multiply weights. This is simpler to derive but can revisit the graph for every query, costing $O(eq)$ in the worst case.

- **Weighted graph plus BFS:** Uses the same ratio-product idea with an explicit queue instead of recursion. It has similar per-query complexity.

- **Union by rank or size:** Tracking component rank/size while retaining the weight algebra would prevent tall trees and, together with path compression, support the manifest’s inverse-Ackermann amortized bound.

- **Known variable divided by itself:** Both finds return the same root and equal weights divide to one.

- **Unknown variable divided by itself:** Membership is checked before equality, so the result is `-1`, as required.

- **Known variables in different components:** Both exist, but roots differ, so no quotient is determined.

- **Reverse query:** If `a / b = v`, same-root weights naturally return `b / a = 1/v`; no explicit reverse equation is stored.

- **Repeated or redundant equation:** When roots already match, the no-contradiction guarantee permits ignoring it.

- **Long parent chain:** The first find may recurse deeply, but path compression makes later finds on those nodes direct or nearly direct.

- **Floating-point ratios:** Results are products and quotients of supplied real values. Ordinary floating-point rounding is expected; exact rational arithmetic is not required.

- **No division by zero:** All equation values are positive, and the contract guarantees query evaluation never requires division by zero.

- **Initialization order:** The exact code initializes every variable in a separate pass before unioning. Interleaving the same unconditional `p[x] = x` assignments with unions would incorrectly reset existing components.
