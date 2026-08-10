## General

**Track parity, not full frequencies.** Whether a substring is wonderful depends only on which character counts are odd. Exact counts are unnecessary. Since input uses only `a` through `j`, a ten-bit integer can store all parities: bit zero for `a`, bit one for `b`, and so on. A set bit means the count in the represented prefix is odd.

**Update a prefix mask with XOR.** `st` starts at zero for the empty prefix. Reading character `c` computes its bit position `ord(c) - ord("a")` and toggles that bit with XOR. Seeing the same character again toggles it back, exactly matching even/odd count changes.

**A substring is the XOR of two prefix masks.** Let one prefix end just before a substring and the other end at the substring's right boundary. XOR cancels characters appearing with the same parity in both prefixes, leaving the parity mask of their difference—the substring. Therefore, prior prefix mask `q` and current mask `st` form a wonderful substring when `st ^ q` has either zero set bits or exactly one.

**Count the all-even case.** If `q == st`, their XOR is zero and every substring character count is even. `cnt[st]` records how many earlier prefixes have this same mask, so `ans += cnt[st]` counts all-even wonderful substrings ending at the current character.

**Count exactly one odd character.** If only character bit `i` differs, prior mask must be `st ^ (1 << i)`. The source checks all ten bit positions and sums the frequencies of these neighboring masks. Each matching prior prefix creates a substring whose parity mask has exactly that single bit set.

The same prior prefix cannot be counted in two different bit choices because two distinct one-bit masks are different. It also cannot overlap the equal-mask case. Thus every wonderful ending is counted exactly once.

**Include substrings beginning at index zero.** `cnt[0] = 1` registers the empty prefix before any characters. When a current prefix itself has zero or one odd letters, pairing it with this empty prefix counts the substring from the beginning. Without this initial entry, those occurrences would be missed.

**Increment after querying.** `cnt[st] += 1` occurs only after all contributions for the current ending are counted. This ensures the current prefix is not paired with itself, which would represent an empty substring. Only strictly earlier prefixes create nonempty substrings.

**Trace `"aba"`.** Masks progress from zero to `001` after `a`, then `011` after `b`, then `010` after the final `a`. Each single character is counted through a one-bit mask difference. At the final prefix `010`, the empty prefix differs by one bit, counting whole substring `"aba"`. Total is four.

**Why occurrences, not distinct text, are counted.** Every pair of prefix positions identifies one start/end occurrence. `cnt` stores how many earlier positions share a mask, not merely whether a mask exists. Adding its full frequency counts repeated substring occurrences separately, as required.

**Why the result is complete.** Every wonderful substring has parity mask zero or one power of two. Its two boundary prefix masks are consequently equal or differ in exactly one bit, both categories queried by the algorithm. Conversely, every counted prefix pair has one of those parity differences and is wonderful. Processing each right boundary once proves exact counting.

## Complexity detail

Let $N$ be word length and $A=10$ the alphabet size. Each character performs one mask update, one equal-mask lookup, and ten one-bit-neighbor lookups. Time is $O(NA)$, which is $O(N)$ because $A$ is fixed at ten.

There are only $2^{10}=1024$ possible masks. The `defaultdict` can create at most that many keys even when queried neighbors were unseen. Space is therefore $O(2^{10})=O(1)$ with respect to $N$, matching the manifest.

The answer can reach $N(N+1)/2$, about five billion for $N=10^5$, so fixed-width implementations need a 64-bit counter. Python integers are safe.

## Alternatives and edge cases

- **Array of 1024 frequencies:** Direct mask indexing avoids dictionary overhead and makes constant bounded storage explicit.
- **Count full frequency vectors:** Much larger states are unnecessary because only parity matters.
- **Enumerate substrings:** Updating counts for all $O(N^2)$ substrings is too slow; prefix-mask pairs aggregate them by state.
- **Single character:** Current mask differs from the empty prefix by one bit, so the one substring is counted.
- **All same character:** Every substring has either zero or one odd count, so all $N(N+1)/2$ occurrences are wonderful.
- **All-even substring:** Equal prefix masks count it through `cnt[st]`.
- **Exactly one odd letter:** One-bit neighbor masks count it, regardless of that letter's actual odd frequency magnitude.
- **Two odd letters:** Prefix masks differ in two bits and are intentionally absent from both queried categories.
- **Alphabet restriction:** Ten neighbor checks rely on letters `a` through `j`. A larger alphabet changes mask width and constant factors.
- **Update order:** Incrementing `cnt[st]` before queries would count an empty substring at every position; the source correctly increments afterward.
