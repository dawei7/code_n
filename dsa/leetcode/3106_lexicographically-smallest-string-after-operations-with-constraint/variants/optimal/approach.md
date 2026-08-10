## General

**Lexicographic order makes the leftmost position decisive.** Two equal-length strings are compared at their first differing character. A smaller character at position zero is better than any improvement at later positions; if position zero ties, position one becomes decisive, and so on. This priority justifies processing `s` from left to right and spending as much of the distance budget as needed to make the current character as small as possible.

The source converts `s` to `cs = list(s)` because Python strings are immutable. It enumerates the original string, so each decision uses the untouched source character `c1` and writes the chosen result into `cs[i]`.

**Cyclic distance between two letters.** Let the alphabet positions be 0 through 25. For a candidate `c2 < c1`, moving backward directly costs:

`ord(c1) - ord(c2)`.

Moving forward through `z` and wrapping to `a` costs:

`26 - ord(c1) + ord(c2)`.

The source takes the smaller of these two values. The ASCII offset cancels in both differences, so it is unnecessary to subtract `ord("a")` explicitly.

For example, changing `z` to `a` costs one through the wraparound route rather than 25 backward steps. Changing `d` to `a` costs three directly, while wrapping costs 23.

**Try replacement letters from smallest upward.** The inner loop follows `ascii_lowercase` in order `a, b, ..., z`. It stops when `c2 >= c1` because a character equal to the original produces no improvement and a larger one would make the result lexicographically worse at this position. Leaving `cs[i]` unchanged already represents the equal candidate at cost zero.

For each strictly smaller `c2`, the code computes cyclic distance `d`. The first candidate with `d <= k` is the lexicographically smallest character affordable using the remaining budget. It writes that character, subtracts the exact distance, and stops the inner loop.

If no smaller candidate is affordable, the original character remains. Saving the budget is then the only useful choice because changing this position to a larger character would harm lexicographic order and cannot enable a better prefix.

**Why spending budget greedily is correct.** Suppose the algorithm can change the current character to `c2`, and consider a plan that chooses a larger character here in order to save budget for later. The greedy result and that plan first differ at the current position. Since the greedy character is smaller, the greedy complete string is lexicographically smaller regardless of every later character. No collection of suffix improvements can compensate for losing at an earlier position.

Therefore, at each index the correct decision is the smallest character reachable with the budget remaining after the already fixed prefix. This establishes an induction: before index $i$, the source has produced the smallest feasible prefix. Choosing the smallest affordable character at $i$ extends it to the smallest feasible prefix of length $i+1$. After the last index, the whole string is optimal.

**The budget is an upper bound, not an exact amount.** The contract requires total distance at most `k`. The source may leave unused budget when no later smaller character is reachable. This is legal; spending extra distance merely to exhaust the budget would not improve the answer.

**A trace for `s = "zbbz"` and `k = 3`.** At the first position, `z` can become `a` for cyclic cost one, leaving two. At the second position, `b` becomes `a` for cost one, leaving one. The third `b` also becomes `a`, exhausting the budget. The final `z` stays unchanged. The result is `"aaaz"`.

For `"xaxcd"` with budget four, `x` reaches `a` by wrapping three steps, leaving one. The existing `a` cannot be made smaller. The next `x` cannot reach `a` with one step, but the inner scan finds `w` as the smallest feasible lower letter at cyclic distance one. Later characters remain, giving `"aawcd"`.

**Why the inner loop searches all smaller letters.** The cheapest lower character is not always the lexicographically smallest affordable one in a cyclic alphabet. A direct decrement uses little budget but may miss `a` through a short wrap from `z`. Trying candidates in lexicographic order and measuring both routes resolves both objectives correctly.

## Complexity detail

For each of $n$ characters, the inner loop examines at most 26 lowercase letters. Every distance calculation is constant time. The total is $O(26n)=O(n)$ under the fixed English alphabet.

`list(s)` creates $n$ character references and `"".join(cs)` creates the returned string. Auxiliary working space is $O(n)$ for `cs`; the result itself is also length $n$. Loop variables use constant space.

The algorithm does not search an exponential set of complete strings. Lexicographic prefix dominance collapses each position to one greedy decision.

## Alternatives and edge cases

- **Compute the target directly:** First test the cyclic distance to `a`. If affordable, choose `a`; otherwise direct backward movement by the remaining budget gives the smallest reachable lower letter. This can avoid the 26-character scan.
- **Dynamic programming over position and budget:** It is correct but unnecessary because lexicographic prefix priority makes the greedy choice decisive.
- **`k = 0`:** No strictly smaller character has distance zero, so the original string is returned.
- **Character `a`:** The inner loop stops immediately at equality, correctly leaving it unchanged.
- **Character `z`:** `a` is only one cyclic step away.
- **Unused budget:** Allowed because the distance constraint is `<= k`.
- **Original-character candidate:** It is represented by doing nothing; the loop does not need to assign it explicitly.
- **Larger replacement:** It can never help lexicographic minimality at the first changed position.
- **Wraparound route:** The second distance expression is essential for letters near `z`.
- **Direct route:** For ordinary lower letters far from the wrap boundary, subtraction may be cheaper.
- **First affordable candidate:** Since candidates are tested from `a` upward, affordability immediately proves lexicographic optimality for that position.
- **Budget subtraction:** Only an actual replacement consumes `d`; failed candidates cost nothing.
- **Input immutability:** The original string remains unchanged while `cs` stores the result.
- **Fixed alphabet:** The linear time claim treats 26 as a constant; a generalized alphabet of size $A$ would give $O(nA)$.
- **Prefix proof:** A smaller current character outweighs every possible suffix, which is why saving budget for later cannot beat the greedy choice.
