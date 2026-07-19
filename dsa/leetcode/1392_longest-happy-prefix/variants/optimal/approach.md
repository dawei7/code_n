## General
**Record the best border ending at every position.** Build the prefix-function array used by Knuth-Morris-Pratt string matching. For each position `i`, let `prefix[i]` be the length of the longest prefix of `s` that equals a suffix of `s[:i + 1]` and is shorter than that substring.

Begin with the candidate length `prefix[i - 1]`. If `s[i]` does not extend that candidate, replace the candidate by `prefix[candidate - 1]`, which is the next-longest border of the already matched prefix. Continue through this chain until the new character matches or the candidate becomes zero. A match extends the border by one.

Every fallback remains a possible border because a border of a border is also a border of the current prefix. Any skipped length cannot work: it is not itself a border of the portion already matched. Thus the final value at each position is the longest valid border there. At the last position, `prefix[n - 1]` is exactly the longest proper prefix that is also a suffix of the complete string; return that many leading characters.

## Complexity detail
Although a mismatch can trigger several fallbacks, each successful extension increases the candidate length and the total number of decreases across the scan is $O(n)$. The prefix function is therefore built in $O(n)$ time. Its $n$ integer entries use $O(n)$ space.

## Alternatives and edge cases
- **Test every prefix length:** Comparing every prefix with the corresponding suffix is simple but requires $O(n^2)$ character work in the worst case.
- **Rolling hash:** Prefix and suffix hashes can find matching lengths in $O(n)$ expected time, but collision avoidance requires either verification or multiple robust hashes.
- **Whole string:** The prefix function always describes a proper border, so the complete string is never returned.
- **Single character:** It has no nonempty proper prefix, so the result is `""`.
- **Repeated characters:** For `"aaaaa"`, the answer is `"aaaa"`; overlapping prefix and suffix occurrences are allowed.
- **No border:** Return the empty string rather than an arbitrary character or the whole input.
