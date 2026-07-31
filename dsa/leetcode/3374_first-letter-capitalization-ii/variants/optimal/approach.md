## General

Ordinary words are delimited by spaces: uppercase the token's literal first character and lowercase everything after it. Case functions leave punctuation unchanged, which matters for a token such as `/abc`: applying `UPPER` to `/` must not postpone capitalization until `a`.

A hyphen receives special treatment only when the complete whitespace-delimited token matches two nonempty alphabetic parts joined by exactly one hyphen. Thus `quick-brown` becomes `Quick-Brown`, while `foo--bar`, `-baz`, `end-`, and `dar-@daz` follow the ordinary rule and do not capitalize a later segment.

The accepted MySQL query walks each source string character by character with a recursive CTE. Its state stores the current position, the beginning of the current whitespace token, and the converted prefix. The current character is uppercased at the token start. It is also uppercased after a hyphen only when the whole current token satisfies `^[A-Za-z]+-[A-Za-z]+$`; every other character is lowercased. When a space is copied, the next position becomes the new token start.

Because every transition appends exactly the current source character, no formatting can move or disappear. The boundary rule normalizes every ordinary token, and the whole-token validation proves that a second capital is introduced exactly for valid two-part hyphenated words. The final state therefore contains the required conversion. The app-local SQLite query expresses the same rule by identifying whitespace token ranges before normalizing and rejoining them with their original number of spaces.

## Complexity detail

Let $n$ be the row count, $S$ the total number of characters, and $L$ the longest whitespace token. The recursive scan emits one state per character. Testing a hyphen may scan its containing token, costing at most $O(L)$, so the conservative bound is $O(SL)$ for conversion; ordering completed rows adds $O(n\log n)$. Recursive state and the result occupy $O(S+n)$ space.

The benchmark defines `size` as $n$ and keeps every source string at the same fixed length, so $S=\Theta(n)$ and $L=O(1)$. The accepted-class query scales with the input rows plus their final ordering. A correct baseline that performs a correlated identifier-prefix scan for each output row adds quadratic growth and must fail the scaling verdict while retaining identical results.

## Alternatives and edge cases

- **Split on spaces and join normally:** A tokenizer that discards empty tokens collapses leading, trailing, or repeated spaces and violates the formatting contract.
- **Capitalize after every hyphen:** It mishandles leading, trailing, repeated, multi-hyphen, and symbol-adjacent patterns.
- **Defer capitalization past punctuation:** `/abc` must become `/abc`, not `/Abc`; the first token character is the capitalization position even when it is not a letter.
- **Lowercase the whole string first:** This is useful preparation but does not identify ordinary word starts or the second part of a valid hyphenated token.
- **Fixed word-count expressions:** They fail when a row contains more tokens than the query anticipates.
- **Repeated spaces:** Empty tokens between spaces are preserved, and the first character after the final space still begins a word.
- **Valid hyphenated word:** Require exactly one hyphen and alphabetic, nonempty text on both sides before capitalizing both parts.
- **Malformed hyphens:** `foo--bar -baz lOO-daR-@Daz-` becomes `Foo--bar -baz Loo-dar-@daz-`.
- **Other punctuation:** Backslash, `@`, `/`, `^`, and comma remain fixed and do not create new word boundaries.
- **Output ordering:** Sort by the unique `content_id` so insertion order cannot affect the result.
