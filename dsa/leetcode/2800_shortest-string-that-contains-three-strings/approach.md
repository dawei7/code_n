## General

**The goal has two levels.** The returned string must contain `a`, `b`, and `c` as substrings. Among all such strings, it must first have minimum length. If several minimum-length answers exist, it must be lexicographically smallest. The algorithm handles this by trying every order in which the three source strings might appear and selecting candidates with the pair `(length, text)` in that priority order.

**Merge two strings as tightly as their order permits.** The helper `f(s, t)` constructs a shortest string that contains both values while treating `s` as coming before `t` unless one is already contained in the other.

Its first two checks are containment checks. If `s in t`, returning `t` already contains both and cannot be improved because any answer containing `t` needs at least `len(t)` characters. Conversely, if `t in s`, returning `s` is optimal. These checks are essential when one input occurs in the middle of another; suffix-prefix overlap alone would not notice every such containment.

If neither contains the other, the only way to shorten the ordered concatenation `s + t` is to overlap a suffix of `s` with an equal prefix of `t`. The loop begins with the greatest possible overlap length, `min(len(s), len(t))`, and decreases toward one. The first match therefore has maximum length. If an overlap of length $q$ is found, `s + t[q:]` retains all of `s` and adds only the part of `t` not already represented by the matching suffix. If no positive overlap exists, ordinary concatenation is necessary.

For example, merging `"abc"` before `"bcd"` finds the length-two match `"bc"` and returns `"abcd"`. Merging `"abc"` before `"xabcx"` instead triggers containment and returns `"xabcx"`.

**Why the helper is shortest for a fixed pair order.** With no containment, any string that places an occurrence of `s` no later than an occurrence of `t` can share only characters where the end of `s` agrees with the beginning of `t`. A larger shared region always removes more characters from the combined length. Because the loop chooses the largest legal region, no ordered merge can be shorter. Containment cases already return the longer containing string, which is an immediate lower bound.

**Try all six permutations.** The call `permutations((a, b, c))` supplies every possible order of the three inputs. For each order, the code first computes `f(a, b)` and then merges `c` into that result with `f(..., c)`.

Trying every order matters because overlap is directional. `"ab"` before `"bc"` saves one character, while reversing them may save none. With only three strings, there are at most $3! = 6$ orders, so exhaustive order selection is a constant-sized search rather than a scalability problem. Equal input strings can cause duplicate permutations, but at most six candidates are still examined and correctness is unaffected.

**Why the six orders cover an optimal answer.** Consider any shortest common superstring and choose one occurrence of each input within it. Sort the three chosen occurrences by their starting positions; that produces one of the enumerated orders. Inputs contained inside another are handled by the helper's containment checks. For non-contained consecutive strings in that order, leaving an avoidable suffix-prefix overlap unused would only make the superstring longer. Thus a maximally overlapped merge for the corresponding order can produce a candidate no longer than that optimal arrangement. Since every order is tried, at least one candidate attains the global minimum length.

There can be subtleties when occurrences coincide or one string is contained in the result of merging the other two. Those do not break the argument: tied starts can be ordered either way, and the second helper call checks containment against the entire intermediate string before looking only at its suffix.

**Apply the tie-break explicitly.** `ans` starts as the empty sentinel. A candidate `s` replaces it if `ans` is empty, if `s` is shorter, or if the lengths match and `s < ans`. Python compares strings lexicographically, exactly matching the problem's secondary rule. A lexicographically smaller but longer candidate never replaces a shorter answer because the text comparison is guarded by equal length.

The loop variables reuse the names `a`, `b`, and `c`. This shadows the original parameters inside the loop but is harmless: each tuple from `permutations` contains the needed values, and the permutation iterator was created from the original tuple before iteration proceeds.

## Complexity detail

Let $L$ be the total length of the three input strings. There are only six permutations. In each helper call, containment testing can take $O(L^2)$ time in a conservative substring-search analysis. The descending overlap loop performs at most $O(L)$ iterations, and Python slicing plus string equality can inspect $O(L)$ characters per iteration, giving $O(L^2)$ time per helper call in the worst case. A constant number of calls therefore yields $O(L^2)$ total time.

This bound is appropriate for the exact straightforward string operations. With the problem's maximum individual length of $100$, it is comfortably small. More sophisticated linear-time pattern-matching could compute overlaps in $O(L)$ per pair, but it is unnecessary for three short strings.

Each candidate and intermediate merged string has length at most $L$. Slices created while testing overlaps are also at most $O(L)$ live at once. The permutation collection and number of candidates are constant. Peak auxiliary space is $O(L)$, including intermediate strings but excluding the returned string; including the output does not change the asymptotic bound.

Lexicographic comparisons between equal-length candidates can inspect $O(L)$ characters, but only a constant number occur, so they are absorbed by the $O(L^2)$ time bound.

## Alternatives and edge cases

- **Bitmask shortest-superstring dynamic programming:** This is the standard generalization for many strings. It tracks the best result for each subset and last string, but for exactly three inputs it adds machinery without improving the practical bound.
- **Precompute pair overlaps:** Computing all directed overlaps first can make the six-order evaluation concise. It must still account for containment and lexicographic ties carefully.
- **KMP or Z-algorithm overlaps:** These can find each maximum suffix-prefix overlap in linear time. They are useful for long strings, but the simple descending checks are clearer under the length-$100$ constraint.
- **One string contains another:** The helper returns the containing string immediately, preventing duplicated characters and allowing containment in the middle rather than only at an edge.
- **All three strings identical:** Every merge returns that same string, and the final answer is the common input.
- **No overlaps at all:** Every order has total length $L$. The candidate comparison selects the lexicographically smallest concatenation among the six orders.
- **Directional overlap:** A match from the suffix of `s` to the prefix of `t` says nothing about the reverse direction. Enumerating permutations is what handles both possibilities.
- **Equal-length candidates:** Only then is lexicographic order consulted. This preserves the primary minimum-length objective.
- **Duplicate permutations:** Repeated input strings may make several generated tuples identical. The work remains constant and the same best candidate is considered more than once harmlessly.
- **Empty strings outside the constraints:** Containment would make an empty string disappear naturally, but the problem guarantees each input has at least one character.
- **Lowercase ordering:** Python's ordinary string comparison agrees with lexicographic order for the constrained lowercase English letters.
- **Greedy choice without permutations:** Merging whichever pair has the largest immediate overlap can miss the global best arrangement. Exhausting all six orders avoids that local-choice trap at negligible cost.
