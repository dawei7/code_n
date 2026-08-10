## General

**Similarity preserves relative cyclic offsets**

Uniformly shifting every character adds the same amount modulo 26. Therefore the cyclic difference between each character and the first character stays unchanged.

Two equal-length words are similar exactly when these relative offsets match at every position.

The source creates a canonical representative by shifting each word so its first character becomes `z`.

**Compute the canonical shift**

For first character `t[0]`, the shift amount is

`k = ord("z") - ord(t[0])`.

Adding this amount modulo 26 maps the first character's alphabet index to 25, which is `z`.

For every later character, the source applies the same cyclic shift:

`(ord(t[i])-ord("a")+k)%26`.

It then explicitly sets `t[0]="z"`. The resulting joined string is the canonical key.

**Why equal keys mean similarity**

If two words differ by a uniform cyclic shift, shifting each so its first letter becomes `z` removes that global difference. Their corresponding normalized letters match.

Conversely, if normalized keys match, undoing each word's normalization shows their original letters differ by one fixed shift—the difference between their first letters. Applying that shift makes the words equal.

Thus key equality is equivalent to the problem's similarity relation.

For the length-one case, every word normalizes to `"z"`, which is correct because any single lowercase letter can be cyclically shifted into any other.

**Count groups rather than comparing pairs**

`cnt[key]` records how many words share a normalized form. A group of size `v` contributes

$$
\binom v2=\frac{v(v-1)}2
$$

index pairs.

Summing this over keys counts every similar pair once. Equal original strings at different indices share a key and correctly form pairs.

The source first builds all counts and then computes combinations. An equivalent streaming version could add the number of earlier equal keys as each word arrives.

**Trace a wraparound**

For `"ab"`, shifting first `a` to `z` means adding 25: `a->z` and `b->a`, giving key `"za"`.

For `"za"`, shift amount zero gives the same key `"za"`. Their equality proves the pair is similar despite alphabet wraparound.

**Why positions and lengths remain aligned**

All words share length `m`. Normalization changes characters but never position or length, so key comparison checks every corresponding offset.

The common-length guarantee avoids any need to include length in the dictionary key.

**View the key as relative offsets**

Writing letters as values zero through 25, normalized position `i` equals

$$
(value(s[i])-value(s[0])+25)\bmod26.
$$

It depends only on the cyclic offset from the first character. The loop begins at index one because the first normalized character is known to be `z` and is assigned directly afterward.

Similarity is an equivalence relation: a zero shift gives reflexivity, reversing a shift gives symmetry, and composing shifts gives transitivity. The canonical key names one equivalence class.

The combination `v(v-1)/2` chooses two distinct indices from a class without order. This matches the requested `i<j` condition because every unordered pair has one increasing order.

The operation may shift either word. Algebraically, shifting them by amounts `a` and `b` makes them equal exactly when their original positions differ uniformly by `b-a`. Normalization removes that one global difference.

If a word begins with `f`, the source adds 20 modulo 26 to every later letter while setting the first to `z`. Any uniformly shifted version of that word produces the same key.

Dictionary groups are disjoint: every word creates exactly one canonical string and increments exactly one counter. Summing combinations across counters therefore cannot count one index pair in two different groups.

## Complexity detail

Let $S$ be the total number of input characters. Each word is copied to a list, normalized, and joined in time proportional to its length. Total time is $O(S)$, plus $O(N)$ to sum group combinations, which is covered because every word is nonempty.

Canonical strings and temporary character lists contain $O(S)$ characters in the worst case. The dictionary also has at most $N$ keys, so auxiliary space is $O(S)$.

## Alternatives and edge cases

- **Compare every word pair:** This costs $O(N^2M)$ instead of grouping once.
- **Store numeric offset tuples:** They are an equally valid canonical key; the source stores a normalized string.
- **Shift without modulo:** Letters near `z` must wrap to `a`.
- **Normalize each position independently:** One uniform shift must be applied to the whole word.
- **Normalize first letter to `a`:** Also valid with a different shift formula; the source chooses `z`.
- **One-character words:** All pairs are similar.
- **Duplicate words:** Distinct indices still contribute combinations.
- **No matching keys:** The sum is zero.
- **Alphabet wraparound:** Modulo 26 handles it.
- **Input preservation:** Each word is copied before character replacement.
- **Pair orientation:** The combination formula counts each `i<j` pair once.
- **First position:** It is assigned directly after later positions use the shared shift.
- **Uniformity:** One shift amount governs every position.
- **Unique grouping:** Each word contributes to exactly one canonical-key counter.
