## General

**Build one ordering from left to right**

The recursive helper keeps `cur`, the prefix selected so far. If its length is $k$, the next recursive depth chooses which unused input element should occupy position $k$. Since all input values are distinct, choosing each unused index once generates the full permutation tree with $n!$ leaves.

The shared Boolean list `used` answers whether an input position already appears in `cur`. At any helper entry, `used[i]` is true exactly when `num[i]` occurs in the current path, and the number of true flags equals `len(cur)`. This relationship is the state invariant that prevents repetition or omission.

**Choose and undo in matched pairs**

The loop examines every input index. If `used[i]` is false, the algorithm performs a choice by setting the flag and appending `num[i]` to `cur`. The recursive call then sees a prefix one element longer and cannot select that index again.

After the child has generated every permutation extending this choice, `cur.pop()` removes the last value and `used[i] = False` restores availability. Both restorations are necessary. Popping without clearing the flag would incorrectly hide the value from sibling branches; clearing without popping would leave a value in the path that the flags no longer describe.

The order of restoration mirrors the choice, but either could technically be restored first after recursion because no other code observes the intermediate state. What matters is that the parent loop resumes with exactly the path and flags it had before selecting index `i`.

**Recognize a complete ordering**

When `len(cur) == len(num)`, the path has one selected value for every input position. The usage invariant guarantees no index appears twice, so it must contain every input element exactly once. The source appends `cur[:]` and returns.

The slice is essential because `cur` is shared. Backtracking immediately pops from it after returning. A result entry that referenced the same object would be shortened and modified along with future searches. A copy freezes the leaf's ordering.

**Following the search tree**

For `[1, 2, 3]`, the root loop first chooses `1`. The next frame chooses `2`, and the next chooses `3`, recording `[1, 2, 3]`. Backtracking from the leaf makes `3` unused, then backtracking one level makes `2` unused. The frame whose prefix is `[1]` can now choose `3` second and `2` third, recording `[1, 3, 2]`.

Once every extension of prefix `[1]` is exhausted, the root restores `1` and selects `2`. In this way, each possible first choice owns a subtree containing every ordering of the remaining elements.

**Why the search is complete**

Take any target permutation of the distinct input values. Its first value occurs at one input index, which the root loop eventually considers. After that choice, its second value's index remains unused and is eventually considered by the next loop. Inductively, the search has a branch that follows all target positions and reaches a leaf containing that permutation.

**Why the search has no duplicate results**

Each root-to-leaf path is a sequence of distinct input indices. Two paths that are not identical have a first depth where they select different indices. Because input values are unique, the output values at that position differ, so the resulting permutations cannot be equal. Thus all $n!$ generated leaves are unique.

**Selected implementation versus `Solution2`**

The same file contains a class named `Solution2` that passes sliced remaining arrays and newly concatenated paths into recursion. The canonical entry class is `Solution`, which uses `used`, append/pop, and shared state. `Solution2` is an unused alternative and its higher allocation cost does not describe the selected branch.

## Complexity detail

The result contains $n!$ permutations, and copying `cur` at each leaf takes $O(n)$ time. Therefore, output construction requires $\Theta(n \cdot n!)$ time. The loops at internal nodes also test candidate indices, and the total remains within the manifest's $O(n \cdot n!)$ bound.

The `used` array, current path, and recursion stack each contain at most $n$ entries or frames, giving $O(n)$ auxiliary space. The returned nested list requires $\Theta(n \cdot n!)$ space for all elements; as usual, this required output is separate from the auxiliary-space bound.

Unlike `Solution2`, the selected method does not allocate a new remaining list and new path on every edge. It creates copies only for completed results, which are necessary for correctness.

## Alternatives and edge cases

- **Preallocated path positions:** Reserve a length-$n$ path and write at the current depth. It keeps the same visited-array logic and avoids append/pop on the path itself.
- **In-place swap recursion:** Swap each suffix element into the current position, recurse, then swap it back. This avoids `used` but temporarily mutates the array.
- **Remaining-list slicing:** Pass `nums[:i] + nums[i+1:]` to each child. It is easy to visualize but creates many intermediate lists and raises auxiliary copying costs.
- **Lexicographic next permutation:** Starting from sorted values, repeatedly compute the next ordering. It avoids recursion but still must copy each of the $n!$ outputs.
- **Single-element list:** One choice reaches the base case and produces exactly one permutation.
- **Negative and zero values:** They are ordinary distinct elements; the algorithm depends on identity and usage flags, not numeric magnitude.
- **Duplicate input outside the contract:** Index tracking would generate duplicate value permutations. Depth-level equal-value skipping would be required for the Permutations II variant.
- **Restoration order:** Both `cur.pop()` and `used[i] = False` must happen after every child so sibling branches begin cleanly.
- **Caller input:** The selected solution neither sorts nor writes to `num`, preserving its original contents and order.
- **Output ordering:** Results follow depth-first input-index order, but the problem permits any order.
