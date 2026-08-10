## General

**Dynamic programming by the final chosen character**

A subsequence may skip characters, but it must retain their original order. When considering whether to append `s[i]` to an earlier ideal subsequence, only one feature of that subsequence affects legality: its last character. If the previous last character is `b`, appending the current character is allowed when:

$$
\left|\operatorname{ord}(\texttt{s}[i])-\operatorname{ord}(b)\right|\le k.
$$

The exact implementation defines `dp[i]` as the maximum length of an ideal subsequence that ends specifically at index `i` and includes `s[i]`. Every single character is an ideal subsequence, so all entries start at one.

**Remember the most useful index for each letter**

The dictionary `d` maps a lowercase letter to its most recent occurrence index among the processed prefix. At first, only `s[0]` has been processed, so `d = {s[0]: 0}`.

At index `i`, the code loops over all 26 characters in `ascii_lowercase`. It skips a candidate `b` if its alphabet distance from `s[i]` is greater than `k`. If `b` is close enough and appears in `d`, the algorithm can extend the ideal subsequence ending at `d[b]`:

```python
dp[i] = max(dp[i], dp[d[b]] + 1)
```

After testing every allowable preceding letter, it sets `d[s[i]] = i`.

At first glance, keeping only the latest occurrence of each letter might seem unsafe: perhaps an earlier occurrence had a longer DP value. Here, the latest occurrence always dominates. When another occurrence of the same letter arrives, alphabet distance zero is at most every allowed `k`, including `k = 0`. It can extend the ideal subsequence ending at the previous same letter, so its new DP value is at least the previous value plus one. Therefore, DP values for occurrences of a fixed letter strictly increase, and the latest index has the best value for that letter.

This dominance fact is the reason the dictionary can discard older indices without losing an optimal predecessor.

**Trace the decision for one character**

Consider `s = "acfgbd"` and `k = 2`. At character `c`, the previous `a` is two alphabet positions away, so the subsequence `"ac"` has length two. Character `f` cannot follow `c` because their distance is three, so its best may remain one.

Later, `b` can follow either `a` or `c` because both are within two positions. The algorithm checks every lowercase candidate that satisfies the distance constraint and selects the predecessor with the greatest stored DP. Finally, `d` can extend the best subsequence ending in `b`, producing `"acbd"` of length four.

The loop does not require adjacent characters in `s` to be compatible. It only connects the current index to an earlier chosen endpoint, which is exactly how subsequences skip unwanted positions.

**Why alphabet order is not cyclic**

The code compares ordinary character codes with `abs(a - ord(b))`. Thus, `'a'` has code distance `25` from `'z'`, not distance one. This matches the statement's non-cyclic alphabet rule.

Using `ascii_lowercase` also bounds the predecessor loop to the exact allowed character domain. There is no wraparound calculation.

**Why the transition is correct**

Any ideal subsequence ending at index `i` either contains only `s[i]`, giving length one, or has some previous selected index `j < i`. Its prefix through `j` is an ideal subsequence ending at `j`, and the last two selected characters must have alphabet distance at most `k`.

For the letter `b = s[j]`, the dictionary's latest stored occurrence has a DP value at least as large as any earlier occurrence of `b`. The loop considers `b` because it satisfies the same alphabet-distance test and offers `dp[d[b]] + 1`. Therefore, the transition achieves at least the length of every valid candidate ending at `i`.

Conversely, every transition the code accepts starts from an already ideal subsequence and appends a character whose distance from its last letter is within `k`. It constructs a valid ideal subsequence, so `dp[i]` cannot overstate what is achievable. Hence `dp[i]` is exact.

Every nonempty ideal subsequence ends at some array index. Taking `max(dp)` after all positions returns the global longest length. The variable `ans = 1` is initialized but never used by the exact implementation; the final maximum over `dp` supplies the result.

**Why updating `d` happens after transitions**

The current index must not be its own predecessor. The loop reads only indices stored from the processed prefix, then writes `d[s[i]] = i` afterward. This preserves strict subsequence index order.

## Complexity detail

Let $n$ be the length of `s` and let $L=26$ be the lowercase alphabet size. For each of the $n-1$ positions after the first, the code scans all $L$ letters and does constant-time work. Time is $O(nL)$, which simplifies to $O(n)$ because $L$ is fixed at 26.

The dictionary stores at most 26 entries. However, the exact `dp` list contains one integer for every string position, so its auxiliary space is $O(n)$. The manifest's $O(1)$ space describes the logically compressed variant that stores one best length per letter directly; it is not the operational bound of this source file.

Returning `max(dp)` performs another $O(n)$ scan, which does not change the linear total.

## Alternatives and edge cases

- **Best length per letter:** Store a 26-entry array where each slot is the best ideal-subsequence length ending in that letter. This removes the $n$-entry DP list and achieves $O(1)$ auxiliary space.
- **Range maximum data structure:** For a much larger alphabet, query the character-code interval within distance `k` using a segment tree. With only 26 letters, scanning the alphabet is simpler.
- **Quadratic predecessor scan:** Checking every earlier index for every current index is correct but takes $O(n^2)$ time.
- **`k = 0`:** Only equal adjacent selected letters are allowed. Latest-occurrence DP chaining computes the maximum frequency of a single character.
- **`k = 25`:** Every lowercase pair is compatible, so the entire string is ideal and the answer is `n`.
- **One-character string:** `dp = [1]`, the loop is empty, and `max(dp)` returns one.
- **Repeated same letter:** Each new occurrence extends the previous best for that letter, justifying replacement in `d`.
- **Non-cyclic boundary:** `'a'` and `'z'` differ by 25 and are compatible only when `k = 25`.
- **Subsequence skipping:** Incompatible source characters can be ignored; only the last selected character constrains an append.
- **Unused `ans` variable:** It does not influence the result; `max(dp)` is the actual final aggregation.
