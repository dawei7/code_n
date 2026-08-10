## General

**Formation depends on character multiplicities**

A word is good when `chars` supplies enough copies of every letter required by that word. Order is irrelevant: the available letters may be rearranged. What matters is frequency.

For example, one `t` in `chars` is not enough for a word containing two `t` characters, even if every other needed letter exists. A simple membership set would lose that multiplicity information, so the solution uses counters.

`cnt = Counter(chars)` maps each available lowercase letter to its number of copies. This counter is built once because the available inventory is the same for every word.

**Build the requirement counter for one word**

For each word `w`, `wc = Counter(w)` records how many copies of each letter that word requires. The word is formable exactly when

`cnt[c] >= wc[c]`

for every character appearing in `w`.

The generator `cnt[c] >= v for c, v in wc.items()` produces one Boolean condition per distinct required character. `all(...)` returns true only when every requirement is satisfied.

Counter lookup returns zero for a missing key, so a letter absent from `chars` automatically fails a positive requirement. No separate membership check is needed.

**Each word receives a fresh conceptual inventory**

The phrase “each character can only be used once for each word” does not mean that letters consumed for one good word are unavailable to later words. Every word is tested independently against the original `chars`.

That is why the code never decrements `cnt`. It compares a temporary requirement counter to the unchanged inventory. If `"cat"` and `"hat"` are both individually formable, both lengths contribute even though their tests reuse the same available `a` and `t`.

Mutating one shared counter across the outer loop would answer a different problem about forming a collection of words simultaneously.

**Add only complete words**

When all frequency inequalities pass, the whole word can be assembled, so `len(w)` is added to `ans`. If even one required character is short, the word is not good and contributes nothing.

Partial formation has no value. A word requiring three copies of a letter when only two are available cannot contribute its formable prefix or a reduced length.

The use of `all` may stop as soon as one failing requirement is found. This can save work for impossible words, though the worst-case analysis still accounts for checking all distinct letters.

**Trace the first example**

For `chars = "atach"`, the inventory contains two `a` characters and one each of `t`, `c`, and `h`.

The word `"cat"` requires one of each `c`, `a`, and `t`, so all comparisons pass and length three is added.

`"bt"` requires `b`, whose available count is zero, so it fails.

`"hat"` requires one `h`, one `a`, and one `t`, so it also contributes three.

`"tree"` requires letters not supplied in sufficient counts and contributes zero. The accumulated result is six.

**Why the algorithm is correct**

If the test accepts a word, the available count of every required character is at least the required count. Assigning those copies by character constructs the word, so every accepted word is good.

If the test rejects a word, some character `c` is required more times than `chars` contains. Since each available character copy may be used at most once for that word, no rearrangement can supply the missing occurrence. The rejected word is not good.

Thus the condition accepts exactly the good words. Adding their lengths and only their lengths gives the required sum.

The lowercase-alphabet guarantee makes counters small, but the reasoning does not depend on any particular letter distribution or word order.

## Complexity detail

Define

`S = len(chars) + sum(len(w) for w in words)`.

Building `cnt` takes `O(len(chars))` time. Building `wc` for a word takes `O(len(w))` time. Iterating its distinct entries takes at most 26 operations and also no more than a constant multiple of its length. Summed across all words, total time is `O(S)`.

Both counters contain at most 26 keys because all input consists of lowercase English letters. Their size is independent of `S`, so auxiliary space is `O(1)` under the fixed-alphabet contract.

The temporary counter for one word is released or replaced before processing the next word; counters for all words are not stored together.

## Alternatives and edge cases

- **Use a 26-element integer array:** Converting letters to offsets gives the same `O(S)` time and constant space with lower hashing overhead. `Counter` expresses frequency intent more directly.
- **Sort every word and `chars`:** Sorted comparisons can test supply but add logarithmic sorting work and repeated processing of the same inventory.
- **Use sets:** A set records only presence and incorrectly accepts words that require more copies than available.
- **Decrement the shared inventory:** That prevents later words from reusing characters, contrary to the independent-per-word rule.
- **A repeated required letter:** Its full multiplicity must fit in `cnt`; one available copy cannot serve multiple positions.
- **A character absent from `chars`:** Counter lookup yields zero, so the word fails immediately when that requirement is checked.
- **Duplicate words in the input:** Each array entry is evaluated and contributes its length independently if good.
- **Empty contribution set:** If no word is good, `ans` remains zero.
- **A word shorter than `chars`:** Length alone does not guarantee formation; its exact character counts still matter.
- **A word equal to `chars` up to permutation:** All counts match and its complete length is included.
- **Lowercase alphabet:** This bound is what makes the counter storage asymptotically constant.
