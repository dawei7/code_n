## General

**Reduce the problem to how many character kinds must survive**

The operations describe positions, directions, and the closest equal character, so the process initially looks as though it requires a careful simulation. The key simplification is to ask what can happen to one letter independently of every other letter.

Suppose the string contains several copies of `'a'`. Choosing any surviving `'a'` lets us delete the closest `'a'` on one side whenever such a copy exists. The operation never changes an `'a'` into another letter, and deleting an `'a'` has no direct effect on the number of copies of `'b'`, `'c'`, or any other character. Therefore each distinct character can be analyzed separately.

**Why every distinct character contributes at least one**

An operation deletes an occurrence of character `c` only by choosing another occurrence of that same `c`. Consequently, deleting a copy requires a different copy to act as the anchor. Once only one `c` remains, there is no second `c` to its left or right, so that last occurrence cannot be removed.

This gives an unavoidable lower bound: every character that appears in the original string must appear at least once in the final string. If the input contains $D$ distinct letters, no legal sequence can make the length smaller than $D$.

This is stronger than merely observing that the operations preserve character values. It explains the exact obstruction: the final occurrence has no equal partner that could delete it.

**Why all duplicate occurrences really can be deleted**

The lower bound is useful only if it is attainable. Fix one character `c` that occurs $r$ times. If $r>1$, select any occurrence that has another `c` on its left or right. The corresponding operation removes the closest equal occurrence on that side, reducing the count from $r$ to $r-1$.

Repeat while at least two copies remain. At every intermediate count greater than one, some pair of occurrences exists. Take the left occurrence of any adjacent pair of `c` occurrences in their current order and delete the closest `c` to its right. That right occurrence is guaranteed to exist and to be the closest equal character in that direction. Thus the rule about “closest” never prevents progress.

After $r-1$ deletions, exactly one `c` remains. Performing this independently for every distinct character leaves exactly one occurrence of each kind, for total length $D$. Since $D$ is both a lower bound and achievable, it is the minimum.

**Why positions and deletion order do not matter to the answer**

Deleting characters shifts later indices, but the solution never needs stable indices. It reasons only about occurrence counts. A deletion of one letter cannot create or destroy an occurrence of another letter, and the relative order of the remaining copies of any fixed letter is enough to choose another legal deletion.

Operations for different letters may be interleaved in any order. They commute with respect to the only quantity that matters: each letter's remaining count. This is why no greedy position selection, linked list, or mutable-string simulation is needed.

**What the exact implementation computes**

Python's `set(s)` keeps one representative for every different character in `s`. Calling `len` on that set returns $D$, precisely the proven optimum. The code does not construct the minimized string because the contract asks only for its length.

For `s = "aaabc"`, the set is `{'a', 'b', 'c'}`, so the answer is three. Two of the three `'a'` characters can be removed, while the final `'a'` and the sole `'b'` and `'c'` cannot be removed.

For `s = "baadccab"`, the distinct letters are `'a'`, `'b'`, `'c'`, and `'d'`. The frequencies differ, but each positive frequency collapses to exactly one, so the result is four.

For a string such as `"zzzz"`, the set has size one. Three deletions can leave one `'z'`, but the last copy has no equal partner and must remain.

**A compact correctness chain**

Every original character kind has a last occurrence that no operation can delete, so any result has length at least the number of distinct characters. For each character kind, repeated legal deletions reduce all of its duplicates to one. Hence a string with exactly one copy of every distinct character is reachable. The exact solution returns the size of that distinct-character set, so it returns the minimum possible length.

## Complexity detail

Let $n$ be the length of `s` and let $D$ be its number of distinct characters. Building `set(s)` examines all $n$ characters, so the expected running time is $O(n)$. Hash-table operations on individual one-character strings are expected $O(1)$.

The set stores $D$ characters, giving $O(D)$ auxiliary space in a general alphabet. Here the input contains only lowercase English letters, so $D\le 26$. Under the problem's fixed alphabet, that storage is bounded by a constant and is correctly summarized as $O(1)$ auxiliary space. The distinction matters: the implementation does allocate a set, but its maximum size does not grow beyond 26 for legal inputs.

The solution performs no deletions and creates no minimized output string. Its work depends on reading the input once, not on the potentially much larger number of imagined position shifts in a literal simulation.

## Alternatives and edge cases

- **Frequency array:** Count the 26 lowercase letters and return how many counts are positive; it has the same $O(n)$ time and fixed $O(1)$ space but is more verbose than a set.
- **Repeated deletion simulation:** Can reproduce a valid operation sequence, but mutable-string deletions and searches add unnecessary work because only distinctness affects the answer.
- **Sort and count changes:** Sorting the characters and counting new groups works in $O(n\log n)$ time, which is slower than hashing.
- **Single-character string:** Its only occurrence cannot be deleted, so the set size and answer are one.
- **All characters equal:** Every copy except one is removable, producing answer one.
- **All characters distinct:** No operation is possible because no selected character has an equal occurrence on either side; the answer remains $n$.
- **Separated duplicates:** Equal characters need not be adjacent. The closest-equal rule still permits deleting one copy because intervening different letters do not matter.
- **Changing indices:** Indices shift after conceptual deletions, but the set computation deliberately avoids depending on them.
- **Lowercase guarantee:** The fixed 26-letter alphabet is what turns $O(D)$ set storage into the manifest's $O(1)$ bound.
