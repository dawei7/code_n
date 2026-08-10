## General

A substring appears in the infinite wraparound alphabet string exactly when every adjacent character advances by one alphabet position, treating `z -> a` as consecutive. For example, `"xyzab"` is valid, while `"xzy"` is not.

Enumerating all substrings would be quadratic, and storing their text would consume even more space. The optimal observation is that, for a fixed ending letter and a fixed length, there is only one possible string that follows the cyclic alphabet. Therefore it is enough to remember the longest valid substring ending at each letter.

**Track the current cyclic run**

`k` is the length of the longest valid wraparound substring ending at the current index.

For character `c = s[i]`, compare it with `s[i - 1]`. They are consecutive in the infinite base exactly when

$$
(\operatorname{ord}(c)-\operatorname{ord}(s[i-1]))\bmod26=1.
$$

If they are consecutive, every valid run ending at the previous character extends by `c`, so increment `k`. Otherwise, no length-two valid suffix crosses this boundary, and the longest valid substring ending here is just `c`, so reset `k = 1`.

Modulo 26 handles the wrap. For `z -> a`, the raw code difference is `-25`, and `-25 % 26` is `1` in Python. Ordinary steps such as `a -> b` also differ by one.

**Store the maximum length for each ending character**

`f[c]` records the greatest `k` seen at any occurrence of ending character `c`. Suppose `f['d'] = 4`. Then the valid cyclic suffixes ending at `d` have lengths one through four:

- length 1: `"d"`
- length 2: `"cd"`
- length 3: `"bcd"`
- length 4: `"abcd"`

All are substrings of the longest observed run because they are its suffixes.

There cannot be two different valid wraparound strings with the same ending letter and same length. Moving backward through the cyclic alphabet uniquely determines every preceding character. Thus a maximum length `L` for ending letter `c` represents exactly `L` distinct valid strings—one for each length from 1 through `L`.

If another occurrence of `c` ends a shorter run, it contributes no new text: all its possible suffix lengths are already covered by the longer run. This is why the update uses `max(f[c], k)` instead of adding `k` for every occurrence.

**Why summing maxima counts every unique substring once**

Every valid nonempty substring has one final character `c` and one length `ell`. It is counted in the `ell` choice among the first `f[c]` lengths. Different final characters cannot describe the same string, and for a fixed final character different lengths produce different strings. Hence the categories are disjoint.

Conversely, every length from one through `f[c]` is realized as a suffix of an observed valid run ending at `c`, so every unit included in the sum corresponds to a genuine substring of `s` that appears in `base`.

Therefore

$$
\sum_c f[c]
$$

is exactly the number of distinct qualifying substrings.

**Trace `"zab"`**

- At `z`, no predecessor exists, so `k = 1` and `f['z'] = 1`.
- `z -> a` is consecutive modulo 26, so `k = 2` and `f['a'] = 2`. These represent `"a"` and `"za"`.
- `a -> b` is consecutive, so `k = 3` and `f['b'] = 3`. These represent `"b"`, `"ab"`, and `"zab"`.

The sum is `1 + 2 + 3 = 6`, matching the six example substrings.

For `"cac"`, neither `c -> a` nor `a -> c` is consecutive. Each position has `k = 1`; maxima exist only for `a` and `c`, so the answer is two. Repeated `c` is not double-counted.

## Complexity detail

Let $n$ be the length of `s`. The loop visits each character once and performs constant-time arithmetic and dictionary operations, so expected time is $O(n)$.

The dictionary has at most 26 keys because input contains only lowercase English letters. Its size is therefore bounded by a constant, giving $O(1)$ auxiliary space. The loop does not create substrings, sets of substring text, or an expanded wraparound string.

Even though `defaultdict` is a hash table, the fixed alphabet makes both its capacity and total stored integer state constant with respect to $n$.

## Alternatives and edge cases

- **Generate every substring and test it:** There are $O(n^2)$ substrings, and storing unique text can require far more space.
- **Use a set of valid substring strings:** It deduplicates correctly but materializes potentially quadratic total character data.
- **Dynamic programming by start position:** Validity can be tracked, but deduplicating equal text from different occurrences remains difficult. Ending-letter maxima encode uniqueness directly.
- **`z -> a` transition:** Modulo 26 treats it as consecutive; a plain difference check would miss it.
- **Repeated same character:** `a -> a` is not consecutive, so the run resets to length one. Repeated occurrences contribute only one unique `"a"`.
- **Single character:** Its maximum is one and the answer is one.
- **Longer than 26 characters:** The infinite base repeats, so valid strings may contain repeated letters and may be arbitrarily long; `k` is not capped at 26.
- **Several occurrences of one ending letter:** Only the longest run matters because it contains all shorter valid suffixes for that ending letter.
- **Empty string outside the contract:** The exact loop would return zero, though the stated input is nonempty.
