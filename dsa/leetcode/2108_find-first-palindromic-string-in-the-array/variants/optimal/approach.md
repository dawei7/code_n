## General

**Preserve array order and stop at the first match**

The word “first” makes the input order essential. The source creates a generator that examines `words` from left to right:

`(w for w in words if w == w[::-1])`.

It yields only words that equal their reversed form. `next(..., "")` requests the first yielded word and uses the empty string as a default if the generator yields nothing.

Because `next` is lazy, later words are not checked after the first palindrome is found. This is important in an example containing both `"ada"` and the later `"racecar"`: the method returns `"ada"` immediately.

**Why reversal tests palindromicity**

`w[::-1]` is Python slicing with a step of -1, producing the characters of `w` in reverse order.

A string is palindromic exactly when its forward sequence equals its backward sequence. Therefore,

`w == w[::-1]`

is true if and only if `w` is a palindrome.

Odd-length strings naturally compare the center character with itself. Even-length strings have no unique center, but complete reversal still compares every mirrored pair. One-character strings always pass.

**Understand the generator and default**

The parenthesized expression is a generator, not a precomputed list. It requests one word, constructs and compares that word's reverse, then proceeds only if necessary.

`next(generator, "")` has two outcomes:

- if a palindromic word is yielded, return that original word;
- if the generator is exhausted, return `""`.

The returned value is `w` from the input, not the reversed copy. For a palindrome they have equal text, but returning the original makes the intent explicit.

The constraints say input words are nonempty, so the default empty string cannot be confused with a valid palindromic input word.

**Trace the evaluation order**

For `["abc", "car", "ada", "racecar", "cool"]`:

- `"abc"` is compared with `"cba"` and rejected;
- `"car"` is compared with `"rac"` and rejected;
- `"ada"` is compared with `"ada"` and yielded;
- `next` returns it, so `"racecar"` and `"cool"` are never examined.

For `["def", "ghi"]`, both comparisons fail. Exhaustion activates the default empty string.

**Why the result is correct**

Every word before the returned one was tested and failed equality with its reverse, so none is palindromic. The returned word passed the exact palindrome definition, making it the first valid word.

If the method returns the default, every word was examined and failed, so no palindrome exists. These cases cover the entire contract.

**Be precise about the implementation's memory**

The branch manifest summary says mirrored character pairs are checked without constructing a reversed copy and lists $O(1)$ space. That description fits a two-pointer character comparison, but the exact solution uses `w[::-1]`.

In Python, slicing creates a new reversed string proportional to `len(w)`. The generator avoids storing reverses for multiple words simultaneously, but one reversed copy exists for each active check. Documentation should reflect this exact behavior.

**Why early stopping is not merely an optimization**

The order requirement means the method should commit as soon as the first valid word is known. Continuing to scan would not change the answer, but it would obscure the proof: at the return point, all earlier words are known failures and the current word is known valid.

The generator-plus-`next` combination encodes this selection rule directly. It does not first compute all palindromes and then choose index zero from a separate list. That saves work when a palindrome occurs early and keeps the returned object tied to its original array occurrence.

**Character comparisons performed by equality**

After the reverse is built, Python string equality compares lengths and characters until it proves equality or finds a mismatch. Since the reverse has the same length by construction, the meaningful work is comparing corresponding forward and reversed positions.

Even though the source does not write explicit left and right pointers, the equality test is logically checking the same mirrored relationships. The difference is material only for allocation and possible early mismatch behavior: the reversed copy must be constructed before equality can reject the word.

## Complexity detail

Let

$$
S=\sum_{w\in\texttt{words}}\lvert w\rvert
$$

over the words examined through the first palindrome, or all words if none exists. Let $L$ be the maximum length of an examined word.

Constructing and comparing one reverse costs $O(\lvert w\rvert)$ time. Total time is $O(S)$, bounded by the total input characters.

The reversed slice for one word uses $O(\lvert w\rvert)$ space, so peak auxiliary space is $O(L)$, not the manifest's $O(1)$ for this exact source. The generator itself uses constant iteration state.

A two-pointer test could achieve $O(1)$ auxiliary space without changing the overall $O(S)$ time.

## Alternatives and edge cases

- **Two mirrored pointers:** Compare characters at the two ends while moving inward. This realizes the manifest's constant-space claim and can stop a word check at its first mismatch.
- **Build a list of all palindromes:** It does unnecessary work and storage after the first match. The lazy generator stops immediately.
- **Sort the words:** This destroys the input-order meaning of “first” and is incorrect.
- **First word is palindromic:** Only one word is examined.
- **No palindrome:** Generator exhaustion returns the explicit empty-string default.
- **One-character word:** It equals its reverse and is always palindromic.
- **Even-length palindrome:** Complete reversal handles it without a special center case.
- **Repeated words:** The earliest palindromic occurrence is returned.
- **Nonempty word guarantee:** It keeps `""` reserved for the no-result case.
- **Reversed-copy allocation:** `w[::-1]` is concise but not constant-space.
- **Input preservation:** Strings and the array are only read.
- **Lazy evaluation:** Words after the first palindrome incur no time or reverse allocation.
- **Long non-palindromic word:** Its full reverse is still allocated before equality can reject it, which is why peak space depends on word length.
- **Return identity versus text:** The generator yields the original `w` value from `words`, not the temporary reverse.
