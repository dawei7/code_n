## General

**Separate content from spacing**

The required output keeps every word in its original order and redistributes only the spaces. The solution first extracts the two pieces of information that fully determine the result:

- `spaces = text.count(" ")` counts the total number of space characters available;
- `words = text.split()` extracts the words and discards the original runs of whitespace.

Because the input uses ordinary space characters and guarantees at least one word, `split()` without an argument produces exactly the ordered word list. It ignores leading spaces, trailing spaces, and any number of spaces between words. No word letters are lost or reordered.

After this normalization, the original placement of spaces is irrelevant. Only their total count matters.

**How many gaps receive equal spacing**

If there are $W$ words, there are $W-1$ internal gaps between adjacent words. For example, four words have three places where equal separators can be inserted.

The problem asks to maximize the equal number of spaces in every internal gap. If $S$ spaces are available and $W>1$, integer division gives the largest equal separator size:

$$
\text{gap}=\left\lfloor\frac{S}{W-1}\right\rfloor.
$$

The remainder

$$
\text{extra}=S\bmod(W-1)
$$

is the number of spaces that cannot be distributed without making some gap larger than another. Those spaces must appear at the end.

The source computes both quantities at once with:

`cnt, mod = divmod(spaces, len(words) - 1)`.

Python’s `divmod(a, b)` returns the quotient and remainder satisfying `a = quotient * b + remainder` with `0 <= remainder < b`.

**Constructing the result**

`" " * cnt` creates the common separator containing exactly `cnt` spaces. Calling `join(words)` with that separator places it between every adjacent pair of words and nowhere before the first or after the last.

The expression then appends `" " * mod`, placing every leftover space at the end as required:

`(" " * cnt).join(words) + " " * mod`.

This construction preserves the order of the words because `join` traverses `words` in order.

For `text = " practice makes perfect"`, there are seven spaces and three words. Two internal gaps receive `7 // 2 = 3` spaces each, consuming six spaces, and `7 % 2 = 1` space remains. The result is `"practice   makes   perfect "`.

**Why one word needs a separate branch**

When there is only one word, there are zero gaps between words. Dividing by `len(words) - 1` would divide by zero, and there is no valid internal location in which to distribute spaces.

The contract says extra spaces go at the end. Therefore, the source returns:

`words[0] + " " * spaces`.

Every original space becomes trailing whitespace after the sole word. This also handles text that originally had spaces before, after, or on both sides of that word.

The at-least-one-word guarantee means `words[0]` always exists. A string containing only spaces is outside the input contract.

**Why the number of spaces per gap is maximal**

Suppose each of the $W-1$ gaps received more than `cnt` spaces. Each would then receive at least `cnt + 1`, requiring:

$$
(W-1)(\text{cnt}+1)>S
$$

spaces because `cnt` is the floor of $S/(W-1)$. That is impossible. Thus no valid arrangement can use a larger equal gap.

The constructed result uses `cnt` spaces in every gap, so it attains the maximum. The `mod` leftover spaces cannot be added to any internal gap without breaking equality, and appending them is exactly the required fallback.

**Why the output length is unchanged**

Let $C$ be the total number of letters across all words. The input length is $C+S$ because every character is either a lowercase letter or a space.

For multiple words, the output contains:

- the same $C$ word characters;
- `cnt * (W - 1)` separator spaces;
- `mod` trailing spaces.

The defining property of `divmod` gives:

$$
\text{cnt}(W-1)+\text{mod}=S.
$$

Therefore, the output length is also $C+S$. In the one-word case, it directly appends all $S$ spaces, so the same argument holds.

**Why the transformation is correct**

All words are extracted without changing their content or order. For multiple words, every adjacent pair receives exactly the same `cnt` spaces, and the quotient proof shows that count is the maximum possible. Every undistributed space is appended after the final word. For one word, all spaces are necessarily extra and are appended. In either case, the construction uses every original space exactly once and returns a string of the original length.

## Complexity detail

Let $L$ be the length of `text`.

`text.count(" ")` scans the string in $O(L)$ time. `text.split()` also scans the string and creates word strings whose total character count is at most $L$. Joining the words and creating trailing spaces produces an output of exactly length $L$, taking another $O(L)$ time. The total time complexity is $O(L)$.

The word list, extracted word strings, separator construction, and returned string collectively require $O(L)$ space. Ignoring the required output, the parsing structures are still $O(L)$ in the checked-in Python implementation. Thus the stated space complexity is $O(L)$.

## Alternatives and edge cases

- **Manual character scan:** One can count spaces and build words with an explicit loop. It has the same $O(L)$ complexity but duplicates behavior already provided clearly by `count` and `split`.
- **Repeated string insertion:** Inserting spaces into an existing immutable Python string can repeatedly copy prefixes and become quadratic. Constructing once with `join` is linear.
- **Preserve original space runs:** Their positions do not matter; only the total space count is relevant. Keeping each run complicates redistribution without adding information.
- **Exactly one word:** There are no internal gaps, so all spaces are placed after the word and division by zero is avoided.
- **Exactly two words:** There is one gap, so every space divides evenly into that gap and no trailing remainder exists.
- **No spaces:** `cnt` and `mod` are zero. `join` places empty separators, which is valid only when the input’s word-separation guarantees allow the corresponding number of words; in practice, no spaces implies one word.
- **Spaces divide evenly:** `mod == 0`, so the result has no extra trailing spaces.
- **Nonzero remainder:** Every gap still has the equal maximum quotient, and only the remainder appears at the end.
- **Leading and trailing input spaces:** `split()` removes their original positions, while `count` preserves their quantity for redistribution.
- **Several spaces between words:** They are collapsed during extraction and reallocated through the quotient and remainder.
- **Maximum length preservation:** The quotient-remainder identity proves no space is lost or invented.
- **At-least-one-word guarantee:** The source assumes `words` is non-empty. An all-space string would need separate behavior but is outside the contract.
