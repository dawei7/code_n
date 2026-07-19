## General
**Preprocess membership once**

Store the distinct letters of `allowed` in a constant-time membership representation. A set is direct; a 26-bit integer is an equally suitable fixed-alphabet representation. This avoids rescanning `allowed` for every character of every word.

**Reject a word at its first forbidden letter**

For each word, test its characters against the membership representation. Count the word if all tests succeed. If any test fails, the word cannot be consistent, so its remaining characters need not be examined.

Every counted word satisfies the definition because each of its characters passed the allowed-membership test. Every uncounted word has at least one character that failed that test and is therefore inconsistent. Processing array entries separately also preserves multiplicity when the same word appears more than once.

## Complexity detail
Building the allowed representation and inspecting the word characters takes $O(S)$ total time. At most 26 lowercase letters are stored, so the auxiliary space is $O(26)=O(1)$. Early rejection may save work on particular words but does not change the worst-case bound.

## Alternatives and edge cases
- **Scan `allowed` for each character:** this is correct but takes $O(A S)$ time when $A = \lvert \texttt{allowed} \rvert$, repeating membership work that preprocessing removes.
- **Bitmask membership:** map each lowercase letter to one of 26 bits; this has the same linear time and constant space as a set with smaller fixed storage.
- **Set difference per word:** checking whether `set(word) - set(allowed)` is empty is concise, but repeatedly allocates a set for each word.
- **Repeated letters:** a consistent word may use the same allowed letter any number of times.
- **Duplicate words:** identical entries are counted independently because the result is over the array, not over distinct strings.
- **One forbidden character:** one disallowed letter invalidates the entire word even if every other letter is allowed.
