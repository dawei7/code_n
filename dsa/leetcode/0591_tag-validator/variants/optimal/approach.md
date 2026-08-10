## General

Nested tags have a last-opened, first-closed rule. If `<A>` contains `<B>`, then `</B>` must appear before `</A>`. A stack represents this perfectly: push each start-tag name, and require each end tag to match and pop the current top.

The parser scans left to right with index `i` and distinguishes four kinds of input:

- ordinary content characters;
- an opening tag beginning with `<`;
- a closing tag beginning with `</`;
- a CDATA section beginning with the exact prefix `<![CDATA[`.

Whenever one construct is recognized, the index jumps to its delimiter so characters inside it are not parsed a second time.

**Validating tag names**

The helper `check(tag)` requires length from 1 through 9 and requires every character to satisfy `isupper()`. Under the stated input alphabet, this is equivalent to allowing only uppercase English letters: digits, lowercase letters, punctuation, and the empty string fail.

This validation is applied to both opening and closing names. Finding a `>` is not enough; `<TOO_LONG_NAME>`, `<a>`, and `<>` must all be rejected.

**The outer-wrapper invariant**

At the start of every iteration, the source checks:

```python
if i and not stk:
    return False
```

Once scanning has moved beyond position zero, an empty stack means the one outer root tag has already closed—or no root was opened—and more input remains. Rejecting at that moment prevents text after the root and prevents a second top-level tag.

For valid `<A></A>`, popping `A` happens at the end of the string, so the loop terminates before the invariant is checked again. For `<A></A>x`, another iteration begins with a nonzero index and empty stack, so trailing `x` is rejected.

This is intended to enforce that all content stays inside one root. However, the exact condition has a gap at index zero, discussed below: it does not explicitly record that a root start tag was ever opened.

**CDATA must be recognized before generic tags**

The first syntax branch tests the exact nine-character prefix `<![CDATA[`. Once recognized, `find(']]>', i + 9)` locates the first subsequent terminator. If none exists, the code is invalid.

The index then jumps across the closing `]]>`. Everything between the prefix and that first terminator is ignored by the parser. It may contain lowercase tags, unmatched angle brackets, or text resembling another CDATA opener; those are plain CDATA content.

This branch must come before generic `<...>` parsing. Otherwise, the parser would interpret `![CDATA[` as a tag name and reject valid CDATA.

Inside an already-open tag, CDATA handling is correct. A malformed `<!...` that lacks the exact prefix falls through to opening-tag parsing, obtains an invalid name containing punctuation, and is rejected.

**Closing tags**

For `</`, the parser searches for the next `>`. Missing `>` is immediately invalid. The substring between `</` and `>` is the closing name `t`.

The combined condition rejects the construct if:

- `t` is not a valid name;
- the stack is empty, so there is no unmatched opener;
- the top name popped from the stack differs from `t`.

The order check catches crossed nesting. For `<A><B></A></B>`, the first closer says `A` while the stack top is `B`, so validation fails at once.

**Opening tags and ordinary text**

A remaining `<` begins an opening tag. The parser finds the next `>`, extracts and validates its name, then pushes it. Any unmatched `<` causes `find` to return -1 and is rejected.

If the current character starts none of these constructs, it is treated as ordinary content and `i` advances by one. Ordinary `>` characters are permitted; the strict parsing rule is triggered by `<`.

At the end, `return not stk` requires every opener to have been popped. Thus, an unclosed `<A>` fails.

**Why the stack logic is correct once a root exists**

At any scan position inside a properly opened root, the stack lists exactly the currently open tag names from outermost at the bottom to innermost at the top. An opening tag preserves the invariant by pushing its valid name. Ordinary text and CDATA change no nesting. A closing tag preserves it only when it matches the top, then pops. Any mismatch is exactly an unbalanced nesting error.

If scanning ends with an empty stack, every opened tag has a correctly ordered closer. If the stack becomes empty before the end, the next-iteration guard rejects content outside the root. Therefore, given that a valid root was opened at position zero, the main stack invariant validates nesting, tag names, delimiters, CDATA, and trailing content.

**Exact-source root-presence defect**

The source returns only `not stk` at the end; it has no `seen_root` flag and no initial check that the first construct is an opening tag. Because `if i and not stk` is disabled at `i = 0`, two invalid forms can be accepted:

- a one-character ordinary string such as `"a"` advances from zero to the end and returns true;
- a standalone `"<![CDATA[x]]>"` is consumed at position zero and returns true.

Both violate the rule that the whole code must be wrapped in a valid closed tag. This is a correctness gap in the exact protected solution, not merely an alternative interpretation. A correct implementation must require a root opening tag—commonly by checking the first token or tracking whether any start tag was seen—and must allow CDATA only while the stack is nonempty.

## Complexity detail

Let $n$ be the code length. The main index only moves forward. Each delimiter search scans from the current construct to its closing delimiter, and the parser then jumps past that construct; tag-name checks cover disjoint extracted names. Under this forward-scan accounting, total time is $O(n)$.

The stack stores at most one name per nested open tag. Each tag needs at least three characters such as `<A>`, so nesting depth is $O(n)$ and stack space is $O(n)$. Temporary slices for names and the fixed-size CDATA-prefix slice also fit within $O(n)$ total live space. This matches the manifest.

Python’s `str.find` is implemented internally, but each call here searches a region that the outer scan then skips rather than restarting from the beginning.

## Alternatives and edge cases

- **Add `seen_root`:** Set it on the first valid opening tag, reject CDATA or text while the stack is empty, and return `seen_root and not stk`. This repairs the exact source’s root-presence defect.
- **Require `code[0] == '<'` plus an opener parse:** An explicit initial-root check can also prevent standalone text and CDATA, provided it distinguishes `<TAG>` from `</TAG>` and `<![CDATA[`.
- **Recursive-descent parser:** Parse one closed tag and recursively parse nested content. It can closely match the grammar but must still special-case CDATA and depth limits.
- **Regular expressions alone:** Backreferences and arbitrary nesting make a single regex fragile or expensive. A stack expresses nesting more reliably.
- **Crossed tags:** `<A><B></A></B>` fails because the closer does not match the stack top.
- **Unclosed opener:** A nonempty stack at end fails.
- **Closer without opener:** An empty stack in the closing branch fails.
- **Second root tag:** Once the first root closes, the next loop sees an empty stack at nonzero index and fails.
- **Trailing text:** Rejected for the same reason after root closure.
- **Standalone CDATA:** The contract says invalid, but the exact source incorrectly accepts it at index zero; require nonempty stack.
- **One-character plain text:** Also incorrectly accepted by the exact source; require a seen root.
- **First CDATA terminator:** `find(']]>')` intentionally ends CDATA at the first subsequent terminator, leaving later characters to normal parsing.
- **Tag-like text inside CDATA:** Ignored completely, even if malformed.
- **Invalid CDATA prefix:** Falls into tag-name validation and fails because punctuation is not uppercase letters.
- **Unmatched `<`:** Missing subsequent `>` makes `find` return -1 and fails.
- **Ordinary `>`:** Allowed as text because only `<` starts special syntax.
- **Name length:** Empty and ten-character names fail; lengths one through nine pass only with uppercase letters.
- **Unicode nuance:** `isupper()` recognizes more than ASCII in general, but the input alphabet is restricted to English letters and listed symbols, so this does not expand accepted test characters.
