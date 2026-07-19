## General
Because characters may be added only at the front, the portion of `s` that remains centered against itself must be a prefix. The fewer characters added, the longer that already-palindromic prefix must be. The core task is therefore to find the longest prefix of `s` that is a palindrome.

Let $r = \operatorname{reverse}(s)$ and build

`combined = s + separator + r`,

where the separator does not occur in `s`. Compute the KMP prefix function over this combined string. At each position, the prefix value is the length of the longest prefix of `combined` that is also a suffix ending there. The final value cannot cross the separator, so it measures the longest prefix of `s` matching a suffix of `r`.

A suffix of `r` is the reverse of a prefix of `s`. Therefore an overlap of length `p` says

`s[:p] == reverse(s[:p])`,

which is exactly a palindromic prefix. The KMP failure links find the longest such overlap in linear time rather than retesting prefixes from scratch.

Once its length `p` is known, the remaining suffix `s[p:]` has no matching material on the left. Prepend its reverse:

`reverse(s[p:]) + s`.

For `abcd`, only `a` is a palindromic prefix, so prepend reverse(`bcd`) = `dcb` to obtain `dcbabcd`. For `aacecaaa`, the longest palindromic prefix is `aacecaa`; only the final `a` must be mirrored in front.

The final prefix-function value is the maximum length `p` for which a prefix of `s` equals the corresponding reversed prefix, so `s[:p]` is the longest palindromic prefix. Prepending `reverse(s[p:])` mirrors every character outside that prefix around it, making the complete result a palindrome. If fewer characters could be prepended, more than `p` original leading characters would have to align with their reverse and form a longer palindromic prefix, contradicting maximality. The constructed palindrome is therefore the shortest possible.

## Complexity detail
Constructing the reversed and combined strings, computing the prefix array, and assembling the output each take $O(n)$ time. The combined string and prefix array use $O(n)$ space.

## Alternatives and edge cases
- Testing prefixes from longest to shortest and checking each for palindrome can take $O(n^2)$ time.
- A rolling-hash comparison can find a candidate in linear expected time, but requires collision handling or verification for deterministic correctness.
- Manacher's algorithm can identify palindromic prefixes in linear time but is more machinery than the prefix-overlap formulation.
- Appending characters solves a different problem; additions are restricted to the front.
- Empty, one-character, and already-palindromic strings are unchanged. If only the first character qualifies, the entire remaining suffix is mirrored.
