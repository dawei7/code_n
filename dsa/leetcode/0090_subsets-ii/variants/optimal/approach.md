## General

If every array position were treated as an independent yes-or-no choice, a length-$n$ array would produce $2^n$ branches. That works when all values are distinct. With duplicates, however, different position choices can describe the same value multiset. For `[2, 2]`, choosing only the first `2` and choosing only the second `2` both produce `[2]`. The selected depth-first search prevents that duplication while still producing every legal multiplicity of each value.

The first essential step is `nums.sort()`. Sorting places equal values next to one another. That changes neither which subsets exist nor how many copies of a value a subset may contain, but it gives the recursion a contiguous run that it can skip as one unit.

**Meaning of one recursive state**

At the start of `dfs(i)`, the list `t` contains the values selected from positions before `i`, and the recursion must generate every distinct continuation using positions from `i` onward. The state makes two conceptual choices concerning `nums[i]`:

- include this occurrence, or
- include no additional occurrence of this value from the run beginning at `i`.

The first branch executes `t.append(nums[i])` and calls `dfs(i + 1)`. Moving by only one position is intentional. If the next position contains the same value, the recursive call may include that next copy too. Repeated include decisions are how the algorithm produces multiplicities one, two, three, and so on.

After that whole branch finishes, `x = t.pop()` both restores the path and remembers which value was just considered. Restoration matters because the second branch must begin with exactly the selections that existed before the current decision. Without the `pop`, the supposed exclusion branch would still contain the value.

The `while` loop then advances `i` across every immediately following occurrence equal to `x`. Finally, `dfs(i + 1)` starts after the entire equal-value run. This is the zero-additional-copies branch.

**A complete trace for `[1, 2, 2]`**

After sorting, the array is unchanged.

1. At index `0`, include `1`. The path is `[1]`.
2. At the first `2`, include it. The path is `[1, 2]`.
3. At the second `2`, include it and reach the end, recording `[1, 2, 2]`.
4. Back at the second `2`, exclude it and record `[1, 2]`.
5. Back at the first `2`, its exclusion branch skips the second equal `2`, recording `[1]`. It does not create another path that selects only the second copy, because that would duplicate `[1, 2]`.
6. Back at `1`, exclude it and repeat the same multiplicity choices for the `2` run, recording `[2, 2]`, `[2]`, and `[]`.

The output order may differ from the Reference example, which is allowed. The significant fact is that every distinct subset appears once.

**Why no valid subset is missed**

Think of the sorted input as groups of equal values. If a value occurs $c$ times, a subset may contain it exactly $0,1,\ldots,c$ times. The recursion represents those choices without naming them explicitly. Taking the include branch $k$ consecutive times and then taking the exclusion branch selects exactly $k$ copies. Taking exclusion immediately selects zero copies. Therefore every possible multiplicity for the current group is represented.

Once that multiplicity is fixed, recursion continues with the next distinct value group. Combining one valid multiplicity choice from every group describes every possible subset of the input multiset. Thus the traversal is complete.

**Why duplicate subsets cannot be generated**

For each equal-value group, a produced recursion path has one unique count: the number of consecutive include choices made before the single branch that skips the rest of the run. The algorithm never offers a second way to choose the same count by selecting different physical copies. For example, “choose one `2`” is represented only by including the first available `2` and then skipping the rest, never by skipping the first and choosing a later identical occurrence.

Two leaves that differed anywhere in their sequence of group multiplicities would contain different numbers of at least one value, so their subsets would differ. Hence distinct recursion leaves produce distinct subsets.

**Why copying occurs only at a leaf**

When `i == len(nums)`, every value group has been decided. The algorithm appends `t[:]`, not `t` itself. The slice makes a snapshot. The list `t` is a single mutable backtracking path that will be changed by later `append` and `pop` operations; storing it directly would make every answer entry refer to the same object and eventually show the same contents.

Only complete decisions are recorded, so the empty subset is naturally produced by taking every exclusion branch. No special insertion of `[]` is necessary.

## Complexity detail

Let $n$ be `len(nums)`, and let $U$ be the number of distinct subsets returned. If the distinct values have frequencies $c_1,c_2,\ldots,c_k$, then

$$
U=\prod_{r=1}^{k}(c_r+1),

$$

because each value group contributes a choice of zero through $c_r$ copies.

There is one leaf per distinct subset. Copying `t` at a leaf costs time proportional to its length, at most $n$, so materializing all outputs costs $O(nU)$. The recursion also visits internal decision states and scans duplicate runs in exclusion branches. Across the generated group-count choices, this work is bounded by the same $O(nU)$ envelope. Initial sorting costs $O(n\log n)$; for nonempty inputs, the output-sensitive bound dominates under the manifest's convention, yielding $O(n\cdot U)$. In the all-distinct worst case, $U=2^n$, so this becomes $O(n2^n)$.

Auxiliary recursion depth is at most $n$, and `t` holds at most $n$ selected values. These use $O(n)$ space. Python's in-place sort may also require up to $O(n)$ temporary references. The answer itself contains $U$ lists and as many as $O(nU)$ stored values; the manifest's $O(n)$ space bound excludes that required output. Including output, total space is $O(nU)$.

## Alternatives and edge cases

- **Iterative cascading:** Start with `[[]]` and extend all existing subsets for a new value, but extend only the subsets created in the immediately preceding step when seeing another copy of that value. This avoids recursion and has the same output-sensitive time bound.
- **Frequency-map recursion:** Compress the sorted input into `(value, count)` groups, then explicitly loop over choosing zero through `count` copies. This can make the multiplicity model especially clear, at the cost of building the compressed representation.
- **Bitmask plus a set:** Enumerate all $2^n$ position masks, canonicalize each produced subset, and deduplicate with a hash set. It is easier to adapt from the distinct-elements problem but deliberately creates duplicates and uses output-scale auxiliary storage.
- **Do not skip duplicates in the include branch:** Later equal copies must remain available so subsets containing two or more copies can be formed. Skipping belongs only to the branch that chooses no further copy of the current value.
- **Sorting mutates the input:** `nums.sort()` changes the caller-provided list order. The contract does not forbid this, but copy and sort into a new list if input preservation is required by a surrounding application.
- **All values equal:** For $n$ copies of one value, the valid answers are exactly the $n+1$ possible multiplicities. The recursion generates those without exploring $2^n$ duplicate position combinations.
- **All values distinct:** The `while` loop never advances extra positions, reducing the method to ordinary include/exclude subset generation with $2^n$ outputs.
- **Negative values and zero:** Sorting and equality are the only value-sensitive operations. Their signs have no effect on the argument.
- **Single element:** The two leaves return the one-element subset and the empty subset, each exactly once.
