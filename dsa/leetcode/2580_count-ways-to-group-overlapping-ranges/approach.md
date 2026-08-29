## General

**Overlapping ranges form inseparable components**

If two ranges overlap, they must be placed in the same group. This requirement is transitive. If range $A$ overlaps $B$ and $B$ overlaps $C$, then all three must share a group even when $A$ and $C$ do not overlap directly.

Imagine a graph whose vertices are ranges and whose edges connect overlapping pairs. Every connected component of this graph must be assigned as one indivisible unit. Different components have no overlap chain between them, so their group choices are independent.

The task is therefore:

1. count the overlap-connected components;
2. choose group one or group two independently for each component.

If there are $c$ components, the answer is $2^c$.

**Sort by starting coordinate**

The code sorts `ranges` lexicographically, which primarily orders them by start. It then scans them while maintaining `mx`, the farthest end coordinate reached by all ranges in the current overlap component.

Initially `mx = -1`. Since every start is nonnegative, the first range necessarily starts a new component and increments `cnt`.

For each `[start,end]`:

- if `start > mx`, there is a strict gap after the previous component, so this range starts a new one;
- otherwise `start <= mx`, so it overlaps the already merged coverage and belongs to the current component.

After either case, `mx = max(mx, end)` extends or preserves the farthest reach.

**Why comparing with the maximum end is enough**

Suppose earlier ranges in the current component have collectively reached through coordinate `mx`. A new sorted range begins no earlier than all previously processed starts.

If `start <= mx`, at least one chain in the current component reaches the new start. More concretely, the interval that established or extended `mx` is connected through prior overlaps to the component, and the new range intersects the merged covered span at an integer coordinate. It therefore joins the same overlap-connected component.

The new range might not overlap the first interval directly. For example, `[1,3]`, `[2,5]`, and `[4,8]` form one component: the third starts after the first ends but before the accumulated maximum end $5$. The scan correctly preserves their transitive connection.

If `start > mx`, every previous range ends at or before `mx`, strictly before the new start. Because later ranges start no earlier than this new one, no future interval can bridge backward across that already completed gap. A new component is unavoidable.

**Inclusive endpoints determine the strict comparison**

Ranges contain both endpoints. If one range ends at $5$ and another starts at $5$, they share integer $5$ and overlap. Therefore `start == mx` stays in the current component.

Only `start > mx` proves disjointness. Using `>=` would incorrectly separate touching inclusive ranges.

**Why each component contributes exactly two choices**

All ranges in one connected component must stay together. The component can be assigned to the first labeled group or the second labeled group, giving two choices.

No constraint relates two different components, so selecting a group for one does not restrict any other. By the multiplication principle, $c$ independent binary choices yield

$$
2\cdot2\cdots2=2^c.
$$

Both groups are allowed to be empty, so assignments putting every component in group one or every component in group two are valid. The groups are distinguished: swapping their contents is generally a different split, which is why even one component gives two ways rather than one.

**Trace the second example**

After sorting, the ranges are `[1,3]`, `[2,5]`, `[4,8]`, and `[10,20]`.

- `[1,3]` begins component one and sets `mx=3`.
- `[2,5]` starts no later than $3$, joins it, and extends `mx` to $5$.
- `[4,8]` starts no later than $5$, joins through the second range, and extends `mx` to $8$.
- `[10,20]` starts after $8$, so it begins component two.

There are two components and therefore $2^2=4$ groupings.

**Modular exponentiation**

The function uses `pow(2, cnt, mod)`. Python's three-argument power computes the exponent modulo $10^9+7$ with fast exponentiation, avoiding construction of the potentially enormous exact value $2^{cnt}$.

Sorting is done in place, so the original ordering of `ranges` is not preserved.

## Complexity detail

Let $n$ be the number of ranges. Sorting costs $O(n\log n)$ time. The scan visits every range once in $O(n)$ time, and modular exponentiation costs $O(\log n)$ multiplications because the exponent is at most $n$. Sorting dominates, so total time is $O(n\log n)$.

Python's Timsort can use $O(n)$ temporary space, matching the manifest. The scan itself uses $O(1)$ additional state. The input list is reordered.

## Alternatives and edge cases

- **Build the overlap graph:** Testing every pair can require $O(n^2)$ edges and work; sorted interval merging finds components directly.
- **Union-find after pair checks:** Disjoint-set union captures transitivity but still needs an efficient way to discover overlaps, which sorting already solves more simply.
- **Touching endpoints:** `[1,3]` and `[3,7]` overlap at $3$ and must stay in one component.
- **Nested ranges:** A contained range never decreases `mx` and remains in the enclosing component.
- **Transitive bridge:** Ranges need not all intersect a common point; a chain of pairwise overlaps is enough.
- **All disjoint:** Every range is its own component, giving $2^n$ assignments modulo the required modulus.
- **All connected:** There is one component and exactly two assignments.
- **Duplicate ranges:** They overlap completely and remain in the same component.
- **Empty groups:** Explicitly allowed, so the two all-in-one-side assignments count.
- **Input mutation:** `ranges.sort()` changes range order; sort a copy if caller order matters.
