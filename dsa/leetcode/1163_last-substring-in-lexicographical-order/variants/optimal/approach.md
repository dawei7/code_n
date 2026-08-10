## General

**The maximum substring must extend to the end**

Consider any substring that starts at index `p` but stops before the end of `s`. The suffix `s[p:]` has that substring as a prefix and then contains additional characters. Under lexicographic ordering, a string is smaller than a longer string when it is a proper prefix of the longer one.

Therefore, extending a candidate substring to the end never makes it smaller and makes it strictly larger when the original stopped early. The answer must be one of the `n` suffixes of `s`.

The problem is now to find the lexicographically greatest suffix without constructing and sorting all suffix strings.

**Maintain two suffix starts and one matched length**

`i` is the start of the best surviving candidate, `j` is the start of another suffix being compared with it, and `k` is the number of equal characters already matched:

`s[i : i + k] == s[j : j + k]`.

Initially, suffix zero is the candidate, suffix one is the challenger, and no characters have been compared, so `i = 0`, `j = 1`, and `k = 0`.

The two starts remain distinct, with the challenger arranged after the candidate search boundary. The loop continues while `j + k < len(s)`, meaning the challenger still has a character available at the comparison offset.

**Advance across a shared prefix**

If `s[i + k] == s[j + k]`, those characters do not decide lexicographic order. The code increments `k` and compares the next pair.

No pointer is eliminated until the first differing character is found or the challenger reaches the end.

**Eliminate a losing block of starts**

Suppose the first mismatch satisfies

`s[i + k] < s[j + k]`.

The suffix beginning at `j` is larger than the suffix beginning at `i` because their first `k` characters match and the challenger's next character is larger. Start `i` cannot be the answer.

The comparison also permits skipping the next `k` starts after `i`. This is the central elimination lemma of the maximum-suffix two-pointer algorithm: after two suffixes share a length-`k` prefix and the first loses at the next character, none of the starts inside that losing matched block can beat the winning suffix. Keeping them would only repeat alignments already shown to belong to the losing region.

Thus the code advances

`i += k + 1`

and resets `k` to zero for a fresh comparison. If this advancement reaches or passes `j`, the old challenger is no longer strictly ahead of the new candidate position, so `j = i + 1` restores two distinct ordered starts.

The symmetric case occurs when

`s[i + k] > s[j + k]`.

Now the challenger loses, and starts `j` through `j + k` can all be discarded. The code uses `j += k + 1` and resets `k`.

Skipping an entire matched-and-losing block, rather than moving only one position, is what prevents repeated quadratic comparisons.

**Handle a challenger that runs out**

If the loop stops because `j + k == len(s)`, the challenger suffix ended while all compared characters were equal. Since `i < j` at that comparison stage, the suffix at `i` has at least the same matched text and extends farther. The shorter challenger is a prefix of the longer candidate and is therefore lexicographically smaller.

No update is needed; `i` remains the winning surviving start.

**Trace `abab`**

The candidate begins at zero with `"abab"`, while the challenger at one is `"bab"`. Their first characters differ, and `"a" < "b"`, so start zero loses. `i` advances to one, and `j` is moved to two.

Comparing suffix `"bab"` at one with `"ab"` at two, the candidate's first `"b"` is larger, so start two is discarded and `j` moves to three.

Suffixes at one and three both begin with `"b"`. After matching that character, the challenger reaches the end. It is `"b"`, a proper prefix of `"bab"`, so start one remains and `s[1:]` is returned.

**Why the algorithm is correct**

At every mismatch, direct lexicographic comparison identifies one suffix as smaller. The elimination lemma discards that losing start and the starts within its already matched losing block, none of which can be the global maximum. At least one proven-better candidate remains.

Pointers only pass over starts that have been eliminated by such a comparison. When the process terminates, every suffix start other than `i` has either lost directly, lies in a losing skipped block, or is the exhausted challenger that is a shorter prefix. Therefore, the suffix at `i` is at least as large as every other suffix.

Since the largest substring must be a suffix, returning `s[i:]` gives the requested last substring in lexicographical order.

## Complexity detail

Let `n` be `len(s)`. Equal-character comparisons increase `k`. At a mismatch, one of the starts advances by `k + 1`, skipping the block just compared, and `k` resets. Across the whole algorithm, these pointer advances and matched offsets account for only `O(n)` amortized comparisons. The search time is `O(n)`.

The final slice `s[i:]` also copies up to `O(n)` characters in Python, which remains within the overall `O(n)` time.

The search itself stores only three indices and uses `O(1)` auxiliary space. The returned string occupies `O(n)` output space in the worst case; the manifest's `O(1)` space convention excludes required output storage. Under a convention that counts the allocated return slice, peak additional storage is `O(n)`.

## Alternatives and edge cases

- **Generate and sort all suffixes:** Constructing suffix strings can use quadratic total characters, and comparison sorting adds substantial time.
- **Compare every suffix against the current best directly:** Repeated long common prefixes can lead to `O(n^2)` character comparisons.
- **Suffix array:** A suffix array can identify the lexicographically last suffix, but general construction machinery and extra storage are unnecessary for this single maximum query.
- **Booth or Duval-style algorithms:** Related linear string algorithms use similar block elimination. The exact two-pointer form is specialized to the maximum suffix.
- **One-character string:** The loop never runs and the complete string is returned.
- **All characters equal:** The later suffix remains a shorter prefix of the first suffix, so index zero wins.
- **Strictly increasing characters:** Each larger character replaces the candidate, and the answer begins at the final character.
- **Repeated long prefixes:** `k` skips through them, while block jumps preserve linear amortized work.
- **Candidate and challenger must differ:** When advancing `i` crosses `j`, resetting `j = i + 1` avoids comparing a suffix with itself.
- **Proper-prefix rule:** If the challenger ends after matching, the longer candidate is lexicographically greater.
- **Returned slice allocation:** Python materializes `s[i:]`. It is output storage rather than search state, but complexity discussions should state the convention.
