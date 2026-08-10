## General

**Group indices by value**

Distances for index `i` involve only other indices holding `arr[i]`. The first pass builds `d[value]` as the increasing list of positions where that value occurs.

Indices are appended during a left-to-right scan, so every group list is already sorted. No explicit sorting is required.

Once groups are separated, each group's distance sums can be computed independently and written into the corresponding positions of `ans`.

**Compute the distance sum at the first occurrence**

For one group with sorted positions

$$
v_0<v_1<\cdots<v_{m-1},
$$

the distance from `v[0]` to every group position is `v[q] - v[0]` because all positions lie to its right or equal it.

The source calculates

`val = sum(v) - v[0] * m`,

which equals

$$
\sum_q(v_q-v_0).
$$

The self-distance contributes zero automatically.

**Update the sum when moving to the next occurrence**

Suppose the center moves from `v[i - 1]` to `v[i]`. Let

`delta = v[i] - v[i - 1]`.

There are `i` positions to the left of `v[i]`. Their distances each increase by `delta`, contributing `i * delta`.

There are `m - i` positions at or to the right of `v[i]`. Relative to the previous center, their distances each decrease by `delta`, contributing `-(m - i) * delta`.

Therefore,

`val += i * delta - (m - i) * delta`.

The updated `val` is written at original position `p = v[i]`.

For `i = 0`, `delta` is defined as zero, so the initial value is written unchanged.

**Trace one occurrence group**

For value 3 at positions `[2, 5, 6]`, $m=3$.

At position 2, the initial sum is $(2+5+6)-2\cdot3=7$.

Move to position 5: `delta = 3`, one position is left and two are at/right. The new value is $7+1\cdot3-2\cdot3=4$.

Move to position 6: `delta = 1`, two positions are left and one is at/right. The new value is $4+2\cdot1-1\cdot1=5$.

These match direct distances 7, 4, and 5.

**Why the recurrence is correct**

When the reference point shifts right by `delta`, every group position lies in one of two categories. Positions left of the new center become exactly `delta` farther away; positions at or right become exactly `delta` closer compared with the old center. The recurrence accounts for every position once with the correct sign.

Starting from the exact first-position sum and applying this exact transition proves every group's written answer by induction.

Every array index belongs to exactly one value group, so all answer entries are filled once. A singleton group has initial sum zero and correctly receives zero.

**Why this avoids pairwise work**

A group of $m$ occurrences has $O(m^2)$ index pairs. Directly summing distances separately for every occurrence repeats the same information.

The initial sum plus $m-1$ constant-time transitions handles the full group in $O(m)$.

**Expand the transition algebra**

Let $F(p)=\sum_q\lvert p-v_q\rvert$. Moving the center from $p=v_{i-1}$ to $p+\delta=v_i$ changes each term independently.

For the $i$ positions $v_0$ through $v_{i-1}$, the center moves farther right, so every absolute difference gains $\delta$. For positions $v_i$ through $v_{m-1}$, the center moves toward them, so every difference loses $\delta$. Summing the changes gives

$$
F(v_i)-F(v_{i-1})=i\delta-(m-i)\delta.
$$

This is exactly the update in the source.

**Why the current position belongs to the right count**

At the old center $v_{i-1}$, the distance to $v_i$ is $\delta$. At the new center it becomes zero, a decrease of $\delta$. Therefore `v[i]` belongs among the `m - i` terms that decrease, even though it is the new center rather than strictly to its right.

This detail explains the coefficient `m - i` rather than `m - i - 1`.

**Grouping retains original multiplicity**

The dictionary values are lists, not sets. Every occurrence index is stored even when many array elements share the same numeric value. This is essential because each occurrence has its own requested output and contributes separately to other occurrences' distance sums.

## Complexity detail

Let $n$ be the array length.

Building groups visits each index once. Across all groups, `sum(v)` and the recurrence loops process exactly $n$ stored positions. Total time is $O(n)$.

The group lists collectively store $n$ indices, and the output stores $n$ values. Auxiliary grouping space is $O(n)$, matching the manifest.

Hash-map operations are expected constant time.

## Alternatives and edge cases

- **Compare every equal pair for every index:** This can become $O(n^2)$ when all values match. The recurrence is linear.
- **Two prefix-sum passes per value:** Prefix index sums can compute left and right contributions directly. It is equivalent in complexity to the delta recurrence.
- **Global prefix sums:** They cannot separate only identical values without grouping.
- **Singleton value:** Its only distance is to itself, zero.
- **All values distinct:** Every answer is zero.
- **All values identical:** One group is processed in linear time.
- **Large gaps between occurrences:** `delta` captures their true index distance.
- **Self-distance:** Included algebraically as zero and requires no special removal.
- **Sorted group requirement:** It is satisfied automatically by left-to-right insertion.
- **Original output positions:** `ans[p]` restores results from group order to array order.
- **Large sums:** Python integers safely hold total distances.
- **Input preservation:** `arr` is only scanned.
- **Current occurrence coefficient:** It is included in the decreasing side of the transition because its prior distance becomes zero.
- **Group multiplicity:** Lists preserve every occurrence position.
