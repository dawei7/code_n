## General

**Generate only valid prefixes in dictionary order**

A happy string uses only `a`, `b`, and `c`, and its next character must differ from its current last character. Backtracking fits this rule naturally: build one prefix, try every legal next character, and undo the choice when that branch is finished.

The exact implementation keeps the current prefix in mutable list `s`. A list supports constant-time append and pop at its end, avoiding a new full string for every recursive edge. Complete strings are created only at leaves with `"".join(s)`.

The nested `dfs` function closes over `n`, `k`, `s`, and `ans`. It needs no parameters because those values remain available from the enclosing call.

**The completion case**

The first condition is:

```python
if len(s) == n:
    ans.append("".join(s))
    return
```

Every prefix constructed by the recursion is already happy, so reaching length `n` means a valid result has been found. Joining creates an immutable snapshot. This is essential: appending the mutable list itself would allow later backtracking to change stored results.

The function returns immediately because a length-$n$ string must be recorded, not extended.

**Prune once enough strings have been reached**

The next condition is:

```python
if len(ans) >= k:
    return
```

Once at least `k` complete strings are stored, any not-yet-complete prefix belongs after the kth discovered leaf and cannot change `ans[k - 1]`. Returning prevents expansion of that branch.

The completion condition appears before this pruning check. As a subtle result, after the kth leaf is appended, its parent at depth $n-1$ may call `dfs` for one remaining sibling leaf. That sibling also reaches the completion condition and can be appended, producing at most one immediately adjacent extra result. New incomplete branches are pruned, so this does not affect the kth element or cause full remaining traversal.

**Choose characters in lexicographical order**

For an incomplete prefix, the loop is:

```python
for c in "abc":
```

Python visits the characters as `a`, then `b`, then `c`. The condition

```python
if not s or s[-1] != c:
```

accepts every character for an empty prefix. Otherwise, it accepts exactly the two letters different from the last chosen letter. This enforces the happy condition at the only new adjacency created by appending `c`. Earlier adjacencies were already valid by the recursive invariant.

For each legal character, the code performs the standard three backtracking steps:

1. `s.append(c)` makes the choice.
2. `dfs()` explores every required completion beneath that prefix.
3. `s.pop()` undoes the choice so the next character starts from the same parent prefix.

The pop occurs even after pruning. Therefore, recursive returns never leak a character into a sibling branch.

**Why depth-first traversal is already sorted**

Lexicographical order compares strings at their first different position. The DFS fully explores the `a` child of a prefix before its `b` child, and fully explores `b` before `c`. Every completion under the `a` child is lexicographically smaller than every completion under `b` because they first differ at that next character. The same relationship holds recursively inside each child.

Consequently, leaves are appended to `ans` in sorted order. No separate sorting pass is needed.

For `n = 3`, the beginning of the traversal is:

```text
aba, abc, aca, acb, bab, bac, bca, bcb, cab, ...
```

The ninth appended leaf is `cab`, matching the example.

**How the final return distinguishes existence**

After `dfs()` finishes:

```python
return "" if len(ans) < k else ans[k - 1]
```

The problem numbers results from one, while Python lists use zero-based indexing, so the kth string is stored at `k - 1`.

If the full search ends with fewer than `k` leaves, no kth happy string exists and the function returns the empty string. The total possible count is $3 \cdot 2^{n-1}$ because the first position has three choices and every later position has two. The implementation does not calculate this formula explicitly; exhaustion of the DFS establishes the same fact.

**Why the algorithm is correct**

Every appended string has length $n$, uses only characters from `"abc"`, and was extended only by a character different from its predecessor. Thus every output candidate is happy.

Conversely, take any happy string of length $n$. Its first character is tried by the root loop, and at every later depth its next character differs from the prefix's last one, so its branch passes the condition. Unless the kth earlier string has already been found, DFS reaches and appends it. Pruned strings occur only after at least `k` lexicographically earlier leaves exist, so they cannot be the desired result.

Finally, the ordered character loop and depth-first completion guarantee leaf order is lexicographical. Therefore, `ans[k - 1]` is exactly the kth happy string whenever it exists.

## Complexity detail

Let $H = 3 \cdot 2^{n-1}$ be the total number of happy strings and let $r = \min(k,H)$. The traversal reaches roughly the first $r$ leaves, plus at most a small number of pruned sibling calls. Building each stored leaf with `join` costs $O(n)$. A safe bound for the exact implementation is therefore $O(nr)$ time.

The list `ans` stores up to about $r$ complete strings, each of length $n$, so it uses $O(nr)$ output-like storage. The current prefix and recursion stack each use $O(n)$.

Because the problem constrains `k <= 100`, `k` is a fixed small cap with respect to growth in `n`. Under that constraint-based convention, $r$ is bounded by a constant and both time and stored-string space simplify to $O(n)$, matching the manifest. If `k` is treated as an independent asymptotic variable, the more informative bounds are $O(n\min(k,H))$ time and space.

## Alternatives and edge cases

- **Combinatorial block skipping:** Each first-character block has $2^{n-1}$ strings, and each later legal-character block has a known power-of-two size. Selecting the block containing `k` constructs the result directly in $O(n)$ time without storing earlier strings.
- **Backtracking with a counter and one result:** Count completed leaves and stop exactly at the kth one. This retains lexicographical DFS but uses only $O(n)$ auxiliary space instead of storing the first `k` strings.
- **Generate everything then sort:** All happy strings can be enumerated and sorted, but DFS already emits sorted order, so sorting and full storage are unnecessary.
- **Breadth-first generation:** Expanding all valid strings level by level is intuitive but stores many prefixes and still needs ordered selection.
- **`n = 1`:** DFS appends `a`, `b`, and `c` in order. Values of `k` from one through three select them, while larger `k` returns empty.
- **`k` exceeds the total:** Pruning never activates, the complete happy-string tree is exhausted, and `len(ans) < k` returns the empty string.
- **Repeated adjacent letter:** The last-character check rejects the branch immediately, so no invalid complete string is ever generated.
- **Backtracking restoration:** Omitting `s.pop()` would leave a previous choice in the prefix and corrupt both lengths and sibling strings.
- **One-based rank:** The result uses `ans[k - 1]`, not `ans[k]`.
- **Extra leaf after reaching `k`:** Because completion is checked before pruning, one sibling leaf can still be appended. It appears after the kth leaf and does not change the returned value.
- **Lexicographical order:** Changing the loop to `"cba"` would generate reverse order and make the stored index incorrect.
