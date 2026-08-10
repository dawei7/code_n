## General

**See a partition as a sequence of cut decisions**

A valid answer divides the original string into contiguous, nonempty pieces, and every piece must read the same from left to right and right to left. The characters cannot be reordered or skipped.

If the next unused character is at index `i`, then the first piece of the remaining suffix must be exactly one of:

- `s[i : i + 1]`,
- `s[i : i + 2]`,
- and so on through `s[i : n]`.

The algorithm tries every possible ending index `j` for that next piece, but recurses only when `s[i : j + 1]` is a palindrome. This is backtracking: choose one legal piece, solve what remains, and undo the choice before trying the next ending.

Checking each candidate by scanning or reversing it would repeat the same palindrome work in many branches. The solution first creates a table `f` so every later check is constant time.

**What the palindrome table represents**

For indices with $0 \le i \le j < n$, `f[i][j]` means that the inclusive substring from `s[i]` through `s[j]` is a palindrome.

A substring is palindromic exactly when:

1. its first and last characters are equal; and
2. the substring strictly between them is also a palindrome.

The code expresses that rule as `s[i] == s[j] and f[i + 1][j - 1]`.

The table is initially filled with `True`, including entries on and below the diagonal. This initialization supplies both base cases without separate branches:

- `f[i][i]` stays `True`, because one character is a palindrome;
- for a two-character substring, the recurrence reads `f[i + 1][i]`, an entry below the diagonal representing an empty interior, and that entry is `True`.

For a longer substring, the interior is a genuine shorter substring. A mismatch at the two ends makes the result false immediately; matching ends defer the answer to that already computed interior.

Rows are processed from right to left: `i` decreases from `n - 1` to `0`. Within a row, `j` increases from `i + 1`. When the formula for `f[i][j]` reads `f[i + 1][j - 1]`, row `i + 1` has already been processed. Thus every dependency is ready before it is used.

For `"aab"`, the table marks `"a"`, the second `"a"`, `"b"`, and `"aa"` as palindromes. It rejects `"ab"` and `"aab"`.

**What one recursive call promises**

The list `t` contains palindromic pieces that concatenate to exactly `s[0:i]`. This is the state carried by `dfs(i)`.

Initially, `i` is zero and `t` is empty, so the promise holds. At a candidate ending `j`, the branch is entered only if `f[i][j]` is true. Appending `s[i : j + 1]` therefore adds a palindromic piece, and its characters begin exactly where the previous pieces stop. Calling `dfs(j + 1)` preserves the promise for the longer prefix.

When `i == n`, the chosen pieces cover every character exactly once, in order, and every piece was table-approved. The current list is consequently a valid complete partition.

The code appends `t[:]`, not `t` itself. This shallow copy freezes the current sequence of string references. Without the copy, all result entries would refer to the same mutable list, and later `pop` operations would erase or change previously recorded answers.

After returning from a recursive branch, `t.pop()` removes exactly the piece that branch appended. Restoring `t` is what permits the loop to test a different ending `j` from the same index without retaining an unrelated earlier choice.

**Why every answer appears exactly once**

Every valid partition has a unique first piece, and therefore a unique first ending index `j`. The loop tries that endpoint. Because the piece is palindromic, its table entry is true, so the algorithm enters the matching branch. Applying the same argument to the remaining suffix shows that the complete partition is eventually recorded.

No invalid partition is recorded because recursion never appends a non-palindrome, never overlaps pieces, and records only after consuming all $n$ characters.

No valid partition is duplicated. Two different recursion paths differ at the first cut where they select different ending indices, so the resulting ordered lists of substrings are different.

The result order follows depth-first traversal with shorter next pieces tried first. The contract does not require a particular outer order.

## Complexity detail

Let $n$ be the string length. Let $L$ denote the total materialized size of all returned partitions, including their substring characters and list entries.

The table contains $n^2$ Boolean entries and its nested loops perform $O(n^2)$ constant-time comparisons. During enumeration, each completed partition must be constructed and copied into the answer. Python slicing also copies the chosen substring. Across all explored branches, this work is output-sensitive and is accounted for by $L$. The total time is therefore $O(n^2 + L)$, matching the manifest.

The palindrome table uses $O(n^2)$ memory. The recursion depth is at most $n$, reached when every piece is one character, and `t` holds at most $n$ pieces. Excluding the returned answer, auxiliary space is $O(n^2+n)$, customarily simplified to $O(n^2)$. The result itself requires $O(L)$ storage and cannot be avoided because the function must return every partition.

The number of partitions can be exponential. If every character is the same, every one of the $n-1$ gaps may independently contain a cut or not, producing $2^{n-1}$ answers. The constraint $n \le 16$ makes exhaustive output feasible, but no algorithm can run in polynomial time when it must explicitly return exponentially many distinct results.

## Alternatives and edge cases

- **Backtracking with direct palindrome scans:** Test each chosen substring using two pointers instead of precomputing `f`. It uses less table memory, but repeated checks add avoidable work across branches.
- **Memoized palindrome predicate:** Cache `isPalindrome(i, j)` results on demand. It can avoid filling never-requested entries, although this enumeration eventually requests many intervals and the recursive logic is less direct.
- **Center expansion plus cut graph:** Expand around every odd and even center to record palindrome intervals, then enumerate paths through those intervals. It has the same broad complexity but organizes preprocessing differently.
- **Bottom-up suffix partitions:** Build all valid partitions for suffixes from right to left. It removes the recursive call stack but can retain exponentially many intermediate lists for multiple suffixes.
- **Dynamic programming for only the minimum cuts:** That related problem stores an optimum count rather than all partitions. It cannot solve this contract because returning one best partition would omit valid answers.
- **One-character input:** Its diagonal table entry is already true, so the only branch records `["a"]` or the corresponding single character.
- **All equal characters:** Every substring is a palindrome, producing the maximum branching and all $2^{n-1}$ cut patterns.
- **No multi-character palindromes:** The single-character branch is always legal, so at least one complete partition exists and consists of individual characters.
- **Even-length palindromes:** The below-diagonal `True` base handles two equal adjacent characters correctly; no special parity case is needed.
- **Mutable path aliasing:** Replacing `ans.append(t[:])` with `ans.append(t)` would be wrong because all answers would share the same list being backtracked.
- **Runtime dependency:** The selected source uses `List` in annotations without importing it. A standalone module needs `from typing import List` unless the harness injects that name.
