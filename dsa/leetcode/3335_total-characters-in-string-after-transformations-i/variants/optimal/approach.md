## General

**Track counts rather than the exponentially growing string.** Character order does not matter when only final length is requested. Every occurrence of a letter transforms identically, so the state after each round is completely described by 26 frequencies.

`f[i][j]` is the number of occurrences of alphabet index $j$ after exactly $i$ transformations. Row zero counts characters in the original string through `ord(c) - ord("a")`.

**Derive the simultaneous transition.** Every original `a` becomes `b`, every `b` becomes `c`, and generally old letter $j-1$ becomes new letter $j$. Old `z` is special: it creates both `a` and `b`.

Therefore:

- new `a` count is old `z` count;
- new `b` count is old `a` plus old `z`;
- for letters `c` through `z`, new count at index $j$ is old count at $j-1$.

The source assigns exactly these equations. Because every entry in row $i$ reads only row $i-1$, all replacements are simultaneous; newly created characters do not transform again within the same round.

After $t$ rounds, summing all 26 frequencies gives the resulting length. The final `% mod` returns the requested residue.

**Example flow.** In `"abcyy"`, the first transformation shifts `a,b,c` to `b,c,d` and both `y` copies to `z`, giving counts for `"bcdzz"`. In the next row, the two old `z` copies each add one `a` and one `b`, while the other letters shift, producing total length seven.
Row zero is the exact initial multiset. Assume row $i-1$ is exact. Every old non-`z` occurrence contributes one copy to its unique next-letter cell, and every old `z` contributes one to cells zero and one. The recurrence sums exactly these contributions and no others, making row $i$ exact. Induction reaches row $t$, whose frequency sum is the length.

**The mathematical recurrence is sound, but the exact numeric implementation is problematic.** Counts are never reduced modulo $10^9+7$ while rows are built. A `z` branches into two characters, and repeated transformations can make counts exponentially large. Python integers are unbounded, so results remain mathematically exact, but arithmetic cost and memory per integer grow with the number of bits. Applying modulo only at the final sum does not prevent this growth.

At $t=10^5$, storing exact enormous counts is potentially infeasible. Modular reduction at every assignment or addition is safe because only the final residue is needed.

**The source also stores every row.** It allocates `(t + 1) * 26` entries, even though each row depends only on its predecessor. The manifest and editorial describe constant-alphabet rolling space, but the protected source uses $O(t)$ rows with respect to $t$. This is another material discrepancy.

## Complexity detail

Counting the input costs $O(n)$. The table performs 26 assignments per transformation, an arithmetic-operation count of $O(26t)=O(t)$ for fixed alphabet. Structurally, this suggests $O(n+t)$ time.

However, without intermediate modulo, integer bit lengths can grow with $t$, so each addition/copy is not constant-time in a bit-complexity model. Practical time can be much worse. The table stores $26(t+1)$ arbitrary-precision integers, giving $O(t)$ entry space plus potentially very large bit storage. The exact source is not $O(1)$ auxiliary space; rolling modular arrays would be.

## Alternatives and edge cases

- **Two 26-entry arrays:** Build a fresh next-frequency row modulo the modulus and replace the current row. This achieves $O(n+t)$ word operations and $O(1)$ alphabet space.
- **In-place careful rotation:** It can reduce allocations further but is easier to corrupt because `z` feeds two destinations.
- **Materialize the string:** Length can grow exponentially, making direct construction impossible.
- **No original `z`:** Length stays unchanged until shifted characters eventually reach `z`.
- **A `z` occurrence:** It increases total length by one in the next transformation because one character becomes two.
- **Exactly one transformation:** The answer is original length plus the original number of `z` characters.
- **Simultaneous semantics:** Newly created `a` and `b` from `z` wait until the next row before transforming again.
- **Modulo timing:** Reducing each new count modulo $10^9+7$ preserves the final answer and prevents enormous integers.
- **Full table:** Earlier rows are never read after the next row is built, so retaining them has no functional benefit.
- **Maximum `t`:** The unmodded full-table source may be impractical despite its concise arithmetic-operation count.
- **Manifest discrepancy:** Actual structural space is $O(t)$, not $O(1)$, and unbounded integer growth weakens the claimed time model.
- **Input preservation:** The original string is only counted and never transformed in memory.
- **Why order is unnecessary:** Transformation output order matters if the final string itself is requested, but total length is additive across characters. Frequencies retain exactly the information needed for length and discard nothing relevant.
- **Final-only modulo is mathematically correct:** Delaying the remainder does not change the final residue; the problem is computational efficiency, because exact intermediate integers become unnecessarily huge.
- **Row-zero allocation:** The table includes the original distribution as transformation zero, making `f[t]` align directly with the requested number of rounds.
