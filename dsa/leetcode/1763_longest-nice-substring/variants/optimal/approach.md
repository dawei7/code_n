## General
**Test the current region as a whole**

Collect the characters present in the current substring. It is nice exactly when every character's `swapcase()` form is also present. If this holds, the complete region is necessarily the longest answer available inside itself.

**Use an unpaired character as a separator**

Suppose character `s[i]` appears in the region but its opposite case does not. No nice substring contained in this region can include `s[i]`: that smaller substring cannot contain a counterpart that is absent from the entire region. Every valid candidate must therefore lie wholly to the left or wholly to the right of this position.

**Solve both independent sides**

Recursively find the longest nice substring on each side of the first unpaired character. Returning the longer result is safe because the separator proof excludes every candidate crossing that position.

**Preserve the earliest tie**

The left recursive result begins before every right result. When their lengths are equal, choose the left result with `>=`; this implements the required earliest-start rule at every split and therefore in the final answer.

A region shorter than two characters cannot contain both cases of any letter and returns empty. Otherwise recursion either proves the entire region nice or splits at a character that no valid answer may cross, so induction over region length establishes completeness and correctness.

## Complexity detail
In the worst case, each recursive level builds a set and slices a substring only one character shorter than its parent, producing the series $n+(n-1)+\cdots+1=O(n^2)$ time. Python substring slices and character sets retained across a maximally unbalanced recursion can likewise total $O(n^2)$ space; recursion depth is $O(n)$.

## Alternatives and edge cases
- **Enumerate all substrings:** Building a character set and checking every candidate directly is simple but can take $O(n^3)$ time.
- **Incremental case masks:** Extending each start position while maintaining lowercase and uppercase bitmasks reduces exhaustive enumeration to $O(n^2)$ time and can compare masks in constant time.
- **Sliding windows by distinct-letter count:** Trying each possible number of distinct letters can also achieve quadratic time but requires more bookkeeping.
- **Single character:** It cannot be nice because only one case is present.
- **Entire string nice:** Return it immediately; no contained substring can be longer.
- **No paired cases:** Repeated splitting eventually returns the empty string.
- **Equal-length answers:** Choose the leftmost occurrence, not the lexicographically smallest text.
- **Repeated characters:** Multiplicity is irrelevant; only the presence of both cases matters.
- **Several letters:** Every letter appearing in the candidate must satisfy the condition independently.
