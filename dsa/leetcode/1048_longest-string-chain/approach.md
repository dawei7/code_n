## General

**Turn the chain into a length-ordered dynamic program**

Every predecessor is exactly one character shorter than its successor. Chain lengths therefore increase by one at every step.

The input's original order is irrelevant, so the code sorts `words` by string length. Once a word at index `i` is processed, every possible predecessor must already appear somewhere before it. This turns the predecessor relation into an acyclic left-to-right dependency.

Let `dp[i]` be the maximum chain length whose final word is `words[i]`. Every word alone forms a chain of length one, so the array begins with ones.

**Test whether one word is a predecessor**

The helper `check(w1, w2)` first requires `len(w2) - len(w1) == 1`. Inserting exactly one character must increase length by exactly one. Equal lengths, a larger gap, or reversed lengths fail immediately.

Two pointers then scan the strings:

- `i` points to the next unmatched character of shorter `w1`.
- `j` scans longer `w2`.
- `cnt` counts characters skipped from `w2`.

If `w1[i] == w2[j]`, both sequences can use that character, so `i` advances. In every iteration `j` advances because the current longer-word character has been consumed either as a match or as the inserted extra character.

If the characters differ, the only legal explanation is that `w2[j]` is the one inserted character. The code increments `cnt` but leaves `i` in place, allowing the next longer-word character to try matching the same shorter-word character.

At the end, `cnt < 2` requires at most one internal mismatch, and `i == len(w1)` requires every character of the shorter word to have matched in order.

**Why an insertion at the end needs no mismatch**

Suppose `w1 = "abc"` and `w2 = "abcd"`. The loop matches `a`, `b`, and `c`. Then `i` reaches the end of `w1` and the loop stops before examining final `d`.

`cnt` remains zero, but the one-character length difference already proves there is exactly one unconsumed longer-word character. The return condition accepts, correctly treating `d` as the insertion.

The same logic handles an insertion at the beginning or middle through one counted mismatch.

**Why character order is preserved**

Pointer `i` never moves backward, and it advances only on equality. The matched positions in `w2` therefore appear in the same order as `w1`.

The helper cannot accept a rearrangement such as `"cba"` leading to `"bcad"`. Once an expected character is passed in `w2`, there is no way to return to it.

**Dynamic-programming transition**

For every current index `i`, the inner loop examines each earlier index `j`. If `words[j]` is a predecessor of `words[i]`, a best chain ending at `j` can append the current word.

The candidate length is `dp[j] + 1`, and:

`dp[i] = max(dp[i], dp[j] + 1)`.

Several predecessors may exist. Keeping the maximum is safe because every future successor cares only about the current final word and the longest chain reaching it, not the identities of earlier words.

`res` tracks the largest `dp[i]` observed. It starts at one because the source guarantees at least one input word. The outer loop starts at index one; index zero's initialized one already represents its only possible chain.

**Trace the first example**

After sorting by length, one-letter words `"a"` and `"b"` come first and each has chain length one.

For `"ba"`, removing the inserted `b` leaves `"a"`, or removing `a` leaves `"b"`. The helper finds valid predecessor relationships, so `dp["ba"]` becomes two.

Word `"bda"` accepts `"ba"` as a predecessor by skipping inserted `d`, producing chain length three.

Word `"bdca"` accepts `"bda"` by skipping inserted `c`, producing four. The result is four.

Other relationships may be considered, but `max` retains the longest route.

**Why sorting only by length is sufficient**

Words of the same length cannot be predecessor and successor because exactly one insertion is required. Their relative order within a length group does not matter.

Every valid predecessor group is one length shorter and therefore entirely before the current word after sorting. No lexical ordering is needed.


If `check` returns true, lengths differ by one, every shorter-word character matched in order, and at most one longer-word character was skipped during matching. The one extra length accounts for exactly one inserted character, including a possible unexamined final character. Thus `w1` is a predecessor.

If `w1` is a predecessor, deleting the inserted character from `w2` leaves `w1` in order. The two-pointer scan matches all other characters and skips only that inserted one, so its return conditions succeed.


Take an optimal chain ending at `words[i]`. If its length is one, initialization is correct. Otherwise, its previous word is a valid predecessor at some earlier sorted index `j`. By induction, `dp[j]` stores the best chain ending there, and the transition considers `dp[j] + 1`.

Every transition also appends a verified predecessor-successor pair, so it creates a valid chain. Therefore, each `dp[i]` and the final maximum `res` are exact.

**Exact implementation versus deletion-map optimization**

The local editorial's faster bottom-up form generates each predecessor by deleting one character and looks it up in a map. The protected solution instead compares every earlier word with every current word using `check`.

The all-pairs form is easy to follow and correct under the small maximum word length, but it has a different asymptotic time bound from the manifest's deletion-map target.

## Complexity detail

Let `W` be the number of words and `L` the maximum word length. Sorting takes `O(W \log W)` comparisons.

The exact nested loops examine `O(W^2)` word pairs. Each `check` scans at most `O(L)` characters after the constant-time length test. Its exact running time is therefore `O(W \log W + W^2L)`.

The `dp` list uses `O(W)` space, and Python sorting may use `O(W)` temporary references. The strings already belong to the input. Thus the exact auxiliary bound is `O(W)`, aside from sort implementation details.

The manifest states `O(W \log W + WL^2)` time and `O(WL)` space, which describes the deletion-generated predecessor map: each of `W` words creates `L` slices costing `O(L)` each. That alternative is outlined below; it is not the pairwise source shown here.

## Alternatives and edge cases

- **Delete-one-character predecessor map:** For each length-sorted word, generate all `L` deletion strings and look up their best chains. This reaches the manifest's `O(W \log W + WL^2)` time and avoids all word pairs.
- **Top-down memoized deletion:** Store all words in a set, recursively delete one character, and memoize the best chain from each word. It has similar deletion-generation complexity.
- **Build an explicit graph:** Add an edge for every predecessor relation and find the longest DAG path. The pairwise DP already performs this implicitly without storing edges.
- **Insertion at the beginning:** The first mismatch is skipped in `w2`, after which matching continues.
- **Insertion in the middle:** Exactly one mismatch is skipped while `i` waits for its character.
- **Insertion at the end:** The loop can finish with zero counted mismatches because the one extra trailing character remains, and the length difference guarantees it.
- **Two mismatches:** `cnt` reaches at least two and the helper rejects, even if lengths differ by one.
- **Reordered characters:** Pointer monotonicity prevents acceptance.
- **Same-length words:** They fail the length check immediately and cannot extend a chain.
- **Single input word:** `res` remains one, the correct trivial chain length.
- **Duplicate words:** Equal strings cannot be predecessor-successor pairs because their lengths are equal; duplicates do not artificially extend a chain.
- **Several predecessors:** `max` chooses the one carrying the longest earlier chain.
- **Input mutation:** Sorting changes the order of `words`. A caller needing original order must sort a copy.
- **Extra DP slot:** The exact array has length `n + 1` although indices zero through `n - 1` are used. The spare entry is harmless.
