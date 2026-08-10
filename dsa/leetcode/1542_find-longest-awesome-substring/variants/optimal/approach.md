## General

**A palindrome depends on frequency parity**

Characters may be rearranged arbitrarily inside the chosen substring. Their original order therefore does not determine whether a palindrome can be formed; only the counts matter.

Every character in an even-length palindrome appears an even number of times. In an odd-length palindrome, exactly one character may have an odd count and occupy the center. Thus a digit substring is awesome exactly when at most one of its ten digit counts is odd.

The solution represents these ten parities with a ten-bit mask. Bit `v` is one when digit `v` has appeared an odd number of times in the current prefix and zero when its count is even.

**Update prefix parity with XOR**

`st` starts at zero for the empty prefix because every digit count is even. Reading digit `v` executes `st ^= 1 << v`.

XOR toggles exactly bit `v`. The first occurrence changes its parity from even to odd; the next changes it back to even. Actual counts are unnecessary because only odd versus even affects palindrome feasibility.

For a substring ending at index `i` and beginning after an earlier prefix ending at `p`, its parity mask is the XOR of the two prefix masks. Bits equal in both prefixes cancel, leaving precisely the parities contributed by positions `p+1` through `i`.

**Case one: every substring count is even**

If the current `st` has appeared before at prefix index `p`, their XOR is zero. Therefore all digit counts in substring `s[p+1:i+1]` are even.

The dictionary `d` stores the earliest index for each observed mask. Using the earliest equal mask produces the longest substring ending at `i`, so the candidate length is `i - d[st]`.

The initialization `d = {0: -1}` represents the empty prefix before index zero. It allows a prefix beginning at the first character to be recognized. If the current mask is zero at index `i`, its length is `i - (-1) = i+1`.

**Case two: exactly one substring count is odd**

An awesome substring may also have one odd digit count. Its two endpoint prefix masks must differ in exactly one bit.

For each digit bit `v` from zero through nine, the source checks whether `st ^ (1 << v)` exists in `d`. That expression toggles one bit of the current mask, generating every mask at Hamming distance one.

If such a prefix mask occurred at index `p`, the substring after it has only bit `v` odd. It can be rearranged into an odd-length palindrome with digit `v` in the center. Again, the earliest stored index yields the maximum length for this ending position.

**Store only the earliest occurrence**

When `st` has not appeared before, the solution records `d[st] = i`. If it has appeared, the existing index is deliberately preserved.

For any future ending index, subtracting a smaller prefix index gives a longer substring. A later occurrence of the same mask can never improve a maximum-length answer, so retaining only the first occurrence loses no useful candidate.

**Tracing the parity idea**

In substring `"24241"`, digit two occurs twice, digit four occurs twice, and digit one occurs once. Its parity mask has exactly the bit for one set. The characters can be rearranged so the even-count digits form mirrored pairs and one occupies the center.

For a string of all distinct digits, any substring longer than one has at least two odd counts. Single characters remain awesome, which is why `ans` safely begins at one for the guaranteed nonempty input.

**Why checking eleven masks is complete**

For a fixed ending index, a valid substring mask is either zero or one of the ten one-bit masks. Zero corresponds to an earlier prefix equal to `st`. A one-bit mask corresponds to an earlier prefix equal to `st` with that bit toggled.

The exact-mask lookup plus ten neighbor lookups covers all eleven possibilities and no invalid parity pattern. Taking the maximum over every ending position therefore examines every awesome substring.

**Why the result is correct**

Prefix-mask XOR gives the exact digit-count parity of each substring. The algorithm accepts exactly masks with zero or one set bit, which is exactly the condition for rearrangement into a palindrome.

For each acceptable endpoint-mask relationship, the earliest compatible prefix gives the longest candidate ending there. Maximizing across all indices yields the globally longest awesome substring.

## Complexity detail

Let $N$ be string length. For each character, the solution performs one mask update, one exact lookup, and ten neighbor lookups. Ten is fixed by the digit alphabet, so work per character is constant and total time is $O(N)$.

There are only $2^{10}=1024$ possible parity masks. The dictionary therefore uses at most 1024 entries. This is $O(1)$ space with respect to $N$, matching the manifest, or $O(2^D)$ if the alphabet size $D$ were treated as variable.

All mask operations fit comfortably in a small integer because only ten bits are used.

## Alternatives and edge cases

- **Enumerate all substrings:** Updating counts for every pair of endpoints costs at least $O(N^2)$.
- **Store full frequency vectors:** Prefix counts work but make comparisons heavier; a parity mask contains exactly the needed information.
- **Store latest mask index:** It is wrong for maximum length because later prefixes produce shorter candidates.
- **All counts even:** Equal prefix masks detect this case.
- **Exactly one odd count:** A one-bit-different prefix mask detects this case.
- **Two odd counts:** The substring cannot be rearranged into a palindrome and is intentionally ignored.
- **Single character:** It always has one odd count and is awesome, supporting initial answer one.
- **Entire string awesome:** The empty-prefix entry at negative one permits returning full length.
- **Leading zeros:** Character conversion treats zero as ordinary digit index zero.
- **Repeated digit:** Each occurrence toggles the same bit, so pairs cancel.
- **Nonempty input:** The contract guarantees at least one character; otherwise initializing answer to one would need adjustment.
- **Fixed digit alphabet:** Ten neighbor checks and at most 1024 states are constant only because input contains digits.
- **Rearrangement permission:** Without arbitrary swaps, parity alone would not characterize palindromic substrings.
