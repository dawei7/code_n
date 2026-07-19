## General
**Reverse the counting from substrings to occurrences**

Enumerating substrings repeats the same question many times. Instead, ask how many substrings count one particular occurrence of a character as unique. Suppose an occurrence is at index $i$, the previous occurrence of that same character is at $p$, and the next is at $q$. Use the virtual boundaries $p=-1$ when there is no previous occurrence and $q=n$ when there is no next occurrence.

For the occurrence at $i$ to be the only copy in a substring, the left boundary may be any position from $p+1$ through $i$, giving $i-p$ choices. Independently, the right boundary may be any position from $i$ through $q-1$, giving $q-i$ choices. This occurrence therefore contributes

$$
(i-p)(q-i)
$$

to the final sum.

**Finalize a contribution when its next occurrence arrives**

Maintain the last two indices for each of the $A$ letters. When the current index becomes the next occurrence $q$, the immediately preceding occurrence $i$ now has both boundaries known, so add its contribution and shift the two saved indices. After scanning the string, use the virtual boundary $q=n$ to finalize the last occurrence of every letter.

**Why summing occurrence contributions equals the requested total**

Every unique character counted inside a particular substring corresponds to exactly one occurrence position in `s`. That substring's boundaries lie between the adjacent equal-character occurrences precisely when the formula counts it. Conversely, every boundary pair counted by the formula contains the chosen occurrence and no other copy of its character, so it contributes one to `countUniqueChars` for that substring. Summing over occurrences therefore counts every requested substring-character contribution once, including equal substring values at different positions.

## Complexity detail
Let $n$ be the string length and $A=26$ the alphabet size. The scan performs constant work per character, and finalizing the alphabet costs $O(A)$, for $O(n+A)=O(n)$ time. Two index arrays of length $A$ use $O(A)$ auxiliary space.

## Alternatives and edge cases
- **Expand every substring with frequency counts:** Updating a count and current unique total for every start/end pair takes $O(n^2)$ time and $O(A)$ space.
- **Recount each materialized substring:** Constructing every substring and counting its characters independently can take $O(n^3)$ time.
- **Store all positions per character:** Sentinel-augmented occurrence lists support the same contribution formula in $O(n)$ time but retain $O(n)$ indices instead of only the last two per letter.
- **First occurrence:** The virtual previous index `-1` permits every left boundary from the start of the string through that occurrence.
- **Last occurrence:** The virtual next index $n$ permits every right boundary from that occurrence through the end of the string.
- **Repeated substring values:** Positions define substrings, so two equal strings from different ranges both contribute.
- **All characters equal:** Only length-one substrings have a unique character, and each occurrence contributes exactly once.
- **All characters distinct:** Every character is unique in every substring containing it, making the sum equal to the total lengths of all substrings.
