## General

A binary string is beautiful when it can be partitioned into substrings such that every substring has even length and contains only one repeated character. At first, this sounds like we may need dynamic programming to decide where those substrings should begin and end. The even-length requirement yields a much simpler characterization.

Group the original string into the fixed adjacent pairs

$$
(0,1),(2,3),(4,5),\ldots.
$$

The string length is guaranteed to be even, so every character belongs to exactly one such pair.

The key equivalence is:

> The whole string can be partitioned into homogeneous even-length substrings if and only if the two characters in every fixed pair are equal.

Once this equivalence is established, the minimum number of changes is simply the number of pairs whose two bits differ.

**Why every beautiful string must have equal fixed pairs**

Assume the string already has a valid beautiful partition. Each part has even length. Starting from index $0$, the first part therefore ends after an even number of characters, so its boundary lies between two fixed pairs rather than through the middle of one. The same is true for every later part because a sum of even lengths is even.

Consequently, no fixed pair $(0,1),(2,3),\ldots$ is split between two parts. Both of its characters lie inside the same homogeneous part, and all characters in that part are identical. The two characters in every fixed pair must therefore be equal.

This proves necessity. If even one pair is `01` or `10` after all changes, no choice of valid even-length boundaries can hide that mismatch.

**Why equal fixed pairs are sufficient**

Now assume every fixed pair contains equal characters. We can use each pair itself as one substring in the partition. Every such substring:

- has length $2$, which is even;
- is either `00` or `11`, so it contains only one character.

Thus the list of pairs is already a valid beautiful partition. Adjacent equal pairs could optionally be merged into a longer homogeneous even part, but merging is not needed to prove validity.

This direction is what removes all boundary-search complexity. We do not need to discover the original statement's larger substrings. Length-two pieces always supply a valid partition whenever the pair condition holds.

**Optimize each pair independently**

Consider one fixed pair.

- If its bits are equal, it already meets the condition and costs zero changes.
- If its bits differ, any beautiful final string must make them equal, so at least one of those two positions must change.
- Flipping either bit makes a differing binary pair equal, so one change is also sufficient.

Therefore the exact minimum cost of a pair is $0$ when equal and $1$ when different. The pairs are disjoint, so changing a bit in one pair cannot repair or damage another pair. Their independent minimum costs can simply be added.

This is both a lower-bound and construction argument. Every mismatching pair forces at least one change, so no solution can use fewer changes than the mismatch count. Changing one bit in every mismatching pair makes all pairs equal, which creates a valid partition and achieves exactly that count. Hence the count is globally minimal.

**How the one-line implementation visits the pairs**

The expression

`range(1, len(s), 2)`

generates the odd indices $1,3,5,\ldots$. Each odd index `i` is the right member of one fixed pair, while `i - 1` is its left member. The comparison

`s[i] != s[i - 1]`

returns a Boolean. In Python, `False` contributes $0$ and `True` contributes $1$ when summed. Thus

`sum(s[i] != s[i - 1] for i in range(1, len(s), 2))`

is exactly the number of unequal pairs and therefore the minimum number of changes.

For example, split `1001` into `10 | 01`. Both pairs mismatch, so the answer is $2$. One possible repair is `11 | 11`; another is `00 | 00`. Either uses two changes. It is not possible to use a single change because the two mismatches occur in disjoint pairs and each independently requires a repair.

For `0011`, the fixed split is `00 | 11`. Both pairs are already homogeneous, so the answer is $0$. The whole string is not homogeneous, but that is irrelevant: the definition allows multiple even-length homogeneous substrings.

**Why the binary alphabet matters only to the construction**

For two unequal binary characters, changing either one necessarily makes it equal to the other because the only choices are `0` and `1`. More generally, if an operation allows replacing a character with any chosen character, the same one-change conclusion would hold for any alphabet. Here the binary contract makes the intended flip especially direct.

## Complexity detail

Let $n$ be the length of `s`.

The generator examines exactly $n/2$ pairs. Each comparison and Boolean addition is constant time, so total running time is $O(n)$. Reading every pair is also necessary in the worst case: an unseen pair might be the only mismatch and change the answer.

The expression is consumed directly by `sum` and does not construct a list of comparison results. Aside from the running total, current index, and generator bookkeeping, storage does not grow with $n$. Auxiliary space is $O(1)$.

The input string itself is not modified. Python strings are immutable, but the task requests only the minimum count, so constructing a repaired string would be unnecessary.

## Alternatives and edge cases

- **Dynamic programming over partition boundaries:** One could test even-length homogeneous suffixes and compute a minimum over prefixes, but the fixed-pair equivalence makes all boundary choices irrelevant. That approach adds time and state without changing the answer.
- **Greedily build maximal runs:** Counting odd-length runs can be made to work with careful reasoning, but run boundaries shift after changes and are easier to mishandle. Disjoint fixed pairs give independent, exact costs.
- **Try all possible beautiful strings:** Enumerating repairs is exponential. Each pair has an immediate local lower bound and construction, so enumeration has no value.
- **Already beautiful with several parts:** A string such as `001100` returns zero even though it is not all one character. Each pair is homogeneous, which is sufficient for a valid partition.
- **A long homogeneous run:** Any even-length run divides into equal pairs and needs no change. The method does not need to identify the run explicitly.
- **A mismatch at the beginning or end:** The odd-index range compares both endpoint pairs normally; no special boundary branch is needed.
- **Even length guarantee:** Because $n$ is even, the final character always has a partner. Without that guarantee, an unpaired final character could not itself form an even-length part and would require separate impossibility handling.
- **Changing both bits of a mismatching pair:** This is never better than changing one. One change already makes the two characters equal, so a second change only wastes an operation.
- **Merging repaired pairs:** It is unnecessary for correctness. Once every pair is homogeneous, treating pairs as separate length-two substrings already satisfies the definition.
- **Boolean arithmetic:** The source relies on Python's `bool` being a subclass of `int`. In a language without numeric Booleans, the comparison should be converted explicitly to $0$ or $1$.
