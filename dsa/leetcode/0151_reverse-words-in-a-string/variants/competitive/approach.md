## General

**Let three built-ins express the complete transformation**

The competitive source is one expression:

`' '.join(reversed(s.split()))`

Each operation has a distinct role:

1. `split()` discovers words and removes irregular whitespace;
2. `reversed(...)` presents those words from last to first;
3. `' '.join(...)` creates normalized output spacing.

The compactness does not hide a different algorithm. It is still parse words, reverse their order, and rebuild the sentence.

**How default `split()` handles spacing**

Calling `s.split()` without a separator is different from calling `s.split(" ")`.

The no-argument form treats runs of whitespace as one boundary and suppresses empty fields. Under this problem’s alphabet, the only possible whitespace is the literal space character, so its behavior is:

- ignore leading spaces;
- separate words across one or more spaces;
- ignore trailing spaces.

For `"  hello world  "`, the result is `["hello", "world"]`.

By contrast, `s.split(" ")` would produce empty strings around repeated separators, requiring additional filtering. The selected no-argument call is intentional.

The allowed words may contain uppercase or lowercase letters and digits. None is whitespace, so each stays intact.

**Why `reversed` changes only word order**

`reversed` receives the list of complete word strings. It returns an iterator that yields list elements from the final index down to zero.

It does not reverse characters inside a word. `"hello"` remains `"hello"`; only its position among other words changes.

The iterator is lazy and does not itself allocate a second word list. `join` consumes it directly.

For `"the sky is blue"`, split produces four words, and the iterator yields `"blue"`, `"is"`, `"sky"`, and `"the"`.

**Why joining guarantees exact output separators**

`' '.join(...)` inserts its one-character separator between consecutive yielded words. It does not prepend or append the separator.

Therefore:

- adjacent output words have exactly one space;
- the output has no leading space;
- the output has no trailing space.

Since the split stage contains no empty strings, joining cannot create extra spaces from empty fields.

**Why all and only input words are returned**

Default splitting partitions the input at each maximal whitespace run and yields every maximal non-whitespace run. Those runs are exactly the Reference’s words.

Reversal is a one-to-one permutation: no element is added, removed, or changed. Joining adds formatting characters but leaves every word’s content unchanged.

Thus the final string contains precisely the original words in reverse order with normalized boundaries.

**The follow-up and Python immutability**

The follow-up asks about constant extra space when the language’s string type is mutable. Python strings are immutable, and `split` necessarily creates word strings and a list.

This solution is appropriate to the Python interface but does not satisfy the hypothetical mutable-buffer in-place follow-up. A lower-level language could reverse and compact a character array directly.

The source does not mutate `s`; it returns a newly constructed string.

This pipeline also preserves exact word spelling. Neither `split`, `reversed`, nor `join` changes capitalization, digit order, or characters inside a token. Only boundary spaces disappear and new single separators appear. That distinction matters: the task asks to reverse the sequence of words, not to reverse the complete character sequence.

## Complexity detail

Let $n$ be the input length and $w$ the number of words.

`split` scans $n$ characters and creates word data totaling $O(n)$. `reversed` creates an $O(1)$ iterator. `join` reads all $w$ words and writes the final $O(n)$-character string. Total time is $O(n)$.

The word list and substrings produced by `split` use $O(n)$ space. The returned string also uses $O(n)$. The reversed iterator itself is constant size. Overall additional storage is $O(n)$, matching the manifest.

No repeated string concatenation occurs, so there is no hidden quadratic copying behavior.

## Alternatives and edge cases

- **Manual two-pointer scan:** Explicitly skip spaces and collect maximal word slices. It exposes every parsing boundary while retaining $O(n)$ time and space.
- **Deque with `appendleft`:** Build words left-to-right but store them in reverse order. It uses linear memory and can avoid a separate reversal view.
- **Mutable-buffer reversal:** Collapse spaces, reverse the full character buffer, and reverse each word. It can achieve constant auxiliary space in languages with mutable strings.
- **Use `split(" ")`:** This requires filtering empty tokens and is less suitable for multiple spaces than the selected default split.
- **One word:** Reversal yields the same sole element, while split removes surrounding spaces.
- **Multiple middle spaces:** Default split collapses the entire run into one logical boundary.
- **Leading/trailing spaces:** Empty fields are suppressed, so join cannot reproduce them.
- **Digits and mixed case:** They remain ordinary word characters and preserve exact spelling.
- **All-space input outside the contract:** Split yields an empty list and join returns `""`; the Reference guarantees at least one word.
- **Other whitespace outside the contract:** Default split would also treat tabs and newlines as separators, which is broader but harmless for the allowed domain.
- **Library-use interviews:** The expression is correct and efficient, but an interviewer asking for parsing mechanics or in-place mutation may expect the manual or mutable-buffer approach.
