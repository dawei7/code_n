## General

**A swap's effect depends only on the two character values**

Swapping one occurrence of character `c1` from `word1` with one occurrence of `c2` from `word2` changes frequencies, not string order.

For a chosen character value, every occurrence has the same effect. Therefore, it is sufficient to examine pairs of distinct character keys present in the two counters rather than every pair of string indices.

The lowercase alphabet has only 26 possibilities, so at most $26^2=676$ character-value pairs are tested.

**Count current frequencies and distinct totals**

`cnt1` and `cnt2` store character frequencies. Their key counts

`x=len(cnt1)` and `y=len(cnt2)`

are the initial numbers of distinct characters.

For every present `c1` with frequency `v1` and present `c2` with frequency `v2`, the algorithm computes what the distinct totals would become after swapping one occurrence.

**Case one: swap equal characters**

If `c1==c2`, both strings give away and receive the same character. Their frequency maps and distinct counts remain unchanged.

Because exactly one move is required, this is still a legitimate move: choose an occurrence of that shared character in each string and swap them.

It succeeds exactly when current totals already match, `x==y`.

If the totals differ, an equal-character swap cannot change them and is useless.

**Case two: swap different characters**

For `word1`:

- removing `c1` decreases its distinct count by one exactly when `v1==1`;
- receiving `c2` increases its distinct count by one exactly when `cnt1[c2]==0`.

Thus its new total is

`a=x-(v1==1)+(cnt1[c2]==0)`.

For `word2`:

- removing `c2` decreases its total exactly when `v2==1`;
- receiving `c1` increases its total exactly when `cnt2[c1]==0`.

Its new total is

`b=y-(v2==1)+(cnt2[c1]==0)`.

Python Booleans act as zero or one, so these formulas implement the frequency boundary changes directly.

**Why frequency one is the removal boundary**

If a character appears once, giving away that occurrence eliminates the key entirely. If it appears twice or more, at least one copy remains and the character is still distinct in the string.

Similarly, receiving a character creates a new distinct key only when its old frequency is zero.

No other frequency magnitude matters for distinct counts.

**Trace `"abcc"` and `"aab"`**

Initial distinct sets are $\{a,b,c\}$ and $\{a,b\}$, so `x=3` and `y=2`.

Choose `c1=c` from the first word, where frequency is two, and `c2=a` from the second, where frequency is two.

- First word keeps another `c` and already has `a`, so `a=3-0+0=3`.
- Second word keeps another `a` but does not have `c`, so `b=2-0+1=3`.

The totals match, and the method returns true.

**Why all possible moves are covered**

Any legal index swap selects some character `c1` occurring in `word1` and some `c2` occurring in `word2`. The nested loops visit that exact value pair.

The computed formulas depend only on their frequencies and presence, so they reproduce the selected index swap's distinct totals. If any move works, its pair makes the algorithm return true.

Conversely, every tested pair comes from actual counter items, so occurrences exist at legal indices. If its computed totals match, swapping those occurrences realizes the result. Thus true returns are constructive.

**Exactly one move versus at most one**

When distinct counts already match, the answer is not automatically true unless some one-swap choice preserves equality. The enumeration checks this explicitly.

In practice, swapping a shared equal character preserves both strings when one exists; swapping different characters may also preserve equality. The source does not assume and instead tests every available pair.

**No string construction**

The method never builds the swapped words. Frequency-delta arithmetic is enough, saving work proportional to string length for each candidate.

## Complexity detail

Let $N=\lvert\texttt{word1}\rvert+\lvert\texttt{word2}\rvert$. Building both counters costs $O(N)$ expected time.

The nested loops test at most $26^2$ pairs, a fixed constant. Total expected time is $O(N)$.

Each counter stores at most 26 entries, so auxiliary space is $O(1)$ relative to input length.

## Alternatives and edge cases

- **Simulate every index pair:** It can cost $O(|word1||word2|)$ and repeats identical character-value effects.
- **Equal characters:** Swapping them changes nothing and works only if totals already match.
- **Frequency one:** Removing the selected occurrence deletes a distinct character.
- **Frequency above one:** The character remains represented after removal.
- **Incoming character already present:** It does not increase the distinct count.
- **Disjoint alphabets with equal totals:** Swapping one unique character from each may preserve equal counts.
- **Single-character strings:** The sole swap can be evaluated by the same formulas.
- **Exactly one move:** A no-op equal-character swap is legal only when that character occurs in both strings.
- **Lowercase alphabet:** It bounds candidate character pairs by 676.
- **Counters:** They let character identities stand in for all equivalent index choices.
