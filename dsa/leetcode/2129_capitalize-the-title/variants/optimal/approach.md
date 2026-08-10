## General

The title is already divided into non-empty words separated by single spaces. Each word can therefore be transformed independently: its required capitalization depends only on its own length, and changing it cannot affect the rule for any neighboring word.

**Separate the title into exactly the units governed by the rule**

The expression `title.split()` produces the sequence of words. Because it is called without an explicit separator, Python treats whitespace as the separator and omits empty pieces. The problem guarantees one space between words and no leading or trailing spaces, so this behavior gives precisely the stated words. The implementation does not need indexes for the spaces because it reconstructs the separators after transforming the words.

The list comprehension visits each word `w` once:

`[w.lower() if len(w) < 3 else w.capitalize() for w in title.split()]`

The condition `len(w) < 3` is exactly another way to say that the word contains one or two letters. There is no overlap or missing case: positive word lengths below three use the short-word rule, and lengths of at least three use the other rule.

**Normalize short words completely**

For a word of length one or two, `w.lower()` converts every uppercase English letter to its lowercase form and leaves an already lowercase letter unchanged. This directly implements the requirement that every letter of a short word be lowercase.

It is important to normalize the entire word rather than merely lowercasing its first character. An input such as `"OF"` must become `"of"`, not `"oF"`. Calling `lower()` expresses this complete transformation in one operation.

**Normalize longer words in both directions**

For a word of at least three letters, `w.capitalize()` makes its first character uppercase and the remaining characters lowercase. Both parts matter. Merely uppercasing the first letter would mishandle mixed-case input such as `"capiTalIze"` because the internal uppercase `T` and `I` would remain. `capitalize()` first establishes the requested leading capital and normalizes the rest, producing `"Capitalize"`.

The input contains only English letters, so there are no punctuation marks, digits, or unusual word-boundary cases to reinterpret. Each source word is non-empty, which also guarantees that there is always a first letter when the long-word branch is selected.

The transformed results are stored in `words`. At this point, an invariant holds for every element already produced: if its original length was below three, all its letters are lowercase; otherwise, its first letter is uppercase and every later letter is lowercase. Since the transformation does not change a word’s length, the branch choice remains valid after capitalization.

**Restore the title**

The expression `" ".join(words)` places one ordinary space between each pair of neighboring transformed words. It adds no leading or trailing space. This reconstructs the format promised by the problem while preserving word order.

Consider `"First leTTeR of EACH Word"`. Splitting produces five words. `"First"`, `"leTTeR"`, `"EACH"`, and `"Word"` have at least three letters, so `capitalize()` yields `"First"`, `"Letter"`, `"Each"`, and `"Word"`. The two-letter word `"of"` goes through `lower()` and remains `"of"`. Joining them yields `"First Letter of Each Word"`.

The correctness follows directly from the independent per-word rule. Every input word is placed into exactly one of the two exhaustive length categories. The selected string operation produces precisely the capitalization required for that category. Joining changes only the separators, not the transformed words or their order. Therefore every word in the returned title satisfies its rule, and the returned text is the required capitalized title.

**Why no extra state machine is needed**

A character-by-character solution could track whether the current character begins a word, how long that word is, and whether later characters must be lowered. That is unnecessary here because the single-space guarantee makes word extraction reliable, and Python’s string methods already perform the two complete word transformations. The exact solution stays close to the specification: split, choose by length, normalize, and join.

## Complexity detail

Let $n$ be the number of characters in `title`, including its spaces. Splitting scans the title and creates word strings whose combined number of letters is at most $n$. For each word, `lower()` or `capitalize()` scans and creates a result proportional to that word’s length. Joining scans the transformed words and writes the final $n$-character result. These are consecutive linear passes, so their costs add rather than multiply. The total time is $O(n)$.

The output string itself has length $n$. In addition, `split()` creates a list of input-word strings, and the comprehension creates the `words` list containing transformed strings. Their combined character content and references are linear in the title length. Thus the exact implementation uses $O(n)$ auxiliary construction space and produces an $O(n)$ return value. Python strings are immutable, so the solution cannot rewrite `title` in place.

The length check is $O(1)$ per word because Python strings store their length. The calls to `lower()` and `capitalize()` are not constant-time shortcuts; they must visit the letters they normalize, which is already included in the aggregate $O(n)$ bound.

## Alternatives and edge cases

- **Manual character scan:** One can locate each word boundary, measure the word, and append transformed characters to a buffer. This is also $O(n)$ time and $O(n)$ output space, but requires more indexing logic and creates more opportunities for off-by-one errors.
- **Lowercase the entire title first:** After `title.lower()`, the first character of every word of length at least three could be uppercased. This is correct with careful boundary and length tracking, but it still needs a second pass and does not simplify the exact split-and-transform solution.
- **Using `title.title()`:** This capitalizes every word regardless of length, so it incorrectly turns short words such as `"of"` and `"i"` into `"Of"` and `"I"`.
- **Uppercasing only the first character:** This fails to lowercase the remaining letters of a long mixed-case word. The `"capiTalIze"` example demonstrates why full normalization is required.
- **One-letter word:** Its length is below three, so `lower()` is selected. An uppercase `"I"` becomes `"i"` as required.
- **Two-letter word:** The strict comparison `len(w) < 3` includes length two. Both letters become lowercase, even when both were originally uppercase.
- **Exactly three letters:** Length three enters the `capitalize()` branch. This boundary is important because the short-word rule applies only to lengths one and two.
- **Already normalized title:** Applying `lower()` or `capitalize()` again leaves every word in the same required form, so the method is idempotent.
- **Mixed original casing:** Each selected string method rewrites all relevant letters, making the result independent of the input’s prior capitalization.
- **One-word title:** `split()` returns a one-element list and `join()` returns that transformed element without adding spaces.
- **Maximum-length title:** The same linear passes apply when the title has length 100; there is no combinatorial behavior or nested scan over all words.
- **Whitespace semantics:** Python’s no-argument `split()` would also collapse repeated whitespace, but the contract guarantees exactly one space and no leading or trailing spaces. The implementation’s output therefore preserves the required separator format for every legal input.
- **Input immutability:** Neither string methods nor `join()` modify `title`; each creates a new string, which matches Python’s immutable string model.
