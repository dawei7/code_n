## General

**Lexicographic sorting puts descendants beside their ancestor**

A subfolder path begins with its parent path followed by a slash. If the path list is sorted lexicographically, every string beginning with a fixed parent prefix appears in one contiguous block immediately after that parent.

For example, sorting `"/a"`, `"/a/b"`, `"/a/b/c"`, and `"/c"` keeps the `"/a"` family together before `"/c"`. This means a single left-to-right pass can discard the entire descendant block.

The exact source sorts `folder` in place and initializes `ans` with the first path. The input is guaranteed nonempty, so `folder[0]` is safe.

**Only compare with the last path that survived**

For each later path `f`, the method compares it with `ans[-1]`, the most recently retained top-level folder. If `f` is a subfolder of that retained path, it is skipped and `ans[-1]` remains unchanged. This is important: deeper descendants are still compared with the original surviving ancestor rather than with a skipped intermediate folder.

If `f` is not a descendant, it is appended and becomes the relevant candidate ancestor for the next sorted paths.

Why is checking only the last retained path sufficient? Suppose `f` had some earlier retained parent. All strings with that parent prefix form a contiguous sorted block. No unrelated retained path could appear between the parent and `f` while still allowing `f` to have that prefix. Therefore, that parent would still be the last retained path.

**The exact boundary test**

Let `m = len(ans[-1])` and `n = len(f)`. A proper subfolder must be longer than its parent, must share the entire parent prefix, and must have `'/'` immediately after that prefix.

The code appends `f` when any part of that condition fails:

`m >= n or not (ans[-1] == f[:m] and f[m] == '/')`.

If `m >= n`, `f` cannot be a proper descendant of `ans[-1]`. This branch also protects the later `f[m]` access from running beyond the current string.

If `m < n`, `f[:m]` extracts the prefix of the parent’s length. Equality checks whether the textual prefix matches. Then `f[m] == '/'` verifies a path-component boundary.

The slash test prevents a false relationship such as treating `"/a/b/ca"` as a subfolder of `"/a/b/c"`. The shorter string is a character prefix, but the next character is `'a'` rather than a slash, so both paths survive.

**Walking through the first example**

After sorting, the order is `"/a"`, `"/a/b"`, `"/c/d"`, `"/c/d/e"`, `"/c/f"`.

- `"/a"` starts the result.
- `"/a/b"` begins with `"/a/"`, so it is skipped.
- `"/c/d"` does not begin with `"/a/"`, so it is retained.
- `"/c/d/e"` begins with `"/c/d/"`, so it is skipped.
- `"/c/f"` does not begin with `"/c/d/"`, so it is retained.

The result is `["/a", "/c/d", "/c/f"]`.

**Why sorting proves global removal**

Maintain the invariant that `ans` contains exactly the non-subfolders among all processed sorted paths, and `ans[-1]` is the only processed path that could be a parent of the next path.

The invariant holds for the first path. For a new `f`, the prefix-and-slash test is exact. If it is a descendant, skipping it preserves the set of top-level folders. If it is not, no earlier retained folder can be its parent by sorted contiguity, so appending it is correct. Induction proves that the final result contains all and only folders with no listed ancestor.

**Order and input mutation**

The output is returned in sorted order, which is allowed because the contract permits any order. `folder.sort()` changes the caller’s list order. The strings themselves are immutable and unchanged.

The loop uses `folder[1:]`, which creates a new list of references to all paths after the first. This affects practical auxiliary memory but not the main algorithmic idea.

## Complexity detail

Let \(n\) be the number of paths and \(L\) their maximum length. Sorting makes \(O(n\log n)\) comparisons, each potentially inspecting \(O(L)\) characters, for \(O(nL\log n)\) time. The scan performs prefix slicing and comparison costing \(O(L)\) per path, or \(O(nL)\), which does not dominate sorting.

The answer can contain \(n\) references, Python sorting may use \(O(n)\) temporary references, and `folder[1:]` creates another \(O(n)\)-reference list. Thus auxiliary reference space is \(O(n)\), excluding returned output if desired. Counting character storage of newly created prefix slices over time does not exceed \(O(L)\) live per iteration, while the original strings are reused.

## Alternatives and edge cases

- **Use `startswith(parent + "/")`:** This expresses the boundary rule directly and avoids manual length/index logic, with the same asymptotic scan cost.
- **Set of all folders:** For each path, repeatedly remove the final component and test ancestors in a set. It avoids sorting but can take \(O(nL^2)\) with repeated string operations.
- **Trie by path components:** Insert folder names into a prefix tree and stop below terminal nodes. It can run in \(O(nL)\) expected time but uses more structures and memory.
- **Similar textual prefixes:** `"/a/b/c"` is not a parent of `"/a/b/ca"` because no slash follows the prefix.
- **Deep descendants:** After a parent is retained, all nested paths beneath it are skipped while the parent remains `ans[-1]`.
- **No subfolders:** Every path fails the parent test and all are returned.
- **One input folder:** It initializes the answer and the sliced loop is empty.
- **Unique path guarantee:** Exact duplicates do not occur. If they did, the `m >= n` branch would retain both duplicates.
- **In-place sorting:** Callers that need the original order should pass a copy. The exact implementation intentionally mutates the list.
- **Slash indexing safety:** Short-circuit evaluation handles `m >= n` before accessing `f[m]`, preventing an out-of-range read.
