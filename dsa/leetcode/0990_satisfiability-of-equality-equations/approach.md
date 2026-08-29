## General

**Treat equality as membership in the same component**

Equality has three crucial properties: every variable equals itself, equality works in both directions, and equality is transitive. If `a == b` and `b == c`, then `a` and `c` must receive the same integer even when no direct equation joins them.

These properties mean that all variables connected by equality equations form one equivalence class. The only possible contradiction occurs when an inequality demands two variables from the same class to differ.

A disjoint-set union structure, also called union-find, maintains exactly these equality classes while equations are processed.

**Represent the twenty-six variables**

Lowercase letters are converted to indices zero through twenty-five with

`ord(letter) - ord('a')`.

Array `p = list(range(26))` starts with `p[x] = x` for every variable. Initially, each letter is the representative, or root, of its own one-element component. No equality has yet forced two different variables together.

An equation always has length four. The code reads its variables from `e[0]` and `e[-1]`, while `e[1]` distinguishes `'='` from `'!'`. Using `e[-1]` is equivalent to `e[3]` and emphasizes that the second variable is the final character.

**Find the representative of a component**

Function `find(x)` follows parent pointers until it reaches an index whose parent is itself. That self-parent is the representative shared by all variables in the component.

The recursive step

`p[x] = find(p[x])`

also performs path compression. After discovering the root, it rewires `x` directly to that root. Future calls for `x`, and often for nodes along the same path, need fewer pointer traversals.

Path compression changes only the shape of the internal forest. It never changes which variables belong to the same component.

**Process every equality before any inequality**

The first loop considers only equations whose second character is `'='`. For `a == b`, it executes

`p[find(a)] = find(b)`.

Both `find` calls return component roots. Attaching the first root to the second merges the complete equality classes, not merely the two individual letters. Every variable already equal to `a` thereby becomes equal to every variable already equal to `b`.

The order of the two passes is essential. An inequality that appears early in the input may become contradictory only after a later chain of equalities is known. Checking inequalities immediately could incorrectly accept it before the components are complete. Unioning all equalities first captures their full transitive closure regardless of input order.

**Check inequalities against the completed classes**

The second loop considers equations whose second character is `'!'`. If

`find(a) == find(b)`,

then equality constraints have forced both variables into the same component. They must receive the same value, directly contradicting `a != b`, so the method returns `False` immediately.

If every inequality connects two different representatives, no contradiction exists and the method returns `True`.

This final acceptance is constructive: assign one distinct integer to each remaining union-find root, and give every variable the integer assigned to its root. Every equality is satisfied because its endpoints were unioned. Every inequality is satisfied because its endpoints were verified to have different roots.

**Trace a transitive contradiction**

Consider

`["a==b", "b==c", "a!=c"]`.

Initially, `a`, `b`, and `c` have different roots. The first equality merges the components of `a` and `b`. The second merges that combined component with `c`. Even though `a==c` never appears directly, `find(a)` and `find(c)` now return the same representative.

During the second pass, `a!=c` detects that shared root and returns `False`. This is exactly the transitive implication the algorithm must capture.

For `["a==b", "c!=a"]`, equality merges only `a` and `b`. Variable `c` retains a different root, so the inequality passes. Assigning zero to the `a`/`b` component and one to `c` demonstrates satisfiability.

**Why no union by rank is needed for correctness**

The assignment always attaches the root of `a` to the root of `b` without comparing tree sizes. Union by rank or size could keep parent trees shallower, but it does not alter component membership. Path compression already shortens searched paths, and the universe contains only twenty-six variables, so the simpler merge is entirely adequate.

Most importantly, the left side is `p[find(a)]` rather than `p[a]`. Reparenting a non-root directly could detach or misrepresent part of a component. Merging roots preserves the forest structure.

**Why the two-pass result is exact**

After the first pass, two variables have the same representative exactly when equality equations connect them through some chain. Each processed equality merges its endpoints, so every equality chain lies within one component. Conversely, components merge only because of equality equations, so membership implies such a chain.

If the second pass finds equal roots for an inequality, transitivity forces equal values and the system is impossible. If it finds no such pair, the distinct-root assignment described above satisfies every equation. Therefore, returning `False` identifies precisely the contradictory systems, and returning `True` is backed by an actual possible assignment.

## Complexity detail

Let `Q` be the number of equations and let the variable universe contain `26` elements.

The algorithm makes two passes over `Q` equations and performs a constant number of union-find operations per equation. Path compression makes representative queries extremely close to constant time; the conventional bound is `O(Q\alpha(26))`, where `\alpha` is the inverse Ackermann function. Since twenty-six is fixed, this is simply `O(Q)` in practical and ordinary asymptotic terms.

Even without relying on the refined amortized notation, a parent path contains at most twenty-six nodes, so the fixed alphabet gives a direct `O(26Q) = O(Q)` bound.

The parent array always contains twenty-six integers. Recursive `find` depth is at most twenty-six before compression, so auxiliary space is `O(26)`, which is constant with respect to `Q`.

## Alternatives and edge cases

- **Equality graph plus DFS:** Add undirected edges for `==` equations, label connected components, and test inequalities afterward. It is equally sound but stores an adjacency structure that can include many repeated edges.
- **Repeated reachability search:** For every inequality, search an equality graph to see whether its endpoints connect. This repeats component work that union-find performs once.
- **Check equations in one input-order pass:** This is unsafe because a later equality may create a contradiction with an earlier inequality. Equalities must be finalized first.
- **Union individual nodes instead of roots:** Assigning `p[a] = b` without `find` can break the representation of existing components. Root-to-root linking preserves equivalence classes.
- **Self-equality `a==a`:** Both roots are already identical, so the union changes nothing and the equation is always satisfied.
- **Self-inequality `a!=a`:** Both endpoints necessarily have the same root, so the second pass immediately returns `False`.
- **Duplicate equations:** Repeating an equality performs an idempotent merge; repeating a compatible inequality does not alter the result.
- **Indirect chains:** Any length of equality chain is compressed into one component, so an inequality between its endpoints is detected.
- **Variables absent from equalities:** They remain singleton components and can freely receive values distinct from incompatible variables.
- **No inequalities:** Equalities alone are always satisfiable by assigning one integer per component, so the method returns `True`.
- **No equalities:** Every letter remains separate; only a self-inequality can be contradictory.
- **Representative identity:** The numeric root chosen for a component is an implementation detail. Only whether roots are equal matters.
