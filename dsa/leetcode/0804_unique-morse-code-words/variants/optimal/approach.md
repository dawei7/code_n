## General

**Map each lowercase letter by its alphabet index**

The list `codes` contains the 26 Morse encodings in alphabetical order:

- index zero is the code for `a`;
- index one is the code for `b`;
- continuing through index 25 for `z`.

For lowercase character `c`, the expression:

`ord(c) - ord('a')`

converts it to the corresponding zero-based alphabet index.

The input contract guarantees lowercase English letters, so every computed index is within the table.

**Transform one word by concatenation**

For each character of a word, the inner list comprehension retrieves its Morse fragment:

`codes[ord(c) - ord('a')]`.

`''.join(...)` concatenates those fragments without separators.

This matches the definition exactly. A word's transformation is not a list of per-letter codes and does not include spaces or punctuation between them.

For `"cab"`, the fragments are `"-.-."`, `".-"`, and `"-..."`. Joining them produces `"-.-..--..."`.

**Why transformation boundaries do not need preservation**

Different letter sequences may concatenate to the same dots-and-dashes string because no separator identifies where one letter code ends and the next begins.

That is intentional. The problem defines uniqueness by the final concatenated transformation, not by the original word or the sequence of fragments.

The algorithm therefore stores only the joined string. If two different words produce the same joined value, the set treats them as one transformation.

**Use a set to deduplicate**

The outer set comprehension transforms every input word and inserts the resulting string into `s`.

A set keeps at most one entry for each equal hashable string. It does not matter how many words produce a transformation; that transformation contributes one to the requested distinct count.

Finally, `len(s)` is exactly the number of different transformations.

**Trace the first example**

For words `"gin"` and `"zen"`:

- `g`, `i`, `n` concatenate to `"--...-."`;
- `z`, `e`, `n` also concatenate to `"--...-."`.

They produce one set entry.

Words `"gig"` and `"msg"` both produce `"--...--."`, creating a second entry.

The set size is therefore two even though four words were supplied.

**Every inserted string is the correct transformation**

The mapping table is aligned with alphabet order. The inner comprehension visits characters in their original left-to-right order and replaces each with exactly its table entry. Joining preserves that order.

Thus every inserted value equals the definition's Morse concatenation for its word.

**Every distinct transformation contributes exactly once**

Every input word is evaluated by the outer comprehension, so no transformation is omitted.

If two transformations are equal, set semantics retain one entry, as required for distinct counting. If they differ at any dot or dash position or in length, they are different strings and occupy separate entries.

Therefore the final set cardinality is exactly the answer.

**Why word identity is irrelevant after encoding**

The desired equivalence relation is:

$$
w_1 \sim w_2
\quad\text{if and only if}\quad
\operatorname{morse}(w_1)=\operatorname{morse}(w_2).
$$

The set stores one representative key for each equivalence class: the transformation itself. No secondary mapping from transformation back to source words is needed because the task asks only for the number of classes.

**Understand the intermediate list**

The exact source uses square brackets inside `join`:

`[codes[...] for c in word]`.

This creates a temporary list of Morse fragments for that word, then joins it.

A generator expression could feed fragments directly to `join` and avoid the explicit list object, but both produce the same transformation. Given word length at most 12, the temporary is small.

**Hashing cost is still linear in produced text**

Set insertion is expected constant time with respect to the number of set entries only after the string's hash is available. Hashing a newly built transformation examines its characters.

Each English Morse fragment has bounded length, at most four. Therefore the total transformation length is at most a constant multiple of the source word length. Building, hashing, and comparing transformations remain linear in the total input character count up to constant factors.

**The fixed table is trusted data**

`codes` is a constant 26-entry lookup table recreated on each method call. It does not grow with the input.

Its order must remain exact; a misplaced entry would systematically encode one letter incorrectly. The direct index formula avoids a longer conditional chain or repeated dictionary construction.

## Complexity detail

Let $C$ be the sum of all input word lengths. Each source character causes one constant-time table lookup and contributes a Morse fragment of length at most four. Constructing all transformations therefore writes $O(C)$ symbols.

Hashing and inserting the resulting strings also costs $O(C)$ expected total time, so overall expected time is $O(C)$.

The set may store transformations whose combined length is $O(C)$. Temporary fragment lists and the current joined string are bounded by the current word length, also no more than $O(C)$. Auxiliary/result-key space is $O(C)$. The 26-entry table is $O(1)$.

## Alternatives and edge cases

- **Dictionary letter mapping:** Map characters directly to strings. It is readable but the array plus alphabet offset is simpler for a dense lowercase alphabet.

- **Store tuples of fragments:** Incorrect for this definition because two different fragment boundaries may yield the same concatenated transformation.

- **Sort all transformations:** Sorting then counting changes works but costs $O(W\log W)$ comparisons after the same encoding work.

- **Duplicate words:** They naturally produce one identical set entry.

- **Different words, same transformation:** They also intentionally collapse to one entry.

- **One word:** Its single transformation makes the answer one.

- **One-letter word:** The transformation is exactly that letter's table entry.

- **No separators:** Adding delimiters would change the equivalence relation and can overcount.

- **Lowercase contract:** It makes `ord(c)-ord('a')` a safe direct index.
