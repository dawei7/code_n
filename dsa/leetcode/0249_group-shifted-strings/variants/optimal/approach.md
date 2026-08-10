## General

Shifting a string means adding the same alphabet offset to every character, with wraparound between `z` and `a`. The absolute letters can change, but the string's relative cyclic shape cannot. To group strings efficiently, the solution converts every member of a shifting sequence to one shared canonical form and uses that form as a dictionary key.

The exact source chooses a particularly intuitive canonical form: shift the string so its first character becomes `a`. Once the required shift is fixed by the first character, every other character must move by the same amount. Strings belonging to the same shifting sequence then normalize to the same text.

For example:

```text
"abc" -> "abc"   (subtract 0)
"bcd" -> "abc"   (subtract 1 from every letter)
"xyz" -> "abc"   (subtract 23 from every letter, wrapping around)
```

All three therefore become keys in the same dictionary bucket.

**Compute the normalization offset**

The value

```text
diff = ord(s[0]) - ord("a")
```

is the zero-based alphabet index of the first character. It lies from `0` for `a` through `25` for `z`. Subtracting `diff` from the code of the first character always turns it into `ord('a')`.

For each character `c`, the solution computes `ord(c) - diff`. If this falls below `ord('a')`, it adds `26` to wrap back into the lowercase alphabet. Only one addition can be needed: the original code is at least `ord('a')`, and `diff` is at most `25`, so the intermediate result is never more than 25 positions below `a`.

The normalized characters are accumulated in `t`, joined into one string, and used as the key in `g`. The original string—not the normalized copy—is appended to that key's group so the returned data contains the inputs as requested.

**Wraparound is part of the identity**

Ordinary subtraction without modulo behavior would group `az` incorrectly. For `s = "az"`, `diff = 0`, so the key remains `"az"`. For `s = "ba"`, `diff = 1`: `b` becomes `a`, while subtracting one from `a` falls just before the alphabet and is corrected by adding `26`, producing `z`. Its key is also `"az"`.

This matches the shifting sequence: one left shift turns `ba` into `az`. The wrap step is therefore essential, not merely a character-code repair.

**Why canonicalization groups exactly the right strings**

Represent letters by numbers in $\{0,1,\ldots,25\}$. If a string has values $x_0,x_1,\ldots,x_{m-1}$, its canonical form is

$$
(0,\;x_1-x_0,\;x_2-x_0,\ldots,x_{m-1}-x_0)\pmod{26}.
$$

First assume two strings are in the same shifting sequence. Then there is one offset $q$ such that every corresponding letter of the second string equals the first plus $q$ modulo 26. Subtracting each string's own first letter cancels that common offset, so their canonical forms are equal.

Conversely, assume two strings have equal canonical forms. At every position, each character's offset from its own first character is the same. Shifting the first string by the cyclic difference between the two first characters therefore makes every position equal to the second string. Thus equal keys imply membership in the same shifting sequence.

The key also preserves length because it is a string containing one normalized character per input character. Strings of different lengths cannot accidentally share a key even if their initial patterns look similar.

**Trace through the representative input**

For

```text
["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
```

the canonical keys are:

| Original | Canonical key | Reason |
|---|---|---|
| `abc` | `abc` | first letter is already `a` |
| `bcd` | `abc` | subtract one from each letter |
| `xyz` | `abc` | subtract 23 with wraparound |
| `acef` | `acef` | first letter is already `a` |
| `az` | `az` | first letter is already `a` |
| `ba` | `az` | subtract one; `a` wraps to `z` |
| `a` | `a` | one-character canonical form |
| `z` | `a` | subtract 25 from `z` |

The dictionary values consequently form the groups `['abc', 'bcd', 'xyz']`, `['acef']`, `['az', 'ba']`, and `['a', 'z']`. The problem permits any group order, so returning `list(g.values())` is sufficient.

**Exact source versus the manifest summary**

The manifest describes a tuple of adjacent differences modulo 26. That is another valid shift-invariant signature, but the protected source instead normalizes every character relative to the first character and uses the resulting string. These representations contain equivalent information: adjacent differences can be accumulated to recover offsets from the first character, and first-relative offsets can be subtracted to recover adjacent differences. The approach here follows the normalization actually executed.

## Complexity detail

Let

$$
L=\sum_{s\in\texttt{strings}}\lvert s\rvert
$$

be the total number of input characters. Every character is converted, shifted, appended to a temporary list, and copied into its joined key once. Expected dictionary insertion is constant time apart from hashing the key, whose character work is already proportional to its length. Total expected time is therefore $O(L)$.

The dictionary's group lists store references to all input strings, using $O(N)$ slots for $N$ strings. The canonical keys collectively can contain up to $L$ characters, and the largest temporary normalization list is bounded by the longest string. Since every string has at least one character, $N\le L$, so total auxiliary and result-grouping storage is $O(L)$.

The returned nested lists themselves contain $N$ references and are part of the output. Even excluding those lists, retained canonical keys can still require $O(L)$ space in the worst case when many distinct shift classes exist.

## Alternatives and edge cases

- **Adjacent-difference tuple:** Record `(s[i] - s[i-1]) mod 26` for every adjacent pair. It is shift-invariant and is the representation summarized by the manifest. The exact source uses the equally valid first-letter normalization.
- **Compare every pair of strings:** Test whether one constant shift converts each pair and merge matches. This repeats character work and can take quadratic time in the number of strings.
- **Generate each string's full shifting sequence:** A string has at most 26 distinct shifts, so it could be matched through all variants, but canonicalizing once is simpler and avoids storing unnecessary forms.
- **Single-character strings:** Every one-letter lowercase string can shift into every other. Normalization maps all of them to the one-character key `a`, so they form one group.
- **Wrap from `a` below the alphabet:** Adding `26` after subtraction restores the correct cyclic character, as in `ba -> az`.
- **Different lengths:** The canonical key retains length, so a one-character string cannot be grouped with a two-character string.
- **Repeated identical strings:** They have the same key and are appended as separate input entries. The grouping preserves duplicates rather than deduplicating them.
- **Already normalized strings:** A string beginning with `a` has `diff = 0` and becomes its own key.
- **All `z` characters:** Subtracting 25 maps each `z` to `a`, so `zzz` shares a group with `aaa` and every other constant three-letter string.
- **Dictionary ordering:** Modern Python preserves insertion order, but the contract explicitly allows any output order. Correctness depends only on group membership.
- **Empty strings:** The source accesses `s[0]`, but the constraints guarantee every string has length at least one. Supporting empty strings would require assigning them a separate empty key.
- **Non-lowercase characters:** The arithmetic assumes contiguous lowercase English codes and a 26-letter cycle. Broader alphabets would require a contract-specific mapping rather than this fixed offset.
