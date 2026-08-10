## General

**Define a prefix subproblem**

Let `f[i]` be the minimum number of extra characters in prefix `s[:i]`, the first $i$ characters.

The empty prefix needs no extras, so `f[0] = 0`.

When computing `f[i]`, every valid optimal arrangement of this prefix ends in one of two ways:

- character `s[i - 1]` is extra;
- some dictionary word occupies a suffix `s[j:i]`.

Considering both possibilities gives a complete recurrence.

**Default to treating the final character as extra**

The assignment `f[i] = f[i - 1] + 1` takes an optimal arrangement for the first $i-1$ characters and leaves the new final character unused.

This transition is always legal, even when no dictionary word matches.

It also provides a finite upper bound for `f[i]` before word transitions are tried.

**Try every possible word start**

For fixed endpoint `i`, the loop tests `j` from zero through $i-1$.

Substring `s[j:i]` is the candidate final dictionary word. If it belongs to set `ss`, then all its characters can be covered with zero additional extras.

The preceding prefix contributes `f[j]`, so the transition is:

$$
f[i]=\min(f[i],f[j]).
$$

The source writes the comparison explicitly as `f[j] < f[i]` before assignment.

**Why words do not overlap**

The prefix state `f[j]` uses only characters before index `j`.

The candidate word uses indices `j` through `i-1`. These ranges are adjacent and disjoint.

Chaining such transitions therefore constructs non-overlapping dictionary substrings automatically, without storing their actual segmentation.

**Why every optimal segmentation is represented**

Take an optimal arrangement for `s[:i]`.

If its last character is unused, it corresponds to the default transition from `f[i-1]`. Otherwise the last covered block must be a dictionary word ending at `i` and starting at some `j`, corresponding to one loop transition from `f[j]`.

Thus at least one tested transition reproduces the optimum, while every tested transition is a valid arrangement. The minimum is exact.

**Trace `"leetscode"`**

When `i = 4`, substring `s[0:4]` is `"leet"`, so `f[4]` can become `f[0] = 0`.

At index four, the character `s` is not part of the chosen words, so the next prefix can have value one.

At the full endpoint, suffix `"code"` starts at index five. Its transition carries `f[5] = 1` to `f[9]` without adding extras.

The final answer is one.

**Convert the dictionary to a set**

`ss = set(dictionary)` allows membership lookup by word value rather than scanning all dictionary entries for every substring.

The dictionary contains distinct words already, but the set still provides expected constant-time table lookup after hashing.

Its construction preserves only membership, which is all the recurrence needs.

**The DP is bottom-up**

Endpoints are processed from one through $n$.

Every transition for `f[i]` reads `f[i-1]` or `f[j]` with $j<i$, so those states are already final.

No recursion or memoization is needed, and `f[n]` directly answers the complete string.

**Exact implementation does not use a trie**

The manifest summary describes a reversed trie and states $O(n^2+W)$ time.

The checked-in source instead creates every substring `s[j:i]` and checks a hash set. There is no trie and no prefix-walk early stopping.

That affects concrete character-time complexity and must not be hidden in the explanation.

**Substring cost in Python**

Python slicing creates a new string of length $i-j$, and hashing that new string for set lookup also processes its characters.

There are $O(n^2)$ candidate pairs, but the sum of their substring lengths is $O(n^3)$. Thus the exact source has a worst-case $O(n^3)$ character-processing bound, even though it performs $O(n^2)$ logical DP transitions.

With $n\le50$, this remains practical.


The prefix invariant says each stored state is the minimum extras for its prefix. The extra-character transition covers all solutions ending unused, and every matching-word transition covers all solutions ending with a word.

These cases exhaust the final status of character $i-1$. Taking their minimum preserves the invariant by induction. Consequently `f[n]` is the globally minimum number of extra characters.

## Complexity detail

Let $n=\lvert s\rvert$ and let $W$ be the total dictionary character count. Set construction costs $O(W)$ expected time and space.

The DP performs $O(n^2)$ substring tests. Because Python creates and hashes slices of length up to $n$, worst-case character time is $O(n^3+W)$, not the manifest's trie bound. Array `f` uses $O(n)$ space, the set uses $O(W)$, and one transient substring uses $O(n)$.

## Alternatives and edge cases

- **Trie-based DP:** Avoids substring construction and realizes $O(n^2+W)$ time, but is not the exact source.
- **Top-down memoization:** Uses the same recurrence from starting positions with recursion.
- **Scan every dictionary word at each index:** Can be effective when dictionary words are short but has different bounds.
- **No dictionary match:** Every default transition is used and the answer is $n$.
- **Whole string is a word:** Transition from `f[0]` makes the answer zero.
- **Overlapping word candidates:** DP chooses compatible non-overlapping transitions.
- **Duplicate dictionary words:** A set would collapse them without changing membership, though inputs are distinct.
- **One-character words:** Can cover individual positions with zero extra cost.
- **Extra characters between words:** Default transitions count them one by one.
- **Input preservation:** Neither `s` nor `dictionary` is modified.
