## General

**Compute the statistic `f` exactly**

For one nonempty string `s`, `f(s)` is not the frequency of the most common character. It is the count of whichever character is lexicographically smallest.

The helper builds `Counter(s)`, then scans `ascii_lowercase` from `a` through `z`. The first character `c` whose count is nonzero is the smallest character present, and `cnt[c]` is returned through `next(...)`.

The nonempty-string guarantee ensures such a character always exists, so `next` cannot exhaust the generator.

For `"dcce"`, counts exist for `c`, `d`, and `e`. The alphabet scan reaches `c` first and returns its count two.

**Precompute every word's frequency once**

The query result compares one query statistic against all word statistics. Recomputing `f(w)` for every query-word pair would repeat the same word work many times.

The generator `f(w) for w in words` calculates each word value once. `sorted(...)` materializes those values in ascending order as `nums`.

After sorting, the words' original order and spelling are irrelevant; each query needs only to know how many numeric values are strictly greater than its own.

**Use an upper-bound binary search**

For query `q`, let `v = f(q)`. `bisect_right(nums, v)` returns the insertion position after every value less than or equal to `v`.

If that position is `p`, indices zero through `p - 1` do not satisfy the required strict inequality. Indices `p` through `n - 1` are all greater than `v`. Their count is

`n - p`.

That is exactly the expression `n - bisect_right(nums, f(q))`.

Using `bisect_left` would find the first value greater than or equal to `v` and would incorrectly count equal frequencies. The problem requires `f(query) < f(word)`, so only strict greater values qualify.

**Trace the second example**

Word frequencies for `"a"`, `"aa"`, `"aaa"`, and `"aaaa"` are one, two, three, and four. Thus `nums = [1, 2, 3, 4]`.

Query `"bbb"` has value three. The right insertion point is after three, at index three, leaving one greater word frequency.

Query `"cc"` has value two. Its right insertion point is index two, leaving values three and four, so the answer is two.

**Why the algorithm is correct**

The helper returns the exact statistic by choosing the first alphabet character present and its multiplicity. Therefore, `nums` contains precisely the `f` values of all words.

Sorting preserves the multiset of those values and places every value at most `v` before every value greater than `v`. The right-bisection boundary separates those two groups exactly. Subtracting it from the number of words counts all and only words whose statistic is strictly larger.

Applying the same argument independently to every query produces the required answer array in query order.

**The exact source differs from the manifest**

The local manifest states `O(S)` time and `O(1)` space. The constraints make every string length at most ten, so a bucket-count solution over the small possible frequency range can indeed achieve a linear aggregate bound with constant auxiliary storage apart from output.

The exact source does not use buckets. It stores all `W` word frequencies, sorts them, and binary-searches once per query. Its actual complexity must include those operations.

## Complexity detail

Let `W = len(words)`, `Q = len(queries)`, and let `S` be the total number of characters across all strings.

Computing all `f` values takes `O(S)` time because the alphabet scan is a fixed 26 steps per nonempty string and every string has at least one character. Sorting word frequencies takes `O(W log W)`. Each query performs a binary search in `O(log W)`, adding `O(Q log W)`.

The exact total time is

`O(S + W log W + Q log W)`.

`nums` stores `W` integers, so auxiliary space is `O(W)`. The returned answer list contains `Q` integers; if required output storage is counted, total additional space is `O(W + Q)`. The temporary counter contains at most 26 keys.

These bounds, rather than `O(S)` time and `O(1)` space, describe the protected Python source as written.

## Alternatives and edge cases

- **Compare every query with every word:** This takes `O(QW)` numeric comparisons after statistics are known. Sorting and bisection reduce the comparison phase.
- **Frequency buckets from one through ten:** Since strings have maximum length ten, count how many words have each `f` value and build suffix totals. This realizes linear processing and constant-size auxiliary buckets.
- **Find the smallest character with `min(s)`:** One can then call `count` for that character, but it scans the string twice. The counter computes all multiplicities in one main pass.
- **Use `bisect_left`:** It counts equal word frequencies, violating the strict comparison. `bisect_right` skips all equals.
- **All word frequencies equal the query:** The insertion point is at the end of that equal block, so none are counted.
- **Query value below every word value:** The right boundary may be zero, producing answer `W`.
- **Query value at the maximum:** No greater value remains, producing zero.
- **One-character strings:** Their smallest character occurs once, so `f = 1`.
- **Repeated smallest character:** Only its full frequency matters; larger characters do not affect `f`.
- **Query order:** The list comprehension evaluates queries in input order and preserves corresponding answer positions.
- **Manifest mismatch:** Sorting `W` values and storing `nums` prevent the exact implementation from having the advertised linear-time, constant-space bounds.
