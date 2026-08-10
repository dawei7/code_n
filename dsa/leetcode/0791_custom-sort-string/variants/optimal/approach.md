## General

**Turn the custom order into numeric ranks**

String `order` already lists its characters from earliest to latest. The dictionary comprehension:

`d = {c: i for i, c in enumerate(order)}`

assigns rank zero to the first character, rank one to the second, and so on. Characters in `order` are unique, so no later dictionary entry overwrites an earlier rank.

Once these ranks exist, arranging the constrained characters is an ordinary key-based sort: smaller rank means earlier in the result.

**Understand exactly what the output condition requires**

If character `x` occurs before character `y` in `order`, every sorted occurrence of `x` must be placed before every occurrence of `y`.

Characters that do not occur in `order` have no constraint relative to any other character. They may appear at the beginning, end, or between constrained groups. The method is therefore free to assign all such characters any convenient rank.

The exact key function is:

`lambda x: d.get(x, 0)`.

For a character in `order`, it returns the recorded index. For an absent character, `get` returns zero.

**Why default rank zero is valid**

Rank zero is also the rank of `order[0]`. Consequently, unconstrained characters are tied with the first custom-ordered character.

This does not violate the problem:

- Every first-ranked character and every absent character still has a key smaller than ranks one, two, and so on.
- The relative placement of absent characters versus the first-ranked character is unrestricted.
- All later custom-ranked groups remain in their required order.

Some implementations put absent characters after all ordered characters by using default rank `len(order)`. That is also valid, but it produces a different permitted answer. The problem accepts any satisfying permutation.

**Use stable sorting for tied characters**

Python's `sorted` is stable. Items with equal keys retain their original relative order.

This means occurrences of the same constrained character stay in their existing order, although identical characters make that invisible. All absent characters and first-ranked characters also preserve their mutual input order within the key-zero block.

Stability is convenient for predicting the exact output but is not necessary for correctness here. The custom rule places no order among absent characters and does not distinguish repeated identical characters.

**Every input character is preserved**

The algorithm sorts the characters of `s` rather than constructing characters from `order`. Therefore:

- it cannot introduce a character that was not in `s`;
- it cannot lose an occurrence;
- repeated characters retain exactly the same multiplicity.

`sorted(s, key=...)` returns a list containing one entry per character of `s`. `''.join(...)` concatenates that complete list into the returned permutation.

**Trace the first example**

Let `order = "cba"` and `s = "abcd"`. The rank map is:

- `c -> 0`;
- `b -> 1`;
- `a -> 2`.

Character `d` is absent and receives default key zero. In the original `s`, `c` occurs before `d` among the key-zero elements. Stable sorting therefore forms key blocks:

`"cd" + "b" + "a" = "cdba"`.

This differs from the sample's `"cbad"` but is valid. The constrained characters occur in `c`, `b`, `a` order, and `d` may appear anywhere.

**Trace an absent character before the first-ranked one**

With the same custom order and `s = "dcba"`, both `d` and `c` have key zero. Stability keeps their order as `"dc"`, followed by `b` and `a`. The output is `"dcba"`.

The leading `d` is legal because `d` has no stated relationship to `c`, `b`, or `a`.

**Why the sort satisfies every pairwise constraint**

Take any two characters `x` and `y` that both occur in `order`, with `x` earlier than `y`. Their ranks satisfy:

$$
d[x] < d[y].
$$

A key-based ascending sort places every item with key `d[x]` before every item with key `d[y]`. Thus every required pairwise relationship holds in the result.

All output characters came from `s` exactly once, and unconstrained characters can occupy their key-zero positions freely. Therefore the returned string is a valid permutation satisfying the custom order.

**Why a comparison sort is more work than the alphabet requires**

The exact solution is concise, but lowercase English letters form a small fixed alphabet. A frequency table could count `s`, emit characters in `order`, and then emit leftovers without comparison sorting.

That counting method is the genuinely linear approach described by the editorial and reflected in the manifest. The exact source instead delegates to Python's general-purpose sorting routine. The approach must distinguish those algorithms rather than claiming the counting bound for code that calls `sorted`.

## Complexity detail

Let $m$ be the length of `order` and $n$ the length of `s`. Building the rank dictionary costs $O(m)$ expected time and $O(m)$ space.

Python sorting evaluates keys for $n$ characters and performs $O(n\log n)$ worst-case comparison-sort work. Joining the sorted list costs $O(n)$. The exact total is therefore:

$$
O(m+n\log n).
$$

The sorted character list and final output contain $n$ characters, while the dictionary contains $m$ ranks. The exact implementation uses $O(m+n)$ additional/output storage under the usual Python accounting.

The manifest lists $O(m+n)$ time and $O(u)$ space. Those bounds correspond to frequency counting over $u$ distinct characters, as in the editorial's second approach, not to this exact `sorted`-based source. With the fixed 26-letter alphabet, `m` and `u` are bounded constants, but sorting $n$ input characters still has the stated comparison-sort cost.

## Alternatives and edge cases

- **Frequency counting:** Count characters in `s`, emit ordered groups following `order`, then emit leftovers. This achieves $O(m+n)$ time and is the method matching the manifest.

- **Default leftovers after the order:** Use key `d.get(x, len(order))` to place absent characters at the end. It remains valid but differs from the exact source's output placement.

- **Custom comparator:** Compare characters by rank directly, but repeated map lookups and comparator calls are more cumbersome than a key function.

- **Characters absent from `order`:** They all receive key zero and may legally appear anywhere relative to constrained characters.

- **First-ranked character:** It shares a key with absent characters, which is safe because their mutual order is unrestricted.

- **Repeated characters:** Sorting preserves their count and groups equal ranked occurrences appropriately.

- **All characters absent:** Every key is zero, so stable sorting returns `s` unchanged, which is valid.

- **All characters constrained:** Rank blocks follow `order` exactly.

- **Any valid output:** Matching the sample's particular leftover placement is not required.
