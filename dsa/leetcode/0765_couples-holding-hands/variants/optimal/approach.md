## General

**Replace people with their couple identifiers**

People are numbered so partners are consecutive: `0` with `1`, `2` with `3`, and so on. Integer division by two converts a person ID to a couple ID. The exact source uses the equivalent bit shift:

`person >> 1`.

Thus both members of couple zero map to zero, both members of couple one map to one, and so forth.

**Treat every adjacent seat pair as a connection**

Seats `0` and `1` must ultimately hold one couple, as must seats `2` and `3`, continuing in pairs. For each seat pair, the solution reads the couple IDs `a` and `b` of its two current occupants.

If `a == b`, that seat pair is already correct. If they differ, it connects two couples whose members are mixed within the same rearrangement problem.

The solution unions `a` and `b` in a disjoint-set structure. After all seat pairs are processed, each union-find component represents a group of couples whose members are interwoven among the same collection of seat pairs.

**Why connected components describe independent work**

Every couple contributes two people, and every seat pair contains two people. Inside one connected component of `c` couple IDs, exactly `2c` people occupy exactly `c` adjacent seat pairs.

No person from that component sits in a seat pair connected to a different component; such a seat pair would have created a union edge. Therefore components can be corrected independently.

**Why a component of size `c` needs `c - 1` swaps**

Choose one seat pair in the component. Keep one occupant fixed and swap the other occupant with the fixed person’s partner, wherever that partner sits. This completes one couple in that seat pair.

The displaced person remains among the component’s remaining seats. Repeating fixes one couple per swap. After `c - 1` swaps, the final two people must already be partners, so the component is solved.

This is also a lower bound. A component of `c` intertwined couples cannot be split into `c` independent correct seat pairs without breaking at least `c - 1` of its connections. One swap can increase the number of separated correct groups by at most one. Thus fewer than `c - 1` swaps cannot suffice.

**Sum the component costs**

If component sizes are `c1, c2, ...` and there are `C` components, total swaps are

`(c1 - 1) + (c2 - 1) + ... = n - C`,

because the sizes sum to `n` couples.

The implementation therefore does not need to recover each size. It counts union-find roots and returns `n - root_count`.

**How the union-find works**

Parent array `p` initially makes every couple its own component. `find(x)` follows parent pointers to a root and performs path compression on the return path.

For every seat pair, the root of `a` is attached to the root of `b`. Unioning a couple with itself changes nothing.

The expression

`sum(i == find(i) for i in range(n))`

counts exactly the roots after all unions. A root is the only node whose index equals its final representative.

**Trace `[0, 2, 1, 3]`**

The first seat pair contains couple IDs zero and one, so those components are united. The second pair also contains couples zero and one, which are already connected.

There are two couples and one component, so the answer is `2 - 1 = 1`. Swapping people 2 and 1 produces adjacent couples.

For `[3, 2, 0, 1]`, each seat pair contains one couple ID twice. No distinct components merge, root count remains two, and the answer is zero.


Union operations create exactly the connected groups induced by mixed adjacent seat pairs. Different components share neither people nor seat pairs and may be solved independently.

Within a component of `c` couples, the constructive partner-swap method uses `c - 1` swaps, and the connectivity lower bound requires at least that many. Summing these exact component costs gives `n - C`, which is precisely what the method returns.

## Complexity detail

Let `n` be the number of couples. The algorithm processes `n` seat pairs and performs a constant number of union-find operations per pair.

The exact source uses path compression but no union-by-rank or union-by-size heuristic. A conservative amortized bound is `O(n log n)`; with the usual rank/size addition it becomes `O(n alpha(n))`, effectively linear. Under the small constraints it is commonly summarized as `O(n)`.

The parent array uses `O(n)` space, and recursive `find` uses stack space bounded by the parent-tree height.

## Alternatives and edge cases

- **Greedy physical swapping with a position map:** For every seat pair, locate the first person’s partner and swap it into place. This gives a direct `O(n)` solution when positions are updated.

- **Search for partners linearly:** It is easy to implement but can cost `O(n^2)`.

- **Union by size or rank:** Adding it supplies the strongest standard near-constant union-find guarantee.

- **Already correct pair:** Both people map to the same couple ID and union changes nothing.

- **One connected cycle of all couples:** Root count is one, so exactly `n - 1` swaps are needed.

- **All pairs correct:** Every couple remains its own component and the answer is zero.

- **Input mutation:** This union-find solution analyzes `row` without changing the seating array.
