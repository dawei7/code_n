## General

**A permutation is a sequence of position choices**

The input has $n$ distinct values, and a permutation must place each one into exactly one of $n$ output positions. The solution fills those positions from left to right. At depth `i`, positions 0 through `i - 1` are already fixed, position `i` is the next decision, and every not-yet-used input index is a legal choice.

This turns the problem into a backtracking tree. The root has $n$ choices for the first position, each child has $n-1$ choices for the second, and the number of leaves is

$$
n(n-1)(n-2)\cdots 1 = n!.
$$

Every leaf corresponds to one complete ordering, so visiting all leaves is unavoidable when all permutations must be returned.

**Why the algorithm tracks indices with `vis`**

`vis[j]` records whether input position `j` is already represented in the current partial permutation. A value becomes unavailable immediately after it is placed and becomes available again when backtracking leaves that branch.

Tracking indices is precise because the requirement is to use every input element once. The contract says the values are distinct, so tracking values in a set could also work, but an index-based Boolean list avoids hashing and maps directly to the iteration over `nums`.

At entry to `dfs(i)`, exactly `i` entries of `vis` are true, and `t[0:i]` contains those corresponding values in the order selected. This is the central invariant. It holds initially for `dfs(0)` because no positions are filled and every flag is false.

**Use a preallocated path array**

`t = [0] * n` reserves all output positions once. When unused input index `j` is chosen at depth `i`, the code writes `t[i] = nums[j]`. This avoids appending and popping path values; recursion depth itself identifies which slot to overwrite.

The placeholder zeros have no semantic meaning. Even if zero is an actual input value, every slot is overwritten along a complete root-to-leaf path before a result is recorded. The algorithm never interprets an unfilled placeholder as a selected value; `vis` is the authoritative usage state.

After setting `vis[j] = True` and writing the value, `dfs(i + 1)` receives a state with one more filled position and one more used index, so the invariant is preserved. When the child returns, the code sets `vis[j] = False`. It does not clear `t[i]`, and that is safe: the next sibling choice overwrites the same slot before descending, and no snapshot is taken until all positions are filled.

**Why a copy is required at a leaf**

When `i >= n`, all $n$ positions have been assigned and every input index is used exactly once. The current `t` is therefore a valid permutation. The code appends `t[:]`, not `t` itself.

All branches reuse one mutable path array. If the result stored the original object, later overwrites would change earlier answers, eventually making every result entry show the same final contents. Slicing creates an independent $n$-element snapshot for that leaf.

The immediate `return` prevents a complete permutation from being extended. There are no unused indices anyway, but returning states the base case clearly and avoids entering another loop.

**A trace for three values**

For `[1, 2, 3]`, the root first selects index 0, so `t[0] = 1`. The next depth can select index 1 and then index 2, recording `[1, 2, 3]`. Backtracking clears only index 2's used flag, allowing it to replace the second position and eventually record `[1, 3, 2]`.

After all permutations beginning with 1 are finished, the root clears index 0's flag and selects index 1, generating the permutations beginning with 2. The Boolean restoration is what ensures each sibling branch starts with exactly the usage state of its parent.

**Why every permutation appears exactly once**

Every recorded list has length $n$, and the usage invariant ensures it contains each input index exactly once. Therefore, every result is a valid permutation.

For completeness, take any desired permutation. At depth 0, the loop eventually selects the index of its first value. At depth 1, that index is marked but the desired second index remains available, so the loop can select it. Repeating this argument follows a unique root-to-leaf path matching the entire ordering.

For uniqueness, two different search paths first differ at some depth where they choose different unused indices. Since input values are distinct, the resulting permutations differ at that position. No two leaves can therefore produce the same value sequence.

## Complexity detail

There are $n!$ output permutations, each containing $n$ values. Copying the path at every leaf alone costs $\Theta(n \cdot n!)$ time. The internal search also loops over up to $n$ indices at its states, which remains within the same conventional $O(n \cdot n!)$ bound. This matches the manifest and is asymptotically optimal with respect to the size of the required output.

Excluding the returned answers, `vis`, `t`, and the recursion stack each use $O(n)$ space, so auxiliary space is $O(n)$. The output itself contains $n!$ lists with $n$ entries and therefore occupies $\Theta(n \cdot n!)$ space. Output storage is conventionally excluded from the auxiliary-space claim but cannot be avoided by a method that returns all permutations.

## Alternatives and edge cases

- **Append/pop path:** Maintain a variable-length list instead of preallocating `t`. This is equally correct and makes filled length visible directly, while the selected source avoids repeated path resizing.
- **In-place swapping:** At depth `i`, swap each suffix value into position `i`, recurse, and swap back. It removes the visited array but mutates the input temporarily and requires careful restoration.
- **Pass a sliced remaining list:** Recurse with all elements except the chosen one. The state is intuitive but repeated slicing and path concatenation increase allocation and copying costs.
- **Iterative next-permutation generation:** Sort the values and repeatedly transform to the next lexicographic permutation. It uses constant path overhead but mutates order and requires a separate snapshot for every result.
- **One input value:** The only branch fills position 0 and records the one-element permutation.
- **Placeholder zero:** It cannot leak into an answer because a leaf is reached only after every path slot has been assigned.
- **Distinctness guarantee:** If duplicate values were allowed, different index paths could produce identical value sequences. That separate problem needs depth-level duplicate suppression.
- **Input preservation:** The solution reads `nums` without swapping or sorting it, so the caller's array is unchanged.
- **Any output order:** Depth-first order follows the original input ordering, but the contract accepts any order.
