## General

**Similarity depends on presence, not frequency or order**

Two words are similar when the set of distinct characters occurring in one equals the set occurring in the other.

For example, `"aba"` and `"aabb"` are both represented by the set $\{a,b\}$. Repetition counts do not matter, and character order does not matter.

Since input uses only 26 lowercase English letters, one integer can encode the whole set with one bit per letter.

**Build a 26-bit signature**

Start `x=0` for each word. `map(ord,s)` yields the numeric code point of each character. Subtracting `ord("a")` converts:

- `'a'` to position 0;
- `'b'` to position 1;
- $\ldots$
- `'z'` to position 25.

`1<<(c-ord("a"))` creates an integer with exactly that letter's bit set. The bitwise OR assignment

`x |= ...`

adds the letter to the signature.

OR is idempotent: setting the same bit repeatedly has no further effect. Therefore, `"aba"` and `"aabb"` both end with bits 0 and 1 set and receive the same signature.

Two signatures are equal exactly when all 26 character-presence decisions agree, which is exactly the definition of similar strings.

**Count matching earlier signatures online**

`cnt` maps each mask to the number of earlier words with that mask. When the current word produces mask `x`, every one of those earlier words forms a valid pair with the current word.

The code first adds

`ans += cnt[x]`

and then records the current word with

`cnt[x] += 1`.

This order enforces `i<j` naturally. The current word pairs only with earlier occurrences and never with itself. Later matching words will count it when their turn arrives.

**Why a group of size `g` yields all pairs**

Suppose a particular mask occurs in `g` words. The successive contributions are

$$
0+1+2+\cdots+(g-1)
=
\frac{g(g-1)}{2}.
$$

That is exactly the number of unordered index pairs in the group. Online counting obtains this total without a second pass or an explicit combination formula.

**Trace the second sample**

For `["aabb","ab","ba"]`, all three words produce the same two-bit mask:

- the first sees zero earlier matches and then makes the count one;
- the second sees one earlier match and makes the count two;
- the third sees two earlier matches.

The answer is $0+1+2=3$, representing all three index pairs.

**Why different masks must not match**

If two masks differ, at least one bit is set in only one of them. The corresponding letter occurs in one word and not the other, so their character sets differ and the words are not similar.

Conversely, if their character sets differ, some letter has different presence, producing a different bit. The encoding has no collisions within the 26-letter alphabet.

**No sorting or set object per word is needed**

A direct representation such as `frozenset(s)` would also be a valid dictionary key, but it allocates a set-like object containing characters. The integer mask is compact, hashable, and cheap to compare.

Sorting every word would retain repeated letters and require extra work before duplicates could be removed. The mask constructs the exact needed set in one scan.

**Input and numeric safety**

Only the lowest 26 bits are used, so the signature fits easily in a standard 32-bit unsigned integer. At most 100 words create at most 4,950 pairs, though the counting pattern also works for much larger inputs.

The words are non-empty, but an empty word would simply receive mask zero; no special logic is otherwise required.


For every current word, `cnt[x]` is precisely the number of indices `i<j` whose word has the same character set, because masks exactly encode those sets. Adding that count creates every valid pair ending at `j` once. No pair can be added at another ending index, and unequal masks add nothing.

Summing across all current indices therefore returns exactly the requested pair count.

## Complexity detail

Let

$$
S=\sum_{w\in\texttt{words}}\lvert w\rvert.
$$

Every character causes constant-time code-point, shift, and OR work, so mask construction takes $O(S)$. Expected counter lookup and update take $O(1)$ per word, adding $O(n)$, which is already bounded by $O(S)$ because words are non-empty.

The counter stores at most one entry per word and at most $2^{26}$ possible masks, giving $O(n)$ auxiliary space. The current mask uses constant space.

## Alternatives and edge cases

- **`frozenset` key:** It directly represents distinct characters but allocates more objects than an integer mask.
- **Sorted unique characters:** It works but requires sorting and deduplication per word.
- **Repeated letters:** They set an already-set bit and do not alter the signature.
- **Anagrams:** They necessarily share a mask, but similarity is broader because multiplicities may differ.
- **Same length not sufficient:** Two equal-length words can contain different character sets.
- **One word:** No index pair exists, so the answer is zero.
- **All masks equal:** The result is $n(n-1)/2$.
- **Current word:** It is inserted only after counting, preventing a self-pair.
- **Lowercase contract:** Subtracting `ord("a")` relies on letters being between `a` and `z`.
- **Counter frequencies:** A set of masks would lose how many earlier matching words exist.
