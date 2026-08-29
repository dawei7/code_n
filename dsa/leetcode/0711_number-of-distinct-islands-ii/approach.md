## General

Two islands are equivalent even when one is translated, rotated by a quarter turn, or reflected. The solution therefore cannot use absolute grid coordinates or only one traversal direction signature.

It performs three stages for each island:

1. depth-first search collects every cell coordinate;
2. all eight rotation/reflection variants are generated and translated to a common origin;
3. the lexicographically smallest normalized variant becomes the island's canonical key.

Equal shapes under any allowed transformation receive the same key.

**Collecting one island**

The outer loops scan every grid cell. When a cell still contains `1`, a new `shape` list is created and `dfs` explores its entire four-directional component.

Each visited coordinate `[i, j]` is appended to `shape`, then `grid[i][j] = 0` marks it visited.

The four offsets `[1,0]`, `[-1,0]`, `[0,1]`, and `[0,-1]` include exactly vertical and horizontal neighbors. Boundary and land checks guard recursive calls.

Mutating land to water ensures every cell belongs to one DFS and every island is processed once.

**Why eight transformed shapes are sufficient**

The symmetries of a square grid that preserve distances and adjacency consist of four rotations and four reflected rotations. For a coordinate `(i,j)`, the code generates:

- `(i,j)`;
- `(i,-j)`;
- `(-i,j)`;
- `(-i,-j)`;
- `(j,i)`;
- `(j,-i)`;
- `(-j,i)`;
- `(-j,-i)`.

These sign changes and coordinate swaps enumerate the full eight-element dihedral symmetry group. Some variants may coincide for a symmetric shape, which is harmless.

**Removing absolute translation**

After transformation, coordinates still contain the island's original location. Each variant list `e` is sorted lexicographically. Its first coordinate is the top-left-most point under that transformed orientation.

Every point then subtracts `e[0]`:

$$
(x,y)\mapsto(x-e_0.x,\ y-e_0.y).
$$

This moves the anchor to `(0,0)` and expresses every other cell relative to it. Translating the original island changes all coordinates by the same offset, which disappears under subtraction.

**Why the subtraction loop runs backward**

The code iterates indices from the end down to zero.

This preserves the original anchor `e[0]` while normalizing all later coordinates. When index zero is finally processed, it becomes `[0,0]`.

If the loop moved forward and changed `e[0]` first, later points would subtract the already modified zero coordinate rather than the original anchor. Their absolute transformed locations would remain, breaking translation invariance.

This reverse order is a small but critical implementation detail.

**Choosing a canonical orientation**

After all eight lists are sorted and translated, `shapes.sort()` orders the complete variants lexicographically.

`shapes[0]` is the smallest normalized representation. It is converted from nested mutable lists into:

`tuple(tuple(e) for e in shapes[0])`.

The immutable tuple can be inserted into a set.

The smallest variant is not intrinsically more “correct” than the others. Its purpose is to make an arbitrary but deterministic choice shared by every rotated or reflected copy.

**Why equivalent islands get equal keys**

Suppose island `B` is obtained from island `A` by an allowed rotation, reflection, and translation.

Generating all eight variants for `A` produces the same set of orientations as generating all eight for `B`, possibly in a different order. Translation normalization removes their positional difference. Sorting the variant collection chooses the same minimum coordinate list for both.

Therefore, their canonical tuples are equal.

**Why equal keys imply equivalent islands**

A canonical key is one complete normalized transformed coordinate set. If two islands have equal keys, each has some allowed transformation whose translated coordinate list equals that key.

Applying one transformation inversely and composing it with the other shows that one original island can be rotated/reflected and translated into the other. Equal keys cannot merge genuinely different shapes.

**A simple rotation example**

An L-shaped island with relative cells `(0,0), (1,0), (1,1)` can be rotated into cells `(0,0), (0,1), (1,0)` after translation.

These may have different raw DFS coordinates, but both eight-variant collections contain the same normalized forms. Their minimum form is identical, so the set counts one class.

**Final counting**

Every island contributes one canonical tuple to set `s`. Sets discard duplicate keys. `len(s)` is therefore the number of equivalence classes.

## Complexity detail

Let `L = RC` be the number of grid cells, and let island sizes be `a_1,a_2,\ldots` with total land at most `L`.

DFS and the outer scan take `O(L)` time. For an island of size `a`, generating eight variants is `O(a)`, but sorting each variant costs `O(a\log a)`. Sorting the constant-size collection of eight variants also compares coordinate lists and remains `O(a)` after their internal sorts.

The literal worst-case time is therefore

$$
O\!\left(L+\sum a_i\log a_i\right)
=
O(L\log L).
$$

The common `O(RC)` headline assumes shape-coordinate ordering or hashing can be canonicalized without comparison sorting; the checked-in code explicitly sorts.

Stored canonical shapes, the current variants, mutated-grid traversal, and recursion can collectively use

$$
O(RC)
$$

space. Eight transformed copies are only a constant factor.

## Alternatives and edge cases

- **Traversal signatures for each symmetry:** Transform coordinates or traversal directions and choose a canonical signature. Coordinate sets are usually easier to reason about.

- **Only translation normalization:** That solves Distinct Islands I but would incorrectly separate rotated or reflected copies here.

- **Single-cell islands:** All eight variants normalize to `((0,0),)`, so every isolated cell shares one class.

- **Symmetric shapes:** Several of the eight variants may be identical; selecting the minimum still works.

- **Diagonal contact:** It does not connect cells because DFS uses only four directions.

- **Grid mutation:** All land is turned to zero. A caller needing the original grid must copy it first.

- **Reverse normalization loop:** Forward mutation of the anchor would be incorrect unless the anchor were saved separately.

- **Reflections and rotations only:** Scaling or arbitrary-angle rotation is not included in the eight transforms.

- **Rectangular grid:** Coordinate transforms describe shape independently of whether a rotated copy would fit at the same absolute location; only relative island cells matter.

- **Recursion depth:** One large winding island may exceed Python's recursion limit; iterative DFS preserves the normalization logic.

- **Hashability:** Nested lists cannot be set keys, which is why the chosen representation is converted to nested tuples.

- **All-water grid:** No canonical key is inserted and the result is zero.
