## General
**Separate the closest occurrence by direction**

For any index `i`, a closest occurrence of `c` is either the nearest one at or to the left of `i`, or the nearest one at or to the right. Any farther occurrence on the same side has a larger absolute index difference and can never improve the answer. It is therefore enough to learn one nearest occurrence from each direction.

**Record distances from the left**

Sweep from left to right while storing the most recent index containing `c`. At each position, write `i - previous` into the result. Before the first occurrence, initialize `previous` far enough to the left to produce a harmless large provisional value; the later right-to-left sweep will replace it with a real distance.

**Improve with distances from the right**

Sweep from right to left while storing the next index containing `c`. At position `i`, compare the existing left distance with `following - i` and keep the smaller value. The guarantee that `c` occurs in `s` ensures at least one of these directional candidates is real for every index.

**Why the two minima are globally sufficient**

After the first sweep, each position knows its closest occurrence on the left because the stored index is the latest one encountered. The reverse sweep analogously supplies the closest occurrence on the right. Every occurrence lies on one of those sides, and the closest on a side dominates all farther occurrences there. Taking the smaller directional distance therefore equals the minimum over every occurrence of `c`.

## Complexity detail
Let `n = len(s)`. Each sweep examines all `n` positions once, so the total time is $O(n)$. The returned distance list contains `n` integers and uses $O(n)$ space; beyond that required output, the algorithm keeps only the two occurrence indices and loop variables.

## Alternatives and edge cases
- **Store positions plus binary search:** Collect every occurrence of `c`, then binary-search its neighbors for each index. This is correct but costs $O(n \log m)$ time for `m` occurrences instead of two linear sweeps.
- **Scan all occurrences for every index:** Directly minimizing over the string at every position is simple but can take $O(n^2)$ time when `c` is rare.
- **Multi-source breadth-first expansion:** Starting from all occurrences and expanding along adjacent indices also finds shortest distances in $O(n)$ time, but a queue adds machinery unnecessary on a line.
- **The current character is `c`:** Both directional distances can be zero, and the answer at that index is zero.
- **One occurrence at an endpoint:** One sweep supplies all final distances while the other retains only larger provisional values.
- **Equal-distance tie:** Keep either directional candidate; only the shared distance is returned.
- **Every character is `c`:** Every answer entry is zero.
- **One-character string:** The guaranteed occurrence is at index zero, producing `[0]`.
