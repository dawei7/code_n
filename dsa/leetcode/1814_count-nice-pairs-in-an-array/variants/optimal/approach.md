## General
**Move each number's reversal to its own side**

Rearrange the nice-pair equality:

$$
\texttt{nums[i]}-\operatorname{rev}(\texttt{nums[i]})
=
\texttt{nums[j]}-\operatorname{rev}(\texttt{nums[j]}).
$$

Thus each array value has one transformed key, and a pair is nice exactly when its two keys are equal. The original cross-sums never need to be evaluated for every pair.

**Count earlier equal keys while scanning**

Maintain a hash map from transformed key to the number of earlier indices with that key. At index `j`, every earlier occurrence forms one valid pair `(i, j)`, so add the current frequency to the answer and then increment the key's count.

**Why each pair is counted exactly once**

When `j` is processed, the map contains precisely indices smaller than `j`. Equal keys are equivalent to the required equality, so every added occurrence is a nice pair with correct index order. Conversely, any nice pair has equal keys; its first index is already in the map when the second is scanned, so that pair is added once at its unique second endpoint.

Apply the modulus during the scan so the stored answer remains bounded. Frequencies themselves need no modulus because each is at most $n$.

## Complexity detail
Reversing a value takes time proportional to its decimal digit count. Across the input this is $O(D)$ work, while hash lookup and update take expected constant time per value. Since every legal value has at most ten digits, $D \le 10n$. The map can hold one distinct key per array element, using $O(n)$ space.

## Alternatives and edge cases
- **Check every index pair:** Directly testing the original equality is correct but takes $O(n^2)$ pair comparisons.
- **Sort transformed keys:** Sorting and counting equal runs works in $O(D+n\log n)$ time and can avoid a hash table, but it is asymptotically slower.
- **Count all groups afterward:** Build a complete frequency map and sum $\binom{c}{2}$ for each count $c$; this is equally efficient but less directly enforces `i < j`.
- **Trailing zeros:** Reversal drops them numerically, as in `rev(120) = 21`.
- **Zero:** `rev(0) = 0`, so zero has transformed key zero like every decimal palindrome.
- **Equal values:** Distinct indices still form separate pairs.
- **Different values:** They may be nice when their transformed keys match, such as `42` and `97`.
- **Negative transformed key:** Hash keys may be negative and require no special handling.
- **Modulo:** Reduce the accumulated pair count, not the transformed keys or their frequencies.
