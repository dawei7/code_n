## General

**Separate the problem into length and existence**

For a fixed length `L`, it is straightforward to ask whether any substring of length `L` appears at least twice. The harder part is choosing the largest successful length.

The existence predicate is monotone:

- If a duplicate substring of length `L` exists, taking the same prefix of both occurrences gives a duplicate of every shorter length.
- If no duplicate of length `L` exists, no longer duplicate can exist, because any longer duplicate would contain a duplicated length-`L` prefix.

The successful lengths therefore form a prefix `0, 1, ..., L_{\max}`. Binary search can find `L_{\max}` without checking every length.

**Check one length with a set**

The nested function `check(l)` slides a window of length `l` over every legal start `i` from zero through `n - l`.

The slice `s[i:i + l]` creates the current substring `t`. The set `vis` contains all length-`l` substring values seen at earlier starts.

If `t in vis`, the same character sequence occurs at the earlier start and at `i`, so `check` returns `t` immediately. Otherwise, it adds `t` and continues.

If every window is unique, it returns the empty string. Because checked lengths are positive, an empty string is an unambiguous “not found” signal.

Python sets use hashes to locate candidates but confirm equality, so a normal hash collision between two different strings does not create an incorrect duplicate result.

**Overlapping occurrences are naturally allowed**

The window advances by one position and does not remove earlier strings from `vis`. Two equal windows may overlap in the original string.

For example, `"aaaa"` contains `"aaa"` at starts zero and one. Both slices are inserted and compared as ordinary values, so the second occurrence is detected. No non-overlap condition is imposed because the source explicitly permits overlap.

**Binary-search boundaries**

`left = 0` is always feasible because the empty-length baseline needs no duplicate evidence. `right = n` is a safe upper bound; the whole string occurs only once, so length `n` normally fails.

While `left < right`, the code chooses

`mid = (left + right + 1) >> 1`.

Right shift by one divides by two, and the added one selects the upper midpoint. The upper midpoint is important when the interval has two adjacent values: a successful check can assign `left = mid` and still make progress.

If `check(mid)` returns a nonempty duplicate, length `mid` is feasible, so `left = mid` keeps it and discards smaller uncertainty.

If it returns empty, `mid` and all longer lengths are impossible, so `right = mid - 1`.

At termination, `left == right == L_{\max}`.

**Why `ans = t or ans` works**

Whenever a tested length succeeds, `t` is an actual duplicated substring of that length. The expression replaces `ans` with `t`.

Whenever a test fails, `t` is empty, so Python's `or` retains the previous successful answer.

Binary search only moves `left` upward on success. Therefore, successful tested lengths increase over time, and every replacement of `ans` is at least as long as its previous value. When the search ends, `ans` is a duplicate of the maximum feasible length.

If every positive length fails, `ans` remains empty, which is the required result.

**Trace `"banana"`**

Length three succeeds because windows include `"ana"` at starts one and three. The occurrences overlap at one character, which is allowed.

Longer candidate lengths fail: no length-four substring appears twice. Binary search narrows its bounds until three is the largest feasible length and returns `"ana"`.

Other strings could have several different longest duplicates. `check` returns the first one encountered twice, and the problem accepts any.

**Trace a string with no repeated character**

For `"abcd"`, every positive-length duplicate check eventually fails. In particular, length one windows `a`, `b`, `c`, and `d` are all distinct.

Binary search reduces `right` to zero. Since no call produced a nonempty `t`, `ans` is `""`.


If `check(l)` returns a string, it saw that exact value in `vis` from an earlier window and sees it again at the current start. It is a valid duplicated contiguous substring of length `l`.

If it returns empty, every length-`l` window was inserted once and none equaled an earlier window. No duplicated substring of that length exists.

Combining this exact predicate with the monotonicity proof makes the binary-search result correct.

**What the exact implementation does differently from Rabin-Karp**

The local editorial's intended high-performance checker uses rolling hashes so moving one character updates a window fingerprint in constant time. The exact solution instead materializes every Python substring and stores full strings.

That choice is collision-safe and very concise, but slicing and initially hashing a length-`L` Python string take `O(L)` time. The approach remains logically correct; its concrete Python resource bounds are weaker than the rolling-hash target in the manifest.

## Complexity detail

Let `N = len(s)`. Binary search performs `O(\log N)` calls to `check`.

Under the abstract constant-time-substring or rolling-hash model, each check scans `O(N)` windows, giving the manifest's `O(N \log N)` time and `O(N)` stored fingerprints.

For the exact Python source, a check at length `L` creates and hashes up to `N - L + 1` strings of length `L`. Its expected time is `O((N - L + 1)L)` and its peak stored character volume is the same order. Across binary-search iterations, a conservative exact bound is `O(N^2 \log N)` time and `O(N^2)` peak space, with many inputs doing less. Hash-table collision pathologies can make worst-case lookup behavior weaker still.

Thus the manifest describes the intended rolling-hash realization, while the protected implementation shown here is a simpler full-substring realization. The binary-search logic is identical in both.

## Alternatives and edge cases

- **Binary search plus rolling hash:** Maintain each length-`L` window hash in constant time and store hashes or hash buckets. This reaches `O(N \log N)` expected time and `O(N)` space, but exact substring verification is needed to eliminate collision risk.
- **Double rolling hash:** Two independent moduli make accidental collision extremely unlikely, though deterministic equality verification remains the strongest guarantee.
- **Suffix array plus longest common prefix:** Sort suffixes and find the largest LCP between adjacent suffixes. Typical implementations use `O(N \log N)` time and `O(N)` space without binary searching lengths.
- **Suffix automaton or suffix tree:** These can solve the problem in linear time with sophisticated construction and larger implementation complexity.
- **Check lengths from largest downward:** It may stop early but takes quadratic or worse work when the answer is short. Monotonicity supports binary search.
- **No duplicate characters:** Even length one fails, so the answer is empty.
- **All characters equal:** The longest duplicate has length `N - 1`, with occurrences starting at zero and one.
- **Overlapping duplicates:** They are valid and detected because all starting positions are considered.
- **Several longest answers:** Returning the first repeated slice found at the maximum length satisfies the “any” requirement.
- **Whole-string length:** Length `N` has only one window and cannot be duplicated within the same string.
- **Upper-midpoint formula:** The `+1` prevents an infinite loop when `left + 1 == right` and `mid` succeeds.
- **Empty answer sentinel:** Checks occur only for positive lengths, so `""` cannot be confused with a successful substring.
- **Input size:** At `N = 30000`, full substring materialization can be expensive; rolling hash or suffix-array machinery is the practical asymptotic choice.
- **Python hash behavior:** Sets verify string equality after hash matches, so ordinary hash collisions affect performance rather than correctness.
