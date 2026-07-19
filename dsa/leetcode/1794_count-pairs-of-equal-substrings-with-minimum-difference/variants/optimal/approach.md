## General
**Prove that a minimum match has length one**

Suppose an eligible pair of equal substrings has length $L>1$. Their final characters, at indices $j$ and $b$, are equal. They alone form another eligible quadruple $(j,j,b,b)$ whose difference is $j-b$.

Because the second substring has $b=a+L-1>a$, this singleton has

$$
j-b < j-a.
$$

The longer quadruple therefore cannot minimize $j-a$. Every globally minimum quadruple must match one character, with $i=j$ and $a=b$. Conversely, each shared character occurrence pair gives such an eligible singleton.

**Choose the extreme occurrence for each character**

For a fixed character $c$, a singleton pair at indices $i$ and $a$ contributes $i-a$. This is minimized by taking the earliest occurrence of $c$ in `firstString` and the latest occurrence of $c$ in `secondString`.

Those two positions are unique. Any later first-string position adds a positive amount, and any earlier second-string position subtracts a smaller index, so no other occurrence pair of $c$ can tie its best difference.

**Count characters tied for the global minimum**

Scan `firstString` to retain the first index of each character, and scan `secondString` to retain the last index of each character. For every character present in both strings, compute

$$
d_c
=
\operatorname{first}_{\texttt{firstString}}(c)
-
\operatorname{last}_{\texttt{secondString}}(c).
$$

The smallest $d_c$ is the minimum possible $j-a$. Since each character contributes exactly one occurrence pair at its own minimum, the answer is the number of shared characters whose $d_c$ equals that smallest value. If there is no shared character, there is no eligible quadruple and the answer is zero.

## Complexity detail
The two occurrence scans inspect $n+m$ characters. Comparing the resulting entries examines at most the 26 lowercase letters, so total time is $O(n+m)$. The occurrence tables have fixed alphabet size and therefore use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Compare every character pair:** Testing all $nm$ singleton pairs is correct after the length-one reduction, but it is unnecessarily quadratic.
- **Enumerate and compare all substrings:** This obscures the singleton proof and creates at least quadratic candidate sets in each string, with much worse comparison cost.
- **Store every occurrence:** Full position lists are unnecessary because only the earliest first-string and latest second-string occurrences can minimize the difference.
- **No shared character:** No equal nonempty substring exists, so return zero without taking a minimum of an empty collection.
- **Repeated occurrences:** Repetition changes the extreme indices but cannot create multiple best pairs for one character.
- **Ties across characters:** Different characters may have the same minimum difference; each contributes one quadruple and must be counted.
- **Negative differences:** They are valid and arise when the chosen second-string index is later than the chosen first-string index.
- **Minimum-length strings:** Two equal one-character strings yield one quadruple; two different characters yield zero.
