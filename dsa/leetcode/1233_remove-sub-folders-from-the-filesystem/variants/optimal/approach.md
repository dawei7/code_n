## General
**Place every parent immediately before its descendants.** Sort the paths lexicographically. If one path is a sub-folder of another, the parent sorts first, and all strings beginning with the parent plus `"/"` form one consecutive block after it. Sorting therefore turns a global ancestor search into a comparison with the most recently retained path.

**Retain only new top-level blocks.** Scan the sorted list. Keep the first path. For each later `path`, test `path.startswith(result[-1] + "/")`. When that is true, the path is below the last retained folder and must be discarded. Otherwise, it cannot be below any earlier retained folder: any earlier prefix block would still contain `path` before lexicographic order moved on to `result[-1]`. Append it as the next top-level folder.

**Include the component boundary.** Testing the retained path alone would incorrectly treat `"/a/bc"` as a child of `"/a/b"`. Adding `"/"` to the candidate parent exactly matches the definition of a sub-folder. Every discarded path has a retained ancestor, while every retained path has been shown not to belong to any earlier ancestor block, so the result contains exactly the required folders.

## Complexity detail
Comparing two paths takes at most $O(L)$ time. Lexicographic sorting uses $O(n\log n)$ comparisons, and the subsequent prefix scan takes $O(nL)$ time, for an overall bound of $O(nL\log n)$. The sorted array and returned references require $O(n)$ auxiliary slots; path strings themselves are reused.

## Alternatives and edge cases
- **Compare every pair of paths:** Checking each folder against every possible parent is straightforward and exact but takes $O(n^2L)$ time.
- **Trie of path components:** A trie can stop below any terminal folder in $O(S)$ character work, but it needs a larger node structure and traversal logic.
- **Hash every ancestor:** Splitting each path and probing all component prefixes is correct, though repeated prefix construction can add considerable string work.
- **Similar textual prefixes:** `"/a"` is not a parent of `"/ab"`; the required slash boundary prevents this false match.
- **Deep chain:** When every path descends from the shortest one, only that shortest root remains.
- **Single path:** With no possible listed parent, the sole folder is returned.
- **Input order:** The original order does not affect membership, and the contract permits the sorted result order.
