## General
**Binary-search the duplicate length:** If some substring of length $L$ occurs twice, then its prefixes prove that every smaller length is also feasible. Conversely, if no duplicate of length $L$ exists, no longer duplicate exists. This monotonicity permits binary search over lengths from $1$ through $N-1$.

**Check one length with rolling hashes:** Encode each letter as an integer and compute two polynomial hashes for the first length-$L$ window. Sliding one position removes the outgoing letter, multiplies by the base, and adds the incoming letter, so every new pair of hashes is obtained in constant time. Store the start indices previously associated with each hash pair.

**Verify matching windows:** A repeated hash pair identifies candidates, not a proof. Compare the actual length-$L$ substrings for every previous start stored under that pair. Return the current start only when the characters match. If a rare collision joins unequal windows, retain both starts so a later genuine duplicate is still discoverable.

**Keep the longest successful result:** When the check succeeds, save its start and length and search the larger half. When it fails, search the smaller half. The last saved window is longest because binary search rules out every greater length.

For a fixed $L$, the checker examines all $N-L+1$ windows. Its explicit equality test confirms that every reported answer really has two occurrences. Conversely, any true duplicate produces the same two polynomial hashes and its later occurrence is compared with the earlier one, so the checker finds it.

## Complexity detail
Binary search performs $O(\log N)$ length checks. Each check rolls across $O(N)$ windows, giving $O(N \log N)$ expected time; explicit collision verification adds character comparisons only for equal hash pairs and genuine matches under the standard rolling-hash model. A check stores $O(N)$ hash entries and start indices, while the encoded input uses $O(N)$ space.

## Alternatives and edge cases
- **Suffix array plus longest-common-prefix array:** Sorting suffixes and finding the largest adjacent common prefix gives a deterministic solution, but implementing an efficient suffix array is more involved.
- **Suffix automaton or suffix tree:** These structures can solve the problem in linear time, with substantially greater implementation complexity.
- **Pairwise suffix comparison:** Compare every pair of suffixes character by character. It is correct but requires at least $O(N^2)$ work and can reach $O(N^3)$ on repetitive strings.
- **Store substring slices directly:** Binary search with a set of slices is simple, but materializing length-$L$ strings can add $O(L)$ copying per window and lose the intended bound.
- **No repeated character:** If every character is distinct, the required answer is `""`.
- **Overlapping occurrences:** Strings such as `"aaaaa"` may use overlapping copies; forbidding overlap would change the problem.
- **Multiple longest answers:** Any one is valid; a deterministic scan may return the first one it confirms.
- **Hash collisions:** Never accept hash equality alone; verify the underlying characters before reporting a duplicate.
